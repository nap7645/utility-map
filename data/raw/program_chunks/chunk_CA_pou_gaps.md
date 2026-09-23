# CA POU chunk — gaps, RTO findings, and things not verified

## RTO / balancing-authority findings (the core deliverable of this job)

These are California publicly-owned utilities, but "in California" does not mean "in CAISO."
Each was checked individually against CAISO's participating-transmission-owner (PTO) list and
balancing-authority structure.

- **LADWP** — `WECC-nonRTO`. LADWP operates its **own balancing authority** (covers the City of
  LA plus the municipal utilities of **Glendale and Burbank**, which sit inside LADWP's BA
  footprint). LADWP is **not** a CAISO Participating Transmission Owner — it kept local control
  of its transmission/generation and ratemaking. It **does** participate in the CAISO Western
  Energy Imbalance Market (joined April 2021) and the LA Board of Water and Power Commissioners
  has approved participation in CAISO's Extended Day-Ahead Market (EDAM). So: own BA, non-RTO,
  but an EIM/EDAM market participant. Source: CAISO EIM entity agreement (ER21-101), LADWP news.
- **Glendale Water & Power** — `WECC-nonRTO`, same basis as LADWP: GWP's territory sits inside
  the LADWP balancing authority area, so it shares LADWP's non-CAISO-PTO status.
- **SMUD** — `WECC-nonRTO`. SMUD operates/is a member of **BANC** (Balancing Authority of
  Northern California, a joint powers agency SMUD created; other BANC members include Modesto
  Irrigation District, Redding, Roseville, Shasta Lake, Trinity PUD). SMUD/BANC is not a CAISO
  PTO. SMUD joined the CAISO EIM in April 2019 and BANC/SMUD have been evaluating EDAM
  participation (preferred option per BANC Commission, no confirmed go-live date found).
- **MID (Modesto Irrigation District)** — `WECC-nonRTO`. BANC member (see SMUD above), own/joint
  balancing authority, not a CAISO PTO. Did not find confirmation of EIM/EDAM participation
  specific to MID in this pass — flagged as unverified below.
- **TID (Turlock Irrigation District)** — `WECC-nonRTO`. TID runs **its own balancing authority**
  (TIDC), separate from BANC. Not a CAISO PTO. TID joined the CAISO Western EIM in March 2021 and
  its board voted (May, per American Public Power Association reporting) to join CAISO's EDAM,
  targeting 2027.
- **IID (Imperial Irrigation District)** — `WECC-nonRTO`. IID runs its own balancing authority
  and has historically been the highest-profile California POU holdout from CAISO markets. As of
  this research (Sept 2026), IID has signed implementation agreements to join **both** the EIM
  and EDAM, but its participation is **targeted for 2028** and has not started — IID is the last
  BA in California to join CAISO-operated markets. Treat IID as **not currently** an EIM/EDAM
  participant.
- **City of Anaheim Public Utilities** — `CAISO`. Anaheim is a CAISO **Participating Transmission
  Owner (PTO)** — it has turned over operational control of its transmission entitlements
  (including SCPPA-held shares of Mead-Adelanto/Mead-Phoenix) to CAISO. This is a different
  relationship than LADWP/SMUD/TID/IID: Anaheim is inside the CAISO controlled grid as a PTO, not
  an EIM-only participant. Source: Anaheim's CAISO PTO application and FERC electric tariff on
  file with CAISO.
- **Riverside Public Utilities** — `CAISO`. Also a CAISO Participating Transmission Owner,
  effective January 1, 2003 (own PTO application/tariff on file with CAISO). Riverside is grouped
  with Anaheim, Azusa, Banning, Colton, and Pasadena as the "Six Cities" — Southern California
  POUs embedded in/adjacent to SCE's transmission footprint under CAISO.
- **Silicon Valley Power (City of Santa Clara)** — `CAISO`. SVP is a Load Serving Entity
  operating **inside the CAISO Balancing Authority Area**, embedded within PG&E's transmission
  system under a Metered Subsystem (MSS) Agreement. Not a full PTO itself but squarely inside
  CAISO's BA, unlike the Southern California/Central Valley non-CAISO BAs above.

**Net takeaway:** of the 9 utilities covered, 3 (Anaheim, Riverside, Santa Clara/SVP) are inside
CAISO's balancing authority / PTO structure; 6 (LADWP, Glendale, SMUD, MID, TID, IID) run their
own balancing authorities outside CAISO, with varying degrees of CAISO market participation
(LADWP and TID in EIM now and approved for EDAM; SMUD in EIM, evaluating EDAM; IID and MID not
confirmed as current EIM/EDAM participants in this pass).

## Verification of the unverified leads given in the prompt

- **SMUD storage/VPP program** — CONFIRMED and well-documented. "My Energy Optimizer Partner+"
  (VPP with Swell Energy as aggregator) offers a large upfront $/kWh enrollment incentive
  ($500/kWh up to $10,000, stepping down to $300/kWh up to $6,000 after Sept 22, 2026) plus
  ongoing quarterly incentives for Tesla batteries. Requires enrollment in SMUD's Solar and
  Storage Rate (SSR). This is genuinely one of the more detailed/public-facing residential
  storage VPP programs found in this pass.
