# scan_SE3 gaps — South Carolina + Alabama presence scan

58/58 targets have rows; many cells are `Unknown` rather than deeply verified. Notes below explain
why and what a follow-up pass should check first.

## South Carolina — Central Electric Power Cooperative (CEPCI) co-ops (16 of 19)

All 19 SC co-op targets are confirmed CEPCI (Central Electric Power Cooperative) G&T members
(cepci.org/member-co-ops). `res_dispatch=Yes` was marked for all 19 via the joint **EnergySmartSC**
Smart Thermostat program (energysmartsc.org/smart-thermostat/), which is co-op-run and coordinated
by Central/ECSC — legitimate shortcut, same logic as a G&T program.

For 16 of the 19, `res_habit`, `ci_habit`, and `ci_dispatch` are left `Unknown` — I did not open each
co-op's own rate schedule PDF individually (many co-op sites are JS-rendered and returned empty on
fetch: aikenco-op.org, berkeleyelectric.coop, blueridge.coop, coastal.coop all returned blank).
A follow-up pass should open each co-op's rate schedule PDF directly (most link a PDF from a
`/rates` page) to check for a residential demand charge or optional TOU rate, and check each for a
dedicated Smart Thermostat / Dual Fuel program page beyond the shared EnergySmartSC portal (Palmetto
and Black River both have their own dedicated pages, suggesting others may too).

Three co-ops have `res_habit=Yes` based on secondary evidence (search-snippet only, not independently
re-fetched — worth confirming directly):
- **Horry Electric** — summer/winter peak-hour rate design (horryelectric.com/members/rate-center/)
- **Blue Ridge Electric** — "EmPOWERment" optional residential TOU rate (via nectarclimate.com,
  third-party; blueridge.coop itself is JS-only)
- **Mid-Carolina Electric** — $15/kW residential demand charge (mcecoop.com/member-benefits/rate-structure/)

**ci_dispatch lead, not converted to Yes**: an SC Energy Office DSM filing/news article references a
"longstanding load-control program... in effect for more than thirty years" reported by Central
Electric on behalf of its member co-ops. I could not find a direct CEPCI program page describing
scope/eligibility, so all 19 co-ops are `ci_dispatch=Unknown`. This is the single highest-value
follow-up — if confirmed, it would flip ci_dispatch to Yes across all 19 SC co-op rows.

## South Carolina — municipal utilities (6)

- **Rock Hill, Greer CPW, Easley Combined Utility System** — confirmed members of **Piedmont
  Municipal Power Agency** (PMPA; pmpa.com/member-cities, 10 members total). No PMPA-wide DR/TOU
  program page was found. All four cells left `Unknown` — needs each city's own utility rates page.
- **City of Orangeburg (DPU)** — site (orbgdpu.com/services/electric) is JS-rendered; fetch returned
  empty. Wholesale supplier not confirmed (likely Santee Cooper given county, not verified).
- **City of Camden** — confirmed wholesale supplier is **Carolina Power Partners** (an NTE Energy
  subsidiary, 2021–2041 all-requirements PPA), *not* Santee Cooper or a co-op G&T. Own programs page
  not checked.
- **Greenwood CPW** — fully checked: own Electric page and all rate codes (2000–2900) reviewed,
  supplier is Carolina Power Partners + SEPA. No TOU/DR/smart-thermostat program exists. Marked `No`
  across all four cells with Primary confidence.

## Alabama — TVA local power companies (14, confirmed)

Huntsville Utilities, Athens Utilities, Florence Utilities, Decatur Utilities, Sheffield Utilities,
Albertville Municipal Utilities Board, Bessemer Electric Service, Joe Wheeler EMC, Cullman EC,
Cherokee EC, Marshall-DeKalb EC, Sand Mountain EC, North Alabama EC, Arab EC — all confirmed TVA
local power companies via tva.com. **Correction to the region-plan lead**: Bessemer was not in the
cluster-notes TVA list but is confirmed TVA (tva.com/energy/public-power-partnerships/local-power-companies/lpc/bessemer-electric-service),
not Alabama Power territory as might be assumed from Birmingham-metro geography.

