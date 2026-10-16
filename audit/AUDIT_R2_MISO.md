# Round 2 presence re-audit: MISO

Sample: audit/samples_r2/MISO.json, seed 20261015, 20 items (8 Yes, 12 No). Results: audit/results_r2/MISO.json. Auditor: independent R2 agent, 2026-10-15. Method: WebFetch/WebSearch only, ~2 fetches/item.

## Rates vs bars
| Cell value | n | Confirmed | Refuted | Inconclusive | Rate excl. inconclusive | Rate counting inconclusive as fail | Bar | Result |
|---|---|---|---|---|---|---|---|---|
| Yes | 8 | 5 | 0 | 3 | 100% (5/5) | 62.5% (5/8) | 95% | PASS excl. / FAIL incl. |
| No | 12 | 8 | 3 | 1 | 72.7% (8/11) | 66.7% (8/12) | 90% | **FAIL** |

Inconclusive (4): idx 0, 1, 7 are G&T-run programs (Hoosier LMR, Great River Energy interruptible C&I) where the cited page does not name the member co-op; idx 10 samhouston.net is robots-blocked.

## Defects (value wrong)
| idx | eia_id | Utility | Cell | Fix | Evidence |
|---|---|---|---|---|---|
| 8 | 18895 | Thumb Electric Cooperative | res_habit | No -> Yes (Schedule A-TOD Optional Farm & Home TOD, eff 2025-02-01) | https://www.michigan.gov/mpsc/-/media/Project/Websites/mpsc/consumer/rate-books/electric/thumb/thumbmemberregcur.pdf |
| 12 | 18895 | Thumb Electric Cooperative | ci_habit | No -> Yes (Schedule GS-TOD Optional General TOD) | same as above |
| 16 | 16971 | Shakopee Public Utilities | res_habit | No -> Yes (residential EV Charging Rate, $0.057 10pm-8am / $0.25 other, separate meter) | https://shakopeeutilities.com/residential/ev-charging-2/ |

Note: Thumb rate book also lists CWH (controlled water heater), CAC (controlled central AC) and IEH (interruptible electric heat), so check Thumb res_dispatch too (not in sample).

## Defects (source only, value correct)
| idx | eia_id | Cell | Problem | Replacement URL |
|---|---|---|---|---|
| 3 | 17833 | ci_dispatch | Cited third-party nectarclimate.com | https://www.cityutilities.net/DocumentCenter/View/162/Interruptible-Rates-PDF |
| 4 | 689 | ci_habit | Cited third-party nectarclimate.com | https://connexusenergy.com/download_file/view/d1a05b74-92f4-4884-9682-8e0047752047 |
| 5 | 1009 | res_dispatch | Cited LoadControlFAQ URL returns "page not found" | https://www.austinutilities.com/assetmanager/downloads/June%202026%20Connections%201.pdf |
| 6 | 24949 | ci_dispatch | Cited Minnkota G&T page; no CCEC C&I terms | https://casscountyelectric.com/sites/default/files/documents/2026_june_business-accounts_handbook.pdf |
| 13 | 6342 | ci_habit | Cited June 2023 schedule is stale | https://www.firstelectric.coop/pdfs/Condensed%20Rate%20Schedule%20April%202025.pdf (via nectarclimate; not opened directly) |
| 16 | 16971 | res_habit | Cited 2020 rate PDF is stale | see value defect |
| 0, 7, 1 | 8179, 22822, 10618 | ci_dispatch | G&T page does not name the member co-op; attribution unverified | need member-co-op page or G&T participant list |
| 8, 12 | 18895 | res/ci_habit | tecmi.coop robots-blocked | MPSC rate book above |

Low-depth confirmations (No kept on one rate page + one search): idx 14 Marquette BLP, 18 Kenergy.
