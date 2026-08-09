# Gaps and unverifiable items — Cluster A (MN, WI, IA, ND, SD)

Row counts: ic_A_state.csv = 5 state rows (MN, WI, IA, ND, SD) + header.
ic_A_utility.csv = 18 utility delta rows + header.

## Utilities researched but NOT given a row (no confirmed deviation from state default)
- **Wisconsin Public Service Corp (WPS)** — NEM (PG4 tariff) matches the PSC 119 statewide 20 kW
  default exactly in every source reviewed. No deviation found, so per schema no row was emitted.
  Recommend a direct tariff pull if a WPS-specific storage/non-export clause turns out to exist.
- **Interstate Power and Light Company (Alliant Energy) — Iowa** — reported to follow the SF 583
  default (outflow = retail rate, 1 MW / 110%-of-usage sizing) with no located deviation. No row
  emitted.
- **Minnesota Power (ALLETE)** and **Otter Tail Power Company** — both are MN IOUs explicitly
  named as cluster priorities, but I could not confirm a specific rate, cap, or storage deviation
  from the Minn. Stat. 216B.164 statewide framework beyond generic tariff-summary language. Given
  the schema's "absence means state default" rule, I did not fabricate a row. This is a real gap —
  both utilities almost certainly have published net metering/DER tariffs (Minnesota Power's is
  referenced in a MN Commerce Dept standby-rate analysis; Otter Tail's is at otpco.com) that were
  not fully read line-by-line. **Recommend direct tariff review** of:
  - https://www.mnpower.com/ProgramsRebates/Interconnections
  - https://www.otpco.com/customer-resources/how-to-connect-to-our-power-grid/minnesota-interconnection/
  before treating these two as confirmed state-default-only.

## Fields left blank or marked "Unclear" / "Not specified in sources reviewed" — state file
- **MN**: `ic_timeline_days` (no single statutory figure found; MN DIP sets tiered deadlines by
  track, not read line-by-line); `grid_charging_allowed` at the state level (genuinely unresolved
  — Xcel's storage guidelines define a non-export mode but don't clearly state whether grid-charged
  energy can ever earn export credit; flagged as an open DGWG stakeholder issue).
- **WI**: `grid_charging_allowed` (no statewide treatment — PSC 119 does not address it uniformly;
  live issue in the open NEM/VOSS docket); most `ic_*` timeline/fee fields (PSC 119 sets these by
  DG category tier, not extracted in full).
- **IA**: `ic_fast_track_kw` / `ic_simplified_kw` / `ic_application_fee` / `ic_study_trigger_kw` /
  `ic_timeline_days` — 199 IAC Chapter 45 uses a "Levels 1–4" application tier system; I could not
  find the exact kW breakpoints for each level in the time available. `grid_charging_allowed` and
  `non_export_option` are both "Unclear" — I found no Iowa-specific storage/non-export interconnection
  guidance comparable to Minnesota's or Wisconsin's; this is a real research gap, not just a blank.
  Also unresolved: whether the inflow-outflow credit truly banks long-term or settles strictly monthly
  (sources conflicted).
- **ND / SD**: Almost every `ic_*` and storage-related field is blank/Unclear because neither state
  has adopted statewide interconnection procedures at all (confirmed via the Freeing the Grid /
  IREC-Vote Solar 2026 scorecard for ND, and the SD PUC's own Solar FAQ page for SD). This is the
  expected and correct outcome per the task brief ("no statewide rule, utility discretion") rather
  than a research shortfall — but it does mean anyone using this tool for ND/SD projects must go
  utility-by-utility, which the utility file only partially covers (only Montana-Dakota Utilities
  was researched for these two states; dozens of small ND/SD munis and co-ops are not covered).

## Utility file — rows with real evidentiary gaps (marked "Low" confidence)
- **MidAmerican Energy Company** — found conflicting claims about the outflow/export credit basis:
  some secondary sources describe an avoided-cost rate (~$0.03–0.05/kWh) while the general SF 583
  summary implies retail parity. This needs a direct MidAmerican tariff pull (their Nov 24 2020
  filing) to resolve — I did not adjudicate the conflict, I flagged it.
- **Dakota Electric Association, Connexus Energy, Rochester Public Utilities, Austin Utilities,
  Owatonna Public Utilities, Moorhead Public Service, Cedar Falls Utilities, Muscatine Power and
  Water** — for all munis/co-ops, `grid_charging_allowed` and `non_export_option` (the two fields
  flagged as most important) are "Unclear" or "not confirmed." None of these smaller utilities
  publish storage-specific interconnection guidance that I could locate; only Xcel-MN (via its
  dedicated storage interconnection guidelines PDF) and We Energies (via its CGS Non-Purchase rate
  structure) had enough public documentation to characterize storage/non-export treatment with any
  confidence. **This is the single biggest unresolved question for the whole cluster** — whether
  battery arbitrage is legal at the smaller MN/IA municipal and cooperative utilities is currently
  unknown and would require direct calls/emails to each utility's engineering department.
- **Ames Electric Services (City of Ames)** — confirmed a genuinely unusual finding: its net
  metering tariff caps at <10 kW (vs. Iowa's 1 MW statewide default) and its interconnection
  agreement still references IEEE 929, a standard that predates IEEE 1547 entirely. This suggests
  Ames' rules may not have been updated in a long time; I could not confirm whether a newer version
  exists, since the only primary document found was a 2021 zoning-permit PDF that references the
  2008 tariff rider by citation rather than reproducing current text.
- **Montana-Dakota Utilities Co.** — found a specific, usable avoided-cost figure ($0.0269/kWh)
  from the utility's own consumer-facing solar page, but could not confirm the effective date or
  cross-check it against a filed tariff document, so confidence is Medium not High.

## Structural notes worth flagging to the schema owner
- Great River Energy is a wholesale generation-and-transmission cooperative with no retail
  customers and therefore no retail interconnection tariff of its own — I emitted a row explaining
  this rather than leaving it absent, since a silent absence could be misread as "follows MN state
  default," which would be wrong (GRE has no retail relationship to apply a default to).
- Two Montana-Dakota Utilities rows were emitted (one for ND, one for SD) since the utility spans
  both states in this cluster with the same deviation; the schema's utility file has a `state`
  column precisely to support this, but it's worth confirming the downstream join logic handles
  the same utility_name appearing twice with different state values correctly.
