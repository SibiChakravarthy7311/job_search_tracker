# Accountability Protocol

> The weekly loop. Thirty minutes, same slot every week, written before spoken.

---

## The cadence

| When | What | How long |
|---|---|---|
| **Sunday (or your week-end day)** | Each person writes their half of the check-in file | 10 min, solo |
| **Sunday/Monday** | Read the other person's half **before** the call | 5 min |
| **The call** | Talk through it — the format below | 30 min |
| **Immediately after** | Each person sets next week's numbers in their `GOALS.md` | 5 min |

Written first, then spoken. If you talk first, the conversation becomes a summary of feelings
about the week. If you write first, the conversation starts from what actually happened.

---

## The file

One file per week in [../Weekly_Checkins/](../Weekly_Checkins/), named `2026-W35.md` (ISO week
number). Copy [../03_Templates/weekly-checkin.md](../03_Templates/weekly-checkin.md).

Both people edit the same file, in their own section. Commit it. The history *is* the record —
in three months you can run `git log Weekly_Checkins/` and see exactly what the search looked
like, which is worth more than any dashboard.

---

## The 30 minutes

| Minutes | Segment | What happens |
|---|---|---|
| 0–5 | **Numbers** | Read the scoreboard out loud. Hit or missed, no elaboration yet. |
| 5–15 | **Person A** | What worked, what did not, where they are stuck. B asks questions. |
| 15–25 | **Person B** | Same, reversed. |
| 25–30 | **Next week** | Each states their numbers and their one commitment for the week. |

**The numbers segment comes first on purpose.** It is very easy to spend thirty minutes on how
the week *felt* and never look at what was done. Reading the scoreboard first anchors everything
after it in fact.

---

## The five questions

Every check-in answers these. They are in the template.

1. **What did I commit to, and what did I actually do?** Numbers.
2. **What worked?** Something to keep. A message that got a reply, a source that had fresh
   postings, a question that opened up a coffee chat.
3. **What did not work?** Something to stop or change. Be specific — "outreach didn't work" is
   not usable; "eight LinkedIn notes, zero replies, all to senior managers" is a hypothesis.
4. **Where am I stuck?** The one thing the other person could actually help with this week.
5. **What am I committing to next week?** Numbers plus one specific non-numeric thing.

---

## Calling it out

This is the function the crew exists for and the one people avoid. So it has a script.

**When someone misses their floor once:** ask what got in the way. Once is noise — a bad week,
a deadline, illness.

**When someone misses the same floor twice in a row:** say it plainly.

> "That is two weeks under on outreach. I am not asking you to feel bad about it — I want to
> know which of these it is: the number is wrong, something is blocking you, or you have stopped
> believing this part matters."

Those three are the whole diagnostic tree, and each has a different fix:

| Diagnosis | Fix |
|---|---|
| **The number is wrong** | Lower it. A floor you miss every week is not a floor, it is a source of guilt. Halve it and hit it. |
| **Something is blocking you** | Name the block and attack *that*. Usually it is not the outreach — it is not knowing who to contact, or dreading the blank message. Both are solvable in twenty minutes together. |
| **You stopped believing it matters** | The most important one to surface. Go back to [WHY-THIS-WORKS.md](../05_Knowledge/WHY-THIS-WORKS.md), or argue the rule down and change it in the repo. Do not leave a rule standing that nobody intends to follow. |

**When someone misses two check-ins in a row:** that is the real alarm, more than any metric.
Message directly, not in the group. Ask whether they are pausing, leaving, or struggling. All
three are acceptable answers; silence is the failure mode.

---

## Receiving it

You asked for this. When the callout comes:

- Do not explain for more than two sentences. The explanation is usually true *and* not the point.
- Do not counter-attack with their numbers. Their week is their segment.
- Answer the three-way diagnostic honestly. "I stopped believing it matters" is a legitimate and
  useful answer, and it is far better than pretending you will do better next week.
- Then change one thing. One. Not five.

---

## Monthly retro

The last check-in of each month, add fifteen minutes and answer three things together:

1. **What is converting?** Look at the trackers, not memory. Which source produced replies?
   Which message variant? Which company tier? Applications-to-screen rate, outreach-to-reply rate.
2. **What are we doing that produced nothing in four weeks?** Kill it or fix it. Four weeks of a
   channel with zero output is enough evidence.
3. **What should change in the repo?** Open the PRs during the retro, not "later".

Log it in [../07_Meta/RETROSPECTIVES.md](../07_Meta/RETROSPECTIVES.md).

---

## When one person lands a job

The crew does not dissolve. It rebalances:

- The landed member moves into the **expertise seat**. Their check-in half becomes shorter — what
  they are seeing from the inside, who they can now introduce, what the interview loop actually
  looked like.
- They keep showing up for the accountability function for at least a month. Their information
  is at peak value in the first weeks, and the person still searching needs the signal that
  landing is possible more at that moment than at any other.
- **A referral from inside is now on the table.** That is the single most valuable thing a crew
  can produce, and it is the reason the alignment bar in the charter is set where it is.
