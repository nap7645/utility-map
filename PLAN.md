# utility-map — buildout plan

Persistent reference across sessions. **Update the Session Log at the bottom every session.**

Owner: Nathan. Purpose: the location-intelligence layer for the BTM electrification design & economics tool. The map answers "what is possible and what is it worth at *this address*" before the Python app runs a full design.

---

## 0. Guiding decisions

**Separate data from presentation.** Do not inline datasets into the HTML. Data lives in `data/processed/` as normalized CSV; a build script emits a compact JSON payload the map fetches at runtime. The Python app reads the same `data/processed/` files. One source of truth, two consumers.

**EIA utility ID is the universal join key.** Every dataset gets an `eia_id` column. HIFLD's `ID` field is the EIA utility ID, which is what makes the map joinable at all. Anything that can't be keyed to `eia_id` needs an explicit documented reason.

**Every row carries provenance.** `source_url`, `last_verified`, `confidence` on every record in every dataset, same convention as `programs.csv`. Non-negotiable — this data goes stale quarterly and will eventually back customer proposals.

**Screening vs. binding.** The map is a screening tool. Hosting capacity, HIFLD polygons, and program availability are all approximate. Never let map output flow into a customer-facing number without a re-verification step.

### Repo layout

```
utility-map/
  data/
    raw/          # immutable per-source snapshots, dated
    processed/    # normalized, eia_id-keyed, one file per layer
    crosswalk/    # name -> eia_id resolution, incl. manual overrides
  scripts/        # ingest + build + validate
  docs/           # published map + reports (GitHub Pages)
  PLAN.md
```

---

## 1. Data layers — status and priority

| # | Layer | Status | Priority | File |
|---|---|---|---|---|
| A | DR / TOU / BESS programs | **457 rows built**, unverified, PA/NJ/DE thin | Phase 1 | `data/processed/programs.csv` |
| B | EIA ID crosswalk | not started — **blocks everything** | Phase 0 | `data/crosswalk/utility_eia_crosswalk.csv` |
| C | Interconnection rules | not started | Phase 2 | `data/processed/interconnection.csv` |
| D | Full bill structure | not started | Phase 3 | `data/processed/bill_structure.csv` |
| E | Aggregator / CSP coverage | not started | Phase 4 | `data/processed/aggregators.csv` |
| F | EIA-861 utility stats | not started | Phase 5 | `data/processed/eia861_*.csv` |
| G | Hosting capacity | not started | Phase 6 | `data/processed/hosting_capacity.csv` |
| H | Historical nodal LMP | not started | Phase 7 | out-of-repo (too large) |

---

## Phase 0 — Crosswalk + scaffold `[IN PROGRESS]`

**Why first:** `programs.csv` keys on free-text `utility_name`; the map keys on EIA ID. They do not join. Nothing else can be integrated until this exists.

- [x] Repo scaffold, move `programs.csv` and reports in
- [x] Write `norm()` name-normalization, mirrored in Python and JS (parity-tested, passing)
- [x] Hand-write `data/crosswalk/aliases.csv` (97 entries, most still `unconfirmed`)
- [x] `scripts/build_map_payload.py` → `docs/data/programs.json`
- [ ] **Open the map, read the console, confirm the `unconfirmed` aliases** — unmatched utilities are logged via `console.table`
- [ ] Click "Export crosswalk CSV", save to `data/crosswalk/utility_eia_crosswalk.csv`, commit
- [ ] Add `eia_id` column to `programs.csv` from the exported crosswalk

**Approach change (decided session 2).** The sandbox has no outbound network — only `web_fetch`/`WebSearch` reach the internet, and `web_fetch` has a ~200-char URL cap that blocks multi-term ArcGIS queries. Pulling all ~2,931 HIFLD records through the model's context to build the crosswalk offline is expensive and slow. **The browser already loads HIFLD.** So: match client-side with `norm()` + an alias table, and have the map *export* the resolved `eia_id → utility_name` crosswalk. The browser is the network-enabled compute the build environment lacks. Offline crosswalk becomes a committed artifact rather than something we recompute.

