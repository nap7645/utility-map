# Verify: ISO-NE + SPP audit verdicts, A1 customer overrides, link repair, merge_region change (2026-10-12)

Independent verifier. Selection: every top-bucket REFUTED item and every wrong_dollar=true item; 4 CONFIRMED (random.Random(7)); 3 sample-bucket REFUTED (same RNG, continued). One WebFetch per item. No data files edited. Running `scripts/audit.py` regenerated `audit/AUTOMATED_latest.md`.

## 1. Region audit verdicts

| region | idx | item | auditor | verifier | evidence |
|---|---|---|---|---|---|
| ISO-NE | 66 | CMP A-TOU (row 865), wrong $ | REFUTED, cv $24.18/mo, on $0.428836, off $0.061470, 5-9pm M-F, no shoulder | AGREE | cmpco.com/time-of-use-delivery-rate, eff 2026-07-01: exactly cv. Note: the auditor says the URL 404s, but it loaded today. The claimed value is still stale. |
| ISO-NE | 72 | GMP Rate 22 (row 825), wrong $ (also drawn in the sample-REFUTED pick) | REFUTED, cv $0.35949 / $0.15322 / $0.876/day | AGREE | Rate-22 PDF: "bills rendered on or after October 1, 2026", same three values |
| ISO-NE | 46 | Eversource MA ConnectedSolutions thermostat (row 776) | CONFIRMED | AGREE | masssave.com thermostat page: $50 ($100 R-2) + $20/yr |
| ISO-NE | 22 | NHEC 13441 ci_dispatch=No | CONFIRMED | CANNOT_TELL | No evidence_url recorded. nhec.com/rates/ returned a fetch error. |
| ISO-NE | 55 | CL&P RRES Buy-All (row 804) | CONFIRMED | AGREE | Zendesk article: 2026 $0.3289, 2025 $0.3195, income-eligible adder $0.055. The fetch summary did not show the $0.0275 distressed adder (not refuted). |
| ISO-NE | 7 | NGrid MA 11804 ci_dispatch=Yes | CONFIRMED | AGREE | C&I ConnectedSolutions PDF lists National Grid (Daily/Targeted Dispatch) |
| ISO-NE | 81 | Chicopee yard equipment rebate (row 864) | REFUTED (non-$) | AGREE | Page publishes $100 / $40 / $25 (cap 50% of price, purchases in 2026) |
| ISO-NE | 78 | UI RRES Netting (row 805) | REFUTED (citation) | AGREE | Article covers Eversource only and does not mention UI. Netting values match the Eversource values. |
| SPP | 35 | SWEPCO NM/DG interconnection (row 10) | REFUTED (unsupported) | AGREE | swepco.com/company/about/rates/ is a landing page with no NM/DG content. Candidate fix: LA_Tariff_Book_as_of_07-30-26.pdf (DG Rider 33.1-33.9, eff 3/31/2026; NM Rider closed), from the link-repair check. |
| SPP | 38 | SPS Business TOU (row 924) | REFUTED, cv Small Gen $0.062040 + $0.187776 on-peak etc. | AGREE | TX TOU FAQ: SG $0.062040 + $0.187776; SecG $0.010016 + $0.169056; on-peak 1-7pm M-F Jun-Sep |
| SPP | 49 | PSO RS (row 980) tagged TOU-Rate | REFUTED (category) | AGREE | PDF: seasonal block rate, not TOU ($17; 8.8792c/11.4186c, 1,350 kWh). TOU is the separate RSTOD schedule. |
| SPP | 53 | PSO VCS (row 984), wrong $ | REFUTED, cv: day-ahead LMP average divided by two, $100/MWh floor | AGREE | Sheet 69-1 verbatim "...divided by two"; floor $100/MWh; >$200/MWh for 2+ hours trigger; notice by 4pm; 1,000 kW minimum |
| SPP | 25 | Custer PPD 4671 ci_dispatch=Yes | CONFIRMED | AGREE | Rate summary p1: irrigation control classes 31/32/33/36 at discounted rates |
| SPP | 9 | PSO 15474 ci_dispatch=Yes | CONFIRMED | AGREE | Peak Performers: "Businesses of all sizes", $32/avg kW |
| SPP | 31 | LREC 10599 res_dispatch=No | CONFIRMED | AGREE | Rates page: flat residential rate; TOU only on Large General Service; no residential DR |
| SPP | 57 | PSO Charge Choice (row 988) | CONFIRMED | AGREE | $60/yr and $120/yr; WeaveGrid; ready-by time + override |
| SPP | 18 | Custer 4671 res_habit No->Yes | REFUTED, cv Yes | AGREE | Rural Res (01) $3.75/kW and Town Res (21) $3.25/kW demand charges. RUBRIC counts a residential demand charge as time-based. |
| SPP | 66 | Edmond R-1 (row 1000) tagged TOU-Rate | REFUTED (category) | AGREE | Seasonal blocks only, no TOU ($14; 8.51c/9.57c, 1,400 kWh summer; 8.51c/4.85c, 600 kWh winter) |
| SPP | 33 | Custer 4671 ci_habit No->Yes | REFUTED, cv Yes | AGREE | Rate 80-TOU Small General: $130, $10.75/kW, summer on-peak 5-9:59pm 19.943c, off-peak 3.292c |

