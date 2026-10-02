#!/usr/bin/env python3
"""Automated audit checks (plans/SPEC.md section 6.2). Read-only; stdlib only.

    python3 scripts/audit.py                 # offline checks, writes audit/AUTOMATED_<date>.md
    python3 scripts/audit.py --links         # also link-check every source URL (needs internet; run locally)
    python3 scripts/audit.py --links --limit 300   # quick smoke test of the link checker

Exit code 0 only if every check passes. Checks:
  A1 every processed row validates (field counts, Yes/No/Unknown vocabulary, source tier, rto vocabulary)
  A2 every target territory (data/raw/hifld_over10k.csv) has exactly one presence row
  A3 every program / interconnection utility name joins a map boundary (same norm() the map uses)
  A4 no cross-state joins (the map's progsFor() rule: a name match on a polygon of another state)
  A5 every Yes cell has a URL; every program/interconnection row has a URL
  A6 link check (--links): >=95% of unique source URLs return non-4xx
  A7 every territory has a governing body (mirror of rtoOf() in docs/index.html; not 'OTHER'/Unknown)
  A8 polygon layer covers the lower 48 + DC (proxy: every state has polygons and every target
     territory has a polygon; true gap detection needs a land mask - not done here)
Keep the rtoOf mirror in sync with docs/index.html (BA_MAP is parsed from it directly).
"""
import argparse, csv, datetime, json, os, re, sys, threading, time, urllib.request, urllib.error
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_map_payload import norm, infer_scope  # noqa: E402

ROOT = os.path.dirname(HERE)
P = lambda *a: os.path.join(ROOT, *a)

CELLS = ["res_habit", "res_dispatch", "ci_habit", "ci_dispatch"]
YN = {"Yes", "No", "Unknown"}
TIERS = {"primary", "secondary", "unverified", "high", "medium", "low"}
RTOS = {"MISO", "PJM", "SPP", "NYISO", "ISO-NE", "CAISO", "ERCOT", "TVA", "AECI", "SERC-nonRTO",
        "FRCC-nonRTO", "WECC-nonRTO", "AK-islanded", "HI-islanded", "Other-nonRTO", "Non-RTO",
        "MISO/PJM", "Unknown"}
LOWER48 = set("AL AZ AR CA CO CT DE FL GA ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY "
              "NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC".split())

