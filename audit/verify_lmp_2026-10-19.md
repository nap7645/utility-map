# Verify: LMP layer (Rank 1 layer 2) - 2026-10-19

Independent verifier. Scope: `scripts/lmp_pull.py`, `scripts/lmp_zone_map.py`, `data/processed/lmp_summary.csv`, `data/processed/lmp_zone_map.csv`, `plans/LMP_NOTES.md`, raw cache `data/lmp_cache/`. No data files edited. Scratch work (own code, own downloads): `/tmp/claude-0/-home-claude/d3bb9943-e471-564e-8107-8a9b626f8977/scratchpad/vlmp/` (`recompute.py`, `recompute.csv`, `spot.py`, `spot.csv`, `dl/`).

## Verdict

| Check | Result |
|---|---|
| 1. Independent recompute from raw cache (17 zones, 6 markets, 5 stats) | **PASS** (85/85 within rounding, max abs diff 0.005) |
| 2. Cache vs ISO public source (2 dates x 6 markets, 852 points) | **PASS** (0 missing, max abs diff 0.0) |
| 3. Zone map, 15+ high-customer mappings vs ISO documents | **PASS with 1 FAIL (omission) + 3 note errors** |
| Year / units / day-ahead stated and true | **PASS** |
| LMP_NOTES.md accuracy | **PASS, minor errors** (see the last section) |

## 1. Independent recompute

Method: stdlib `csv`/`gzip`/`zoneinfo` only, no project functions. Read every cache file for the market, dedupe on (zone, ts_utc) keeping the first, convert UTC to the market's `tz`, keep local year 2025, then compute: mean; daily spread = max-min per local calendar day, p90 by linear interpolation; count of price < 0; summer (Jun-Sep) local hour-beginning 17 mean.

| Market | Zones | n_hours | mean | p90_daily_spread | neg_hours | summer_h17 | Result |
|---|---|---|---|---|---|---|---|
| NYISO | A (WEST), J (N.Y.C.), K (LONGIL) | 8760 x3 | match | match | match | match | PASS |
| ISO-NE | .Z.NEMASSBOST, .Z.CONNECTICUT, .H.INTERNAL_HUB | 8760 x3 | match | match | match | match | PASS |
| ERCOT | LZ_NORTH, LZ_HOUSTON, LZ_WEST | 8760 x3 | match | match | match (1/2/220) | match | PASS |
| CAISO | DLAP_PGAE, DLAP_SCE, DLAP_SDGE | 8760 x3 | match | match | match (218/877/748) | match | PASS |
| MISO | ILLINOIS.HUB, MICHIGAN.HUB, MINN.HUB | 8760 x3 | match | match | match (7/0/14) | match | PASS |
| SPP | SPPNORTH_HUB, SPPSOUTH_HUB (only 2 exist) | 8760 x2 | match | match | match (623/729) | match | PASS |

Every zone had 365 local days. All |diff| ≤ 0.005, which is 2-dp rounding. Full table: `recompute.csv`.

Example values (mine = summary): J mean 65.41, p90 spread 100.06, summer h17 90.99; LZ_WEST mean 42.72, neg 220; DLAP_SCE neg 877; MINN.HUB summer h17 72.04.

## 2. Spot-check against ISO public sources

Dates: 2025-03-15 and 2025-08-05. Each source was fetched fresh into `dl/`, parsed with my own code, and converted to UTC hour-beginning before comparing with the cache.

