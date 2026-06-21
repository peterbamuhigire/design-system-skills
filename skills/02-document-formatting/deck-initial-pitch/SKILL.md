---
name: deck-initial-pitch
description: Generates a 15-slide initial pitch presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke when a consultant has completed a client intake (01-client-brief) and needs to present their proposed approach to the prospective client before the engagement is signed. This deck is the live pitch — the biz-dev-proposal is the leave-behind document. Tone is confident, diagnostic, and client-centred — not a sales brochure.
---
<!-- dual-compat:start -->
## Use when
- Generates a 15-slide initial pitch presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke when a consultant has completed a client intake (01-client-brief) and needs to present their proposed approach to the prospective client before the engagement is signed. This deck is the live pitch — the biz-dev-proposal is the leave-behind document. Tone is confident, diagnostic, and client-centred — not a sales brochure.
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
- Read `references/pitch-psychology.md` when you need the deeper framework, examples, or supporting material it contains.
- Read `references/storytelling.md` when you need the deeper framework, examples, or supporting material it contains.

<!-- dual-compat:end -->

## Overview

This skill generates the initial pitch deck presented to a prospective client after intake and before signing. The deck demonstrates that the consultant has understood the client's situation, identifies the gap, proposes a strategic direction, and presents the engagement scope and investment. Slide sequencing follows: Situation → Gap → Stakes → Approach → Evidence → Scope → Investment → Decision. Output is paste-ready markdown; the consultant transfers slides into PowerPoint, Canva, or Google Slides.

---

## Required Input

Ask for all of the following before generating any slides:

- Client name and industry
- Country/city (default: Uganda/East Africa)
- Client's stated goals — verbatim from the intake brief
- Current platforms in use and what is not working (from 01-client-brief output)
- Primary audience as described by the client
- Key challenge or gap identified in the intake conversation
- Budget range (if disclosed during intake)
- One case study or comparable result from the agency's portfolio (for Slide 8)
- Consultant name and contact details (email, phone, WhatsApp)

---

## Slide Generation

Generate all 15 slides in full. Write every field. Apply the persuasion frameworks from `references/pitch-psychology.md` and `references/storytelling.md` throughout.

---

**Slide 1 — Title**
**Headline:** [Client Name] — A Social Media Proposal from [Agency Name]
**Bullets:**
- [Consultant Name], [Title]
- [Date]
- Prepared exclusively for [Client Name]
**Speaker Notes:** Frame-setting opening — arrive as a peer, not a supplicant. Do not open by thanking them for their time. Open with a brief peer-level observation about their market or sector. Keep this slide on screen for 30 seconds before moving forward.
**Visual Direction:** Full-bleed neutral or brand colour background; agency logo and client logo displayed together; clean, confident typographic design with generous white space.
**Persuasion Note:** Klaff — Frame Control. The frame is set in the first 30 seconds. Own the room before the first word of content.

---

**Slide 2 — Agenda**
**Headline:** Five conversations — from where you are today to what we propose together
**Bullets:**
- 01 What we heard
- 02 The gap
- 03 What it is costing you
- 04 Our recommended approach
- 05 The proposal
**Speaker Notes:** "This is a diagnostic conversation, not a sales presentation. We are here to show you what we have understood and what we would recommend. Please interrupt — your corrections make everything more accurate."
**Visual Direction:** Clean numbered list; one icon per agenda item; white background; restrained typography.
**Persuasion Note:** Hatton — Two Strategic Questions. Before presenting this deck you should have answered: Why should they say yes? and Why will they remember this meeting? Both should be visible in the opening.

---

