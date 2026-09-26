# ic_SEb gaps (AL, FL, TN) -- run 2026-09-24, INCOMPLETE

Run stopped early: WebSearch hit the session limit and web_fetch/browser tools became unavailable (auto-mode classifier timeouts). Relaunch with the same prompt to resume; completed rows below are final.

## Done
- State FL (Primary, Rule 25-6.065 full text via LII + s. 366.91 F.S.).
- State AL (Secondary, WBHM/Inside Climate News 2026-03-31). Needs upgrade to Primary from Alabama Power RGB.pdf and Rate_PAE.pdf (URLs found, not read): https://www.alabamapower.com/content/dam/alabama-power/pdfs-docs/Rates/RGB.pdf , https://www.alabamapower.com/content/dam/alabama-power/pdfs-docs/Rates/Rate_PAE.pdf ; court opinion https://www.selc.org/wp-content/uploads/2026/03/Doc.-165-2026.03.25-Memorandum-Opinion.pdf
- Utility: Florida Power & Light Company (Primary).

## Not done
- State TN row (TVA interconnection / Dispersed Power Production / Green Connect) -- not written; no source read.
- Utility rows still to research: Alabama Power Company; Duke Energy Florida, LLC; Tampa Electric Company; JEA; Orlando Utilities Commission; Lee County Electric Cooperative (LCEC); Withlacoochee River Electric Cooperative; SECO Energy; Clay Electric Cooperative, Inc.; Lakeland Electric; City of Tallahassee Utilities; Gainesville Regional Utilities; Nashville Electric Service; Memphis Light, Gas and Water Division; Knoxville Utilities Board; EPB (Electric Power Board of Chattanooga); Huntsville Utilities.

## Open questions in written rows
- AL: whether SELC appealed the 2026-03-25 M.D. Ala. ruling to the 11th Circuit; any small-system exemption from RGB; current Rate PAE avoided-cost value; whether batteries/grid charging are addressed in RGB (storage_allowed/grid_charging left Unclear).
- FL: 25-6.065 still cites IEEE 1547-2003/UL 1741-2005; no 1547-2018 transition found. grid_charging_allowed Unclear at state level (rule silent); FPL explicitly bars battery export on NEM systems. Whether adding an AC-coupled battery to an FPL NEM system counts as a gross-power-rating increase requiring a new agreement: Unclear.
- FL munis/co-ops: s. 366.91(6) requires each to adopt its own NEM + interconnection program -- terms per utility not yet collected.


---
# Resume run 2026-09-26
## Done this run
- State AL upgraded to Primary (Alabama Power RGB.pdf, Rate_PAE.pdf, Special_Rules_PAE.pdf, APC DER Interconnection Process July 2025, DER TIR Guidebook V3.2 Feb 2026).
- State TN written (TVA DPP PPA terms + Dec 2025 CSPP price schedule + Green Connect FAQ). Primary.
- Utility rows: Alabama Power, Duke Energy Florida, Tampa Electric, JEA (Secondary), OUC, LCEC, WREC, SECO, Clay Electric, Lakeland Electric.
- WebSearch hit weekly limit mid-run (after Lakeland).

---
# Resume run 2026-09-26 (#2) -- utility rows COMPLETE
## Done this run
- Utility rows added: City of Tallahassee Utilities (Primary); Gainesville Regional Utilities (Primary); Nashville Electric Service (Primary); Memphis Light, Gas and Water Division (Primary); Knoxville Utilities Board (Primary); Huntsville Utilities (AL, Primary).
- State cells filled: FL standby_threshold_kw; TN ic_fast_track_kw, ic_simplified_kw, ic_timeline_days, standby_threshold_kw (all "set by each LPC" with examples from utility rows). All 3 state rows now have no blank cells.

## TVA LPC decisions
- NES, MLGW, KUB, Huntsville all deviate from the TVA state row (own export-purchase programs, fees, charges or disconnect/insurance terms) -> rows written.
  - NES and Huntsville have their own LPC-run buyback programs (NESolar Savings/Connect; HU Solar Connect 6.427c/kWh 2026) instead of relying only on TVA DPP.
  - MLGW: no buyback of its own, but a $14.40/mo residential Electric Service Availability charge on self-generators, and exports without DPP get nothing; application fee $250 + $5/kW.
  - KUB: $500 application fee, no insurance, 60-day notice + KUB approval for any component change (battery retrofit).
- EPB (Electric Power Board of Chattanooga): NO ROW. epb.com / business.epb.com publish no customer-generation interconnection terms (only Solar Share community solar, Green Switch/Flex/Invest). Only third-party sites (tennesseesolarauthority.com, doineedapermit.org) claim a $500 fee, and an old EPB snippet mentions a $150 charge from the retired Green Power Providers era -- neither verified. Whether EPB deviates from TVA rules: Unknown, not "follows unchanged".
- Other TVA LPCs (the ~150 co-ops/munis beyond these five) not checked -- out of scope for this wave.

## Open items / could not verify
- grid_charging_allowed is Unclear for all 6 new rows: none of the utilities publishes a grid-charging rule. NES program rates apply only to solar-generated energy; Huntsville says battery-commutated systems can't run grid-parallel and batteries typically need open-transition throw-over switches (so grid-parallel battery export looks restricted).
- Adding a battery to an existing system:
  - Tallahassee: agreement terminates on any PV system modification, so a new agreement is required.
  - KUB: 60-day notice and approval required.
  - NES: written approval required for any capacity expansion.
  - GRU: must give notice; GRU may audit.
  - Whether a battery retrofit moves a pre-April-2024 GRU retail-NEM customer onto fuel-rate credits: Unclear.
- GRU: the current interconnection agreement (Revised 04/08/2024) is an image-only PDF and was not read. Insurance amounts differ between the web page (T2 $1M / T3 $2M) and the 2022 agreement (T2 $300k / T3 $1M). Grandfathering of pre-April-2024 NEM customers comes only from news reports (Secondary).
- MLGW: the insurance amount in the Interconnection and Parallel Operation Agreement was not read.
- KUB: read the older agreement PDF; the site now links KUB_Interconnection_Agreement_2024.pdf (not read).
- Huntsville: the Solar Connect interconnection agreement is a web form (tfaforms) and was not read; the program participation cap in MW is not published.
- NES: current NESolar subscription against the 10 MW / 35 MW caps is not published; the NES Interconnection and Operating Agreement was not read.
