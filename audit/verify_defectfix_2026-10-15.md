# Verify: INFER_NO rule change + defect fixes (2026-10-15)

Independent verifier. Scope: `scripts/build_presence.py` INFER_NO change; `audit/fixlog_defects_2026-10-15.json` (241 entries: 213 APPLIED, 26 SKIPPED, 2 ALREADY); file integrity. No data files edited; no commit. 24 web fetches used.

**Overall: PASS with 1 FAIL** (raw chunk `chunk_07_pjm_south.csv` line 12, Dominion VA Net Metering, now unparseable by the merge script and its source_url is gone).

## (1) INFER_NO rule

| Item | Result | Evidence |
|---|---|---|
| Only behavioural change in build_presence.py | PASS | `git diff`: adds `INFER_NO = False` and gates the inferred-No branch with `if INFER_NO and ...`, plus a comment. Nothing else changed. |
| Rebuild reproduces committed outputs | PASS | `python3 scripts/build_presence.py` leaves `docs/data/presence.json` and `data/processed/presence.csv` byte-identical (cmp). |
| Count from the rule alone | PASS | HEAD tree with only the new script (git archive into scratch): exactly **102 No->Unknown**, no other cell changes. 29 non-cell field changes: scan-backed "No" cells now show their scan source URL and tier (before, the inferred No had overridden the scan No and left the source blank). The value is still No, so this is expected. |
| Net HEAD -> working tree | PASS | No->Unknown 97 (= 102 - 5 top-utility cells that scan rows turned to Yes); No->Yes 9; Yes->Unknown 5; Yes->No 4; Unknown->Yes 1. All 97 No->Unknown were sourceless (inferred) at HEAD. |
| Yes->other changes explained by fixlog | PASS | All 9 are fixlog scan entries: Niles rd and Wheeling cd go to Unknown; Taylor TX rh/rd/cd go to Unknown; College Station rd goes to No; HECO/HELCO/Maui rh go to No. None are unexplained. |
| Data-driven source-only changes | PASS | 38 cell/source diffs vs the rule-only build. Each one traces to a fixlog scan entry or to a source_url edit in programs.csv that is in the fixlog (AEP Ohio rd, Penn Power ch, PSE&G rh, PSNH rh, CMP rh). |

## (2) Fixlog entries

| Item | Result | Evidence |
|---|---|---|
| programs.csv APPLIED edits (115): value now equals "new" | PASS | Every row was located by line number plus utility/program name. 115/115 match. |
| Raw chunk APPLIED edits (64 non-scan): value equals "new" after the merge script's own repair() | **FAIL (3 entries)** | 61 pass. Fixlog #33-35 target `chunk_07_pjm_south.csv` line 12 (Dominion VA Net Metering, Schedule 1/1G/1S/1T). At HEAD this row already had 23 fields because of an unquoted comma; `merge_program_chunks.repair()` could still rebuild it. The fix wrote by column position into the shifted row. As a result the old export text moved into `storage_eligible`, the original `n/a` was overwritten, and **source_url (`https://www.dominionenergy.com/virginia/renewable-energy-programs/net-metering`) was replaced by `2026-10-15`**, with the old date pushed into the `confidence` slot. repair() now returns None, so the row would be **dropped as "unrepairable"** on the next merge. The processed programs.csv row is correct. Fix: rewrite line 12 as a properly quoted 22-field row copied from programs.csv line 404. |
| programs.csv and chunk edits are paired | PASS (except above) | Each programs.csv edit has a matching chunk edit with the same field and new value. The only mismatch is the Dominion row, where the chunk's "old" values were read from shifted columns. Full-row parity between each edited chunk row and its programs.csv row: identical for every repairable row. |
| scan_AUDIT.csv APPLIED edits (30): value and source match; flows to presence_scan.csv and presence.csv | PASS | 30/30. scan_AUDIT went from 32 to 58 rows (26 added, 0 removed). |
| SKIPPED/ALREADY entries left untouched | PASS | No value changes found for the skipped rows (PSE&G AC cycling 324, PECO 365/367, SPP 980/1000/1014, etc.). |

### Web evidence: presence cells

