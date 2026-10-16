# Round 3 presence re-audit: MISO

Seed 20261016. Sample: audit/samples_r3/MISO.json (20 presence cells: 8 Yes, 12 No). Results: audit/results_r3/MISO.json. Method: WebFetch/WebSearch only, cited source first, at most one replacement lookup on the utility's own site.

## Counts
| Claimed | Confirmed | Refuted | Inconclusive |
|---|---|---|---|
| Yes (8) | 6 | 1 | 1 |
| No (12) | 8 | 2 | 2 |

## Rates vs bars
- Yes rate (excl. inconclusive): 6/7 = 85.7% (bar 95%): FAIL. With inconclusive counted as misses: 6/8 = 75%.
- No rate (excl. inconclusive): 8/10 = 80% (bar 90%): FAIL. With inconclusive counted as misses: 8/12 = 66.7%.

## Inconclusive
- idx 3, 14471 Parke County REMC, res_dispatch=Yes: same invalid WVPA citation as Heartland (see defects). No Parke-specific program page was found. Probably a wrong Yes.
- idx 14, 18312 Sun Prairie Utilities, res_dispatch=No: the thermostat page is a purchase rebate only, but the site has an "Interruptible Load Credits" page that would not load.
- idx 16, 16613 Sam Houston EC, ci_habit=No: samhouston.net blocks fetching (robots).

## Defects
| eia_id | utility | cell | claimed -> fix | URL |
|---|---|---|---|---|
| 59505 | Heartland REMC | res_dispatch | Yes -> No (or Unknown). The cited WVPA page is PowerShift for schools via Hendricks Power, not residential; the Heartland rebates page shows no DR program | https://www.heartlandremc.com/rebates |
| 4362 | Corn Belt Energy | res_habit | No -> Yes. Rate 1-EV is an optional residential/farm EV and battery TOU (2-7 pm M-F $0.185, off-peak $0.030), amended 2024-07-25 | https://cornbeltenergy.com/wp-content/uploads/2024/07/Rate-1-EV-Amended-7-25-24.pdf |
| 5585 | Eastern Illini EC | res_habit | No -> Yes. "Demand component for all rate classes" since Mar 2024; $/kW not shown (moderate confidence) | https://eiec.org/demand-information |
| 14471 | Parke County REMC | res_dispatch | Re-research. The cited WVPA page does not support it; set Unknown/No unless a member page is found | https://www.wvpa.com/summer-enrollment/ |
| 14468 | People's Energy Coop | res_habit | Keep Yes. Re-cite to the rates page (Optional Residential TOU, Residential Demand, EV TOU); the off-peak page is a controlled-load program (res_dispatch evidence) | https://peoplesenergy.coop/rates |
| 1366 | Bay City EL&P | ci_dispatch | Keep No. The cited rate book is 2022-2024 vintage; check for a newer schedule | https://www.baycitymi.gov/DocumentCenter/View/6126/2022-2024-BCELP-Electric-Service-Rate-Schedule-v2 |

Systemic: WVPA summer-enrollment/PowerShift has been used as residential-dispatch evidence for WVPA member co-ops. docs/data/presence.json cites https://www.wvpa.com/summer-enrollment/ 8 times. Re-check all of those cells.
