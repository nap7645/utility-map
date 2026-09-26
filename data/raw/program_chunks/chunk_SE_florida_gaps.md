# Gaps — chunk_SE_florida.csv

Target utility list per PLAN.md SE wave 2 HANDOFF: Florida Power & Light Company; Duke Energy
Florida, LLC; Tampa Electric Company; JEA; Orlando Utilities Commission; Withlacoochee River
Electric Cooperative; Lee County Electric Cooperative (LCEC); SECO Energy; Clay Electric
Cooperative, Inc.; Lakeland Electric; City of Tallahassee Utilities; Gainesville Regional
Utilities. All 12 utilities now have at least one row.

## Could not verify / left blank

- **JEA** — jea.com pages (Distributed Generation Policy, SmartSavings, Net Metering PDF,
  commercial rates) return a bot-detection interstitial to automated fetches (captcha challenge
  page, no usable content) on every direct URL tried. Rows were built from Google-indexed
  snippets of JEA's own pages plus the PSC tariff-filing docket, so confidence is marked
  Secondary rather than Primary even though the cited URL is JEA's own page. JEA's specific
  dollar demand-charge rates ($/kW) for SmartSavings/Dual Flex Pricing were not found published
  anywhere — left blank rather than guessed. JEA large-industrial demand response program
  (mentioned in passing in search results) has no dedicated program page findable — not enough
  to write a row; flagging as a gap.
- **City of Tallahassee Utilities TOU rate** — the on/off-peak cent figures came from a
  third-party rate-comparison site (EnergyBot/utility-rates aggregator pattern), not talgov.com
  directly; talgov.com's own rate PDF was not reachable in the time available. Marked
  Unverified. Tallahassee's 2015 DOE-funded Automated Demand Response pilot (10 MW C&I) appears
  to be a completed demonstration project, not an ongoing tariff program — no row written for it
  since it's not a standing/current program.
- **Gainesville Regional Utilities (GRU) residential demand response / TOU** — search results
  reference "GRU offers residential time-of-use rates as an option for some customers" and a
  demand-response earnings program, but no dedicated residential DR or TOU tariff page/PDF with
  dollar figures was located (only the C&I General Service Time-of-Demand tariff, which is in
  the CSV). Treat GRU residential DR/TOU as unconfirmed — not written as a row per the
  never-invent rule.
- **SECO Energy, Clay Electric Cooperative, Withlacoochee River Electric Cooperative** — none of
  the three have a TOU rate, storage rebate, or standalone DR/curtailable-rate program found
  beyond the shared Seminole Electric "Cooperative Rewards" BYOT program and standard avoided-cost
  net metering. Their own rate-tariff PDFs (linked from clayelectric.com/rates,
  secoenergy.com's tariff PDF, and the WREC PSC filing) were found in search but not deep-fetched
  for exact avoided-cost cents/kWh figures — flagged as a follow-up if deeper verification is
  wanted.
- **Lee County Electric Cooperative (LCEC)** — the Interruptible General Service-Demand (IS-GSD)
  rebate is confirmed to exist (tariff sheet page 35) but the specific $/kW or $/event credit
  amount was not visible in the search snippet and the full tariff PDF was not deep-fetched;
  incentive_value_usd left blank. LCEC does not appear to run a residential TOU or DLC program
  (not found on lcec.net) — no row written.
- **Seminole Electric "Cooperative Rewards"** — confirmed as a BYOT program spanning "all nine"
  Seminole member co-ops (Talquin, Tri-County, Suwannee Valley, Clay Electric, Central Florida
  Electric, SECO Energy, Withlacoochee River Electric, Peace River, Glades Electric). Rows were
  written only for the three co-ops on our target list (Withlacoochee, SECO, Clay); Lee County
  Electric Cooperative (LCEC) is NOT listed among Seminole's nine members on seminole-electric.com
  and was not given a Cooperative Rewards row.
- **Storage/VPP pilots** — no dedicated battery-storage incentive or VPP pilot was found for any
  Florida co-op or municipal utility on the target list beyond OUC's Battery Storage Rebate (in
  CSV) and Duke Energy Florida's EnergyWise Home Battery Control (already in file from prior
  session). FPL, TECO, JEA, GRU, Tallahassee, and the co-ops appear to have no standalone
  storage/VPP program as of this research pass.
- Search budget used moderately; no utility was skipped entirely, but several rows above rely on
  Secondary or Unverified sources due to bot-blocked or unreachable primary tariff PDFs.
