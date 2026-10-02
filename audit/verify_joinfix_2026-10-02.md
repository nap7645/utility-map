# Verify: JOIN_EXCLUDE / Other-nonRTO / lookup text (2026-10-02)
Method: Playwright + /opt/pw-browsers/chromium; Leaflet routed to local npm 1.9.4 (CDN not used); tiles aborted; geocode stubbed (Houston 29.76,-95.37, Nominatim not used). HEAD version served on a second port for before/after rtoOf over all 2914 features.

| # | Check | Result |
|---|---|---|
| 1a | 11788 CONSUMERS ENERGY (IA): programs | PASS: 0 programs, drawer "No program data matched"; RTO MISO (from HIFLD BA, not 4254's row), owner Cooperative (HIFLD); no market-products section. Old: 7 programs, IOU. |
| 1b | 3726 CLAY ELECTRIC COOP INC (IL) | PASS: 0 programs, RTO MISO (was FRCC-nonRTO), owner Unknown; "no program data" drawer |
| 1c | 4254 / 3757 still joined | PASS: 4254 = 7 programs, MISO, IOU; 3757 = 2 programs, FRCC-nonRTO, Cooperative |
| 1d | 9726 JCP&L, 12390 Met-Ed | PASS: 2 programs each, PJM |
| 2a | 5609 label/color/legend | PASS: 'Other-nonRTO', fill #c9d1b0, legend entry present (rgb(201,209,176)) |
| 2b | rtoOf diff HEAD vs new (all 2914) | 4 diffs: 5609 OTHER->Other-nonRTO (expected); 3726 FRCC-nonRTO->MISO (expected, exclusion); 10171 KENTUCKY UTILITIES and 11249 LOUISVILLE G&E: 'Non-RTO' -> 'LG&E/KU (non-RTO)' (NOT in the expected list; see note) |
| 3 | Address lookup text (Houston, 4 Finds) | PASS: Find1 names CENTERPOINT (matches drawer); Find2 "-> ENTERGY TEXAS" drawer matches, Also = CenterPoint + San Bernard; Find3 San Bernard, Find4 wraps to CenterPoint; current never listed in "Also overlapping" |
| 4 | Console | PASS: no pageerror; only net::ERR_FAILED from intentionally aborted tile/font requests (same in HEAD) |

## Notes / defects
- No functional defects.
- Unexpected but benign: 10171/11249 presence rto is 'Non-RTO'; old code returned the literal 'Non-RTO' (a label absent from RTO_COLORS, so grey/unlisted), new guard skips it and falls to BA_MAP -> 'LG&E/KU (non-RTO)' (colored, in legend). Improvement, but a label change beyond the stated expectation; no program/presence-derived real RTO changed.
- 3726 now shows MISO for an Illinois co-op named Clay Electric via HIFLD control area; unresearched, so unverified either way.
