# ic_NEa gaps (MA, RI, CT) - run 1, 2026-09-26

Run 1 was cut short by a session usage limit after the MA state row. A relaunch should resume per SKILL.md section 2.

## Done
- MA state row written (Primary: mass.gov net metering guide; interconnection facts from NSTAR M.D.P.U. No. 55D eff 2026-05-01 https://www.mass.gov/doc/iirg-materials-18/download, MECo M.D.P.U. No. 1579 eff 2025-04-15, and Eversource MA application page https://www.eversource.com/residential/about/doing-business-with-us/interconnections/massachusetts/massachusetts-application-to-interconnect for fees).

## Not done / not verified
- MA blank or Unclear cells: nem_sizing_rule, external_disconnect, insurance amounts, standby_charge, storage_counts_toward_cap, grid_charging_allowed (read https://www.mass.gov/info-details/energy-storage-and-net-metering and D.P.U. 17-146-A https://www.massaca.org/pdf/D.P.U.%2017-146-A%20Order%2002.01.19.pdf - PDF did not render text via web_fetch or the browser pane), ConnectedSolutions non-export path, UL 1741 SB requirement, D.P.U. 25-48 outcome and CSM fee.
- MA fee schedule Table 6 (tariff page 67) is past the web_fetch truncation point; the $4.50/kW figure comes from Eversource's own application page (Primary for Eversource) - National Grid/Unitil schedule assumed identical but not verified.
- RI state row: NOT WRITTEN. Leads: RI Gen. Laws 39-26.4; post-2023-04-15 projects reported at reduced credit (OER page https://energy.ri.gov/renewable-energy/net-metering); RI Energy interconnection tariff R.I.P.U.C. No. 2180-series not located.
- CT state row: NOT WRITTEN. Leads: RRES netting vs buy-all (2026 buy-all $0.3289/kWh; netting Solar Energy Adjustment $0.0402/kWh); PURA interconnection standards (Guidelines for Generator Interconnection); ESS program interconnection requirements.
- Utility file: header only. No delta rows written for any of the 12 target utilities. Chunk leads for munis: Reading (fuel-charge-only export credit, https://www.rmld.com/home/pages/solar-choice-frequently-asked-questions), Holyoke (retail, secondary only), Taunton (two tiers <=60 kW / 60-2000 kW, secondary only), Peabody (policy PDF https://www.pmlp.com/DocumentCenter/View/148/Net-Metering-Policy-PDF), Chicopee and Braintree (no NM lead).
- Rows from leads were deliberately NOT written so a relaunch treats RI, CT and all utilities as remaining work rather than finished rows.

## Run 2 (resume), 2026-09-26

### Done
- MA row cells filled: grid_charging_allowed = Requires non-export (mass.gov 'Energy storage and net metering' summary of D.P.U. 17-146-A: exporting ESS must charge only from the NM facility; non-exporting ESS may grid-charge; 30-second inadvertent-export limit, uncompensated; non-conforming paired systems lose NM eligibility and cap allocation, may interconnect as QF). storage_allowed extended with the retrofit rule (System of Assurance reporting). MECo tariff citation updated to M.D.P.U. No. 1599 (eff. 2025-06-01, cancels 1579).
- RI state row (Primary: R.I. Gen. Laws 39-26.4-2/-3; RIPUC Order 22991; Docket 4982 open-meeting minutes 2019-12-17; R.I.P.U.C. No. 2258). grid_charging_allowed = No.
- CT state row (Primary: RRES Program Manual v2024.1; Eversource/UI <=25 kW guidelines; Eversource CT application page; Eversource RRES FAQ filed in Docket 22-08-01). grid_charging_allowed = Unclear.
- Utility rows (7): Reading, Peabody, Taunton, Holyoke, Chicopee, Braintree (all deviates_on=all), CL&P (add-on Netting path).
- No row for NSTAR, MECo, FG&E, Rhode Island Energy, United Illuminating: no verified deviation from their state rows (RI state row is effectively RI Energy's tariff; MECo expedited/standard fee $4.50/kW same as Eversource per secondary search summary).

### Not verified / open
- MA: storage_counts_toward_cap, nem_sizing_rule, external_disconnect, insurance dollar amounts, standby_charge still blank/Unclear (tariff insurance section is past web_fetch truncation). D.P.U. 17-146-A order PDF itself still not read - used DPU's own summary page.
- RI: whether the post-2023-04-15 20% credit reduction applies to behind-the-meter systems (statute ties it to the 275 MW ground-mounted remote cap); excess-credit basis conflict (statute: ISO-NE energy clearing price; OER page: last resort service rate); R.I.P.U.C. No. 2258 Sec. 4.3 non-export text and Sec. 10 insurance amounts (truncated); Docket 24-34-EL storage tariff outcome; IEEE 1547-2018/UL 1741 SB date.
- CT: grid charging with Netting/legacy NM - no rule found (Unclear). CT Fast Track/Study guideline PDF returned empty; UI fees/insurance assumed same as Eversource (state row fee/insurance values are Eversource-sourced). RRES/NRES program end date and 2025-2026 manual version not verified; 2026 rates are from Eversource help-center article (secondary). NRES (non-res >25 kW) not researched. Eversource Appendix H add-on Netting conditions not read. Flexible interconnection Docket 25-01-27 outcome pending.
- Munis: Peabody procedure is dated 2015 (may be superseded; no storage terms). Braintree DG tariffs dated 2017 and DG Interconnection Policy not found online; Braintree Electric Light Department not present in data/processed/programs.csv (join key unverified). Chicopee tariff silent on storage. Holyoke: chunk lead (nuwattenergy) claiming full-retail NM is WRONG - HG&E is buy-all/sell-all at a wholesale-based DG credit.
