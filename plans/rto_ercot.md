# Region plan — ERCOT (Texas)

Read `plans/PLAYBOOK.md` first. This file is deltas only.
*Regional facts below are from training knowledge (mid-2026); the first agent in each phase must verify them.*

## Why ERCOT breaks the model

ERCOT is a **retail-choice** market across ~75% of Texas load. The HIFLD polygon is the
**TDU** (Oncor, CenterPoint, AEP Texas North/Central, TNMP) — a wires company that does not sell
energy and does not run residential price-signal programs. The **REP** (retail electric provider)
sells the energy and offers the TOU plans, free-nights plans, and increasingly the VPP programs
(Tesla Electric, Octopus, Rhythm, Base Power). A customer at one address can choose among dozens.

So for the competitive area:
- `res_habit` is **not a property of the territory**. It is `Yes` everywhere a REP offers a TOU
  plan, which is everywhere. Record it as `Yes` with `notes=retail choice; via REP` and cite
  PowerToChoose, not the TDU.
- `res_dispatch` splits: TDU-run programs (Oncor and CenterPoint have residential demand-response
  and smart-thermostat programs funded through EE riders) **and** REP/aggregator VPPs. Record both.
- `ci_dispatch` is largely **ERCOT-level**: Emergency Response Service (ERS), Load Resources
  (Controllable Load Resource / CLR for batteries, Non-Controllable for interruptible), and
  4CP transmission-charge avoidance — the single biggest C&I load-shifting signal in the state and
  it isn't a "program" at all. Capture 4CP as a `Demand-Charge` row against each TDU.

The **non-competitive** area — munis (Austin Energy, CPS Energy San Antonio, Denton, Garland,
Georgetown, Bryan, Lubbock — note Lubbock moved to retail choice in 2024) and co-ops (Pedernales,
CoServ, Bluebonnet, Bandera, Guadalupe Valley, Magic Valley, and ~50 others) — behaves like the
rest of the country. Standard scan applies.

## Denominator

States: TX only, but **exclude** Entergy Texas (MISO, already done), SWEPCO (SPP), Xcel SPS
(SPP, panhandle), El Paso Electric (WECC). HIFLD `STATE='TX' AND CUSTOMERS>9999` returns ~130
records; tag those four out-of-footprint and keep the rest. Expect ~120 in-footprint territories.

## Load-bearing utilities for full program rows (≈20)

TDUs: Oncor, CenterPoint Houston, AEP Texas Central, AEP Texas North, TNMP.
Munis: Austin Energy, CPS Energy, Denton, Garland, Georgetown, Bryan, College Station, Lubbock P&L.
Co-ops: Pedernales, CoServ, Bluebonnet, Guadalupe Valley, Bandera, Magic Valley, United Coop.
Plus a synthetic "REP market" entity for the competitive area (see below).

## Program families to look for

- TDU: Oncor/CenterPoint residential demand response and smart-thermostat programs (EE rider
  funded, run via load-management vendors); commercial load management; 4CP.
- REP: TOU and free-nights plans (habit); Tesla Electric / Octopus / Rhythm / Base Power VPPs
  (dispatch, via aggregator). These become `ViaAggregator` once Phase 4 exists — for now record
  under a synthetic utility `ERCOT competitive retail (REP market)` with `scope=state`.
- ERCOT-level: ERS, Load Resources (CLR/NCLR), Aggregate DER (ADER) pilot — the Order 2222
  analogue; note ERCOT is FERC-exempt so 2222 does not apply directly.
- Munis: Austin Energy's Power Partner thermostat program and its VOST-style solar tariff; CPS
  Energy's demand-response and STEP programs.

## Interconnection

PUCT Substantive Rule 25.211/25.212 set interconnection for all ERCOT utilities. **Texas has no
statewide net metering.** Export compensation is set by the REP (buyback plans, often at avoided
cost or a fixed ¢/kWh) in the competitive area, and by each muni/co-op elsewhere. The state file
row for TX should say `No statewide rule` and point to PUCT 25.211; the utility file will be
long, because every muni/co-op sets its own.

## Wholesale (Opus, one agent)

ERS, CLR/NCLR Load Resources, ancillary services (RRS, ECRS, Non-Spin, Reg-Up/Down) with recent
clearing prices, the ADER pilot rules, real-time co-optimization status, 4CP methodology.
Sources: ERCOT Nodal Protocols, ERCOT market reports, Potomac Economics SOM.

## Cluster split

- Presence A: TDUs + munis (≈40). Presence B: co-ops (≈80, two agents).
- Programs: one agent for TDUs + REP-market entity (Opus — retail-choice nuance), one for munis
  + co-ops (Sonnet).
- Interconnection: one Opus agent, TX only, but budget it like three states — the utility file
  is the work.
- Wholesale: one Opus agent.

## Hard problem to flag in PLAN.md

The presence layer's four cells assume the utility polygon is the program provider. In ERCOT's
competitive area it isn't. Until Phase 4 (aggregators) exists, the map will either overstate
(paint the whole TDU green because REPs exist) or understate (paint it gray). Recommend: paint
`res_habit` green with a distinct "via retail choice" hatch, and hold `res_dispatch` at
`ViaAggregator` once that state is wired.
