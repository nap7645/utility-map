# Prompt template — presence scan (Sonnet)

Fill `{{...}}` from the region file. One agent per target file. Run clusters in parallel.

---

Fast presence scan of electric utilities: does each one offer (a) a price-signal rate and (b) a utility-controlled demand-response program, for residential and for C&I customers. Yes/No/Unknown per cell, one URL per Yes. This is a breadth task — speed over depth.

READ FIRST: {{repo}}/data/raw/presence_scan/SCAN_SCHEMA.md
YOUR TARGETS ({{n}} utilities): {{repo}}/data/raw/presence_scan/targets_{{cluster}}.csv
WRITE TO: {{repo}}/data/raw/presence_scan/scan_{{cluster}}.csv

CLUSTER NOTES — read these before searching; they save half the work:
{{cluster_notes}}

RTO TAGGING: the `rto` column gates everything downstream. Valid values for this region: {{rto_values}}. {{rto_notes}}

WORKFLOW (non-negotiable):
1. Work down the list in customer-count order (it is pre-sorted).
2. Write with Python's `csv.writer`. Write the header plus your first 8 rows to disk as soon as you have them; append every ~8 rows after that. Do not hold results in memory — previous runs were killed mid-task and lost everything unwritten.
3. Before reporting done, re-read the file with `csv.reader` and assert every row has exactly 17 fields and every target eia_id appears exactly once. Fix anything that fails.
4. Only write "No" when you looked at the utility's own site or tariff and found nothing. If the site was unreachable or JS-only, write "Unknown".
5. Never invent a URL. Every "Yes" needs a link on the utility's, its G&T's, or its regulator's domain.
6. In `confidence`, write the source tier: Primary / Secondary / Unverified, per the schema.

You have roughly 200 web searches. If you are running low, finish the remaining rows as Unknown with `notes=search budget exhausted` rather than guessing.

Report back only: row count, Yes/No/Unknown per cell, the RTO breakdown, and what you could not verify. Do not paste the CSV.
