# Independent verification - AK/HI + overlap cycling
Date: 2026-10-02. Live: https://nap7645.github.io/utility-map/ (loaded with ?v=20261002a and with no query string; in-app browser 622x696). Repo HEAD 96d3b4e.
Repo docs/data/territories.geojson: 2914 features, AK 65, HI 4, snapshot 2026-09-29 (matches expectation).

Result: PASS on all required checks. 3 minor defects, none blocking.

## Pass/fail

| # | Check | Result | Evidence |
|---|---|---|---|
| 1a | Status line / BOUNDARY_SOURCE | PASS | "2914 territories (snapshot 2026-09-29)"; window.BOUNDARY_SOURCE = "snapshot 2026-09-29" on cache-busted and plain loads |
| 1b | plain vs ?cb= geojson | PASS | Both: 2914 features, AK 65, HI 4, metadata.snapshot 2026-09-29. After STATE_FIX Alaska Power & Telephone (ID 219) is AK, so allFeatures AK=66 |
| 1c | Deployed index.html has fix + jump control | PASS | fetch('data/territories.geojson',{cache:'no-cache'}) present; 48 / AK / HI buttons rendered and working. Prior stale-cache defect (verify_AKHI_2026-09-29 #1) not reproduced |
| 2a | Jump buttons | PASS | 48: centre 38.06,-95.75 z3; AK: 63.0,-150.0 z4, 93 features in view; HI: 20.56,-157.5 z7, all 4 HI features in view |
| 2b | RTO legend | PASS | Legend lists AK-islanded and HI-islanded |
| 2c | AK/HI drawers | PASS | Opened Chugach, AEL&P, AVEC, Ketchikan, Copper Valley (AK); HECO, Kauai IUC (HI); Maui spot-checked. Subtitle shows correct STATE, real customers (Chugach 113,096; HECO 308,485), RTO label AK-/HI-islanded. Program counts match programs.json (Chugach 4, AEL&P 7, HECO 14, Maui 13, KIUC 2, MEA 4). Presence cells match presence.json (e.g. AVEC ch "No", cd "Unknown" shown as "Not yet checked"; KIUC rd/ch Unknown shown "Not yet checked"). Scan notes shown. Un-researched AK utilities show "No program data matched" |
| 2d | No -999,999 / wrong STATE | PASS | No AK/HI feature has negative customers. 12 other features (Oncor, CenterPoint, etc.) carry raw -999999; drawer shows "n/a customers" |
| 3a | Lower-48 overlap, Houston (29.76,-95.37) | PASS | Real clicks: 3 overlap (CenterPoint, Entergy Texas, San Bernard EC). Order researched first, then smaller bbox. Clicks 1-4 cycled CNP, Entergy, San Bernard, back to CNP. Banner "N territories overlap here - showing k of 3" present |
| 3b | Clickable list | PASS | Clicking "SAN BERNARD" link in banner showed it (3 of 3), highlight moved. Next map click went to 1 of 3 |
| 3c | Address lookup | PASS | "Houston, TX" (Nominatim) and "lat,lon" both go through findContaining: CenterPoint first, "Also overlapping" lists the other two, banner shown |
| 3d | AK overlap | PASS | (64.5,-149) 11 overlap; click 1 Golden Valley (researched), click 2 AVEC (presence-only), then unresearched by area. HI: scan of 0.05 deg grid found no overlap in HI (NOT APPLICABLE) |
| 3e | Single-territory click | PASS | Met-Ed at (40.497,-76.158): 2 clicks, n=1, no banner, no cycling |
| 3f | Ocean click | PASS | Real click at (26,-90): no error, no change |
| 4a | 3 random lower-48 drawers | PASS | Con Edison (14 programs), PSCo (13), Gainesville RU (2); counts match programs.json |
| 4b | Console | PASS | No errors. Only the expected warn "Unmatched payload utilities" (1: Muscatine Power and Water, IA) |

## Defects (all minor)

1. Address lookup with no polygon leaves a stale drawer. Repro: search "25,-150" right after a successful lookup. Result text says "No territory polygon found" but the previous utility's drawer and `overlap` state remain. Cause: the `else` branch of the locBtn handler in docs/index.html (~line 831) does not close the drawer or reset `overlap`. Fix: call closeDrawer / set `overlap={key:'',hits:[],i:0}` there.
2. Repeating the same address search does not cycle. The locBtn handler always sets `i:0` (~line 826), unlike selectAt(), which steps when the key matches. Spec says "same path"; this is a small divergence. Fix: reuse selectAt(lat,lon) semantics (compare key before reset).
3. Two features resolve to rtoOf = "Non-RTO" (Kentucky Utilities, LG&E, KY), a label absent from RTO_COLORS, so they render grey and the status line prints "Non-RTO 2". Legend has "LG&E/KU (non-RTO)". Fix in rtoOf() (~line 254): map u.rto 'Non-RTO' for these IDs to 'LG&E/KU (non-RTO)'.

Observations (not defects): AVEC's HIFLD polygon blankets most of AK, so central/west AK points have 8-11 overlaps; cycling works but is long. Panel text still says "AK, HI pending" (index.html ~line 123) although 5 AK and 4 HI utilities are researched.
