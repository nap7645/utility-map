# Audit R3 presence re-audit: SE

Seed 20261016. Sample: audit/samples_r3/SE.json (20 items). Results: audit/results_r3/SE.json. Method: WebFetch/WebSearch, cited URL first, <=1 replacement search on utility's own site.

## Rates vs bars

| Claimed | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Rate incl. inconcl. as fail | Bar | Pass |
|---|---|---|---|---|---|---|---|
| Yes | 6 | 1 | 1 | 85.7% | 75.0% | 95% | FAIL |
| No | 10 | 2 | 0 | 83.3% | 83.3% | 90% | FAIL |

## Items

| idx | eia_id | utility | cell | claimed | verdict | correct | evidence |
|---|---|---|---|---|---|---|---|
| 0 | 7639 | Greenville Utilities Commission (GUC) | ci_habit | Yes | CONFIRMED | Yes | https://www.guc.com/sites/default/files/uploads/07-01-25%20Rates/07-01-25%20electric%20rates/electric-rate-schedule-eg-3-july-1-2025.pdf |
| 1 | 3757 | Clay Electric Cooperative, Inc. | ci_dispatch | Yes | CONFIRMED | Yes | https://clayelectric.com/sites/default/files/documents/RateBook0625.pdf |
| 2 | 17033 | Sheffield Utilities | res_dispatch | Yes | CONFIRMED | Yes | https://greatergrid.com/enroll/programs/thermostats/tvaenergyright/faq/lpc |
| 3 | 9617 | JEA | ci_dispatch | Yes | INCONCLUSIVE | Yes | https://www.jea.com/My_Account/Rates/Electric_Tariff.aspx |
| 4 | 6784 | French Broad Electric Membership Corporation | res_habit | Yes | REFUTED | No | https://www.frenchbroademc.com/index.php/billing/rates-and-fees/ |
| 5 | 3916 | Cobb EMC | res_habit | Yes | CONFIRMED | Yes | https://www.cobbemc.com/smart-choice-rate |
| 6 | 944 | Athens Utilities | res_dispatch | Yes | CONFIRMED | Yes | https://greatergrid.com/enroll/programs/thermostats/tvaenergyright/faq/lpc |
| 7 | 17539 | Dominion Energy South Carolina | ci_dispatch | Yes | CONFIRMED | Yes | http://www.dominionenergy.com/en/South-Carolina/Large-Business-Services |
| 8 | 7450 | Grady EMC | res_dispatch | No | CONFIRMED | No | https://gradyemc.com/rebates-services/ |
| 9 | 15211 | Pontotoc Electric Power Association | res_dispatch | No | CONFIRMED | No | https://greatergrid.com/enroll/programs/thermostats/tvaenergyright/faq/lpc |
| 10 | 4624 | Cumberland Electric Membership Corporation | res_habit | No | CONFIRMED | No | https://cemc.org/wp-content/uploads/2025/01/RATES-2025-FCA192-202501-002.pdf |
| 11 | 26218 | Little Ocmulgee EMC | res_dispatch | No | CONFIRMED | No | https://www.loemc.com/ |
| 12 | 9616 | Beaches Energy Services | res_dispatch | No | CONFIRMED | No | https://www.beachesenergy.com/energy-savings/residential-commercial-rates |
| 13 | 12330 | Meriwether Lewis Electric Cooperative | res_dispatch | No | REFUTED | Yes | https://greatergrid.com/enroll/programs/thermostats/tvaenergyright/faq/lpc |
| 14 | 19219 | Diverse Power | res_habit | No | CONFIRMED | No | https://www.diversepower.com/content/uploads/Residential-Service-Electric-Rate-1.pdf |
| 15 | 18305 | Sumter EMC | ci_dispatch | No | CONFIRMED | No | https://sumteremc.coop/fees-and-rates |
| 16 | 19162 | Tri-County Electric Membership Corporation | res_dispatch | No | REFUTED | Yes | https://www.tcemc.org/?p=1894 |
| 17 | 15700 | Rayle EMC | res_dispatch | No | CONFIRMED | No | https://www.rayleemc.com/customer-service |
| 18 | 1891 | Blue Ridge Mountain EMC | ci_habit | No | CONFIRMED | No | https://www.brmemc.com/electric-rate-sheet/ |
| 19 | 40212 | Colquitt EMC | res_dispatch | No | CONFIRMED | No | https://colquittemc.com/energy-management |

## Defects (data fixes; not applied)

- presence: eia_id 6784 (French Broad Electric Membership Corporation), cell res_habit: Yes -> No. Residential: Primary/Secondary/FlexPay flat 12.9c/kWh + base charge; demand charge only on Large Power. Site search found no res TOU/CPP/EV rate. URL: https://www.frenchbroademc.com/index.php/billing/rates-and-fees/
- presence: eia_id 12330 (Meriwether Lewis Electric Cooperative), cell res_dispatch: No -> Yes. Meriwether Lewis Electric Cooperative is listed as a participating LPC in TVA EnergyRight Smart Thermostat Rewards (thermostat DR, up to 4F/4h at peak). URL: https://greatergrid.com/enroll/programs/thermostats/tvaenergyright/faq/lpc
- presence: eia_id 19162 (Tri-County Electric Membership Corporation), cell res_dispatch: No -> Yes. Tri-County EMC (TN) own Demand Response Program: water-heater switch cycling and thermostat -3F during TVA peaks; $1,500 install fee waived for participants. (Not in TVA thermostat LPC list, which the No apparently relied on.) URL: https://www.tcemc.org/?p=1894

## Source defects / inconclusive

- eia_id 9617 ci_dispatch (INCONCLUSIVE): Cited tariff page and Oct-2026 rates PDF both return bot-verification (captcha) pages; unreadable. URL: https://www.jea.com/My_Account/Rates/Electric_Tariff.aspx
