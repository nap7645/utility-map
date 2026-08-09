#!/usr/bin/env python3
"""Build the map payload from processed data.

Reads  data/processed/programs.csv
       data/crosswalk/aliases.csv        (our utility_name -> HIFLD NAME)
       data/crosswalk/scope_overrides.csv (our utility_name -> scope)
Writes docs/data/programs.json

The map joins HIFLD features to this payload client-side using `norm()`, which
is mirrored exactly in JS. Keep the two implementations in sync.
"""
import csv, json, os, re, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

# --- normalization (MIRRORED IN JS - keep in sync) ---------------------------
SUFFIX = r"(CO|COMPANY|INC|LLC|CORP|CORPORATION|LP|LTD|PLC)"
PREFIX = r"(CITY OF|TOWN OF|VILLAGE OF|BOROUGH OF|COUNTY OF)"
WORDS = [
    (r"\bELEC\b", "ELECTRIC"), (r"\bCOOP\b", "COOPERATIVE"), (r"\bCO-OP\b", "COOPERATIVE"),
    (r"\bASSN\b", "ASSOCIATION"), (r"\bPWR\b", "POWER"), (r"\bUTIL\b", "UTILITIES"),
    (r"\bDEPT\b", "DEPARTMENT"), (r"\bMUN\b", "MUNICIPAL"), (r"\bSVC\b", "SERVICE"),
    (r"\bSERVICES\b", "SERVICE"), (r"\bUTILITY\b", "UTILITIES"), (r"\bLT\b", "LIGHT"),
    (r"\bLGT\b", "LIGHT"), (r"\bCOMM\b", "COMMISSION"), (r"\bDIV\b", "DIVISION"),
]

