#!/usr/bin/env python3
"""Combine URDB-extracted tariffs with agent-researched rows (data/raw/tariffs/*_tariffs.csv, *_periods.csv).
Agent rows (tier Primary) replace all URDB rows for the same eia_id. Writes data/processed/tariffs_merged.csv and
tariff_periods_merged.csv. URDB-only files (tariffs.csv, tariff_periods.csv) are left untouched.
    python3 scripts/merge_tariffs.py"""
import glob, os
import pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
ut = pd.read_csv(P("data/processed/tariffs.csv"), dtype=str, keep_default_na=False)
up = pd.read_csv(P("data/processed/tariff_periods.csv"), dtype=str, keep_default_na=False)
at = pd.concat([pd.read_csv(f, dtype=str, keep_default_na=False) for f in sorted(glob.glob(P("data/raw/tariffs/*_tariffs.csv")))], ignore_index=True)
ap = pd.concat([pd.read_csv(f, dtype=str, keep_default_na=False) for f in sorted(glob.glob(P("data/raw/tariffs/*_periods.csv")))], ignore_index=True)
agent_ids = set(at.eia_id)
t = pd.concat([ut[~ut.eia_id.isin(agent_ids)], at], ignore_index=True).fillna("")
p = pd.concat([up[~up.eia_id.isin(agent_ids)], ap], ignore_index=True).fillna("")
if "scope" in t: t["scope"] = t["scope"].replace("", "core")
t.to_csv(P("data/processed/tariffs_merged.csv"), index=False); p.to_csv(P("data/processed/tariff_periods_merged.csv"), index=False)
print("territories", t.eia_id.nunique(), "(agent", len(agent_ids), ") schedules", len(t), "period rows", len(p))
