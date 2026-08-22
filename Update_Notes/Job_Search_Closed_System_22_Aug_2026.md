# Job Search Operating System

A closed-loop process: **Discover → Apply → Reach → Follow up → Review.** Nothing exits the loop until it hits a definite rejection or an offer.

Treat it as a full-time job. Everything below is designed to be run from one tracker and a calendar.

---

## 0. Set up today (2–3 hours, one time)

| # | Task | Output |
|---|---|---|
| 1 | Build the tracker (Section 6) | One spreadsheet, 5 tabs |
| 2 | Write the target company list | 25–40 companies, tiered |
| 3 | Lock the master resume + 3 role variants | Base files to tailor from |
| 4 | Rewrite LinkedIn headline + About | Positioned for target role |
| 5 | Write the **source registry** — where jobs actually get posted (Section 1) | One list, every source named, with its URL and how it notifies |
| 6 | Turn on every alert those sources offer | Alerts land in one inbox folder |
| 7 | Block the weekly calendar (Section 5) | Recurring events, not to-dos |

One task that is **not** for today: building the watcher (Section 1, Step 2). That is a first-weekend
build, and it only works if the source registry exists first.

### Target company list — tiering

- **Tier 1 (Dream, 8–10):** you'd take almost any relevant role. Relationship-building starts here immediately, before any job exists.
- **Tier 2 (Strong fit, 12–20):** apply on posting, outreach on posting.
- **Tier 3 (Volume, open-ended):** apply if the role fits; outreach only if a warm contact exists.

Build the list on **field**, not just geography: computer vision, applied ML/AI research, agri-tech and precision agriculture, biotech/health imaging, robotics, plus the ML teams at banks, telecoms, and consultancies with Halifax/Atlantic or remote-Canada presence.

Each week, add 3–5 new companies. The list is never finished.

---

## 1. Discover — find postings within hours, not weeks

Speed from posting to submission is the second-biggest lever in this whole system. Do this in two
steps, in this order: **name the sources, then automate the watching of them.**

### Step 1 — Build the source registry (once, today)

Before anything is automated, write down every place a relevant job actually appears. One row per
source. A source that is not on this list does not exist as far as the system is concerned.

| Field | What goes in it |
|---|---|
| Source | Name of the board, company, or feed |
| Type | Career page / ATS board / aggregator / alert email / research board / person's feed |
| URL | The exact page or feed, not the homepage |
| How it notifies | RSS, API, email alert, or "poll the page" |
| Check frequency | Hourly / daily / weekly |
| Owner | Who on the crew maintains it |

Sources to cover:

- **Tier 1 company career pages** — they post there before aggregators index them. Find the underlying ATS board (Greenhouse, Lever, Workday, Ashby, BambooHR); those usually have a clean, stable JSON or RSS endpoint behind the pretty page.
- **LinkedIn job alerts** — one saved alert per role keyword × per location setting, notifications ON, set to daily. Delivered as email into a dedicated inbox folder. **Alerts, not scraping** — see the guardrails below.
- **Aggregators:** Indeed, Glassdoor, Google Jobs, Otta/Welcome to the Jungle, Wellfound (startups).
- **AI/ML-specific boards** and Canadian academic/research boards for research-scientist roles.
- **University and government research postings** if research roles are in scope.
- **People you follow at target companies** — teams often post openings personally before HR does. This one stays manual; it is a feed to read, not a feed to parse.

### Step 2 — Build the watcher (first weekend)

The point of the watcher is one number: **minutes between the posting going live and you knowing about it.**
Everything else is secondary.

What it has to do:

1. **Poll every source in the registry on its own schedule** — hourly for Tier 1 ATS boards and RSS feeds, daily for the rest.
2. **Dedupe** against everything seen before (job ID, or a hash of company + title + URL) so a re-index does not re-alert you.
3. **Filter** on the rules below before it interrupts you. A watcher that cries wolf gets muted within a week.
4. **Alert immediately** on a new match — push notification, phone or desktop, not a daily email. A daily digest defeats the purpose for Tier 1; keep the digest for Tier 3 volume.
5. **Write the row for you** — company, role, URL, posted date, and *first-seen timestamp* straight into the Applications tab with status `Found`.
6. **Track time-to-apply** — first-seen to submitted. That is the metric the Friday review reads.

`06_Tools/fresh_jobs.py` is the seed for this: it already does the recency sweep, ghost-job flagging, and
the morning digest. The work is turning it from a thing you run into a thing that runs itself and taps you
on the shoulder — a scheduler (cron / Task Scheduler / a small always-on box), per-source adapters, and a
push channel.

