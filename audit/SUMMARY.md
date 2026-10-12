# Audit summary (partial) - 2026-10-12

Seed 20261002, top-5 per region + SPEC samples. Bars: Yes >=95%, No >=90% (excluding inconclusive), 0 wrong $ in top bucket.
Not yet run: ERCOT, ISO-NE, PJM, SPP, state interconnection (IC). Detail per item: results/<REGION>.json, AUDIT_<REGION>.md. Fix list: DEFECTS.md.

| Region | Items done | Yes confirmed | No confirmed | Program rows | Wrong $ (top) | Status |
|---|---|---|---|---|---|---|
| MISO | 120/120 | 21/23 = 91% (1 inconcl.) | 13/19 = 68% (0 inconcl.) | 62 ok / 12 wrong (3 inconcl.) | 4 | complete |
| West | 121/121 | 25/27 = 93% (0 inconcl.) | 9/12 = 75% (1 inconcl.) | 62 ok / 8 wrong (11 inconcl.) | 6 | complete |
| SE | 105/105 | 23/23 = 100% (10 inconcl.) | 14/16 = 88% (3 inconcl.) | 25 ok / 16 wrong (12 inconcl.) | 1 | complete |
| NYISO | 81/113 | 19/19 = 100% (2 inconcl.) | 0/1 = 0% (0 inconcl.) | 55 ok / 4 wrong (0 inconcl.) | 2 | incomplete |
| AKHI | 54/97 | 8/11 = 73% (0 inconcl.) | 1/1 = 100% (4 inconcl.) | 20 ok / 15 wrong (3 inconcl.) | 15 | incomplete |
| CAISO | 44/97 | 9/9 = 100% (0 inconcl.) | n/a (0 inconcl.) | 27 ok / 7 wrong (1 inconcl.) | 3 | incomplete |

Read: no region meets the bars yet. Biggest pattern: C&I 'No' cells at large IOUs (DTE, Consumers, Ameren MO, LADWP, United Power, Black Hills CO) are often wrong; top-5 program rows carry stale dollar figures (Xcel CO rates, PSE, Consumers, Ameren IL, FPL).
