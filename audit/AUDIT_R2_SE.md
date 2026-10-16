# Round 2 presence re-audit: SE
Sample: audit/samples_r2/SE.json, seed 20261015, 20 presence cells (8 Yes, 12 No). Results: audit/results_r2/SE.json. Method: WebFetch/WebSearch, <=~2 fetches per item, cited URL first.

| Bucket | n | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Bar | Rate incl. inconcl. as fail |
|---|---|---|---|---|---|---|---|
| Yes | 8 | 6 | 1 | 1 | 85.7% (6/7) | 95% | 75.0% (6/8) |
| No | 12 | 10 | 1 | 1 | 90.9% (10/11) | 90% | 83.3% (10/12) |

**Result: Yes bar FAIL, No bar PASS (marginal).**

## Defects (data)
| eia_id | utility | cell | claimed -> fix | URL |
|---|---|---|---|---|
| 13216 | Nashville Electric Service | res_habit | Yes -> No | https://www.nespower.com/rates/ (residential RS flat; TOU/EV only on commercial) |
| 7646 | Greenwood CPW | res_habit | No -> Yes | https://greenwoodcpw.com/wp-content/uploads/2025/12/2026-01_E2500-Residential-EV-Charger.pdf (Code 2500 residential EV TOU) |

## Inconclusive
| eia_id | utility | cell | issue |
|---|---|---|---|
| 11291 | Lumbee River EMC | res_dispatch (Yes) | Only 2020/2021 news shows Connect to Save participation; no current utility page. Lean Yes |
| 4068 | Columbus Light & Water (MS) | res_habit (No) | Empty source_url; no utility rate page found |

## Caveats on confirmed items
- PowerFlex (3075, 40236, 3855, 5399 ci_dispatch): TVA-wide program, >1 MW only; LPC appears in signup dropdown, LPC-specific participation not separately stated.
- 18957 Tri-County EMC res_dispatch: Connect to Save enrollment temporarily paused (resumes Dec 1).
- 8571 High Point res_dispatch No: ElectriCities NCEMPA residential load-management program exists for member cities; High Point participation not shown. Re-check.

## Source defects (URL fix only)
- 17539 DESC res_dispatch: thermostatrewards.com/desc/faq/ 302 -> https://greatergrid.com/enroll/programs/thermostats/desc/faq
- 11291 Lumbee River res_dispatch: stale 2020 news article.
- Empty source_url: 4068 Columbus L&W, 8846 Hopkinsville (use https://hop-electric.com/electric/residential-electric/schedule-of-rates), 3222 Central Alabama EC (use https://caec.coop/electric-service/rates-availability/).
