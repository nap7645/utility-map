# Playbook — onboarding a new RTO / region onto the utility map

This is the generic recipe. Each `plans/rto_*.md` file holds only the deltas for its region. Read
this first, then the region file, then run the phases in order. Everything here was learned the
hard way on MISO+PJM (sessions 1–4, see `PLAN.md`); don't re-learn it.

## What "done" means for a region

Four layers, in this order of value:

| # | Layer | Output | Agent tier | Cost (observed) |
|---|---|---|---|---|
| 1 | **Presence** — has/doesn't-have, 4 cells | `presence_scan.csv` rows | Sonnet | ~5–6k tokens/utility |
| 2 | **Programs** — full 22-column rows for the load-bearing utilities | `programs.csv` rows | Sonnet (Opus for wholesale) | ~15k tokens/utility |
| 3 | **Interconnection** — state floor + utility deltas | `interconnection_state.csv`, `interconnection_utility.csv` | **Opus** | ~40k tokens/state incl. deltas |
| 4 | **Wholesale** — RTO market products a BTM asset can touch | `programs.csv` rows, `rto=<X>-market` | **Opus** | ~150k tokens/RTO |

Presence over the whole >10k-customer denominator. Programs over the utilities that together cover
~85% of the region's customers (usually the IOUs plus the largest munis/co-ops — 15–40 entities).
Interconnection for every state in the region. Wholesale once per RTO.

Opus where numbers and legal nuance matter (interconnection, wholesale, anything customer-facing).
Sonnet for breadth. Never Haiku for research — it invents URLs.

## Phase 0 — Denominator (no agent; ~30 min, cheap)

1. List the region's states. Note which are *partially* in the RTO — the region file says.
2. Pull HIFLD territories >10k customers per state:
   ```
   https://services3.arcgis.com/OYP7N6mAJJCyH6hd/arcgis/rest/services/Electric_Retail_Service_Territories_HIFLD/FeatureServer/0/query?where=STATE='XX' AND CUSTOMERS>9999&outFields=ID,NAME,CUSTOMERS&returnGeometry=false&f=json
   ```
   One state per call. The fetch tool caps URLs around 200 chars; multi-state `OR` clauses fail.
3. **HIFLD `STATE` is the utility's HQ state, not where it serves.** FirstEnergy and AEP subsidiaries
   sit under `OH`; SWEPCO under `OK`; Rockland Electric under `NY`. After the state pulls, list the
   region's known multi-state IOUs and query each by `NAME LIKE 'FOO%'` to find its real record.
   Add those IDs to `EXTRA_IDS` in `docs/index.html` and to the denominator file.
4. Write `data/raw/hifld_over10k_<region>.csv` with `eia_id,hifld_name,hifld_state,customers`.
   Assert unique `eia_id`.
5. Split into scan target files of **40–60 utilities**, sorted by customers descending, grouped by
   state cluster. Bigger lists hit the per-agent WebSearch cap (200 calls) before finishing.

## Phase 1 — Presence scan (Sonnet, one agent per target file, run in parallel)

Schema: `data/raw/presence_scan/SCAN_SCHEMA.md`. Prompt template: `plans/prompts/presence_scan.md`.
The region file supplies the **cluster notes** — G&T memberships, TVA-style shortcuts, which
co-ops are actually in a different RTO. Those notes are what make a scan fast; without them the
agent researches 50 co-ops individually.

Gates before merging: every row has 17 fields (`csv.reader` assert); every `Yes` has a URL; `rto`
is filled on every row; no eia_id outside the target file.

## Phase 2 — Programs (Sonnet, clusters of 12–20 utilities)

Schema: `data/processed/programs_SCHEMA.md`. Prompt template: `plans/prompts/programs.md`.
Assign utilities by state cluster, IOUs first. The region file lists the load-bearing utilities
and the region-specific program families to look for (e.g. ConnectedSolutions in ISO-NE, ERS in
ERCOT, ELRP in CAISO).

Gates: 22 fields per row; `source_url` on every row; no holding-company rows — one row per
operating company; category vocabulary matches the schema exactly.

## Phase 3 — Interconnection (Opus, clusters of 3–5 states)

Schema: `data/processed/interconnection_SCHEMA.md`. Prompt template: `plans/prompts/interconnection.md`.
State rules first, utility deltas only where a utility departs from the state floor. Munis and
co-ops that set their own rules go in the utility file with `deviates_on=all`.

The two cells that matter most and are hardest: `grid_charging_allowed` and whether adding a
battery to a legacy-NEM system forfeits grandfathering. Expect `Unclear` often; that is a finding.

## Phase 4 — Wholesale (Opus, one agent per RTO)

Prompt template: `plans/prompts/wholesale.md`. Cite the RTO's own manuals/BPMs and the IMM
State of the Market report. Get formulas right; leave numbers blank rather than approximate.
Capture the Order 2222 status and any **state opt-outs** from aggregation — those are hard gates.

## Phase 5 — Merge, alias, build (no agent)

1. Merge chunks with the same validation as `scripts/merge_program_chunks.py` (repair pass if any
   row is off by fields — the agent left an unquoted comma).
2. Add aliases to `data/crosswalk/aliases.csv` for every new utility whose `norm()` key won't
   match its HIFLD name. Open the map, read the `console.table` of unmatched, iterate.
3. Add the region's states to `STATES` in `docs/index.html` **only if the whole state is in
   footprint**. Otherwise load its utilities by ID via `EXTRA_IDS`. (Adding TX for one utility
   pulled 300 ERCOT polygons and recentered the map.)
4. `python3 scripts/build_map_payload.py && python3 scripts/build_presence.py`, commit, push,
   then open the live site and click three utilities you know. Screenshots lag in the in-app
   browser; trust the DOM.

## Rules that are not optional

- **Write CSVs with `csv.writer`, then re-read and assert the field count.** Two of five agents
  skipped this on MISO/PJM and cost a repair pass. Put it in the prompt verbatim.
- **Write to disk early and incrementally.** Session and spend limits kill agents mid-run; five
  research agents were lost that way. Header + first ~8 rows immediately, then append.
- **Never invent a row, a value, or a URL.** Blank beats a guess. `Unknown` beats a wrong `No`.
- **Source tier, not confidence**: `Primary` (link is the source) / `Secondary` (link reports on
  it) / `Unverified`. Written into the `confidence` column; derived in `scripts/source_tier.py`.
- **One row per operating company.** Holding companies (AEP, FirstEnergy, Exelon, Duke, Southern,
  Berkshire, Xcel) have different tariffs per state jurisdiction.
- **Name collisions are real.** Carroll Electric exists in AR and OH; Southwestern Electric in
  IL, NM, and as SWEPCO. Always carry the state and EIA ID.
- Each agent gets ~200 WebSearch calls. Size the target list so it finishes; when it hits the cap
  the tail of the list comes back `Unknown`, not wrong — but it's wasted.

## Budget reference (from MISO+PJM)

| Job | Utilities | Tokens |
|---|---|---|
| Presence cluster A (MN/ND/SD/WI) | 61 | 272k |
| Presence cluster E (AR/LA/MS/TX) | 62 | 267k |
| Programs cluster (WI/MI, 17 utilities, 95 rows) | 17 | 338k |
| Interconnection cluster (MI/IN/OH/KY + 25 deltas) | 4 states | 216k |
| Wholesale (PJM + MISO together) | 2 RTOs | 149k |

A full region of ~400 territories and ~30 program utilities and ~8 states runs roughly
**2.5–3.5M tokens** across 12–15 agents. Budget for one failed agent in every five.
