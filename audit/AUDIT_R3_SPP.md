# Round 3 presence re-audit: SPP

Seed 20261016. Sample: audit/samples_r3/SPP.json (20 presence cells: 8 Yes, 12 No). Results: audit/results_r3/SPP.json. Method: WebFetch/WebSearch only, cited source first, at most one replacement lookup on the utility's own site.

## Counts
| Claimed | Confirmed | Refuted | Inconclusive |
|---|---|---|---|
| Yes (8) | 6 | 0 | 2 |
| No (12) | 12 | 0 | 0 |

## Rates vs bars
- Yes rate (excl. inconclusive): 6/6 = 100% (bar 95%): PASS. With inconclusive counted as misses: 6/8 = 75%.
- No rate (excl. inconclusive): 12/12 = 100% (bar 90%): PASS.

## Inconclusive
- idx 0, 20510 Wheatland EC, ci_habit=Yes: cited GS Time of Day PDF has no text layer; tariff index (https://www.weci.net/tariffs) lists GS TOD and GS Large TOD, but a list label alone does not meet the rubric.
- idx 5, 16267 Rolling Hills EC, res_habit=Yes: rate-study page shows the current residential demand charge as $0.00/kW and a proposed $2/$1 per kW. Adoption (Oct 1 newsletter) could not be verified. If it was not adopted, this is a wrong Yes.

## Defects (no data errors found; source-quality only)
| eia_id | cell | fix | URL |
|---|---|---|---|
| 20510 | ci_habit | Replace the image-only PDF citation with a text tariff or rate page; re-verify | https://www.weci.net/tariffs |
| 16267 | res_habit | Confirm the residential demand charge is in effect (rate matrix / Oct newsletter); set to No if it is still $0 | https://www.rollinghills.coop/2025-rate-study |
| 19293 | res_dispatch | Cite the rates page (Rate 310 controlled water-heater credit), not the generic load-control page | https://southeasternelectric.com/about/rates-policies/ |
| 20927 | res_habit | Cited FAQ has no rates; cite the Rates & Fees page | https://www.wcec.org/your-account/rates-line-extension-charges/ |

Notes: 12524 ci_dispatch is confirmed on an irrigation-only load-control tariff (counts as ag C&I). Confirmations for 20476, 6198 and 27238 rest on index pages without opening the tariff PDFs (moderate confidence).