**Guardrails on the build:**

- **Never scrape LinkedIn.** It is a ToS violation, and a restricted account mid-search is a serious loss. Use their native job alerts into a filtered inbox folder, and parse *your own* inbox if you want them machine-readable.
- **Official feeds and public endpoints only** — RSS, JSON, published APIs. If a source has no feed, poll the public page politely (a few times an hour, real user agent), or leave it manual.
- **The watcher surfaces; you decide.** It never applies, never sends anything, never writes an email.
- **Timebox it.** If the build is eating application hours, the build is losing. Ship a version that watches three Tier 1 boards and alerts you, then extend it a source at a time.

### Filter rules

**Daily, 30 minutes (morning block)** to work the queue the watcher produced. A posting enters the tracker only if it passes all three:

1. Role maps to your skill stack (CV/ML/data engineering/research).
2. You meet ~60%+ of listed requirements. Do not self-reject below 100%.
3. Work authorization is compatible — flag anything requiring clearance or citizenship and drop it.

**Log the posting date.** Applications submitted in the first 48 hours get disproportionately more attention. Posting date is a tracked field, and anything older than ~2 weeks moves to low priority unless you have an inside contact.

---

## 2. Apply — same day where possible

For every posting that passes the filter:

1. **Tailor the resume.** Pull keywords from the job description, mirror their exact phrasing (not synonyms), reorder bullets so the most relevant work is top of section. Every bullet carries measurable impact — a number, a percentage, a scale, a time saved.
2. **Run the ATS check.** Use a Chrome extension (Jobscan, Teal, or similar) to score resume-vs-JD. Set a floor — don't submit below ~75% match. Log the score.
3. **Write the cover letter to a person, not a department.** Named hiring manager or team lead, one page, three paragraphs: why this role specifically, the two most relevant things you've built, the ask for a conversation.
4. **Submit.** Save the confirmation and the job ID.
5. **Immediately trigger the outreach sequence** (Section 3). The application and the outreach are one action, not two.

At 3–5 applications a day (Section 5), tailoring has to get faster without getting generic. That means the
role variants locked up front and a snippet library of pre-written, already-measured bullets you assemble
from — not a blank page every time.

**Why the outreach matters:** the ATS is a filter you may never clear. The point of contacting the team directly is that a human on the team sees the resume, and if they think you fit, they tell the hiring manager to pull you in. The application makes you legitimate; the outreach makes you visible.

---

## 3. Reach — people, not portals

### Who to contact (in priority order)

1. **Anyone you already have a real link to** — a friend working there, a former classmate, a labmate, someone who took the same course or worked with the same professor. The closest link wins, every time.
2. **Alumni from your university** at the company — the highest reply rate of the cold contacts, and the easiest opening line.
3. People in the exact target role or team.
4. People one or two levels above the target role.
5. The hiring manager.
6. Recruiters — last, not first.

**Three people per company, three different teams.** Do not send the same email to three people on one team.

### Who to pick — stack the signals

Reply rate is not a volume problem, it is a question of how many true things you can say in the first two
lines. Score each candidate against the signals below. **Three or more, and you should almost always write.**

| Signal | Why it moves the needle |
|---|---|
| **Alumni from your university** | Strongest single signal. Shared campus, shared professors, shared complaints about the same building |
| **A close link** | A friend already at the company, a classmate, a labmate, a shared supervisor, the same city |
| **Same field** — Computer Science / ML / CV | They read your work in their own vocabulary instead of translating it |
| **Same target role or team** | They know what the job actually needs, and their opinion carries weight with the hiring manager |
| **Named in, or next to, the JD's team** | A direct line to the req you are applying for |
| **Same location** as the role | Coffee becomes possible, and coffee is the whole ask |
| **Reads as down-to-earth and helpful** | Replies to comments, answers beginners' questions, mentors, TAs, maintains open source, "happy to help" energy in their posts. The most under-used filter available |
| **A shared interest outside work** | Sport, hometown, music, a paper you both cite. Turns a cold email into a conversation |

The ranking that falls out of it: *alum in the target role* > *alum anywhere at the company* >
*close link inside the target team* > *target role or team with no link* > *hiring manager* > *recruiter*.

Skip people with zero signals no matter how senior they are. A perfect-title stranger replies less often
than a junior engineer who went to your school and answers every question in their comments.

### Finding them

- LinkedIn search: company + role keywords + your university as the school filter. Filter on location and on the team named in the job description too.
- Email via **Apollo** (or Hunter/Clearbit as backup). Verify the pattern against a known company address before sending.
- Before writing, scan their LinkedIn activity, posts, and any public work for one specific hook — a paper, a talk, a project, a shared course or professor.

