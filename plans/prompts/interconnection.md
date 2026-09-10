# Prompt template — interconnection & export rules (Opus)

Fill `{{...}}` from the region file. Clusters of 3–5 states. This is legal/regulatory nuance;
use Opus.

---

Research state interconnection and net-metering/export rules for a behind-the-meter PV+storage design tool.

READ FIRST: {{repo}}/data/processed/interconnection_SCHEMA.md — two CSV files, exact columns. Follow it precisely. State rules are the floor; the utility file carries only deltas.

CLUSTER {{cluster}} — states: {{states}}.

FILE 1 priorities (one row per state):
{{state_priorities}}

FILE 2 — utility deltas. Cover deviations for:
{{utility_list}}
Copy those utility_name strings EXACTLY — they are join keys into programs.csv. Municipals and co-ops that set their own rules get a row with deviates_on=all. A utility that follows the state rule with no deviation gets NO row.

THE TWO CELLS THAT MATTER MOST: `grid_charging_allowed` (can a battery charge from the grid and still export or earn credit — this decides whether arbitrage is legal) and, in `storage_specific_notes`, whether adding a battery to an existing legacy-net-metered system forfeits grandfathering (this decides most retrofit deals). Expect "Unclear" often; say so explicitly rather than leaving blank — an explicit Unclear is a finding.

REGION GOTCHAS:
{{gotchas}}

WORKFLOW (non-negotiable):
1. Write with Python's `csv.writer`. Header plus first 2 state rows to disk immediately; append as you go.
2. Before reporting done, re-read both files with `csv.reader` and assert 31 fields (state) / 21 fields (utility) on every row.
3. `source_url` mandatory, deep link to the rule, order, or tariff sheet. DSIRE is an index, not a source — use it to find the citation, then read the citation.
4. Flag anything mid-transition with the docket number and expected date.
5. In `confidence`, write the source tier: Primary / Secondary / Unverified.

Write to:
{{repo}}/data/raw/interconnection/ic_{{cluster}}_state.csv
{{repo}}/data/raw/interconnection/ic_{{cluster}}_utility.csv
{{repo}}/data/raw/interconnection/ic_{{cluster}}_gaps.md

Report back only: row counts and what you could not verify. Do not paste the CSVs.