**Known gotchas:**
- **HIFLD `STATE` is the utility's home state, not every state it serves.** `STATE='WV'` returns 4 records — no Appalachian Power, no Mon Power, no Potomac Edison. `STATE='NJ'` returns no JCP&L or Rockland. Never filter attributes by state and assume completeness. Geographic coverage is still fine because the polygons cross state lines.
- HIFLD names are municipal-style (`CITY OF LANSING - (MI)`); ~40 needed hand aliases.
- One utility → many EIA IDs and many polygons; several utilities share one HIFLD record across two tariff jurisdictions (APCo VA/WV, Potomac Edison MD/WV, Pepco DC/MD, Delmarva DE/MD). Crosswalk is many-to-one both directions.
- HIFLD `TYPE` is frequently `NOT AVAILABLE`. Our `ownership_type` is better — **we override HIFLD's, done in v0.6.**
- A point often falls inside several overlapping polygons. v0.6 collects all hits and prefers the one with program data; it lists the others.
- ~20 of our 143 entities are state agencies or G&T co-ops with **no retail polygon at all** — they can never match. Handled via the `scope` field (`utility` / `state` / `wholesale` / `rto`), so they don't pollute the match rate.

## Phase 1 — Programs into the map `[MOSTLY DONE — v0.6]`

- [x] `scripts/build_map_payload.py` → `docs/data/programs.json` (314 KB; 111 utility-scope, 16 wholesale, 4 state agencies, 32 market products)
- [x] Replaced heuristic RTO coloring with verified `rto`, falling back to the heuristic
- [x] Override HIFLD `TYPE` with our `ownership_type`
- [x] Detail drawer replaces the cramped Leaflet popup — programs grouped by category, collapsible, with source links and confidence badges
- [x] Color-by: RTO, ownership, program count, storage-eligible count
- [x] Placeholder sections for Interconnection / Bill / Aggregators / Hosting capacity so later phases have a home
- [x] RTO wholesale products shown per territory based on its RTO
- [ ] **Verify in browser** — match rate, alias corrections, drawer rendering
- [ ] Snapshot HIFLD to local GeoJSON so the map stops re-querying ArcGIS on every load

