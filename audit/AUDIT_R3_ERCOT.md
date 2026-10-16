# AUDIT R3 presence re-audit: ERCOT

Seed 20261016. Sample audit/samples_r3/ERCOT.json (20 items). Results audit/results_r3/ERCOT.json. Method: cited URL first, then at most one utility-site search/replacement; WebFetch/WebSearch only. NOT_DONE: 0.

| Set | Confirmed | Refuted | Inconclusive | Rate (excl. inconcl.) | Bar | Pass |
|---|---|---|---|---|---|---|
| Yes | 8 | 0 | 0 | 8/8 = 100.0% | 95% | PASS |
| No | 10 | 1 | 1 | 10/11 = 90.9% | 90% | PASS |

Counting inconclusive as not-confirmed: Yes 8/8, No 10/12. Small n (~10 per set): one miss moves the rate ~10 pts.

## Items

| idx | eia_id | utility | cell | claimed | verdict | evidence | note |
|---|---|---|---|---|---|---|---|
| 0 | 5063 | Denton Municipal Electric | ci_habit | Yes | CONFIRMED | https://www.cityofdenton.com/333/Business-Electric-Services | General Service Time of Use (TGS): on-peak demand $13.97/kVA vs off-peak $2.76/kVA. |
| 1 | 1175 | Bandera Electric Cooperative | res_habit | Yes | CONFIRMED | https://www.banderaelectric.com/account/payment-billing-options/time-based-usage/ | Voluntary Time Based Usage rate, single-phase rates effective 7/1/2026. |
| 2 | 1175 | Bandera Electric Cooperative | res_dispatch | Yes | CONFIRMED | https://www.banderaelectric.com/energy-services/programs/smart-thermostat/ | BEC adjusts enrolled ecobee thermostats at peak; $8/mo credit at >=70% event participation; enroll now. |
| 3 | 14626 | Pedernales Electric Cooperative, Inc. | ci_habit | Yes | CONFIRMED | https://mypec.com/large-power-rates/ | Large power TOU base power charge (summer peak 4:01-8 pm) + 4CP transmission charge. |
| 4 | 7752 | Guadalupe Valley Electric Cooperative (GVEC) | res_habit | Yes | CONFIRMED | https://www.gvec.org/electric/time-of-use-billing/ | Residential Time of Use program, enroll by phone. |
| 5 | 5078 | CoServ Electric (Denton County Electric Cooperative, Inc.) | ci_habit | Yes | CONFIRMED | https://www.coserv.com/service/commercial/commercial-rates/ | Demand Metered TOU, Industrial TOU, Public Buildings TOU rates. |
| 6 | 6182 | Farmers Electric Cooperative (Texas) | res_dispatch | Yes | CONFIRMED | https://farmerselectric.coop/energy-solutions/google-nest-rush-hour-rewards-program/ | Residential Nest Rush Hour Rewards DR, $50 first-year credit, Enroll Now. |
| 7 | 19490 | United Cooperative Services (United Electric Cooperative Services, Inc.) | res_dispatch | Yes | CONFIRMED | https://ucs.net/thermostat-program | BYOT Nest/Honeywell DR, $10/mo Jun-Sep, up to 20 events. |
| 8 | 7559 | Grayson-Collin Electric Cooperative, Inc. | res_habit | No | REFUTED | https://www.gcec.net/rates | Cited rates page lists residential 'Time of Use' plan: $28 base, on-peak $0.250/kWh (2-7 pm M-F), off-peak $0.1150/kWh. Flip res_habit to Yes. |
| 9 | 2409 | Brownsville Public Utilities Board (BPUB) | ci_dispatch | No | CONFIRMED | https://www.bpub.com/services/electric/energy-conservation | Programs: rebates, audits, solar only; site search found no C&I DR/interruptible. |
| 10 | 1273 | Bartlett Electric Cooperative | res_dispatch | No | CONFIRMED | https://bartlettec.coop/energy-conservation | Tips only; site search returns only B-Green Rebates; no DR. |
| 11 | 4146 | Concho Valley Electric Cooperative, Inc. | res_dispatch | No | CONFIRMED | https://cvec.coop/services/faqs | Only V.I.P. heat-pump incentive; site search found no load control. |
| 12 | 8620 | HILCO Electric Cooperative, Inc. | res_dispatch | No | CONFIRMED | https://hilco.coop/energy-conservation/for-consumers | Thermostat page is purchase rebate only (2026); consumer page has peak-hour conservation tips only, no co-op control. |
| 13 | 6958 | Garland Power & Light | res_dispatch | No | CONFIRMED | https://www.gpltexas.org/save-energy-money/energysaver-program | EnergySaver = efficiency bill credits (page says ended 9/30/2020 - stale source); site search found no thermostat/DR program. |
| 14 | 6182 | Farmers Electric Cooperative (Texas) | res_habit | No | CONFIRMED | https://farmerselectric.coop/billing-plans/ | Billing plans: prepaid, monthly, budget; rates page shows class % changes only; site search for TOU returned nothing. |
| 15 | 8620 | HILCO Electric Cooperative, Inc. | ci_habit | No | INCONCLUSIVE | https://static.spacecrafted.com/b993f461c2024818b0c102c57b4d48fc/r/b9129c1aca994a4fba67d678ca0fe16a/1/HECRateSheet.pdf | Rate sheet PDF has no machine-readable text (image). Business page shows conservation tips only. |
| 16 | 13418 | New Braunfels Utilities | ci_habit | No | CONFIRMED | https://www.nbutexas.com/wp-content/uploads/2023/04/FY-2024-Electric-Rates.pdf | SGS/LGS/VLP: seasonal generation rate, flat transmission, 15-min demand; no TOU/4CP/RTP. SOURCE DEFECT: FY2024 sheet is stale (FY26-27 rates approved); site search found no TOU. |
| 17 | 19159 | Tri-County Electric Cooperative, Inc. (Texas) | res_habit | No | CONFIRMED | https://www.tcectexas.com/sites/default/files/2025-05/rate-schedules-effective-january-2024.pdf | 202.1 Residential flat $0.14425/kWh; TOU only for public buildings (202.13) and LGS (202.14). Edge: 3-phase residential >=50 kVA can be on LGS-1 with demand charge. |
| 18 | 14626 | Pedernales Electric Cooperative, Inc. | res_dispatch | No | CONFIRMED | https://www.pec.coop/your-service/critical-load-program/ | Cited page is nonresidential critical-load registry (weak source). Site search: Power Rush Hour = voluntary peak alerts, no device control/VPP found. SOURCE DEFECT: cite irrelevant page. |
| 19 | 7979 | Hamilton County Electric Cooperative Association | res_dispatch | No | CONFIRMED | https://www.hamiltonelectric.coop/new-service/rates-fees/ | Rate 01 flat; site search found newsletters/tips only. |

## Defects

| eia_id | cell | issue | fix | URL |
|---|---|---|---|---|
| 7559 | res_habit | wrong value (No) | set Yes; update source_url | https://www.gcec.net/rates |
| 6958 | res_dispatch | source/data defect (see note) | replace source_url with evidence URL; fix noted field | https://www.gpltexas.org/save-energy-money/energysaver-program |
| 8620 | ci_habit | inconclusive | re-check (see note) | https://static.spacecrafted.com/b993f461c2024818b0c102c57b4d48fc/r/b9129c1aca994a4fba67d678ca0fe16a/1/HECRateSheet.pdf |
| 13418 | ci_habit | source/data defect (see note) | replace source_url with evidence URL; fix noted field | https://www.nbutexas.com/wp-content/uploads/2023/04/FY-2024-Electric-Rates.pdf |
| 14626 | res_dispatch | source/data defect (see note) | replace source_url with evidence URL; fix noted field | https://www.pec.coop/your-service/critical-load-program/ |
