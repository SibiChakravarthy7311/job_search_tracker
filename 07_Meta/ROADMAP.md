# Roadmap

> What this repo is, phase by phase. Not a product roadmap — a plan for how the crew's workflow
> matures as real data accumulates.

**Current: Phase 1**

---

## Phase 0 — Written ✅

The workflow exists on paper. Playbooks, templates, trackers, rules, the crew protocol, and the
sweep tool. Assembled from mentor conversations and published research.

**Status:** done, 2026-08-21. Everything in it is an untested prior.

---

## Phase 1 — Run it (weeks 1-6)

**Goal: generate real data.** Nothing here is validated yet, and it cannot be until somebody
works it for six weeks.

- [ ] Both crew members onboarded, folders created, target lists built
- [ ] Weekly check-in running without being missed
- [ ] `fresh_jobs.py` set up, or the manual sweep habit established
- [ ] 30+ outreach contacts logged (the minimum for the numbers to mean anything)
- [ ] 30+ applications logged with `hours_since_posting`
- [ ] 5+ coffee chats held
- [ ] 6 consecutive weeks of LinkedIn posts

**Exit criterion:** enough logged data to answer "what is actually converting for us" with
numbers instead of impressions.

**The main risk in this phase is not doing it.** Every failure mode is the same one: the sweep
gets skipped, outreach slides, the check-in gets postponed, and week 4 arrives with nothing
logged. That is what the crew is for.

---

## Phase 2 — Measure (weeks 6-12)

**Goal: replace assumptions with evidence.**

- [ ] First real analysis pass over the trackers
- [ ] Reply rate by seniority tier — who actually answers us
- [ ] Reply rate by opener type — which template is doing the work
- [ ] Application → screen rate, **split by referred vs cold.** The number that either validates
      [Rule 1](../00_Start_Here/THE-RULES.md) or forces us to rewrite it
- [ ] Which sources produce *interviews*, not just postings
- [ ] Rewrite the playbooks wherever our data disagrees with them

**Deliverable:** an `ANALYSIS.md` in `07_Meta/`, updated monthly, that supersedes
[WHY-THIS-WORKS.md](../05_Knowledge/WHY-THIS-WORKS.md) wherever the two conflict. Our numbers
beat general research for our search.

**Tooling worth building here, and only here:** the response-rate analysis script. It needs no
scraping and answers the questions that matter most.

---

## Phase 3 — Tighten (weeks 12+)

**Goal: cut what does not work, double what does.**

- [ ] Drop any channel with four weeks of zero output
- [ ] Rebalance the volume/targeted application ratio against actual conversion
- [ ] Rewrite the templates that are not getting replies
- [ ] Re-tier the target companies against reality
- [ ] Follow-up reminder tooling, if follow-ups are still being missed by then
- [ ] Repost detection in the sweep

---

## Phase 4 — Hand it on

**Goal: make it useful to the next person.**

- [ ] Strip anything crew-specific, publish the repo publicly
- [ ] Write up what actually worked, honestly, including what did not
- [ ] Keep it alive as members land jobs and move into the expertise seat

A crew member who has landed knows things about the process that nobody still searching does.
Capturing that before they forget is the point of this phase.

---

## Known gaps

Honest list of what is missing or weak right now:

| Gap | Why it is still open |
|---|---|
| **No validation of any of it** | Phase 1 exists to fix this. Every number in the knowledge base is someone else's |
| **No response-rate analysis** | Needs ~30 contacts of data first. Highest-value thing to build in Phase 2 |
| **Ghost detection is crude** | Cannot see the strongest signal — unchanged reposts on a 30-day cycle. Needs months of history |
| **No salary benchmarking** | Deliberately deferred. Levels.fyi and coffee chats cover it manually |
| **No follow-up reminders** | Manual, off `outreach.csv`. Fine at current volume; a real gap above ~50 contacts |
| **Interview question bank is per-member** | Should probably be shared and anonymised once there is enough of it |
| **`fresh_jobs.py` covers only what JobSpy covers** | Company careers pages are still manual — and they are where target-company postings appear first |
| **Nothing covers contract, freelance, or non-traditional paths** | Out of scope for now. Worth adding if either member goes that route |

---

## Deliberately not doing

Decided once, so it does not get re-litigated at every retro:

- **No scraping LinkedIn.** ToS, and a restricted account mid-search is a serious loss.
  See the ethics note in [SOURCES-REGISTRY.md](../05_Knowledge/SOURCES-REGISTRY.md)
- **No automated outreach.** It reads as automated and destroys the only advantage the approach
  has. Templates yes, bots no
- **No web app.** Markdown and CSV in git is readable, forkable, diffable, and needs no
  maintenance. A web app would be a project competing with the job search for time
- **No AI-generated cover letters sent unreviewed.** Assisted drafting is fine; unread output is
  how you send a letter with the wrong company name in it