def rd(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

class R:
    def __init__(self): self.rows = []; self.detail = {}
    def add(self, cid, title, ok, summary, detail=None):
        self.rows.append((cid, title, ok, summary)); self.detail[cid] = detail or []
R_ = R()

# ---------------------------------------------------------------- data
presence = rd(P("data/processed/presence_scan.csv"))
programs = rd(P("data/processed/programs.csv"))
ic_state = rd(P("data/processed/interconnection_state.csv"))
ic_util = rd(P("data/processed/interconnection_utility.csv"))
denom = rd(P("data/raw/hifld_over10k.csv"))
aliases = {r["utility_name"].strip(): r["hifld_name"].strip() for r in rd(P("data/crosswalk/aliases.csv"))}
geo = json.load(open(P("docs/data/territories.geojson"), encoding="utf-8"))
feats = [f["properties"] for f in geo["features"]]
payload = json.load(open(P("docs/data/programs.json"), encoding="utf-8"))
index_html = open(P("docs/index.html"), encoding="utf-8").read()

JOIN_EXCLUDE = set(re.findall(r"'(\d+)'", (re.search(r"const JOIN_EXCLUDE = new Set\(\[(.*?)\]\)", index_html) or [None, ""])[1]))

def map_joins(key, states):
    """Polygons the map would attach payload entry `key` to (mirror of progsFor())."""
    out = []
    for p in geo_by_key.get(key, []):
        if str(p["ID"]) in JOIN_EXCLUDE: continue
        sfx = re.search(r"\(([A-Z]{2})\)\s*$", p["NAME"] or "")
        if sfx and states and sfx.group(1) not in states: continue
        out.append(p)
    return out

# ---------------------------------------------------------------- A1 validation
def a1():
    probs = []
    for name, path, nf in (("presence_scan", "data/processed/presence_scan.csv", 17), ("programs", "data/processed/programs.csv", 22),
                           ("interconnection_state", "data/processed/interconnection_state.csv", 31),
                           ("interconnection_utility", "data/processed/interconnection_utility.csv", 21)):
        with open(P(path), newline="", encoding="utf-8") as fh:
            rr = list(csv.reader(fh))
        if len(rr[0]) != nf: probs.append(f"{name}: header has {len(rr[0])} columns, expected {nf}")
        for i, r in enumerate(rr[1:], 2):
            if len(r) != nf: probs.append(f"{name} line {i}: {len(r)} fields, expected {nf}")
    for name, rows, nf in (("presence_scan", presence, 17), ("programs", programs, 22),
                           ("interconnection_state", ic_state, 31), ("interconnection_utility", ic_util, 21)):
        for i, r in enumerate(rows, 2):
            if None in r or any(v is None for v in r.values()):
                probs.append(f"{name} line {i}: wrong field count")
                continue
            tier = (r.get("confidence") or "").strip().lower()
            if tier not in TIERS:
                probs.append(f"{name} line {i}: confidence={r.get('confidence')!r}")
            if name == "presence_scan":
                for c in CELLS:
                    if r[c] not in YN: probs.append(f"{name} line {i} eia {r['eia_id']}: {c}={r[c]!r}")
                if r["rto"] not in RTOS: probs.append(f"{name} line {i} eia {r['eia_id']}: rto={r['rto']!r}")
                if r["ownership_type"] not in {"IOU", "Cooperative", "Municipal", "Federal/State", ""}:
                    probs.append(f"{name} line {i} eia {r['eia_id']}: ownership={r['ownership_type']!r}")
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["last_verified"] or ""):
                    probs.append(f"{name} line {i} eia {r['eia_id']}: last_verified={r['last_verified']!r}")
            if name == "programs" and r["customer_segment"] == "" :
                probs.append(f"{name} line {i}: blank customer_segment ({r['utility_name']} / {r['program_name'][:40]})")
    for r in denom:
        if not (r["customers"] or "").strip().isdigit():
            probs.append(f"denominator eia {r['eia_id']} {r['hifld_name']}: customers={r['customers']!r}")
    # customers sanity on the boundary layer
    blank = {r["eia_id"] for r in denom if not (r["customers"] or "").strip().isdigit()}
    sentinel = [p for p in feats if not isinstance(p.get("CUSTOMERS"), (int, float)) or p["CUSTOMERS"] < 0]
    info = [f"(info, HIFLD no-data sentinel; UI hides it) geojson {p['ID']} {p['NAME']}: CUSTOMERS={p.get('CUSTOMERS')!r}"
            for p in sentinel if str(p["ID"]) not in blank]
    R_.add("A1", "Every row validates", not probs, f"{len(probs)} problem(s) (+{len(info)} sentinel-customer polygons, info only)", probs + info)

# ---------------------------------------------------------------- A2 presence coverage
def a2():
    pj = json.load(open(P("docs/data/presence.json"), encoding="utf-8"))   # what the map reads (scan rows + rows derived from programs)
    ids = Counter(pj.keys())
    dup = [k for k, v in Counter(r["eia_id"] for r in presence).items() if v > 1]
    tg = {r["eia_id"] for r in denom}
    miss = sorted(tg - set(ids))
    stray = sorted(set(ids) - tg)
    nm = {r["eia_id"]: r["hifld_name"] for r in denom}
    d = [f"missing presence row: {i} {nm[i]}" for i in miss] + [f"duplicate presence rows: {i}" for i in dup]
    d += [f"presence row not in denominator (info): {i}" for i in stray]
    R_.add("A2", "Every target territory has a presence row (docs/data/presence.json)", not miss and not dup,
           f"{len(tg)} targets, {len(miss)} missing, {len(dup)} duplicated, {len(stray)} extra rows (info only)", d)

# ---------------------------------------------------------------- A3 / A4 joins
geo_by_key = defaultdict(list)
for p in feats: geo_by_key[norm(p["NAME"])].append(p)

scope_ovr = {r["utility_name"].strip(): r["scope"].strip() for r in rd(P("data/crosswalk/scope_overrides.csv"))}
alias_notes = {r["utility_name"].strip(): (r.get("note") or "") for r in rd(P("data/crosswalk/aliases.csv"))}

def utility_names():
    out = {}
    sc = lambda n, rto: scope_ovr.get(n) or infer_scope(n, rto or "")
    for r in programs:
        if sc(r["utility_name"], r["rto"]) == "utility": out.setdefault(r["utility_name"], ("programs", r["state"]))
    for r in ic_util:
        n = r["utility_name"].strip()
        if n and sc(n, r["rto"]) == "utility": out.setdefault(n, ("ic_util", r["state"]))
    return out

