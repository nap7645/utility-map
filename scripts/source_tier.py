"""Source tier — replaces the research agents' self-reported High/Medium/Low.

Three levels, about the evidence rather than the researcher's feeling:

  Primary     the linked page is the authority itself: the utility's own site, a regulator
              (PUC/PSC/ICC), an RTO (PJM/MISO), a statute or code, a state agency
  Secondary   a linked page that reports on the authority: news, DSIRE/OpenEI, trade press,
              aggregator sites, a G&T describing a member's program
  Unverified  no usable link, or a link that doesn't show the claim

Derivation is heuristic and errs toward the lower tier: a Primary claim means "click this and you
are looking at the source". The original `confidence` column is retained in the raw data as a
tiebreaker and for audit; nothing is overwritten.
"""
import re
from urllib.parse import urlparse

SECONDARY_HOSTS = (
    "dsireusa.org", "openei.org", "wikipedia.org", "energysage.com", "solarreviews.com",
    "pv-magazine", "utilitydive.com", "canarymedia.com", "solarpowerworldonline.com",
    "electrek.co", "greentechmedia.com", "energynews.us", "lailluminator.com", "patch.com",
    "newsandsentinel.com", "wvgazettemail.com", "freeingthegrid.org", "electricrate.com",
    "findenergy.com", "chooseenergy.com", "saveonenergy.com", "solar.com", "palmetto.com",
    "sunrun.com", "tesla.com", "enphase.com", "thermostatrewards.com", "energyhub.com",
    "reuters.com", "bloomberg.com", "apnews.com", "nytimes.com", "washingtonpost.com",
    ".news", "news.", "gazette", "tribune", "times", "herald", "journal", "post-", "sentinel",
)
PRIMARY_HOSTS = (
    ".gov", ".state.", "pjm.com", "misoenergy.org", "spp.org", "tva.com", "tva.gov",
    "puc.", "psc.", ".icc.", "scc.virginia", "michigan.gov", "law.justia.com", "legis.",
    "leg.state", "legislature", "casetext.com", "law.cornell.edu",
)
# regulator-ish and statute mirrors count as primary; justia/cornell reproduce statute text verbatim.

def host_of(url):
    try:
        h = urlparse(url.strip()).netloc.lower()
    except Exception:
        return ""
    return h[4:] if h.startswith("www.") else h

def is_homepage(url):
    try:
        p = urlparse(url.strip())
    except Exception:
        return True
    return p.path.strip("/") == "" and not p.query

def source_tier(url, confidence=""):
    """Return 'Primary' | 'Secondary' | 'Unverified'."""
    url = (url or "").strip()
    conf = (confidence or "").strip().lower()
    # accept the new vocabulary too, so future research can write tiers directly
    conf = {"primary": "high", "secondary": "medium", "unverified": "low"}.get(conf, conf)
    if not url.startswith("http"):
        return "Unverified"
    h = host_of(url)
    if not h:
        return "Unverified"
    if any(s in h for s in SECONDARY_HOSTS):
        return "Secondary" if conf != "low" else "Unverified"
    if any(p in h for p in PRIMARY_HOSTS):
        return "Primary" if conf != "low" else "Secondary"
    # Unknown host: assume it's the utility's own domain, but only trust it as Primary if the
    # researcher read it directly (High) and it's a deep link rather than a homepage.
    if conf == "high" and not is_homepage(url):
        return "Primary"
    if conf in ("high", "medium"):
        return "Secondary"
    return "Unverified"

TIER_HELP = {
    "Primary":    "Linked page is the source itself: utility tariff/program page, regulator order, RTO manual, or statute.",
    "Secondary":  "Linked page reports on the source (news, DSIRE, trade press, a G&T describing a member program). Check the original before quoting.",
    "Unverified": "No usable link, or the link doesn't show the claim. Treat as a lead, not a fact.",
}
