#!/usr/bin/env python3
"""
fresh_jobs.py — the daily recency sweep.

Surfaces everything posted in the last N hours matching your searches, pins target-company
matches at the top, flags likely ghost jobs, and writes a markdown digest you can work through
in the morning application block.

Why it exists: first-24-hour applications show roughly 5x the interview rate. Seeing the
posting on day zero is the whole game. See 02_Playbooks/02-EARLY-APPLICATION-SYSTEM.md.

Usage:
    python fresh_jobs.py                  # uses config.yml, last 24h
    python fresh_jobs.py --hours 48       # widen the window
    python fresh_jobs.py --show-seen      # include postings from previous runs
    python fresh_jobs.py --config me.yml  # per-crew-member config

Setup: see README.md in this directory.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEEN_FILE = HERE / ".seen_jobs.json"
OUTPUT_DIR = HERE / "output"

# Terms that, stacked up in one posting, suggest nobody wrote this req for a real team.
# (regex, human-readable label)
GHOST_PATTERNS = [
    (r"\brockstar\b", "rockstar"),
    (r"\bninja\b", "ninja"),
    (r"\bwear many hats\b", "wear many hats"),
    (r"\bfast[- ]paced environment\b", "fast-paced environment"),
    (r"\bwork hard,? play hard\b", "work hard play hard"),
]


# --------------------------------------------------------------------------- config


def load_config(path: Path) -> dict:
    """Load YAML config, falling back to the example file with a warning."""
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML not installed. Run: pip install -r requirements.txt")

    if not path.exists():
        example = HERE / "config.example.yml"
        if not example.exists():
            sys.exit(f"No config at {path} and no config.example.yml to fall back to.")
        print(f"[!] {path.name} not found — using config.example.yml.")
        print(f"[!] Copy it to {path.name} and edit it for your own search.\n")
        path = example

    with path.open("r", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh) or {}

    cfg.setdefault("search_terms", [])
    cfg.setdefault("locations", [])
    cfg.setdefault("sites", ["linkedin", "indeed"])
    cfg.setdefault("target_companies", [])
    cfg.setdefault("exclude_keywords", [])
    cfg.setdefault("results_per_search", 40)
    cfg.setdefault("country_indeed", "canada")

    if not cfg["search_terms"]:
        sys.exit("config has no search_terms — nothing to search for.")

    return cfg


# ------------------------------------------------------------------------ seen cache


def load_seen() -> dict:
    if not SEEN_FILE.exists():
        return {}
    try:
        with SEEN_FILE.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        print("[!] Could not read the seen-jobs cache; starting fresh.")
        return {}


def save_seen(seen: dict, keep_days: int = 45) -> None:
    """Persist the cache, dropping entries older than keep_days so it does not grow forever."""
    cutoff = (datetime.now() - timedelta(days=keep_days)).isoformat()
    pruned = {k: v for k, v in seen.items() if v >= cutoff}
    try:
        with SEEN_FILE.open("w", encoding="utf-8") as fh:
            json.dump(pruned, fh, indent=0)
    except OSError as exc:
        print(f"[!] Could not write the seen-jobs cache: {exc}")


def job_key(job: dict) -> str:
    """Stable identity for a posting across runs. URLs vary with tracking params."""
    company = str(job.get("company") or "").strip().lower()
    title = str(job.get("title") or "").strip().lower()
    location = str(job.get("location") or "").strip().lower()
    return f"{company}|{title}|{location}"


# --------------------------------------------------------------------------- scoring


def normalize(name: str) -> str:
    """Loose company-name match: 'Example Corp, Inc.' -> 'examplecorp'."""
    return re.sub(r"[^a-z0-9]", "", str(name or "").lower())


def is_target(job: dict, targets: list[str]) -> str | None:
    """Return the configured target name this job matches, or None."""
    company = normalize(job.get("company"))
    if not company:
        return None
    for target in targets:
        t = normalize(target)
        if t and (t in company or company in t):
            return target
    return None


def ghost_score(job: dict) -> tuple[str, list[str]]:
    """Cheap heuristic ghost-job flag. Downranks; never hides. Returns (level, reasons).

    Weighted, because the signals are not equal: a posting still live after three months is
    far stronger evidence than any number of buzzwords. See
    05_Knowledge/WHY-THIS-WORKS.md for the underlying research.
    """
    reasons: list[str] = []
    points = 0
    description = str(job.get("description") or "").lower()

    buzzwords = [label for pattern, label in GHOST_PATTERNS if re.search(pattern, description)]
    if buzzwords:
        reasons.append("buzzwords: " + ", ".join(buzzwords))
        points += len(buzzwords)

    if description and len(description) < 400:
        reasons.append("very short description")
        points += 1

    age = posting_age_hours(job)
    if age is not None:
        if age > 24 * 90:
            reasons.append("posted 90+ days ago")
            points += 3
        elif age > 24 * 45:
            reasons.append("posted 45+ days ago")
            points += 2

    level = "high" if points >= 3 else "med" if points == 2 else "low"
    return level, reasons


def excluded(job: dict, keywords: list[str]) -> str | None:
    """Return the exclude keyword that matched the title, if any."""
    title = str(job.get("title") or "").lower()
    for kw in keywords:
        if kw and kw.lower() in title:
            return kw
    return None


def posting_age_hours(job: dict) -> float | None:
    """Hours since the posting went up, or None when the source gave no date."""
    raw = job.get("date_posted")
    if raw is None or (isinstance(raw, float) and raw != raw):  # NaN check
        return None
    try:
        posted = raw if isinstance(raw, datetime) else datetime.fromisoformat(str(raw))
    except (ValueError, TypeError):
        return None
    if posted.tzinfo is not None:
        posted = posted.replace(tzinfo=None)
    return max(0.0, (datetime.now() - posted).total_seconds() / 3600)


# ---------------------------------------------------------------------------- search


def search(cfg: dict, hours: int) -> list[dict]:
    """Run every (term, location) pair through JobSpy and return deduped raw postings."""
    try:
        from jobspy import scrape_jobs
    except ImportError:
        sys.exit(
            "python-jobspy not installed. Run: pip install -r requirements.txt\n"
            "Or do today's sweep manually — see 02_Playbooks/02-EARLY-APPLICATION-SYSTEM.md"
        )

    locations = cfg["locations"] or [""]
    collected: dict[str, dict] = {}

    for term in cfg["search_terms"]:
        for location in locations:
            label = f"'{term}'" + (f" in {location}" if location else "")
            print(f"  searching {label} ...", end=" ", flush=True)
            try:
                frame = scrape_jobs(
                    site_name=cfg["sites"],
                    search_term=term,
                    location=location or None,
                    results_wanted=cfg["results_per_search"],
                    hours_old=hours,
                    country_indeed=cfg["country_indeed"],
                )
            except Exception as exc:  # noqa: BLE001 - one bad source must not kill the sweep
                print(f"failed ({type(exc).__name__}: {exc})")
                continue

            if frame is None or len(frame) == 0:
                print("0")
                continue

            rows = frame.to_dict("records")
            for row in rows:
                collected.setdefault(job_key(row), row)
            print(len(rows))

    return list(collected.values())


# ---------------------------------------------------------------------------- digest


def build_digest(jobs: list[dict], cfg: dict, hours: int, seen: dict, show_seen: bool) -> str:
    """Sort into target / fresh / older buckets and render the markdown digest."""
    targets = cfg["target_companies"]
    excludes = cfg["exclude_keywords"]

    target_hits: list[dict] = []
    fresh: list[dict] = []
    older: list[dict] = []
    skipped = 0
    already_seen = 0

    for job in jobs:
        if excluded(job, excludes):
            skipped += 1
            continue

        key = job_key(job)
        if key in seen and not show_seen:
            already_seen += 1
            continue

        job["_age"] = posting_age_hours(job)
        job["_target"] = is_target(job, targets)
        job["_ghost"], job["_ghost_reasons"] = ghost_score(job)
        job["_seen_before"] = key in seen

        if job["_target"]:
            target_hits.append(job)
        elif job["_age"] is not None and job["_age"] <= 24:
            fresh.append(job)
        else:
            older.append(job)

    def by_age(items: list[dict]) -> list[dict]:
        return sorted(items, key=lambda j: (j["_age"] is None, j["_age"] or 0))

    now = datetime.now()
    lines = [
        f"# Fresh Jobs — {now:%Y-%m-%d %H:%M}",
        "",
        f"Window: last **{hours}h** · sites: {', '.join(cfg['sites'])} · "
        f"{len(target_hits) + len(fresh) + len(older)} new postings",
        "",
        f"_{already_seen} already seen in earlier runs, {skipped} excluded by keyword._",
        "",
        "---",
        "",
    ]

    lines += render_section(
        "Target companies — these jump the queue",
        by_age(target_hits),
        empty="No target-company postings in this window.",
        note="**Outreach rule applies.** Someone must be contacted here before you apply "
        "([Rule 1](../../00_Start_Here/THE-RULES.md)).",
    )

    lines += render_section(
        f"Posted in the last 24h ({len(fresh)})",
        by_age(fresh),
        empty="Nothing under 24h outside the target list.",
        note="Apply today. Every hour of delay costs measurable conversion.",
    )

    if older:
        lines += render_section(f"Older in window ({len(older)})", by_age(older), empty="")

    lines += [
        "## Next",
        "",
        "1. Triage each posting: **apply today** / **outreach first** / **skip**",
        "2. Target companies: check `04_Trackers/outreach.csv` — has anyone been contacted?",
        "   If not, send the message now, then apply. Do not wait for a reply",
        "3. Log everything you apply to in `04_Trackers/applications.csv`, "
        "including `hours_since_posting`",
        "",
    ]
    return "\n".join(lines)


def render_section(heading: str, jobs: list[dict], empty: str, note: str = "") -> list[str]:
    lines = [f"## {heading}", ""]
    if note:
        lines += [note, ""]
    if not jobs:
        if empty:
            lines += [f"_{empty}_", "", "---", ""]
        return lines

    for job in jobs:
        age = job["_age"]
        age_str = f"{age:.0f}h ago" if age is not None else "date unknown"
        flags = []
        if job["_target"]:
            flags.append(f"**TARGET: {job['_target']}**")
        if job["_ghost"] in ("med", "high"):
            flags.append(f"ghost-risk: {job['_ghost']}")
        if job.get("_seen_before"):
            flags.append("seen before")

        title = job.get("title") or "(no title)"
        company = job.get("company") or "(unknown company)"
        url = job.get("job_url") or ""

        lines.append(f"### {title} — {company}")
        lines.append("")
        lines.append(
            f"- **Posted:** {age_str} · **Location:** {job.get('location') or 'n/a'} "
            f"· **Source:** {job.get('site') or 'n/a'}"
        )
        if url:
            lines.append(f"- **Link:** {url}")
        if flags:
            lines.append(f"- {' · '.join(flags)}")
        if job["_ghost_reasons"] and job["_ghost"] != "low":
            lines.append(f"- _Ghost signals: {', '.join(job['_ghost_reasons'])}_")
        lines.append("")

    lines += ["---", ""]
    return lines


# ------------------------------------------------------------------------------ main


def main() -> int:
    parser = argparse.ArgumentParser(description="Daily fresh-jobs sweep.")
    parser.add_argument("--hours", type=int, default=24, help="lookback window (default 24)")
    parser.add_argument("--config", default="config.yml", help="config file (default config.yml)")
    parser.add_argument(
        "--show-seen", action="store_true", help="include postings from previous runs"
    )
    parser.add_argument("--no-cache", action="store_true", help="do not update the seen cache")
    args = parser.parse_args()

    cfg = load_config(HERE / args.config)
    seen = load_seen()

    print(f"Sweeping the last {args.hours}h across {', '.join(cfg['sites'])}...")
    jobs = search(cfg, args.hours)

    if not jobs:
        print("\nNo postings returned. Either it is a quiet day, or a source is failing.")
        print("Do the sweep manually today — see 02_Playbooks/02-EARLY-APPLICATION-SYSTEM.md")
        return 1

    print(f"\n{len(jobs)} unique postings. Building digest...")
    digest = build_digest(jobs, cfg, args.hours, seen, args.show_seen)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / f"{datetime.now():%Y-%m-%d}-fresh-jobs.md"
    out_path.write_text(digest, encoding="utf-8")

    if not args.no_cache:
        stamp = datetime.now().isoformat()
        for job in jobs:
            seen.setdefault(job_key(job), stamp)
        save_seen(seen)

    print(f"\nDigest written to: {out_path}")
    print("Open it, triage, and work the queue. 45 minutes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
