# Weekly Check-Ins

One file per week, named by ISO week: `2026-W35.md`.

**At the start of each week:**

```bash
cp 03_Templates/weekly-checkin.md Weekly_Checkins/2026-W__.md
```

Both members fill in their own section **before** the call. Both read the other's section
**before** the call. Then talk. Protocol:
[../01_Crew/ACCOUNTABILITY-PROTOCOL.md](../01_Crew/ACCOUNTABILITY-PROTOCOL.md).

---

## Why this is a file and not a chat message

Chat disappears. This does not.

In three months `git log Weekly_Checkins/` shows exactly what the search looked like — what was
committed to, what was done, where things stalled and for how long. That record is worth more
than any dashboard, and on a bad week it is proof that the work happened even though the results
have not arrived yet.

It also makes patterns visible that neither of you would notice week to week. Three consecutive
weeks of "stuck on outreach" reads very differently in a list than it does in three separate
conversations.

---

## Finding the ISO week number

```bash
date +%G-W%V          # bash / Git Bash
```

```powershell
Get-Date -UFormat "%Y-W%V"
```

Or just count from the start of the year — nobody is checking.
