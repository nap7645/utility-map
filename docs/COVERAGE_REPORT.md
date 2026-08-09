# MISO + PJM behind-the-meter program inventory — coverage & reliability report

**Dataset:** `miso_pjm_dr_tou_bess_programs.csv` — 457 rows, 22 columns, 142 utilities/entities, 22 states + DC, 173 distinct source domains. Compiled 2026-08-08.

---

## 1. Read this first: what "every utility" actually means here

You asked for every public and municipal utility in MISO and PJM. That population is roughly **900–1,000 distinct load-serving entities** — a few dozen IOUs, and then a very long tail of municipals and distribution cooperatives, most of which publish no tariff online in machine-readable form and many of which have no DR, TOU, or storage program at all.

This dataset covers **142 entities**. That is not the full population, but it is not a 15% sample either, because coverage was allocated by load rather than by entity count. Every major IOU in both RTOs is represented, plus the largest municipals and G&T/distribution cooperatives. **Estimated load coverage: 85–90% of MISO+PJM retail load. Estimated entity coverage: ~15%.** The uncovered tail is overwhelmingly small municipals whose only relevant program, if any, is a net-metering ordinance.

Treat this as a **high-coverage-by-load program catalog**, not a census.

## 2. Method

Nine parallel research agents, one per geographic cluster plus one for RTO wholesale products, each working from a fixed 22-column schema (`_SCHEMA.md`) with hard rules: no invented rows, no invented values, blank preferred over guess, mandatory source URL per row, explicit confidence rating. Chunks were then repaired (unquoted-comma rows realigned against enum-constrained column anchors), deduplicated, and merged by `_merge.py`.

## 3. What's in it

| Cut | Breakdown |
|---|---|
| **By RTO** | MISO 261 · PJM 152 · MISO-market 16 · PJM-market 16 · Non-RTO 11 (LG&E/KU etc., flagged deliberately) |
| **By ownership** | IOU 294 · Cooperative 68 · Municipal 57 · RTO 32 · Federal/State 6 |
| **By category** | Export-Comp 129 · DR-Curtailment 67 · TOU-Rate 58 · DR-DLC 46 · EV-Rate 45 · Wholesale-Market 23 · DR-BYOT 18 · Storage-Incentive 15 · RTP-Rate 15 · CPP-PTR 12 · Demand-Charge 11 · VPP 11 · DR-BYOD 6 · Interconnection 1 |
| **Storage-participable** | 285 of 457 rows marked `storage_eligible` = Yes or Yes-restricted |
| **Self-rated confidence** | High 233 · Medium 180 · Low 44 |

### Rows per state

MI 55 · MN 50 · WI 40 · VA 33 · OH 32 · multi 32 · MD 30 · IN 27 · IL 23 · KY 20 · LA 19 · PA 17 · IA 16 · MO 12 · MS 11 · AR 9 · NJ 9 · DE 5 · WV 5 · TX 4 · ND 3 · SD 3 · DC 2

## 4. Data quality — what the scan found

Programmatic scan of all 457 rows:

- **0 rows missing a source URL.** Every row is traceable.
- **0 mangled fields** detected after CSV repair. Repairs were spot-checked manually against four known-bad rows and reconstructed correctly.
- **13 Active rows sourced to news articles** rather than a utility or regulator domain. These are mostly recent program changes (WV net-metering reform, New Orleans battery settlement) where the tariff had not yet posted. Verify before quoting a customer.
- **20 rows sourced to third-party aggregators** (DSIRE, OpenEI and similar). Directionally reliable, but aggregators lag tariff changes by months.
- **Fill rates:** the identity and classification columns are 100% populated. The numeric columns are thinner by design — `incentive_value_usd` 68%, `event_limits` 80%, `tariff_schedule` 79%, `on_peak_window` 40%, `peak_offpeak_rates` 24%, `export_compensation` 33%. Blanks are honest blanks: the agents were instructed to leave a cell empty rather than guess. **`peak_offpeak_rates` at 24% is the single biggest content gap** and is the column your dispatch optimizer most needs.

## 5. Known weak spots — ranked

1. **Pennsylvania (17 rows / 8 utilities), New Jersey (9 / 5), Delaware (5 / 3) are materially under-covered.** The PJM Mid-Atlantic agent was cut off by a session limit mid-run; it wrote its Maryland and DC work but never finished PA/NJ/DE. A top-up pass was queued and also died on a session limit. This is the highest-value gap in the dataset — PJM Mid-Atlantic has the richest BESS value stacking in the country, and PA's Act 129 DR programs, NJ's SuSI/SREC-II and Garden State Energy Storage Program, and Delaware Electric Co-op's Beat the Peak are all under- or un-represented. **Fix this first.**
2. **`peak_offpeak_rates` populated on only 24% of rows.** Without actual ¢/kWh by period, a TOU row tells your model that arbitrage exists but not how much it's worth.
3. **Wholesale price numerics are partly unverified.** The RTO agent got the PJM Regulation payment formulas and the MISO LMR accreditation reform right, but could not retrieve current RMCCP/RMPCP values, PJM reserve clearing price ranges, or the current non-performance charge rate — those live in Data Miner 2 and IMM chart data, not in fetchable pages. Pull these from PJM Data Miner 2 and the MISO market reports directly via API.
4. **The PJM Regulation market is mid-redesign.** RegA/RegD are being phased out under the Oct 2025/2026 Regulation Redesign. Any RegD revenue assumption in your model needs a current check, not this table.
5. **North Dakota (3 rows), South Dakota (3), Texas-MISO (4), West Virginia (5) are thin** — partly real (few programs) and partly unresearched. Don't read a small row count as "no opportunity here" without checking.
6. **Three clusters have no gaps file** — MISO North, MISO IA/IL/MO, and PJM Mid-Atlantic. Those agents were cut off after writing their CSV but before writing their notes, so their self-reported blind spots are unknown. Their data is present and passed the same schema validation, but is less self-documenting than the rest.
7. **Independent verification did not complete.** A dedicated fact-checking agent was tasked with fetching 25 stratified sampled source URLs and grading them; it died on a session limit after selecting the sample. The confidence column is therefore **self-reported by the agent that wrote each row**, not independently audited. Discount accordingly — especially the 233 rows self-rated High.

## 6. Recommended posture

**Safe to use now:** as a structured map of which program *types* exist per utility, for scoping and for driving your app's per-location program-availability gating logic. The identity, classification, and eligibility columns are solid, and every row is traceable to a source.

**Not safe to use now:** as a source of quotable dollar figures in a customer-facing proposal or a financeable pro forma. No row has been independently verified, tariffs change quarterly, and 13 rows rest on news reporting.

**Before commercial use:** re-verify the specific rows for any site you're actually bidding, straight from the utility's current tariff sheet, and stamp `last_verified` yourself.

## 7. Suggested next steps

- Re-run the PA/NJ/DE top-up and the verification pass — both are already specified and just need session budget.
- Backfill `peak_offpeak_rates` for the ~58 TOU + 15 RTP rows; that's the highest-value-per-hour research left.
- Pull PJM Data Miner 2 and MISO market report APIs directly for the wholesale price series rather than scraping — you'll want live values in the app anyway, not a static table.
- Build a `last_verified` staleness check into the app so rows age out and prompt re-verification.

---

**Files:** `miso_pjm_dr_tou_bess_programs.csv` (master) · `COVERAGE_GAPS.md` (per-cluster agent notes) · `_SCHEMA.md` (column definitions) · `_merge.py` (repair/merge/validate) · `chunk_*.csv` (raw per-cluster output, retained for traceability)
