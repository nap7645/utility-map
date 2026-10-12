# Customer-count overrides in data/raw/hifld_over10k.csv
ERCOT T&D utilities have blank customers in HIFLD. Filled from EIA-861 2024, Delivery_Companies_2024.xlsx (Part C, Service Type Delivery, Data Type O, TOTAL Customers count). File downloaded by Nathan from https://www.eia.gov/electricity/data/eia861/zip/f8612024.zip.
| eia_id | utility | customers (EIA-861 2024) | cross-check |
|---|---|---|---|
| 44372 | Oncor Electric Delivery Company LLC | 4010973 | SEC 8-K: 4,111 thousand active meters at 2025-12-31 |
| 8901 | CenterPoint Energy (Houston Electric) | 2811820 | SEC 10-K: 2,859,313 metered customers at 2025-12-31 |
| 3278 | AEP Texas Central Company | 916131 | AEP Texas fact sheet 2024: 1,122,118 combined Central+North (EIA sum 1,116,260) |
| 20404 | AEP Texas North Company | 200129 | (see above) |
| 40051 | Texas-New Mexico Power Co | 277003 | none public |