| Market | Source fetched | Zones | Points | Missing in cache | Max abs diff | Result |
|---|---|---|---|---|---|---|
| NYISO | mis.nyiso.com `202503/202508 01damlbmp_zone_csv.zip` (daily CSV inside) | A, J, K | 72+72 | 0 | 0.0 | PASS |
| ISO-NE | iso-ne.com `histRpts/da-lmp/WW_DALMP_ISO_<date>.csv` | NEMA, CT, Hub | 72+72 | 0 | 0.0 | PASS |
| MISO | docs.misoenergy.org `<date>_da_expost_lmp.csv` (HE in EST) | IL, MI, MN hubs | 72+72 | 0 | 0.0 | PASS |
| SPP | portal.spp.org `DA-LMP-SL-<date>0100.csv` (GMTIntervalEnd) | N, S hubs | 48+48 | 0 | 0.0 | PASS |
| CAISO | OASIS `PRC_LMP` DAM v12, separate 1-day queries | PGAE, SCE, SDGE | 72+72 | 0 | 0.0 | PASS |
| ERCOT | ercot.com NP4-180 `DAMLZHBSPP_2025.xlsx` (direct MIS download, not gridstatus) | LZ_NORTH, LZ_HOUSTON, LZ_WEST | 72+72 | 0 | 0.0 | PASS |

This was 11 fetches. Exact matches also confirm the timestamp conventions: NYISO hour-beginning EPT; ISO-NE HE-1; MISO fixed EST (+5h to UTC); SPP GMT hour-ending -1h; CAISO GMT start; ERCOT HE CPT.

**DA confirmation:** every source is the day-ahead product: `damlbmp`, `da-lmp`, `da_expost_lmp` (the final DA settlement LMP), `DA-LMP-SL`, OASIS `market_run_id=DAM`, and ERCOT DAM SPP. No real-time files are used anywhere in `lmp_pull.py`. **Units:** $/MWh in all sources (NYISO labels it "$/MWHr"). **Year:** 2025 local calendar, 8760 h each.

## 3. Zone-map check (largest-customer territories first)

Sources: NYISO Subzone Definition (Apr 2024) [nyiso.com/documents/20142/44209877/Subzone-Definition-041524.pdf]; Con Edison ESCO capacity/energy guidelines 2025 (CECONY is TO for subzones in H, I, J); CAISO Jun-3-2015 Load Granularity compliance filing (4 DLAPs = PG&E, SCE, SDG&E, VEA service areas); ISO-NE maps-and-diagrams page (8 load zones + Hub). For ERCOT, MISO and SPP I did not find a fetchable ISO zone-to-utility table. Those rows rest on domain knowledge and are marked "K".

