# Trackers

> Five CSVs. Plain text in git, so they diff, merge, and open in Excel, Sheets, or pandas.
>
> Each file ships with **one example row** showing the expected format. Delete it when you start.

| File | What it holds | When you write to it |
|---|---|---|
| `applications.csv` | Every application submitted | At submit |
| `outreach.csv` | Every person contacted | **At send time** ([Rule 6](../00_Start_Here/THE-RULES.md)) |
| `target-companies.csv` | Your 10-15 and their contact status | Weekly |
| `coffee-chats.csv` | Every chat held | Within 24 hours |
| `events.csv` | Events attended and what came of them | Next morning |

---

## Privacy — read this before you log anything

**This repo may become public. Assume it will.**

- **Never log full names, email addresses, or phone numbers** of people you contact. Use
  **initials + role + company**: `P.K., Senior Backend Engineer, ExampleCorp`
- Keep the real contact details in your own private notes, your address book, or your email
  client — all of which you already have
- A public list of people being cold-emailed is a problem for *them*, not just for you

The tracker's job is pattern analysis — which seniority tier replies, which channel works, which
source produces interviews. **None of that needs a real name.**

---

## Sharing versus keeping separate

Two workable models. Pick one at the first check-in.

**Shared files (default).** Both people log into the same CSVs, distinguished by a `member`
column you add. Pros: you can compare response rates directly, which is genuinely useful. Cons:
merge conflicts if you both edit the same file at the same moment.

**Per-member files.** `applications-sam.csv`, `applications-amal.csv`. No conflicts ever. Combine
with pandas at the monthly retro. **Recommended for crews of three or more.**

If you hit a merge conflict on a CSV: both versions are usually correct and the fix is to keep
both sets of rows. That is the one merge conflict you never need to think hard about.

---

## Column notes

### applications.csv

| Column | Values / notes |
|---|---|
| `tier` | `A` / `B` / `C` from your target list, or `-` for off-list |
| `hours_since_posting` | **The important one.** Lets you verify the 24-hour rule is real for you |
| `referral` | `yes` / `no` — the column that will eventually justify the outreach-first rule to you |
| `contact_initials` | Who you contacted there before applying |
| `ghost_risk` | `low` / `med` / `high` |
| `status` | `applied` → `screen` → `technical` → `onsite` → `offer` / `rejected` / `ghosted` |

### outreach.csv

| Column | Values / notes |
|---|---|
| `seniority` | `recruiter` / `ic` / `senior-ic` / `manager` / `director+` — **response rates differ enormously; this is the highest-value column in the file** |
| `channel` | `linkedin` / `email` / `event` / `intro` / `discord` |
| `opener_type` | `alumni` / `their-work` / `shared-community` / `funding` / `event` / `cold` |
| `template_used` | Which variant, so you can compare them |
| `outcome` | `no-reply` / `replied` / `in-conversation` / `chat-held` / `referral` / `cold` |
| `days_to_reply` | Sets a realistic follow-up cadence |

### coffee-chats.csv

| Column | Values / notes |
|---|---|
| `intro_offered` / `intro_names` | Did the compounding question work? Count of people they pointed you to |
| `hiring_signal` | Anything they said about headcount |
| `next_touch_date` | **Set it every time.** 2-3 months out. This is what stops a contact going stale |
| `rating` | 1-5, your own read on how it went. Useful for spotting which openers produce good chats |

---

## What to look at monthly

Pull these at the retro. They are the questions the trackers exist to answer:

| Question | How |
|---|---|
| **Application → screen rate** | Screens ÷ applications |
| **Referred vs cold screen rate** | Split by the `referral` column. Usually the most striking number in the whole tracker |
| **Outreach reply rate by seniority** | Group `outreach.csv` by `seniority` |
| **Reply rate by opener type** | Group by `opener_type` — tells you which template is doing the work |
| **Reply rate by channel** | LinkedIn note vs email |
| **% of applications inside 24h** | Whether the 5x lever is actually being pulled |
| **Chats → referrals** | The conversion the whole networking effort is aiming at |
| **Which sources produce interviews** | Not which produce *postings* — which produce interviews |

A one-line pandas start:

```python
import pandas as pd
o = pd.read_csv("outreach.csv")
print(o.groupby("seniority")["replied"].value_counts(normalize=True))
print(o.groupby("opener_type")["replied"].value_counts(normalize=True))
```

---

## Sample size warning

**Do not draw conclusions before ~30 outreach contacts and ~30 applications.** Below that you are
reading noise, and the most common failure is abandoning a working channel after eight tries.

Six weeks of consistent logging is roughly the point where the numbers start meaning something.
Until then, track the *inputs* — sends, applications, chats — because those are what you control.
