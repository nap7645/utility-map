# Region plan — CAISO (California)

Read `plans/PLAYBOOK.md` first. This file is deltas only.
*Regional facts below are from training knowledge (mid-2026); verify before relying.*

## Why CAISO is different

Three IOUs (PG&E, SCE, SDG&E) serve ~75% of load under one regulator (CPUC) with **the most
mature storage policy in the country** — and the most churn. The rules changed materially in
2023 (NEM 3.0 / "Solar Billing Plan") and the numbers change every rate case. Treat every
figure as dated; put the effective date in the cell.

Publicly-owned utilities (LADWP, SMUD, Imperial Irrigation District, plus ~40 smaller munis
via NCPA/SCPPA) are **outside CPUC jurisdiction** and set their own NEM and DR rules. LADWP
alone is 1.5M customers. SMUD has one of the best-documented residential storage/VPP programs
anywhere. These are not edge cases here; they're a quarter of the map.

Community Choice Aggregators (CCAs — MCE, CleanPowerSF, Peninsula Clean Energy, Clean Power
Alliance, ~25 total) buy energy for ~11M customers inside IOU territories. The IOU still runs
the wires and the interconnection; the CCA sets generation rates and often runs its own DR/VPP
program. Model as `ViaAggregator`-adjacent: record CCA programs under a synthetic
`California CCAs (statewide)` entity with `scope=state` until Phase 4.

## Denominator

States: CA. `STATE='CA' AND CUSTOMERS>9999` returns ~60 records. Small number, high stakes.
Balancing-area note: a sliver of CA (Imperial Irrigation District, parts of the north) is outside
CAISO; tag `rto` per utility. Also pull NV (NV Energy is WECC, not CAISO — tag it and skip).

## Load-bearing utilities for full program rows (≈15)

PG&E, SCE, SDG&E, LADWP, SMUD, Imperial Irrigation District, Modesto ID, Turlock ID, Riverside,
Anaheim, Pasadena, Glendale, Burbank, Roseville, Silicon Valley Power (Santa Clara), plus the
synthetic CCA entity.

## Program families to look for

- **Rates**: default residential TOU (all three IOUs since 2020–22 — TOU-C/TOU-D/TOU-DR1),
  EV-TOU rates, and the Solar Billing Plan's export prices (hourly avoided-cost, "ACC" values —
  these are the arbitrage signal; get the ACC Plus adders by utility).
- **Dispatch**: Emergency Load Reduction Program (ELRP — the residential Power Saver Rewards
  version pays per kWh during CAISO alerts and is the model for the whole country), Demand
  Response Auction Mechanism (DRAM — third-party aggregators bidding into CAISO), Capacity
  Bidding Program, Base Interruptible Program (C&I), SGIP-funded storage with DR obligations,
  SCE Smart Energy Program, PG&E SmartAC / SmartRate, SDG&E Power Saver Rewards. SMUD's
  Virtual Power Plant / PowerDirect. LADWP's Smart Home DR.
- **Storage incentives**: SGIP (Self-Generation Incentive Program) — residential equity and
  resiliency budgets; large and documented.
- **Export**: NEM 1.0 / 2.0 grandfathered vs NBT (net billing tariff). Whether adding storage to a
  grandfathered NEM 2.0 system triggers NBT is a live, high-value question — capture the CPUC
  decision language precisely.

## Interconnection

CPUC Rule 21 governs IOUs (fast track thresholds, the Rule 21 storage "non-export" and
"limited export" paths — these are well-defined and worth capturing in detail; they're the
template other states copy). POUs set their own. Grid charging: NBT allows it; NEM 2.0 has
paired-storage metering rules. Get the Rule 21 Section-level citations.

## Wholesale (Opus, one agent)

CAISO products a DER aggregation can reach: Proxy Demand Resource (PDR), Reliability DR Resource
(RDRR), the DER Provider (DERP) model, Resource Adequacy value via DRAM, ancillary (Reg Up/Down,
Spin, Non-Spin), and the Order 2222 implementation. Sources: CAISO BPMs, tariff Sections 4.13–4.14,
DMM annual report. CA has **not** opted out of aggregation; note that explicitly.

## Cluster split

- Presence: one Sonnet agent for everything >10k (≈60). Add a second for the CCA list.
- Programs: IOUs (Opus — the rate structures are complex and the figures matter), POUs (Sonnet).
- Interconnection: one Opus agent, CA only — but it's the longest state file in the country.
- Wholesale: one Opus agent.

## Hard problem to flag

Rate churn. CA numbers go stale in months. Build the `last_verified` staleness indicator into
the map before loading CA, or the map will confidently show 2024 export rates in 2027.
