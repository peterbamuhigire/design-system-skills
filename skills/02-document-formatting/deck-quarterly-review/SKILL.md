---
name: deck-quarterly-review
description: Generates a 16-slide quarterly strategy review presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill at the end of each quarter (Q1–Q4) when presenting a full performance review and recommending strategy adjustments. More substantial than the monthly report — this deck revisits the strategy and proposes changes for the next quarter.
---
# Quarterly Strategy Review Deck

<!-- dual-compat:start -->
## Use when
- Generates a 16-slide quarterly strategy review presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill at the end of each quarter (Q1–Q4) when presenting a full performance review and recommending strategy adjustments. More substantial than the monthly report — this deck revisits the strategy and proposes changes for the next quarter.
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

This skill generates a 16-slide quarterly review presentation. The quarterly review is more substantial than the monthly report — it revisits the strategy, assesses what is working and what is not, and recommends specific adjustments for the next quarter.

The deck serves two purposes: accountability (what happened) and direction (what changes). Give equal weight to both.

Output is paste-ready markdown. Transfer each slide into PowerPoint, Canva, or Google Slides. Populate all data fields with actual client figures before presenting.

---

## Required Input

Collect all of the following before generating the deck. Ask for any missing items.

- **Client name** and industry
- **Country/city** (default: Uganda/East Africa)
- **Primary goal** agreed in the strategy
- **Quarter being reviewed** (e.g. Q1 2026: January–March 2026)
- **All platform metrics for the quarter**: follower count start and end, total reach, total impressions, engagement rate (average), enquiries or leads generated, top content type by reach and by engagement
- **Original 90-day targets** from the strategy document (05-social-media-strategy)
- **Content pillar performance data** — which pillar generated most reach, most engagement, most saves/shares
- **Competitor observations** — 1–2 observations per competitor (from an updated 02-platform-audit)
- **Budget spend summary** — by activity type (content creation, scheduling tools, any paid promotion)
- **Campaign ideas for next quarter** — 1–2 concepts with objective, concept, and timing
- **Emerging opportunities** — new platform features, audience segments, seasonal moments for next quarter
- **Consultant name** and contact details

---

## Slide Generation

Generate all 16 slides in full. Write every field. Replace all bracketed placeholders with actual client data when presenting.

---

**Slide 1 — Title**
**Headline:** [Client Name] — [Q1/Q2/Q3/Q4] [Year] Strategy Review
**Bullets:**
- Prepared by [Consultant Name]
- Presented on [date]
- Covering: [start month] – [end month] [year]
**Speaker Notes:** Open with a brief framing statement: "Today we are doing more than reviewing numbers — we are assessing whether the strategy is working and deciding what to adjust for [next quarter]." Set the expectation that this meeting is about decisions, not just data. Allow 60–90 minutes for a full quarterly review.
**Visual Direction:** Full-bleed brand colour. Client logo top-right, agency logo bottom-left. Quarter and year prominently displayed. Clean, authoritative — this is a significant meeting and the cover should reflect that.

---

**Slide 2 — Quarter in Numbers**
**Headline:** Five numbers that define [Q1/Q2/Q3/Q4] [year]
**Bullets:**
- Follower growth: [net change across all platforms — e.g. "+1,240 followers"]
- Total reach: [total accounts reached across all platforms — e.g. "218,000"]
- Engagement rate: [average across all platforms — e.g. "3.8%"]
- Enquiries / leads generated: [number — e.g. "47 WhatsApp enquiries attributed to social content"]
- Top content type: [e.g. "Facebook video — drove 42% of total reach"]
**Speaker Notes:** This slide delivers the quarter's story in five numbers. Read each number with a brief comment — is it good, is it better than last quarter, is it against target? Keep it brief — the detail comes on Slide 3. The goal here is to give the client a clear, confident headline before the granular review.
**Visual Direction:** Five large-number cards in a prominent grid (2+2+1 or 3+2 layout). Each card: the metric name as a small label above, the number large and bold in brand colour, a brief descriptor below (e.g. "+1,240" with "net follower gain" below). White background. Bold and data-forward — these numbers are the hero.

---

**Slide 3 — Progress vs. 90-Day Targets**
**Headline:** Here is how every KPI performed against the targets set at the start of the quarter
**Bullets:**
- Green = achieved or exceeded, amber = within 20% of target, red = more than 20% below target
**Speaker Notes:** This is the accountability slide. Walk through every KPI. For greens, acknowledge the achievement. For ambers and reds, do not move on until the cause is briefly stated — the full analysis comes on Slide 8. Be honest: missed targets are information, not failure. If targets were missed due to external factors (platform algorithm change, public holiday, client asset delays), state this clearly.

