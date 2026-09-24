# scan_F gaps — PA/NJ/MD/DE/VA/WV/DC cluster (31 utilities)

Researched 2026-09-24. Notes on what could not be fully verified, and why.

## Full Unknown across most/all cells (search budget or JS/thin sites)
- **City of Newark, DE (13519)** — city rate-increase notices, ordinance, and FAQ pages checked; no TOU, dispatch, or C&I curtailment program could be confirmed. Full current rate-schedule PDF exists (cityofdover.gov-style tariff on newarkde.gov) but was not opened in depth.
- **Borough of Butler, NJ (2650)** — only NJ BPU LEAC (fuel adjustment) filings surfaced; no rate tariff or DR/thermostat program page found on the borough's own site.
- **Easton Utilities Commission, MD (5625)** — own electric tariff (P.S.C. Md. No. 11, eastonutilities.com) located but the PDF itself was not opened; only a secondary description of the GS-L rate class was available.
- **City of Dover, DE (5335)** — confirmed a Transmission Voltage Interruptible Service (IT) classification in the utility's own tariff document title, so ci_dispatch=Yes; res_habit, res_dispatch, and ci_habit remain Unknown because the tariff PDF's rate tables were not opened.

## Partially verified — one or two cells confirmed, others Unknown due to per-co-op detail not checked
- **PA Allegheny Electric Cooperative members** (Valley Rural, REA Energy, Northwestern Rural ECA, Tri-County Rural, United Electric, Somerset Rural) — res_dispatch confirmed Yes via Allegheny's own CLMS member list (Secondary tier: G&T page naming the member, not each co-op's own program page). res_habit, ci_habit, ci_dispatch left Unknown — did not open each individual co-op's own rate-schedule page to check for a residential Time-of-Day rate or a C&I curtailable rider, which several confirmed members (Adams, Claverack) do have.
- **Northern Neck Electric Cooperative (13762)** — res_dispatch (smart thermostat) sourced from a search-engine synthesis of NNEC's Beat the Peak page rather than a direct fetch; tier marked Secondary rather than Primary for that reason.

## Confirmed "No" only for the specific cell checked, not the whole utility
- **Harrisonburg Electric Commission (8198)** — a trade-press (Public Power Association) article claims some C&I customers are on interruptible/load-reduction rates, but no interruptible rate schedule or program page could be found on HEC's own site to confirm it — left as Unknown rather than a guessed Yes.

## Cluster-note corrections worth flagging
- **Central Virginia Electric Cooperative (3291)** is *not* an ODEC member (confirmed against ODEC's own 11-member list) — it independently procures wholesale power and settles in PJM. One AI-search synthesis incorrectly suggested it receives ODEC power; that claim was disregarded as unsupported.
- **Bristol Virginia Utilities / BVU Authority (2248)** is on **TVA**, not PJM — confirmed via TVA's own local-power-company directory (its rate tariff also carries a TVA Fuel Cost Adjustment line). This is the only non-PJM row in the cluster.
- **Sussex Rural Electric Cooperative (40299, NJ)** turned out to be a member of **Allegheny Electric Cooperative's** PA/NJ Coordinated Load Management System (CLMS) alongside the Pennsylvania co-ops, not a stand-alone NJ program — its own site brands the same offering "Beat the Peak."

## Search budget
Did not exhaust the ~200-search budget, but stopped extending per-utility research once cells were Unknown-with-explanation for the smaller municipal utilities (Newark DE, Butler NJ, Easton MD) rather than making further speculative searches.
