#!/usr/bin/env python3
"""Rank 1 Phase A: URDB coverage of target territories.
    python3 scripts/urdb_coverage.py [data/usurdb.csv]
Reads the URDB bulk CSV (not in git) and data/raw/hifld_over10k.csv; writes
data/processed/urdb_coverage.csv (one row per target eia_id) and prints a summary."""
import ast, sys, os
import pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "data/usurdb.csv")
cols = ["label", "eiaid", "name", "is_default", "startdate", "enddate", "latest_update", "sector",
        "energyweekdayschedule", "flatdemandunit", "demandweekdayschedule", "flatdemandstructure/period0/tier0rate",
        "demandratestructure/period0/tier0rate", "fixedchargefirstmeter"]
u = pd.read_csv(src, usecols=lambda c: c in cols, low_memory=False)
u["eiaid"] = pd.to_numeric(u["eiaid"], errors="coerce").astype("Int64").astype(str)
for c in ("startdate", "enddate", "latest_update"):
    u[c] = pd.to_datetime(u[c], errors="coerce", utc=True)
u["active"] = u["enddate"].isna() | (u["enddate"] > pd.Timestamp.now(tz="UTC"))
def nper(s):
    try:
        m = ast.literal_eval(s) if isinstance(s, str) else None
        return len({x for row in m for x in row}) if m else 0
    except Exception:
        return 0
u["tou"] = u["energyweekdayschedule"].map(nper) > 1
u["demand"] = u[["flatdemandstructure/period0/tier0rate", "demandratestructure/period0/tier0rate"]].notna().any(axis=1) if "demandratestructure/period0/tier0rate" in u else u["flatdemandstructure/period0/tier0rate"].notna()
den = pd.read_csv(os.path.join(ROOT, "data/raw/hifld_over10k.csv"), dtype=str)
out = []
now = pd.Timestamp.now(tz="UTC")
for _, d in den.iterrows():
    g = u[(u.eiaid == d.eia_id) & u.active]
    row = {"eia_id": d.eia_id, "hifld_name": d.hifld_name, "state": d.hifld_state, "customers": d.customers}
    for sec, key in (("Residential", "res"), ("Commercial", "com")):
        s = g[g.sector == sec]
        last = s["startdate"].max()
        row[f"{key}_n"] = len(s)
        row[f"{key}_latest_start"] = "" if pd.isna(last) else last.date().isoformat()
        row[f"{key}_stale"] = bool(len(s)) and (pd.isna(last) or (now - last).days > 730)
        row[f"{key}_tou"] = bool(s["tou"].any())
        row[f"{key}_demand"] = bool(s["demand"].any())
    row["status"] = ("missing" if row["res_n"] == 0 else "stale" if row["res_stale"] else "current")
    out.append(row)
o = pd.DataFrame(out)
o.to_csv(os.path.join(ROOT, "data/processed/urdb_coverage.csv"), index=False)
cust = pd.to_numeric(o.customers, errors="coerce").fillna(0)
print("URDB rows:", len(u), "active:", int(u.active.sum()))
for st in ("current", "stale", "missing"):
    m = o.status == st
    print(f"{st:8s} territories {m.sum():4d}  customers {cust[m].sum()/1e6:6.1f}M ({100*cust[m].sum()/cust.sum():.0f}%)")
print("res TOU in URDB (current):", int((o.res_tou & (o.status == 'current')).sum()), " commercial schedules present:", int((o.com_n > 0).sum()))
