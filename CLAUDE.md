# CLAUDE.md — Job Search Tracker

> Context file for any AI assistant or new human reader working in this repo.
> Read this first, then [README.md](README.md).

---

## What this repo is

A shared, updatable job-search operating system for a small crew — two people to start, possibly
more later. Markdown and CSV in git. **Not an application.** See
[07_Meta/decisions/0001-markdown-and-csv-in-git.md](07_Meta/decisions/0001-markdown-and-csv-in-git.md)
for why, and treat that decision as settled.

It exists because a job search run alone is run on mood, and a job search run with a crew that
holds you to weekly numbers is run on a system.

---

## Orientation, in order

1. This file
2. [README.md](README.md) — the front door
3. [00_Start_Here/THE-RULES.md](00_Start_Here/THE-RULES.md) — the nine non-negotiables
4. [02_Playbooks/00-WEEKLY-OPERATING-RHYTHM.md](02_Playbooks/00-WEEKLY-OPERATING-RHYTHM.md) — the master workflow
5. [07_Meta/ROADMAP.md](07_Meta/ROADMAP.md) — current phase and known gaps

---

## The three facts that drive every decision here

1. **Referrals and relationships beat applications.** The mentor consensus behind this repo was
   unanimous. This drives the hardest rule in it: never apply to a target company without
   contacting a human there first.
2. **First-24-hour applications get ~5x the interview rate.** Speed from discovery to submission
   is the second-biggest lever. **Any feature or process that adds friction to time-to-apply is
   suspect.**
3. **~75% of resumes are auto-rejected by ATS** on formatting and keywords, not qualifications.
   Fixing that once pays out on every application.

Evidence and sources: [05_Knowledge/WHY-THIS-WORKS.md](05_Knowledge/WHY-THIS-WORKS.md).

---

## Repo structure

```
00_Start_Here/    Quickstart, THE-RULES.md
01_Crew/          Charter, roster, accountability protocol, per-member folders
02_Playbooks/     Numbered 00-11 in the order you need them
03_Templates/     Copy-paste scripts: outreach, follow-ups, chats, posts, check-in
04_Trackers/      CSVs: applications, outreach, target companies, chats, events
05_Knowledge/     Evidence base, mentor wisdom, sources registry
06_Tools/         fresh_jobs.py — the daily recency sweep
07_Meta/          Roadmap, decisions, proposals, retrospectives
Weekly_Checkins/  One file per week. The accountability record
```

---

## Conventions

- **Two file classes.** Personal files (`01_Crew/members/<name>/`, your tracker rows, your half
  of a check-in) are edited freely. Shared files (playbooks, templates, rules, knowledge, tools)
  change by PR with another crew member reviewing. See [CONTRIBUTING.md](CONTRIBUTING.md)
- **Attribute every tip.** "From a senior dev at a mid-size company" is fine; unattributed is
  not. Six months later you will want to know whether a rule came from a hiring manager or a
  Reddit comment
- **Keep contradictions.** When new advice conflicts with what is written, record both and mark
  which one the crew is currently running. The two-follow-ups cap in
  [THE-RULES.md](00_Start_Here/THE-RULES.md) versus the mentor advice to follow up until reply is
  a live, deliberate example
- **Every rule carries a why and an escape hatch.** Rules without escape hatches get broken
  quietly and then abandoned
- **Process changes bump the version** in [CHANGELOG.md](CHANGELOG.md). Logging a week does not
- **Decisions that would otherwise get re-litigated get an ADR** in `07_Meta/decisions/`

---

## Writing style for this repo

Direct, specific, and honest about uncertainty. The reader is a stressed person looking for the
next action, not an audience.

- **Name the next action.** "Work on networking" fails. "Email 3 alumni Tuesday at 10:24, using
  template B" works
- **Numbers over adjectives.** "9 outreach, 3 replies, 1 chat booked" beats "networked more"
- **State what is uncertain.** The research figures are indicative, not precise, and the repo
  says so. Where there is counter-evidence, it is included
- **No motivational filler.** The crew charter is about mechanism, not inspiration

---

## Privacy — this matters

**Assume this repo goes public.**

- **Never commit** full names, emails, or phone numbers of outreach contacts. Use initials + role
  + company: `P.K., Senior Backend Engineer, ExampleCorp`
- **Never commit** resumes with home addresses or phone numbers (gitignored by pattern)
- **Never commit** API keys. `06_Tools/config.yml` and `.env` are gitignored
- Salary numbers, rejections, and doubts shared inside the crew are confidential per the
  [charter](01_Crew/CREW-CHARTER.md)

---

## Red flags — push back if you see these

- **Anything that slows time-to-apply.** See fact #2. This is the most common way well-meaning
  additions make the search worse
- **Building tooling instead of applying.** The most comfortable procrastination available to an
  engineer running a job search. `06_Tools/README.md` carries an explicit warning about it, and
  it applies to anyone proposing new tools
- **Scraping LinkedIn.** ToS violation, and a restricted account mid-search is a serious loss.
  Deliberately excluded, not overlooked
- **Automating outreach messages.** Reads as automated, destroys the only advantage the approach
  has
- **A rule with no escape hatch**, or a claim with no source
- **Adding a 40-company target list.** 10-15 is the number; more turns the list back into a wish
  list that cannot be worked
- **Turning this into a web app.** Settled in ADR 0001
