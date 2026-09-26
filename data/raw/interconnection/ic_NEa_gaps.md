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
