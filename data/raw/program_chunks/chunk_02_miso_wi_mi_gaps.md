# Cluster 2 — MISO Wisconsin & Michigan: Research Gaps

## Utilities with no retail tariffs found (structural gap, not an oversight)

- **Dairyland Power Cooperative (WI)** — Confirmed to be a generation & transmission (G&T) wholesale cooperative that supplies power to 24 member distribution cooperatives across WI/MN/IA/IL. It does not sell retail power directly to end-use customers and therefore has no retail TOU/DR/EV/export-compensation tariffs of its own to report. Its member co-ops (which are NOT on the target list for this cluster) hold the retail tariffs. Battery storage and solar activity by Dairyland is limited to wholesale-side generation projects (e.g., USDA PACE-funded battery/solar projects), not customer-facing programs.
- **Wolverine Power Cooperative (MI)** — Could not locate a working corporate website. `wolverine.org` is a squatted/for-sale domain, `wolverinepower.com` belongs to an unrelated company (Wolverine Power Systems, a Generac generator dealer), and `wolverinepower.coop` returned an empty/unresponsive page. Wolverine Power Cooperative is understood to be a Michigan G&T wholesale cooperative (headquartered in Cadillac, MI) supplying member distribution co-ops, similar in structure to Dairyland — meaning it likely has no direct retail tariffs of its own either, but this could not be confirmed with a live source in this session.
- **Michigan Public Power Agency (MPPA)** — `mppa.org` and `mppa.org/about` returned near-empty responses (likely JS-rendered content not captured by static fetch). MPPA is understood to be a joint action agency that provides wholesale power supply, financing, and shared services to its municipal member utilities (e.g., small Michigan municipal electric systems not on this cluster's target list) — it is not itself a retail utility and would not be expected to hold retail TOU/DR/EV/export tariffs. This could not be verified with a live source in this session.

## Utilities fully researched with programs found

The following 16 utilities were successfully researched with verified tariff/program data captured in the CSV: Wisconsin Electric Power Co (We Energies), Wisconsin Public Service Corp, Wisconsin Power & Light Co (Alliant Energy), Madison Gas and Electric Co, Northern States Power Co - Wisconsin (Xcel Energy), Superior Water Light & Power Co, WPPI Energy, Consumers Energy Co, DTE Electric Co, Upper Peninsula Power Company (UPPCO), Upper Michigan Energy Resources (UMERC), Lansing Board of Water & Light, Holland Board of Public Works, Traverse City Light & Power, Cloverland Electric Cooperative, Great Lakes Energy Cooperative, Indiana Michigan Power - Michigan.

## Notes on partial/lower-confidence findings within the covered utilities

- **UMERC (Upper Michigan Energy Resources)**: Its own MPSC No. 1 tariff book (combined WEPCo/WPSC rate zones) confirms rate codes Rg2 (residential TOU) and Cp-I (large C&I interruptible rider) exist, but the fetched tariff excerpt was table-of-contents/index level only — specific $/kWh and $/kW figures were not recoverable from the extracted text, so those two rows are marked Low confidence. The Distributed Generation Program (DG-1) tariff was fetched in full and is High confidence.
- **Northern States Power Co - Wisconsin (Xcel)**: Interruptible Service Option Credit — no published $ credit figures found; marked Low confidence.
- **DTE Electric**: Several C&I interruptible/curtailable riders (D3.3, D8, Rider 10, Rider 12, Rider 1.1 Metal Melting) do not publish exact $ credit amounts on the public site; marked Medium confidence.
- **Lansing Board of Water & Light**: RES22 (separately metered EV charging rate) tariff exists but rate figures were not present in the extracted PDF text; marked Low confidence.
- **Indiana Michigan Power - Michigan**: DG Rider / legacy Net Metering Service Rider 1 (NMS-1) confirmed to exist (referenced on the EV charging page) but no dedicated tariff page/PDF with credit rates was fetched; marked Low confidence. The RS-PEV EV charging tariffs (Options 1-3) are High confidence with full published rates.
- **Holland Board of Public Works / Traverse City Light & Power / Cloverland Electric Cooperative / Great Lakes Energy Cooperative**: All fully verified with High confidence tariff/program pages and PDFs.

## Search/access constraints encountered

- WebSearch tool budget was exhausted partway through the session (200/200 calls used), forcing exclusive reliance on direct URL fetches (mcp__workspace__web_fetch) with known or guessed utility URL patterns for the remainder of the research.
- UPPCO's `wp-content/uploads` PDF paths returned empty content via direct fetch; the same files hosted on UPPCO's CloudFront CDN (`d2x43qaqyo0a2i.cloudfront.net`) worked and were used instead.
- `umerc.com` is a squatted/parked domain unrelated to Upper Michigan Energy Resources; the real corporate site is `uppermichiganenergy.com`.
- `wolverine.org` and `wolverinepower.com` do not belong to Wolverine Power Cooperative (see gap note above).
