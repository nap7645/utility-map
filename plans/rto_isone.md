# Region plan — ISO-NE (New England)

Read `plans/PLAYBOOK.md` first. Deltas only. *Verify regional facts before relying.*

## Shape of the market

Six states, two dominant holding companies (Eversource: CT/MA/NH; National Grid: MA/RI), plus
Unitil, Liberty (NH), Central Maine Power and Versant (ME), Green Mountain Power (VT), Burlington
Electric, and ~40 munis (MA has many — Reading, Taunton, Braintree, Hingham, Wellesley…). Retail
choice for supply in MA/CT/NH/RI/ME, but the utility runs the DR programs.

The headline program is **ConnectedSolutions** — Eversource/National Grid/Unitil/Cape Light
Compact in MA, National Grid + RI Energy in RI, Eversource/UI in CT, Eversource/Unitil in NH —
the largest residential-battery dispatch program in the country by enrollment, paying $/kW-summer
for battery discharge during called events. It is the single best-documented example of what
this whole map is for. Capture its per-state $/kW rates, event caps, and the 2025–26 rate changes
precisely, and note which states have paused or reduced it.

Green Mountain Power (VT) runs the other reference case: utility-owned Tesla Powerwall lease
("Energy Storage System" program) plus BYOD, dispatched against ISO-NE peaks and GMP's own
capacity/transmission charges.

## Denominator

States: CT, MA, RI, NH, VT, ME. Six pulls. ≈70 records >10k. Note Eversource subsidiaries file
under different HIFLD names by state (NSTAR Electric, Western Massachusetts Electric,
Connecticut Light & Power, Public Service Co of NH) — alias each.

## Load-bearing utilities (≈15)

Eversource ×3 (CT, MA, NH), National Grid MA, RI Energy, United Illuminating (CT), Unitil (MA/NH),
Liberty NH, Central Maine Power, Versant, Green Mountain Power, Burlington Electric, Cape Light
Compact (a CCA that runs its own EE/DR — treat as a utility), plus the 5 largest MA munis.

## Program families

- **Habit**: TOU is thin in New England — MA has default-TOU pilots, CT has opt-in TOU, GMP has
  a residential TOU. Most `res_habit` will be `No` (checked). That's a real finding; don't let an
  agent inflate it.
- **Dispatch**: ConnectedSolutions (battery, thermostat, EV — separate tracks); GMP ESS/BYOD;
  Efficiency Maine's demand-management programs; Cape Light Compact; C&I "Daily Dispatch" and
  "Targeted Dispatch" tracks; Mass Save-funded programs generally.
- **Storage incentives**: MA SMART (solar+storage adder, closing/transitioning — check status),
  the MA Clean Peak Standard (CPECs — a tradable certificate for peak-period clean energy, the
  only one of its kind; storage-eligible), CT Energy Storage Solutions (upfront + performance
  incentive), RI storage programs, Efficiency Maine storage rebates.
- **Export**: MA net metering caps and the SMART successor; CT's netting tariff (post-2022
  successor to NEM with buy-all/netting options); RI net metering; NH's 2022 net metering
  order; ME's NEB (net energy billing) and its 2024–25 reforms; VT's net metering with
  adjustors.

## Interconnection

Each state has its own PUC standard; MA (DPU tariff-based, with the "Group Study" and
Affected System Operator process), CT (PURA), NH, RI, ME, VT. Cluster as two Opus agents:
{MA, RI, CT} and {NH, VT, ME}. Storage-specific: MA's "System Modification" rules and the
ConnectedSolutions non-export path.

## Wholesale (Opus, one agent)

Forward Capacity Market (FCM) DR participation (Active Demand Capacity Resources), Price-Responsive
Demand, the Order 2222 DER aggregation model (effective 2026 — verify), Regulation, reserves.
Sources: ISO-NE Manuals M-20/M-20A (DR), M-27, IMM annual report. No state opt-outs.

## Cluster split

- Presence: two Sonnet agents (north {NH, VT, ME}; south {MA, RI, CT}).
- Programs: one Opus agent for the ConnectedSolutions utilities + GMP (rates and event rules
  must be exact), one Sonnet for the rest.
- Interconnection: two Opus agents.
- Wholesale: one Opus agent.

## Hard problem to flag

ConnectedSolutions rates and caps have been cut or paused in some states since 2024 and vary by
program year. A row that's right today is wrong next June. This region needs the annual
program-year refresh built into the staleness logic more than any other.