### Send the LinkedIn connection request too

Yes — and usually **without a note**. The email carries the message; the request just puts your name and
face in their notifications the same week. Add a note only when there is no email and the request is the
whole approach.

### The cold email — four things, nothing more

1. **Who you are** — one line: your university plus what you actually do ("<university> alum, AI researcher"). That is the opening.
2. **Why them specifically** — the hook, built from the signals above. This is the part that gets replies.
3. **The ask** — 15 minutes.
4. **Availability** — two concrete options, then flexibility.

> Would Wednesday or Friday around noon work? Happy to work around your schedule.

Give them easy options. Don't make them think. Keep it under ~150 words.

**Attach the resume.** It costs them nothing to ignore, and it saves a round-trip when they are interested.
One page, the tailored version, sensibly named.

### Cadence per company

| Email | Recipient | Timing |
|---|---|---|
| E1 | Person A (Team 1) | Day 0 |
| E2 | Person B (Team 2) | Day 3 |
| E3 | Person C (Team 3) | Day 7 |
| Follow-up on E1 | Person A | Day 14 |

**Hard cap: three emails to any one person.** That holds for application-driven outreach and relationship
contacts alike. After the third, they move to the light-touch list (Section 4) — comments, shared work, a
note when you ship something — not the email queue.

---

## 4. Coffee chats — relationship before requirement

The core principle: **build the relationship before the job exists.** When a role opens at a company where you've already had a real conversation, you're not a cold applicant asking for a favour — you're someone they know who happens to be a strong fit.

Run these against Tier 1 companies continuously, whether or not they're hiring.

**Target: 3 coffee chats a week.**

Run each chat off the Coffee Chat Playbook (separate document). The two outcomes to land every time:
1. A connection to someone else relevant.
2. A referral, or agreement to pass your name along.

**After every chat, within 24 hours:**
- Thank-you note, plus any questions you didn't get to ask.
- Log notes, personal details, and their advice in the People tab.
- Set the next touch date — 4–6 weeks out.
- Send any promised material (paper, project link, resume).

**Ongoing touches** for people you've already spoken to: comment on their posts, share a relevant paper, send a short update when you ship something. Two or three light touches between conversations keeps you present without asking for anything.

---

## 5. The weekly rhythm

Put these on the calendar as recurring events.

| Block | When | Duration | Work |
|---|---|---|---|
| Discovery | Daily, morning | 30 min | Work the watcher's queue, log new postings |
| Applications | Daily | 2–3 hrs | Tailor + submit + trigger outreach |
| Outreach | Daily | 45 min | New emails, connection requests, Apollo lookups |
| Follow-up queue | Daily | 20 min | Clear everything due today |
| Coffee chats | Tue/Wed/Thu | As booked | The chats themselves + notes |
| LinkedIn presence | Daily 10 min + Thu 30 min | — | Likes and comments daily; the week's post on Thursday |
| Weekly review | Friday | 45 min | Metrics, new companies, next week's targets |
| Skill work | Daily | 60–90 min | Certification, project, gaps in the JD requirements |

**Weekly targets (adjust after two weeks of real data):**

- **3–5 tailored applications per day — 15–25 a week**
- 12–15 new people contacted
- 3 coffee chats held
- 1 LinkedIn post (or 1 post + 1 repost) / 10+ meaningful comments
- On the two-week clock: 1 certification finished, **or** a project/presentation shipped each week
- 5 new companies added to the list
- 100% of the follow-up queue cleared

If the application number cannot be hit without quality dropping, the bottleneck is the tailoring workflow,
not the target. Fix the workflow.

---

## 6. The tracker

One spreadsheet. Five tabs. Build this today.

### Tab 1 — Companies
`Company | Tier | Field | Location | Careers URL | Contacts logged (n) | Coffee chats held (n) | Roles applied (n) | Status | Notes`

### Tab 2 — Applications
`Job ID | Company | Role | Link | Posted date | First seen (watcher) | Applied date | Hours-to-apply | Resume version | ATS score | Cover letter addressed to | Outreach triggered? | Status | Next action | Next action date`

Status values: `Found → Applied → Outreach sent → Response → Screen → Interview → Offer / Rejected / Ghosted-closed`

### Tab 3 — People
`Name | Company | Team | Title | Same school? | Link type (friend/classmate/lab/none) | Signals | LinkedIn | Email | Email source | Hook | Connection sent | E1 date | E1 reply | E2 date | E2 reply | E3 date | E3 reply | Relationship tier | Next touch date | Notes`

