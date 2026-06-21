---
name: deck-monthly-report
description: Generates a 10-slide monthly performance report presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill at the end of each calendar month when preparing a client reporting meeting. The consultant must replace all placeholder data with actual client figures before presenting.
---
# Monthly Performance Report Deck

<!-- dual-compat:start -->
## Use when
- Generates a 10-slide monthly performance report presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill at the end of each calendar month when preparing a client reporting meeting. The consultant must replace all placeholder data with actual client figures before presenting.
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

This skill generates a 10-slide monthly performance report for presenting to the client. Tone is professional but conversational. Clients leave the meeting feeling informed and confident — not overwhelmed by data.

Lead with good news. Acknowledge what did not work briefly and directly. Move to solutions quickly. The meeting should feel like a forward-looking conversation, not an audit.

**Important:** this skill generates the structure and placeholder text. The consultant must populate every data field with actual client figures before presenting. Never present a deck with placeholder text remaining.

Output is paste-ready markdown. Transfer each slide into PowerPoint, Canva, or Google Slides.

---

## Required Input

Collect all of the following before generating the deck. Ask for any missing items.

- **Client name** and industry
- **Country/city** (default: Uganda/East Africa)
- **Primary goal** agreed in the strategy
- **Report month and year** (e.g. February 2026)
- **Platform metrics** for the month: follower counts, net follower change, total reach, impressions, engagement rate per platform, top-performing posts (3)
- **Targets** from the strategy document (05-social-media-strategy) for comparison
- **Top 3 posts** — platform, content type, key metric achieved (reach, engagement, clicks, saves)
- **Next month campaign dates** and themes
- **Issues encountered** — anything that underperformed, any external factor, any delivery problem
- **Experiments or tests** planned for next month (2–3 hypotheses)
- **Consultant name** and contact details
- **Next meeting date** (or placeholder if not yet confirmed)

---

## Slide Generation

Generate all 10 slides in full. Write every field. Replace all bracketed placeholders with actual client data when presenting.

---

**Slide 1 — Title**
**Headline:** [Client Name] — Social Media Report — [Month Year]
**Bullets:**
- Prepared by [Consultant Name]
- [Date presented]
- Reporting period: 1–[last day] [Month] [Year]
**Speaker Notes:** Open with a brief warm welcome. State the purpose of the meeting: "Today we are reviewing [Month]'s performance, sharing what the data tells us, and confirming the plan for [next month]." Keep this slide on screen for no more than 30 seconds — move to the executive summary promptly.
**Visual Direction:** Full-bleed brand colour or a clean professional background. Client logo top-right, agency logo bottom-left. White text. Month and year displayed prominently. Minimal — this is a cover slide.

---

**Slide 2 — Executive Summary**
**Headline:** [Month] was [characterisation — e.g. "a strong month for reach, with one area to address"]
**Bullets:**
- What went well: [top positive — specific and data-backed, e.g. "Engagement rate on Facebook reached 4.2% — above our 3.5% target"]
- What did not go as planned: [honest, brief — e.g. "Instagram follower growth was flat at +12 vs. a target of +50"]
- What we are doing about it: [concrete action — e.g. "We are testing Reels-first content in [next month] to drive follower growth"]
**Speaker Notes:** This is the most important slide in the deck for client confidence. Lead with the good news — not to spin results, but because progress deserves to be acknowledged first. State the underperformance clearly and without hedging, then move immediately to the solution. If everything went well, say so. If it was a difficult month, say that too — clients trust consultants who are honest. Do not move past this slide until the client has acknowledged the three points.
**Visual Direction:** Three-card horizontal layout. Card 1: green accent, tick icon, "What went well." Card 2: amber accent, alert icon, "What did not go as planned." Card 3: blue accent, arrow icon, "What we are doing." Bold headline at top. Clean white background.

---

**Slide 3 — KPI Scorecard**
**Headline:** Here is how we performed against every target this month
**Bullets:**
- See table below — green = on or above target, amber = within 20% of target, red = more than 20% below target
**Speaker Notes:** Walk through the table row by row. Do not rush. For any red or amber metric, refer to the relevant slide later in the deck (Slide 6 or Slide 9) for explanation and action. Acknowledge that some metrics take longer to respond to strategy changes — particularly follower count and reach, which are slower-moving than engagement. Remind the client that targets were set at the start and will be reviewed at the 90-day mark.