- **SMUD residential TOU rate** — CONFIRMED. Time-of-Day (5-8pm) Rate is SMUD's standard
  residential rate (not just optional) — off-peak/mid-peak/peak structure, weekday 5-8pm peak.
  Exact current cent/kWh figures were only found via a third-party site (nrgcleanpower.com);
  SMUD's own Rate Details subpage was not fetched directly for the numeric table, so the specific
  cent amounts in the CSV are marked as third-party-reported, not primary-confirmed.
- **LADWP residential TOU + demand response** — CONFIRMED. R-1B is LADWP's optional TOU rate
  (High Peak/Low Peak/Base). "Power Savers" is a residential/small-C&I smart-thermostat demand
  response program ($55 enrollment + $40-$90/yr participation incentive, primary source).
  LADWP's TOU rate page does not publish the actual cent/kWh values (they're in separate
  ordinance PDFs not fully parsed here) — incentive_value_usd left blank for that row rather than
  guessed.
- **Non-CPUC export compensation rules, utility by utility** — CONFIRMED for all 9 and captured
  in `export_compensation`. Notably these are NOT uniform "1:1 net metering" — most have moved to
  their own non-retail export rate distinct from both legacy NEM and CPUC NEM 3.0:
  - LADWP: kept full retail-rate net metering (notably generous, ~26-31c/kWh vs SCE's NEM3 ~5c).
  - SMUD: flat 9.6c/kWh export rate (Solar and Storage Rate), legacy NEM grandfathered to 2030.
  - IID: "Net Billing" at a variable rate pegged to IID's wholesale solar cost, currently 6.98c/kWh.
  - MID: retail-rate NEM2.0 netting (not directly rate-confirmed on primary page, "own tariff").
  - TID: on/off-peak monthly netting + annual excess paid at TID's published Short Run Marginal
    Cost (~7.86c/kWh in 2024), i.e. avoided-cost basis, not retail; legacy true 1:1 net metering
    (RNT/NNT) closed to new accounts.
  - Anaheim: NEM 2.0, wholesale-based export rate (transitioned from full retail NEM1 after
    hitting the 5%/30MW cap in 2019).
  - Riverside: export credited at RPU's Avoided Cost of Energy x Time-of-Delivery factor, not 1:1.
  - Santa Clara/SVP: annual netting with a "Generation Buy-back rate" true-up; the actual rate
    value is only disclosed on the customer's individual annual NEM bill, not published generally.
  - Glendale: kept retail-rate net metering under its own L-1-D/L-1-E tariff (GWP no longer offers
    solar incentives, but NEM itself remains).

## Not verified / could not confirm

- Exact current cent/kWh SMUD TOD rate figures — only found via a third-party aggregator
  (nrgcleanpower.com), not confirmed against SMUD's own numeric rate table page.
- MID: no residential-specific demand response or battery storage incentive program was found on
  mid.org. MID does have interruptible/curtailable options for agricultural and large C&I
  (P-4, GS-PAC), and a utility-scale flow-battery demo project, but nothing residential-facing —
  treated as a real gap, not a missed search.
- MID and IID: could not confirm current EIM or EDAM participation status specific to each (as
  distinct from their BANC/own-BA status). Flagged as `Unknown` risk in the RTO write-up above
  rather than asserted either way.
- LADWP R-1B and Glendale L-1-B: on-peak/off-peak cent/kWh figures for LADWP were not found in
  parseable form on the rate page (values live in separate ordinance PDFs not opened); left
  `incentive_value_usd`/`peak_offpeak_rates` blank for LADWP TOU rather than guess. Glendale's
  numbers WERE published directly on its rate page and are included with full confidence.
- SVP/Santa Clara Generation Buy-back rate: SVP states the excess-generation buy-back value is
  disclosed only on a customer's individual Annual NEM Bill — no published rate table found, left
  blank rather than guessed.
- Riverside DTOU on-peak/off-peak/mid-peak cent/kWh values: found the tariff PDF (effective
  1/1/2024) but did not extract the embedded per-kWh numbers from the PDF; on-peak/off-peak
  windows were also not itemized on the public-facing program page. Left blank.
- Did not reach Glendale's separate Sunrun-partnered virtual power plant program (City Council
  directed contract negotiations with Sunrun for ~3,000-4,000 residential + 30-40 multifamily
  properties, ~25MW average solar+storage); this was still in contract-negotiation stage per the
  news coverage found, not yet an active enrollable program, so no row was written for it —
  worth re-checking in a future pass once/if it launches.
- Did not research: LADWP EV-specific rate details beyond the R-1B TOU page reference; MID's and
  TID's non-residential/agricultural DR and curtailment programs (P-4, Power Partners) were noted
  but out of scope since this job is retail/residential program rows.

## Utilities not reached

All 9 target utilities (including the bonus, Glendale) were researched. No utility was skipped
for budget reasons — approximately 45-50 web searches and ~20 page fetches were used out of the
~200-search budget.
