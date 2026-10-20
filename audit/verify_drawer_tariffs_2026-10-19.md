# Verify: drawer "Bill structure" / "Wholesale price shape" (2026-10-19)

Method: headless Chromium (harness copy at scratchpad/vdr/run.js), docs/ served on :8771, drawer opened via openDrawer() at 1300px and 390px; DOM text compared with an independent pandas re-derivation from data/processed/*.csv and data/raw/tariffs/riders_*.csv. Raw output: scratchpad/vdr/res_1300.json, res_390.json.

Note: ConEd is EIA 4226, not 4214. 4214 has no feature, no TAR entry and no CSV rows (nothing renders; correct). Tested 4226. Co-op tested: 12377 Midwest Energy Coop (MI; EIA + LMP hub only, no schedules).

## Results

| # | Check | Result |
|---|-------|--------|
| 1 | Drawer renders, no page errors (8 territories, 2 widths) | PASS (0 pageerror; only aborted external tile fetches in console) |
| 2 | Values == source: fixed charge, energy min-max, effective date, default flag, row count/order, EIA averages + delivery + dyn chips, LMP mean/spread/p90/neg hours, sparkline y-axis min/max | PASS for all 8 (0 mismatches). Caveat: "energy min-max" matches source only for tier 0 (D2) |
| 3a | Peak windows intraday-only | PASS: 338 payload schedules with pk, 0 whole-day (0-24) windows, 0 windows not at the max weekday price |
| 3b | TOU -> Seasonal/Flat relabel | FAIL for same-name schedules (D1); correct elsewhere (SCE, Ameren, Tampa, ConEd checked) |
| 4 | Riders: only ALL/ALL-RES or first residential schedule's, no dupes | PASS (Oncor, Ameren: ALL-RES only; Tampa: RS only; "(...)" placeholder rows dropped; SCE "(none: included)" dropped; no duplicates). Minor D5/D6 |
| 5 | Sparkline draws two paths | PASS (2 paths for ConEd, co-op, Narragansett, PG&E, SCE, Oncor); 0 svg for Ameren MO and Tampa, correct (no LMP zone in lmp_zone_map) |
| 6 | 390px layout | PASS: table fits, no table overflow; screenshots scratchpad/vdr/m_19436.png, m_14328.png. A ConEd dBody scrollWidth-clientWidth of 104px was seen once but no overflowing element reproduced |

## Defects

D1 (HIGH) Same-name schedules merged. Periods are joined on (eia_id, rate_schedule name), not urdb_label. 170 core schedules / 31 utilities have 2+ URDB labels under one name (Narragansett A-16, A-60, G-02, C-06; 1167, 11171, 13998, 15477, ...). Effects: (a) each is listed twice with identical text; (b) price ranges mix both labels (Narragansett A-16 shows 14.1-24.1c, really 24.142c in one label and 14.074c in the other; 1167 Sched R shows 6.2-22.9c for both a "Seasonal" and a "Flat" row); (c) the intraday test sees two prices in one month-group, so all-day schedules keep "TOU" (11171, 13998, 15477: "TOU", no peak; 57 TOU rows with empty peak payload-wide).
Fix: in build_tariff_payload.py select periods by `per.urdb_label == r.urdb_label` (tier "0") instead of by name; then drop duplicates on (rate_schedule, fx, lo, hi, pk) or suffix the label.

D2 (MEDIUM) Energy shows tier 0 only. PG&E E-1 shows 32.6c (tier 1 is 40.7c; EIA avg 39.6c), SCE Tiered D 30c (tier 1 39c), ConEd SC-1 [NYC] 18.1c (summer >250 kWh 20.5c), Ameren Anytime hides 7.14c above 750 kWh. Footnote says "base per-kWh charges" without disclosing the tier cut.
Fix: min/max over all tiers, or add a "tiered, tier 1+: x" tag when tier>0 rows exist.

D3 (MEDIUM) 8-row cap sorted alphabetically hides useful schedules. PG&E (65 core schedules) shows only 8 "E-1 ... Region/All Electric" rows, all 32.6c; E-TOU-C, EV2 etc. never appear although the EIA chip says "TOU, CPP". 76 territories are truncated at 8.
Fix: collapse near-identical names (strip " Region X" / "(All Electric Service)") before head(8), rank TOU/EV/default first, and add a "+N more" line.

D4 (LOW) 65 territories have eia == {} (EIA row with no values), e.g. Oncor 44372: the "Averages = revenue / sales" footnote renders with no chips.
Fix: set out[eid]["eia"] only when non-empty, or guard on Object.keys(t.eia).length in billHTML.

D5 (LOW) Rider name truncated at 50 chars: Ameren "Rider SUR (securitized utility tariff, Rush Island" loses ")". Fix: raise to 70 or cut at word boundary.

D6 (LOW) Riders line follows a table that also lists commercial schedules (Tampa, Ameren), but riders are residential-only. Fix: label "Riders (residential):".

D7 (INFO) Ameren 1(M) Residential Anytime (10.6-15.6c) is seasonal but labelled "Flat": relabel only handles source TOU. Fix: apply the Seasonal relabel to Flat when len(prices)>1 and not intraday.

## Re-check (after fixes to D1-D6), same 8 territories

Same harness and independent pandas comparison (every displayed row matched to a source urdb_label: fixed, effective date, all-tier min-max; EIA chips and LMP chips re-compared; DOM dumps scratchpad/vdr/re_1300.json, re_390.json, screenshots n_19436.png, n_14328.png).

| Check | Result |
|---|---|
| 1 No page errors, 8 territories x 1300/390px | PASS |
| 2 Values == source (fixed, energy all-tier range, eff. date, default flag, EIA, LMP mean/spread/p90/neg, sparkline axis) | PASS (0 mismatches; 1 apparent miss was a double space in a PG&E name collapsed by the DOM) |
| 3a Peak text intraday-only | PASS (0 whole-day windows in 1099 schedules) |
| 3b Relabel TOU->Seasonal/Flat, Flat->Seasonal | PASS (Ameren Anytime and SGS Standard now "Seasonal"; SCE/Tampa/PG&E unchanged and correct) |
| 4 Riders ALL/ALL-RES or first residential schedule's, no dupes, labelled "(residential)", 70-char names | PASS (Ameren SUR name now complete) |
| 5 Sparkline two paths | PASS (2 paths where LMP exists; 0 svg for Ameren MO, Tampa as expected) |
| 6 390px layout | PASS (no table overflow) |
| D1 duplicate-name merge | FIXED: 0 payload territories with duplicate names; Narragansett A-16 shows 24.1c (default label), A-60 13.8c, no mixed ranges |
| D2 tiers | FIXED: PG&E E-1 32.6-40.7c "Flat tiered", SCE Tiered D 30-39c, Ameren Anytime 7.1-15.6c |
| D3 cap/order | FIXED: PG&E now E-1, E-ELEC, E-TOU-C/D, EV, EV2 before A-1; Region/All-Electric variants collapsed |
| D4 orphan EIA footnote | FIXED (Oncor: none) |

Remaining (LOW, non-blocking):
- R1: Peak text lists contiguous equal-price windows separately (PG&E A-1 TOU: "May-Oct 08-12,18-21; May-Oct 12-18" = 08-21). Fix: merge adjacent hour ranges per month-group.
- R2: Peak is computed from tier-0 rows but the range now spans all tiers; 13 TOU schedules have no peak (e.g. 14063 R-VPP 3.96-41.78c, 14006 RS-TOD, 20151). Fix: compute peak over all tiers, or omit "TOU" label's peak blank by design and note it.
- R3: ConEd Rate III shows a 16h "peak" (Jun-Sep 08-24) because the max price covers all non-night hours; correct per source, just wide.