| Platform | KPI | Target | Actual | Status |
|---|---|---|---|---|
| [Platform 1] | [e.g. Followers] | [target] | [actual] | 🟢 / 🟡 / 🔴 |
| [Platform 1] | [e.g. Engagement rate] | [target] | [actual] | 🟢 / 🟡 / 🔴 |
| [Platform 2] | [e.g. Reach] | [target] | [actual] | 🟢 / 🟡 / 🔴 |
| [Platform 2] | [e.g. Follower growth] | [target] | [actual] | 🟢 / 🟡 / 🔴 |
| [Platform 3] | [e.g. Click-throughs] | [target] | [actual] | 🟢 / 🟡 / 🔴 |

**Visual Direction:** Full-width table. Status column uses coloured dots or emoji traffic lights. Header row in brand primary colour with white text. Alternating row shading. Platform logos in the first column for visual clarity. Keep font size legible — this table will be read in the room.

---

**Slide 4 — Platform Highlights**
**Headline:** [Month]'s platform-by-platform performance at a glance
**Bullets:**
- [Platform 1]: [3 key metrics or 1 short paragraph — what happened, what it means]
- [Platform 2]: [3 key metrics or 1 short paragraph]
- [Platform 3 if applicable]: [3 key metrics or 1 short paragraph]
**Speaker Notes:** Give each platform its own 60-second narrative. Explain what the numbers mean in context — a 3% engagement rate on Facebook is excellent; 0.8% needs attention. Connect the numbers to content decisions made in the previous month's plan. Note any platform algorithm changes or external factors (public holidays, events) that may have affected performance.
**Visual Direction:** One section per platform, separated by a subtle dividing line or card border. Platform logo beside the section heading. Metrics displayed as large numbers with small labels (e.g. "4.2% Engagement Rate" in bold). Clean, data-forward layout. White background, brand accent for section headers.

---

**Slide 5 — Best-Performing Content**
**Headline:** Three posts drove the most value this month — here is what they tell us
**Bullets:**
- Post 1: [Platform] / [Content type] / [Key metric — e.g. "Reached 4,200 accounts"] / [1-sentence analysis — why it worked]
- Post 2: [Platform] / [Content type] / [Key metric] / [1-sentence analysis]
- Post 3: [Platform] / [Content type] / [Key metric] / [1-sentence analysis]
**Speaker Notes:** Spend time on this slide — it is where learning happens. For each post, explain the connection between the content decision and the result. Look for patterns: did video outperform static? Did posts with questions in the caption drive more comments? Did a particular time of day deliver higher reach? These patterns feed directly into next month's content plan. Ask the client: "Do any of these surprise you?"
**Visual Direction:** Three cards in a row, one per post. Each card: platform icon top-left, content type label, key metric displayed large in brand colour, 1-sentence analysis in smaller text at the bottom. If post screenshots are available, include a small thumbnail. Clean card design on a white background.

---

**Slide 6 — What Worked and Why**
**Headline:** Three insights from [Month]'s data that will shape [next month]'s content
**Bullets:**
- Insight 1: [Pattern or finding — e.g. "Posts published before 08:00 EAT consistently outperformed midday posts by 40% on reach"]
- Insight 2: [Pattern or finding — e.g. "Content featuring real team members generated 3× more comments than product-only posts"]
- Insight 3: [Pattern or finding — e.g. "The Educational pillar drove more saves than any other pillar — suggesting high value to the audience"]
**Speaker Notes:** These insights are the intellectual value of the engagement. Do not just describe what happened — explain what it means and what the implication is for content decisions. Reference the relevant content pillars (10-content-pillars) where the insight validates or challenges a pillar's performance. Ask: "Based on these insights, is there anything you want us to do differently?"
**Visual Direction:** Three insight cards stacked vertically or in a 3-column layout. Each card has a bold insight statement at the top and 1–2 lines of supporting context below. Use a lightbulb or chart icon per card. Accent colour for the bold statement. White background. Generous whitespace.

---