| # | Utility (customers) | Map zone | Evidence | Verdict |
|---|---|---|---|---|
| 1 | PG&E (5.60M) | DLAP_PGAE-APND | CAISO filing | PASS |
| 2 | SCE (5.22M) | DLAP_SCE-APND | CAISO filing | PASS |
| 3 | Oncor (4.01M) | LZ_NORTH (medium) | K: DFW in North; Permian portion in West | PASS (multi-zone caveat correctly noted) |
| 4 | Con Edison (3.59M) | J (medium) | NYISO subzones: ConEd in G, H, I, J; J dominant | PASS. Note "Westchester is zone I" is incomplete: ConEd also has subzones in H (Millwood) and G |
| 5 | CenterPoint (2.81M) | LZ_HOUSTON | K | PASS |
| 6 | DTE Electric (2.26M) | MICHIGAN.HUB | K (LRZ 7) | PASS (hub, not zone; correctly caveated) |
| 7 | Consumers (1.88M) | MICHIGAN.HUB | K (LRZ 7) | PASS |
| 8 | Niagara Mohawk / National Grid NY (1.71M) | C (low) | NYISO subzones: NMPC in A, B, C, D, E, F | PASS-low. A defensible single default; C as "dominant" is unverified (Buffalo A and Albany F are also large). Low confidence is appropriate |
| 9 | NSP-Minnesota (1.54M) | MINN.HUB | K (LRZ 1) | PASS |
| 10 | Eversource MA / NSTAR (1.51M) | .Z.NEMASSBOST (low) | ISO-NE 8 zones; NSTAR spans NEMA, SEMA (Cape) and WCMA (ex-WMECO) | PASS-low |
| 11 | SDG&E (1.50M) | DLAP_SDGE-APND | CAISO filing | PASS |
| 12 | National Grid MA / Mass Electric (1.35M) | blank | spans WCMA, NEMA, SEMA | PASS (blank is defensible under the never-guess rule; it is a coverage gap for the #12 territory) |
| 13 | CL&P / Eversource CT (1.28M) | .Z.CONNECTICUT | ISO-NE CT zone = state | PASS |
| 14 | Ameren Illinois (1.23M; HIFLD state MO) | ILLINOIS.HUB | K (Illinois Hub is in the Ameren IL area, LRZ 4) | PASS. Name-first matching correctly overrides the HQ state |
| 15 | LIPA (1.15M) | K (LONGIL) | NYISO subzones: LIPA = K | PASS |
| 16 | NYSEG (0.92M) | C (low) | NYISO subzones: NYSEG in A, C, D, E, F, G, H (not B) | PASS-low. The rule note "Spans B-G" is **wrong**: should say A, C-H |
| 17 | Narragansett Electric / RI Energy (0.50M) | **blank** | ISO-NE RI load zone; Narragansett serves only RI | **FAIL (omission).** Should be .Z.RHODEISLAND, high confidence. The LMP_NOTES rationale "serves RI zone plus some MA" is incorrect. No RI row is mapped at all; the RI state default never fires because the name rule matches first and blanks it |
| 18 | ComEd (PJM) | COMED, has_price_data=No | PJM zone | PASS |
| 19 | Entergy LA/AR/MS/TX | LOUISIANA/ARKANSAS/MS/TEXAS.HUB | K | PASS |
| 20 | Central Hudson, O&R | G | NYISO subzones: O&R G; CHG&E E+G | PASS (could be high for O&R) |
| 21 | RG&E | B | NYISO subzones | PASS |
| 22 | AEP Texas Central / North; CPS; Austin | LZ_SOUTH / LZ_WEST / LZ_CPS / LZ_AEN | K | PASS |
| 23 | OG&E, PSO, SWEPCO, SPS / Evergy, OPPD | SPPSOUTH_HUB / SPPNORTH_HUB (low) | K | PASS-low (hub context only, correctly labelled) |

Gaps, not errors: Ameren Missouri (1.25M), WEPCo (1.15M), WPL and WPS (MISO LRZ 2/5, no hub) are blank. Indiana Michigan Power and Mississippi Power are correctly blanked because of presence.json rto errors (I&M is PJM-AEP; Mississippi Power is in the Southern BA, not MISO). These rto errors should be fixed upstream in presence.json.

Integrity: 514 rows, no duplicate eia_id, 383 mapped. Every non-PJM mapped zone exists in lmp_summary (has_price_data=Yes for all of them); PJM 66 rows are No. Per-market counts match the notes.

## LMP_NOTES.md accuracy

| Claim | Check | Result |
|---|---|---|
| 2025, DA hourly only, $/MWh, 49 rows, n_hours 8760 | verified | PASS |
| Hour-of-day local hour-beginning; MISO from fixed EST | verified via spot check | PASS |
| "ERCOT >$500 hours = 4 in DA" | summary shows 4-11 by zone (LZ_LCRA 11; LZ_NORTH, LZ_WEST, HB_WEST, HB_PAN, AEN, CPS, RAYBN 6) | MINOR ERROR: say "4-11" |
| Cache "~10 MB" | 5.8 MB | MINOR |
| Narragansett "serves RI zone plus some MA" | incorrect | ERROR: see row 17 |
| Final bullet ("Hour-of-day in MISO ... fixed EST;") | truncated mid-sentence | MINOR |
| NYSEG "Spans B-G" (script note) | NYISO subzones say A, C-H | ERROR (note only; zone C unaffected) |

## Fixes recommended (not applied)
1. `lmp_zone_map.py`: map NARRAGANSETT to `.Z.RHODEISLAND`, iso_table, high. Keep MASSACHUSETTS ELECTRIC blank.
2. Correct the NYSEG note to "Spans A, C-H" and the ConEd note to "subzones in G, H, I; J dominant".
3. LMP_NOTES: fix the >$500 count, the cache size, the Narragansett rationale, and the truncated last line.
4. Optional: MISO WI/MO rows could take a nearest-hub default (low confidence) if coverage matters more than strictness.