Relationship tiers: `Cold → Contacted → Replied → Chatted → Advocate`

### Tab 4 — Coffee chats
`Date | Person | Company | Prep done? | Questions asked | Their advice | Ask 1 (connection) made? | Ask 2 (referral) made? | Thank-you sent | Outcome | Next touch date`

### Tab 5 — Weekly metrics
`Week | Applications | New contacts | Reply rate | Chats held | Referrals secured | Screens | Interviews | Median hours-to-apply | Notes on what changed`

**The follow-up engine is a formula, not memory.** Filter every tab on `Next action date <= TODAY()`. That filtered view *is* your daily follow-up queue. If it's empty, you're behind on outreach, not ahead on follow-ups.

---

## 7. Visibility — be findable before you're needed

**Ship something, then post about it.** The artifact comes first; the post is the byproduct. Pick one of
these two rhythms and hold it:

- One **certification finished every two weeks**, or
- One **project or presentation shipped every week**, with a post about it.

**Post cadence: one post a week.** Not two. If there is a second slot in the week, make it a **repost with
two or three lines of your own on top** — your read on someone else's work is cheaper to produce and often
travels further than a second original post.

**The daily work is comments, not posts.** Like and comment on the people you follow, especially at target
companies — substantively, not "great post". Repeated visibility is what makes them recognize your name when
your application lands. 10+ meaningful comments a week is the floor.

Keep the profile aligned with the target role title, not your current title.

---

## 8. Weekly review — Friday, 45 minutes

Answer these in writing:

1. Which numbers hit target, which missed?
2. What's the reply rate on outreach? Below ~10% means the hook is weak — rewrite the template, not the volume.
3. What was the median time from first-seen to submitted? Which applications went out more than 48 hours after posting, and why?
4. Which chats produced a connection or a referral? What did those have in common?
5. Which requirement keeps appearing in JDs that you can't yet claim? That's next week's skill block.
6. Which 5 companies get added to the list?

Change **one** variable a week — the hook, the resume format, the target role, the outreach channel. Changing several at once tells you nothing about what worked.

---

## 9. Rules that hold regardless

- Follow up at least twice on every application. Nothing closes without a definite rejection.
- Three emails maximum to any one person. After that, light touches only.
- Never lead with the degree where experience is the thing being bought. Lead with what you built and what it did.
- Even unpaid work must be value-added and portfolio-worthy. Momentum comes from real work in real organizations.

---

## 10. Automation roadmap

Run the manual loop while the watcher gets built — you need real data before you automate the wrong thing.
The watcher is the one piece worth building early, because it buys hours on every application after it.

**v1 — this week (manual):** the spreadsheet, calendar blocks, the source registry, saved job alerts, email templates in a drafts folder.

**v2 — first weekend (the watcher, Section 1 Step 2):**
- Per-source adapters pulling from ATS boards, RSS, and public APIs; dedupe against the tracker.
- Scheduled runs — hourly for Tier 1, daily for the rest.
- Push alert on every new match, and the row written into the Applications tab with posted date and first-seen timestamp.

**v3 — weeks 3–4 (ranking and reminders):**
- Keyword-match score between JD text and your resume corpus — a simple TF-IDF or embedding similarity ranking to prioritize which postings to tailor for.
- Google Apps Script on the tracker: daily digest email of everything where `Next action date <= today`.

**v4 — later (assisted):**
- Contact enrichment: given a company + role, surface candidate profiles ranked by the signal stack in Section 3 — alumni and close links first.
- Hook generation: summarize a contact's recent public activity into two or three specific conversation openers.
- Auto-draft tailored resume bullets per JD for you to edit — never send unedited.

Build in that order. The tracker is the system; the scripts only make it faster.

---

## Calibration — what we're running

**Positioning.** Lead as **an alum of your university, and as what you actually build** — e.g. "<university> alum, AI researcher". That is the first line of most outreach
and the reason a stranger opens the reply box. The alumni angle is the strongest single lever in this plan,
and the whole targeting strategy in Section 3 is built on it.

**Contact limits.** Three emails per person — application outreach and relationship contacts alike. Day 0 /
Day 3 / Day 7 across three people at a company, follow-up on E1 at Day 14. Run it as written for a few
weeks; adjust once there is real reply data to adjust against.

One practical note: for cold outreach in Canada, keep emails to work addresses, tied to that person's professional role, with a clear identification of who you are and a way to opt out of further contact. That's both good manners and how CASL expects business outreach to look.