**Slide 7 — What We Are Testing Next Month**
**Headline:** [Next month], we are running [number] experiments to improve performance
**Bullets:**
- Experiment 1: We believe [action] will [result] because [reason based on this month's data]
- Experiment 2: We believe [action] will [result] because [reason based on this month's data]
- Experiment 3 (if applicable): We believe [action] will [result] because [reason based on this month's data]
**Speaker Notes:** Frame experiments as hypothesis-driven decisions, not guesses. The hypothesis format ("We believe... will... because...") demonstrates analytical rigour. Confirm the client is comfortable with the planned tests. Note that one successful experiment becomes standard practice; one that underperforms is discarded — not a failure, just information. Experiments are small adjustments within the approved strategy, not departures from it.
**Visual Direction:** Hypothesis cards, one per experiment. Each card formatted as: bold "We believe" statement / supporting rationale below / small "success looks like" label at the bottom with the metric being measured. Use a test-tube or arrow icon. Blue or teal accent to signal "forward-looking". Clean, optimistic layout.

---

**Slide 8 — Content Calendar Preview**
**Headline:** Here is what is planned for [next month]
**Bullets:**
- Key themes: [pillar focus for the month — e.g. "Community stories and product education"]
- Campaign or event dates: [list key dates — e.g. "Uganda Independence Day — 9 October", "Product launch — 15 October"]
- Platform focus: [which platform gets the most content investment this month and why]
- Volume: [total planned posts — e.g. "28 posts across Facebook, Instagram, and WhatsApp"]
**Speaker Notes:** This slide reassures the client that next month is already planned. Reference the full content calendar (11-content-calendar) and confirm the client has received it (or will receive it within [X] days). Highlight any dates where the client needs to provide assets or approvals in advance. Confirm approval process and lead times.
**Visual Direction:** A simple monthly calendar grid or a clean list layout showing week-by-week themes. Highlight campaign dates in brand accent colour. Platform icons beside platform-specific entries. Keep it legible — this is a preview, not a full calendar. White background.

---

**Slide 9 — Issues and Recommendations**
**Headline:** [Issue summary — e.g. "One underperformance issue this month — here is what changed"]
**Bullets:**
- Issue: [What went wrong — specific, factual, without blame]
- Cause: [Why it happened — platform algorithm, content gap, approval delay, external event]
- Change: [What is different from next month — specific action or process adjustment]
**Speaker Notes:** Handle this slide with confidence and directness. If there were no issues, say so briefly and move on. If there were issues, do not minimise them — present the cause and the solution clearly. Clients respect honesty more than spin. If the issue was on the agency's side (missed deadline, weak content), own it and state what has been fixed. If the issue was external (platform outage, client approval delay), explain it without assigning blame.
**Visual Direction:** Three-row layout: Issue row (red-left border), Cause row (amber-left border), Change row (green-left border). Each row has a clear label and a short statement. Simple, honest design. No unnecessary decoration. If there were no issues, replace with a "No issues this month" card in green with a brief positive note.

---

**Slide 10 — Thank You**
**Headline:** [Month] is done — [next month] is planned — let us keep building
**Bullets:**
- [Consultant Name]
- [Email address]
- [Phone / WhatsApp number]
- Next meeting: [date placeholder — e.g. "Last week of [next month] — date TBC"]
**Speaker Notes:** Close on a positive, forward-looking note. Summarise the top takeaway in one sentence: "The headline from [Month] is [positive result], and [next month] we are focused on [priority]." Confirm the next meeting date before leaving. Ask if the client has any questions or requests not covered in the deck. Follow up with a written summary email within 24 hours.
**Visual Direction:** Full-bleed brand colour or a clean professional background consistent with the cover slide. Large warm closing message — brief and confident. Contact details and next meeting date in white text. Agency and client logos at the bottom. No data on this slide — it is a relational close.

---

## Persuasion Frameworks

Apply frameworks from `references/presentation-frameworks.md` when generating this deck.

Key principles for monthly reports:
- Every KPI slide title is a complete assertion: "Engagement rate is 2× the benchmark this month" not "Engagement rate" (Duarte: Big Idea per slide)
- Lead with the so-what before the data — the client cares about business impact, not platform metrics (Duarte: Executive 10% Rule — conclusions first)
- Close with a forward-looking slide: next month's focus, recommendations, or decision needed — never end on historical data (Hatton: Persuasion Sandwich — bottom slice)
- Frame every metric in terms of the client's business: "40 more enquiries" not "18% reach increase" (Hatton: Empathy Model)
- The report opening slide must state the key result of the month in one sentence — the decision-maker should know the headline before they see any data (Duarte: Executive 10% Rule)

Read `references/presentation-frameworks.md` for the full framework guide.

---

## Quality Criteria

- Every slide has a complete Headline, Bullets, Speaker Notes, and Visual Direction — no field is empty
- The executive summary on Slide 2 leads with good news, states the underperformance honestly, and gives a concrete next action
- All KPIs on Slide 3 correspond directly to targets set in the strategy document — no invented metrics
- The best-performing content on Slide 5 includes a one-sentence analysis (not just the metric) explaining why it worked
- Insights on Slide 6 are data-derived observations, not generic statements — each connects to a specific number from the month
- Experiments on Slide 7 use the hypothesis format: "We believe [action] will [result] because [reason]"
- Issues on Slide 9 are stated factually with a cause and a concrete change — no vague reassurances
- The deck tells a coherent story from month summary to forward plan — a client who reads only the headlines understands the full picture
