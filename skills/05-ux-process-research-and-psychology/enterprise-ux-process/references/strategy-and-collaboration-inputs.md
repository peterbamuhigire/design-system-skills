# Strategy Framing, Competitor Analysis and Product-Team Collaboration

Parent skill: [`../SKILL.md`](../SKILL.md) (`enterprise-ux-process`).

**When to read:** in Phase 1 (strategy framing) and Phase 5 (competitor analysis) of the parent
skill, and when setting up the working rhythm with a product manager or client team.

---

## 1. Strategy framing (Phase 1)

UX strategy is set before design or development starts and is checked with real prospective
customers, not only with stakeholders. Four conditions must hold at the same time; if any one fails,
the strategy fails, however strong the others are.

| Condition | Question to answer in one line | Evidence that counts | If left blank |
|---|---|---|---|
| Business strategy | How does the product create and capture value (revenue model, market, constraints)? | Sponsor-approved model and constraints | Design optimises a product nobody can fund |
| Value innovation | What distinctive value does it offer that alternatives do not? | Competitor analysis (section 2) showing the gap | A copy of the market leader with no reason to switch |
| Validated user research | What evidence from real potential users supports the need? | Interview, field or test findings with dates and sample | The strategy rests on internal opinion |
| Strong UX design | How will the experience deliver the value, and how has design shaped the other three? | Early flows or prototypes tested with users | A sound model ruined by an unusable product |

**Procedure**

1. Write one line per condition in the engagement brief.
2. Mark each line with its evidence source and date.
3. Any blank or unevidenced line is a stop condition: gather the evidence before Phase 2 continues.
4. Revisit the four lines at every major gate; a change in one (for example, a new revenue model)
   re-opens the others.

## 2. Competitor analysis (Phase 5)

### Scope decisions

| Decision | Rule | Consequence of getting it wrong |
|---|---|---|
| How many competitors | At least five direct and three indirect | Too few hides the real benchmark; the brief overstates novelty |
| Which counts as indirect | Include regional competitors and informal alternatives (WhatsApp ordering, agents, paper forms, a cousin who "does it for you") | International-only lists miss what users actually do today |
| Mobile and desktop differ greatly | Two rows for that competitor | Averaged scores hide a weak channel |
| Time budget | About 30 minutes per competitor on the first pass; deepen only where it matters | Weeks lost on uniform depth |
| Account access | One shared team test account per product; never personal logins; buy paid apps where needed | Personal data exposure; incomplete view of paid features |

### Competitor profile template

One row per competitor, attributes grouped by what they tell you.

**A. Identity and access**

| Attribute | Record |
|---|---|
| Web address and app-store links | Every platform offered |
| Test login | Shared team account reference (not the password in the document) |
| Purpose | One or two sentences on the value proposition |
| Year founded | |

**B. Business model and scale**

| Attribute | Record |
|---|---|
| Funding | Publicly available funding information |
| Revenue streams | Fees, subscription, advertising, data, commission |
| Traffic or usage estimate | Triangulate at least two current estimation tools; label as an estimate and date it |
| Catalogue size or listings (optional) | Proxy by searching one common term on each product |

**C. Product and content**

| Attribute | Record |
|---|---|
| Primary categories | Copy the global navigation labels |
| Content types | Balance of text, photo and video; scannability; depth of detail pages |
| Personalisation | Favourites, saved items, profiles, messaging |
| Community and user content | Comments, posts, forums; balance of editorial and user content |
| Social channels in active use | Channels with a visible, current strategy; ignore dormant accounts |

**D. Quality and perception**

| Attribute | Record |
|---|---|
| Quick heuristic grade (A-F) | Can the primary goal be completed? Is it consistent? Can things be found? Are feedback and errors useful? |
| Customer reviews | Recurring complaints and recurring praise |
| Competitive advantage | Top three concrete differentiators |

**E. Working notes**

| Attribute | Record |
|---|---|
| General notes | |
| Questions for the team | Open questions the analysis raised |
| Analysis | Filled in during the analysis procedure below |

### Analysis procedure

1. Scan each attribute across all competitors and colour-code highs and lows.
2. Group competitors that behave alike (for example, "agent-led", "app-only", "marketplace").
3. Benchmark every competitor against the same yardstick (the heuristic grade and the attributes the
   focus user cares about most).
4. Write a one-page findings brief for the product owner: gaps, threats, the value-innovation
   opportunity, and recommendations. This brief feeds the "value innovation" line in section 1.

### Example (original)

A Kampala private clinic plans online appointment booking. Direct competitors: three other clinic
booking portals and two health-app aggregators. Indirect: phoning the receptionist, WhatsApp
messages to a nurse, and walking in early to queue. The matrix shows every direct competitor scores
"B" or lower on findability of doctor availability, and customer reviews repeatedly complain that
confirmations never arrive. The informal WhatsApp route wins on trust (a named nurse replies). The
brief recommends booking with a named staff confirmation by SMS and WhatsApp, rather than an
anonymous portal, as the value innovation.

## 3. Product-team collaboration

### Principles to agree with stakeholders at kick-off

| Principle | What it means in practice | Failure if not agreed |
|---|---|---|
| Design is how it works, not only how it looks | Design reviews cover flows and rules, not only screens | Design is called in late to "make it pretty" |
| Good design improves understanding | The interface must explain itself; users rarely watch tutorials | Help content and training compensate for unclear screens |
| Design needs experimentation | Budget several prototype rounds | The first draft ships untested |
| Design is teamwork | The product owner takes part and gives continual feedback | Late reversals from an absent owner |
| Design is measured and tested | Usability tests, interviews, field visits, quick first-impression tests, A/B tests | Opinion decides |
| Design is continuing work | Plan for iteration after launch | The product decays after the project closes |

### Working practices

| Practice | Rule |
|---|---|
| Kick-off workshop | Everyone with responsibility for the product attends; produce personas, journeys and look-and-feel direction together |
| Weekly design meeting | One representative per function; about five people; no longer than about 90 minutes |
| Specification | Clickable wireframes instead of long specification documents; they surface questions early |
| Disputes | Settle opinion disputes with user research; record test sessions and show key clips to stakeholders |

### Team roles

| Decision | Rule | Consequence of the wrong choice |
|---|---|---|
| Role coverage | UI design, UX design and UX research are distinct roles (not necessarily three people) | Research silently disappears |
| One-person team | Protect research explicitly; it is the first thing a solo designer drops and the most important feedback signal | Decisions without user evidence |
| Seniority | Never place a junior alone in the role; pair a senior with a junior | Unchallenged beginner decisions in production |

### Sprint rhythm

1. Run week-long design sprints.
2. Open each sprint with a design meeting (designer, researcher, business lead, technical lead) that
   reviews the latest designs and research and agrees the next tasks.
3. End each sprint with tested design input that developers can build in their next sprint.

---

Sources: Levy, J. (2015) *UX Strategy*, O'Reilly Media (four conditions of UX strategy; competitor
attribute set and four-step analysis); Fekeshazi, Z., *Product Managers' Guide to UX Design*, UX
Studio (collaboration principles, practices, roles and sprint rhythm).
