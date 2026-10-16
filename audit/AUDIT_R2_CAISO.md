# Round 2 presence re-audit: CAISO

Sample: audit/samples_r2/CAISO.json, seed 20261015, 11 items (8 Yes, 3 No). Results: audit/results_r2/CAISO.json. Auditor: independent R2 agent, 2026-10-15. Method: WebFetch/WebSearch only, ~2 fetches/item.

## Rates vs bars
| Cell value | n | Confirmed | Refuted | Inconclusive | Rate | Bar | Result |
|---|---|---|---|---|---|---|---|
| Yes | 8 | 8 | 0 | 0 | 100% | 95% | PASS |
| No | 3 | 3 | 0 | 0 | 100% | 90% | PASS (small n) |

No value defects.

## Defects (source only, value correct)
| idx | eia_id | Utility | Cell | Problem | Replacement URL |
|---|---|---|---|---|---|
| 4 | 11124 | Lodi Electric Utility | res_habit | **Wrong utility**: cited lodiutilities.org appears to be Lodi, WI (608-592 phone, different TOD window). Medium-high confidence. | https://www.lodi.gov/1143/EV-Charger-and-Installation-Rebates (Schedule EV, residential EV TOU) |
| 6 | 16655 | Silicon Valley Power | ci_habit | Cited doc 6253 is D-1 residential only | https://www.siliconvalleypower.com/home/showpublisheddocument/6251/639032065160570000 (CB-1 TOU option, eff 2026-01-01) |
| 5 | 16655 | Silicon Valley Power | res_habit | Cited versioned URL returned client error | https://www.siliconvalleypower.com/home/showdocument?id=6253 |
| 7 | 11148 | Lompoc Electric Utility | ci_dispatch | Cited doc 1014 returned client error | https://cityoflompoc.com/home/showpublisheddocument/1004/638641596125370000 (Schedule CUR-1 Firm Curtailable) |
| 9 | 1192 | City of Banning | ci_habit | Non-www URL robots-blocked; URL title says 2022 but sheet is eff 2025-11-01 | https://www.banningca.gov/DocumentCenter/View/9909/... |

Low-depth confirmation: idx 9 Banning ci_habit No (only MC-1 50-500 kW checked; large-commercial schedule not opened).
