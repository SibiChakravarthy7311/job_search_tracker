# The Weekly Operating Rhythm

> The master workflow. Everything else in `02_Playbooks/` is a zoom-in on one block of this page.
>
> The goal is that on any given day you do not decide what to do. You open this file, see what
> day it is, and execute. **Mechanical, not emotional** — you should be able to run a good week
> on a bad mood.

---

## The shape of the week

```
MON   Sweep (15m)  ·  Apply (45m)  ·  Outreach block (45m)  ·  Prep (60m)
TUE   Sweep (15m)  ·  Apply (45m)  ·  OUTREACH PRIME 10-11am  ·  Prep (60m)
WED   Sweep (15m)  ·  Apply (45m)  ·  Follow-ups (30m)  ·  LinkedIn post (30m)
THU   Sweep (15m)  ·  Apply (45m)  ·  OUTREACH PRIME 10-11am  ·  Prep (60m)
FRI   Sweep (15m)  ·  Apply (45m)  ·  Coffee chats  ·  Engage (20m)
SAT   Deep work: project, portfolio, or interview prep. Events.
SUN   Log the week (20m)  ·  Plan next week (10m)  ·  CHECK-IN (30m)
```

Roughly **2.5 hours a day on weekdays**. Scale it to what you actually have — a person working
full time might run half of this and be fine, as long as the sweep and the outreach block survive
the cut. Those two are the engine. Everything else is amplification.

---

## Daily: the sweep — 15 minutes, first thing

**Non-negotiable, weekdays.** [Full playbook](02-EARLY-APPLICATION-SYSTEM.md).

1. Run `python 06_Tools/fresh_jobs.py` (or the manual filters if you have not set it up).
2. Scan for anything posted in the **last 24 hours**.
3. Triage into three buckets: **apply today** / **needs outreach first** / **skip**.
4. Anything from a target company jumps the queue regardless of everything else.

Fifteen minutes, before email, before anything. The whole 5x timing advantage lives in this block
and it is worthless done on Thursday for Monday's postings.

---

## Daily: the application block — 45 minutes

[Full playbook](09-APPLICATION-PROCESS.md).

For each posting in the "apply today" bucket:

1. **Check the outreach rule.** Target company? Someone must be contacted there first. If nobody
   has been, send the message *now* — then apply. Do not wait for a reply
   ([Rule 1](../00_Start_Here/THE-RULES.md)).
2. **Tailor the keywords.** 10 minutes maximum. Pull exact phrases from the JD into your
   experience and project bullets. Not a rewrite — a keyword pass
   ([resume playbook](08-RESUME-AND-ATS.md)).
3. **Submit.**
4. **Log it** in `04_Trackers/applications.csv`, including hours since posting.

Speed is the point. Three applications submitted beats one perfected
([Rule 4](../00_Start_Here/THE-RULES.md)).

---

## Tue / Thu 10:00–11:00 — outreach prime time

**The most important hour in the week.** [Full playbook](03-OUTREACH-PLAYBOOK.md).

Tuesday and Thursday, mid-morning, is when professional email and LinkedIn messages get read.
Send at a **random minute** — 10:24, not 10:00 — so it does not look scheduled.

Each block:

- **3–5 new contacts** at target companies. One step above your level is the sweet spot: senior
  enough to know about hiring, close enough to remember being where you are.
- LinkedIn connection request **with a note**, or email if you can resolve the address.
- Log every one in `04_Trackers/outreach.csv` at send time.

The messages should be pre-drafted before the block starts — Monday evening is a good time.
The block itself is for sending, not composing. Composing during the block is how the block
becomes twenty minutes of staring at a blank message box.

**Prepare on Monday:** who, at what company, which template, what the personalised line is.

---

## Wednesday — follow-ups + the post

**Follow-ups (30 min).** Filter `outreach.csv` for anything sent 7+ days ago with no reply.
Send follow-up 1. Anything at 14 days gets follow-up 2. Anything past that gets marked `cold`
([Rule 7](../00_Start_Here/THE-RULES.md) — two follow-ups, then stop).

Most replies come from a follow-up, not the first message. This block routinely outperforms the
new-contact block, and it is the one people skip.

**LinkedIn post (30 min).** One per week, minimum. [Full playbook](04-LINKEDIN-VISIBILITY-ROUTINE.md).
Progress, a project, something you learned, a certification, a take. It does not need to be good.
It needs to exist, so that when a recruiter at a target company sees your name in an applicant
list, it is the second or third time they have seen it.

---

## Friday — chats and engagement

**Coffee chats.** Schedule them here when you can — people are more relaxed and more likely to say
yes to a Friday 20-minute call than a Monday one. [Full playbook](05-COFFEE-CHAT-PLAYBOOK.md).

**Engagement (20 min).** Comment on posts from your target companies and the people you have
contacted. Substantive comments, not "Great post!". This is what makes the connection request you
send next month land warm instead of cold.

---

## Saturday — deep work

Whichever of these is currently the bottleneck:

- **Interview prep** — algorithms, system design, behavioural stories
- **The portfolio project** — built in the stack your target JDs keep asking for
- **Events** — most meetups and conferences are weekends. [Playbook](06-NETWORKING-EVENTS.md)
- **The monthly resume rebuild** — once a month, not weekly

---

## Sunday — close the week

**Log (20 min).** Fill in your half of `Weekly_Checkins/2026-W__.md`. Actual numbers from the
trackers, not from memory. Memory inflates outreach and deflates applications, reliably.

**Plan (10 min).** Next week's numbers in your `GOALS.md`. Draft Tuesday's outreach list so
Tuesday morning is pure execution.

**Check-in (30 min).** With the crew. [Protocol](../01_Crew/ACCOUNTABILITY-PROTOCOL.md).

---

## Monthly

| What | Why |
|---|---|
| **Review the target list** | Companies get dropped, the watchlist promotes. [Playbook](01-TARGET-COMPANY-LIST.md) |
| **Rebuild the master resume** | Fold in the last month's work. Re-run the ATS check |
| **Retro with the crew** | What converted, what produced nothing in four weeks, what changes in the repo |
| **Skill-demand pass** | What keywords keep appearing in JDs you cannot claim yet? That is next month's learning |

---

## When the week collapses

It will. A deadline lands, you get sick, a rejection knocks you sideways for three days.

**The minimum viable week** — if you can only do one thing:

> **The Tuesday outreach block.** Three messages. Twenty minutes.

Not applications. Outreach — because applications you skipped are replaceable (there will be more
postings next week) and relationships you did not start are not. A conversation started today is
a referral available in six weeks. An application you did not send this week is an application
you send next week.

Log the collapsed week honestly. A week of 3 outreach and 0 applications, logged, is a real data
point. A blank week teaches nobody anything.