**Slide 3 — What We Heard**
**Headline:** [Client Name], here is what stood out from our conversation
**Bullets:**
- [Verbatim goal or challenge from intake — use the client's own words]
- [Verbatim second point from intake]
- [Verbatim third point — platform frustration, audience gap, or growth ambition]
- [Verbatim fourth point if available]
**Speaker Notes:** Mirror back. Read slowly. Ask: "Does this capture your situation accurately? Is there anything we have missed or misunderstood?" Any correction here improves everything that follows. This slide builds more trust than any credential.
**Visual Direction:** Quote-style layout — each point as a brief statement on a card or list; client-focused, minimal agency branding; warm, attentive design.
**Persuasion Note:** Sant — Primacy Principle. The deck opens with the client's reality, not the agency's. Klaff — demonstrating you listened before pitching signals high status.

---

**Slide 4 — The Gap**
**Headline:** Where you are today versus where you want to be — the distance between them is the opportunity
**Bullets:**
- Where you are now: [current state from audit or intake — specific, measurable if possible]
- Where you want to be: [client's stated goals — specific, time-bound]
- The gap: [what is missing — capability, strategy, consistency, or platform presence]
**Speaker Notes:** Duarte's Sparkline lives here. Make the contrast concrete — not "your reach is low" but "your competitors are receiving X enquiries per month via social media while you are receiving Y. That gap is the opportunity." Pause after presenting the contrast. Let it land.
**Visual Direction:** Two-column layout — left column muted colours labelled "What Is"; right column brand-energised colours labelled "What Could Be"; clean contrast between the two states.
**Persuasion Note:** Duarte — Sparkline. The tension between What Is and What Could Be is the engine of the entire pitch. Do not rush this slide. The longer the client sits with the gap, the more motivated they are to close it.

---

**Slide 5 — The Opportunity Cost**
**Headline:** Every month without a strategy is a month your competitors extend their lead
**Bullets:**
- [Specific competitor activity or sector benchmark data for Uganda/EA — e.g. average enquiries generated per month by comparable businesses]
- [Platform penetration or usage statistic relevant to the client's audience]
- [Quantified cost of inaction — revenue, market share, or audience lost per month]
**Speaker Notes:** Klaff: Intrigue and Stakes. The purpose is not to frighten — it is to establish that inaction has a cost. "Every month you wait is a month your competitor is building an audience you cannot recover." If you have data on competitor social activity, use it here. Make the stakes specific and credible.
**Visual Direction:** One striking statistic displayed large and bold at centre; supporting context in smaller text below; high-contrast design — dark background, white text, single accent colour. This is the energy slide.
**Persuasion Note:** Klaff — Revealing the Intrigue (R in STRONG). This is the moment of productive urgency. Information must be novel and specific — the crocodile brain ignores generalities but responds to concrete, unexpected facts. This is the natural home of the S.T.A.R. moment (Duarte).

---

**Slide 6 — Our Recommended Approach**
**Headline:** Here is the strategic direction we recommend for [Client Name]
**Bullets:**
- Primary platform focus: [platform(s) aligned to the client's audience — e.g. Facebook and WhatsApp for broad Ugandan consumer reach]
- Content approach: [content pillar framework drawn from intake — e.g. educational, social proof, promotional in a 10-4-1 ratio]
- Audience targeting: [specific demographic and psychographic profile from intake]
- Primary 90-day goal: [one SMART objective — e.g. "Generate 40 qualified enquiries per month within 90 days"]
**Speaker Notes:** Sant: Outcome. State what success looks like before describing how to get there. "If this strategy performs as designed, in 90 days you should see [specific outcome]. Here is how we get there." Pause for reactions — this is where engaged clients start leaning forward.
**Visual Direction:** Three or four strategic recommendation cards — each with an icon and a one-sentence recommendation; confident, clean layout; brand colour accents.
**Persuasion Note:** Sant — NOSE framework, O (Outcome). Clients decide to pursue the outcome, not the method. State the destination clearly before showing the route. Duarte — this is the first full picture of What Could Be.

---

**Slide 7 — How We Work**
**Headline:** Here is what the working relationship looks like week to week
**Bullets:**
- Strategy — monthly direction set in advance with the client
- Content creation — posts, captions, and visuals produced to the approved calendar
- Scheduling and publishing — content goes live on time, every time
- Community management — comments, enquiries, and messages handled
- Monthly reporting and review — data reviewed together; strategy adjusted
**Speaker Notes:** Klaff: Prize Framing. "Our clients do not manage social media — we do. Your job is to approve content and brief us when things change in the business." Present the process as access to a system, not a service being sold. The agency is the resource the client needs — not the other way around.
**Visual Direction:** Circular or linear process flow — Strategy → Content → Publish → Measure → Optimise → Repeat; clean icons; brand colour; uncluttered layout.
**Persuasion Note:** Klaff — Offering the Prize (O in STRONG). The engagement is presented as a system with a proven return, not a cost. The agency holds the prize; the client is deciding whether to access it.

---

**Slide 8 — Why This Works**
**Headline:** We have done this before — here is a comparable result
**Bullets:**
- Client type and industry: [e.g. "A mid-sized hospitality business in Kampala"]
- The challenge: [brief one-sentence description of their situation before engagement]
- The approach: [one-sentence summary of what was done]
- The result: [specific, measurable outcome — numbers, percentages, or UGX revenue figures]
**Speaker Notes:** Sant: Evidence. Choose the case study that most closely mirrors this client's sector, size, and challenge. Be specific — "A similar client went from [X enquiries/month] to [Y enquiries/month] in [Z months] using a comparable approach." If you do not have an exact match, use the closest analogue and note it.
**Visual Direction:** Single case study card — challenge on the left, outcome on the right; result number displayed large; clean, credible, professional design.
**Persuasion Note:** Sant — Evidence (E in NOSE) is most persuasive when it mirrors the prospective client's situation directly. Klaff — Nailing the Hookpoint (N in STRONG): this is where engaged clients start asking "could you do this for us?" Watch for that signal.

---

**Slide 9 — Proposed Scope**
**Headline:** Here is exactly what we are proposing — what is included and what is not
**Bullets:**
- In scope: [list of included services — e.g. social media strategy, content calendar, post creation, community management, monthly reporting]
- Out of scope: [explicit exclusions — paid ad management, graphic design, video production, web development]
- Monthly deliverables: [what the client receives — e.g. 20 posts/month across 2 platforms, 1 strategy document, 1 report, 1 review meeting]
**Speaker Notes:** Read the out-of-scope list explicitly. "It is important we are aligned on what this engagement covers — these items are handled separately." Clarity here prevents every scope dispute later. Pause for questions. This slide is the contract in plain language.
**Visual Direction:** Two-column table — In Scope (left, green accent) / Out of Scope (right, neutral grey); monthly deliverables below as a clean bulleted list; professional and clear.
**Persuasion Note:** Hatton — Filling of the Persuasion Sandwich. Frame deliverables as benefits: "You receive X" not "We will do X." The client should leave this slide knowing exactly what they are buying.

---

**Slide 10 — Timeline**
**Headline:** Here is what the first 90 days look like
**Bullets:**
- Month 1: Strategy document delivered, brand onboarded, first content live within two weeks
- Month 2: Optimise based on early data, amplify what is working, first data review with client
- Month 3: Scale high-performing content, campaign launch if applicable, 90-day results review
**Speaker Notes:** Make it tangible. "In Month 1 you will see content go live within the first two weeks — before the end of the first month you will have a functioning social media presence." Connect each month to the outcomes on Slide 6. Confirm start date: "For a [start date], we need your brand assets and platform access by [date minus 7 days]."
**Visual Direction:** Three-column roadmap — one column per month; key milestones as bullets under each month label; horizontal flow arrow at the top; brand colours; clean and sequential.
**Persuasion Note:** Duarte — Sparkline resolution. The timeline is the bridge between What Is (today) and What Could Be (the 90-day outcome). Make each month feel achievable and clearly sequenced.

---

**Slide 11 — Investment**
**Headline:** Here is what this costs and what it is designed to return
**Bullets:**
- [Tier name — e.g. Growth Retainer]: UGX [amount]/month (approx. USD [equivalent])
- Includes: [brief list of what this tier covers]
- ROI projection: At [X]% enquiry-to-client conversion, [Y] monthly enquiries generates approximately UGX [revenue figure] — a [multiplier]× return on the monthly investment
- Payment terms: [e.g. monthly in advance; first month includes onboarding fee of UGX X]
**Speaker Notes:** Present with confidence — do not apologise for the fee. Connect the investment to the expected return: "At a conservative [X]% conversion rate, this investment returns [Y]× in new revenue." Reference the ROI formula: (TLV − COCA) ÷ COCA (Bodnar and Cohen, 2012). If the client challenges the fee, return to the return calculation, not the cost breakdown.
**Visual Direction:** Clean pricing table — line items on the left, amounts on the right; bold total line; ROI expectation in a coloured callout box below the table; professional, finance-appropriate design.
**Persuasion Note:** Klaff — Prize Framing at the price reveal. Present the ROI before the fee line if possible. The frame is investment, not cost. Maximum two options to avoid crocodile-brain paralysis.

---

**Slide 12 — What You Get**
**Headline:** Every month, here is what [Client Name] receives
**Bullets:**
- Social media strategy document (Month 1; updated quarterly)
- Monthly content calendar — approved in advance
- [X] posts published across [Y] platforms, on schedule
- Community management — comments, messages, and enquiries handled
- Monthly performance report with key metrics and recommendations
- Monthly review meeting (45 minutes) — strategy adjusted to data
**Speaker Notes:** Make deliverables concrete and visible. "You will receive these items every month, on time, without chasing." Clients often do not fully understand what they are buying until they see a list this specific. Specificity signals professionalism and reassures cautious decision-makers.
**Visual Direction:** Icon grid — one deliverable per icon with a brief label and one-line description; clean, reassuring layout; warm, professional colour palette.
**Persuasion Note:** Hatton — Physical Evidence principle. A detailed, specific deliverables list is itself a credibility signal. It demonstrates the agency operates with discipline and clarity, not improvisation.

---

**Slide 13 — What We Need From You**
**Headline:** Four things that make this work
**Bullets:**
- Brand access: platform credentials, logo files, and brand kit provided at kickoff
- Content approval within 24 hours of receiving the weekly calendar
- One designated point of contact for all approvals and briefings
- Monthly review meeting — 45 minutes; same time each month
**Speaker Notes:** Set expectations clearly. "These four things — especially the 24-hour approval window — are what allow us to keep the content calendar on track. Delays in approval push the posting schedule back." Confirm the point of contact in the room. Ask: "Is [name] the right person for approvals?"
**Visual Direction:** Four cards in a 2×2 grid; each card with an icon and a one-sentence requirement; slightly warmer colour palette to signal client responsibility; clean and direct.
**Persuasion Note:** Hatton — Empathy Model. Frame each requirement as enabling the client's own success: "The faster approvals come through, the better the results." Not as a condition of service — as a partnership mechanism.

---

**Slide 14 — Next Steps**
**Headline:** If you are ready to proceed, here is exactly what happens next
**Bullets:**
- Client reviews and signs service agreement — Client — by [date]
- Client provides brand assets and platform access — Client — by [date]
- Agency delivers kickoff pack and Month 1 content calendar — Agency — by [date]
- First content goes live — [specific date]
**Speaker Notes:** Ask directly: "Are you ready to move forward?" If hesitation: "On a scale of 1 to 10, how ready are you to address this today?" Anything below 7 — uncover the specific concern before discussing anything else. Create logical urgency: "If you sign this week, the first content goes live by [specific date]." Do not confuse logical urgency with pressure.
**Visual Direction:** Three or four sequential step cards; clear owner labels (Client / Agency); dates displayed prominently; decisive, clean design; forward-motion visual language.
**Persuasion Note:** Klaff — Getting the Decision (G in STRONG). The goal is a binary yes or no — not "we will think about it." Connect the decision directly to the outcome: saying yes today means [specific first milestone] by [specific date].

---

**Slide 15 — Q&A / Close**
**Headline:** [Client Name], let us build something excellent together
**Bullets:**
- [Consultant Name]
- [Email address]
- [Phone / WhatsApp number]
- [Website or portfolio link]
**Speaker Notes:** Close with energy and warmth. "I would love to hear what resonates and what questions you have — please be candid." Listen carefully; their questions reveal their real concerns. Take notes. Do not be defensive. Leave a printed one-page summary of the proposal. Confirm the next step before the client leaves the room.
**Visual Direction:** Full-bleed brand colour or high-quality professional lifestyle image; large closing statement as hero text; contact details below in clean white type; both logos at the bottom.
**Persuasion Note:** Duarte — S.T.A.R. moment option. If no S.T.A.R. moment was used earlier, close with a vivid, specific picture of what the client's world looks like in 12 months if this strategy works — make it personal to their stated goals.

---

## Persuasion Frameworks

Apply frameworks from `references/pitch-psychology.md` and `references/storytelling.md` throughout.

Key principles:
- Open with the client's reality — never the agency's credentials or history (Sant: Primacy Principle)
- Structure the narrative as What Is → What Could Be before revealing the solution (Duarte: Sparkline)
- Design every slide for the primitive brain first — simple, novel, non-threatening, high-contrast (Klaff: Croc Brain rules)
- Behave as the prize throughout — confident, scarce, and desirable (Klaff: Prize Framing)
- Every slide title is a complete sentence stating a conclusion — never a topic label (Duarte: Big Idea discipline)
- Include one S.T.A.R. moment (Shocking statistic, Transformative visual, Acting it out, or Relatable anecdote) — typically on Slide 5 or Slide 15 (Duarte)

Read `references/pitch-psychology.md` for Klaff's full STRONG method and Frame Control guide.
Read `references/storytelling.md` for Duarte's Sparkline, Big Idea, and S.T.A.R. frameworks.

---

## Quality Criteria

- Every slide has a complete Headline, Bullets, Speaker Notes, Visual Direction, and Persuasion Note — no field is blank
- Slide 3 (What We Heard) mirrors back the client's exact language from the intake brief — not generic observations
- Slide 4 (The Gap) presents a concrete, specific contrast between current state and desired state — not vague category descriptions
- Slide 11 (Investment) includes a ROI calculation — not just a cost statement — connecting the fee to expected revenue return using (TLV − COCA) ÷ COCA (Bodnar and Cohen, 2012)
- The Sparkline structure is visible: Slides 3–5 establish What Is; Slide 6 introduces What Could Be; Slides 9–14 deliver the resolution
- Speaker Notes are written for a live presenter — they include things to say, questions to ask, and what to do when the client hesitates
- Pricing on Slide 11 is in UGX with USD equivalent noted; tiers use the names Starter / Growth / Premium for retainers or Basic / Full / Comprehensive for projects
- The deck reads as a diagnostic conversation, not a sales brochure — the client's name and goals appear on every major slide
