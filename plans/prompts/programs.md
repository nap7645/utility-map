# Prompt template — full program rows (Sonnet; Opus if the cluster includes a retail-choice market)

Fill `{{...}}` from the region file. Clusters of 12–20 utilities. IOUs first.

---

You are researching retail electric utility programs for a behind-the-meter PV+storage economics engine. Read the schema at {{repo}}/data/processed/programs_SCHEMA.md FIRST and follow it exactly — 22 columns, category vocabulary, one row per operating company.

CLUSTER {{cluster}} — {{region}}, states {{states}}. Research these utilities and emit every demand response, TOU/RTP/CPP rate, storage incentive, VPP, EV rate, and export-compensation program you can verify:

{{utility_list}}

Copy those utility names EXACTLY as given — they are join keys.

REGION-SPECIFIC PROGRAM FAMILIES to look for (these are what make this region different):
{{program_families}}

REGION GOTCHAS:
{{gotchas}}

WORKFLOW (non-negotiable):
1. Write with Python's `csv.writer`. Header plus first ~8 rows to disk immediately; append in batches. Previous runs were killed mid-task and lost unwritten work.
2. Before reporting done, re-read with `csv.reader` and assert every row has exactly 22 fields. Fix anything that fails.
3. `source_url` on every row — a deep link to the tariff sheet or program page, not a homepage. Prefer the utility's own site or the regulator's docket over aggregators.
4. Never invent a row or a value. A blank cell is expected and correct when the utility doesn't publish the figure.
5. In `confidence`, write the source tier: Primary / Secondary / Unverified.
6. `last_verified` = {{today}}.

A verified row with a real tariff link beats five vague rows. Target {{target_rows}} rows.

Write to:
{{repo}}/data/raw/program_chunks/chunk_{{cluster}}_{{label}}.csv
{{repo}}/data/raw/program_chunks/chunk_{{cluster}}_{{label}}_gaps.md — utilities you checked and found nothing for, and utilities you could not check. This is as valuable as the data.

Report back only: row count, utilities covered, utilities you could not verify. Do not paste the CSV.
