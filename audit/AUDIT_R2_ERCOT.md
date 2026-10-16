# AUDIT R2 (presence re-audit) — ERCOT
Seed 20261015. Sample: audit/samples_r2/ERCOT.json (20 presence items: 8 Yes, 12 No). Results: audit/results_r2/ERCOT.json. WebFetch/WebSearch only, 2026-10-15.

| Set | n | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Rate incl. inconcl. as fail | Bar | Result |
|---|---|---|---|---|---|---|---|---|
| Yes | 8 | 6 | 1 | 1 | 85.7% (6/7) | 75.0% (6/8) | >=95% | FAIL |
| No | 12 | 11 | 0 | 1 | 100% (11/11) | 91.7% (11/12) | >=90% | PASS |

Inconclusive: Garland P&L res_habit (6958; site fetch errors on cited + replacement page); TNMP res_habit (40051; tariff text lacks Section 6.1 schedules).

## Defects
| eia_id | utility | cell | issue | fix | URL |
|---|---|---|---|---|---|
| 11501 | Magic Valley EC | res_habit | Yes refuted: residential page shows one flat rate ($.091870/kWh + $28.25); /electric-bill/ also flat | set No (or Unknown if bar-graph image is believed to show a TOU) | https://www.magicvalley.coop/residential/ |
| 2442 | Bryan Texas Utilities | res_dispatch | source defect: cited PowerShare page is a bill-donation program | repoint source to https://www.btutilities.com/energy-efficiency/smarthome-programs/ (value No stands) | https://btutilities.com/for-home/powershare-program |
| 8620 | HILCO EC | res_habit | source defect: cited HECRateSheet.pdf has no extractable text | repoint to https://hilco.coop/faq/what-is-a-demand-charge (value No stands) | https://hilco.coop/faq/what-is-a-demand-charge |
| 40051 | TNMP | res_habit | source unverifiable (schedules not in cited PDF) | cite the Chapter 6 rate-schedule document | tnmp.com tariff PDF |

Notes: Medina EC ci_dispatch confirmed on irrigation-only interruptible (ag counted as C&I) — reviewer judgement. Weak No-confirmations (no C&I tariff published on page): Lamar EC, Farmers EC ci_habit.