| KPI | Target | Actual | Status |
|---|---|---|---|
| [KPI 1 — e.g. Follower growth] | [target] | [actual] | 🟢 / 🟡 / 🔴 |
| [KPI 2 — e.g. Engagement rate] | [target] | [actual] | 🟢 / 🟡 / 🔴 |
| [KPI 3 — e.g. Reach] | [target] | [actual] | 🟢 / 🟡 / 🔴 |
| [KPI 4 — e.g. Enquiries] | [target] | [actual] | 🟢 / 🟡 / 🔴 |
| [KPI 5 — e.g. Website clicks] | [target] | [actual] | 🟢 / 🟡 / 🔴 |

**Visual Direction:** Full-width table with traffic light status column. Header row in brand primary colour. Alternating row shading. Bold the KPI names. Status column uses clear colour-coded dots or emoji traffic lights. Keep font size legible at presentation distance.

---

**Slide 4 — Platform-by-Platform Performance**
**Headline:** Each platform tells a different story — here is what the data shows
**Bullets:**
- [Platform 1]: [2–3 key metrics] — [1-sentence insight: what the data means for this platform]
- [Platform 2]: [2–3 key metrics] — [1-sentence insight]
- [Platform 3 if applicable]: [2–3 key metrics] — [1-sentence insight]
**Speaker Notes:** Spend 60–90 seconds per platform. Explain trends — is engagement improving, flat, or declining? Is reach growing as content volume grows, or has growth plateaued? For any platform that significantly underperformed, indicate that Slide 8 (strategy assessment) will address whether to continue or adjust the approach. Note any platform changes during the quarter (algorithm updates, new features introduced).
**Visual Direction:** One section per platform with a clear heading and the platform logo beside it. Each section: three metric chips (follower growth, reach, engagement rate) in brand accent boxes, followed by the insight sentence in italics. Dividing lines between platforms. Clean, white background. Scannable layout.

---

**Slide 5 — Audience Growth and Engagement Trends**
**Headline:** The audience is changing — here is who is engaging with the brand now
**Bullets:**
- Growing segments: [demographic or interest groups gaining share — e.g. "Women aged 25–34 in Kampala now represent 38% of Facebook followers, up from 29%"]
- Declining segments: [any segments losing share or engagement — e.g. "Male 35–44 segment engagement dropped by 12% — likely reflecting content mix"]
- New follower sources: [where new followers are discovering the account — e.g. "35% of new Instagram followers found the account via Reels — up from 8% last quarter"]
**Speaker Notes:** Audience data is where strategy earns its credibility. Show the client how the audience is responding to the content. If a growing segment is a valuable one, suggest doubling down. If the audience is drifting away from the target persona, flag it. Reference the audience personas established in 03-audience-personas and assess whether they still reflect the actual audience.
**Visual Direction:** Three horizontal sections: Growing (green accent), Declining (amber accent), New Sources (blue accent). Each with a one-sentence finding and a supporting data point. If platform analytics provide demographic charts (Facebook Insights), add a note to include a screenshot. Clean, insight-led layout.

---

**Slide 6 — Content Performance Analysis**
**Headline:** The data tells us clearly what content the audience values most
**Bullets:**
- Best-performing pillar (by reach): [Pillar name] — [reach figure] — [1-sentence reason]
- Best-performing pillar (by engagement): [Pillar name] — [engagement rate] — [1-sentence reason]
- Best-performing format: [e.g. short video / carousel / single image] — [metric] — [1-sentence reason]
- Underperforming pillar: [Pillar name] — [metric] — [1-sentence reason or hypothesis]
**Speaker Notes:** Connect every finding to a strategic implication. "The [pillar] pillar drove the most reach because [reason] — this tells us [implication for Month 4+]." Reference the Hero/Hub/Hygiene content model (YouTube/Google) if relevant — which content is driving discovery (Hero), which is building loyalty (Hub), and which is maintaining consistency (Hygiene). This analysis directly informs Slide 11 (content pillar refresh).
**Visual Direction:** Pillar performance cards — one per pillar — with a simple bar or dot indicator showing relative performance. Highlight the top performer in brand primary colour. Flag the underperformer in amber. Below the pillar cards, add a format comparison — a simple horizontal bar chart showing reach by format type (video, image, carousel, story). Clean, data-led layout.

