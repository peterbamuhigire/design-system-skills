---
name: deck-strategy-presentation
description: Generates a 14-slide social media strategy presentation deck in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill when a strategy document exists (from 05-social-media-strategy) and the consultant needs to present it to the client for the first time. Applies Minto's Pyramid Principle — conclusion first, then evidence, then detail.
---
# Social Media Strategy Presentation Deck

<!-- dual-compat:start -->
## Use when
- Generates a 14-slide social media strategy presentation deck in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill when a strategy document exists (from 05-social-media-strategy) and the consultant needs to present it to the client for the first time. Applies Minto's Pyramid Principle — conclusion first, then evidence, then detail.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Read files in `references/` only when the body points to them or when you need the deeper framework, examples, or evidence.
4. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not turn the deck into a generic outline; every slide needs an assertion, usable speaker notes, and visual direction.

## Outputs
- A slide-by-slide markdown deck using `Headline`, `Bullets`, `Speaker Notes`, and `Visual Direction` for every slide.

## References
- Read `references/presentation-frameworks.md` when you need the deeper framework, examples, or supporting material it contains.

<!-- dual-compat:end -->

## Overview

This skill generates a 14-slide strategy presentation deck. Slide sequencing follows Minto's Pyramid Principle: lead with the destination and the reason it matters, present the evidence that supports the direction, then deliver the execution detail. Clients decide with confidence before they see the detail.

Output is paste-ready markdown. The consultant transfers each slide into PowerPoint, Canva, or Google Slides. No .pptx file is generated.

---

## Required Input

Collect all of the following before generating the deck. If any item is missing, ask for it.

- **Client name** and industry
- **Country/city** (default: Uganda/East Africa)
- **Primary goal** the strategy is designed to achieve
- **Strategy document** — key findings from 05-social-media-strategy (audit summary, personas, platform selection, pillars, KPIs, roadmap)
- **Personas** — 2–3 audience personas with names and key characteristics
- **Audit findings** — top 3 findings with traffic light status (green/amber/red)
- **SMART goals** — 3 primary goals with measurable targets
- **Platform selection** — which platforms, one reason per platform; any platform to deprioritise
- **Content pillars** — 3–5 pillar names, one-sentence purpose, one example post type each
- **Posting frequency** — posts per week per platform, best times
- **KPI table** — KPI name, 90-day target, how measured
- **90-day roadmap** — 3 milestones each for Month 1, Month 2, Month 3
- **Investment summary** — fee structure and payment terms (include only if agreed with client)
- **Consultant name** and contact details (email, phone, WhatsApp)

---

## Slide Generation

Apply the slide structure below in full. Write every field for every slide. Do not leave any field blank or marked TBC.

---

**Slide 1 — Title**
**Headline:** [Client Name] Social Media Strategy [Year]
**Bullets:**
- Prepared by [Consultant Name]
- [Date]
- Confidential — prepared for [Client Name] only
**Speaker Notes:** Open with a warm greeting. Confirm who is in the room. State the purpose: "Today we are presenting the social media strategy we have developed for [Client Name]. By the end of this session you will know exactly where we are going, why, and what we will do together." Keep this slide on screen for no more than 60 seconds.
**Visual Direction:** Full-bleed brand colour or a high-quality image representing the client's industry. Agency logo bottom-left, client logo top-right. White headline text. Minimal text — name and date only.

---

**Slide 2 — Agenda**
**Headline:** Six topics — from where you are now to how we measure success
**Bullets:**
- 01 Your audience — who we are talking to
- 02 Where you are now — audit findings
- 03 Where we are going — strategy and goals
- 04 What we will do — platforms, content, and rhythm
- 05 Measuring success — KPIs and targets
- 06 The 90-day roadmap — Month 1 to Month 3
**Speaker Notes:** Walk through the six agenda items briefly. Tell the client: "We will keep this interactive — please ask questions as we go." Set the expected duration (typically 45–60 minutes for a first strategy presentation).
**Visual Direction:** Clean numbered list on a white or light background. Use a simple icon beside each item. No imagery — this is a navigation slide. Brand accent colour for numbers.

---

**Slide 3 — Your Audience**
**Headline:** We are not targeting everyone — we are targeting [primary persona name(s)]
**Bullets:**
- [Persona 1 name]: [age range, occupation, platform, key motivation]
- [Persona 2 name]: [age range, occupation, platform, key motivation]
- [Persona 3 name if applicable]: [age range, occupation, platform, key motivation]
**Speaker Notes:** Explain why defining the audience is the first strategic decision. Reference the persona development process — how the personas were derived (from the client brief, competitor research, and platform data). Ask the client: "Does this match who you see walking through the door or enquiring on WhatsApp?" Correct if needed — this is a working document.
**Visual Direction:** Three columns side by side, one per persona. Each column has a simple illustrated avatar (no real photos unless client provides them), the persona name in bold, and 3–4 key facts. Use a soft background per column in brand colours. Keep text minimal — this is a visual slide.

