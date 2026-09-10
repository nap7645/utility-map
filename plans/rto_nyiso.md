# Region plan — NYISO (New York)

Read `plans/PLAYBOOK.md` first. Deltas only. *Verify regional facts before relying.*

## Shape of the market

Six IOUs under the PSC ("Joint Utilities": Con Edison, Orange & Rockland, National Grid NY,
NYSEG, RG&E, Central Hudson) plus LIPA/PSEG Long Island (state authority, outside PSC rate
jurisdiction) and NYPA (wholesale, plus a few municipal customers). Retail choice exists for
supply (ESCOs) but, unlike ERCOT, the utility still runs the DR programs — so the polygon *is*
the program provider. Standard model applies.

New York has the most **layered** DER compensation stack anywhere: the Value Stack (VDER) with
its LSRV/DRV/E/capacity/environmental components, plus NY-Sun incentives, plus utility DR
programs that explicitly allow dual participation with NYISO. Capturing the stack correctly is
the whole job.

## Denominator

States: NY. `STATE='NY' AND CUSTOMERS>9999` ≈ 25 records. Also recover Rockland Electric
(NJ, EIA ID to find — it's O&R's NJ sub and belongs to the PJM set; add to `EXTRA_IDS`).

## Load-bearing utilities (≈9)

Con Edison, O&R, National Grid (Niagara Mohawk), NYSEG, RG&E, Central Hudson, PSEG Long Island,
plus the two largest munis (Jamestown BPU, Massena) for completeness.

## Program families

- **Habit**: Con Ed's SmartHome Rate and the mandatory-TOU-for-EV-and-large-customers rules;
  the Joint Utilities' opt-in residential TOU; Con Ed's standby tariff (Rider Q / SC 9 Rate IV
  standby — the most complex standby structure in the country; storage economics hinge on it).
- **Dispatch**: Con Ed's Commercial System Relief Program (CSRP) and Distribution Load Relief
  Program (DLRP) — $/kW-month reservation payments, explicitly BESS-eligible, explicitly
  stackable with NYISO SCR; the same program pair exists at every Joint Utility. Bring Your Own
  Thermostat programs at all six. Con Ed's residential battery "Smart Home" VPP. National
  Grid's ConnectedSolutions (yes, also in NY, not just New England).
- **Storage**: NYSERDA Retail Storage Incentive ($/kWh, by region), the 2024–25 6 GW roadmap
  residential storage block, NY-Sun for PV.
- **Export**: VDER Value Stack vs Phase One NEM for mass-market (residential PV under 750 kW can
  still elect Phase One NEM with the Customer Benefit Contribution charge). Storage paired with
  PV: the "hybrid" rules. Community DG (CDG) crediting.

## Interconnection

NY Standardized Interconnection Requirements (SIR) — a single statewide document covering all
IOUs, revised regularly, with explicit storage and non-export provisions and a well-defined
CESIR study process. One Opus agent, one state, but the SIR is long: budget it as two states.
LIPA follows its own SIR (near-identical). Capture: hosting-capacity gating ("Flexible
Interconnection"), 50 kW / 300 kW / 5 MW tiers, and the storage-specific "SIR Appendix" rules.

## Wholesale (Opus, one agent)

Special Case Resources (SCR — the ICAP/capacity DR product, per-zone prices matter: NYC (J) and
Long Island (K) are much higher), Emergency DR (EDRP), Day-Ahead DR (DADRP), the DER Participation
Model (Order 2222 — NYISO was first to implement), ancillary via aggregation, and Regulation.
Sources: NYISO ICAP Manual, Emergency DR Manual, DER Aggregation guide, Potomac Economics SOM.
NY has **not** opted out of aggregation.

## Cluster split

- Presence: one Sonnet agent (≈25).
- Programs: one Opus agent for the six IOUs + LIPA (the value stack and standby tariffs are
  numerically dense; Sonnet will flatten them), one Sonnet for munis.
- Interconnection: one Opus agent.
- Wholesale: one Opus agent.

## Hard problem to flag

The Value Stack is a **time-varying, location-varying** export price, not a number. The
`export_compensation` cell can't hold it. Record the component structure and the utility's
Value Stack calculator URL; the economics engine will need the actual hourly series from the
Joint Utilities' published files, which is a Phase-7-style data pull, not research.
