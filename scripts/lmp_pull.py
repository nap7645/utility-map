#!/usr/bin/env python3
"""Day-ahead hourly LMP pull + summary (Rank 1 layer 2). See plans/LMP_NOTES.md.

Usage: python3 scripts/lmp_pull.py [--year 2025] [--markets NYISO,ISO-NE,...] [--summary-only]

Raw pulls are filtered to target settlement points and cached per day/month/year as
data/lmp_cache/<market>/*.csv.gz (columns: zone, ts_utc, price; ts_utc = hour START, UTC).
Cache is gitignored; re-running skips cached files. Output: data/processed/lmp_summary.csv.
Direct public downloads (gridstatus' NYISO path uses http:// which the sandbox proxy
blocks; its ERCOT path works but is one file/yr, so direct URLs are used throughout).
PJM needs a Data Miner 2 API key (PJM_API_KEY env); without it PJM is skipped and logged.
"""
import argparse, calendar, csv, io, os, sys, time, zipfile, datetime as dt
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import pandas as pd
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "data", "lmp_cache")
OUT = os.path.join(ROOT, "data", "processed", "lmp_summary.csv")
LOG = os.path.join(CACHE, "pull.log")
S = requests.Session()
S.headers["User-Agent"] = "utility-map-lmp-pull/1.0 (research)"

TZ = {"NYISO": "America/New_York", "ISO-NE": "America/New_York", "MISO": "America/New_York",
      "ERCOT": "America/Chicago", "CAISO": "America/Los_Angeles", "SPP": "America/Chicago",
      "PJM": "America/New_York"}
NY_LETTER = {"WEST": "A", "GENESE": "B", "CENTRL": "C", "NORTH": "D", "MHK VL": "E", "CAPITL": "F",
             "HUD VL": "G", "MILLWD": "H", "DUNWOD": "I", "N.Y.C.": "J", "LONGIL": "K"}
CAISO_NODES = ["DLAP_PGAE-APND", "DLAP_SCE-APND", "DLAP_SDGE-APND", "DLAP_VEA-APND"]
SPP_LOCS = ["SPPNORTH_HUB", "SPPSOUTH_HUB"]
SRC = {
    "NYISO": "https://mis.nyiso.com/public/csv/damlbmp/YYYYMM01damlbmp_zone_csv.zip (public CSV, zonal DA LBMP)",
    "ISO-NE": "https://www.iso-ne.com/histRpts/da-lmp/WW_DALMP_ISO_YYYYMMDD.csv (public DA hourly LMP, LOAD ZONE + .H.INTERNAL_HUB rows)",
    "MISO": "https://docs.misoenergy.org/marketreports/YYYYMMDD_da_expost_lmp.csv (public DA ex-post LMP, Hub rows; zonal LMP not in this file)",
    "ERCOT": "https://www.ercot.com/mp/data-products/data-product-details?id=NP4-180-ER (Historical DAM Load Zone and Hub Prices, via gridstatus.Ercot.get_dam_spp)",
    "CAISO": "https://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&market_run_id=DAM (OASIS, DLAP nodes)",
    "SPP": "https://portal.spp.org/file-browser-api/download/da-lmp-by-settlement-location (public DA LMP by settlement location, hubs)",
    "PJM": "https://api.pjm.com/api/v1/da_hrl_lmps (Data Miner 2; API key required)",
}


def log(msg):
    os.makedirs(CACHE, exist_ok=True)
    line = f"{dt.datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def get(url, tries=4, **kw):
    for i in range(tries):
        try:
            r = S.get(url, timeout=120, **kw)
            if r.status_code == 200:
                return r
            if r.status_code in (404, 403):
                return None
        except requests.RequestException:
            pass
        time.sleep(2 * (i + 1))
    return None


def cpath(mkt, name):
    return os.path.join(CACHE, mkt, name + ".csv.gz")


