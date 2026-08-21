# Why This Works — the evidence base

> Every rule in this repo traces back to something here. When a rule feels arbitrary at 9pm on a
> Tuesday, this is the page to reread.
>
> **Caveat, stated up front:** these figures come from industry research, published surveys, and
> practitioner reports of varying rigour. Directionally they are consistent and widely
> corroborated; treat the exact percentages as indicative rather than precise. Where a finding
> has real counter-evidence, it is noted.

---

## The three headline numbers

| Finding | Figure | What it forces |
|---|---|---|
| Resumes auto-rejected by ATS on formatting and keywords | **~75%** | [Resume and ATS playbook](../02_Playbooks/08-RESUME-AND-ATS.md) |
| Interview-rate advantage of applying in the first 24 hours | **~5x** | [Early application system](../02_Playbooks/02-EARLY-APPLICATION-SYSTEM.md) |
| Job postings that are "ghost jobs" | **20-30%** | Downrank, do not hide |

Supporting context: average job search runs around **5 months**; best application timing is
**Tue-Thu, 8-11 AM**; personalization correlates with **substantially faster** searches.

---

## 1. Referrals and relationships beat applications

**This is the least quantified and most strongly corroborated finding in the whole repo.**

Every mentor conversation behind this project independently reached the same conclusion, without
prompting: the good jobs were not applied for.

- One person's role in a new city **was never posted publicly.** The company called them because
  they had spoken months earlier
- The same person's next role came from asking a stranger for a coffee chat
- The consistent framing across all of them: *"Talk to people you'd like to be like. Talk to them
  even if you feel uncomfortable or out of place doing so, and add them to your contacts."*

The mechanism is simple and is not about fairness. A hiring manager with 400 applications is
looking for a reason to shortlist. A person who has spoken to you is not a row in a spreadsheet,
and internal referrals arrive through a different channel with an implicit endorsement attached.

**Cold application → screen rates run around 2-5%.** Referred applications routinely run several
times that. When you have your own numbers in `04_Trackers/applications.csv` split by the
`referral` column, this stops being an argument.

**Drives:** [Rule 1](../00_Start_Here/THE-RULES.md) ·
[Outreach playbook](../02_Playbooks/03-OUTREACH-PLAYBOOK.md) ·
[Coffee chats](../02_Playbooks/05-COFFEE-CHAT-PLAYBOOK.md) ·
[Target companies](../02_Playbooks/01-TARGET-COMPANY-LIST.md)

---

## 2. Timing — the 5x finding

**Applications submitted in the first 24 hours show roughly 5x the interview rate.**

The mechanism, which is what makes it credible:

1. **ATS queues are ordered by submission time.** The first in are the first read
2. **Recruiter attention is highest at the top of the pile**
3. **Manual review is capped.** A posting with 1000 applicants commonly gets ~50 resumes read by
   a human. Being #40 and being #400 are different situations entirely
4. **Some recruiters carry fill-speed incentives** and close early

The corollary is the part worth internalising: **you can perform excellently in every round and
still be dropped** because someone adequate reached the final stage first and the manager decided
they were good enough.

**Optimal windows:** Tuesday-Thursday, 8-11 AM local, roughly 30% better response than average.
Worst: weekends, and Monday after 4 PM.

**Counter-evidence:** about **22% of successful applicants applied in the last 48 hours** of a
posting. Exceptional, obvious fit overrides timing. So do not skip a great late-stage match —
just never build a strategy that requires being that person.

**Reposts are high-value.** A posting reappearing after ~3 weeks *with edits* means they searched,
did not find anyone, and still need the person. Higher urgency, exhausted applicant pool.

**Drives:** [Rule 2, 3, 4](../00_Start_Here/THE-RULES.md) ·
[Early application system](../02_Playbooks/02-EARLY-APPLICATION-SYSTEM.md) ·
[06_Tools/fresh_jobs.py](../06_Tools/)

---

## 3. ATS rejects ~75% of resumes on format and keywords

Not on qualifications. On parsing failures and missing exact-match terms.

**Root causes**, in rough order of damage: text boxes and layered elements the parser ignores;
information carried in graphics; **multi-column layouts that scramble reading order**;
non-standard date formats; unusual margins; decorative fonts; contact details in headers and
footers.

**Keyword behaviour:**

- **Exact phrase matching is real.** "Adobe Creative Cloud" does not match "Adobe Creative Suite"
- **Placement is weighted** — a term in the summary carries roughly **3-5x** the weight of the
  same term in a role from four years ago
- Modern systems do some NLP ("JS" → "JavaScript"), but relying on it is a bad bet

**After the parser, a human spends 30-100 seconds.** Density is a liability; findability is the
asset. Optimizing only for the machine produces a document no human will read.

**Free scanners:** Jobscan, ATSFriendly, Enhancv, ResyMatch. Run 2-3, target 75%+ match.

**Drives:** [Resume and ATS playbook](../02_Playbooks/08-RESUME-AND-ATS.md)

---

## 4. Ghost jobs — 20-30% of postings

Postings for roles that do not exist or that the employer has no intention of filling now.

**Worst offenders:** companies in the 1,001-5,000 employee band, around a 24.8% ghost rate.

