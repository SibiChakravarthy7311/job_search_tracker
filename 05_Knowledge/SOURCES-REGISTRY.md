# Sources Registry

> Where to find postings, market intelligence, salary data, and people.
>
> **Review monthly.** Sources go stale, pricing changes, APIs get deprecated. A source that has
> produced nothing in three weeks comes out of your daily sweep.
>
> Costs are indicative and change — verify before relying on them.

---

## A. Job posting sources

### Tier 1 — the daily sweep

| Source | Access | Cost | Notes |
|---|---|---|---|
| **Indeed** | API / site filters | Free | Highest raw volume in most markets |
| **LinkedIn Jobs** | Site, "Past 24 hours" filter | Free | Largest professional posting base. **Do not scrape it** — see ethics below. Use JobSpy, which reads it through supported paths |
| **JobSpy** (open source) | Python library | Free | Aggregates LinkedIn, Indeed, Glassdoor, ZipRecruiter, Google Jobs in one call. What [fresh_jobs.py](../06_Tools/) is built on |
| **Target company career pages** | Per company | Free | **Check these directly.** Aggregators miss postings and run hours behind. This is why the target list exists |

### Tier 2 — high value, lower volume

| Source | Access | Cost | Notes |
|---|---|---|---|
| **Community Discord / Slack servers** | Manual or bot | Free | Field-specific servers often post roles before the boards. Find the ones for your niche |
| **University career portals** | Manual | Free | Co-op, internship, new-grad. Much lower competition |
| **Regional tech associations** | Portal / newsletter | Free-small | Local roles, far less competition than national boards |
| **GitHub posting repos** | Scrape / RSS | Free | Community-maintained new-grad and internship lists, usually seasonal |
| **Wellfound (AngelList)** | Site | Free | Startups. Direct founder contact is common |
| **Hacker News "Who is Hiring"** | Monthly thread | Free | First of each month. High-signal, low-noise, and applications go straight to a human |
| **Stack Overflow Jobs** | API | ~$4/mo | Developer-specific where still available in your market |

### Premium — only if aggregation is eating your time

| Source | Cost | Notes |
|---|---|---|
| **TheirStack** | $25-100/mo | Aggregates a very large number of sources. Consider only if building your own sweep proves genuinely too costly |

---

## B. Market intelligence

| Source | What it gives | Quality | Notes |
|---|---|---|---|
| **r/cscareerquestions** | Trends, market temperature | High | Noisy and doom-heavy. Calibrate accordingly |
| **r/EngineeringResumes** + wiki | Resume formatting and tailoring | High | **The single strongest free resume resource.** The wiki alone is worth an hour |
| **Company-specific subreddits** | Insider hiring signals, comp | High | Interview loops, timelines, team gossip |
| **Hacker News** (Show HN, Who's Hiring, YC) | Emerging skills, funding signals | High | Easy to read, plain HTML |
| **Crunchbase** | Series A/B/C funding alerts | High | Drives the funding outreach play |
| **Blind** | Anonymous comp and culture | Medium-high | Verify against a second source; skews negative |
| **Levels.fyi** | Crowd-sourced comp | High | Best single salary source for tech |
| **Stack Overflow Developer Survey** | Annual skill demand | High | Published data, easy to use |
| **GitHub Trending** | 6-12 month leading indicator | High | What is about to appear in JDs |
| **The Pragmatic Engineer** and similar newsletters | Curated industry trends | High | RSS |
| **Engineering blogs of target companies** | What they actually build | High | Coffee chat and cover letter material |

---

## C. Salary data

Levels.fyi (strongest for tech), Glassdoor, Blind, Indeed salary estimates, national and regional
salary surveys, and government labour statistics where published.

**The best source is a conversation.** People will discuss ranges for a role in general terms far
more readily than their own number, especially peers. Ask in coffee chats.

→ [Offer and negotiation](../02_Playbooks/11-OFFER-AND-NEGOTIATION.md)

---

## D. ATS and resume scoring

| Tool | What it gives |
|---|---|
| **Jobscan** | Match rate, keyword analysis, recruiter preference signals |
| **ATSFriendly** | Tests against real ATS platforms |
| **Enhancv** | AI grader |
| **ResyMatch** | Compatibility check |

Run 2-3 on a representative JD, target 75%+. All have usable free tiers.

**The free version of all of them:** paste your PDF into a plain text editor and read what comes
out. That is roughly what the parser sees, and it catches most formatting problems in thirty
seconds.

---

## E. Finding people

- **LinkedIn people search** — company filter plus title filter. Add your school first
- **Your school's alumni tools** — LinkedIn alumni page, alumni directory, department lists.
  **Highest response rate of any discovery method**
- **Apollo** and similar browser extensions — resolve a professional email from a LinkedIn profile.
  Free tiers are usually sufficient at this volume
- **Corporate email pattern inference** — `firstname.lastname@company.com` is the most common.
  Verify before sending in volume
- **Conference speaker lists, engineering blog bylines, GitHub contributors, meetup attendee
  lists** — anyone who has published something has handed you an opener

---

## F. Events

Meetup, Eventbrite, local tech association calendars, university department events, target
companies' own event pages, LinkedIn Events, and community Discord/Slack servers.

→ [Networking events](../02_Playbooks/06-NETWORKING-EVENTS.md)

---

## Ethics and rate limits

**Read this before writing any scraper.**

- **LinkedIn's terms prohibit scraping** and they actively block it. Accounts get restricted, and
  a restricted account is a serious loss mid-search. Use the site normally, or use JobSpy through
  its supported paths. This is a deliberate restriction, not an oversight
- **Prefer official APIs** where they exist. Reddit, Stack Overflow, and GitHub all have
  documented APIs with published rate limits
- **Cache aggressively.** Do not re-fetch what you already have. `fresh_jobs.py` keeps a seen-file
  for exactly this reason
- **Respect robots.txt and rate limits.** A polite scraper that runs once a day is invisible; an
  aggressive one gets your IP blocked from a source you need
- **Never automate outreach messages.** Beyond the ToS problem, automated outreach reads as
  automated and destroys the only advantage the whole approach has. Templates are fine; a bot
  sending them is not

---

## Reviewing this file

At the monthly retro:

- Which sources produced postings you actually applied to?
- Which produced postings that turned into **interviews**? That is the real metric — a source
  with high volume and no conversions is costing you sweep time
- What is new? New job boards and communities appear constantly in every field
- What is dead? Remove it rather than leaving a stale entry that someone re-tries in six months
