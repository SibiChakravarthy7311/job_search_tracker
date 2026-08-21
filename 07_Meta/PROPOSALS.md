# Proposals

> Ideas for changing the workflow that are not ready to be a PR yet — because they need
> discussion, data, or somebody to try them first.
>
> A proposal that sits here for two months with nobody willing to test it should be deleted.
> An idea nobody will try is not a backlog item, it is clutter.

---

## Format

```markdown
### [Title]

**Proposed by:** · **Date:** · **Status:** open / testing / adopted / rejected

**What:** One or two sentences.

**Why:** What made you think of it — a result, a source, a person. "It feels better" is a valid
answer; say so explicitly rather than dressing it up.

**How we would test it:** What would we measure, over how long?

**What would make us reject it:** Name the signal.
```

---

## Open

### Example — split-test two cold email openers

**Proposed by:** — · **Date:** — · **Status:** open

**What:** Run the alumni opener and the their-work opener on alternate sends for four weeks, then
compare reply rates in `outreach.csv` grouped by `opener_type`.

**Why:** We are guessing about which one works. The tracker already has the column for it, so the
test costs nothing beyond remembering to alternate.

**How we would test it:** 40 contacts, 20 each, four weeks. Compare reply rate by `opener_type`.

**What would make us reject it:** if the sample stays under 30 by week four, the result is not
worth acting on and we keep using whichever one feels better.

---

## Adopted

<!-- Moved here when merged, with a link to the PR. -->

## Rejected

<!-- Kept, with the reason. Stops the same idea coming back every three months. -->
