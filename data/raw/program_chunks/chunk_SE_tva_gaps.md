# chunk_SE_tva — gaps and unverified items

## Checked, no independent program found (beyond generic TVA EnergyRight pass-through, already captured on the TVA rows)

- **Huntsville Utilities** — checked residential rates page (hsvutil.org) and business incentive
  programs page. Only standard flat Residential Service (Schedule RS, ~11.2c/kWh effective rate)
  and generic EE/HVAC/weatherization rebates found. No published TOU rate, no DR/load-control
  program, no EV-specific rate or rebate found via web search or site fetch. hsvutil.org pages did
  not render full content through `web_fetch` (JS-heavy); a manual browser check would be needed to
  fully rule this out — marking `Unknown` rather than `No`.
- **Volunteer Energy Cooperative (VEC)** — residential/commercial rate pages show only flat
  Schedule RS / SRS / GSA rates (TVA wholesale pass-through). VEC's own energy-efficiency page
  offers "EnergyRight Residential Services," which is TVA's program, not a VEC-specific TOU, DR, or
  EV offering. No VEC-specific dollar figures beyond what's already on the TVA EnergyRight rows.
- **Cumberland Electric Membership Corporation (CEMC)** — CEMC's Energy Solutions page links
  directly to TVA's Smart Thermostat Rewards / EnergyRight Home Energy Resources / Heat Pump Loan
  Program; no CEMC-specific enrollment numbers, dollar figures, or independent TOU/DR/EV program
  found. CEMC's own rate sheets (cemc.org/wp-content/uploads/.../RATES-*.pdf) show a standard
  TVA-driven demand/energy tariff; large accounts (>5,000 kW) are billed on TOU/MS schedules, which
  is the TVA wholesale TOU structure already captured on the TVA "Wholesale Time-of-Use Rate
  Structure" row, not a CEMC retail program.

## Not independently verified / soft spots

- **TVA PowerFlex and Peak Rewards dollar values** (rows already in the CSV from a prior pass) are
  not published as a $/kW rate anywhere found — TVA and Enel (Peak Rewards administrator) state the
  programs pay a "bill credit" without a public rate card. Treat as a real gap for the consulting
  summary: PowerFlex/Peak Rewards $/kW cannot be quantified from public sources.
- **KUB eScore Smart Thermostat Pilot** — no cash incentive amount published; appears to be a
  device-provision + event-participation program only (no $/event or annual bill credit found).
- **EPB Time Shift / Night Shift rates** are quoted inclusive of the variable TVA Fuel Cost
  Adjustment "as of 11/1/24" per EPB's own site — these will drift with the monthly TVA fuel
  adjustment and should be re-checked periodically; the underlying flat off-peak/on-peak spread
  (energy charge only, ex-fuel) was not separately published.
- **KUB GSA-TOU** pilot is capped at contract demand <=1,000 kW; KUB references TDGSA/TDMSA rates
  for larger customers but those tariff sheets were not located/fetched this pass.
- Other TN LPCs not in this run's target list (e.g., Chattanooga's neighbors, other smaller TVA
  distributors) were out of scope per the handoff spec (only NES, MLGW, MTE, KUB, EPB, Huntsville,
  Volunteer EC, Cumberland EMC + TVA itself were targeted).
