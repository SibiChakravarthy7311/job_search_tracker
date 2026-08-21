# Job Search Crew

> A shared, updatable job-search operating system for a small crew — two people to start,
> more if they earn it.
>
> The premise: a job search run alone is run on mood. A job search run with a crew is run on
> a system. This repo is the system.

---

## What this is

A GitHub repo that two or more people run their job search out of, together. It holds:

- **The playbooks** — what to do, in what order, with the reasoning attached
- **The templates** — the exact words to send, so cold outreach stops being a blank page
- **The trackers** — CSVs for applications, outreach, target companies, coffee chats
- **The crew protocol** — weekly goals, weekly check-ins, and the rules for holding each other to them
- **A small tool** — surfaces the freshest job postings, because applying early is worth ~5x

It is deliberately **not** an app. It is markdown and CSV in git, so anyone can read it, fork it,
change it, and propose the change back. The workflow improves because the people using it keep
editing it.

---

## The three things that actually move the needle

Everything in this repo exists to serve one of these. If a proposed addition serves none of
them, it does not go in.

| # | Fact | What it forces |
|---|---|---|
| 1 | **Referrals and relationships beat applications.** People who already know you get contacted before the role is posted. | [Never apply cold](00_Start_Here/THE-RULES.md). Outreach comes *before* the application. |
| 2 | **First-24-hour applications get ~5x the interview rate.** | A [daily fresh-postings sweep](02_Playbooks/02-EARLY-APPLICATION-SYSTEM.md), not a weekly one. |
| 3 | **~75% of resumes are auto-rejected by ATS** on formatting and keywords, not qualifications. | A [format and keyword ruleset](02_Playbooks/08-RESUME-AND-ATS.md) that is not optional. |

Evidence and sources: [05_Knowledge/WHY-THIS-WORKS.md](05_Knowledge/WHY-THIS-WORKS.md).

---

## Start here

**New crew member, first hour:** [00_Start_Here/QUICKSTART.md](00_Start_Here/QUICKSTART.md)

**The non-negotiables, read before anything else:** [00_Start_Here/THE-RULES.md](00_Start_Here/THE-RULES.md)

**How the week actually runs:** [02_Playbooks/00-WEEKLY-OPERATING-RHYTHM.md](02_Playbooks/00-WEEKLY-OPERATING-RHYTHM.md)

---

## Repo map

```
job-search-crew/
├── 00_Start_Here/       Quickstart, the non-negotiable rules, the vocabulary
├── 01_Crew/             Charter, roster, accountability protocol, per-member folders
│   └── members/         One folder per person. Your goals, targets, logs live here
├── 02_Playbooks/        The how-to, numbered in the order you'll need them
├── 03_Templates/        Copy-paste scripts: LinkedIn notes, cold emails, follow-ups, posts
├── 04_Trackers/         CSVs — applications, outreach, target companies, coffee chats
├── 05_Knowledge/        The evidence base. Why each rule exists, with sources
├── 06_Tools/            fresh_jobs.py — the recency sweep
├── 07_Meta/             Roadmap, decision records, how to propose changes
└── Weekly_Checkins/     One file per week, shared. The accountability record
```

---

## How the crew uses it

1. **Every member has a folder** in [01_Crew/members/](01_Crew/members/). Your target companies,
   your goals, your logs. No merge conflicts, because you only ever edit your own.
2. **The shared docs change by proposal.** Found a tip that works? Open a PR against the playbook.
   The other person reviews it. See [CONTRIBUTING.md](CONTRIBUTING.md).
3. **Weekly check-in is a file, not a chat message.** Every week gets a file in
   [Weekly_Checkins/](Weekly_Checkins/) that both people fill in and both people read.
   Chat disappears; the file is the record. See
   [01_Crew/ACCOUNTABILITY-PROTOCOL.md](01_Crew/ACCOUNTABILITY-PROTOCOL.md).
4. **Numbers, not vibes.** The check-in has a scoreboard. "I networked more this week" is not
   an entry. "9 outreach messages, 3 replies, 1 coffee chat booked" is.

---

## The one rule that matters most

> **No application to a target company without a human contacted there first.**

Not "ideally." Not "when there's time." Applying cold to a target company puts your resume in
a stack of 900 with a ~2% read rate. One message to one engineer changes the odds more than any
resume edit you will ever make.

The full rule set, including the deliberate escape hatches: [00_Start_Here/THE-RULES.md](00_Start_Here/THE-RULES.md).

---

## Status

Version 0.1 — the workflow is written, the crew is forming. See [07_Meta/ROADMAP.md](07_Meta/ROADMAP.md)
for what is next and [CHANGELOG.md](CHANGELOG.md) for what has changed.

This repo is meant to be edited. If something here is wrong, or stopped working, or you found
better — change it and say why.
