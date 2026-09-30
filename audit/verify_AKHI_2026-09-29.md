# Independent verification - AK/HI push
Date: 2026-09-29. Live: https://nap7645.github.io/utility-map/?v=20260929z1 and ?v=20260929z2 (in-app browser, 646x696)

Result: NOT DEPLOYED as served to the page. Checks 1-4 not run, per instruction to stop.

## Pass/fail

| Check | Result | Evidence |
|---|---|---|
| Deployment | FAIL | Status line "2845 territories (snapshot 2026-09-28)"; window.BOUNDARY_SOURCE = "snapshot 2026-09-28"; features with STATE=AK: 1 (only Alaska Power & Telephone via STATE_FIX), HI: 0. Same on two fresh page loads. |
| Page code is new | PASS | Deployed JS has "48/AK/HI" jump control, AK/HI in STATES, 'AK-islanded'/'HI-islanded' in RTO_COLORS, STATE_FIX {20404,3278,56146,219}. Buttons render (48, AK, HI) under zoom. |
| Data file is new | PASS (with cache-buster) | fetch('data/territories.geojson?y=<ts>') returns 2914 features, snapshot 2026-09-29, AK 65, HI 4. Plain fetch('data/territories.geojson') returns 2845 / 2026-09-28. |
| 1-4 (map view, drawers, regression, console) | NOT RUN | blocked by deployment failure |

## Defects

1. Stale territories.geojson served to the page. Plain URL returns the 2026-09-28 snapshot while the same URL with any query string returns 2026-09-29. Cause is HTTP/CDN cache on the plain URL (GitHub Pages max-age=600, and my forced reload did not fix it on the next load). The page fetches `fetch('data/territories.geojson')` with no cache control, so returning users see old data with new code (AK/HI buttons that zoom to empty ocean). Fix in index.html load(): `fetch('data/territories.geojson?v='+(window.SNAP||'20260929'))` (bump per snapshot), or `{cache:'no-cache'}` as already done for programs.json and presence.json. Then re-run this verification after cache clears.
2. Side effect of (1): while stale, only 1 AK-islanded feature exists and 0 HI, so the legend and status line cannot show HI-islanded.