def save(mkt, name, df):
    os.makedirs(os.path.join(CACHE, mkt), exist_ok=True)
    df.to_csv(cpath(mkt, name), index=False, compression="gzip")


def utc(naive_local, tz, ambiguous="infer"):
    return naive_local.dt.tz_localize(tz, ambiguous=ambiguous).dt.tz_convert("UTC").dt.strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------- per-ISO fetchers (each returns DataFrame[zone, ts_utc, price] or None) ----------------
def f_nyiso(month):
    y, m = month
    r = get(f"https://mis.nyiso.com/public/csv/damlbmp/{y}{m:02d}01damlbmp_zone_csv.zip")
    if r is None:
        return None
    z = zipfile.ZipFile(io.BytesIO(r.content))
    d = pd.concat([pd.read_csv(z.open(n)) for n in sorted(z.namelist())])
    d = d.rename(columns={"Time Stamp": "t", "Name": "zone", "LBMP ($/MWHr)": "price"})
    d["t"] = pd.to_datetime(d["t"], format="%m/%d/%Y %H:%M")
    out = []
    for zone, g in d.groupby("zone"):
        g = g.sort_values("t", kind="stable").reset_index(drop=True)
        g["ts_utc"] = utc(g["t"], TZ["NYISO"], ambiguous="infer")
        out.append(g)
    d = pd.concat(out)
    d["zone"] = d["zone"].map(lambda z: f"{NY_LETTER[z]} ({z})" if z in NY_LETTER else None)
    return d.dropna(subset=["zone"])[["zone", "ts_utc", "price"]]


def f_isone(day):
    r = get(f"https://www.iso-ne.com/histRpts/da-lmp/WW_DALMP_ISO_{day:%Y%m%d}.csv")
    if r is None:
        return None
    rows = [x for x in csv.reader(io.StringIO(r.text)) if x and x[0] == "D" and x[5] in ("LOAD ZONE", "HUB")]
    d = pd.DataFrame(rows).iloc[:, [1, 2, 4, 6]]
    d.columns = ["date", "he", "zone", "price"]
    d["x"] = d["he"].str.endswith("X")
    d["h"] = d["he"].str.slice(0, 2).astype(int) - 1
    d["t"] = pd.to_datetime(d["date"], format="%m/%d/%Y") + pd.to_timedelta(d["h"], unit="h")
    d["ts_utc"] = d["t"].dt.tz_localize(TZ["ISO-NE"], ambiguous=(~d["x"]).values).dt.tz_convert("UTC").dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    d["price"] = d["price"].astype(float)
    return d[["zone", "ts_utc", "price"]]


def f_miso(day):
    r = get(f"https://docs.misoenergy.org/marketreports/{day:%Y%m%d}_da_expost_lmp.csv")
    if r is None:
        return None
    d = pd.read_csv(io.StringIO(r.text), skiprows=4)
    d = d[(d["Type"] == "Hub") & (d["Value"] == "LMP") & d["Node"].str.endswith(".HUB")]  # 8 trading hubs (Type=Hub also lists AZ/ARR nodes)
    d = d.melt(id_vars=["Node"], value_vars=[f"HE {i}" for i in range(1, 25)], var_name="he", value_name="price")
    d["h"] = d["he"].str.slice(3).astype(int) - 1
    # market reports are in fixed EST (no DST): hour-beginning UTC = date + h + 5h
    t = pd.Timestamp(day) + pd.to_timedelta(d["h"] + 5, unit="h")
    d["ts_utc"] = t.dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    d = d.rename(columns={"Node": "zone"})
    d["price"] = pd.to_numeric(d["price"], errors="coerce")
    return d[["zone", "ts_utc", "price"]]


