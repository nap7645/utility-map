#!/usr/bin/env python3
"""Tag each row of data/processed/tariffs.csv with scope = core | deferred (Rank 1 scope: residential + small C&I).
C&I rows are deferred when the name says large/medium/primary/transmission/industrial/lighting/standby/irrigation etc.
or the eligibility minimum is >= 100 kW. Idempotent; rewrites tariffs.csv in place.
    python3 scripts/tariff_scope.py"""
import os, re
import pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(ROOT, "data/processed/tariffs.csv")
t = pd.read_csv(p, dtype=str, keep_default_na=False)
BIG = re.compile(r"large|medium|primary|transmission|industrial|\bLGS\b|\bMGS\b|\bLP\b|standby|lighting|street|irrigation|pumping|"
                 r"outdoor|multiple dwelling|direct access|\b[5-9]\d{2}\s?kw|\b\d,?\d{3}\s?kw", re.I)
mn = pd.to_numeric(t.peak_kw_min, errors="coerce")
deferred = (t.sector == "C&I") & (t.rate_schedule.str.contains(BIG) | (mn >= 100))
t["scope"] = deferred.map({True: "deferred", False: "core"})
t.to_csv(p, index=False)
print(t.groupby(["sector", "scope"]).size().to_string())