| Cell | New | Result | Evidence |
|---|---|---|---|
| HECO Oahu / HELCO / Maui res_habit | No | **PASS** (medium-high) | The cited HECO EV-rates page says "Schedules ARD TOU-R, TOU-RI, and TOU EV are no longer open for enrollment" and "Hawaiian Electric currently offers a single rate option, Schedule R". Schedule R is listed for Oahu, Maui, Lanai, Molokai and Hawaii Island. The Shift and Save press release closes it to new enrollments from 2025-02-01, existing customers grandfathered, and "PUC has not yet outlined next steps". A web search found no reopening or replacement TOU announced through Oct 2026. Shift and Save is ARD TOU-R, so it is covered. Residual risk: the page's meta description still mentions "TOU-EV and EV-Rates", which conflicts with the body text. A future PUC-ordered successor TOU would flip these cells. |
| Taylor Electric Coop TX (27369) rh/rd/cd | Unknown | **PASS** | taylorelectric.org belongs to Taylor Electric Cooperative, N1831 State Hwy 13, **Medford, WI**. The TX co-op (Merkel) is taylorelectric.com. The old Yes cells cited the wrong entity, so Unknown is correct pending re-research. |
| PSE&G ch | Yes | PASS (caveat) | BGS Sheet 82: BGS-CIEP energy is "hourly and include PJM Locational Marginal Prices", effective June 1, 2026. The sheets are marked **DRAFT**, so repoint to the final sheet. |
| PECO rh | Yes | PASS (indirect) | peco.com/TOU renders only via JS and returns no content. The greatergrid Flex & Save FAQ says "All PECO residential electric customers are eligible who are not on a Time-of-Use rate", which confirms a TOU rate exists. The audit evidence (PECO PTC PDF) agrees. |
| PECO rd | Yes | PASS | Flex & Save FAQ: "PECO will pause your charging during busy peak hours and shift it", available through 5/31/2031. peco.com/flexandsave is JS-only. |
| AEP Ohio ch | Yes | PASS (partial) | Oct-2026 tariff book table of contents: GS-TOU Sheet 221, effective 4/10/2026, with no "no new customers" label. GS-TOD is "(no new customers)". The text of Sheet 221 itself was not extracted. |
| Dominion VA ch | Yes | PASS | GS-2T is "Intermediate General Service Time of Usage", voluntary, non-residential, 30-500 kW, effective 01-01-25. |
| Owen ch (cd repoint) | Yes | PASS | Schedule I-C Small Commercial TOD and Schedule IIA Large Power TOD. Schedule XV interruptible credit is $6.20/6.90/7.60 per kW-month. |
| NHEC ch | Yes | PASS | Schedule of Rates 2026-02 lists General TDF2/TDN2 and TDF3/TDN3 (<50 kW) time-of-day rates. |
| Victoria rd | Yes | PASS | Beat The Peak: the provider raises the thermostat "up to two degrees higher" during Load Shed events, with an enrollment credit. |
| College Station rd | No | PASS | The page is a $30 purchase rebate only. The only remote control mentioned is by the customer, with no utility control. |
| Custer rh/ch (cd repoint) | Yes | PASS | Residential Rate 01 has $3.75/kW and Rate 21 has $3.25/kW demand charges. Irrigation control classes 31-36. |
| Western Coop rh | Yes | PASS | Residential demand charge is $1.00/kW from 1/1/2026, rising to $2.00 in 2027 and $3.00 in 2028. |
| Wheeling cd | Unknown | PASS | The cited APCo WV page lists no DR/curtailment rider, and its rate text is APCo-only. |
| Niles rd | Unknown | not fetched | The change removes a claim, so it lowers risk. Accepted on the audit evidence. |

### Web evidence: $ changes in top-bucket rows

| Row | Result | Evidence |
|---|---|---|
| ComEd VLR 272: $ blanked, "rate not published" | PASS | The change removes an unsupported generic estimate, so no fetch was needed. |
| AEP Ohio NEMS 354: ~$0.11/kWh blanked | PASS | The change removes an unsourced figure. |
| PSE&G RS-TOU 326 | PASS | compare-rates page: summer 59.9/27.4/10.4 c/kWh, winter 38.5/26.5/10.5 c/kWh, flat RS 29.2 summer / 25.9 winter. Exact match. |
| Dominion Smart Thermostat 399 | PASS | Page: "$25 rebate for signing up, plus an additional $25 rebate each year" and "instant $50 rebate" on marketplace thermostats. |
| Dominion Non-Res Curtailment 400 | PASS | Page: "$36 per kW per year, paid monthly", "at least 100 kW", "10 to 20 times per year". |
| Dominion Off-Peak Plan 407 | PASS | Summer $0.310059/0.151011/0.133130, winter $0.270582/0.155396/0.149173. Exact match. |
| Dominion Net Metering 404 (processed) | PASS (value) | Text-only change, processed row correct. See the FAIL above for the chunk. |
| Austin Power Partner Battery 899 | PASS | $500 per battery (PTO / final inspection on or after 2/18/25). "$75/kW each year based on the maximum device size, backup reserve level, and average ... event hours". ~$324 example. The "$750 headline" part was not verified. |
| CMP A-TOU 865 | PASS | $24.18 service charge, on-peak $0.428836, off-peak $0.061470, no shoulder period, effective 2026-07-01. |
| PSO VCS 984 | PASS | Sheet 69-1: simple average DA LMP for event hours "divided by two", floor $100/MWh. |
| SPS Business TOU 924 | PASS | TX TOU FAQ: Small General $0.062040 + $0.187776 on-peak; Secondary $0.010016 + $0.169056 + $13.75/kW. The FAQ also lists residential TOU. |

## (3) Integrity

| Item | Result | Evidence |
|---|---|---|
| No whole-file line-ending churn | PASS | CR line counts at HEAD and now are the same in every file, CRLF or LF. presence_scan.csv went from 915 to 919 CR lines, which is just the 4 new rows. |
| No whole-file quote churn | PASS | Diffs are limited to edited lines: programs.csv 34/34, chunks 1-6 lines each, presence.csv 99 lines. Edited chunk rows were re-serialized with minimal quoting, which explains the quote-count deltas in chunk_07/NE/TX on those lines only. |
| Pre-existing malformed chunk rows | info | chunk_01 [41,48], chunk_03 [9 rows], chunk_06 [5], chunk_07 [9], chunk_08 [14] have the wrong field count at both HEAD and now. All repair() cleanly except chunk_07:12 (now). |
| docs/data/*.json parse | PASS | presence.json and programs.json load. programs.json contains the new values (e.g. "$36/kW-yr"). |
| `python3 scripts/audit.py` (offline, run on a scratch copy) | PASS | A1-A5, A7, A8 PASS; A6 NOT RUN (links). Output is identical to the committed `audit/AUTOMATED_latest.md`. |
