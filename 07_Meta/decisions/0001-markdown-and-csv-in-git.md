# 0001 — Markdown and CSV in git, not an app

**Date:** 2026-08-21 · **Status:** Accepted

---

## Context

The crew needs a shared, updatable job-search workflow that two people (and possibly more later)
can read, follow, edit, and hold each other to. The obvious options were a Notion workspace, a
spreadsheet, a purpose-built web app, or plain files in a git repository.

There is a real pull toward building the app. Both crew members are engineers, the data model is
interesting, and a tracker with a proper schema and a dashboard would be genuinely nicer to use
than a CSV.

## Decision

**Markdown and CSV in a GitHub repository.** No application, no database, no hosted service.

## Rationale

- **The workflow must be editable by the people running it**, on a Sunday evening, from a phone
  if necessary. Markdown clears that bar; a schema migration does not
- **Git gives us the review mechanism for free.** Branch, PR, the other person reviews. That is
  exactly the "propose a change to the shared workflow" loop the crew needs, and it took zero
  code
- **Git history is the accountability record.** `git log Weekly_Checkins/` shows what the search
  actually looked like over three months. No dashboard we would build would beat that
- **Per-member folders eliminate merge conflicts** without any coordination mechanism
- **The failure mode of building an app is the decisive argument.** Time spent on the tracker is
  time not spent applying and not spent on outreach. A job-search tool that delays the job search
  is a net negative, and it is *very* comfortable procrastination for an engineer under pressure
- **CSV is not a limitation in practice.** It opens in Excel, Sheets, and pandas. Every analysis
  in the Phase 2 plan is a two-line groupby

## Consequences

**Accepted costs:**

- Manual data entry. Mitigated by keeping the tracker columns few and the logging habit immediate
- No automatic reminders. Follow-up timing is manual off `outreach.csv` — a real gap above ~50
  contacts, noted in the roadmap
- CSV merge conflicts are possible when two people edit the same file simultaneously. The fix is
  trivial: keep both sets of rows. Per-member files are the escape hatch for crews of 3+
- No pretty dashboard. Nobody's motivation actually depends on this

**One exception granted:** `06_Tools/fresh_jobs.py`. Automating the daily sweep is justified
because it directly serves the highest-leverage rule in the repo (apply within 24 hours) and
because 15 minutes a day, every weekday, is a real recurring cost. It is deliberately kept to a
single script with no state beyond a seen-file, and the tool README carries an explicit warning
against expanding it.

## Revisit if

- The crew grows past four people and per-member CSVs stop scaling
- Somebody lands a job and has spare capacity to build the app for the next cohort
- Manual logging is demonstrably being skipped *because* of the friction — as opposed to being
  skipped for the ordinary reason, which is that logging is boring
