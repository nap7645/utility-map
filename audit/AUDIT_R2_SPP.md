# AUDIT R2 (presence re-audit) — SPP
Seed 20261015. Sample: audit/samples_r2/SPP.json (20 presence items: 8 Yes, 12 No). Results: audit/results_r2/SPP.json. WebFetch/WebSearch only, 2026-10-15.

| Set | n | Confirmed | Refuted | Inconclusive | Rate excl. inconcl. | Rate incl. inconcl. as fail | Bar | Result |
|---|---|---|---|---|---|---|---|---|
| Yes | 8 | 5 | 1 | 2 | 83.3% (5/6) | 62.5% (5/8) | >=95% | FAIL |
| No | 12 | 12 | 0 | 0 | 100% (12/12) | 100% | >=90% | PASS |

Inconclusive: Pioneer EC (KS) ci_dispatch (15073; robots-disallowed on all pioneerelectric.coop PDFs); Evergy Missouri West res_dispatch (12698; enrollment page captcha-blocked).

## Defects
| eia_id | utility | cell | issue | fix | URL |
|---|---|---|---|---|---|
| 19293 | Southeastern EC (SD) | res_habit | Yes refuted: cited /demand/ page states residential members are not currently charged for demand; Rate 310 is tiered per-kWh, no TOU/CPP/EV | set No | https://southeasternelectric.com/about/rates-policies/ |
| 12698 | Evergy Missouri West | res_dispatch | source defect: cited PSC TOU-implementation deck has no device-control DR | repoint to Evergy MO thermostat T&C (Energy Savings Events) and re-verify open status | https://www.evergy.com/-/media/documents/ways-to-save/discounts/evergy-thermostat-program-terms-and-conditions-mo.pdf |
| 9996 | Kansas City BPU | res_habit | source defect: cited /billing-rates/rates/ lists only C&I classes | repoint to https://www.bpu.com/ForHome/Rates.aspx (value No stands) | https://bpu.com/billing-rates/rates/ |

Notes: Weak No-confirmations (tariff PDFs not readable/not read): Choctaw EC res_habit (Google Drive rate sheet), Prairie Land ci_habit. Norris PPD ci_dispatch confirmed from schedule title "Rate 23 Commercial Interruptible Service" only.
