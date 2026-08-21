# Tools

## `fresh_jobs.py` — the daily recency sweep

Surfaces everything posted in the last 24 hours matching your searches, pins target-company
matches at the top, flags likely ghost jobs, and writes a markdown digest for the morning
application block.

**Why it exists:** first-24-hour applications show roughly 5x the interview rate. Seeing the
posting on day zero is the entire advantage. See
[the early application playbook](../02_Playbooks/02-EARLY-APPLICATION-SYSTEM.md).

---

## Setup — five minutes

```bash
cd 06_Tools
python -m venv .venv

# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Windows (Git Bash):    source .venv/Scripts/activate
# macOS / Linux:         source .venv/bin/activate

pip install -r requirements.txt
cp config.example.yml config.yml
```

Then edit `config.yml`:

1. **`search_terms`** — your role, **with title variants**. The same job is posted as "Software
   Engineer" at one company and "Member of Technical Staff" at another. Missing a variant means
   missing a whole category of postings
2. **`locations`** — your cities. Keep the empty string `""` entry to catch remote and
   unspecified-location postings
3. **`target_companies`** — your 10-15 from `TARGET-COMPANIES.md`. These get pinned to the top
   and flagged with the outreach rule
4. **`exclude_keywords`** — titles to filter out. **Keep this short.** Over-filtering is how you
   miss the role that was worth applying to

`config.yml` is gitignored, so every crew member keeps their own search without stepping on
anyone else's.

---

## Running it

```bash
python fresh_jobs.py                  # last 24h, the daily default
python fresh_jobs.py --hours 48       # after a weekend or a missed day
python fresh_jobs.py --show-seen      # include postings from previous runs
python fresh_jobs.py --config amal.yml  # a second config in the same checkout
python fresh_jobs.py --no-cache       # do not record what was seen this run
```

Output lands in `output/YYYY-MM-DD-fresh-jobs.md` (gitignored). Open it, triage into
**apply today / outreach first / skip**, and work the queue.

---

## What the digest gives you

**Three sections, in priority order:**

1. **Target companies** — pinned to the top regardless of age, with the outreach-first rule
   attached ([Rule 1](../00_Start_Here/THE-RULES.md))
2. **Posted in the last 24h** — the 5x bucket. Apply today
3. **Older in window** — everything else, oldest last

**Per posting:** age in hours, location, source, link, and a `ghost-risk` flag where the
heuristic fired.

**The seen-cache** (`.seen_jobs.json`) means the same posting does not reappear every morning.
It is keyed on company + title + location rather than URL, since URLs carry tracking parameters
that change between runs. Entries older than 45 days are pruned automatically.

---

## The ghost-risk flag

A weighted heuristic, not a verdict:

| Signal | Weight |
|---|---|
| Posted 90+ days ago | 3 |
| Posted 45+ days ago | 2 |
| Each buzzword ("rockstar", "wear many hats", …) | 1 |
| Very short description | 1 |

3+ points is `high`, 2 is `med`, below that it is not shown.

**It downranks; it never hides.** The cost of a false positive — skipping a real job — is far
higher than a wasted twelve-minute application. What a `high` flag should stop is *outreach and
tailoring effort*, not the application itself.

The heuristic is deliberately crude and cannot see the strongest real signal — the same posting
reappearing unchanged on a 30-day cycle. Tracking that needs months of history. Your own memory
is better at it for now.

---

## When it breaks

It will, occasionally. Job boards change their markup, rate-limit, or block a request.

**Do the sweep manually and fix the tool on Saturday.** The sweep never gets skipped because
tooling broke ([Rule 3](../00_Start_Here/THE-RULES.md)).

**Manual sweep — five extra minutes:**

- LinkedIn Jobs → your search → **Date Posted: Past 24 hours** → sort by most recent
- Indeed → search → **Last 24 hours** filter (or `&fromage=1` in the URL)
- Each Tier A/B company's **own careers page** — aggregators miss postings and run hours behind
- Your school's career portal
- Community Discord and Slack job channels in your field

**Common failures:**

| Symptom | Cause / fix |
|---|---|
| `PyYAML not installed` | Virtualenv not activated, or `pip install -r requirements.txt` not run |
| `python-jobspy not installed` | Same |
| One site returns 0 every time | That source is rate-limiting or blocking. Drop it from `sites` for a few days |
| Zero results everywhere | Usually too-narrow `search_terms` or an over-aggressive `exclude_keywords` list. Widen both |
| Everything is "date unknown" | Some sources do not publish a posting date. Not a bug; those land in the "older" bucket |

---

## A warning worth taking seriously

**Building and tuning this tool is the most comfortable procrastination available to an engineer
running a job search.** It feels productive, it is technically interesting, and it produces zero
applications.

The tool is a 15-minute-a-day convenience. If you have spent more than one Saturday on it, stop
and go send some outreach messages.

---

## Ideas, if you genuinely have spare time

Roughly in order of value per hour spent:

- **Response-rate analysis** over `04_Trackers/outreach.csv` — reply rate by seniority tier, by
  opener type, by channel. This is the highest-value addition and needs no scraping at all
- **Follow-up reminders** — read `outreach.csv`, print who is due for follow-up 1 or 2 today
- **Repost detection** — keep posting hashes over time, flag anything reappearing unchanged
- **A digest email or webhook** so the sweep arrives instead of needing to be run
- **JD keyword extraction** across everything you applied to, to see which terms keep appearing
  that you cannot yet claim. That is next month's learning plan, generated from real demand

**Do not build:** anything that automates sending outreach messages. It violates platform terms,
it reads as automated, and it destroys the only advantage the whole approach has.