def a3():
    miss = []
    names = utility_names()
    for n, (src, st) in sorted(names.items()):
        if not map_joins(norm(aliases.get(n, n)), {x for x in re.findall(r"\b[A-Z]{2}\b", st or "")}):
            if "NOT IN HIFLD" in alias_notes.get(n, "").upper(): continue   # documented exception (alias note)
            miss.append(f"{src}: {n!r} ({st}) joins no boundary")
    R_.add("A3", "Every program/IC utility name joins a boundary", not miss,
           f"{len(names)} utility names, {len(miss)} unjoined", miss)

STATE_FIX = dict(re.findall(r"'(\d+)':'([A-Z]{2})'", re.search(r"const STATE_FIX = \{(.*?)\}", index_html).group(0))) if re.search(r"const STATE_FIX = \{(.*?)\}", index_html) else {}

JOIN_EXCLUDE = set(re.findall(r"'(\d+)'", (re.search(r"const JOIN_EXCLUDE = new Set\(\[(.*?)\]\)", index_html) or [None,""])[1]))

def centroid(pid):
    for f in geo["features"]:
        if str(f["properties"]["ID"]) == str(pid):
            pts = []
            def walk(c):
                if c and isinstance(c[0], (int, float)): pts.append(c)
                else: [walk(x) for x in c]
            walk(f["geometry"]["coordinates"])
            return sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)
    return None

def a4():
    """FAIL: one payload entry attaches to >1 polygon in different states (Carroll Electric AR/OH case).
    WARN (info): the matched polygon's HIFLD STATE differs from the utility's state (HIFLD STATE = HQ state;
    index.html STATE_FIX corrects a few). Centroid is printed so a human can sanity-check the polygon."""
    bad, warn = [], []
    for key, u in payload["utilities"].items():
        states = {x for x in [u.get("state")] + u.get("alt_states", []) if x}
        for st in list(states):
            if len(st) > 2: states |= set(re.findall(r"\b[A-Z]{2}\b", st))
        hits = []
        for p in geo_by_key.get(key, []):
            if str(p["ID"]) in JOIN_EXCLUDE: continue          # rejected by progsFor()
            sfx = re.search(r"\(([A-Z]{2})\)\s*$", p["NAME"] or "")
            if sfx and sfx.group(1) not in states: continue   # rejected by progsFor()
            hits.append(p)
        pst = {STATE_FIX.get(str(p["ID"]), p["STATE"]) for p in hits}
        if len(hits) > 1 and len(pst) > 1:
            bad.append(f"{u['name']!r} attaches to {len(hits)} polygons in {sorted(pst)}: " + "; ".join(f"{p['NAME']} eia {p['ID']}" for p in hits))
        for p in hits:
            ps = STATE_FIX.get(str(p["ID"]), p["STATE"])
            if states and ps not in states:
                c = centroid(p["ID"])
                warn.append(f"(info) {u['name']!r} ({'/'.join(sorted(states))}) -> polygon {p['NAME']} eia {p['ID']} HIFLD STATE={ps}, centroid={c[0]:.2f},{c[1]:.2f}" if c else f"(info) {u['name']!r} -> {p['NAME']}")
    R_.add("A4", "No cross-state name joins", not bad,
           f"{len(bad)} ambiguous cross-state join(s); {len(warn)} polygon-STATE differences listed for review (info)", bad + warn)

# ---------------------------------------------------------------- A5 Yes needs URL
def a5():
    bad = []
    for r in presence:
        for c in CELLS:
            if r[c] == "Yes" and not r[c + "_src"].startswith("http"):
                bad.append(f"presence eia {r['eia_id']} {r['utility_name']}: {c}=Yes without URL")
    for r in programs:
        if not r["source_url"].startswith("http"): bad.append(f"programs: {r['utility_name']} / {r['program_name'][:50]}: no URL")
    for r in ic_state:
        if not r["source_url"].startswith("http"): bad.append(f"ic_state {r['state']}: no URL")
    for r in ic_util:
        if r["utility_name"].strip() and not r["source_url"].startswith("http"): bad.append(f"ic_util {r['utility_name']}: no URL")
    R_.add("A5", "Every Yes (and every program row) has a URL", not bad, f"{len(bad)} missing", bad)

