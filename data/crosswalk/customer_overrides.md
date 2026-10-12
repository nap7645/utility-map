# Customer-count overrides in data/raw/hifld_over10k.csv
EIA-861 not reachable from the build sandboxes (eia.gov blocked by proxy). Filled from company SEC filings (Primary):
| eia_id | utility | customers | source |
|---|---|---|---|
| 44372 | Oncor Electric Delivery | 4111000 (active meters, 4,111 thousand, 2025-12-31) | https://www.sec.gov/Archives/edgar/data/1193311/000119312526073624/d17515dex991.htm |
| 8901 | CenterPoint Energy Houston Electric | 2859313 (metered customers, 2025-12-31) | https://www.sec.gov/Archives/edgar/data/1130310/000113031026000008/cnp-20251231.htm |
Still blank (no division-level public figure found; needs EIA-861 Sales_Ult_Cust delivery rows): 3278 AEP Texas Central, 20404 AEP Texas North (combined AEP Texas = 1,122,118 per 2024 AEP Texas fact sheet), 40051 TNMP.
