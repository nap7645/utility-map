# NY interconnection — gaps and notes

## Row 2: LIPA / PSEG Long Island

### Premise check: is LIPA PSC-jurisdictional?
Confirmed NOT subject to the PSC's Standardized Interconnection Requirements (SIR) or to
PSL §66-j/66-l. LIPA's own December 2025 tariff-change filing states directly: **"LIPA is
not subject to PSL §66-j"** (citing Case 19-E-0079, *In the Matter of the Continuation of
Standby Rate Exemptions*). LIPA runs its own Small Generator Interconnection Procedures
("SGIP," current edition July 2026, https://www.lipower.org/wp-content/uploads/2026/07/July-2026-SGIP-1.pdf)
and its own Tariff for Electric Service net-metering rules (Leaf 34A–34K), separate from the
statewide SIR the six PSC IOUs use.

That said, LIPA has **not** simply ignored the state framework — it voluntarily built a
near-mirror of it:
- SGIP fast-track/expedited tiers are 50 kW and 300 kW, identical to the PSC SIR.
- SGIP requires UL 1741 Supplement B, identical to the PSC SIR.
- LIPA's residential net-metering size caps (25 kW, 100 kW farm-solar, 500 kW farm-wind,
  10 kW fuel cell/micro-CHP) track PSL 66-j/66-l almost exactly, even though LIPA says it
  isn't bound by that statute.
- LIPA's nonresidential net-metering cap is 5,000 kW — larger than the PSC utilities'
  2,000 kW PSL 66-j cap. This is a real, verified deviation, not an oversight.
- LIPA runs a Value Stack (VSC) tariff parallel to the PSC's VDER Value Stack (Statement
  No. 102, effective 2026-09-01), for Large Onsite/Offsite and Community Distributed
  Generation projects, while Mass Market customers can stay on 1:1 net billing.

### grid_charging_allowed — Unclear (verified search, not a guess)
The single most important cell. LIPA's SGIP requires ESS applicants to declare both
"Maximum Export" and "Maximum Import" (Appendix J, Sec I.E), so grid-charging is a
recognized, studied interconnection characteristic — a battery is explicitly allowed to be
sized/rated for import from the grid. What is **not** stated anywhere found in this pass is
how energy the battery imported from the grid and later exported is treated on the
compensation side: whether it's credited the same as PV-charged export, excluded, or
netted differently, under Net Billing, Value Stack (VSC), or Buyback (SC-11).
Checked and came up empty on this specific question:
- SGIP Sec I.E / Appendix J (declares import/export capacity, no crediting rule)
- LIPA Tariff Leaf 34A–34K net metering rules (confirms storage may be paired with a
  Mass Market NEM system without losing NEM eligibility, but doesn't distinguish
  charging source)
- LIPA Statement No. 102 (VSC) — component pricing only, no charging-source distinction
- The "December 2025 Tariff Changes" SC-11/SC-12 redesign document — addresses Buyback
  Contract Demand Charge exemptions for storage (15-year exemption for stand-alone ESS
  reaching SGIP Step 3 before 2030-12-31), but not grid-charging crediting

If this matters for the economics engine, the next document to pull is the PSEG Long
Island CDG Net Crediting Manual
(https://www.lipower.org/wp-content/uploads/2021/01/PSEG-Long-Island-CDG-Net-Crediting-Manual-Final.pdf)
and the full Standardized Interconnection Contract for Systems Including Energy Storage
referenced in SGIP Sec I.E — neither was opened in this pass.

### Other things not verified in this pass
- Whether a paired ESS's AC kW counts toward the 25 kW / 5,000 kW net-metering size cap
  (storage_counts_toward_cap = Unclear — the Tariff's cap language is written against the
  generator's rated capacity only).
- Whether LIPA's SGIP imposes a separate *external, manual, visible, lockable,
  gang-operated* disconnect switch requirement (like the PSC SIR does for systems >25 kW).
  The SGIP text found only describes an automatic (protective-relay) disconnect device.
  LIPA's "Red Book" (Specifications & Requirements for Electric Installations,
  https://www.psegliny.com/buildingrenovationservices/codesandstandards/redbook) may cover
  this and was not opened.
- SGIP application fee for systems under 50 kW (only the $750, 50 kW–10 MW fee schedule
  was found; carried over unchanged from the prior pass, still unverified for <50 kW).
- Exact SC-11/SC-12 rate schedule dollar figures (Service Charge $, Contract Demand Charge
  $/kW) — the December 2025 filing describes the rate design and mandatory/exemption
  structure but the actual tariff-leaf rate table was not pulled in this pass.
- Aggregate/program-wide subscription level for net metering or Value Stack (whether a cap
  is close to full) — no aggregate cap of any kind was found for LIPA, unlike the PSC row's
  PSL 66-j percentage cap, so there may simply be none to report.

### Access note
lipower.org required a fresh one-time browser access grant on nearly every navigation in
this session (the "site" scope grant request was silently downgraded to "once" by the
tool); psegliny.com was granted persistent site access. Direct `curl` from the shell
sandbox is blocked by an egress allowlist proxy (403 blocked-by-allowlist), so all fetching
went through the workspace web_fetch tool and the browser pane.