`res_dispatch` and `ci_dispatch` marked Yes via TVA EnergyRight Smart Thermostat Rewards and
PowerFlex (system-wide TVA programs, cited once per the skill's TVA shortcut). `res_habit`/`ci_habit`
(TVA "Time of Day" rate) left `Unknown` for all 14 — TVA's own materials note LPC adoption of
load-shifting TOU rates is uneven and needs per-LPC confirmation; not done here.

## Alabama — PowerSouth co-ops (12, confirmed membership only)

Baldwin EMC, Central Alabama EC, Clarke-Washington EMC, Coosa Valley EC, Dixie EC, Pea River EC,
Pioneer EC, South Alabama EC, Southern Pine EC, Tallapoosa River EC, Wiregrass EC, Covington EC —
all confirmed PowerSouth Energy Cooperative G&T members. No PowerSouth-wide or member-specific
TOU/DR program page was found (PowerSouth's own site was not deeply crawled; only search snippets
checked). All four cells `Unknown` for all 12 — this is the largest verification gap in the file by
row count and should be the first follow-up target (start with powersouth.com's own program pages,
then each member co-op's own rates page).

## Alabama — AMEA municipal systems (3)

Foley (Riviera Utilities), Opelika (Opelika Power Services), Dothan (Dothan Utilities) are members
of the **Alabama Municipal Electric Authority** (AMEA), not PowerSouth or TVA.
- **Riviera Utilities (Foley)** — fully checked: Electric Service page lists only flat rate PDFs
  (residential, general service, industrial, lighting), no TOU/DR/smart-thermostat program. Marked
  `No` across all four cells, Primary confidence.
- **Opelika Power Services** and **Dothan Utilities** — sites did not surface a rates/programs page
  within budget (Dothan's site is JS-rendered and returned empty on fetch). Left `Unknown`.

## Alabama — Black Warrior EMC

Not on PowerSouth's published member list and not a confirmed TVA local power company. Own site
(blackwarrioremc.com) has no visible rates or programs page in its navigation (only Company, My
Account, News Room, Contact, Outages). `rto` marked `SERC-nonRTO` as the safe regional default
(Alabama has no organized wholesale market regardless of supplier), but the actual wholesale supplier
is unconfirmed. All four program cells `Unknown`.

## Not attempted

Nothing was skipped outright for search-budget exhaustion — all 58 targets got at least an `rto`/
`ownership_type` determination and an attempt at the utility's own site. The `Unknown` cells above
are honest gaps, not guesses.

## Follow-up pass (2026-09-26)

- **Central Electric Power Cooperative ci_dispatch (SC, 19 co-ops)** — chased the "highest-value
  follow-up" flagged above. Read Central's own 2023 IRP (Section 4 DSM table) in full: it describes
  only *residential* direct-load-control (AC thermostat/switch, water-heater AMI/Wi-Fi/RF switches,
  EV charging) plus commercial *efficiency* incentives — no C&I interruptible/curtailable program.
  Then read SC ORS's 2018 Demand Side Management Report in full: it confirms "Central Electric
  Power Cooperative is reporting on behalf of the 20 distribution electric cooperatives," an active
  DR program (water heater control, AC control, voltage control, and generic "interrupted loads")
  reducing ~125 MW winter / ~60 MW summer peak demand, running 30+ years, plus a 2016 voluntary
  "Beat the Peak" alert program and a 2018 smart-thermostat program. The state summary table checks
  "Interruptible Service Incentives" for the co-ops with a footnote "*Available from select
  Co-ops" but does NOT name which co-ops, and does not describe a large-industrial/commercial
  scope distinct from residential. Neither document supports a clean C&I-specific ci_dispatch=Yes
  across all 19 co-ops, so **ci_dispatch was left Unknown for all 19 SC co-ops** rather than
  guessed — this contradicts the prior fill pass's ci_dispatch=Yes-via-cepci.org-homepage-language
  entries already in the CSV (rows 35-53), which cite only the vague phrase "facilitat[es]
  demand-response programs" on cepci.org's homepage. Recommend a future pass reconsider downgrading
  those to Unknown/Unverified, or find each co-op's own interruptible-rate tariff sheet directly.
- **AL PowerSouth member co-ops** — spot-checked several via search/fetch this pass:
  - **Pioneer Electric Cooperative (eia 30517)** — confirmed via its OWN site
    (pioneerelectric.com/time-of-use, Greenville/Selma AL) a residential Time-of-Use rate
    (res_habit=Yes). Note: a separate, unrelated "Pioneer Electric Cooperative" exists in
    southwest Kansas at pioneerelectric.coop — its tariff PDF was fetched and read by mistake
    initially, confirmed to be the wrong entity (no AL address/phone anywhere in it, "We Power
    Southwest Kansas" tagline), and discarded before any data was applied to this row.
  - Clarke-Washington EMC, Coosa Valley EC, Tallapoosa River EC — WebSearch only returned
    third-party rate-estimate sites, no own-domain TOU/interruptible confirmation; left Unknown.
  - PowerSouth's own site (powersouth.com) has no visible demand-response/load-management program
    page in its top nav (Safety/Generation/Transmission/Renewable only) — the G&T itself does not
    appear to run a shared DR program the way TVA does; each member co-op's own site remains the
    only path to fill ci_habit/ci_dispatch for the remaining PowerSouth co-ops.

