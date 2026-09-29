# Independent verification - SPP + West push
Date: 2026-09-28. Live: https://nap7645.github.io/utility-map/?v=20260928a (in-app browser, 646x696 viewport)

Deployed check: status line "2845 territories (snapshot 2026-09-28)"; 2845 layers; STATE values include OK/KS/NE. Deployed.

## Pass/fail

| Check | Result | Evidence |
|---|---|---|
| Snapshot live | PASS | 2845 territories, OK/KS/NE present |
| 1a. Coverage counts | PASS w/ flags | see table below |
| 1b. rtoOf values in legend | PASS | 0 values outside RTO_COLORS keys (note: rtoOf takes the props object; rtoOf(14063) by id returns OTHER, rtoOf(props) returns SPP) |
| 1c. Large (>10k) territories without PRES | PASS | 0 in the 13 states (PRES has 983 entries; hifld_over10k.csv has 983 rows) |
| 1d. RTO assignments plausible | FAIL (minor) | SWEPCO shown MISO (should be SPP), Kiamichi shown AECI (Western Farmers, SPP), 5 MT co-ops MISO, others - defects 2, 3 |
| 2. Drawers, 17 utilities | PASS on content, 3 defects | All 16 researched utilities: program count, Homes/Business x Time-based/Device-control flags and "matched as" name match presence.csv / programs.csv exactly (program counts 8,11,8,12,6,13,12,10,8,23,7,11,7,6,9,6). 17603 shows "Not yet checked" x4 and no program list, with reset note. No wrong-utility matches |
| 2. "-999,999 customers" fix | PASS | Badger 1572, WPPI 20858, Wolverine 20910, East Kentucky 5580 all read "n/a customers". No -999,999 in drawer subtitle |
| 2. Note: line under table | PASS | Present for all 17 utilities (17603 shows reset note) |
| 3. Visual RTO/ISO mode | PASS w/ flags | West brown WECC-nonRTO, Plains tan SPP, AECI beige NE OK, no wrong colors in AZ/UT/CO/NM/OR/WA; legend matches 15 RTO_COLORS keys |
| 3. Visual Program count mode | PASS | Legend (10+, 6-9, 3-5, 1-2, has programs not itemized, none found, not researched, outside) matches; only 158 of 749 features in the 13 states are shaded (rest grey "not researched"), as expected |
| 3. Uncolored gaps | PASS | Grid test (0.25 deg, point-in-polygon over all 2845 features): interior gaps only in central ID/W MT wilderness, NV-ID border (lat 40.5-42.75, lng -117.5 to -115.5), NW NV (41.25-41.75, -119.5), Yellowstone/Teton/Bob Marshall, INL (43-43.75, -113 to -111.75), Mt Hood. Unverified slivers: 46.5N -111.25 to -110 (central MT), 36.75N -99 (OK), 42.75N -99.25 (NE), 33.25N -108.25 (NM Gila), 39.75N -120 |
| 4. Console errors | PASS | none |
| 4. Load time | PASS | DOMContentLoaded 219 ms, load 581 ms |

### Coverage (feature count / rtoOf breakdown by feature STATE)
| State | n | rtoOf |
|---|---|---|
| OK | 92 | SPP 78, AECI 9, WECC-nonRTO 2, MISO 1, ERCOT 2 |
| KS | 145 | SPP 144, MISO 1 |
| NE | 151 | SPP 135, WECC-nonRTO 16 |
| WA | 58 | WECC-nonRTO 57, OTHER 1 |
| OR | 37 | WECC-nonRTO 37 |
| ID | 26 | WECC-nonRTO 26 |
| MT | 27 | WECC-nonRTO 20, MISO 5, SPP 2 |
| WY | 21 | WECC-nonRTO 21 |
| CO | 52 | WECC-nonRTO 51, SPP 1 |
| UT | 44 | WECC-nonRTO 44 |
| NV | 13 | WECC-nonRTO 13 |
| AZ | 39 | WECC-nonRTO 39 |
| NM | 23 | WECC-nonRTO 19, SPP 4 |

## Defects and exact fixes

1. Wrong STATE on two features (data). AEP Texas North (20404) and AEP Texas Central (3278) carry STATE=OK, CUSTOMERS=-999999, but centroids are in Texas (31.86,-101.70 and 28.06,-98.63). They inflate the OK count (2 ERCOT features in OK) and drawers say "OK". Black Hills Colorado Electric (56146) carries STATE=SD but its polygon is at 38.25,-104.31 (Pueblo CO); its drawer subtitle reads "SD" and it is missing from the CO count (CO shows 52, should be 53). Fix: add state override for eia ids 20404, 3278 -> TX and 56146 -> CO in the snapshot build (or override STATE from polygon centroid/state-boundary).

2. SWEPCO (17698) RTO wrong. PRES.rto = MISO, but SWEPCO is in SPP (West zone). Drawer: "OK - 551,152 customers - MISO". Also the customer count is the company-wide total, not OK. Fix: set rto to SPP for 17698 in presence.csv; note state split.

3. Questionable RTO on OK/MT co-ops. Kiamichi Electric (10170) shows AECI, but it is a Western Farmers Electric member (SPP). Also verify Central Rural (3226), East Central OK (5598), Indian Electric (9246). Five MT co-ops (11272 Lower Yellowstone, 11989 McCone, 13749 Norval, 16759 Sheridan, 17593 Southeast) resolve to MISO via the HIFLD CNTRL_AREA fallback in rtoOf(); these are eastern-MT co-ops (Basin/UGP, SPP or WAPA-UGP area), so the teal MISO block in NE Montana is likely wrong. Goldenwest/Grand (MT, 7318/7484) show SPP with no PRES entry (unresearched fallback). Fix: add explicit rto for these ids in presence.csv (or an override map in rtoOf) instead of relying on CNTRL_AREA text.

4. Alaska Power & Telephone (219) is STATE=WA, RTO OTHER (only OTHER in WA). Its territory is Southeast Alaska plus a little WA; render is a large grey polygon in Alaska. Fix: exclude or label as AK; low priority.

5. Stale header/status text. Header still "Researched: MISO - PJM - NYISO - CAISO", page title "MISO + PJM + NYISO (v0.8)", status "MISO 781 - PJM 304 - NYISO 59 - CA 408 - other 1293", and "Programs matched to 243/241 researched utilities" (matched > total, impossible). Fix: update the header/title strings, regenerate the status line counts to include SPP/West, and fix the numerator/denominator in the matched-utilities counter (likely counting matches vs distinct PRES ids with different filters).

6. Zero customers. Waelder (19952) has CUSTOMERS=0 (not covered by the n/a fix, which handles negatives). Fix: treat CUSTOMERS<=0 as n/a in the subtitle formatter.

7. Empty "source" fallback text. Nevada Power (13407) Businesses time-based and PSE (15500) Businesses time-based show "source (utility's own page)" instead of a rate/program name. Cosmetic; fix by populating the ci_habit program name in programs.csv or hiding the fallback when no name exists.

8. PacifiCorp (14354) drawer is labeled OR/2,037,121 customers though it covers 6 states; note explains, but subtitle could say "multi-state". Cosmetic.
