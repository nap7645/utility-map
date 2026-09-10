# Region plan — SPP (Southwest Power Pool)

Read `plans/PLAYBOOK.md` first. Deltas only. *Verify regional facts before relying.*

## Shape of the market

Fourteen states, mostly partial: KS, OK, NE (fully), plus the western halves of MO and AR (done
for MISO — carry over the Evergy/Empire/AECC-west rows already tagged SPP), the Dakotas'
western portions, MT/WY/NM/TX panhandles, and small slivers of IA/MN/LA. Load is concentrated
in Evergy (KS/MO), OG&E, PSO (AEP), Xcel SPS, Westar/KCP&L legacy, Nebraska's three big
public power districts (OPPD, NPPD, LES — Nebraska is 100% public power, no IOUs), and a very
long co-op tail via G&Ts (KAMO, Western Farmers, Sunflower, KEPCo, Tri-State's eastern members).

SPP is the **thinnest DR market** of the seven. There is no capacity market; resource adequacy is
bilateral. Retail DR is utility-by-utility and mostly C&I interruptible plus co-op water-heater
switches. Expect a lot of `No (checked)` in `res_dispatch` and treat that as the finding.

## Denominator

States: KS, OK, NE fully; then pull MO/AR/ND/SD/TX/NM/MT/WY/IA/MN/LA and keep only records whose
`rto` the scan agent tags SPP. The MO/AR/ND/SD pulls already exist from MISO — reuse the files,
don't re-fetch. Xcel SPS and SWEPCO's TX/OK/AR/LA portions are SPP.

## Load-bearing utilities (≈18)

Evergy Kansas Central, Evergy Metro, Evergy Missouri West, OG&E, PSO, SWEPCO (SPP portion —
already have rows; extend), Xcel SPS, Empire District (Liberty), OPPD, NPPD, LES, Kansas City
BPU, Kansas Gas Service (no — gas), Sunflower/Mid-Kansas, Western Farmers, KAMO, Oklahoma
Electric Cooperative, CoServ (no — ERCOT), Golden Spread.

## Program families

- **Habit**: OG&E SmartHours (a real residential CPP/VPP — one of the largest smart-thermostat
  DR programs anywhere, ~400k customers; OG&E is the SPP reference case), Evergy's TOU
  (mandatory-default transition in MO, opt-in in KS), PSO Power Hours, NPPD/OPPD/LES TOU pilots,
  Xcel SPS TOU.
- **Dispatch**: OG&E SmartHours thermostat control, Evergy Thermostat Program, PSO Power Hours,
  OPPD Cool Smart, co-op water-heater programs via G&T (KEPCo, Sunflower, WFEC).
- **Export**: KS net metering (residential 15 kW cap, IOU-only, mandatory but with legislated
  demand-charge fights — capture the 2019 Kansas Supreme Court ruling and the 2024 successor),
  OK net metering (weak), NE net metering (25 kW, statewide incl. public power).
- **Storage**: essentially no state incentives. SPP's own ESR participation model.

## Interconnection

KCC (KS), OCC (OK), Nebraska PSC (limited — public power boards set their own). Nebraska is the
odd one: every utility is public; the state file row says `applies_to = statute applies to all
public power`, and OPPD/NPPD/LES each get a utility row. One Opus agent for all three states.

## Wholesale (Opus, one agent)

SPP has energy and ancillary markets (Integrated Marketplace) but **no capacity market**; DR
value is in bilateral RA and in ancillary via the Order 2222 aggregation model (SPP's
implementation — verify effective date). Capture: the Demand Response Load (DRL) registration
type, Regulation Up/Down and Spinning/Supplemental clearing price ranges, the ESR model, and
state opt-outs (verify — several SPP states have opted out of aggregation for small utilities).
Sources: SPP Market Protocols, SPP State of the Market (Market Monitoring Unit).

## Cluster split

- Presence: A {KS, OK} (≈70), B {NE + panhandles} (≈50), C: SPP-tagged rows from MO/AR/ND/SD
  reuse — just re-scan the 51 all-Unknown rows.
- Programs: one Sonnet agent for IOUs (OG&E, PSO, Evergy ×3, SPS, Empire), one for public power
  (OPPD, NPPD, LES, KC BPU) + G&Ts.
- Interconnection: one Opus agent {KS, OK, NE}.
- Wholesale: one Opus agent.

## Hard problem to flag

The value case in SPP is weak for the dispatch bucket and mostly about OG&E and Evergy TOU.
If the business isn't going to sell here soon, this region is the one to defer.
