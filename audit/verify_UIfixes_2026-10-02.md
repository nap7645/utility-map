# Independent verification - 4 UI fixes in docs/index.html
Date: 2026-10-02. Method: python http.server on docs/, Playwright 1.56 + /opt/pw-browsers/chromium (1200x800).
Sandbox deviations: cdnjs Leaflet returned 403, so it was route-intercepted to npm leaflet@1.9.4 (local). OSM tiles aborted (source of "Failed to load resource" console noise). Nominatim not used: `geocode` was overridden via page.evaluate to fixed coords (Houston 29.76,-95.37; nowhere 25,-150). Map clicks were real mouse clicks.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | LG&E/KU rtoOf / color / no 'Non-RTO' | PASS | 10171 and 11249 -> rtoOf "LG&E/KU (non-RTO)"; fillColor #a8c6d9 in RTO view; status+legend contain no "Non-RTO" (status shows "LG&E/KU (non-RTO) 14"); 0 features resolve to 'Non-RTO' |
| 2a | Same query cycles; banner "showing 2 of N" | PASS | Houston x4: 1 of 3 (CenterPoint), 2 of 3 (Entergy), 3 of 3 (San Bernard), 1 of 3 |
| 2b | Different query resets to 1 | FAIL (spec) | Reset keys on the overlap set, not the query. A different query string resolving to the same point continued cycling (query "Other" -> 2 of 3). A different query at a different location does reset (new key). |
| 3 | No-polygon geocode (25,-150) | PASS (minor) | drawer closed, overlap={key:'',hits:[]}, highlighted null, text "...No territory polygon found." Then real map click at Met-Ed (40.497,-76.158): drawer open, n=1. |
| 4 | Coverage text | PASS | "Researched: lower 48 + DC + AK + HI" |
| 5 | Regression | PASS | Houston real clicks cycle 1/2/3/1 of 3; 48/AK/HI buttons move view (AK 63.0,-150 z4; HI 20.56,-157.5 z8; 48 38.06,-95.75 z4); console: only the "Unmatched payload utilities" warning (plus sandbox tile failures) |

## Defects
1. (Spec mismatch, low) Cycle key is the territory set, so a "different query" at the same coordinates does not reset to 1. Same-address re-search (the intended case) works. Fix if needed: store last query alongside key.
2. (Minor) After the no-polygon branch, the closed drawer's #dBody still holds the old ".warn" overlap banner DOM (hidden; state cleared). Cosmetic; clear dBody there.
3. (Observation, pre-existing) With the drawer open at 1200px, the 48/AK/HI buttons are covered by the drawer (Playwright click intercepted; dispatched click worked). Not verified with a real click while open.
4. (Observation) Address-lookup result text always shows "-> hits[0]" even when cycling to another territory.