---

**Slide 4 — Where You Are Now**
**Headline:** Three findings from your audit that this strategy directly addresses
**Bullets:**
- [Finding 1]: [one sentence — status: 🔴 / 🟡 / 🟢]
- [Finding 2]: [one sentence — status: 🔴 / 🟡 / 🟢]
- [Finding 3]: [one sentence — status: 🔴 / 🟡 / 🟢]
**Speaker Notes:** This slide sets the baseline. Do not dwell here — the purpose is to establish shared understanding, not to criticise past activity. Frame findings constructively: "Here is what the data tells us, and here is why it creates an opportunity." Acknowledge any quick wins already underway. Reference the full audit document (02-platform-audit) for the complete picture.
**Visual Direction:** Three rows, each with a traffic light icon (red/amber/green) on the left, finding text in the centre, and a one-word status label on the right. Use a simple table or card layout. Muted background. Bold the status words.

---

**Slide 5 — Where We Are Going**
**Headline:** [Strategy statement — one sentence describing the direction and the outcome]
**Bullets:**
- Goal 1: [SMART — specific metric, 90-day timeframe]
- Goal 2: [SMART — specific metric, 90-day timeframe]
- Goal 3: [SMART — specific metric, 90-day timeframe]
**Speaker Notes:** This is the conclusion slide — the most important slide in the deck. Spend time here. Read the strategy statement aloud. Explain each goal: what it means, why it was chosen, and how it connects to the client's business objective. Use the RACE framework (Chaffey, 2024) to show how goals map to Reach, Act, Convert, and Engage where applicable. Ask for agreement before moving on.
**Visual Direction:** Strategy statement in large, bold type at the top — this is the hero element. Three goal cards below, each with an icon representing the goal type (reach, engagement, conversion). Brand primary colour. White text. Simple and bold — this slide should feel decisive.

---

**Slide 6 — Platform Selection**
**Headline:** We are prioritising [Platform A] and [Platform B] because that is where [primary persona] spends time
**Bullets:**
- [Platform 1]: [one-sentence rationale — audience size, persona match, content fit]
- [Platform 2]: [one-sentence rationale]
- [Platform 3 if applicable]: [one-sentence rationale]
- Deprioritised: [Platform X] — [one-sentence reason: low audience match, resource cost, wrong content format]
**Speaker Notes:** Explain the platform selection logic: the goal is not to be everywhere but to be excellent on the right channels. Reference the Uganda/East African platform context where relevant — e.g., Facebook and WhatsApp dominate for most consumer brands; LinkedIn is relevant for B2B and professional services. If the client pushes back on a deprioritised platform, acknowledge their perspective and explain the trade-off.
**Visual Direction:** Platform logos displayed prominently (official icons). Selected platforms above a dividing line labelled "Active". Deprioritised platform(s) below the line, greyed out, labelled "Not in scope — Year 1". Clean white background. No clutter.

---

**Slide 7 — Content Pillars**
**Headline:** Every post we publish will serve one of [3–5] content pillars
**Bullets:**
- [Pillar 1 name]: [one-sentence purpose] — e.g. [example post type]
- [Pillar 2 name]: [one-sentence purpose] — e.g. [example post type]
- [Pillar 3 name]: [one-sentence purpose] — e.g. [example post type]
- [Pillar 4 if applicable]: [one-sentence purpose] — e.g. [example post type]
**Speaker Notes:** Explain what a content pillar is — a theme that gives every post a strategic reason to exist. Connect each pillar back to a goal or persona. Reference the full content pillars document (10-content-pillars) for detailed guidance. Ask the client: "Do these pillars capture what your brand is about? Is there a topic we should add or remove?"
**Visual Direction:** One card per pillar, displayed in a grid (3 across or 2+2 if 4 pillars). Each card: pillar name in large bold type, one-sentence purpose below, icon representing the theme. Brand colour palette — each pillar gets its own accent colour. Simple and visual.

---

