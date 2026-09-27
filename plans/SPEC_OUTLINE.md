# Utility Map — "presentable" build spec (outline)

Fill in each section. Where a **[default: …]** is given, leave it blank to accept it — only write
where you disagree. Items marked **DECIDE** block the build; everything else has a workable default.
Aim: one launch wave per region + one UI pass, no mid-build questions.

---

## 1. Definition of done
- **DECIDE** Who is the first viewer? (you in a client meeting / a client alone / a prospective
  partner or investor) — this sets polish level and how much jargon is allowed.
- **DECIDE** The 3–5 demo flows that must work flawlessly, written as steps.
  e.g. "Type a client address → see utility, RTO, programs with $ values, interconnection rules
  → export a one-page summary."
- Deadline and what gets cut first if it slips. [default: cut §4 features before §3 coverage]

## 2. Audience & access
- Public URL (GitHub Pages, as now) or private? Any password/obscurity? [default: public, no client data ever stored]
- Branding: product name, company name, logo, colors, contact line. [default: neutral, no branding]
- Desktop only, or must work on a phone in a meeting? [default: both; desktop primary]

## 3. Coverage (data)
- **DECIDE** Regions required for the demo, in order. Current state:
  done — MISO, PJM, NYISO, CAISO/CA, Southeast, ISO-NE · partial — West (W4 + programs +
  interconnection + wholesale left) · not started — SPP, ERCOT/Texas, remaining states (AK, HI, KS,
  NE, OK, TX, etc.)
- **DECIDE** Texas: include? If yes, how to show retail-choice areas (a) "programs via retail
  provider — see list", (b) list top REPs' DR/TOU/VPP offers, (c) grey out with an explanation.
- Depth per region. [default: presence for every territory >10k customers; full program rows for
  the utilities covering ~85% of customers; interconnection for every state; wholesale per RTO]
- Clean-up passes wanted before demo? (the ~100–150 fully-Unknown territories; PowerSouth co-ops;
  JS-only municipal sites) [default: one fill pass per region, then stop]
- Staleness tolerance: how old may a row be before it is flagged? [default: 12 months; ISO-NE
  ConnectedSolutions and GMP 6 months]

## 4. Features — mark each Must / Nice / Later
- **Address lookup → drawer** (exists). Anything missing from the drawer?
- **Bill structure / rate calculator**: show the full residential/C&I tariff (customer charge,
  energy tiers, TOU windows, demand charge, riders)? Or compute an annual bill from a load profile?
  Inputs you'd type in a meeting?
- **$ value estimate per program** for a given system (e.g. "5 kW / 13.5 kWh battery here earns
  ~$X/yr from programs + TOU arbitrage")? Assumptions you want exposed vs fixed.
- **Hosting capacity**: link out to each utility's map (DOE list) vs. ingest data. [default: link out]
- **Aggregator layer**: which aggregators (Tesla, Sunrun, EnergyHub, Voltus, CPower, Enel…) and
  what to show (where they operate / which programs they enroll in).
- **EIA-861 overlay**: which fields (customers, sales, avg price ¢/kWh, DR enrollment, NEM MW)?
- **Historical LMP**: which nodes/zones, what view (heatmap, TB4 spread, monthly averages)?
- **Export**: PDF one-pager per utility / CSV of programs / shareable link to a utility? 
- **Comparison view**: two or more utilities side by side?
- **Search & filters**: filter by program type, $ value threshold, battery-eligible, etc.?
- Links from the map into the Python design/economics app (tariff + program JSON export)? [default: Later]

## 5. UI / presentation
- Layout changes wanted (panel, legend, drawer order). Screenshots or sketches help most.
- Plain-language rules: which terms to ban/rename (e.g. RTO names, "C&I", "BYOD"). [default:
  plain English first, technical term in parentheses]
- Units and number formats. [default: ¢/kWh, $/kW-month, $/yr per household; USD; dates ISO]
- Source/confidence display: keep Primary/Secondary/Unverified badges? [default: keep]
- Disclaimer text (not legal/financial advice, verify with utility). [default: short footer line]

## 6. Accuracy bar
- Minimum confidence to show a number as fact vs. "reported". [default: Primary = fact;
  Secondary = "reported"; Unverified = hidden unless toggled]
- Must every $ figure link to its source? [default: yes]
- Spot-check protocol before demo: which utilities you personally know and will check.

## 7. Budget & process
- Token/credit budget for the push, and hard stop. [rough: finish West ~1.5M; SPP ~2M; Texas
  ~2–3M; clean-up passes ~0.3M/region; each major feature ~0.2–0.5M]
- Parallelism: max agents at once. [default: 3]
- Check-in cadence: after each region / only at the end / only on blockers. [default: blockers only]
- Who pushes: you (current) or allow me a deploy key? [default: you]

## 8. Out of scope (explicitly)
- List what must NOT be built or researched this round (keeps agents from drifting).

## 9. Known decisions already made (confirm or override)
- Program buckets: time-based pricing vs. paid device control; homes vs. businesses.
- Denominator: HIFLD territories >10k customers; one row per operating company.
- Source tiers: Primary / Secondary / Unverified; blanks beat guesses; checked "No" ≠ "Unknown".
- Utilities with ≥3 researched program rows: missing families shown as "None found".
- Basemap OSM grayscale; boundary snapshot committed as GeoJSON (you re-run it per new state).
