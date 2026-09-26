# Gaps — chunk_SE_carolinas.csv

All 13 utilities in the handoff spec have at least one row. Notes on what could not be
fully verified or is missing detail:

## Rate values not published / not found in searched sources
- **Cobb EMC NiteFlex** — confirmed the rate exists (residential EV/TOU) but the actual
  on-peak/off-peak cents/kWh were not published on the page reviewed. Row captures
  structure only; dollar values blank.
- **Sawnee EMC Residential TOU (Schedule TU-27)** — rate exists per Sawnee's own rate-schedule
  page, but the per-kWh on/off-peak values were not visible in the fetched summary (likely
  behind a PDF not directly retrieved). Recommend pulling the actual PDF rate sheet in a
  follow-up pass.
- **Sawnee EMC NEM Rider** — rider exists and mechanics (net-negative months only) are
  documented, but the specific $/kWh credit rate was not found.
- **GreyStone Power GS-SOFF (Rate 72)** and **Load Management Service (Rate 9)** — tariff
  PDFs exist and were cited, but $/kW or $/kWh figures were not visible without opening the
  full PDF (only summary text was retrieved). Confidence kept at Primary because the PDF
  link is the tariff itself, but the incentive_value_usd cell is blank.
- **Berkeley Electric Cooperative Time-of-Day (Rate 80/81)** — on/off-peak rate values not
  found in the pages reviewed.

## Not researched in this pass (out of the 13-utility list, no findable program)
None — every listed utility yielded at least one row.

## Utilities from the broader handoff list NOT in this file's scope
This file was scoped to the 13 utilities in the "chunk_SE_carolinas" line of the SE wave 2
HANDOFF: Duke Energy Carolinas, Duke Energy Progress, Georgia Power, Alabama Power, Dominion
Energy South Carolina, Santee Cooper, Jackson EMC, Cobb EMC, Sawnee EMC, GreyStone Power,
Walton EMC, EnergyUnited, Berkeley Electric Cooperative. Florida and TVA utilities are handled
in separate chunks per the handoff (chunk_SE_florida.csv, chunk_SE_tva.csv) and are not
attempted here.

## Categories not found for any utility in this set
- No wholesale/organized-market rows were created (correct — this region has no RTO; per
  region_southeast.md the presence/interconnection layers carry that signal, not the
  programs file).
- No BESS-specific storage-incentive program was found for the Georgia EMCs, Alabama Power,
  Dominion SC, Santee Cooper, EnergyUnited, or Berkeley Electric — only Duke (PowerPair) and
  Georgia Power (IRP-approved Solar Plus Storage Pilot) have a captured storage incentive in
  this file. Worth a follow-up search targeting each co-op's G&T (Oglethorpe Power for the
  Georgia EMCs) for any G&T-level battery program that flows down to members.
- Cobb EMC, Sawnee EMC, GreyStone, Walton EMC are EMCs whose wholesale power comes from
  Oglethorpe Power (G&T) — no G&T-level DR/storage program specific to these members was
  searched in this pass; flagged for a follow-up per the skill's G&T-shortcut guidance.