# ---------------------------------------------------------------- A7 governing body
BA_MAP = []
for m in re.finditer(r"^\s*\[/(.+?)/,\s*'([^']+)'\],?\s*$", index_html, re.M):
    BA_MAP.append((re.compile(m.group(1)), m.group(2)))
pres_by_id = {r["eia_id"]: r for r in presence}
prog_by_key = payload["utilities"]

def rto_of(p):
    """Mirror of rtoOf() in docs/index.html."""
    if p["STATE"] == "AK": return "AK-islanded"
    if p["STATE"] == "HI": return "HI-islanded"
    u = None if str(p["ID"]) in JOIN_EXCLUDE else prog_by_key.get(norm(p["NAME"]))
    if u:
        sfx = re.search(r"\(([A-Z]{2})\)\s*$", p["NAME"] or "")
        if sfx and u.get("state") and sfx.group(1) not in u["state"]: u = None
    if u and u.get("rto") and u["rto"] != "Non-RTO": return u["rto"]
    pr = pres_by_id.get(str(p["ID"]))
    if pr and pr["rto"] not in ("Unknown", "Other-nonRTO", "Non-RTO", ""): return pr["rto"]
    s = ((p.get("CNTRL_AREA") or "") + " " + (p.get("PLAN_AREA") or "")).upper()
    if "MIDCONTINENT" in s or re.search(r"\bMISO\b", s): return "MISO"
    if "PJM" in s: return "PJM"
    if "NEW YORK" in s or re.search(r"\bNYIS", s): return "NYISO"
    if re.search(r"\bCISO\b|CALIFORNIA INDEPENDENT", s): return "CAISO"
    if re.search(r"\bERCO\b|ELECTRIC RELIABILITY COUNCIL", s): return "ERCOT"
    for rx, label in BA_MAP:
        if rx.search(s): return label
    return "Other-nonRTO" if pr and pr["rto"] == "Other-nonRTO" else "OTHER"

def a7():
    if len(BA_MAP) < 8:
        R_.add("A7", "Every territory has a governing body", False, f"could not parse BA_MAP from index.html (got {len(BA_MAP)})", [])
        return
    tgt = {r["eia_id"] for r in denom}
    unk = [p for p in feats if rto_of(p) == "OTHER"]
    unk_t = [p for p in unk if str(p["ID"]) in tgt]
    d = [f"OTHER: {p['NAME']} [{p['STATE']}] eia {p['ID']} cust {p['CUSTOMERS']} CNTRL_AREA={p.get('CNTRL_AREA')}" for p in
         sorted(unk_t, key=lambda p: -p["CUSTOMERS"])]
    c = Counter(rto_of(p) for p in feats if str(p["ID"]) in tgt)
    d.append("distribution over target territories: " + ", ".join(f"{k}={v}" for k, v in c.most_common()))
    R_.add("A7", "Every target territory has a governing body", not unk_t,
           f"{len(unk_t)} of {len(tgt)} target territories resolve to OTHER ({len(unk)} of {len(feats)} polygons incl. <10k)", d)

# ---------------------------------------------------------------- A8 coverage proxy
def a8():
    by_state = Counter(p["STATE"] for p in feats)
    miss_states = sorted(LOWER48 - set(by_state))
    ids = {str(p["ID"]) for p in feats}
    tg = [r for r in denom if r["hifld_state"] in LOWER48]
    no_poly = [r for r in tg if r["eia_id"] not in ids]
    ci = lambda r: int(r["customers"] or 0)
    cust = sum(ci(r) for r in tg); lost = sum(ci(r) for r in no_poly)
    d = [f"state with no polygons: {s}" for s in miss_states]
    d += [f"target without polygon: {r['eia_id']} {r['hifld_name']} ({r['customers'] or '?'} customers)" for r in no_poly]
    R_.add("A8", "Polygon layer covers the lower 48 + DC (proxy)", not miss_states and not no_poly,
           f"{len(LOWER48)-len(miss_states)}/{len(LOWER48)} states have polygons; {len(tg)-len(no_poly)}/{len(tg)} targets "
           f"have a polygon ({100*(cust-lost)/max(cust,1):.2f}% of target customers). Geographic gaps need a land-mask check (not done).", d)

