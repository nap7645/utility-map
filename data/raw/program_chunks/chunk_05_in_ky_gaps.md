# Cluster 5 (Indiana + Kentucky) — Research Gaps

## Utilities covered with at least one verified row
NIPSCO, Duke Energy Indiana, AES Indiana (formerly IPL), Indiana Michigan Power (AEP/PJM), CenterPoint Energy Indiana South (formerly Vectren), Hoosier Energy, Wabash Valley Power Alliance, Jackson County REMC, Richmond Power & Light, Louisville Gas & Electric, Kentucky Utilities, Duke Energy Kentucky (PJM), Kentucky Power (AEP/PJM), East Kentucky Power Cooperative, Big Rivers Electric (via member co-op Kenergy), Owensboro Municipal Utilities.

## Utilities checked but with little/no verifiable retail program found
- **Indiana Municipal Power Agency (IMPA)**: IMPA is a wholesale joint-action agency supplying 53 municipal members; it does not publish a single retail tariff. Its board adopted a resolution permitting purchase of excess member-generated energy, but no published $/kWh rate, TOU rate, or DR program could be found at the IMPA (wholesale) level. Retail net metering / EDG-equivalent terms are set independently by each of its 53 member municipal utilities (e.g., Richmond P&L, which is covered separately). Flagging as a gap for IMPA itself — recommend researching individual IMPA member cities if per-city granularity is needed.
- **Anderson Municipal Light & Power**: Confirmed net metering is offered (city ordinance / IURC filing 50507), but no specific $/kWh credit rate, cap size, or TOU/DR program details could be located in public search results. Rate schedule details were not found in an accessible tariff PDF.
- **Jackson County REMC**: Confirmed net-metering-like interconnection exists (rate schedule "R13 Rate-G" referenced) and a smart-thermostat DR pilot (with Hoosier Energy/NRECA) is documented in detail and included as a row. However, the specific solar/DG credit rate ($/kWh) for Jackson County REMC could not be verified from public sources — flagged Low confidence would have been needed; no export-comp row emitted for this utility beyond noting the pilot.
- **Big Rivers Electric**: As a generation & transmission cooperative, Big Rivers does not serve retail customers directly — retail net metering/DG terms are set by its three member cooperatives (Kenergy Corp, Meade County RECC, Jackson Purchase Energy Corp). Only Kenergy's program was verified (interconnection required, capacity-constrained by substation, no published $/kWh credit rate found). No verifiable TOU, DR, or EV program found at the Big Rivers G&T level itself.
- **East Kentucky Power Cooperative**: EKPC is also primarily a G&T cooperative; the interruptible industrial service program is real and documented (via PSC-filed Industrial Power Agreements), and net metering/DG credit terms are set per member distribution cooperative rather than uniformly by EKPC. No EKPC-level TOU, CPP, storage incentive, VPP, or EV program could be verified.

## Program categories not found for any IN/KY utility in this cluster
- No dedicated **Storage-Incentive** (upfront $/kWh rebate for BESS) program was found at any Indiana or Kentucky utility in this cluster (Duke's PowerPair/Power Manager Battery Control programs are confirmed only in the Carolinas, not Indiana or Kentucky — excluded for lack of verification).
- No **VPP** (aggregated dispatchable BESS fleet) program beyond Hoosier Energy's broader CPMP (which is closer to C&I curtailment/capacity) was verified for any utility in this cluster.
- No residential **RTP-Rate** (hourly/real-time indexed) retail rate was found for any IN/KY utility; NIPSCO's Rate 831/832 and I&M's curtailment riders are large-C&I products tied to wholesale prices but are not true hourly retail RTP tariffs.
- Kentucky Power's residential EV rate / managed charging program (if any, beyond the interruptible/net-metering programs found) could not be verified — Kentucky Power's EV program specifics were not found in search results (only Kentucky Power's general PJM DR/net-metering info was verifiable).
- Duke Energy Kentucky's demand response / interruptible program (analogous to LG&E/KU's Curtailable Service Rider or Duke Indiana's IDR) could not be located with a working source link; only a Time-of-Day rate tariff reference (partially confirmed, low confidence, cancelled/superseded tariff page) was found.

## Utilities not independently researched in depth (time-boxed)
- Anderson Municipal Light & Power — only net metering existence confirmed, not rate specifics (see above).
- Indiana Municipal Power Agency — wholesale-only entity, no direct retail tariff (see above).

## Notes on RTO/market labeling
- LG&E and Kentucky Utilities are **non-RTO** (self-supply / not members of MISO or PJM as a bundled retail utility) — labeled `Non-RTO` in the `rto` column per cluster instructions, even though this value is not in the base schema enum. This is intentional per the cluster note to flag LG&E/KU as non-RTO.
- Duke Energy Kentucky and Kentucky Power are labeled `PJM` (AEP and Duke transmission territory in Kentucky is functionally under PJM).
- Big Rivers Electric and Owensboro Municipal Utilities are labeled `MISO` (Big Rivers joined MISO as a transmission-owning member in 2013; western KY footprint is inside the MISO footprint) — flagged Low/Medium confidence on program specifics given limited published detail.
