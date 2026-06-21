---
name: deck-annual-review
description: Generates an 18-slide annual performance and strategy refresh presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill at the end of Year 1 of a client engagement when presenting the full-year review and proposing the Year 2 retainer renewal. This is the highest-stakes deck the consultant presents — it must make the client feel the year was well-invested and excited about Year 2.
---
# Annual Review and Year 2 Strategy Deck

<!-- dual-compat:start -->
## Use when
- Generates an 18-slide annual performance and strategy refresh presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill at the end of Year 1 of a client engagement when presenting the full-year review and proposing the Year 2 retainer renewal. This is the highest-stakes deck the consultant presents — it must make the client feel the year was well-invested and excited about Year 2.
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

This skill generates an 18-slide annual performance review and Year 2 strategy presentation. The annual review serves two purposes: demonstrating the value delivered in Year 1, and proposing the direction and investment for Year 2.

Structure the deck in two distinct halves: Year 1 in review (Slides 1–10), and Year 2 direction (Slides 11–18). The client should feel proud of Year 1 and energised about Year 2 before the renewal proposal appears.

This is the highest-stakes deck in the consultancy lifecycle. Prepare it with care. Populate every data field with actual client figures. Never present this deck with placeholder text remaining.

Output is paste-ready markdown. Transfer each slide into PowerPoint, Canva, or Google Slides.

---

## Required Input

Collect all of the following before generating the deck. Ask for any missing items.