**Backlog carried in:** PA/NJ/DE top-up (17/9/5 rows — the worst gap, and it's the richest BESS region); independent source verification of the 25-row sample (never ran); `peak_offpeak_rates` only 24% populated.

**Backlog carried in:** PA/NJ/DE top-up (17/9/5 rows — the worst gap, and it's the richest BESS region); independent source verification of the 25-row sample (never ran); `peak_offpeak_rates` only 24% populated.

## Phase 1b — "Has program?" presence layer `[BUILT — 160/305 scanned]`

**Reframed goal (session 4):** the layer that matters is *which utilities have programs*, in two
buckets — **habit** (customer responds to a price signal: TOU/RTP/CPP/demand/EV rate) and
**dispatch** (utility or aggregator controls the asset: DLC/BYOT/BYOD/VPP/curtailment) — split
residential / C&I. Completeness means the *absence* color is trustworthy, which requires three
states per cell: `Yes` / `No` (checked, none found) / `Unknown` (not researched). A fourth,
`ViaAggregator`, is reserved for dispatch once Phase 4 exists.

Decisions: separate res / C&I layers; denominator = every territory >10k customers (387 in the
22 states); CSP route renders as a distinct state, not as Yes.

- [x] Denominator pulled from HIFLD: `data/raw/hifld_over10k.csv` — 387 territories, 56.2M customers
- [x] `scripts/build_presence.py` → `data/processed/presence.csv` + `docs/data/presence.json` (keyed by EIA ID — no name matching)
- [x] Derived Yes from `programs.csv` (109 territories); 4 map views + drawer chips
- [x] Presence scan clusters A (MN/ND/SD/WI), B (MI/IA/IL), E (AR/LA/MS/TX) — 160 rows, zero malformed
- [ ] **Clusters C (IN/OH, 52), D (KY/MO, 62), F (PA/NJ/MD/DE/VA/WV/DC, 31) — 145 targets, killed by monthly spend limit before first write.** Target files and schema are on disk; just re-run.
- [ ] Re-scan the 51 rows that came back fully Unknown (mostly WebSearch quota exhaustion mid-run, not absence)
- [ ] Out-of-footprint tagging is in — TVA (20), SPP (9), AECI/Other (9) render gray. Verify Evergy/Empire/Black Hills got tagged when cluster D runs.

**Current state:** 87% of customers have at least one cell resolved. Yes/No/Unknown per cell —
res_habit 107/39/241 · res_dispatch 97/25/265 · ci_habit 47/12/328 · ci_dispatch 99/7/281.
`ci_habit` is structurally the hardest cell: most utilities don't publish C&I TOU design clearly.

**Findings worth keeping:**
- HIFLD "NORTHERN STATES POWER CO" (267k) is NSP-**Wisconsin**; "... - MINNESOTA" (1.5M) is NSP-MN. My alias had them backwards for two sessions — fixed, and the fix un-collided the two entities in the payload (131 → 132).
- `norm()` mangled "CO-OP" (→ "OP") because punctuation stripping ran before word replacement. Fixed in both Python and JS; parity re-tested.
- The 82 already-researched utilities cover **82% of customers**; the 305 scan targets are 18%. The long tail is long but light.
- Central EPA (MS) is TVA, not Cooperative Energy — agent caught and corrected my brief.
- "Carroll Electric Cooperative" exists in both AR and OH; an agent nearly cross-attributed and caught it. Name-only lookups are a trap.

## Phase 2 — Interconnection rules → the address drawer `[BUILT — needs verification]`

- [x] `interconnection_SCHEMA.md` — two files, state rules as the floor, utility rows as deltas
- [x] `data/processed/interconnection_state.csv` — **22 states**, 31 columns
- [x] `data/processed/interconnection_utility.csv` — **97 utility deltas**, 21 columns, **100% join** against `programs.csv`
- [x] Payload + drawer rendering: utility deltas shown first, state default below, "no deviations on file" stated explicitly rather than left blank
- [ ] Verify in browser
- [ ] Backfill `grid_charging_allowed` (see below)

**The headline result is a negative one.** `grid_charging_allowed` — whether a battery may charge from the grid and still export or receive credit, which is the cell that decides whether arbitrage is legal at all — is **`Unclear` for 13 of 22 states**. This is not a research failure; most states simply never wrote a rule for it, because their net-metering statutes predate customer storage. Missouri's and Mississippi's rules contain no mention of batteries whatsoever (confirmed by direct text search).

Practical consequence: in those 13 states the answer is determined by utility practice and interconnection-engineer discretion, not by published rule. **Model it as a per-utility unknown with a risk premium, not as a permission.** Resolving it means calling utility interconnection desks, which is a phone-call project, not a research project.

Where it *is* answered: NJ (BPU actively enabling), MD (PSC approved storage provisions), IL (Level 1–4 forms address grid charging and non-export explicitly). Two states are `Yes-but-not-credited`. That trio plus PA is where storage arbitrage has the clearest legal footing.

### Other Phase 2 findings worth carrying forward

- **Michigan is the only state with a clear rule that adding a battery to a legacy net-metered PV system does not forfeit grandfathering** (R 460.920(5)(m)). IN/OH/KY/VA/WV produced no statutory answer. This single question decides most retrofit deals — treat it as a per-utility question to confirm before quoting a retrofit.
- **Mississippi H.B. 1139 (2016)** bars the MPSC from setting cooperative compensation, so ~57% of MS ratepayers are outside the state rule entirely.
- **Louisiana has no statewide interconnection standard at all** — it is utility-tariff-specific.
- **Pennsylvania's 200% sizing rule** derives from the AEPS Act statutory definition (73 P.S. § 1648.2), not from 52 Pa. Code § 75.13 — the PUC tried to codify it in the regulation in 2016 and IRRC struck it. Cite the statute.
- **Correction to an earlier assumption:** the Maryland PSC storage pilots at BGE/Pepco/Potomac Edison are utility-owned grid assets, not customer BYOD tariffs. Only Delmarva's (Sunverge VPP, 110 homes) matches a BYOD model.
- **Live cap risk:** MD's 3,000 MW aggregate cap is ~51% used but the community-solar pipeline may exhaust it; PSC has asked the legislature to act in 2026. NJ (5.8%) and DE (8%, raised from 5% in 2022) both have subscription-level gaps.
- **Virginia standby charge:** threshold moves 15 → 20 kW AC on 7/1/2026 under HB 1255; Dominion at $2.79/kW distribution + $1.40/kW transmission.
- **West Virginia grandfathering:** AEP/Wheeling Power cutoff is an interconnection application by 2/28/2026, ~12.4¢/kWh after. Mon Power/Potomac Edison is a separate 2024 regime, 25-year grandfathering, cutover 3/27/2024.
- `standby_threshold_kw` is only 64% populated; `export_credit_value` 82%.

### Original scope notes

The highest-value thing in the popup: it determines whether a design is *legal* before whether it's profitable.

Per utility capture: system size caps by customer class; export limits and non-export/limited-export options; standby charges and their kW threshold; UL 1741-SA/SB and IEEE 1547 requirements; external disconnect switch requirement; interconnection application fees and study thresholds; net-metering aggregate cap and current subscription level; expedited/fast-track eligibility; typical timeline; whether storage may charge from grid and still export; AHJ/permitting notes.

Source order: state PUC interconnection rules first (they set the floor for all IOUs in the state — big efficiency win), then per-utility tariff deviations, then co-op/muni which set their own.

**Design note:** state-level rules and utility-level deviations should be two files — `interconnection_state.csv` and `interconnection_utility.csv` — with the utility file holding only deltas. Avoids duplicating one rule 40 times.

## Phase 3 — Full bill structure

`programs.csv` captures rate *design*, not the whole bill. NPV needs the whole bill.

Capture per rate schedule: fixed/customer charge; energy charges by season and period; demand charges incl. ratchets; all riders (fuel/PCA, capacity, transmission, EE surcharge, decoupling); minimum bills; taxes/franchise fees; and the escalation history for the last 5–10 years so the app can fit a real escalation rate rather than assume 2.5%.

**Watch:** fuel/PCA riders can move a residential bill 10–20% and are updated monthly or quarterly. Model them as a time series, not a constant.

## Phase 4 — Aggregator / CSP layer

**The gap in `programs.csv`.** It is utility-program-centric. Most residential BTM assets actually reach DR and ancillary markets through a third-party CSP, not a utility tariff. Without this layer the app will systematically understate revenue in territories with no utility program but active aggregators.

Capture per CSP × territory: which CSPs operate where (Voltus, CPower, Enel X, EnergyHub, Leapfrog, Tesla/Sunrun VPPs, Renew Home); asset types accepted; residential vs C&I; revenue share / $ per kW-yr offered; which RTO product they bid into; contract length and exit terms; whether they stack with the utility program in the same territory.

Sources: CSP websites, PJM/MISO registered-CRA lists, state DR program participant lists.

## Phase 5 — EIA-861

**Blocked from the sandbox** (`eia.gov` is not on the fetch allowlist and the sandbox has no outbound network). Download the zip manually on the host, drop it in `data/raw/`, then parse locally.

Files worth parsing: Utility Data (ownership, RTO membership, service territory), Sales to Ultimate Customers (revenue/sales/customers by class → derived average ¢/kWh, a sanity check on Phase 3), Demand Response (actual enrollment, incentive payments, energy/peak savings by utility — ground truth against our program table), Net Metering (installed DG capacity and customer counts by utility), Reliability (SAIDI/SAIFI → backup value, which is the only quantitative handle on the customer-satisfaction objective).

Also the authoritative full utility roster — the only way to know what the long tail we skipped actually contains.

## Phase 6 — Hosting capacity

**Source found: [DOE U.S. Atlas of Electric Distribution System Hosting Capacity Maps](https://www.energy.gov/cmei/vehicles/us-atlas-electric-distribution-system-hosting-capacity-maps)** — 58 utilities and state agencies across 26 states + DC + PR as of May 2024. Start here rather than hunting utility by utility.

- [ ] Pull the Atlas list, filter to the 21-state footprint (expect ~12–18 utilities)
- [ ] For each, find the underlying ArcGIS REST service URL behind the viewer (this is the actual work)
- [ ] Ingest as GeoJSON; store feeder/line-section geometry + capacity values

**Two caveats that matter:**
1. Nearly all published HCA is **generation** hosting capacity. Our thesis is maximal electrification — a **load** addition problem. Load hosting capacity is rarely published. Expect to model load headroom ourselves from transformer/feeder proxies, or treat it as unknown risk.
2. HCA is non-binding, feeder-resolution, refreshed quarterly-to-annually. Render it as a risk flag, never a constraint.

## Phase 7 — Historical nodal LMP

Deferred by decision. This is the arbitrage signal and the largest dataset by far.

Approach when we get there: don't warehouse it in this repo. Either hit MISO/PJM APIs live, or use GridStatus.io rather than building ingest. Needs a location → pnode mapping, which is its own problem. Store aggregate statistics (TB2/TB4 spread by node by month, hours-at-price-percentile) in the map; keep full time series out-of-repo for the Python app.

---

## NYISO — COMPLETE (session 5, 2026-09-11)

First region onboarded through `plans/PLAYBOOK.md` and the research skill. **12 territories >10k**
(the region file guessed ~25; actual is 12 — NY's municipal tail sits almost entirely below the
threshold). All four phases done:

| Phase | Result |
|---|---|
| Presence | 5 municipals scanned. 4 of 5 are `No` across the board; **Rockville Centre runs a real utility-dispatched smart-thermostat DSM program** (PSC Case 07-E-1303, event called 7/16/2024, 158 customers, 0.3 MW) — res + C&I dispatch both Yes. |
| Programs | **88 rows** across 7 IOU/authority entities + NYSERDA statewide. Con Ed 14, National Grid 9, and 9 each for O&R / NYSEG / RG&E / Central Hudson / LIPA. |
| Interconnection | 2 state rows (PSC-regulated IOUs; LIPA separately) + 7 utility deltas. |
| Wholesale | **32 NYISO-market rows**, 28 Primary. |

**120 NY rows total, 105 Primary / 15 Secondary / 0 Unverified** — the cleanest provenance of any
region so far, because NY publishes tariffs and PSC orders well.

### Findings that corrected the region plan

- **Rockland Electric is EIA 16213, filed under `STATE=NY`.** It is O&R's New Jersey subsidiary and
  a PJM utility. This closes one of the five unmatched utilities outstanding since session 4 —
  added to `EXTRA_IDS`.
- **Massachusetts Electric (1.35M) and Nantucket Electric also file under NY** but are National
  Grid MA / ISO-NE. Added to the denominator with `rto=ISO-NE` and all cells `Unknown`, so they
  render as out-of-footprint gray rather than silently as "<10k". They belong to the ISO-NE phase.
- **LIPA is confirmed not subject to PSL §66-j or the state SIR** (its own Dec 2025 filing says so,
  citing Case 19-E-0079) — but it voluntarily mirrors the state framework closely, diverging in
  real ways: 5,000 kW non-residential NEM cap vs 2,000, no aggregate program cap at all, and an
  annual cash-out of banked credits.
- **The CSRP/DLRP parallel-program lead was right** — but not uniformly. **Central Hudson has no
  DLRP and no Term/Auto-DLM**, only CSRP and Targeted DR. Do not assume IOU parity in New York.
- **NYSEG/RG&E DLRP reportedly pays $0.00/kW-month.** Marked Secondary, sourced to a search index
  of the DPS Case 14-E-0423 annual report rather than a page-by-page read. **Worth one confirmation
  pass**: any model treating "has a DLRP" as revenue will over-credit both utilities.
- **`grid_charging_allowed` = `Yes` for the NY IOUs** — the SIR expressly studies an ESS's Maximum
  Import alongside Maximum Export. That is the first unambiguous `Yes` in the dataset; 17 of 22
  MISO/PJM states were `Unclear`. For LIPA it is `Unclear` (Maximum Import is declared in SGIP
  Appendix J, but no document says how grid-charged export is credited).
- Central Hudson's TDR ($6.82/kW-mo) and CSRP ($1.23–1.54/kW-mo) are **mutually exclusive**.
- LIPA exempts stand-alone storage reaching SGIP Step 3 before 2030-12-31 from Buyback Contract
  Demand Charges for 15 years — a dated economic cliff worth modeling.

### Known gaps carried forward

Standby $/kW rates at all five non-Con-Ed utilities (structure confirmed, numbers live in tariff
leaves not exposed as HTML); PSEG LI System Peak Relief has no published $/kW (set by MCOS study);
LIPA Battery Storage Rewards payment is aggregator-set — the agent correctly declined to write the
"$250/kWh" figure circulating on vendor sites.

## CAISO / California — COMPLETE (session 6, 2026-09-23)

29 territories >10k. Programs 90 rows (PG&E 19, SCE 14, SDG&E 7, CA statewide 12, 9 public
utilities 26, CAISO wholesale 12). Presence 17. Interconnection 1 state row + 12 utility rows.

Findings:
- **6 of 9 large CA public utilities are outside CAISO** (LADWP, Glendale, SMUD, MID, TID, IID →
  `WECC-nonRTO`). Merced ID sits in TID's BA (non-CAISO); Lassen MUD is inside CAISO/PG&E. The map
  treats `WECC-nonRTO` rows *with our data* as researched.
- **Battery retrofit on grandfathered NEM 2.0 does NOT forfeit NEM 2.0** (D.22-12-056; PG&E NEM2
  SC 8.b, SCE NEM-ST SC 8.d) — **except** storage added via SGIP with reservation accepted on/after
  2024-06-04 → moves to Net Billing Tariff (D.24-03-071), with equity/resiliency budget exemptions.
- **grid_charging_allowed = Yes-but-not-credited** under NBT/NEM paired storage: grid charging is
  allowed; only renewable-derived export earns credit (≤10 kW: monthly cap on exports; >10 kW:
  extra metering or power control). LADWP and MID require non-export for storage.
- **DRAM ended 2024-12-31** (D.24-04-006). **DER aggregations (DERP) cannot provide RA or
  Regulation** — only Spin/Non-Spin. Regulation needs the wholesale NGR model. CA has no
  opt-out on third-party aggregation. No WEIM/EDAM path for customer batteries in non-CAISO BAs.
- Unverified carry-forwards in `data/raw/interconnection/ic_CA_gaps.md` and
  `chunk_CA_caiso_wholesale_gaps.md` (SDG&E NEM-ST not read directly; several POU tariff PDFs
  did not render; flexible-RA must-offer window from 2018 BPM).

Bug fixed: `icStates` was keyed by state alone, so a state's second rule set overwrote the first —
NY IOUs were showing LIPA's rules. Now a list per state; drawer picks the rule set whose
`applies_to` names the utility and shows the others collapsed.

## Beyond MISO + PJM

Region buildout plans live in **`plans/`** — see `plans/README.md` for the sequence and cost
estimates. `plans/PLAYBOOK.md` is the generic recipe; `plans/rto_*.md` and `plans/region_*.md`
hold per-region deltas; `plans/prompts/` has the four agent prompt templates.

The research loop itself is packaged as a skill at
`.claude/skills/utility-program-research/` so any agent gets the schema-reading, incremental-write,
source-tier and validation discipline without being re-taught. Its `validate_csv.py` is tested
both ways — it passes all four current datasets and catches planted field-count, missing-URL,
blank-RTO, bad-tier, and missing-target defects.

Recommended order: finish MISO/PJM (clusters C/D/F) → NYISO → ISO-NE → CAISO → Southeast →
ERCOT (blocked on the aggregator layer) → West → SPP. Full national coverage ≈ 10.5M tokens.

## Provenance — source tiers (decided session 4)

High/Medium/Low was the research agent's self-assessment and was dropped. Every row now carries a
derived **source tier**, computed in `scripts/source_tier.py` from the `source_url` domain plus the
researcher's original note, erring toward the lower tier:

- **Primary** — the link *is* the source: utility tariff/program page, regulator order, RTO manual, statute.
- **Secondary** — the link *reports on* the source: news, DSIRE/OpenEI, trade press, a G&T describing a member program.
- **Unverified** — no usable link, or the link doesn't show the claim.

Raw `confidence` columns are retained for audit but not displayed. New research writes the tier
vocabulary directly (schemas updated). Current split — programs 247 / 150 / 28; state rules
20 / 2 / 0; utility deltas 32 / 40 / 25; presence Yes-cells 106 / 69 / 2.

Known limitation: "Primary" is a domain heuristic, not a fetch. A link on the utility's domain
that 404s or points at the wrong page still reads Primary. A link-checker pass (HEAD every
`source_url`, demote dead ones) is cheap and should run before any customer-facing use.

## Ongoing — bug/debt list

- [ ] Link-checker pass over every `source_url`; demote dead/redirected-to-homepage links to Unverified.

- [x] **CARTO basemap tiles return "API KEY REQUIRED"** (observed live 2026-09-09) — switched to OSM standard tiles in `93b78e9`. Move to a keyed provider before real traffic.
- [x] **v0.6 verified live 2026-09-09** at https://nap7645.github.io/utility-map/ — 1,478 territories load; 387 presence + 132 utilities + 22 state rules load; 109/112 researched utilities match; presence views color correctly; drawer renders chips → programs → interconnection (utility delta open, state default collapsed). Not yet verified: crosswalk export click, address lookup, mobile collapse (commit after the verified one).
- [x] Regression caught in verification: adding `TX` to `STATES` loaded ~300 ERCOT territories and recentered the map on Texas. Removed; Entergy Texas and SWEPCO now load by ID via `EXTRA_IDS`.
- [ ] Muscatine P&W is not in HIFLD under any name; Rockland Electric is filed under NY. Both stay unmatched until an EIA ID is added to `EXTRA_IDS`.
- [ ] **Policy question:** a well-researched IOU (DTE, 16 rows) shows `C&I · price signal: Unknown` because `build_presence.py` only derives Yes from `programs.csv`, never No. Options: (a) leave as-is — honest, but looks unresearched; (b) infer No when a utility has ≥N rows and none in the cell. Leaning (a) until the C/D/F scan lands.
- [ ] The browser pane used for verification doesn't tick CSS transitions; drawer `.open` applies but the 0.18s slide never completes there. Real browsers should be fine — confirm once on a phone.

- [ ] RTO assignment in the map is a heuristic; replace with verified data (Phase 1)
- [ ] HIFLD `TYPE` shows `NOT AVAILABLE` for many municipals; override with our `ownership_type`
- [ ] Map re-queries ArcGIS on every load — no caching, slow. Snapshot territories to local GeoJSON.
- [ ] `docs/index.html` and `utility_map_v0.5.html` are duplicates and will drift. Pick one; make the other a build artifact.
- [ ] Nominatim geocoding has no error handling and no usage-policy compliance (needs a User-Agent, rate limiting)
- [ ] No `last_verified` staleness surfacing in the UI — rows should visibly age
- [ ] `programs.csv` confidence ratings are self-reported by the research agents, never independently audited
- [ ] 13 Active rows sourced to news articles rather than tariffs; 20 to third-party aggregators

---

## Working notes for future sessions

- Sessions hit API limits. **Write files early and incrementally**; do not hold work in memory to write at the end. Two research runs were lost that way.
- Research subagents work well for breadth. Give them a schema file to read, a hard "never invent a row" rule, mandatory source URLs, and instructions to write incrementally.
- Long `web_fetch` URLs fail with `cowork_web_fetch_url_too_long`. Keep query strings minimal.
- Large `web_fetch` responses persist to a file instead of returning inline — read them from that path.

## Session log

**2026-08-08 — Session 1.** Built `programs.csv`: 457 rows, 142 utilities, 22 states + DC, 22 columns, every row source-linked. Nine parallel research agents by cluster. Two agents lost to session limits (PA/NJ/DE top-up, and the independent verification pass) — both still outstanding. Wrote `COVERAGE_REPORT.md` and `COVERAGE_GAPS.md`.

**2026-08-09 — Session 2.** Scaffolded repo, moved data in, wrote this plan. Identified the EIA-ID join gap as the blocker. Located the DOE Hosting Capacity Atlas as the Phase 6 source. Discovered HIFLD's `STATE` is home-state-only, which invalidates state-filtered attribute queries. Pivoted the crosswalk to a browser-side join with an exportable crosswalk. Built `norm()` (Python + JS, parity-tested), `aliases.csv` (97 entries), `build_map_payload.py`, and map **v0.6** with a detail drawer, verified RTO/ownership overrides, program-count layers, overlapping-polygon handling, and placeholder sections for Phases 2/3/4/6. `utility_map_v0.5.html` → `docs/legacy_v0.5.html`; `docs/index.html` is now canonical.

**2026-08-09 — Session 3.** Phase 2 built. Five research agents by region → 22 state rule rows + 97 utility delta rows, joining 100% against `programs.csv`. Wired into the payload and the drawer (utility deltas first, state default beneath, explicit "no deviations on file" rather than silent blanks). Key negative finding: `grid_charging_allowed` is unresolved in 13 of 22 states because the rules predate customer storage.

Process note: two of five agents again emitted unquoted-comma CSVs. A dedicated repair agent realigned them semantically rather than re-researching — much cheaper, and the right move since all the content was present, just misplaced. **Next time, put "write with `csv.writer`, then re-read and assert field counts" directly in the research prompt.** Three of five agents did this unprompted; two did not.

**2026-09-09 — Session 4.** Reframed the target as the "has program?" presence layer (Phase 1b). Pulled the 387-territory >10k denominator from HIFLD by state (home-state field; multi-state IOUs are filed under HQ state — OH holds FirstEnergy and AEP subs). Built `build_presence.py`, four map views, drawer chips. Six scan agents launched; three completed (160 rows, zero malformed — the `csv.writer` + assert mandate worked); three died on a **monthly spend limit** before writing anything. Fixed the NSP-MN/WI alias inversion and the `norm()` CO-OP bug. Aliases now 65 confirmed / 47 unconfirmed.

Budget note: the monthly spend limit is a hard wall, unlike the session limits. Each presence-scan agent cost ~270–350k tokens for 37–62 utilities. Remaining 145 targets ≈ 3 agents ≈ ~900k tokens. WebSearch has a 200-call-per-agent cap that two agents hit — a follow-up pass on the 51 all-Unknown rows should be a separate small agent.

**Next session — start here:**
1. Re-run presence scan clusters **C, D, F** (prompts are in this session's transcript; schema + targets on disk). That closes the >10k denominator.
2. Open `docs/index.html`, switch to the four "Has program?" views, sanity-check colors against a few utilities you know. Check `console.table` of unmatched.
3. Export the crosswalk CSV, commit, add `eia_id` to `programs.csv`.
4. Then Phase 4 (aggregators) — it feeds the `ViaAggregator` state and is the last piece of the presence layer — before Phase 3 (bill structure).
