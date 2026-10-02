# Utility Map — build spec

Status: v1, 2026-09-27. Supersedes `SPEC_OUTLINE.md`. Items marked **OPEN** still need Nathan's call;
everything else is decided (Nathan's notes) or a default Nathan can override.

## 1. Purpose
A consulting tool for Nathan: select a client's area or address and get everything needed to start
a job — the utility, its governing market, its programs, and what those mean for which technology
pays and by how much. The core lens is **multipliers**: programs or conditions where two
technologies together save more than each alone (e.g. battery + TOU + low solar export credit;
heat pump + winter thermostat DR; EV + managed-charging credit + TOU). The map should make present
and likely-future multipliers visible at a glance.

- Scope: US only.
- User: Nathan (consultant). Plain language still required: clients may see the screen.
- Hosting: public GitHub Pages, no client data stored.

## 2. Map layers
| Layer | Content | Rank | State (2026-10-02) |
|---|---|---|---|
| Governing bodies | ISO/RTO or the non-RTO alternative (balancing authority, TVA, BPA, etc.) | 0 | **Done**: the "RTO / ISO" color-by layer (utilities colored by market). Separate outline polygons not required. |
| Utilities | Service-territory boundaries | 0 | **Done**: all 50 states + DC (2,914 polygons) |
| Ownership type | IOU / municipal / co-op / federal-state | 0 | Present where researched |
| Programs | Every program that saves customers money against the base rate: two buckets (time-based pricing, paid device control) × homes/businesses; program type, $ values, sources | 0 | **Done for all 50 states + DC** (presence for every territory >10k customers; program rows for the large utilities). 89 territories (1.8M customers, 1.2%) still all-Unknown (2026-10-02). Interconnection/wholesale only for MISO, PJM, NYISO, CAISO, Southeast, ISO-NE. |
| Gas ÷ electricity price ratio | Relative cost of gas vs electric heat by area | 1 | **Planning only**: data-source survey (EIA state gas/electric prices, EIA-861 utility average ¢/kWh, utility gas tariffs) |
| Multipliers | Flag co-occurring programs that stack (derived from program rows + `stackable_with`) | 1 (planning) | Concept only |

## 3. Info pane (left drawer)
- On area or address select: all location-specific info needed for analysis/design work.
- **No changes now** (judged good as of 2026-09-27 noon).
- Rank 2: a button that exports the location's data (tariff, programs, interconnection, market)
  to Nathan's electrotech design/simulation app. Default format: JSON, schema defined later.

## 4. Priorities
- **Rank 0**: ISO/RTO polygons · utility boundary polygons · ownership type · utility programs.
- **Rank 1**: full bill structure · historical LMP · DER hosting capacity · DER aggregators ·
  gas/electric ratio (plan first).
- **Rank 2**: local electrotech installers · local "greentech sentiment" (legislation and public
  stance, e.g. Idaho county renewable bans, Ohio siting bills) · export-to-app button · other tools.

## 5. Definition of done (all tasks)
A task is done only when **an agent other than the one that built it has verified it works**, with
evidence: validator output, counts, screenshots of the live site, or re-checked sources. "Wrote the
file" is not done.

## 6. September push: Rank 0 for the whole US + audit
### 6.1 Coverage work
1. **Governing-body layer**: done (RTO / ISO color-by). Only needs new states tagged.
2. **West: finish.** NV/AZ/NM presence; program rows (reference IOUs by Opus, PNW, SW+Mountain);
   state interconnection rules; wholesale (WEIM/WEIS, EDAM/Markets+, SPP RTO West status).
3. **SPP**: KS, OK, NE + SPP portions of MO/AR/LA/TX/NM/SD/ND/MT/WY; presence, programs,
   interconnection, SPP wholesale.
4. **Texas/ERCOT.** DONE with the default: TDU territory shows TDU
   programs (TDU-funded load management / standard offer programs) plus the label "retail offers vary
   by provider". Munis and co-ops outside retail choice are researched normally. Non-ERCOT Texas
   (SPP, MISO, El Paso) is tagged to its market. REP offers → Rank 1.
5. **Alaska, Hawaii.** Presence + programs + interconnection (Hawaii is program-rich).
6. **Fill passes**: one per region on fully-Unknown territories (currently ~150, 8.8M customers,
   before West W4).
7. **Interconnection and wholesale are NOT Rank 0**: deferred for new regions (SPP, TX, AK, HI, rest of West). Previously OPEN; Default: state rows for every new state; utility deviation rows
   only for utilities with program rows.

### 6.2 Audit (the rubric is written first; agents and Nathan both use it)
- **Automated checks** (script, every region). Each must pass:
  - Every row passes validation.
  - Every target territory has a presence row.
  - Every program/interconnection utility name joins to a boundary.
  - No cross-state name joins.
  - Every Yes has a URL.
  - A link check returns non-4xx for ≥95% of source URLs; Nathan runs it, since it needs internet.
  - Every territory has a governing body assigned.
  - The polygon layer covers 100% of the lower 48.
- **Sampled source re-verification** by independent Opus auditor agents:
  - Stratified random samples per region: ~5% of presence cells (minimum 20), ~10% of program rows
    (minimum 15), every state interconnection row's two focus cells, and 100% of the top-10 utilities
    by customers.
  - Pass bar [default]: ≥95% of sampled Yes confirmed; ≥90% of sampled No confirmed; 0 wrong $ figures
    among the top-10 utilities; every error logged and fixed.
- **UI verification**: an agent loads the live site, clicks 3 utilities per region (largest IOU,
  a co-op, a muni) and checks drawer contents against the data. Output: screenshots plus a pass/fail
  table.
- **Nathan's rubric**: a one-page checklist version of the above, plus spot checks on utilities Nathan
  knows personally.
- **Output**: `audit/AUDIT_<region>.md` per region + `audit/SUMMARY.md` (scores and open defects).

### 6.3 Process
- Maximum 3 agents in parallel. Sonnet for breadth, Opus for interconnection, wholesale, reference
  IOUs and auditing.
- Nathan pushes and re-runs `snapshot_boundaries.py` whenever new states are added.
- Check-ins only on blockers, plus a summary per completed region.
- Out of scope this push: all Rank 1 and 2 work except the gas/electric ratio data-source survey;
  UI redesign; Program-layer and drawer changes other than adding the new states.

## 7. Standing decisions (unchanged)
- Presence cells: time-based pricing / paid device control × homes / businesses; Yes / No / Unknown.
  Residential demand charges count as time-based pricing.
- Denominator: HIFLD territories with >10k customers; one row per operating company; utility state
  taken from the `(XX)` suffix of HIFLD names.
- Source tiers: Primary / Secondary / Unverified. A blank beats a guess; a checked "No" is not
  "Unknown".
- Utilities with ≥3 researched program rows: any missing program family is shown as "None found".
