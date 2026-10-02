# audit.py re-verification 2 (2026-10-02)
Copy: scratchpad/mut2. Baseline: A1 FAIL (5 = Texas denominator rows), all else PASS/NOT RUN. Confirmed.

| Mutation | Result |
|---|---|
| (a) presence_scan cell 'Maybe' | CAUGHT, A1 count 6, lists line 6 eia 20996 |
| (b) extra column in a programs.csv row | CAUGHT, A1 lists "programs line 4: 23 fields, expected 22" but count is 7 not 6 (ragged row also reported again by the DictReader "wrong field count" branch: double count, cosmetic) |
| (c) name whose only polygon is JOIN_EXCLUDE'd | CAUGHT, A3 FAIL. First attempt (Clay Electric, IL) was not a valid mutation: a second FL polygon matches because no (XX) suffix. Valid run: renamed FL polygon 3757 so only excluded 3726 matched -> A3 FAIL, 2 unjoined. |
| (d) programs confidence 'Maybe' | CAUGHT, A1 count 6 |

Link check: `--links --limit 10` runs without crash; 0/10 OK, A6 FAIL, all 10 URLs listed in detail and linkcheck.csv.
Code review (check, a6): no real bugs. Notes: 429 not retried; 403/429 counted as failures in the pass test (reported separately as soft); label says "non-4xx" but test is <400 (unfollowed 3xx would fail).
