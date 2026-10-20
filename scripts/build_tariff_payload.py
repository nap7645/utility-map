#!/usr/bin/env python3
"""Build docs/data/tariffs.json for the map drawer: per eia_id, core tariff schedules (residential default first),
EIA-861 2024 averages, riders and the LMP zone summary.
    python3 scripts/build_tariff_payload.py"""
import glob, json, os
import pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P = lambda *a: os.path.join(ROOT, *a)
rd = lambda p: pd.read_csv(P(p), dtype=str, keep_default_na=False)
t, per = rd("data/processed/tariffs_merged.csv"), rd("data/processed/tariff_periods_merged.csv")
eia, zm, ls = rd("data/processed/eia861_rates.csv"), rd("data/processed/lmp_zone_map.csv"), rd("data/processed/lmp_summary.csv")
rid = pd.concat([rd(os.path.relpath(f, ROOT)) for f in sorted(glob.glob(P("data/raw/tariffs/riders_*.csv")))], ignore_index=True)
num = lambda x: float(x) if x not in ("", None) else None
out = {}
t = t[t.get("scope", "core").replace("", "core") == "core"] if "scope" in t else t
import re as _re
per["_key"] = per.urdb_label.where(per.urdb_label != "", per.eia_id + "|" + per.rate_schedule)
t["_key"] = t.urdb_label.where(t.urdb_label != "", t.eia_id + "|" + t.rate_schedule)
PG = {k: g for k, g in per.groupby("_key")}
for eid, g in t.groupby("eia_id"):
    g = g.assign(_o=(g.sector != "Residential").astype(int) * 4 + (g.is_default != "Yes").astype(int) * 2
                 + (~g.rate_type.str.contains("TOU|EV")).astype(int)).sort_values(["_o", "rate_schedule"])
    scheds, stems = [], set()
    for _, r in g.iterrows():
        if len(scheds) >= 8: break
        stem = (r.sector, _re.sub(r"\s*-?\s*((baseline\s+)?region|baseline|territory|zone|coastal|inland|desert|mountain|valley|climate)\b.*$", "",
                                    r.rate_schedule, flags=_re.I).strip().lower())
        short = (r.sector, _re.sub(r"[^a-z0-9]", "", r.rate_schedule.lower())[:28])
        if stem in stems or short in stems: continue
        stems.update([stem, short])
        pp = PG.get(r._key, per.iloc[0:0])
        allp = sorted({float(x) for x in pp.energy_usd_per_kwh if x})
        t0 = pp[pp.tier == "0"]
        prices = sorted({float(x) for x in t0.energy_usd_per_kwh if x})
        peak, ty = "", r.rate_type
        wk = t0[t0.day_type == "weekday"]
        intraday = any(m.energy_usd_per_kwh.nunique() > 1 for _, m in wk.groupby("months")) or \
                   any(h not in ("0-24", "00-24") for h in wk.hours)
        if len(prices) > 1 and intraday:
            w = wk[(wk.energy_usd_per_kwh.astype(float) == prices[-1]) & ~wk.hours.isin(["0-24", "00-24"])]
            peak = "; ".join(sorted({f"{a.months} {a.hours}" for _, a in w.iterrows()}))[:80]
        elif not intraday and ty in ("TOU", "Flat", "EV-TOU", "EV-Flat"):
            ty = ty.replace("TOU", "Flat").replace("Flat", "Seasonal") if len(prices) > 1 else ty.replace("TOU", "Flat")
        tiered = (pp.tier != "0").any()
        scheds.append({"n": r.rate_schedule[:70], "s": "R" if r.sector == "Residential" else "C", "d": r.is_default == "Yes",
                       "ty": ty + (" tiered" if tiered else ""), "fx": num(r.fixed_monthly_usd), "fu": r.fixed_units,
                       "lo": allp[0] if allp else None, "hi": allp[-1] if allp else None, "pk": peak,
                       "dm": num(r.demand_flat_usd_per_kw) or num(r.demand_tou_usd_per_kw_p0),
                       "ef": r.effective_date, "u": r.source_url, "m": r.method})
    out[eid] = {"t": scheds}
for _, e in eia.iterrows():
    o = out.setdefault(e.eia_id, {})
    o["eia"] = {k: num(e[c]) for k, c in (("r", "bundled_res_cents_kwh"), ("c", "bundled_com_cents_kwh"), ("rd", "delivery_res_cents_kwh"), ("cd", "delivery_com_cents_kwh")) if e[c]}
    dyn = [lab for lab, c in (("TOU", "res_tou"), ("RTP", "res_rtp"), ("CPP", "res_cpp"), ("PTR", "res_cpr"), ("VPP", "res_vpp")) if e[c] == "Y"]
    if dyn: o["eia"]["dyn"] = dyn
for eid, g in rid.groupby("eia_id"):
    res_def = next((x["n"] for x in out.get(eid, {}).get("t", []) if x["s"] == "R"), None)
    g = g[g.rate_schedule.isin(["ALL", "ALL-RES"]) | (g.rate_schedule.str[:70] == (res_def or "\0"))]
    rows = [{"n": r.rider_name[:70], "k": num(r.usd_per_kwh), "mo": num(r.usd_per_month), "kw": num(r.usd_per_kw), "a": r.additive != "No", "sc": r.rate_schedule[:30]}
            for _, r in g.iterrows() if not r.rider_name.startswith("(")]
    if rows and eid in out: out[eid]["rd"] = rows[:12]
lsx = ls.set_index(["market", "zone"])
for _, z in zm[zm.zone != ""].iterrows():
    if (z.market, z.zone) not in lsx.index: continue
    s = lsx.loc[(z.market, z.zone)]
    out.setdefault(z.eia_id, {})["lmp"] = {"mk": z.market, "z": z.zone, "cf": z.confidence, "mean": num(s["mean"]), "sp": num(s["mean_daily_spread"]),
                                           "p90": num(s["p90_daily_spread"]), "neg": num(s["neg_hours"]),
                                           "su": [num(s[f"summer_h{h:02d}"]) for h in range(24)], "wi": [num(s[f"winter_h{h:02d}"]) for h in range(24)]}
json.dump(out, open(P("docs/data/tariffs.json"), "w"), separators=(",", ":"))
print("territories", len(out), "with schedules", sum("t" in v for v in out.values()), "with lmp", sum("lmp" in v for v in out.values()),
      "size KB", os.path.getsize(P("docs/data/tariffs.json")) // 1024)