**Slide 8 — What We Will Post**
**Headline:** Content is planned, purposeful, and varied — not random
**Bullets:**
- [Content type 1]: [brief description — e.g. "Short educational tips — 3 per week on Facebook, addressing common questions from Persona 1"]
- [Content type 2]: [brief description — e.g. "Behind-the-scenes video — fortnightly on Instagram Reels, showing the team and process"]
- [Content type 3]: [brief description — e.g. "Customer testimonials — monthly on Facebook and WhatsApp, one per pillar"]
- [Content type 4 if applicable]: [brief description]
**Speaker Notes:** Clarify that this slide shows content types and their purpose — not the actual posts. The actual posts appear in the content calendar (11-content-calendar). Emphasise variety: a content mix that educates, entertains, and converts (10-4-1 rule: Bodnar and Cohen, 2012). Ask the client about content assets they already have — existing photos, testimonials, product shots.
**Visual Direction:** Three or four content type cards arranged horizontally. Each card shows the content type name, a representative icon or illustration, and 2–3 descriptive bullets. Soft background. Keep it visual — the goal is for the client to picture the content.

---

**Slide 9 — Posting Rhythm**
**Headline:** Consistency builds audiences — here is the posting schedule
**Bullets:**
- See table below
**Speaker Notes:** Walk through the table row by row. Explain that posting at the right time on each platform is as important as what is posted. Reference platform-specific best-time data for Uganda/East Africa — Facebook engagement peaks in early morning and evening; Instagram is strongest midday and evenings; WhatsApp broadcast messages perform best before 8am. Note that the schedule will be reviewed after Month 1 using actual engagement data.

| Platform | Posts/week | Best times (EAT) |
|---|---|---|
| [Platform 1] | [X] | [e.g. Mon/Wed/Fri — 07:00 and 19:00] |
| [Platform 2] | [X] | [e.g. Tue/Thu/Sat — 12:00 and 20:00] |
| [Platform 3] | [X] | [e.g. Daily — 07:30] |

**Visual Direction:** Clean table with platform logos in the first column. Alternating row shading in brand light colour. No unnecessary borders. Add a small clock icon in the header. Simple, scannable.

---

**Slide 10 — Community Management**
**Headline:** Every comment and message is an opportunity — here is how we handle them
**Bullets:**
- Respond to all comments within [X hours] on weekdays, [Y hours] at weekends
- Use a warm, professional tone — friendly but never informal to the point of unprofessionalism
- Escalation protocol: tag [client contact] for complaints, pricing queries, and media enquiries
- Monthly review of frequently asked questions to add to the content plan
**Speaker Notes:** Community management is where the brand relationship is built or broken. Reference playbook-community-management for detailed tone guidance and response templates. Clarify responsibilities — what the agency handles vs. what the client handles. Confirm the client's escalation contact and response expectation.
**Visual Direction:** Four principle cards in a 2x2 grid. Each card has an icon (clock, speech bubble, escalation arrow, calendar) and a 1–2 sentence principle. Clean layout on a white or very light background. Brand accent colour for icons.

---

**Slide 11 — Measuring Success**
**Headline:** What gets measured gets improved — here are the KPIs we will track
**Bullets:**
- See KPI table below
**Speaker Notes:** Walk through the KPI table. Explain the difference between vanity metrics (follower count) and value metrics (enquiries, reach, engagement rate). Connect each KPI back to a goal stated on Slide 5. Confirm that monthly reports will track progress against these targets (deck-monthly-report). Note that targets will be reviewed at the 90-day mark.

| KPI | 90-day target | How measured |
|---|---|---|
| [KPI 1 — e.g. Follower growth] | [e.g. +500 followers] | [Platform analytics] |
| [KPI 2 — e.g. Engagement rate] | [e.g. ≥3.5% per post] | [Platform analytics] |
| [KPI 3 — e.g. Reach] | [e.g. 15,000 accounts/month] | [Platform analytics] |
| [KPI 4 — e.g. Enquiries via social] | [e.g. 20/month] | [Client CRM or WhatsApp log] |
| [KPI 5 — e.g. Website clicks] | [e.g. 300/month] | [Google Analytics] |

**Visual Direction:** Clean table — KPI column wider on the left, target and method narrower on the right. Add a small status dot column (to be filled in each month — green/amber/red). Present on a white background. Header row in brand primary colour with white text.

---

**Slide 12 — 90-Day Roadmap**
**Headline:** Here is exactly what happens in the first 90 days
**Bullets:**
- Month 1: [Milestone 1] / [Milestone 2] / [Milestone 3]
- Month 2: [Milestone 1] / [Milestone 2] / [Milestone 3]
- Month 3: [Milestone 1] / [Milestone 2] / [Milestone 3]
**Speaker Notes:** Walk through the roadmap month by month. Be specific — clients need to know what they will see and when. Month 1 is typically about setup, establishing baseline content, and building consistency. Month 2 is about refining based on early data. Month 3 is about scaling what is working. Reassure the client that the roadmap is a living document — it will be updated at each monthly review.
**Visual Direction:** Three-column layout — one column per month. Each column has a month label at the top (Month 1, Month 2, Month 3) and three bullet milestones below. Use a horizontal flow arrow across the top to show progression. Brand colours for column headers. Clean, timeline feel.