def norm(s):
    s = (s or "").upper()
    s = s.replace("&", " AND ")
    s = re.sub(r"\([^)]*\)", " ", s)          # drop parentheticals
    s = re.sub(r"\s*-\s*\([A-Z]{2}\)\s*$", " ", s)  # drop HIFLD " - (MI)"
    s = re.sub(r"\bD/B/A\b.*$", " ", s)        # drop d/b/a tails
    s = re.sub(r"[^A-Z0-9 ]+", " ", s)
    for pat, rep in WORDS:
        s = re.sub(pat, rep, s)
    s = re.sub(r"^" + PREFIX + r"\b", " ", s)
    s = re.sub(r"\b" + SUFFIX + r"\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()

# --- scope inference ---------------------------------------------------------
# Entities with no retail service territory. These cannot bind to a HIFLD polygon.
STATE_AGENCY = re.compile(
    r"POWER AGENCY|ENERGY ADMINISTRATION|BOARD OF PUBLIC UTILITIES|"
    r"PUBLIC SERVICE COMMISSION|statewide", re.I)
WHOLESALE = re.compile(
    r"GREAT RIVER ENERGY|HOOSIER ENERGY|BUCKEYE POWER|AMERICAN MUNICIPAL POWER|"
    r"WPPI ENERGY|DAIRYLAND|BASIN ELECTRIC|EAST RIVER ELECTRIC|MISSOURI RIVER ENERGY|"
    r"WABASH VALLEY|ILLINOIS MUNICIPAL ELECTRIC AGENCY|PRAIRIE POWER|"
    r"SOUTHERN ILLINOIS POWER|ARKANSAS ELECTRIC COOPERATIVE|EAST KENTUCKY POWER|"
    r"BIG RIVERS|OLD DOMINION ELECTRIC|DELAWARE MUNICIPAL ELECTRIC|"
    r"LOUISIANA ENERGY AND POWER|LEPA|MICHIGAN PUBLIC POWER|WOLVERINE POWER|"
    r"ASSOCIATED ELECTRIC|CENTRAL IOWA POWER|CORN BELT POWER", re.I)

def infer_scope(name, rto):
    if rto.endswith("-market"):
        return "rto"
    if STATE_AGENCY.search(name):
        return "state"
    if WHOLESALE.search(name):
        return "wholesale"
    return "utility"

def load_kv(path, a="key", b="value"):
    if not os.path.exists(path):
        return {}
    with open(path, newline="", encoding="utf-8") as fh:
        return {r[a].strip(): r[b].strip() for r in csv.DictReader(fh) if r.get(a, "").strip()}

def main():
    aliases = load_kv(P("data", "crosswalk", "aliases.csv"), "utility_name", "hifld_name")
    scope_ovr = load_kv(P("data", "crosswalk", "scope_overrides.csv"), "utility_name", "scope")

    with open(P("data", "processed", "programs.csv"), newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    utils, market = {}, []
    for r in rows:
        name, rto = r["utility_name"], r["rto"]
        scope = scope_ovr.get(name) or infer_scope(name, rto)
        prog = {
            "n": r["program_name"], "cat": r["program_category"], "seg": r["customer_segment"],
            "assets": r["eligible_assets"], "enroll": r["enrollment_basis"],
            "struct": r["incentive_structure"], "val": r["incentive_value_usd"],
            "limits": r["event_limits"], "tariff": r["tariff_schedule"],
            "peak": r["on_peak_window"], "rates": r["peak_offpeak_rates"],
            "export": r["export_compensation"], "stor": r["storage_eligible"],
            "stack": r["stackable_with"], "status": r["program_status"],
            "url": r["source_url"], "conf": r["confidence"],
        }
        if scope == "rto":
            market.append({**prog, "rto": rto})
            continue
        key = norm(aliases.get(name, name))
        u = utils.setdefault(key, {
            "name": name, "state": r["state"], "rto": rto,
            "own": r["ownership_type"], "scope": scope, "programs": [],
        })
        u["programs"].append(prog)
        # a utility spanning states/RTOs: keep the first, note the rest
        if r["state"] != u["state"]:
            u.setdefault("alt_states", [])
            if r["state"] not in u["alt_states"]:
                u["alt_states"].append(r["state"])

    # --- interconnection: state rules are the floor, utility rows are deltas ---
    ic_states, ic_utils = {}, {}
    p_state = P("data", "processed", "interconnection_state.csv")
    p_util = P("data", "processed", "interconnection_utility.csv")
    if os.path.exists(p_state):
        with open(p_state, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                ic_states[r["state"]] = {k: v for k, v in r.items() if v.strip()}
    if os.path.exists(p_util):
        with open(p_util, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                nm = r["utility_name"].strip()
                if not nm:
                    continue
                key = norm(aliases.get(nm, nm))
                ic_utils.setdefault(key, []).append({k: v for k, v in r.items() if v.strip()})
    # attach deltas to the matching utility entry
    unattached = []
    for key, deltas in ic_utils.items():
        if key in utils:
            utils[key]["ic"] = deltas
        else:
            unattached.append(deltas[0].get("utility_name", key))

    payload = {
        "generated": "2026-08-09",
        "note": "Screening data. Unverified. Do not quote to customers without re-checking source.",
        "utilities": utils,
        "market": market,
        "icStates": ic_states,
        "aliasIndex": {norm(v): norm(aliases.get(k, k)) for k, v in aliases.items()},
    }

    out = P("docs", "data", "programs.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, separators=(",", ":"))

    by_scope = defaultdict(int)
    for u in utils.values():
        by_scope[u["scope"]] += 1
    print(f"wrote {out} ({os.path.getsize(out)/1024:.0f} KB)")
    print(f"  utility entities : {len(utils)}")
    for k, v in sorted(by_scope.items()):
        print(f"    scope={k:10s} {v}")
    print(f"  market products  : {len(market)}")
    print(f"  aliases loaded   : {len(aliases)}")
    print(f"  ic state rules   : {len(ic_states)}")
    print(f"  ic utility deltas: {sum(len(v) for v in ic_utils.values())} "
          f"attached to {sum(1 for u in utils.values() if 'ic' in u)} utilities")
    if unattached:
        print(f"  !! {len(unattached)} ic delta rows did not attach to a utility:")
        for n in unattached:
            print(f"       {n}")
    print("\n  sample normalized keys:")
    for k in list(utils)[:6]:
        print(f"    {k!r}")

if __name__ == "__main__":
    main()
