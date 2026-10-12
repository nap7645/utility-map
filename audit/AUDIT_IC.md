# Audit: state interconnection rules (IC)

- **Sample:** `audit/samples/IC.json`, seed **20261002**, 74 items (37 state rows x 2 focus cells: `export_credit_basis` and `grid_charging_allowed`; NY has 2 rows, NY-PSC and LIPA).
- **Auditor:** independent agent, 2026-10-12. Inputs were `audit/RUBRIC.md` and the sample file only. Researcher notes and other audit files were not read.
- **Results:** `audit/results/IC.json`. `idx` is the item's position in the sample's `items` list.

## Method
1. I opened each cited `source_url` fresh with WebFetch and checked the claim against the page text only.
2. A page counts as defective when it was blocked by robots.txt or did not address the cell. For those items I ran one replacement search of a regulator, statute or utility tariff and fetched the best hit, which in a few cases meant a second chunk of the same document. Each case is logged as `SOURCE DEFECT`.
3. Verdict rules:
   - **CONFIRMED:** the page shows the claim as currently in force.
   - **REFUTED:** the page contradicts the claim. The `correct_value` field holds the right value.
   - **INCONCLUSIVE:** neither the cited page nor the replacement shows or contradicts the claim. This includes pages that were readable but silent on the claim.
4. A claim of "Unclear" is CONFIRMED when the source is silent on grid charging.
5. **PARTIAL** in a note means the core basis is confirmed but a secondary sub-clause is not shown on the page. Those sub-clauses are not contradicted. 7 items are PARTIAL.
6. No fetches were done with curl or python. No data files were edited.

## Counts
| Verdict | n |
|---|---|
| CONFIRMED | 59 |
| REFUTED | 3 |
| INCONCLUSIVE | 12 |
| NOT_DONE | 0 |
| **Total** | **74** |

- **CONFIRMED rate, excluding INCONCLUSIVE:** 59/62 = **95.2%**
- **CONFIRMED rate, including INCONCLUSIVE:** 59/74 = **79.7%**
- **Bar:** >=95% (changed from 100% by Nathan 2026-10-12). 59/62 = 95.2% excl. inconclusive: **PASS** on checked cells; the 3 refuted cells are fixed (verify_defectfix_2026-10-12.md). 12 inconclusive remain unchecked.
- **Source defects:** 21 of the cited URLs are blocked or do not address the cell (WI, IA, ND, MI, IN, OH, IL, TX, PA, NJ, DC, NY x2, SC x2, AL, TN, MA, RI, NH, ME). Most of them are interconnection-procedure rules cited for compensation facts. Each one needs `source_url` repointed to the evidence URL in the results file.

## Refuted items (file: `data/processed/interconnection_state.csv`)
| idx | State | Column | Claimed | Proposed fix | Evidence |
|---|---|---|---|---|---|
| 12 | IN | export_credit_basis | avoided cost | `avoided cost x1.25 (EDG: 1.25 x utility's average marginal price of energy, IC 8-1-40)`; repoint source_url to an EDG rider | AES Indiana Rider 16 EDG eff. 2026-07-27 (5.4325 c/kWh) |
| 68 | NH | export_credit_basis | unbundled generation rate | `NEM 2.0: 100% default energy service + 100% transmission + 25% distribution per exported kWh (legacy NEM 1.0: 1:1 retail)`; repoint source_url | NHPUC Order 27074, DE 22-060 (2024-11-18) |
| 70 | VT | export_credit_basis | 1:1 retail | `blended residential rate (Rule 5.127(A)) +/- siting & REC adjustors per production kWh` | PUC Rule 5.100 eff. 2024-03-01, s5.126-5.127 |

## Inconclusive items (logged as defects that need re-sourcing)
| idx | State | Column | Issue |
|---|---|---|---|
| 2 | WI | export_credit_basis | PSC 119 covers interconnection only. No PSC or tariff source was found. |
| 10 | MI | export_credit_basis | Neither R 460.920 nor MCL 460.1177 sets an outflow rate. Cite the DTE and Consumers DG tariffs. |
| 11 | MI | grid_charging_allowed | "Yes" has no support. Downgrade to Unclear unless a tariff or order is cited. |
| 19 | IL | grid_charging_allowed | "Yes-but-not-credited" has no support. P.A. 104-0569 s16-107.5(l-10) net-meters BTM storage on hourly/TOU rates. |
| 33 | NJ | grid_charging_allowed | "Yes-with-conditions" has no support. GSESP is grid-scale. |
| 37 | MD | grid_charging_allowed | The NM report does not mention DRIVE/EDSSS. Cite the PSC order. |
| 41 | VA | grid_charging_allowed | s56-594 is silent on grid charging. |
| 50 | NC | export_credit_basis | The page gives fixed rates of 3.35 and 3.40 c/kWh but does not label the basis as avoided cost. |
| 52 | SC | export_credit_basis | The page uses the "commission determined value" set in the fuel case. Avoided cost is not stated. The cited eTariff URL is blocked. |
| 58 | AL | export_credit_basis | Rider RGB is the wrong document. Rate PAE gives fixed TOD payments and does not label them avoided cost. |
| 72 | ME | export_credit_basis | Ch.324 only cross-references Ch.313. Cite Ch.313. |
| 73 | ME | grid_charging_allowed | The Ch.324 s10 charging-mode form is confirmed. The Docket 2020-00332 advisory-ruling core is not on the page. |

To pass, all 3 refuted cells must be fixed, the 12 inconclusive cells re-sourced, and the 21 defective `source_url` values repointed. A different agent must then re-verify every one of them.
