# How to change this repo

This workflow is expected to be wrong in places. It was assembled from mentor conversations,
published research, and things that worked for other people — not from a controlled trial of
*your* search. The whole point of keeping it in git is that it gets corrected.

---

## Two kinds of files, two different rules

| Kind | Where | Rule |
|---|---|---|
| **Yours** | `01_Crew/members/<you>/`, your rows in `04_Trackers/*.csv`, your half of a check-in | Edit freely, commit directly, no review needed |
| **Shared** | `02_Playbooks/`, `03_Templates/`, `00_Start_Here/`, `05_Knowledge/`, `06_Tools/` | Propose it. Another crew member reviews before merge |

The split exists so nobody is ever blocked on someone else to log their own work, and nobody
wakes up to a workflow that changed overnight without discussion.

---

## Proposing a change to a shared doc

```bash
git checkout -b playbook/outreach-followup-cadence
# edit the file
git commit -m "outreach: drop follow-up interval from 7 to 5 days"
git push -u origin playbook/outreach-followup-cadence
gh pr create
```

**In the PR description, answer three questions.** This is the whole review standard:

1. **What changes?** One sentence.
2. **What made you think so?** A result you got, a source you read, or a person who told you.
   "It felt better" is a valid answer — say so explicitly rather than dressing it up.
3. **What would make us revert it?** Name the signal. If nothing would, it is a preference,
   not an improvement — which is fine, just label it.

**Review standard:** the reviewer is not a gatekeeper. Merge unless it (a) contradicts
[THE-RULES.md](00_Start_Here/THE-RULES.md) without arguing the case, (b) adds friction to
time-to-apply, or (c) makes a factual claim with no source. Default to yes. A workflow that is
hard to change stops being edited, and then stops being true.

---

## Adding a tip you got from someone

Tips are the main input to this repo. Most of what is here came from someone's advice.

- Put it in the playbook it belongs to, not in a new file
- **Attribute it** — "from a senior dev at X", "recruiter on r/cscareerquestions", "my cousin
  who hires". Anonymised is fine; unattributed is not. Six months from now you will want to
  know whether a rule came from a hiring manager or a Reddit comment
- If it contradicts something already written, do not delete the old line. Put both, and mark
  which one the crew is currently running. Contradictions are information

---

## Adding a new crew member

See [01_Crew/CREW-CHARTER.md](01_Crew/CREW-CHARTER.md) — there is an alignment bar, and it is
intentionally high. Mechanically: copy `01_Crew/members/_TEMPLATE/` to
`01_Crew/members/<name>/`, add a row to `01_Crew/ROSTER.md`, done.

---

## Commit message convention

```
area: what changed

outreach: add LinkedIn note variant for alumni
tools: fix fresh_jobs.py timezone handling on Windows
crew: log week 2026-W35 check-in
templates: shorten cold email para 2
```

Areas: `outreach`, `apply`, `resume`, `interview`, `linkedin`, `events`, `tools`, `crew`,
`meta`, `templates`, `knowledge`.

---

## What does not belong in this repo

- **Anyone's private contact details.** Names of people you are reaching out to, their emails,
  their phone numbers. Track those in your own private notes. The repo may end up public, and
  a public list of "people I am cold-emailing" is a problem for them, not just for you.
  In `outreach.csv`, use a role + company + initials, never a full name and address.
- **Full resumes with home address and phone number.** Keep a redacted version if you want
  crew review, or share the real one directly.
- **Credentials.** API keys go in `06_Tools/.env`, which is gitignored. Never in a config file
  you commit.
- **Vent posts.** Frustration is legitimate and belongs in the check-in's "where I'm struggling"
  field, which is a designed place for it. It does not belong in a playbook.
