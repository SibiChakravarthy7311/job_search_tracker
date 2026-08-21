# The Early Application System

> Applications submitted in the first 24 hours show roughly **5x** the interview rate.
> This playbook is the machine that makes that possible: a 15-minute daily sweep that surfaces
> everything posted since yesterday.

---

## Why speed beats quality here

The mechanism is not mysterious and it is not about merit:

1. **ATS queues are ordered by submission time.** The first applications are the first read.
2. **Recruiters read the first batch.** Attention is highest at the top of the pile.
3. **Manual review is capped.** A posting with 1000 applicants often gets 50 resumes actually
   read by a person. Being #40 and being #400 are different jobs.
4. **Some recruiters have fill-speed incentives.** They close early when they have enough.

The corollary is the uncomfortable part: **you can be the strongest candidate and never be seen**,
because someone adequate reached the final round while your application was still queued.

**Nothing else in your search has this leverage-to-effort ratio.** A better resume takes weeks to
build. Applying on day zero instead of day four takes fifteen minutes a morning.

### The counter-evidence, honestly

About **22% of successful applicants applied in the last 48 hours** of a posting. Exceptional,
obvious fit overrides timing. So: do not skip a great late-stage match. Just never build a
strategy that requires you to be that person.

---

## The 15-minute sweep

Every weekday morning. Before email, before anything.

### Step 1 — Run the tool (2 min)

```bash
cd 06_Tools
python fresh_jobs.py
```

Outputs a markdown digest of everything posted in the last 24 hours matching your search terms,
with target-company matches pinned at the top. See [06_Tools/README.md](../06_Tools/README.md).

**No tool?** Do it manually, it takes five minutes more:

- LinkedIn Jobs → your search → **Date Posted: Past 24 hours** → sort by most recent
- Indeed → search → `&fromage=1` in the URL, or the "Last 24 hours" filter
- Each Tier A/B company's **own careers page** — the aggregators miss postings and are hours
  behind. This is why the target list matters
- Your school's career portal, if you have one
- Community job channels (Discord/Slack servers in your field)

### Step 2 — Triage into three buckets (5 min)

| Bucket | Criteria | What happens |
|---|---|---|
| **Apply today** | Reasonable fit, posted <24h, not obviously a ghost | Goes into the application block |
| **Outreach first** | Target company, or great fit worth the extra step | Send the message *now*, then apply today anyway |
| **Skip** | Ghost signals, hard-requirement mismatch, wrong location/authorization | Note it and move on |

Do not agonise. Triage is a 10-second decision per posting. The application block is where
judgment happens.

### Step 3 — Priority sort (3 min)

When there are more postings than time, rank by:

```
priority  =  recency          (steep decay after 24h)
          ×  fit              (can I claim most of the must-haves?)
          ×  (1 - ghost_risk) (see below)
          ×  referral_bonus   (do I know anyone inside? big multiplier)
```

A mediocre-fit posting at a company where you know someone beats a perfect-fit cold posting.
Almost every time.

### Step 4 — Queue it (5 min)

Add each "apply today" posting to `04_Trackers/applications.csv` with its posting time, then
work the queue in the application block.

---

## Ghost job filtering

**20-30% of postings are for roles nobody intends to fill now.** Companies post them to build
resume pipelines, probe salary expectations, gather skill-trend data, or look like they are
growing. The 1,001-5,000 employee band is the worst offender at around 24.8%.

**Signals, in rough order of reliability:**

- Live for **3+ months** without being taken down
- Reappears every 30-ish days, unchanged — a genuine repost usually has *edited* requirements
- Vague description with no team, no product, no actual responsibilities
- Unrealistic skill stacking — every technology in the industry on one requisition
- No named hiring manager or recruiter anywhere
- The company has had "12 open roles" continuously for a year

**How to act on it:** downrank, do not hide. The cost of a false positive (skipping a real job)
is far higher than the cost of a wasted 12-minute application. Flag it in the tracker as
`ghost_risk=high` and apply anyway if the fit is strong — but never do outreach or tailoring
work for one.

---

## Reposts are the opposite — they are gold

A posting that reappears after ~3 weeks *with changes* means: they searched, they did not find
anyone, and they still need the person. The urgency is higher, the applicant pool has already
been exhausted once, and the bar has often quietly moved.

Distinguish from a ghost: **a real repost shows edited requirements, a changed title, or a live
recruiter attached.** An unchanged repost on a 30-day cycle is a pipeline-builder.

---

## When to apply

| | |
|---|---|
| **Best days to submit** | Tuesday - Thursday |
| **Best time** | 8-11 AM local, roughly 30% better response |
| **Worst** | Weekend, Monday after 4 PM |

**But recency beats the ideal window.** A Saturday-evening application to something posted two
hours ago beats a Tuesday-morning application to the same posting on day four. Never hold a
fresh posting for a better time slot.

---

## Weekly maintenance

- **Add and remove search terms.** Titles vary wildly across companies for identical work —
  "Software Engineer", "Software Developer", "Backend Engineer", "Member of Technical Staff",
  "SDE I". Missing a title variant means missing a whole category of postings
- **Check which sources produced anything.** A source with zero relevant postings in three weeks
  comes out of the rotation
- **Verify the target-company careers pages** are still where you think they are

---

## The failure mode to watch for

Building and tuning the tool instead of applying to jobs. It is the most comfortable-feeling
procrastination available to an engineer running a job search, and it is still procrastination.

**Rule: if the tool is broken, do the sweep manually and fix the tool on Saturday.** The sweep
never gets skipped because tooling broke.