**Why companies do it:** building a resume pipeline for future openings, researching competitor
employee availability, probing market salary expectations, gathering skill-trend data, and
appearing to grow.

**Detection signals:** live 3+ months without removal; reappears unchanged every ~30 days; vague
description with no team or product; unrealistic skill stacking; no named recruiter or hiring
manager anywhere.

**How to act:** **downrank, do not hide.** The cost of a false positive — skipping a real job — is
much higher than a wasted twelve-minute application. What ghost-risk should stop is *outreach and
tailoring effort*, not the application itself.

**Drives:** the triage step in the [early application system](../02_Playbooks/02-EARLY-APPLICATION-SYSTEM.md)

---

## 5. Personalization

- Personalized cover letters: around **15% higher response rate** than templated ones
- Personalization plus targeting correlates with a **substantially faster search** — reports of
  5 months compressing to 1-3
- Manual cover letter: 20-30 minutes. Template plus real personalization: ~5 minutes

**The reconciliation this repo uses:** do not write more cover letters. Write fewer, better ones
for Tier A and B, using a small set of tuned variants adapted in five minutes — and spend the
saved time on outreach, which converts far better than any letter.

The same logic governs outreach templates: [03_Templates/](../03_Templates/) exists so that
personalization costs you three changed sentences rather than a blank page.

**Drives:** the cover letter section of the
[resume playbook](../02_Playbooks/08-RESUME-AND-ATS.md) · the whole template pack

---

## 6. Visibility compounds

Recruiters search LinkedIn. Profiles with current keywords, a clear headline, and recent activity
surface in searches; dormant profiles do not surface at all.

Recognition is a shortlisting heuristic under time pressure. Someone who has seen your name on
three thoughtful comments and a project post is not evaluating a stranger.

**The timeline is the hard part.** Weeks 1-6: nothing. Weeks 6-12: engagement begins. Months 3-6:
inbound messages start. This is why it starts in week one — it cannot be compressed later, at the
point where you need it.

**Comments outperform posts** for a job search. Your post reaches your network, which mostly
cannot hire you. Your comment on a target-company employee's post reaches *theirs*.

**Drives:** [Rule 8](../00_Start_Here/THE-RULES.md) ·
[LinkedIn visibility routine](../02_Playbooks/04-LINKEDIN-VISIBILITY-ROUTINE.md)

---

## 7. Bias in automated screening

Documented in resume-screening AI: white-sounding names receiving substantially more callbacks
than identical resumes with African-American-sounding names, and male-associated names
statistically favoured. Root cause is training data encoding existing societal bias.

Two reasons it is in a job-search repo:

1. **A bad search is not necessarily a verdict on you.** Some filtering is structural. That is
   worth knowing on a bad week and worth saying out loud at a check-in
2. **It is another argument for outreach-first.** A human who has spoken to you is not running a
   biased classifier over your name. Referrals route around the filter

If anyone builds scoring tooling on top of this repo: make it explainable, show *why* a score is
what it is, and prefer auditable open-source parsers to black-box scoring.

**Sources:** Brookings on gender, race and intersectional bias in AI; FAIRE bias-auditing work
(arXiv).

---

## 8. Interview dynamics

- **Pipelines run 2-7 rounds.** After an OA there is an internal score that gates the next round
- **The OA is often not measuring ability so much as producing a defensible cut.** Speed through
  the funnel frequently matters more than the score
- **Technical rounds evaluate reasoning, not completion.** Two to three problems, and solving all
  of them is a bonus rather than the bar. Brute force plus clear narration beats silence plus a
  half-finished optimal solution
- **System design is the most common under-prepared area** for candidates out of school — more so
  than algorithms, because there is no grind that makes it feel like progress
- **Preparation benchmarks:** 200-300 problems for interview-ready (3-4 months at 2-3 hrs/day);
  300-400 for top-tier (6-8 months); 50-100 system design problems

**Drives:** [Interview playbook](../02_Playbooks/10-INTERVIEW-PLAYBOOK.md)

---

## 9. Negotiation timing

**Accommodations, accessibility needs, and salary belong in the last 10-15 minutes of the final
round, or after a written offer.**

By then they have chosen you, run a process, spent internal time, and told people they found
someone. Replacing you is expensive, and **withdrawal at that point is rare.** The realistic worst
case for a polite, well-researched ask is "no, that is our best offer".

Raised early, a requirement has time to become an objection. Raised late, it is a logistics
problem to solve.

**Drives:** [Offer and negotiation](../02_Playbooks/11-OFFER-AND-NEGOTIATION.md)

---

## Where these came from

- **Mentor conversations** — technology practitioners, independently corroborating on
  networking, timing, and negotiation. Condensed in [MENTOR-WISDOM.md](MENTOR-WISDOM.md)
- **Published research** — ATS behaviour and formatting studies, application-timing research,
  ghost-job prevalence surveys, resume-screening bias auditing
- **Practitioner communities** — r/EngineeringResumes (the wiki is the strongest free resume
  resource available), r/cscareerquestions, Blind, Levels.fyi
- **Direct experience** — logged in `04_Trackers/`, which is the only source on this page
  generated by the people using it

**That last one is the point.** Everything above is a prior. Six weeks of your own tracker data
beats all of it for *your* search, and when it contradicts this page, update this page.