- **Client name** and industry
- **Country/city** (default: Uganda/East Africa)
- **Primary goal** agreed at the start of Year 1
- **Year being reviewed** (e.g. Year 1: January–December 2025)
- **All 12-month platform metrics**: monthly follower counts (Jan–Dec) per platform, total annual reach, total annual impressions, average annual engagement rate per platform, total enquiries or leads generated
- **Original Year 1 goals** — as stated in the strategy document (05-social-media-strategy)
- **Top 5 content pieces** — for each: platform, format, the metric achieved, one-sentence learning
- **Campaign list** — all campaigns run in the year, with timing and primary result per campaign
- **Brand voice evolution** — how the brand's tone and style changed over the year
- **Competitor observations** — 2–3 observations about what competitors did during the year
- **Year 2 strategy direction** — the proposed direction and focus for Year 2 (from a strategy refresh or the consultant's recommendation)
- **Year 2 KPI targets** and stretch targets
- **Year 2 campaign calendar** — 4 planned campaign windows mapped to Q1–Q4
- **Retainer renewal proposal** — current Year 1 fee, proposed Year 2 fee, scope changes, value justification
- **Consultant name** and contact details

---

## Slide Generation

Generate all 18 slides in full. Write every field. Replace all bracketed placeholders with actual client data before presenting.

---

**Slide 1 — Title**
**Headline:** [Client Name] — Year 1 in Review and Year 2 Strategy — [Year]
**Bullets:**
- Prepared by [Consultant Name]
- Presented on [date]
- Year in review: [January – December Year]
**Speaker Notes:** Open with genuine warmth and appreciation. "Before we look at the data, I want to say something: this has been a genuinely good year of working together. What I am going to share today is the story of what we built in [Year] and where we are going in [Year 2]." Set the tone — this meeting is a celebration and a strategy session in equal measure. Allow 90–120 minutes.
**Visual Direction:** Full-bleed brand colour. Client logo and agency logo prominently placed. Year in large type — the year number should feel significant. Consultant name below. Authoritative, celebratory, and confident — the most polished cover of all the deck skills.

---

**Slide 2 — Year in Numbers**
**Headline:** Five numbers that define what [Client Name] achieved on social media in [Year]
**Bullets:**
- Total reach achieved: [figure — e.g. "847,000 accounts reached across all platforms"]
- Follower growth: [net change — e.g. "+3,420 followers — from [start] to [end]"]
- Best engagement rate: [e.g. "4.6% — Facebook, October — the highest single-month rate of the year"]
- Enquiries / leads generated: [e.g. "312 WhatsApp and DM enquiries directly attributed to social content"]
- Top platform: [e.g. "Facebook — 68% of total annual reach"]
**Speaker Notes:** Display these numbers with pride. Read each one aloud with a brief comment. The annual totals should feel significant — even modest monthly numbers accumulate into impressive annual figures. Connect the headline metrics to the business: "312 enquiries from social — at your current conversion rate, that represents approximately [X] new customers and [UGX value] in revenue." Pause after the revenue figure.
**Visual Direction:** Five very large-number cards on a bold background. Each number dominates its card — the metric label is small below it. Brand primary colour for the card backgrounds or the numbers. This slide should feel like a statement — bold, clean, celebratory. Full-bleed or near-full-bleed layout with generous whitespace.

---

**Slide 3 — Goals We Set vs. Results We Achieved**
**Headline:** Here is an honest account of every goal we set at the start of [Year]
**Bullets:**
- See table below — met and exceeded goals are celebrated; missed goals are explained with cause and learning
**Speaker Notes:** This slide establishes credibility through honesty. Present it directly: "Not every target was hit — I want to be transparent about that. Where we fell short, I will explain why and what we learned." Do not minimise missed targets or make excuses. An honest assessment of a missed goal, paired with a clear learning and a Year 2 adjustment, is more valuable to the client than an unacknowledged shortfall. Spend more time on the goals that were exceeded — these are the wins.

| Goal | Target | Actual | Status | Note |
|---|---|---|---|---|
| [Goal 1] | [target] | [actual] | 🟢 Achieved | [brief note] |
| [Goal 2] | [target] | [actual] | 🟢 Exceeded | [brief note] |
| [Goal 3] | [target] | [actual] | 🟡 Partially achieved | [cause in 5 words] |
| [Goal 4] | [target] | [actual] | 🔴 Missed | [cause + learning] |

**Visual Direction:** Full-width table with a "Note" column for brief context. Traffic light status column. Header row in brand primary colour. Bold the "Exceeded" rows — these are the highlights. The "Missed" rows should have the note column filled in with a cause and a learning. Professional, honest, clear.

---

**Slide 4 — Platform-by-Platform Performance Trends**
**Headline:** Twelve months of data — here is how each platform performed
**Bullets:**
- [Platform 1]: [Follower count Jan vs. Dec] / [average monthly reach] / [average engagement rate] — [1-sentence trend insight: e.g. "Consistent growth with a strong surge in Q3 driven by the back-to-school campaign"]
- [Platform 2]: [same format] — [1-sentence trend insight]
- [Platform 3 if applicable]: [same format] — [1-sentence trend insight]
**Speaker Notes:** Describe the chart on this slide: "This line graph shows follower count month by month on [Platform 1] — you can see the growth curve from [start] to [end], with a clear spike in [month] when we ran [campaign or content moment]." Annotate the key moments on the line — campaign launches, algorithm changes, high-performing content months. Show the trend clearly — even flat months have a story.
**Visual Direction:** One section per platform. Each section contains a described line graph (label it: "Line graph — [Platform] follower count, January–December [Year]"). Below the chart description: three key metrics in large-number chips. Trend insight in italics. Clean, data-forward layout. Dividing lines between platform sections. If actual chart data is available, insert the screenshot and annotate it.

---

**Slide 5 — Audience Growth Story**
**Headline:** The [Client Name] social media audience today is different from — and better than — 12 months ago
**Bullets:**
- Who is following now: [demographic or interest profile — e.g. "The Facebook audience is now 54% women aged 25–44 in Kampala — closer to Persona 1 than at any point in the year"]
- What changed: [2 specific shifts — e.g. "Male 18–24 segment grew 22% following TikTok-style Reels content" / "Follower source shifted: 40% now discover the brand via shared posts rather than direct search"]
- What this means: [strategic implication — e.g. "The audience is becoming more targeted and more engaged — a smaller, more relevant audience is more valuable than a large, passive one"]
**Speaker Notes:** The audience story is about quality, not just quantity. A brand that has grown 1,200 highly targeted followers is in a stronger position than one that has grown 5,000 mismatched followers. Celebrate audience quality improvements even if quantity growth was modest. Reference the original personas (03-audience-personas) and assess whether the audience now more closely reflects the target persona than it did at the start of the year.
**Visual Direction:** Two-column layout. Left: "12 months ago" audience snapshot (key demographic data from January). Right: "Today" audience snapshot (December data). A brief "What changed" section below with two bullet points. Use a before/after visual metaphor — simple and legible. If platform demographics screenshots are available, include them with annotations.

---

**Slide 6 — Top 5 Content Pieces of the Year**
**Headline:** Five posts that defined what [Client Name]'s audience responds to
**Bullets:**
- Post 1: [Platform] / [Format] / [Key metric — e.g. "Reached 18,400 accounts"] / Learning: [1 sentence — e.g. "Educational carousel posts outperform all other formats for saves and shares"]
- Post 2: [Platform] / [Format] / [Key metric] / Learning: [1 sentence]
- Post 3: [Platform] / [Format] / [Key metric] / Learning: [1 sentence]
- Post 4: [Platform] / [Format] / [Key metric] / Learning: [1 sentence]
- Post 5: [Platform] / [Format] / [Key metric] / Learning: [1 sentence]
**Speaker Notes:** These five posts are evidence — they define the content strategy for Year 2. Spend time on each one. Ask the client: "Do you remember when this post went out? Do you know why it performed so well?" Client recall of top-performing content is a strong engagement signal — it shows they are paying attention. The five learnings from this slide feed directly into the Year 2 content pillar refresh on Slide 14.
**Visual Direction:** Five content cards stacked or in a grid. Each card: post number (01–05), platform icon, format label, metric displayed prominently in brand accent colour, learning statement below in italics. If post screenshots are available, include a small thumbnail on the card. The top post (highest metric) should be visually prominent — larger card or bold accent.

---

**Slide 7 — Brand Voice Evolution**
**Headline:** The [Client Name] brand voice is stronger, more distinctive, and more consistent than it was 12 months ago
**Bullets:**
- 12 months ago: [honest description of the brand voice at the start — e.g. "Posts were inconsistent — sometimes formal, sometimes casual, with no clear tone of voice or personality"]
- Today: [description of the current brand voice — e.g. "Warm, knowledgeable, and direct — the brand sounds like a trusted expert who speaks plainly"]
- What drove the change: [1–2 factors — e.g. "Introduction of brand voice guidelines in Q1 / Consistent use of the 'educator' content pillar / Client team trained on tone of voice"]
**Speaker Notes:** Brand voice evolution is a qualitative achievement — it cannot always be measured in a metric, but clients feel it. Show the contrast by reading one early post and one recent post aloud (with client permission). The difference should be audible. Reference the brand voice intake (04-brand-voice-intake) and the east-african-english language standard. This slide also validates the strategic investment in consistent content — voice consistency builds brand recognition and trust over time (Kotler et al., 2023).
**Visual Direction:** Two-column layout: "Then" (left, muted colours) and "Now" (right, brand primary colour). A brief quote or sentence example from an early post and a recent post for contrast. "What drove the change" section below. Simple, visual, evocative. The "Now" column should feel more confident and distinct than the "Then" column.

---

**Slide 8 — Campaigns**
**Headline:** [Number] campaigns ran in [Year] — here is what each one achieved
**Bullets:**
- See table below

| Campaign | Period | Objective | Primary result |
|---|---|---|---|
| [Campaign 1 name] | [Month–Month] | [1-sentence objective] | [Key metric — e.g. "2,800 reach / 47 enquiries"] |
| [Campaign 2 name] | [Month–Month] | [1-sentence objective] | [Key metric] |
| [Campaign 3 name if applicable] | [Month–Month] | [1-sentence objective] | [Key metric] |

**Speaker Notes:** Walk through each campaign row. For the best-performing campaign, spend an extra 30 seconds explaining why it worked. For any campaign that underperformed its target, acknowledge it briefly and state what was learned. Note the aggregate campaign impact: "Across all [X] campaigns this year, the combined additional reach was [figure] and the campaigns generated [X] additional enquiries beyond the baseline." Campaigns are the most visible work the client sees — celebrate them.
**Visual Direction:** Full-width table with clear columns. Campaign names in bold. The best-performing campaign row highlighted in brand accent colour. Period column shows months as a visual bar or date range. Clean, professional, easy to read at a glance.

---

**Slide 9 — Competitor Landscape**
**Headline:** The market moved in [Year] — here is what changed around [Client Name]
**Bullets:**
- [Competitor 1]: [1–2 observations — what they did in the year, e.g. "Grew Facebook following from ~800 to ~2,100 — likely boosted content, judging by reach patterns"]
- [Competitor 2]: [1–2 observations — e.g. "Launched Instagram account in May but posting has been inconsistent — no clear strategy visible"]
- Implication for [Client Name]: [1–2 sentences — how the competitive landscape affects Year 2 strategy — e.g. "[Client Name] now has a content quality advantage — sustaining this in Year 2 is a strategic priority"]
**Speaker Notes:** The competitor analysis contextualises the client's performance — good numbers mean more when the market context is understood. Keep observations professional and factual. If a competitor is outperforming the client in a particular area, acknowledge it and connect it to the Year 2 strategy as an opportunity. Reference 02-platform-audit for the full competitive audit methodology. Anonymise competitors if the client prefers.
**Visual Direction:** One section per competitor, then a "Implication" section at the bottom. Each competitor section has the competitor name (or "Competitor A/B") and 2 bullet observations. The implication section uses a callout box in brand accent colour. Professional, neutral design for competitor sections.

---

**Slide 10 — What We Learned About Your Audience**
**Headline:** Four audience insights that will shape [Client Name]'s strategy in Year 2
**Bullets:**
- Insight 1: [Specific data-backed finding — e.g. "The audience responds most strongly to content that shows real people — not products alone. Posts featuring team members or customers consistently outperformed product-only posts by 2×"]
- Insight 2: [e.g. "Educational content drives saves and shares — the highest-save posts of the year were all from the 'Expert Advice' pillar. The audience saves content they plan to act on."]
- Insight 3: [e.g. "Posting before 07:30 EAT consistently outperformed midday posts — the audience is most active in the commute and early morning window"]
- Insight 4: [e.g. "WhatsApp enquiries spike within 48 hours of a Facebook post with a direct CTA — the path from content to enquiry is short and reliable"]
**Speaker Notes:** These four insights are the intellectual output of a year of work. They are specific, evidence-based, and actionable. Each insight should lead the client to say "that makes sense" or "I had not thought of it that way." Connect every insight to a Year 2 decision: "Because the audience saves educational content, we are going to invest more in the Expert Advice pillar in Year 2." Insights without implications are observations — with implications, they become strategy.
**Visual Direction:** Four insight cards, each with a number (01–04) in large type, the insight statement bold at the top, and a supporting data point or example below in smaller text. Brand accent colour for the numbers. White card backgrounds. Generous whitespace. These cards should feel like intellectual deliverables — worth framing.

---

**Slide 11 — Channels to Grow in Year 2**
**Headline:** Invest more here in Year 2 — the data shows where the opportunity is
**Bullets:**
- [Platform 1 to grow]: [2–3 sentences — why: audience data, engagement trend, untapped content format, or emerging platform opportunity in Uganda/East Africa]
- [Platform 2 to grow if applicable]: [same format]
- Investment implication: [what "investing more" means — more content, more paid media, a new content format, a new content series]
**Speaker Notes:** Connect the platform growth recommendation to audience data from the year. "We are recommending more investment in [Platform] because [metric] shows [insight] and we believe [opportunity]." Be specific about what "more" means — more posts per week, a new format like Reels, a paid media test. If a platform that was not active in Year 1 is being proposed for Year 2, explain the case clearly with reference to the Ugandan/East African market context.
**Visual Direction:** Platform logo(s) displayed prominently. For each platform: growth rationale as bullet points, and an "investment implication" label at the bottom of the section. Use an upward arrow motif to signal growth. Brand optimistic colours — green or blue. Clean, forward-looking.

---

**Slide 12 — Channels to Reduce or Exit**
**Headline:** Not every platform deserves the same investment in Year 2
**Bullets:**
- [Platform to reduce/exit]: [2–3 sentences — why: low ROI, audience mismatch, low engagement despite consistent effort, resource cost not justified by returns]
- What "reduce" means: [specific — e.g. "Reduce from 5 posts per week to 2 — maintain brand presence but redirect creative energy to [Platform to grow]"]
- What "exit" means (if applicable): [e.g. "Archive the account and redirect the audience via a final post to [primary platform] — this is a strategic decision, not an abandonment"]
**Speaker Notes:** This is a bold recommendation — clients sometimes resist it, especially if they feel personally attached to a platform. Present the data clearly: "Despite consistent effort, [Platform] generated [X]% of our reach on [X]% of our content effort. Reducing investment here and redirecting it to [Platform] is a more efficient use of the budget." Be prepared to show the comparison. If the client wants to keep the platform, propose a reduced investment level rather than arguing for full exit.
**Visual Direction:** Platform logo displayed in muted/greyscale to signal reduced status. Rationale as bullet points below. "What this means" as a clear, plain-language statement in a bordered box. Honest, professional design — this is not a failure slide, it is a smart allocation decision.

---

**Slide 13 — Year 2 Strategy Statement**
**Headline:** [One bold sentence: where [Client Name] is going on social media in Year 2 and why]
**Bullets:**
- Foundation established: [What Year 1 built — the platform, the voice, the audience — that Year 2 builds on]
- Year 2 shift: [What changes — the emphasis, the ambition, the new capability being added]
- The outcome: [What the client will have at the end of Year 2 that they do not have today]
**Speaker Notes:** This is the strategic pivot point of the deck. The Year 2 strategy statement is a declaration — one sentence that the client can repeat to their team, their board, or their stakeholders. Spend time crafting it. Read it aloud in the meeting. Ask the client: "Does this capture where you want to take the brand in Year 2?" Make adjustments if needed — this is a collaborative statement, not a consultant's decree.
**Visual Direction:** Strategy statement in very large, bold type — centred on the slide. It should be the only large-text element. Three smaller bullet points below in a clean row. Brand primary colour for the statement. White background. Simple, decisive, memorable. This slide should feel like a manifesto.

---

**Slide 14 — Content Pillar Refresh**
**Headline:** Year 2 content strategy: [number] pillars to keep, [number] to adjust, [number] to introduce
**Bullets:**
- Keep: [Pillar name] — [1-sentence rationale — strong performance in Year 1, audience clearly values this content]
- Keep: [Pillar name] — [1-sentence rationale]
- Adjust: [Current pillar name] → [Adjusted name/focus] — [1-sentence rationale — audience appetite has evolved, or Year 2 goals require a shift in emphasis]
- Introduce: [New pillar name] — [1-sentence rationale — gap identified in Year 1 data, new business priority, or audience insight from Slide 10]
**Speaker Notes:** Connect every pillar decision to evidence: the top 5 content pieces (Slide 6), the audience insights (Slide 10), and the Year 2 strategy direction (Slide 13). If introducing a new pillar, explain the gap it fills. If retiring a pillar, show the performance data that supports the decision. The client should leave this slide knowing exactly what content will be created in Year 2 and why.
**Visual Direction:** Two-column layout: "Year 1 Pillars" (left) and "Year 2 Pillars" (right). Arrows connecting them — straight = keep, curved = adjust, new entry = introduce, no arrow from left = retired. Colour-coded status: green = keep, amber = adjust, blue = new. Clean, clear, decision-focused.

---

**Slide 15 — Year 2 KPI Targets**
**Headline:** Year 2 targets are set to be ambitious and achievable — with a stretch goal for each
**Bullets:**
- See table below — targets are based on Year 1 actual performance and Year 2 strategy direction

| KPI | Year 1 Actual | Year 2 Target | Stretch Target |
|---|---|---|---|
| [KPI 1 — e.g. Follower growth] | [Year 1 actual] | [Year 2 target] | [Stretch] |
| [KPI 2 — e.g. Engagement rate] | [Year 1 actual] | [Year 2 target] | [Stretch] |
| [KPI 3 — e.g. Monthly reach] | [Year 1 actual] | [Year 2 target] | [Stretch] |
| [KPI 4 — e.g. Enquiries/month] | [Year 1 actual] | [Year 2 target] | [Stretch] |
| [KPI 5 — e.g. Website clicks] | [Year 1 actual] | [Year 2 target] | [Stretch] |

**Speaker Notes:** Walk through the table column by column — Year 1 actual first (so the client sees the baseline), then Year 2 target (the standard), then stretch target (the ambition). Explain the rationale for each target: "We achieved [X] in Year 1. With the Year 2 strategy adjustments and an additional investment in [channel], we are targeting [Y]. If everything goes well, [stretch target] is achievable." Apply SMART criteria — all targets must have a timeframe (annual or quarterly milestone).
**Visual Direction:** Clean three-column table with a Year 1 / Year 2 / Stretch structure. Year 2 target column in brand primary colour — this is the commitment. Stretch column in a lighter shade or secondary colour — this is the aspiration. Bold the target column header. Professional, data-forward.

---

**Slide 16 — Year 2 Campaign Calendar Preview**
**Headline:** Four campaign windows in Year 2 — here is where the biggest opportunities are
**Bullets:**
- Q1 [months]: [Campaign name or theme] — [Objective in 1 sentence] — [Key dates or moment]
- Q2 [months]: [Campaign name or theme] — [Objective in 1 sentence] — [Key dates]
- Q3 [months]: [Campaign name or theme] — [Objective in 1 sentence] — [Key dates]
- Q4 [months]: [Campaign name or theme] — [Objective in 1 sentence] — [Key dates — e.g. Christmas, end-of-year]
**Speaker Notes:** The Year 2 campaign calendar gives the client a picture of the full year — four distinct campaign moments mapped to business priorities and seasonal opportunities. These are concepts, not full briefs — when each campaign approaches, use deck-campaign-proposal to develop it. Reference the Uganda/East African annual calendar: Ugandan Independence Day (October), school terms, Ramadan and Eid (dates vary), Christmas and New Year, Valentine's Day, agricultural seasons where relevant.
**Visual Direction:** Horizontal annual timeline with four campaign windows marked as coloured bands. Q1/Q2/Q3/Q4 labels above. Each campaign window has the campaign name, objective, and key dates below the timeline. Campaign accent colours — one per campaign (four distinct colours). A visual calendar that the client can picture at a glance. Forward-looking, energetic layout.

---

**Slide 17 — Investment Recommendation for Year 2**
**Headline:** Year 2 investment: [amount] — here is what changes and why it represents value
**Bullets:**
- Year 1 retainer: [amount] / Year 2 proposed retainer: [amount]
- What changes in Year 2: [scope additions or adjustments — e.g. "Addition of Instagram Reels production (2/month) / Quarterly paid media test budget (UGX [X]/quarter)"]
- What stays the same: [core services that continue — e.g. "Strategy, content creation, scheduling, community management, monthly reporting, quarterly reviews"]
- Value justification: [connect the fee to the Year 1 results — e.g. "Year 1: 312 enquiries generated at a cost of UGX [X] per enquiry — Year 2 target: 480 enquiries at a cost of UGX [X] per enquiry — 35% more efficient"]
**Speaker Notes:** Present the Year 2 fee with confidence and context. Ground it in Year 1 results: "Here is what last year's investment produced. Here is what Year 2's investment will build on that." Apply the ROI formula (Bodnar and Cohen, 2012): (TLV − COCA) ÷ COCA. If the fee is increasing, explain why the additional scope justifies the increase. If the fee is the same, note what the client is getting for the same investment. Have the Year 2 service agreement ready to share after the meeting.
**Visual Direction:** Clean comparison table: Year 1 fee vs. Year 2 fee in two columns. Scope changes listed below. Value justification in a coloured callout box — framed as "what this investment produces." Professional, confident, finance-appropriate. The Year 2 fee should look like a logical next step, not a demand.

---

**Slide 18 — Thank You and Next Steps**
**Headline:** [Client Name], it has been an honour to work alongside you in [Year] — let us make Year 2 even better
**Bullets:**
- Next step 1: [Action — owner — date — e.g. "Client confirms renewal of retainer — by [date]"]
- Next step 2: [Action — owner — date — e.g. "Agency delivers Year 2 strategy document — by [date]"]
- Next step 3: [Action — owner — date — e.g. "Q1 content calendar published — by [date]"]
- [Consultant Name] — [Email] — [Phone / WhatsApp] — [Website]
**Speaker Notes:** Close with genuine appreciation. In the East African professional and relational context, the closing of an annual review is a significant moment — it is worth acknowledging the relationship, not just the results. "Working with [Client Name] this year has been a genuine privilege. I have seen the brand grow, and I am proud of what we have built together." Then ask directly: "Are you ready to continue into Year 2?" Confirm all three next steps verbally. Send a follow-up email within 24 hours with the next steps and the service agreement attached.
**Visual Direction:** Full-bleed brand colour — bookending the cover slide. Large, warm closing statement. Three next step cards with dates and owner labels. Contact details in clean white text. Agency and client logos side by side. The most personal and relational slide in the deck — it should feel like the end of a chapter and the start of another.

---

## Persuasion Frameworks

Apply frameworks from `references/presentation-frameworks.md` when generating this deck.

Key principles for annual reviews:
- The Sparkline structure frames the year: What Was (Year 1 baseline) → What Is Now (Year 1 results) → What Could Be (Year 2 direction) — the deck closes with the forward vision, not the backward summary (Duarte: Sparkline)
- The year's headline result appears in the first two slides in one sentence — the decision-maker should understand the value before seeing any analysis (Duarte: Executive 10% Rule)
- Every results slide title is a complete assertion: "Social media generated UGX 12 million in attributed revenue this year" not "Annual results" (Duarte: Big Idea per slide)
- The annual review is the most important credibility document in the client relationship — it must answer Hatton's Two Strategic Questions: why should they renew? and why will they remember this presentation?
- Close with the Year 2 proposal or recommendation, not a year-in-review summary — the Persuasion Sandwich bottom slice is a forward commitment (Hatton)

Read `references/presentation-frameworks.md` for the full framework guide.

---

## Quality Criteria

- All 18 slides have complete Headline, Bullets, Speaker Notes, and Visual Direction — no field is empty
- Slide 3 (goals vs. results) includes every Year 1 goal with actual results and a brief note on any missed targets — honesty is non-negotiable
- The top 5 content pieces on Slide 6 each include a one-sentence learning that is specific and actionable — not a generic observation
- Year 2 KPI targets on Slide 15 are derived from Year 1 actuals — they are ambitious but grounded in evidence, not arbitrary
- The Year 2 strategy statement on Slide 13 is a single, bold, memorable sentence — not a paragraph or a list
- Campaign calendar on Slide 16 references real Ugandan/East African seasonal and cultural moments (or the specified market) for at least two campaign windows
- The investment slide (Slide 17) includes a value justification that connects the Year 2 fee to Year 1 results using a specific metric (cost per enquiry, ROI, or comparable measure)
- The deck reads as two coherent halves: Year 1 accountability (Slides 1–10) and Year 2 direction (Slides 11–18) — the transition on Slide 11 should feel like a clear pivot from past to future
