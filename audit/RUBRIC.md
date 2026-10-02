# Utility Map audit rubric (one page)

Used by the audit agents and by Nathan. Source of truth for thresholds: `plans/SPEC.md` section 6.2.
Rule: a "No" or "Unknown" is never counted as a miss against the data; a wrong "Yes", a wrong dollar figure, or a wrong join is.

## 0. Run first (2 min, offline)
`python3 scripts/audit.py` : must print PASS on A1-A5, A7, A8. Then, on your own machine (needs internet):
`python3 scripts/audit.py --links` : A6 must show >=95% non-4xx (403/429 are listed separately: likely bot-blocking, spot-check by hand).

## 1. Sampled source re-verification (per region)
Draw a stratified random sample (strata: ownership type IOU / co-op / muni, and customer-size tercile; seeded; write the seed in the report). Open the cited URL fresh; do not read the researcher's notes first.

| Sample | Size | Verdict per item | Pass bar |
|---|---|---|---|
| Presence cells set to **Yes** | ~5% of presence cells, min 20 | Confirmed / Refuted / Inconclusive | >=95% of Yes confirmed |
| Presence cells set to **No** | same draw | Confirmed (found nothing on the utility's own site/tariff) / Refuted (found a program) / Inconclusive | >=90% of No confirmed |
| Program rows | ~10% of rows, min 15 | Name, category, $ value + units, status, URL each correct | 0 wrong $ among the top-10 utilities; log every other error and fix it |
| State interconnection rows | every state: the 2 focus cells (export credit basis, grid-charging) | Confirmed / Refuted | 100%; every error fixed |
| Top-10 utilities by customers (region) | 100% of their program rows and presence cells | as above | 0 wrong $ figures |

Count Inconclusive separately (unreadable site, 403, image-only PDF). Report the rate with and without them. An item is Confirmed only if the page itself shows the claim: a menu label or a marketing line is not enough.

What counts (SCAN_SCHEMA): residential time-based = TOU, RTP, CPP/PTR, residential demand charge, EV TOU. Residential device control = utility/contractor-controlled switch, thermostat, BYOD/battery, VPP. C&I time-based = TOU/RTP/shifting-oriented rate (a plain demand charge on every C&I rate does not count). C&I dispatch = interruptible/curtailable/aggregator DR.

## 2. Live-site check (3 utilities per region: largest IOU, one co-op, one muni)
- [ ] Drawer opens; utility name, state, customers (never -999,999), ownership, governing body correct
- [ ] Program names, $ values, status match `programs.csv`; each source link opens
- [ ] Presence cells (4) match `presence_scan.csv`; scan note shown
- [ ] Overlap click: researched utility first; repeat click cycles; list works
- [ ] Console has no errors; status line shows the expected territory count and snapshot date

## 3. Nathan's spot checks (utilities you know)
Pick 5 per region you can judge from experience: write utility, cell or program, what you believe, what the map says. Anything that disagrees goes to the defect log even if the source link "supports" the map.
- [ ] Your own utility and your parents'/clients' utilities
- [ ] One utility with a program you know was closed or renamed (stale-program check)
- [ ] One co-op whose G&T runs its program (is it attributed to the member correctly?)
- [ ] One retail-choice or non-RTO territory (is the governing-body label right?)

## 4. Record
Per region `audit/AUDIT_<region>.md`: sample seed, tables (item, claimed, verdict, URL), rates vs bars, defect list with exact file/row/cell and the fix. Roll up to `audit/SUMMARY.md` (scores, open defects). A region passes only when every bar is met AND every logged miss is fixed and re-verified by a different agent.
