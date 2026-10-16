# Round 2 presence re-audit: West
Sample: audit/samples_r2/West.json, seed 20261015, 20 presence cells (8 Yes, 12 No). Results: audit/results_r2/West.json. Method: WebFetch/WebSearch, <=~2 fetches per item, cited URL first.

| Bucket | n | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Bar | Rate incl. inconcl. as fail |
|---|---|---|---|---|---|---|---|
| Yes | 8 | 4 | 1 | 3 | 80.0% (4/5) | 95% | 50.0% (4/8) |
| No | 12 | 9 | 2 | 1 | 81.8% (9/11) | 90% | 75.0% (9/12) |

**Result: FAIL both bars.**

## Defects (data)
| eia_id | utility | cell | claimed -> fix | URL |
|---|---|---|---|---|
| 3660 | Clark Public Utilities | res_habit | Yes -> No | https://www.clarkpublicutilities.com/about-cpu/public-documents/current-electric-water-rates/ (flat 8.79c/kWh only) |
| 3660 | Clark Public Utilities | res_dispatch | No -> Yes | https://www.clarkpublicutilities.com/residential-customers/reduce-energy-waste-and-lower-your-bill/all-rebates-incentives/electric-vehicle-managed-charging-program/ (Optiwatt EV managed-charging pilot through 2026; cap 1,400 EVs). Habit/dispatch evidence was swapped. |
| 20997 | Yellowstone Valley EC | res_habit | No -> Yes | https://www.yvec.com/your-account/electrical-rates/ ($2.00/kW demand on net-metered residential; borderline, subset-only) |

## Inconclusive (re-check, lean noted)
| eia_id | utility | cell | issue |
|---|---|---|---|
| 26916 | Ravalli EC | res_habit (Yes) | Rate brochure + demand info sheet robots-blocked; residential demand charge implied, not shown |
| 18429 | Tacoma Power | ci_dispatch (Yes) | Cited 2021 Utility Dive pilot had 0 signups; Schedule CP (2025) "subject to curtailment" but closed, no DR program. Lean No |
| 17166 | Sierra Pacific (NVE North) | ci_dispatch (Yes) | Cited BES summary is EE-only; only commercial thermostat DR doc found is Oct 2018 |
| 15419 | Mason County PUD 3 | ci_dispatch (No) | Empty source_url; no rate/DR pages found |

## Source defects (URL fix only)
- 18429 Tacoma ci_dispatch: secondary 2021 news article, replace with utility source.
- 17166 NVE North ci_dispatch: cited PDF contains no DR.
- 3660 Clark res_habit/res_dispatch: URLs attached to wrong cells.
- 26916 Ravalli res_habit: cite PEAK-DEMAND-CHARGE-info-sheet.pdf once readable.
- 15419 Mason PUD 3 ci_dispatch: empty source_url.
- 14371 Paducah Power (KY) is in the West sample: check region assignment.