**Agreement rate**
- ISO-NE: 7/7 decidable items (8 checked, 1 CANNOT_TELL).
- SPP: 11/11.

**Disagreements:** none.

Minor notes:
- ISO-NE 66: the auditor's "cited URL 404" remark is wrong today. The page loads and confirms cv.
- SPP 35: the processed programs.csv row still cites company/about/rates. The 07-30-26 LA tariff book is the obvious replacement.

## 2. A1: ERCOT TDU customer overrides

`data/raw/hifld_over10k.csv` compared with `Delivery_Companies_2024.xlsx` (Part C, Delivery, Data Type O, TOTAL Customers):

| eia_id | utility | hifld_over10k | EIA-861 2024 | match |
|---|---|---|---|---|
| 44372 | Oncor | 4010973 | 4010973 | yes |
| 8901 | CenterPoint | 2811820 | 2811820 | yes |
| 3278 | AEP Texas Central | 916131 | 916131 | yes |
| 20404 | AEP Texas North | 200129 | 200129 | yes |
| 40051 | TNMP | 277003 | 277003 | yes |

- `data/crosswalk/customer_overrides.md` lists the same five values and source (EIA-861 2024, Part C, Delivery, O, TOTAL). The AEP sum of 1,116,260 is stated correctly.
- `python3 scripts/audit.py`: **A1 PASS, 0 problems.** It also lists 12 info lines for sentinel polygons.
- Residual (info, not a failure): all five TDU polygons in the HIFLD boundary layer still carry CUSTOMERS=-999999. `docs/index.html` reads CUSTOMERS from the polygon, not from hifld_over10k.csv, so the live drawer shows "n/a customers" for Oncor, CenterPoint, AEP TX and TNMP. The override fixes only the denominator. A RUBRIC section-2 "customers" live check on these utilities would fail.

## 3. Link repair (audit/linkrepair_2026-10-12.json)

### SWAPPED (10)

Each new_url was fetched against its cells_or_rows. Each old_url was grepped across `data/`.

| cells_or_rows | new_url supports claim | old_url gone from data/ | note |
|---|---|---|---|
| Entergy Arkansas ic_util | yes | yes | Rate Schedule 71 NLN-M: avoided-cost credit, fees $196.75 / $667.60 / $31.50 |
| 8447 Hendricks res_habit=Yes | yes | yes | Residential on-peak $0.2491 5-8pm, off-peak $0.1083, super off-peak $0.0594 |
| 13955 Ocala res_dispatch=No | yes | yes | Voluntary conservation only, no device control |
| PacifiCorp ID export credit row | yes | yes | Idaho PUC release 11/17/2025, average 4.2c/kWh. The literal-space URL is absent. |
| 691 Anoka res_habit=Yes | yes (weak) | yes | EV-only TOU (separate meter, $0.055 / $0.250). Counts under the RUBRIC "EV TOU". |
| 10331 Kingsport ci_dispatch=Yes | **weak** | yes | Tariff PSEDR exists (non-res, 250 kW min), but it took effect 2012-06-01 with an initial term of 4 delivery years. It is unverified whether it is still open, so the Yes rests on a possibly expired rider. |
| 3400 Chaska res_habit=Yes | yes (narrow) | yes | Residential on/off-peak space-heating and EV rates, on-peak M-F 7a-7p |
| 1050 Azusa ci_habit=Yes | yes | yes | Schedule TOU, mandatory above 200 kW |
| 44372 Oncor res_dispatch=Yes | yes | yes | Residential Load Management via REPs, Jun 1-Sep 30. presence_scan.csv carries the new URL. presence.csv cites the 2026 Residential LM Program Manual (build-derived), which is fine. |
| SWEPCO LA tariff book (chunk_04 NM/DG row) | yes | **NO** | The 07-30-26 book lists NM Rider (closed) 30.1-30.9 and DG Rider 33.1-33.9. The dead `LA_Tariff_Book_as_of_06-01-26.pdf` is still in 3 places (below). |

