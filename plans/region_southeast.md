# Region plan — Southeast (non-RTO: SERC, TVA, FRCC)

Read `plans/PLAYBOOK.md` first. Deltas only. *Verify regional facts before relying.*

## Shape of the market

No RTO. Vertically-integrated IOUs run their own balancing areas: Duke Energy Carolinas and
Progress (NC/SC), Dominion South Carolina, Santee Cooper (SC state authority), Southern
Company (Georgia Power, Alabama Power, Mississippi Power — MS done), TVA (federal, wholesale to
~150 local power companies in TN/KY/MS/AL/GA/NC/VA), Florida Power & Light, Duke Energy
Florida, Tampa Electric, JEA, OUC, Gulf Power (now FPL NW). Plus Georgia's EMCs (Oglethorpe
Power G&T, ~38 members) and municipals (MEAG).

**The wholesale layer does not exist.** No capacity market, no ancillary market a BTM asset can
bid into. Every dollar of dispatch value comes from the utility's own program or nothing. This
makes the presence layer *more* decisive here, not less — a `No` in `res_dispatch` means zero
revenue in that bucket, full stop. Phase 4 (wholesale) is skipped; the region gets an `rto`
value of `SERC`, `TVA`, or `FRCC` and renders as "no wholesale market" in the drawer.

## Denominator

States: NC, SC, GA, AL, FL, TN. Six pulls, ≈150 records >10k. TVA distributors are numerous and
uniform — tag `rto=TVA` and use the TVA shortcut (cite TVA EnergyRight programs once).

## Load-bearing utilities (≈25)

Duke Energy Carolinas, Duke Energy Progress, Dominion Energy South Carolina, Santee Cooper,
Georgia Power, Alabama Power, FPL, Duke Energy Florida, Tampa Electric, JEA, OUC, Gainesville RU,
Lakeland, Tallahassee, TVA (as the program provider for its LPCs), Nashville Electric Service,
Memphis Light Gas & Water, Knoxville UB, Chattanooga EPB, Huntsville Utilities, plus the 3–4
largest Georgia EMCs (Jackson EMC, Cobb EMC, Sawnee EMC, GreyStone) and the NC co-ops' G&T
(North Carolina EMC).

## Program families

- **Habit**: Duke's residential TOU (NC/SC — and the 2023–24 NC rate-design overhaul with the
  new TOU-CPP default option), Georgia Power's Smart Usage and Nights & Weekends rates, Alabama
  Power's Time Advantage, FPL's TOU, TECO's TOU, TVA's Time-of-Day (via LPCs; uneven adoption —
  check per LPC), Chattanooga EPB's TOU.
- **Dispatch**: Duke's Power Manager (AC switch) and EnergyWise, Duke's BYOT; Georgia Power's
  Smart Thermostat program; Alabama Power's Smart Neighborhood/BYOT; FPL's On Call (the largest
  residential DLC program in the country, ~800k switches — reference case); TVA's PowerFlex (C&I)
  and Smart Thermostat Rewards via LPCs; Duke's PowerPair (NC solar+storage incentive with a
  battery-control track — the region's most important storage program; capture in detail);
  Santee Cooper's programs.
- **Export**: NC net metering's 2023 successor (Duke's new "Bridge Rate" and the residential
  solar choice tariffs with minimum bills and non-bypassable charges); SC Act 62 successor
  tariffs; Georgia's monthly netting with the 5,000-customer instantaneous-netting cap; Alabama's
  capacity reservation charge on solar customers (the famous $5/kW fee — capture the 2024–25
  litigation status); Florida's net metering (HB 741 veto history — full retail NEM survives);
  TVA's Dispersed Power Production and the Green Connect rules per LPC.
- **Storage incentives**: Duke PowerPair (NC), Duke's SC storage pilot, Santee Cooper, FPL's
  SolarTogether (not storage), Georgia Power's BYOD battery pilot.

## Interconnection

NC (NCUC — the 2023 rewrite), SC (PSC — Act 62), GA (PSC — thin; Georgia Power's own procedures
dominate), AL (PSC — near-absent; Alabama Power procedures), FL (PSC Rule 25-6.065 — Tier 1/2/3
by kW, the standard model), TN (no PUC jurisdiction over TVA LPCs; TVA's own interconnection
rules). Two Opus agents: {NC, SC, GA} and {AL, FL, TN}.

## Cluster split

- Presence: A {NC, SC} (≈45), B {GA, AL} (≈55), C {FL, TN} (≈50).
- Programs: Duke ×2 + Dominion SC + Santee Cooper (Opus — NC/SC tariff design is complex);
  Southern ×2 + FL IOUs (Sonnet); TVA + LPCs + munis (Sonnet).
- Interconnection: two Opus agents.
- Wholesale: **skip**. Record a single `programs.csv` row per balancing authority stating
  "no organized wholesale market; BTM DER cannot bid" with a source, so the drawer explains the
  absence rather than showing nothing.

## Hard problem to flag

Alabama Power's solar fee and Georgia's instantaneous-netting cap are anti-DER rules that make
the *habit* bucket look fine (TOU exists) while the *export* economics are terrible. The presence
layer will paint these green. The interconnection/export layer is what tells the truth here —
make sure the drawer surfaces `export_credit_basis` prominently for this region.
