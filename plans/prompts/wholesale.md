# Prompt template — RTO wholesale products (Opus)

One agent per RTO. Numbers and formulas matter here more than row count.

---

You are researching WHOLESALE market revenue streams available to behind-the-meter distributed energy resources in {{rto_name}}, for a BTM PV+storage economics engine. Read {{repo}}/data/processed/programs_SCHEMA.md FIRST. Use rto = `{{rto_code}}-market`, state = `multi`, ownership_type = `RTO`, utility_name = `{{rto_legal_name}}`.

Cover each of these as its own row (several rows where sub-products differ):
{{product_list}}

For each row: the money goes in `incentive_value_usd` (most recent clearing prices or payment rates, with the delivery year or month), operational requirements in `event_limits`, the eligibility gate in `enrollment_basis`, and the dual-participation / telemetry / minimum-size rules in `storage_eligible` and `stackable_with`.

STATE OPT-OUTS AND GATES: capture, as their own rows, any state that has opted out of third-party aggregation of retail customers under this RTO's rules, and the Order 2222 implementation status and effective dates. These are hard gates on the whole dispatch bucket.

SOURCES: the RTO's own manuals / business practice manuals, the tariff, market reports, and the Independent Market Monitor's State of the Market report. Cite the manual number and section. Use current values as of {{today}} where available.

REGION GOTCHAS:
{{gotchas}}

WORKFLOW (non-negotiable):
1. Write with Python's `csv.writer`. Header plus first ~8 rows to disk immediately; append as you go.
2. Before reporting done, re-read with `csv.reader` and assert 22 fields per row.
3. Leave a number blank rather than approximate it. A formula with a blank coefficient is more useful than a wrong number.
4. In `confidence`, write the source tier: Primary / Secondary / Unverified.

Write to:
{{repo}}/data/raw/program_chunks/chunk_{{cluster}}_{{rto_code}}_wholesale.csv
{{repo}}/data/raw/program_chunks/chunk_{{cluster}}_{{rto_code}}_wholesale_gaps.md

Report back only: row count, products covered, anything you could not verify. Do not paste the CSV.
