#!/usr/bin/env python3
"""Rank 1 Phase A: convert current URDB residential + commercial schedules for target territories into
data/processed/tariffs.csv and tariff_periods.csv (schema: plans/TARIFF_SCHEMA.md). Rows are method=URDB, tier=Secondary.
Only territories whose URDB status is 'current' (data/processed/urdb_coverage.csv) are converted; the rest are Phase B.
    python3 scripts/urdb_extract.py [data/usurdb.csv]"""
import ast, csv, os, sys
import pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "data/usurdb.csv")
MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
cov = pd.read_csv(os.path.join(ROOT, "data/processed/urdb_coverage.csv"), dtype=str)
cur = set(cov[cov.status == "current"].eia_id)
u = pd.read_csv(src, low_memory=False)
u["eiaid"] = pd.to_numeric(u["eiaid"], errors="coerce").astype("Int64").astype(str)
u = u[u.eiaid.isin(cur) & u.sector.isin(["Residential", "Commercial"])]
for c in ("startdate", "enddate"): u[c] = pd.to_datetime(u[c], errors="coerce", utc=True)
u = u[u.enddate.isna() | (u.enddate > pd.Timestamp.now(tz="UTC"))]
# URDB rarely end-dates old versions: drop anything another row supersedes, and anything that started
# more than 24 months before that utility+sector's newest schedule (old versions with new names).
sup = set(pd.read_csv(src, usecols=["supersedes"], low_memory=False).supersedes.dropna().astype(str))
u = u[~u.label.astype(str).isin(sup)]
newest = u.groupby(["eiaid", "sector"]).startdate.transform("max")
u = u[u.startdate >= newest - pd.Timedelta(days=730)]
def f(x):
    return "" if pd.isna(x) else (round(float(x), 6) if isinstance(x, (int, float)) else x)
def ranges(xs):
    xs = sorted(xs); out = []; s = p = xs[0]
    for x in xs[1:]:
        if x == p + 1: p = x; continue
        out.append((s, p)); s = p = x
    out.append((s, p)); return out
def blocks(sched):
    """12x24 matrix -> {period: [(months, hours)]} with months grouped by identical hour patterns."""
    out = {}
    pats = {}
    for m, row in enumerate(sched):
        for per in set(row):
            hrs = tuple(h for h in range(24) if row[h] == per)
            pats.setdefault((per, hrs), []).append(m)
    for (per, hrs), months in pats.items():
        ms = ",".join(f"{MON[a]}-{MON[b]}" if a != b else MON[a] for a, b in ranges(months))
        hs = ",".join(f"{a:02d}-{b+1:02d}" for a, b in ranges(list(hrs)))
        out.setdefault(per, []).append((ms, hs))
    return out
T, Pr = [], []
for _, r in u.iterrows():
    wk = ast.literal_eval(r.energyweekdayschedule) if isinstance(r.energyweekdayschedule, str) else None
    we = ast.literal_eval(r.energyweekendschedule) if isinstance(r.energyweekendschedule, str) else None
    nper = len({x for row in (wk or []) for x in row})
    dem = r.get("flatdemandstructure/period0/tier0rate")
    tdem = r.get("demandratestructure/period0/tier0rate")
    name = str(r["name"])
    kind = "TOU" if nper > 1 else ("Demand" if pd.notna(dem) or pd.notna(tdem) else "Flat")
    if "EV" in name or "Electric Vehicle" in name: kind = "EV-" + kind
    T.append({"eia_id": r.eiaid, "utility_name": r.utility, "sector": "Residential" if r.sector == "Residential" else "C&I",
              "rate_schedule": name[:120], "is_default": "Yes" if str(r.is_default).lower() in ("true", "1") else "",
              "rate_type": kind, "effective_date": "" if pd.isna(r.startdate) else r.startdate.date().isoformat(),
              "fixed_monthly_usd": f(r.fixedchargefirstmeter) if str(r.get("fixedchargeunits", "")) == "$/month" else "",
              "fixed_units": f(r.get("fixedchargeunits")), "min_bill": f(r.get("mincharge")),
              "demand_flat_usd_per_kw": f(dem), "demand_tou_usd_per_kw_p0": f(tdem),
              "peak_kw_min": f(r.get("peakkwcapacitymin")), "peak_kw_max": f(r.get("peakkwcapacitymax")),
              "source_url": f(r.source), "urdb_label": r.label, "method": "URDB", "tier": "Secondary", "last_verified": ""})
    if not wk: continue
    for day, sched in (("weekday", wk), ("weekend", we or wk)):
        for per, bl in blocks(sched).items():
            for t in range(11):
                rate = r.get(f"energyratestructure/period{per}/tier{t}rate")
                if pd.isna(rate): break
                adj = r.get(f"energyratestructure/period{per}/tier{t}adj")
                for ms, hs in bl:
                    Pr.append({"urdb_label": r.label, "eia_id": r.eiaid, "rate_schedule": name[:120], "day_type": day, "months": ms,
                               "hours": hs, "period": per, "tier": t, "tier_max_kwh": f(r.get(f"energyratestructure/period{per}/tier{t}max")),
                               "energy_usd_per_kwh": round(float(rate) + (0 if pd.isna(adj) else float(adj)), 6)})
pd.DataFrame(T).to_csv(os.path.join(ROOT, "data/processed/tariffs.csv"), index=False)
pd.DataFrame(Pr).to_csv(os.path.join(ROOT, "data/processed/tariff_periods.csv"), index=False)
t = pd.DataFrame(T)
print("schedules", len(T), "periods rows", len(Pr), "territories", t.eia_id.nunique())
print(t.groupby(["sector", "rate_type"]).size().to_string())
