# Round-2 presence re-audit: AKHI

Seed 20261015. Sample: audit/samples_r2/AKHI.json (1 items). Auditor: independent r2 agent, 2026-10-15. Method: cited source_url first, one replacement search; WebFetch/WebSearch only.

## Rates

| Claimed | n | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Rate incl. inconcl. (as miss) | Bar | Pass |
|---|---|---|---|---|---|---|---|---|
| Yes | 1 | 1 | 0 | 0 | 100.0% | 100.0% | 95% | PASS |
| No | 0 | - | - | - | n/a | n/a | 90% | n/a |

Note: small n; one miss moves the Yes rate by >10 pts in PJM/NYISO.

## Items

| idx | eia_id | utility | cell | claimed | verdict | correct | evidence |
|---|---|---|---|---|---|---|---|
| 0 | 213 | Alaska Electric Light & Power (AEL&P) | res_habit | Yes | CONFIRMED | Yes | https://www.aelp.com/Energy-Conservation/Electric-Vehicles |

## Defects

Value defects (cell must change):

- none

Source defects (value OK, cited URL does not show the claim; replace source_url):

- none

Inconclusive (needs human / browser check):

- none

## Item notes

- [0] Alaska Electric Light & Power (AEL&P) res_habit: AEL&P off-peak EV rate (10pm-5am, Level II charger), residential and small commercial non-demand customers eligible.