---

**Slide 7 — Competitor Snapshot**
**Headline:** The competitive landscape shifted this quarter — here is what to know
**Bullets:**
- [Competitor 1]: [1–2 observations about what changed — e.g. "Increased Facebook posting frequency to 14/week; appear to be testing video-first content"]
- [Competitor 2]: [1–2 observations — e.g. "Launched a LinkedIn company page in February — signals B2B intent"]
- Strategic implication: [what this means for [Client Name]'s approach — e.g. "Video-first on Facebook is becoming the category norm — our Reels test in Q2 is well-timed"]
**Speaker Notes:** The competitor snapshot is not about copying competitors — it is about understanding the context in which the client's content is received. Reference the competitive audit process (02-platform-audit). Keep observations factual and professional. If a competitor is doing something well that the client should consider, frame it as an opportunity, not a threat. If the client knows one of the competitors personally, be sensitive in how observations are presented.
**Visual Direction:** One section per competitor. Each section has the competitor name (anonymise if preferred — "Competitor A"), 2 bullet observations, and a "so what" implication in a coloured callout box. Use a neutral, professional colour scheme for competitor sections — avoid using the client's brand colour for competitor references.

---

**Slide 8 — Strategy Assessment**
**Headline:** Three things to keep doing, two to change, and one to test
**Bullets:**
- Keep doing: [thing 1 — specific practice that is generating results]
- Keep doing: [thing 2 — specific practice that is generating results]
- Keep doing: [thing 3 — specific practice that is generating results]
- Change: [thing 1 — specific practice that is underperforming with proposed adjustment]
- Change: [thing 2 — specific practice that is underperforming with proposed adjustment]
- Test: [something unclear — one thing to experiment with in Q(N+1)]
**Speaker Notes:** This is the pivot point of the deck — from "what happened" to "what changes." Apply the "keep / change / test" framework clearly. Be specific: not "improve content quality" but "replace static product posts with short video demonstrations on Facebook." Reference the RACE framework (Chaffey, 2024) to assess whether underperformance is at the Reach, Act, Convert, or Engage stage — this diagnoses where the strategy needs adjustment.
**Visual Direction:** Three columns: "Keep" (green header), "Change" (amber header), "Test" (blue header). Bullet points under each column. Simple, decisive layout. Brand-consistent colours for headers. This slide should feel like a clear, confident assessment — not a list of problems.

---

**Slide 9 — Recommended Strategy Adjustments**
**Headline:** Three specific changes to the strategy starting [next quarter]
**Bullets:**
- Adjustment 1: [Change to platform mix, content pillar, or posting frequency] — Rationale: [1 sentence]
- Adjustment 2: [Change] — Rationale: [1 sentence]
- Adjustment 3: [Change] — Rationale: [1 sentence]
**Speaker Notes:** Present each adjustment as a data-driven recommendation, not a preference. State the evidence: "We are recommending [change] because [data point] showed us that [insight]." Invite the client to respond to each recommendation before moving on. If the client disagrees, record their perspective and note it — do not override their judgement on adjustments that affect their brand identity. Adjustments take effect at the start of [next quarter].
**Visual Direction:** Three recommendation cards, stacked or side by side. Each card: bold adjustment statement at top, rationale sentence below in lighter text, a small "evidence" data point in a coloured tag. Use a clean, authoritative layout. Green accent for confirmed adjustments after client approval.

---

**Slide 10 — New Opportunities Identified**
**Headline:** [Q(N+1)] presents [number] opportunities worth acting on
**Bullets:**
- [Opportunity 1 — e.g. "Instagram Broadcast Channels — now available in Uganda; test as a direct audience communication tool"]
- [Opportunity 2 — e.g. "Ramadan / seasonal moment — strong engagement uplift pattern in EA market; plan content series for [dates]"]
- [Opportunity 3 — e.g. "Partnership with [sector] influencer — audience overlap 62% with Persona 1; propose collaboration in Q2"]
**Speaker Notes:** Opportunities should be specific, timely, and actionable. Do not list generic trends — identify what is relevant for this client in this market at this time. Reference the Uganda/East African seasonal calendar for relevant moments: Independence Day (9 October), Christmas, Eid, Ugandan school terms, agriculture seasons (if applicable). Assign each opportunity to either "pursue in Q(N+1)" or "monitor for Q(N+2)."
**Visual Direction:** Opportunity cards with a star or arrow icon. Each card: opportunity title in bold, 1–2 sentence description, "Act in Q[N]" or "Monitor" label in a coloured tag. Optimistic, forward-looking colour palette — blues and greens. White background.

---

**Slide 11 — Proposed Content Pillars Refresh**
**Headline:** [Number] of [total] pillars remain strong — here is what changes and why
**Bullets:**
- Keep: [Pillar name] — [1-sentence rationale — performing above target, strong audience response]
- Keep: [Pillar name] — [1-sentence rationale]
- Modify: [Pillar name] → [New or adjusted name/focus] — [1-sentence rationale — underperforming or audience appetite has changed]
- Replace: [Pillar name] → [New pillar name] — [1-sentence rationale — no longer aligned with strategy or audience]
**Speaker Notes:** Pillar reviews are one of the highest-value outputs of a quarterly review. Connect every keep / modify / replace recommendation to the content performance data on Slide 6. If a pillar is being replaced, explain what gap the new pillar fills. If the client is attached to a pillar that is underperforming, present the data and ask: "Would you like us to test a modified version before we replace it entirely?"
**Visual Direction:** Two-column layout: "Current Pillars" on the left, "Proposed Pillars" on the right. Arrows connecting them — straight arrow = keep, curved arrow = modify, new entry = replace. Colour-coded: green = keep, amber = modify, red/new blue = replace. Clean, clear, decision-focused.

---

**Slide 12 — Campaign Recommendations for Next Quarter**
**Headline:** Two campaign opportunities for [Q(N+1)] that align with your goals
**Bullets:**
- Campaign 1: [Working title] — Objective: [1 sentence] — Concept: [1 sentence] — Timing: [dates]
- Campaign 2: [Working title] — Objective: [1 sentence] — Concept: [1 sentence] — Timing: [dates]
**Speaker Notes:** Campaign recommendations at the quarterly review are conceptual — not fully developed briefs. For each concept, explain why the timing is right (seasonal moment, product launch, audience data) and what success looks like in one metric. If the client wants to proceed with a campaign, use deck-campaign-proposal to develop the full brief. Note any production lead time requirements.
**Visual Direction:** Two campaign concept cards side by side. Each card: working title in bold, objective and concept in body text, timing displayed as a date bar at the bottom. Use distinct colours for the two campaigns. Clean, pitch-ready layout.

---

**Slide 13 — Budget Performance**
**Headline:** Here is how the investment was used this quarter
**Bullets:**
- Content creation: [amount or % of retainer — e.g. "45% — strategy, copywriting, and scheduling"]
- Reporting and analytics: [amount or % — e.g. "20% — monthly reports and this quarterly review"]
- Tools and subscriptions: [amount or % — e.g. "10% — scheduling and analytics tools"]
- Paid promotion (if applicable): [amount — e.g. "UGX 200,000 — Facebook boosted posts x4"]
- Total spend this quarter: [amount] vs. retainer total: [amount]
**Speaker Notes:** Budget transparency builds client trust. If there was underspend (common in early quarters as systems are built), explain what it will be used for in Q(N+1). If there was overspend, acknowledge it and explain the cause. If paid promotion produced strong results, use this slide to make the case for a dedicated paid media budget. Keep the tone factual — this is a professional accounting of value delivered.
**Visual Direction:** Horizontal bar chart or pie chart showing budget allocation by activity. Each segment labelled with activity type and percentage. Total spend vs. retainer displayed as a simple comparison below. Professional, finance-appropriate design. No fussy decoration — this is a business slide.

---

**Slide 14 — Next Quarter Roadmap**
**Headline:** [Q(N+1)] — month by month, here is the plan
**Bullets:**
- [Month 1 of next quarter]: [2–3 priorities — e.g. "Launch refreshed content pillars / Begin Campaign 1 pre-launch teaser / Instagram Reels test"]
- [Month 2]: [2–3 priorities — e.g. "Campaign 1 live / Quarterly content calendar published / Audience growth push on [platform]"]
- [Month 3]: [2–3 priorities — e.g. "Campaign 1 close-out and reporting / Prepare Q(N+1) review / Test new pillar content mix"]
**Speaker Notes:** This roadmap connects the strategy adjustments (Slide 9) and campaigns (Slide 12) to a specific timeline. Walk through it month by month. Highlight any client actions required (asset delivery, approvals, events). Confirm which items need client sign-off before the next quarter begins. This slide is a commitment — both the agency and the client should leave with a shared understanding of what happens next.
**Visual Direction:** Three-column layout — one column per month of the quarter. Month label as column header in brand primary colour. 2–3 priority bullets per column. Horizontal flow arrow across the top. Clean, clear, action-oriented.

---

**Slide 15 — Proposed Next Quarter Priorities**
**Headline:** Three strategic priorities for [Q(N+1)]
**Bullets:**
- Priority 1: [Stated clearly as an outcome — e.g. "Grow Facebook reach to 25,000 accounts/month through video-first content"]
- Priority 2: [Stated as an outcome — e.g. "Establish Instagram as a lead generation channel — 15 enquiries/month by end of Q2"]
- Priority 3: [Stated as an outcome — e.g. "Launch and complete Campaign 1 — achieve 5,000 campaign-specific reach and 200 link clicks"]
**Speaker Notes:** These three priorities are the strategic contract for [Q(N+1)]. They should be agreed by both the agency and the client before the end of this meeting. They become the targets on Slide 3 of the next quarterly review. Apply SMART criteria: every priority should have a specific metric, a timeframe, and a clear definition of success. Ask the client: "Do these three priorities reflect what matters most to your business in [next quarter]?"
**Visual Direction:** Three large priority cards, displayed prominently — one per priority. Each card: a priority number (01, 02, 03) in very large type, the outcome statement in bold below. Brand primary and secondary colours. This slide should feel ambitious and decisive.

---

**Slide 16 — Questions and Next Steps**
**Headline:** Three actions to complete before [next quarter] begins
**Bullets:**
- Action 1: [Specific action — owner (agency or client) — date] e.g. "Agency delivers revised content pillar document — [date]"
- Action 2: [Specific action — owner — date] e.g. "Client provides approval on Campaign 1 concept — [date]"
- Action 3: [Specific action — owner — date] e.g. "Agency publishes Q(N+1) content calendar — [date]"
- Next quarterly review: [Q(N+1) review date placeholder]
**Speaker Notes:** Do not leave the room without three agreed actions. Write them on the slide or in the notes during the meeting if they change. Confirm the next quarterly review date. Ask: "Is there anything from today's session that you would like us to follow up on in writing?" Send a one-page meeting summary email within 24 hours with the three actions and who owns them.
**Visual Direction:** Three action cards with owner labels (agency badge vs. client badge) and date tags. Next review date displayed in a clear box at the bottom. Clean, professional close. Brand colours. No data — this is a relational, action-focused close.

---

## Persuasion Frameworks

Apply frameworks from `references/presentation-frameworks.md` when generating this deck.

Key principles for quarterly reviews:
- The opening slide states the quarter's headline result in one sentence — the single most important business outcome (Duarte: Big Idea)
- Every results slide title is a complete assertion with the number: "WhatsApp enquiries grew 64% this quarter" not "WhatsApp performance" (Duarte: Big Idea per slide)
- Apply the Executive 10% Rule — the first two slides carry the full summary; the rest are evidence for those who want to go deeper (Duarte)
- Close with the next quarter's focus and a decision slide — the Sparkline closes with What Could Be, not What Was (Duarte: Sparkline + Hatton: Persuasion Sandwich)
- Frame all results in terms of business value to the client: revenue attributed, customers generated, cost per enquiry (Hatton: Empathy Model)

Read `references/presentation-frameworks.md` for the full framework guide.

---

## Quality Criteria

- All 16 slides have complete Headline, Bullets, Speaker Notes, and Visual Direction — no field is empty
- Slide 3 (progress vs. targets) uses traffic light coding and covers every KPI set in the original strategy — no metric is omitted or added without explanation
- Slide 8 (strategy assessment) uses the "keep / change / test" framework specifically — not vague observations
- Strategy adjustments on Slide 9 each include a one-sentence data-based rationale — no recommendation is unsupported
- Pillar refresh on Slide 11 connects directly to content performance data on Slide 6 — changes are evidence-based
- Campaign recommendations on Slide 12 are conceptual but specific: each has a named objective, a one-sentence concept, and a timing
- The three priorities on Slide 15 are SMART outcomes — not activity descriptions
- The deck flows as a coherent narrative: accountability (Slides 1–7), assessment (Slides 8–9), forward planning (Slides 10–16)
