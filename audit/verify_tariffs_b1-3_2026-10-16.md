# Verify: Phase B tariff batches 1-3 (2026-10-16)

Independent check of `data/raw/tariffs/b{1,2,3}_{tariffs,periods}.csv` against `plans/TARIFF_SCHEMA.md` and each row's `source_url`. 10 fetches. No data edited.

## Structural checks (all rows, all three batches)

| Check | b1 | b2 | b3 |
|---|---|---|---|
| tariffs header == pilot_tariffs.csv (21 cols, same order) | PASS | PASS | PASS |
| periods header == pilot_periods.csv (10 cols, same order) | PASS | PASS | PASS |
| Every row has header column count | PASS | PASS | PASS |
| 12x24 coverage, tier 0, each schedule x day_type, exactly once | PASS (40/40 groups) | PASS (38/38) | PASS (36/36) |
| Both day_types present for every schedule with periods | PASS | PASS | PASS |
| Orphan period rows (no tariff row) | none | none | none |
| Tariff rows with no period rows | CEI Rate GS (logged) | none | GMP Rate 11, O&R SC1 TOU (logged) |
| "Same period id = same price" (per period+tier) | **FAIL**: DESC Rate 8 and Rate 9 reuse period 0 for summer and winter but tier-1 price differs (Rate 8: 0.17442 May-Sep vs 0.15253 Oct-Apr). Winter rows should be period 1. | PASS | PASS |

## Sample: 8 schedules, field accuracy against source

| # | Batch | Schedule | Fixed | Energy rates | Periods / hours | Tiers | Demand | Eff. date | Composition note | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | b1 | Tampa Electric RS (18454) | PASS $0.45/day | PASS 0.08948 / 0.09948 | PASS flat | PASS 1000 kWh | PASS none | PASS 2026-01-01 (34th Rev. Sheet 6.030) | PASS base only; insert all-in 15.897/17.897c and fuel 3.210/4.210c confirmed (base 8.948 + 0.621 clause = insert energy 9.569c) | PASS |
| 2 | b1 | Appalachian Power VA R.S. (733) | PASS $7.96/mo; min = BSC | PASS 0.07622 = 3.794 gen + 3.828 dist | PASS flat | PASS none | PASS none | PASS 2025-01-01, PUR-2024-00024 | PASS bundled gen+dist, riders excluded | PASS |
| 3 | b1 | Dominion Energy SC Rate 8 (17539) | PASS $0.36164/day (label missing on source; positional mapping consistent) | PASS 0.15878; 0.17442 May-Sep; 0.15253 Oct-Apr | PASS seasons May-Sep / Oct-Apr | PASS 800 (threshold text blank on extraction; "First 800 kWh" label present) | PASS none | PASS 2026-07-01, Order 2026-374 | PASS fuel 3.949c, DSM, storm, pension embedded; $1/mo DER charge excluded from fixed and noted | PASS values; **FAIL schema** (period id reuse, above) |
| 4 | b2 | Entergy Arkansas RS (814) | PASS $8.40; min 8.40 | PASS 0.07392/0.09593 Jun-Sep; 0.06990/0.05154 Oct-May | PASS | PASS 1500 / 1000 | PASS none | PASS 2019-02-01, Docket 18-073-TF | PASS base only; ECRF and Sched 17 riders excluded | PASS |
| 5 | b2 | PSO RSTOD (15474) | PASS $17.00; min 17.00 | PASS 0.248475 on / 0.051016 off; winter 0.079241/0.052529/0.035221 | PASS Jun-Oct wkdy 14-19; holidays not coded (noted) | PASS 475 / 1250 cum. | PASS none | PASS 2025-01-30 | PASS bundled; FCA + Tax Adj riders excluded. Note's "parse ambiguity" is unnecessary: source lists the tiers under the Off-Peak Season heading | PASS |
| 6 | b2 | NIPSCO Rate 611 (13756) | PASS $14.00 | PASS $0.205000/kWh, single rate all kWh, confirmed on Second Revised Sheet 48 | PASS flat | PASS none | PASS none | PASS 2026-03-01 | PASS bundled base; Appendix A riders excluded. High price is genuine as printed, not a capture error | PASS |
| 7 | b3 | Green Mountain Power Rate 1 (7601) | PASS $0.673/day | PASS 0.23066 | PASS flat | PASS none | PASS none | PASS bills on/after 2026-10-01 | PASS bundled; "subject to adjustment"; 7,600 kWh limit correct | PASS |
| 8 | b3 | Potomac Edison R-TOU MD (15263) | PASS $6.00/mo | PASS 0.17007/0.10007 summer; 0.16392/0.09392 non-summer (= dist 0.02787/0.01787 + trans 0.00396 + SOS) | **FAIL (minor)**: peak is fixed 4-9pm EDT. March is coded 15-20, but EDT starts the 2nd Sunday of March, so most of March (about 3 weeks) should be 16-21 local. Nov 15-20 is correct (EST from 1st Sunday). Correct coding: Mar-Oct 16-21, Nov-Feb 15-20 | PASS none | PASS none | PASS 2026-06-01 (SOS filing) | PASS dist+trans+SOS summed; SOS admin charge excluded and noted. Non-summer SOS is the Oct 2026-May 2027 vintage, also applied to Jan-May; the Apr 20-May 31 2026 values (0.12806/0.06806) are superseded, so this is acceptable | FAIL minor (hours) |

## Field accuracy summary

- 8 schedules x 7 value fields = 56 field checks. 55 PASS, 1 FAIL (Potomac Edison R-TOU March hours).
- No dollar-value errors found. All fixed charges, energy rates, tier boundaries and effective dates match the source documents.
- Every composition statement (bundled / base-only / delivery+supply sum) matches its source.
- Schema defect: DESC Rate 8 and Rate 9 reuse period id 0 for different winter tier-1 prices (b1). Fix by setting the Oct-Apr rows to period 1.

## Fixes recommended (not applied)
1. b3_periods 15263 R-TOU: move Mar from the 15-20 block to the 16-21 block, so it reads Mar-Oct 16-21 and Nov-Feb 15-20.
2. b1_periods 17539 Rate 8 and Rate 9: set the Oct-Apr rows to period 1.
3. Optional: drop the "parse ambiguity" wording from the PSO RSTOD note.