def f_spp(day):
    r = get(f"https://portal.spp.org/file-browser-api/download/da-lmp-by-settlement-location?path=/{day:%Y}/{day:%m}/By_Day/DA-LMP-SL-{day:%Y%m%d}0100.csv")
    if r is None:
        return None
    d = pd.read_csv(io.StringIO(r.text), usecols=["GMTIntervalEnd", "Settlement Location", "LMP"])
    d = d[d["Settlement Location"].isin(SPP_LOCS)]
    end = pd.to_datetime(d["GMTIntervalEnd"], format="%m/%d/%Y %H:%M:%S")
    d["ts_utc"] = (end - pd.Timedelta(hours=1)).dt.strftime("%Y-%m-%dT%H:%M:%SZ")  # interval is hour-ending
    return d.rename(columns={"Settlement Location": "zone", "LMP": "price"})[["zone", "ts_utc", "price"]]


def f_caiso(span):
    a, b = span  # UTC datetimes
    q = "https://oasis.caiso.com/oasisapi/SingleZip?resultformat=6&queryname=PRC_LMP&version=12&market_run_id=DAM"
    q += f"&startdatetime={a:%Y%m%dT%H:%M}-0000&enddatetime={b:%Y%m%dT%H:%M}-0000&node={','.join(CAISO_NODES)}"
    for _ in range(4):
        time.sleep(6)  # OASIS rate limit
        r = get(q, tries=1)
        if r is not None and r.content[:2] == b"PK":
            z = zipfile.ZipFile(io.BytesIO(r.content))
            d = pd.concat([pd.read_csv(z.open(n)) for n in z.namelist()])
            d = d[d["LMP_TYPE"] == "LMP"]
            d["ts_utc"] = pd.to_datetime(d["INTERVALSTARTTIME_GMT"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            return d.rename(columns={"NODE": "zone", "MW": "price"})[["zone", "ts_utc", "price"]]
        time.sleep(10)
    return None


def f_ercot(year):
    import gridstatus
    d = gridstatus.Ercot().get_dam_spp(year)
    d = d[d["Location"].str.startswith(("LZ_", "HB_"))]
    d = pd.DataFrame({"zone": d["Location"].astype(str),
                      "ts_utc": pd.to_datetime(d["Interval Start"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
                      "price": d["SPP"].astype(float)})
    return d.drop_duplicates(["zone", "ts_utc"])


def f_pjm(year):
    key = os.environ.get("PJM_API_KEY")
    if not key:
        return None
    # UNTESTED (no key available when written): zonal DA hourly LMP, Eastern prevailing time.
    out, start = [], 0
    while True:
        r = S.get("https://api.pjm.com/api/v1/da_hrl_lmps", headers={"Ocp-Apim-Subscription-Key": key}, timeout=120,
                  params={"download": "true", "startRow": start + 1, "rowCount": 50000, "type": "ZONE",
                          "datetime_beginning_ept": f"1/1/{year} 00:00 to 12/31/{year} 23:59", "fields": "datetime_beginning_utc,pnode_name,total_lmp_da"})
        if r.status_code != 200:
            return None
        d = pd.read_csv(io.StringIO(r.text))
        out.append(d)
        if len(d) < 50000:
            break
        start += 50000
    d = pd.concat(out)
    return pd.DataFrame({"zone": d["pnode_name"], "ts_utc": pd.to_datetime(d["datetime_beginning_utc"]).dt.strftime("%Y-%m-%dT%H:%M:%SZ"), "price": d["total_lmp_da"]})


def days(year):
    d = dt.date(year, 1, 1)
    while d.year == year:
        yield d
        d += dt.timedelta(days=1)


def jobs(mkt, year):
    if mkt == "NYISO":
        return [((year, m), f"{year}{m:02d}", f_nyiso) for m in range(1, 13)]
    if mkt in ("ISO-NE", "MISO", "SPP"):
        fn = {"ISO-NE": f_isone, "MISO": f_miso, "SPP": f_spp}[mkt]
        return [(d, f"{d:%Y%m%d}", fn) for d in days(year)]
    if mkt == "CAISO":
        out, a = [], dt.datetime(year, 1, 1, 8)  # PST midnight = 08:00Z
        end = dt.datetime(year + 1, 1, 1, 8)
        while a < end:
            b = min(a + dt.timedelta(days=30), end)
            out.append(((a, b), f"{a:%Y%m%d}", f_caiso))
            a = b
        return out
    if mkt == "ERCOT":
        return [(year, f"{year}", f_ercot)]
    if mkt == "PJM":
        return [(year, f"{year}", f_pjm)]


def pull(mkt, year):
    todo = [j for j in jobs(mkt, year) if not os.path.exists(cpath(mkt, j[1]))]
    if not todo:
        return
    log(f"{mkt}: {len(todo)} fetches")
    workers = {"CAISO": 1, "ERCOT": 1, "PJM": 1, "NYISO": 4}.get(mkt, 8)

    def run(j):
        arg, name, fn = j
        try:
            d = fn(arg)
        except Exception as e:  # noqa
            log(f"{mkt} {name} ERROR {type(e).__name__}: {str(e)[:120]}")
            return False
        if d is None or d.empty:
            log(f"{mkt} {name} MISSING (no data / auth required)")
            return False
        save(mkt, name, d)
        return True

    with ThreadPoolExecutor(workers) as ex:
        ok = sum(ex.map(run, todo))
    log(f"{mkt}: {ok}/{len(todo)} ok")


# ---------------- summary ----------------
def load(mkt):
    d = os.path.join(CACHE, mkt)
    if not os.path.isdir(d):
        return None
    fs = sorted(os.listdir(d))
    fs = [f for f in fs if f.endswith(".csv.gz")]
    if not fs:
        return None
    df = pd.concat([pd.read_csv(os.path.join(d, f)) for f in fs])
    df = df.drop_duplicates(["zone", "ts_utc"])
    df["ts"] = pd.to_datetime(df["ts_utc"], utc=True)
    return df


def summarize(year):
    rows = []
    for mkt in TZ:
        df = load(mkt)
        if df is None:
            continue
        df["loc"] = df["ts"].dt.tz_convert(TZ[mkt])
        df = df[df["loc"].dt.year == year]
        for zone, g in df.groupby("zone"):
            g = g.sort_values("ts")
            p = g["price"].astype(float)
            date, hr, mo = g["loc"].dt.date, g["loc"].dt.hour, g["loc"].dt.month
            dd = p.groupby(date.values).agg(lambda s: s.max() - s.min())
            row = dict(market=mkt, zone=zone, year=year, n_hours=len(g), mean=p.mean(),
                       p10=p.quantile(.1), p50=p.quantile(.5), p90=p.quantile(.9),
                       mean_daily_spread=dd.mean(), p90_daily_spread=dd.quantile(.9),
                       neg_hours=int((p < 0).sum()), hours_gt_500=int((p > 500).sum()))
            for lab, months in (("summer", (6, 7, 8, 9)), ("winter", (12, 1, 2))):
                sel = mo.isin(months).values
                hm = p[sel].groupby(hr.values[sel]).mean()
                for h in range(24):
                    row[f"{lab}_h{h:02d}"] = hm.get(h, np.nan)
            row["tz"] = TZ[mkt]
            row["source"] = SRC[mkt]
            rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        log("no data to summarize")
        return
    num = out.select_dtypes("float").columns
    out[num] = out[num].round(2)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out.to_csv(OUT, index=False)
    log(f"wrote {OUT}: {len(out)} rows")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=2025)
    ap.add_argument("--markets", default="NYISO,ISO-NE,ERCOT,CAISO,MISO,SPP,PJM")
    ap.add_argument("--summary-only", action="store_true")
    a = ap.parse_args()
    if not a.summary_only:
        for m in a.markets.split(","):
            if m == "PJM" and not os.environ.get("PJM_API_KEY"):
                log("PJM SKIPPED: Data Miner 2 requires an API key (set PJM_API_KEY)")
                continue
            pull(m, a.year)
    summarize(a.year)


if __name__ == "__main__":
    main()
