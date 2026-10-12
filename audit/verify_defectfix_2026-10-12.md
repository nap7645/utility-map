# Verify: defect-fix pass 2026-10-12

Verifier: independent. Inputs: `audit/fixlog_defects_2026-10-12.json` (272 entries: 210 APPLIED field-edits = 42 defects, 44 ALREADY, 18 SKIPPED) and `audit/results/<REGION>.json`. I did not read the fixer's reasoning beyond the log. I made no edits to data files. Rebuilds ran in a scratch copy.

Caveat on attribution: HEAD (96d3b4e) is behind several uncommitted passes (2026-10-02 fill/link/ownership, plus the earlier 2026-10-12 dollars/auditfixes pass). A diff against HEAD can't isolate this pass on its own. I used file mtimes, both fixlogs, and per-row field diffs to attribute changes.

## Summary

| Item | Verdict | Evidence |
|---|---|---|
| 1a. All 42 APPLIED defects: current value == log `new` | PASS | 210/210 field edits match, in both `data/processed/*` and the mirrored `data/raw/*` rows (row identity checked by line and eia_id) |
| 1b. APPLIED `new` vs auditor `correct_value` | PASS (40/42) | 2 exceptions: SE 72 (FAIL, see 2) and West 18 PSE (FAIL output, see 2). Minor residuals listed below |
| 1c. WebFetch of 13 high-customer / $ entries | PASS 12 / FAIL 1 | See the WebFetch table. Only SE 72's utility attribution is unsupported |
| 1d. Random 15 ALREADY (seed 20261012) | PASS 15/15 | AKHI 38/60/61/63, MISO 6/14/51/57/80, NYISO 6/90, West 10/22/48/99. Current values match correct_value. West 48 (Xcel CO PG) is blanked pending re-pull, not corrected. MISO 51 says "through later of 2024-12-31 or new tariff", which is looser than the auditor's "only through 2024-12-31" (dollars pass) |
| 2a. SE 72 Duke PowerShare re-attribution DEP -> DEC | **FAIL** | Duke release (and theenergymag.com coverage) says only "Duke Energy" in SC and never names Duke Energy Carolinas. DEC and DEP both serve SC. The DEC attribution comes from the auditor's correct_value, not from the page. Name, $120/kW (+$30), $3.50/kW-mo, $0.10/kWh, Aug 2026 operation and "nonresidential" are all supported. The row also still has `eligible_assets=GeneralLoad` and `storage_eligible=Unclear` for a storage-only program |
| 2b. West 118 El Paso Electric NM TOD row | PASS | Page shows TOD: $7/mo, on-peak 3-7pm weekdays Jun-Sep $0.22108, off-peak $0.05527, winter $0.05816, opt-in. Row matches. Residual: `tariff_schedule` still reads "NM Residential Service Rate (Rate 01)" (the standard rate) |
| 2c. MISO 83 NSP-MN Solar*Rewards $ blanked | PASS | Cited billing-guide PDF has no $/kWh incentive and no 20 kW limit (only the $25 credit-payout threshold). Blank is defensible. Residual: `incentive_structure` still says "upfront + production credit + net metering", with confidence=High |
| 2d. Alpena ci_habit Yes -> Unknown | PASS | Page shows only the residential PEV TOU. It mentions a "General Service PEV rate" with no figures. Unknown is better supported than the auditor's "No". presence.json = Unknown |
| 2e. PSE ci_habit Yes -> Unknown | **FAIL (output)** | Sch 324 PDF: "will not be available on or after December 20, 2025", which supports Unknown or No. But PSE has at least 6 active program rows, so build_presence infers "No" for empty cells and a scan "Unknown" can't override it. **presence.json shows `ch=No`, not Unknown** as logged. "No" is within the auditor's "No (or Unknown)", so the substance holds, but the logged value doesn't match the map |
| 3a. CRLF/LF churn, data/processed/*.csv | PASS | All 5 changed processed CSVs keep HEAD's EOL style (all CRLF). Zero EOL-only or quote-only changed lines |
| 3b. CRLF/LF / quoting churn, data/raw | FAIL (attribution uncertain) | `chunk_SE_carolinas.csv`: HEAD was mixed (lines 1-23 LF, 24-50 CRLF), now all CRLF. That is 11 EOL-only lines and 3 quote-only lines. Quote-only churn (csv re-serialisation): chunk_01 13 lines, chunk_02 30, chunk_03 31, chunk_05 8. All of these files have mtime 12:49 (this pass), but earlier uncommitted passes also edited them, so this pass can't be proven the sole cause. chunk_06 (59) and chunk_08 (21) quote churn are from 10-02 (mtime). There is no whole-file EOL flip. `scan_AUDIT.csv` (untracked) is LF while every other scan_*.csv is CRLF |
| 3c. docs/data/*.json parse and match a fresh rebuild | PASS | Ran build_presence.py and build_map_payload.py in a scratch copy. presence.json, programs.json and presence.csv are byte-identical to the working tree |
| 3d. `python3 scripts/audit.py` (offline) | PASS for this pass | A2-A5, A7, A8 PASS. A6 NOT RUN (offline). A1 FAIL: 5 blank `customers` for TX TDUs in hifld_over10k.csv (10-02 edit, not this pass). Note: running it rewrote `audit/AUTOMATED_latest.md` (it is staged as an empty file in the index) |
| 4. presence.json collateral | PASS for this pass; 1 extra from earlier pass | 66 cells differ from HEAD. This pass's 8 expected cells all changed, and PSE's lands on No (see 2e). Earlier-10-12 cells: 12. All other cells trace to presence_scan changes from the 10-02 raw scans (0 unexplained). Zero cells are driven by programs.csv (rebuilt with HEAD programs.csv: identical), so the SE 72 row move changed no presence cell. **Extra:** Black Hills CO `res_dispatch` Yes -> No. The earlier-pass scan_AUDIT row overwrote the original scan row with Unknown in res_habit, res_dispatch and ci_habit. The resulting inferred No is not among that pass's 12 listed cells. United Power's scan row was overwritten the same way (res_habit and res_dispatch set to Unknown), which program-derived Yes hides on the map |

## WebFetch checks (APPLIED, highest customers / $)

| Defect | Page result | Verdict |
|---|---|---|
| CAISO 61 PG&E SmartAC | "currently closed to new enrollments"; "$50 enrollment incentive check" | PASS |
| CAISO 65 SCE SDP | "Summer Discount Plan for Homes", residential forms only; $160, Jun 1-Sep 30 | PASS |
| CAISO 69 SCE Charge Smart | $50 enroll + $50/yr, no 3-yr cap; Gateway Cities; Tesla, ChargePoint, Emporia, Wallbox | PASS |
| MISO 66 DTE CoolCurrents | up to 29% cooling / 25% heat pump; no c/kWh | PASS |
| MISO 83 NSP-MN | no $/kWh, no 20 kW | PASS |
| SE 72 Duke PowerShare Storage | $ values and dates OK; utility not named | FAIL (DEC unsupported) |
| SE 76 Georgia Power DRC-1 | "levelized value of demand reduction derived from the Company's capacity price forecast"; Company-installed; no "100%" | PASS |
| SE 77 Georgia Power pilot | mgrid: PSC approval Jul 2025; $15/kW + $1.50/kWh, $45 LMI, $750/$1,000/kW | PASS (secondary source, confidence=Secondary is correct) |
| SE 96 Alabama Power RTA | 25.0728 / 12.0728 / 10.0728 c/kWh (June 2023 adj.) | PASS |
| NYISO 86 NYSEG OptimizEV | Baseline $25, Advanced $150, rate-diff x off-peak kWh, 80%, $0.032 example | PASS |
| West 118 EPE NM TOD | matches | PASS |
| West 18 PSE Sch 324 | closed on/after 2025-12-20 | PASS on substance (output mismatch, 2e) |
| MISO 33 Alpena | residential PEV only; GS PEV mentioned without figures | PASS |

## Minor residuals (not failures of the logged edit)

- SE 97 EnergyUnited: segment is now non-residential only, but `program_name` still reads "Net Metering (Residential & Non-Residential)".
- SE 103 OUC Battery Rebate: `stackable_with` still asserts TruNet exclusivity, which the updated export_compensation contradicts.
- SE 77: auditor asked for an approval or Georgia Power page as source; the fixer used the auditor's mgrid.org secondary URL.
- Validator `CONF` set in merge_program_chunks.py is {High, Medium, Low}, but SE rows use Primary/Secondary/Unverified. This is pre-existing and not introduced by this pass.
