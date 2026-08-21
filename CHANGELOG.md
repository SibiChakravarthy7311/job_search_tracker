# Changelog

All notable changes to the crew workflow. Version bumps mean the *process* changed, not that
someone logged a week.

Format: `## [version] — YYYY-MM-DD`, newest first.

---

## [0.1.0] — 2026-08-21

Initial workflow. Assembled from mentor conversations, the manual job-search process notes, and
published research on ATS behaviour, application timing, and ghost jobs.

**Added**
- Crew charter, roster, and the weekly accountability protocol
- The non-negotiable rules, including outreach-before-application
- Playbooks 00–11: weekly rhythm, target companies, early application, outreach, LinkedIn
  visibility, coffee chats, networking events, charisma and small talk, resume and ATS,
  application process, interviews, offer and negotiation
- Copy-paste template pack: LinkedIn connection notes, cold emails, follow-up sequences,
  coffee-chat question banks, referral asks, LinkedIn post formats
- Four CSV trackers and a weekly scoreboard
- `06_Tools/fresh_jobs.py` — recency-first job sweep built on JobSpy
- Knowledge base: the evidence behind each rule, with sources

**Known gaps** — see [07_Meta/ROADMAP.md](07_Meta/ROADMAP.md)
- No response-rate analysis yet; needs ~6 weeks of real outreach data first
- `fresh_jobs.py` has no dedupe across runs beyond the seen-file
- Salary benchmarking is a stub