Where the dead SWEPCO 06-01-26 URL still appears:
- `data/raw/program_chunks/chunk_04_miso_south.csv:33` (LMSOP / Interruptible row)
- `data/processed/programs.csv:85` (same row)
- `data/processed/presence.csv:388` (17698 ci_dispatch_src)

The 07-30-26 book's table of contents has no LMSOP or interruptible schedule. The nearest entries are the Voluntary Curtailment Service Rider (60.1-60.3) and the Supplemental Reserve DR Pilot (69.1-69.4). A plain URL swap therefore would not support the LMSOP row: the row needs re-research or renaming, not just a new link.

**Result: 9/10 swaps clean; 1 incomplete (SWEPCO); 1 weakly supported (Kingsport).**

### EXCEPTION sample (8, random.Random(7))

| cells_or_rows | loads | relevant | note |
|---|---|---|---|
| programs Cleco | yes | yes | Index rev 04/01/2026 lists MVDR, PM, DG, TP |
| 18304 SECO res_habit / ci_dispatch / ic_util | yes | yes | RS-TOU, GSDI interruptible, net metering 16.4, interconnection 17.x |
| programs East River | yes | yes | Load management switches, about 75,500 loads |
| 5535 EECA res_dispatch=No | yes | yes | PPR is a behavioural peak-reduction program ($1/kWh), explicitly "no ... controlling of any devices". Supports No. |
| 5535 EECA res_habit=Yes | yes | yes (weak) | Schedule A-2 test rate: $0.50/kW residential demand charge. The TOU periods are currently priced identically and enrollment is capped at 5 members. |
| programs O&R (x2) | yes | yes | DLRP $3/$5 per kW-mo, CSRP $3, $0.50/kWh, voluntary $1/kWh |
| 13830 Nueces res_habit=No | yes | yes | Residential General Service is flat with no TOU or demand charge. The fetch was truncated at 100k of 113k characters. |
| programs Duke Energy Carolinas (x3) | yes | **mismatch** | The page describes **Duke Energy Progress** NC TOU changes, not DEC. Cited for DEC rows (programs.csv ~671-674). DEC applicability is unverified, so these need a DEC-specific URL. |

**Result: 8/8 load. 7/8 are relevant to their rows. The DEC rows cite a DEP page.**

## 4. scripts/merge_region.py change

The diff appends `scan_AUDIT.csv` after the tag's presence files when `--tag != AUDIT`, the tag matched at least one presence file, and the file exists.

- **No double-append.** The tag regex `^scan_{t}\d*\.csv$` never matches `scan_AUDIT.csv` for other tags (e.g. A gives `scan_A\d*`). The `a.tag != "AUDIT"` guard covers the self case.
- **No duplicate rows.** AUDIT rows whose eia_id is already in presence_scan.csv replace that row in place (`db[pos[k]] = r`) and are never appended. Dry run: +0 new.
- **No dropped rows.** The script only replaces or appends; it never deletes.
- **Edge case (latent, not hit today).** Suppose a tag file introduces a *new* eia_id in the same run and that eia_id also has an AUDIT row. The key is in `seen` but not in `pos`, so the AUDIT row is counted as "already merged" and is not applied. The fix lands only on the next merge.
- **Edge case: AUDIT eia_id absent from presence_scan.csv.** If an AUDIT row's eia_id is not in presence_scan.csv, any tag merge would append it as a new row unrelated to that tag. Not hit today: all 32 AUDIT ids are present.
- **Counter inflation (cosmetic).** The `updated` counter counts the same row twice when a tag file changes it and AUDIT reverts it.
- **Design caveat.** AUDIT rows are full-row overrides. Any later legitimate rescan of those eia_ids (e.g. a new scan_A fill for Black Hills 56146) is silently reverted until scan_AUDIT.csv is edited.

Dry run of `python3 scripts/merge_region.py --tag A`: presence files=[scan_A.csv, scan_AUDIT.csv], +0 new, 4 updated, 89 already merged; programs/ic +0. The md5 of all processed CSVs and of hifld_over10k.csv is unchanged after the run.

Simulating the merge shows the 4 "updates" are 2 rows (56146 Black Hills CO, 2285 Brookings), each overwritten by scan_A and then restored by scan_AUDIT. **Net change to presence_scan.csv: 0 rows.**

Both AUDIT rows are deliberate corrections:
- 56146: ci_dispatch=Yes; the other cells are left to program-derived values.
- 2285: res_dispatch Yes->Unknown.

Net, nothing unintended. Note that scan_A.csv still holds the pre-audit values for both rows.