# ---------------------------------------------------------------- A6 link check
def all_urls():
    u = defaultdict(list)
    for r in presence:
        for c in CELLS:
            if r[c + "_src"].startswith("http"): u[r[c + "_src"].strip()].append(f"presence {r['eia_id']} {c}")
    for r in programs:
        if r["source_url"].startswith("http"): u[r["source_url"].strip()].append(f"programs {r['utility_name']}")
    for r in ic_state:
        if r["source_url"].startswith("http"): u[r["source_url"].strip()].append(f"ic_state {r['state']}")
    for r in ic_util:
        if r["source_url"].startswith("http"): u[r["source_url"].strip()].append(f"ic_util {r['utility_name']}")
    return u

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
_lock = threading.Lock(); _host_sem = {}; _host_last = {}

def _sem(host):
    with _lock:
        if host not in _host_sem: _host_sem[host] = threading.Semaphore(2)
        return _host_sem[host]

def check(url):
    host = urlparse(url).netloc
    with _sem(host):
        with _lock:
            wait = _host_last.get(host, 0) + 0.25 - time.time(); _host_last[host] = max(time.time(), _host_last.get(host, 0) + 0.25)
        if wait > 0: time.sleep(wait)                      # per-host throttle (~4 req/s/host max)
        last = "ERR"
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
                with urllib.request.urlopen(req, timeout=20) as resp:
                    return url, resp.status
            except urllib.error.HTTPError as e:
                last = e.code
                if method == "HEAD": continue              # any HEAD failure: retry as GET (many servers mishandle HEAD)
                return url, e.code
            except Exception as e:
                last = f"ERR {type(e).__name__}"
        return url, last

def a6(limit):
    urls = all_urls()
    import random
    items = sorted(urls)
    if limit: items = random.Random(7).sample(items, min(limit, len(items)))   # seeded random sample, not alphabetical
    print(f"link check: {len(items)} unique URLs (of {len(urls)}) ...", flush=True)
    with ThreadPoolExecutor(max_workers=24) as ex: res = list(ex.map(check, items))
    out = P("audit", "linkcheck.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["url", "status", "used_by"])
        for u, s in res: w.writerow([u, s, "; ".join(urls[u][:3])])
    ok = sum(1 for _, s in res if isinstance(s, int) and s < 400)
    soft = sum(1 for _, s in res if s in (403, 429))  # frequently bot-blocking, not necessarily dead
    hard = [(u, s) for u, s in res if not (isinstance(s, int) and s < 400)]
    pct = 100 * ok / max(len(res), 1); pct_soft = 100 * (ok + soft) / max(len(res), 1)
    d = [f"{s}  {u}  <- {urls[u][0]}" for u, s in hard]
    R_.add("A6", "Link check >=95% non-4xx", pct >= 95,
           f"{ok}/{len(res)} OK ({pct:.1f}%); counting 403/429 as live: {pct_soft:.1f}%. Full list: audit/linkcheck.csv", d)

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--links", action="store_true", help="run the link check (needs internet)")
    ap.add_argument("--limit", type=int, default=0, help="link check: only the first N URLs (smoke test)")
    a = ap.parse_args()
    a1(); a2(); a3(); a4(); a5(); a7(); a8()
    if a.links: a6(a.limit)
    else: R_.add("A6", "Link check >=95% non-4xx", True, "NOT RUN - run: python3 scripts/audit.py --links", [])
    today = datetime.date.today().isoformat()
    lines = [f"# Automated audit - {today}", "", "| ID | Check | Result | Summary |", "|---|---|---|---|"]
    for cid, title, ok, s in sorted(R_.rows):
        res = "NOT RUN" if s.startswith("NOT RUN") else ("PASS" if ok else "FAIL")
        lines.append(f"| {cid} | {title} | {res} | {s} |")
    for cid, title, ok, s in sorted(R_.rows):
        d = R_.detail[cid]
        if d:
            lines += ["", f"## {cid} detail ({len(d)} lines)", ""] + [f"- {x}" for x in d[:200]]
            if len(d) > 200: lines.append(f"- ... {len(d)-200} more")
    txt = "\n".join(lines) + "\n"
    with open(P("audit", "AUTOMATED_latest.md"), "w", encoding="utf-8") as fh: fh.write(txt)
    print("\n".join(lines[:4 + len(R_.rows)]))
    print("\nfull detail: audit/AUTOMATED_latest.md")
    return 0 if all(ok for _, _, ok, _ in R_.rows) else 1

if __name__ == "__main__":
    sys.exit(main())
