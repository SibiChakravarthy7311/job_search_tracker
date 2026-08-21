# Interview Playbook

> Stage by stage. Anywhere from two to seven rounds depending on the company.

```
Application → ATS screen → [OA] → Recruiter screen → Technical → [System design]
            → Behavioural → Final / culture fit → Offer → Negotiation
```

---

## 1. Online assessment

Usually algorithmic, timed, automated. Take it **as soon as it arrives** — the same timing
dynamics that govern applications govern the funnel.

**The thing worth understanding:** in many cases the OA is not measuring your ability so much as
**producing a defensible reason to cut the pile down**. Performing well is necessary but the
decisive variable is often how fast you move through the funnel. Someone who finishes the final
round first can end the process for everyone behind them.

**Preparation benchmarks** — general industry rules of thumb, not laws:

| Target | Problems | Timeline at 2-3 hrs/day |
|---|---|---|
| Interview-ready | 200-300 | 3-4 months |
| Top-tier / FAANG-level | 300-400 | 6-8 months |

**How to practise:** at 1.2-1.3x your current comfort level, not at the hardest tier available.
Patterns over volume — two-pointer, sliding window, BFS/DFS, binary search, dynamic programming,
heaps, graphs. Twenty problems understood deeply beat a hundred half-solved.

---

## 2. Recruiter phone screen — 30-60 min

They are clarifying, not evaluating deeply. It is mostly a checklist:

- Work eligibility and legal status
- Notice period and start availability
- **Salary expectations**
- Location, relocation, remote preference
- A high-level walk through your background

**Salary handling:** give a **researched range**, never a single number, and do not commit.

> "Based on what I have seen for this kind of role in [market], I have been looking at
> [X to Y]. But I would want to understand the full scope before committing to a number —
> what range does the role sit in?"

**Turn it back if you can.** Whoever names a number first anchors the negotiation. The real
negotiation happens at the end anyway — see [offer and negotiation](11-OFFER-AND-NEGOTIATION.md).

**Prepare:** a two-minute version of your background, a clear reason you want *this* role, three
questions about the process and the team.

---

## 3. Technical round — 20-45 min with an engineer

- Two to three problems. **You are not expected to solve them all.** Solving all of them is a
  bonus, not the bar
- Screen shared. Assume no external help
- **They mainly want to hear how you think**

### The rules that actually matter

**Narrate constantly.** Silence is the failure mode. A wrong approach explained out loud is
recoverable; a correct answer arrived at silently teaches the interviewer nothing about you.

**Brute force plus a clear explanation beats silence plus a half-finished optimal solution.**
Say what the naive approach is, say what is wrong with it, say what you would do instead, and
start coding. If time runs out, you have shown everything they were looking for.

**Ask clarifying questions first.** Input size, edge cases, constraints, expected behaviour on
empty input. This is graded, and skipping it reads as carelessness.

**Talk through the test cases** at the end. Walk your own code through an example.

**If you get stuck:** say so, out loud, specifically. "I am trying to figure out how to avoid the
nested loop here" invites a hint. Silent flailing does not.

---

## 4. System design

Concept-driven and trade-off oriented. "How would you design [a well-known product] from scratch."

**The standard shape:**

1. **Clarify requirements** — functional and non-functional. Scale, latency, consistency needs
2. **Estimate** — users, requests per second, storage. Rough numbers, said out loud
3. **High-level design** — boxes and arrows. Client, API, service, storage, cache, queue
4. **Deep dive** on whichever component they push on
5. **Trade-offs** — this is the actual evaluation. Why this database, why this consistency model,
   what breaks at 10x

**ML variant:** hypothesis questions rather than architecture. Why is your model overfitting?
Underfitting? What would you check first? How would you know the training set is the problem?
How would you deploy and monitor it?

**Benchmark:** 50-100 design problems studied to be comfortable.

**This is the most common under-prepared area for candidates coming out of school**, more so than
algorithms — because there is no LeetCode-equivalent grind that makes it feel like progress.
Weight prep accordingly, and prefer reading real system design write-ups and company engineering
blogs over memorising a template.

---

## 5. Behavioural

Traditional HR territory: conflict with a teammate, a failure, a disagreement with a manager,
where you see yourself in five years, why you are leaving.

**This is the most preparable round and the one people most often walk into cold.**

**Prepare 6-8 stories in STAR form** — Situation, Task, Action, Result — covering:

- A conflict with a teammate
- A failure and what you did about it
- Something you led or drove
- A hard technical problem
- A time you learned something quickly under pressure
- A time you disagreed with a decision

**Each story gets a number in the Result.** And **each story can be reshaped** for multiple
questions — six well-prepared stories cover twenty possible questions.

**Write them down** in your `logs/`. Rehearse out loud once each. Out loud, not in your head —
they are different skills, and the gap between them is where people ramble.

---

## 6. Final round / culture fit

Usually HR plus the manager you would report to. Values, working style, hobbies, how you handle
things.

**Have real questions ready.** Three minimum. "No, I think you covered everything" is a wasted
opportunity and reads as low interest.

Good ones:

- What does success look like in this role at six months?
- What is the biggest challenge the team is facing right now?
- How do you decide what to work on?
- What is the thing people find hardest about working here?

### The negotiation window

**Accessibility needs, accommodations, and salary go in the last 10-15 minutes of this round.**

By that point you are effectively their preferred candidate and the odds of them withdrawing are
very low. Raising a requirement early gives it time to become an objection; raising it at the end,
once they have decided they want you, makes it a logistics problem to solve rather than a reason
to reconsider.

---

## Cross-cutting

**Speed through the funnel.** Reply to scheduling emails immediately. Take the earliest slot
offered. The funnel is a race more often than is comfortable.

**Log every round** in `01_Crew/members/<you>/logs/interview-<company>-<round>.md`: date,
interviewer, every question you can remember, what you said, what you would change. By the fifth
interview this is a personal question bank no prep site can match, because it is the actual
questions from the actual companies you are targeting.

**Debrief with the crew.** Within a day, while it is fresh. What was asked, where you stumbled.
The other person learns from your round without having sat it, which roughly doubles the value of
every interview either of you does.

**Mock interviews are the single highest-value crew activity.** Alternate, 45 minutes, every
other week. Technical one round, behavioural the next. Being watched while you code is the actual
skill being tested, and the only way to get used to it is to be watched while you code.

---

## After

- **Thank-you note within 24 hours** to each interviewer, referencing something specific from the
  conversation. Low cost, occasionally decisive between two close candidates
- **Write your notes before you check your email.** Memory decays fast
- **Follow up if the stated timeline passes** by more than a few days. One short note. Silence
  usually means an internal delay, not a rejection
- **Rejected at a late stage?** Ask for feedback, stay connected with the people you met, and put
  the company on the watchlist. "We hired someone else this time" is a real thing that happens to
  strong candidates, and those interviewers are contacts now
