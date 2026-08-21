# Resume and ATS

> **~75% of resumes are auto-rejected before a human sees them** — on formatting and keywords,
> not on qualifications.
>
> Fix this once, properly, and it pays out on every application for the rest of the search.
> It is the highest return-on-time work available, and it is a weekend, not a lifestyle.

---

## The two-audience problem

Your resume is read twice by two readers with opposite preferences:

| Reader | Wants | Fails you by |
|---|---|---|
| **The ATS parser** | Machine-readable structure, exact keyword matches | Silently discarding a resume it cannot parse |
| **A human, in 30-100 seconds** | Skimmable, findable, quantified | Not finding the relevant thing fast enough |

You must satisfy both. Optimizing only for the parser produces a keyword-stuffed document a human
will not read. Optimizing only for the human produces a beautiful two-column PDF the parser turns
into gibberish.

---

## Formatting rules — the 75% root causes

| Mistake | Why it fails | Fix |
|---|---|---|
| Text boxes and layers | Parser ignores their contents entirely | Flat formatting only |
| Graphics carrying information | Cannot be parsed. Skill bars convey nothing | Text only |
| **Multi-column layout** | Breaks reading order — your job titles interleave with your skills | **Single column** |
| Non-standard date formats | Parsing errors, roles dropped | Standardize on `MM/YYYY` |
| Unusual margins | Content gets clipped | 0.5-1 inch |
| Custom or decorative fonts | Renders unpredictably in the parser | Calibri, Arial, Helvetica, Georgia |
| Headers and footers | Often ignored entirely | Never put contact details there |
| Tables for layout | Reading order breaks | Plain paragraphs and bullets |
| Non-standard section names | "My Journey" is not recognised | `Experience`, `Education`, `Skills`, `Projects` |

**Base template:** Jake's Resume (the widely-used LaTeX template) or any clean single-column
format. Do not design your own.

**File format:** submit what the portal asks for. When it does not specify, PDF is generally safe
for modern systems; some older ATS parse `.docx` more reliably. If a posting explicitly says Word,
send Word.

**One page** for under ~10 years of experience. Two is acceptable for genuinely deep experience.
Not three.

---

## Keyword rules

- **Exact phrases matter.** Many systems match literally: "Adobe Creative Cloud" does not match
  "Adobe Creative Suite". **Copy the phrasing from the job description verbatim.**
- **Placement is weighted.** A keyword near the top — summary, current role — carries roughly
  **3-5x** the weight of the same word buried in a role from four years ago
- **Modern systems do some NLP** — "JS" often resolves to "JavaScript". Do not rely on it
- **Keywords must appear in experience and project bullets**, not only in the skills section.
  The skills list gets you past the parser; the bullets are what convince the human
- **The skills section can be broad.** No need to be conservative there — list everything you can
  honestly discuss

**Never** use white text, hidden keyword blocks, or invisible stuffing. Modern parsers extract
raw text and flag it, recruiters see it, and it ends the application.

---

## Content rules

**Quantify every bullet.** The formula:

> **Achieved [A] by [B%] by doing [C] in [D]**

> "Cut model inference time 40% by replacing the preprocessing pipeline with a batched
> GPU implementation, across a 12-camera deployment."

A fair estimate beats no number. "Improved performance" is invisible; "cut latency ~40%" is not.

**Write for a reader with no expertise in your specialization.** A recruiter screening a deep
learning role may not know that TensorFlow is a deep learning library. **If the JD says "Python",
your bullet says "Python"** — do not make anyone infer it from "PyTorch".

**Density is a liability.** Ten projects and a wall of text means the parser finds "Python" and
the human cannot find *where* you used it or *why it mattered*. Cut to what is relevant to this
role.

---

## The tailoring pass — 10 minutes, not an hour

Per application. Any longer and [Rule 4](../00_Start_Here/THE-RULES.md) says you are losing more
to delay than you gain in fit.

1. **Read the JD, extract the must-haves.** Usually 5-8 real requirements under the boilerplate
2. **Check your top third.** Do the JD's top three terms appear in your summary and most recent
   role? If not, rewrite those lines
3. **Reorder bullets** so the most JD-relevant one is first in each role. Reordering costs
   seconds and changes what a skimmer sees
4. **Swap the projects.** Feature the 2-3 closest to this role, drop the rest
5. **Mirror their vocabulary.** They say "distributed systems", you say "distributed systems",
   not "large-scale backend"

**Maintain a master resume** with every bullet, every project, every metric you have ever had —
longer than any resume you would send. Each application is a *deletion and reorder* from the
master, never a rewrite from scratch. This is what makes 10-minute tailoring possible.

---

## Verify it

**Once, when you build it:**

- **Copy-paste test** — open your PDF, select all, paste into a plain text editor. What you see
  is roughly what the parser sees. Scrambled order, missing sections, or interleaved columns mean
  you have a formatting problem, and this test catches most of them in thirty seconds
- **Run 2-3 scanners** and target **75%+ match** on a representative JD. Jobscan, ATSFriendly,
  Enhancv, and ResyMatch all have free tiers
- **Have a crew member read it for 30 seconds** and then tell you what you do and what your
  strongest achievement is. If they cannot, a recruiter will not either. This is the single most
  useful review available and it costs one minute

**Monthly:** rebuild the master, re-run one scanner, fold in the last month's work.

---

## Cover letters

**Default: skip them.** They cost 20-30 minutes and slow your application rate, and
[speed matters more](02-EARLY-APPLICATION-SYSTEM.md).

**Write one when:**

- The posting requires it
- It is a Tier A company and you have something genuinely specific to say — about their product,
  a problem they have written about, a real connection to the work
- You have a referral and the letter can name them

**When you write one:** 350-400 words. Address a named person if you can find one. Reference
something specific about the company that is not on their homepage. Echo the JD's language. Lead
with a quantified achievement.

There is counter-evidence worth knowing: personalized cover letters show around **15% higher
response rates**, and personalization plus targeting correlates with substantially faster
searches. The reconciliation is not "write more letters" — it is **template plus 5 minutes of
real personalization**, not 25 minutes from a blank page. Keep three tuned variants and adapt one.

---

## A note on automated screening bias

Resume-screening AI carries documented bias. Studies have found white-sounding names receiving
substantially more callbacks than identical resumes with African-American-sounding names, and
male-associated names statistically favoured. The cause is training data that encodes existing
societal bias.

Two reasons this is in a job-search playbook:

1. **If your search is going badly, it is not necessarily you.** Some of the filtering is
   structural and has nothing to do with your qualifications. That is worth knowing on a bad week,
   and it is worth saying out loud in a crew check-in
2. **It is another argument for the outreach-first rule.** A human who has spoken to you is not
   running a biased classifier over your name. Referrals route around the filter entirely

If you build any scoring tooling on top of this repo: make it explainable, show *why* a score is
what it is, and prefer auditable open-source parsers over black-box scoring.

---

## Sources

Reddit r/EngineeringResumes and its wiki is the strongest single free resource for resume
formatting and tailoring — the wiki alone is worth an hour. Jobscan's ATS formatting guides and
Cultivated Culture's scanner roundups cover the parser mechanics. Bias findings: Brookings on
gender and race bias in AI, and the FAIRE bias-auditing work on arXiv.
