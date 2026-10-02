# Automated audit - 2026-10-02

| ID | Check | Result | Summary |
|---|---|---|---|
| A1 | Every row validates | FAIL | 5 problem(s) (+7 sentinel-customer polygons, info only) |
| A2 | Every target territory has a presence row (docs/data/presence.json) | PASS | 993 targets, 0 missing, 0 duplicated, 0 extra rows (info only) |
| A3 | Every program/IC utility name joins a boundary | PASS | 261 utility names, 0 unjoined |
| A4 | No cross-state name joins | PASS | 0 ambiguous cross-state join(s); 17 polygon-STATE differences listed for review (info) |
| A5 | Every Yes (and every program row) has a URL | PASS | 0 missing |
| A6 | Link check >=95% non-4xx | NOT RUN | NOT RUN - run: python3 scripts/audit.py --links |
| A7 | Every target territory has a governing body | PASS | 0 of 993 target territories resolve to OTHER (10 of 2914 polygons incl. <10k) |
| A8 | Polygon layer covers the lower 48 + DC (proxy) | PASS | 49/49 states have polygons; 983/983 targets have a polygon (100.00% of target customers). Geographic gaps need a land-mask check (not done). |

## A1 detail (12 lines)

- denominator eia 44372 ONCOR ELECTRIC DELIVERY COMPANY LLC: customers=''
- denominator eia 8901 CENTERPOINT ENERGY: customers=''
- denominator eia 40051 TEXAS-NEW MEXICO POWER CO: customers=''
- denominator eia 3278 AEP TEXAS CENTRAL COMPANY: customers=''
- denominator eia 20404 AEP TEXAS NORTH COMPANY: customers=''
- (info, HIFLD no-data sentinel; UI hides it) geojson 1572 BADGER POWER MARKETING AUTHORITY: CUSTOMERS=-999999
- (info, HIFLD no-data sentinel; UI hides it) geojson 20858 WPPI ENERGY: CUSTOMERS=-999999
- (info, HIFLD no-data sentinel; UI hides it) geojson 20910 WOLVERINE POWER SUPPLY COOP: CUSTOMERS=-999999
- (info, HIFLD no-data sentinel; UI hides it) geojson 5580 EAST KENTUCKY POWER COOP, INC: CUSTOMERS=-999999
- (info, HIFLD no-data sentinel; UI hides it) geojson 13687 NORTH CAROLINA EASTERN M P A: CUSTOMERS=-999999
- (info, HIFLD no-data sentinel; UI hides it) geojson 16821 SAM RAYBURN MUNICIPAL PWR AGNY: CUSTOMERS=-999999
- (info, HIFLD no-data sentinel; UI hides it) geojson 17583 SOUTH TEXAS ELECTRIC COOP, INC: CUSTOMERS=-999999

## A4 detail (17 lines)

- (info) 'Southwestern Electric Power Co (SWEPCO)' (AR/LA) -> polygon SOUTHWESTERN ELECTRIC POWER CO eia 17698 HIFLD STATE=OK, centroid=32.86,-94.56
- (info) 'Ameren Illinois Company d/b/a Ameren Illinois' (IL) -> polygon AMEREN ILLINOIS COMPANY eia 56697 HIFLD STATE=MO, centroid=39.10,-89.19
- (info) 'Upper Michigan Energy Resources (UMERC)' (MI) -> polygon UPPER MICHIGAN ENERGY RESOURCES CORP. eia 60631 HIFLD STATE=WI, centroid=46.25,-87.73
- (info) 'Northern States Power Co - Wisconsin (Xcel Energy)' (WI) -> polygon NORTHERN STATES POWER CO eia 13780 HIFLD STATE=MN, centroid=44.60,-91.48
- (info) 'Kentucky Power (AEP)' (KY) -> polygon KENTUCKY POWER CO eia 22053 HIFLD STATE=OH, centroid=37.81,-82.93
- (info) 'Potomac Edison Co (FirstEnergy - Maryland)' (MD/WV) -> polygon THE POTOMAC EDISON COMPANY eia 15263 HIFLD STATE=PA, centroid=39.26,-78.28
- (info) 'Jersey Central Power & Light Co (JCP&L)' (NJ) -> polygon JERSEY CENTRAL POWER & LT CO eia 9726 HIFLD STATE=OH, centroid=40.53,-74.52
- (info) 'Rockland Electric Co (RECO)' (NJ) -> polygon ROCKLAND ELECTRIC CO eia 16213 HIFLD STATE=NY, centroid=41.04,-74.15
- (info) 'Metropolitan Edison Co (Met-Ed)' (PA) -> polygon METROPOLITAN EDISON CO eia 12390 HIFLD STATE=OH, centroid=40.55,-75.78
- (info) 'Pennsylvania Electric Co (Penelec)' (PA) -> polygon PENNSYLVANIA ELECTRIC CO eia 14711 HIFLD STATE=OH, centroid=41.09,-78.22
- (info) 'Pennsylvania Power Co' (PA) -> polygon PENNSYLVANIA POWER CO eia 14716 HIFLD STATE=OH, centroid=40.88,-79.87
- (info) 'Appalachian Power Co (AEP - Virginia)' (VA/WV) -> polygon APPALACHIAN POWER CO eia 733 HIFLD STATE=OH, centroid=37.56,-81.31
- (info) 'Monongahela Power Co (FirstEnergy - West Virginia)' (WV) -> polygon MONONGAHELA POWER CO eia 12796 HIFLD STATE=PA, centroid=38.78,-80.27
- (info) 'Wheeling Power Co (AEP - West Virginia)' (WV) -> polygon WHEELING POWER CO eia 20521 HIFLD STATE=OH, centroid=39.74,-80.65
- (info) 'Massachusetts Electric Co (National Grid MA)' (MA) -> polygon MASSACHUSETTS ELECTRIC CO eia 11804 HIFLD STATE=NY, centroid=42.35,-71.30
- (info) 'Fitchburg Gas & Electric Light Co (Unitil MA)' (MA) -> polygon FITCHBURG GAS & ELEC LIGHT CO eia 6374 HIFLD STATE=NH, centroid=42.39,-71.58
- (info) 'Liberty Utilities (Granite State Electric)' (NH) -> polygon LIBERTY UTILITIES eia 57483 HIFLD STATE=CA, centroid=39.14,-120.13

## A7 detail (1 lines)

- distribution over target territories: MISO=201, WECC-nonRTO=150, SERC-nonRTO=139, PJM=112, TVA=105, SPP=80, ERCOT=59, ISO-NE=40, AECI=33, FRCC-nonRTO=31, CAISO=18, NYISO=12, AK-islanded=6, HI-islanded=4, LG&E/KU (non-RTO)=2, Other-nonRTO=1
