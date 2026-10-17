#!/usr/bin/env python3
"""Load EIA-861 2024 average prices and dynamic-pricing flags for every target territory.
    python3 scripts/eia861_load.py
Inputs: data/raw/eia861/Sales_Ult_Cust_2024.xlsx, Dynamic_Pricing_2024.xlsx (from eia.gov f8612024.zip), data/raw/hifld_over10k.csv
Output: data/processed/eia861_rates.csv. Average price = revenue / sales (cents/kWh), by Part/Service Type:
  bundled_* = Part A Bundled (utility sells energy + delivery); delivery_* = Part C Delivery (wires only, retail choice).
Rows for the territory's own state are used when present, else all states for that utility number."""
import os
import openpyxl, pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P = lambda *a: os.path.join(ROOT, *a)
def sheet(fn, skip):
    ws = openpyxl.load_workbook(P("data/raw/eia861", fn), read_only=True).worksheets[0]
    rows = list(ws.iter_rows(values_only=True))[skip:]
    return rows
num = lambda x: float(x) if isinstance(x, (int, float)) else 0.0
S = []
for r in sheet("Sales_Ult_Cust_2024.xlsx", 3):
    if not r or r[1] is None: continue
    S.append({"eia_id": str(r[1]), "state": r[6], "part": r[3], "stype": r[4], "res_rev": num(r[9]), "res_mwh": num(r[10]), "res_cust": num(r[11]),
              "com_rev": num(r[12]), "com_mwh": num(r[13]), "com_cust": num(r[14])})
S = pd.DataFrame(S)
D = {}
for r in sheet("Dynamic_Pricing_2024.xlsx", 3):
    if not r or r[1] is None: continue
    k = (str(r[1]), r[4]); f = lambda i: "Y" if str(r[i]).strip().upper() == "Y" else ""
    D[k] = {"dyn_res_enrolled": num(r[6]), "dyn_com_enrolled": num(r[7]), "res_tou": f(11), "com_tou": f(12), "res_rtp": f(15), "com_rtp": f(16),
            "res_vpp": f(19), "com_vpp": f(20), "res_cpp": f(23), "com_cpp": f(24), "res_cpr": f(27), "com_cpr": f(28)}
den = pd.read_csv(P("data/raw/hifld_over10k.csv"), dtype=str)
out = []
for _, d in den.iterrows():
    s = S[S.eia_id == d.eia_id]
    if (s.state == d.hifld_state).any(): s = s[s.state == d.hifld_state]
    row = {"eia_id": d.eia_id, "hifld_name": d.hifld_name, "state": d.hifld_state}
    for lab, part in (("bundled", s.stype == "Bundled"), ("delivery", s.stype == "Delivery")):
        g = s[part]
        for sec in ("res", "com"):
            mwh = g[f"{sec}_mwh"].sum(); rev = g[f"{sec}_rev"].sum()
            row[f"{lab}_{sec}_cents_kwh"] = round(100 * rev / mwh, 2) if mwh > 0 else ""
            row[f"{lab}_{sec}_customers"] = int(g[f"{sec}_cust"].sum()) if mwh > 0 else ""
    dd = D.get((d.eia_id, d.hifld_state)) or next((v for (i, st), v in D.items() if i == d.eia_id), {})
    row.update(dd)
    row["eia861_found"] = "Y" if len(s) else ""
    out.append(row)
o = pd.DataFrame(out)
o.to_csv(P("data/processed/eia861_rates.csv"), index=False)
print("territories", len(o), "with EIA-861 sales rows", (o.eia861_found == "Y").sum(),
      "| bundled res price", (o.bundled_res_cents_kwh != "").sum(), "| delivery-only res", (o.delivery_res_cents_kwh != "").sum(),
      "| any res dynamic pricing", (o[["res_tou","res_rtp","res_vpp","res_cpp","res_cpr"]].fillna("") == "Y").any(axis=1).sum())