---

**Slide 13 — Investment and Next Steps**
**Headline:** Here is what is included, what it costs, and what happens next
**Bullets:**
- Monthly retainer: [fee] — includes [list of deliverables]
- Payment terms: [invoice date, payment due, method]
- Next step 1: [action + owner + date — e.g. "Review and sign service agreement — Client — by [date]"]
- Next step 2: [action + owner + date — e.g. "Provide brand assets and access — Client — by [date]"]
- Next step 3: [action + owner + date — e.g. "Content calendar for Month 1 delivered — Agency — by [date]"]
**Speaker Notes:** Present the fee with confidence — do not apologise for it. Connect the investment to the expected outcomes stated in Slide 11. If the client questions the fee, return to the value: "This retainer covers strategy, content creation, scheduling, community management, and monthly reporting." Have the service agreement ready to share after the meeting. Confirm next steps verbally before leaving.
**Visual Direction:** Two-section slide. Top section: investment summary in a clean one-row table or three-card layout. Bottom section: three next step cards with owner icons (client vs. agency) and dates. Use a subtle dividing line between sections. Professional and clean.

---

**Slide 14 — Thank You / Q&A**
**Headline:** [Client Name], let us build something excellent together
**Bullets:**
- [Consultant Name]
- [Email address]
- [Phone / WhatsApp number]
- [Website or portfolio link]
**Speaker Notes:** Close warmly and with confidence. Invite questions: "I would love to hear your thoughts — what resonates, what questions do you have, and is there anything you would like us to revisit?" Listen carefully. Take notes. Do not be defensive about any element of the strategy — treat pushback as information. Confirm the next step before the client leaves the room.
**Visual Direction:** Full-bleed brand colour or a warm, professional lifestyle image relevant to the client's industry. Large "Thank you" or the client name as the hero text. Contact details below in clean white text. Agency logo and client logo side by side at the bottom.

---

## The Case for Visuals — 3M/Wharton Data

*Cited in Pinskey (1997)*

- Presentations using visuals are **43% more persuasive** than those without
- Audiences retain information **65% better** when paired with a relevant visual
- A presenter using visuals is perceived as more prepared, more professional, and more credible

**Implication for strategy decks:** Every data point should have a chart. Every conceptual argument should have a diagram. Every case study should have a before/after visual. Text-only slides are an opportunity cost.

**Principles:**
- One idea per slide — never two arguments on the same slide
- Headline each slide with the **conclusion**, not the topic (Minto's Pyramid Principle — conclusion first, evidence below)
- Use images where possible, bullet lists only where genuinely required
- The handout must add value beyond the slide content — include supporting data, references, and action items the slide did not have room for

---

## Persuasion Frameworks

Apply frameworks from `references/presentation-frameworks.md` when generating this deck.

Key principles for strategy presentations:
- Slide 5 (Where We Are Going) is the Big Idea slide — the strategy statement must be one complete sentence with a point of view and what is at stake, not a summary of activities (Duarte: Big Idea)
- The Sparkline structure is visible in the deck: Slide 4 (Where You Are Now) = What Is; Slide 5 (Where We Are Going) = What Could Be — the contrast creates the motivation to proceed (Duarte: Sparkline)
- Every slide title is a complete assertion: "We are prioritising Facebook and WhatsApp because that is where your buyers spend time" not "Platform selection" (Duarte: Big Idea discipline)
- Open with the client's audience and goals — not the agency's process — the client is the hero of this presentation (Hatton: Empathy Model)
- Answer Hatton's Two Strategic Questions before writing: Why should they approve this strategy? and Why will they remember this presentation?

Read `references/presentation-frameworks.md` for the full framework guide.

---

## Quality Criteria

- Every slide has a complete Headline, Bullets, Speaker Notes, and Visual Direction — no field is left empty or marked as placeholder
- Minto's Pyramid Principle is visible in the structure: the strategy statement and goals appear on Slides 5–6, before the execution detail on Slides 7–12
- All goals stated on Slide 5 are SMART (specific metric, named platform or channel, 90-day timeframe)
- KPI table on Slide 11 connects directly to goals on Slide 5 — no KPI without a corresponding goal
- Platform selection on Slide 6 references the Uganda/East African platform context unless the client is in a different market
- Speaker notes are written for a consultant presenting live — they include things to say, questions to ask, and responses to likely pushback
- The 90-day roadmap on Slide 12 contains 9 named, specific milestones (3 per month) — not generic labels
- The deck reads as a coherent narrative from Slide 1 to Slide 14 — each slide builds on the previous one
