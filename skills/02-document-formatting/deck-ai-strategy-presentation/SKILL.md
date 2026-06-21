---
name: deck-ai-strategy-presentation
description: Produces a 14-slide board-level AI marketing strategy presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Uses Minto's Pyramid Principle (conclusion-first), the AI Marketing Canvas framework (Venkatesan & Lecinski, 2026), and Randazzo's MVOSSTE model (2024) to present a business case, investment requirements, and ROI expectations. Invoke when a client needs to present an AI marketing strategy to their board, senior leadership, or investors, or when a consultant needs to demonstrate AI capability to a prospective client.
---
# AI Marketing Strategy Presentation Deck

<!-- dual-compat:start -->
## Use when
- Produces a 14-slide board-level AI marketing strategy presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Uses Minto's Pyramid Principle (conclusion-first), the AI Marketing Canvas framework (Venkatesan & Lecinski, 2026), and Randazzo's MVOSSTE model (2024) to present a business case, investment requirements, and ROI expectations. Invoke when a client needs to present an AI marketing strategy to their board, senior leadership, or investors, or when a consultant needs to demonstrate AI capability to a prospective client.
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

This skill generates a 14-slide AI marketing strategy presentation. Slide sequencing follows Minto's Pyramid Principle: state the conclusion on Slide 2, present the evidence and framework in Slides 3–10, then deliver the roadmap, governance, and decisions in Slides 11–14.

The deck is grounded in two primary sources:

- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas* (2nd ed., Stanford Business Books) — 5-step canvas framework
- Randazzo, G. W. (2024) *Winning Marketing Strategies Using Generative AI* (Business Expert Press) — MVOSSTE framework, use case mapping, human-in-the-loop principles

Supporting references:

- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book* — ROI formula: (TLV − COCA) ÷ COCA
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice* — RACE framework

Output is paste-ready markdown. Transfer each slide into PowerPoint, Canva, or Google Slides. No .pptx file is generated.

Cross-reference these skills as noted:

- `ai-marketing-canvas-assessment` — canvas step assessment and 12-month roadmap
- `ai-readiness-diagnostic` — current step and readiness data for Slide 3 and Slide 7
- `policy-ai-content-ethics` — ethics policy referenced on Slides 9 and 10
- `training-ai-foundations` — referenced on Slides 8 and 12

---

## Required Input

Collect all of the following before generating the deck. If any item is missing, ask for it.

- **Client organisation name**, sector, and country/city (default: Uganda/East Africa)
- **Current AI Marketing Canvas step** (from `ai-readiness-diagnostic`; Step 1–5)
- **Audience for presentation** — board / senior leadership / investors / prospective client
- **Key business goal for the year** (one primary goal, SMART format preferred)
- **Approximate Year 1 tool budget range** (in UGX)
- **Names of AI tools already identified** for the stack (if any)
- **AI Champion candidate** — proposed name and role (if known)

---

## Slide Generation

Apply the slide structure below in full. Write every field for every slide. Do not leave any field blank or marked TBC. Fill client-specific placeholders using the inputs collected above, or insert clearly labelled editorial notes in square brackets where the consultant must insert real data.

---

**Slide 1 — Title**
**Headline:** [Organisation Name]: AI Marketing Strategy [Year]
**Bullets:**
(none — title slide)
**Speaker Notes:** Open with the core argument in one sentence: "AI is not a threat to how we market — it is the biggest productivity multiplier our marketing team will ever have access to. Today I will show you exactly how we will use it." State the presenter's name and role. Confirm who is in the room and acknowledge any board members by name where appropriate.
**Visual Direction:** Full-bleed image of a Ugandan or East African business scene — a team in a meeting, a busy market, or an office environment that reflects the organisation's sector. Organisation logo centred or top-right. Presenter name and date bottom-left. Minimal text — headline and name only.

---

**Slide 2 — The Strategic Imperative**
**Headline:** AI-powered marketing is not optional — it is the new cost of competition
**Bullets:**
- Every competitor is already using AI content tools; generic content is invisible
- AI reduces content production time by 60–80%; same output with smaller teams or bigger volume
- Clients who adopt AI marketing in 2026 will have a 12–18 month advantage over late adopters
**Speaker Notes:** Cite Schaefer's "pandemic of dull" — the risk is not using AI and falling behind. The greater risk is using AI badly and producing undifferentiated content. Reference Randazzo (2024): the MVOSSTE framework positions AI as a strategic multiplier, not a replacement for human judgement. Emphasise that this organisation is making an active choice to lead, not react.
**Visual Direction:** Single bold statistic — for example, "60% faster content production" — in large display type. Dark background (near-black or deep brand colour). White or high-contrast text. No additional clutter. One number, one message.

---

**Slide 3 — The AI Marketing Canvas**
**Headline:** We are currently at Step [X] — here is our path to Step [X+1]
**Bullets:**
- Step 1–5 framework: Foundation → Experimentation → Expansion → Transformation → Reinvention (Venkatesan & Lecinski, 2026)
- We are at Step [X]: [one-line description of what that means for this organisation, drawn from `ai-readiness-diagnostic`]
- Our 12-month target: Step [X+1], with [named capability — e.g., AI-assisted content workflow] as the primary outcome
**Speaker Notes:** Explain the canvas briefly — most board members will not have encountered it. Stress that the five steps are sequential: organisations cannot skip steps sustainably. Emphasise that most East African organisations are at Step 1–2, which means the opportunity is clear and the path is well-defined. For the full canvas assessment and 12-month roadmap, reference `ai-marketing-canvas-assessment`.
**Visual Direction:** Five labelled boxes in a horizontal progression bar. Current step highlighted in a strong accent colour (e.g., brand primary). Steps before current: completed colour (e.g., green). Steps ahead: muted or grey. Step name and one-word descriptor under each box. Clean, minimal — no decorative elements.

---

**Slide 4 — What AI Can Do for [Organisation]**
**Headline:** AI will change how we produce, distribute, and measure marketing
**Bullets:**
- Content production: 3× more output at the same cost using AI drafting and scheduling tools
- Customer targeting: AI segmentation identifies highest-value audiences automatically, reducing wasted spend
- Response time: Automated replies to 80% of common enquiries within 60 seconds via WhatsApp and chatbot
**Speaker Notes:** Ground each bullet in something specific to this organisation's marketing operations. Pull figures from the readiness diagnostic where available. If the organisation has already trialled any AI tools, reference those results here. Keep this grounded — avoid hyperbole. Randazzo (2024): AI excels at pattern recognition, repetitive tasks, and personalisation at scale.
**Visual Direction:** Three icons arranged horizontally — a pen or document icon for content production, a target icon for customer targeting, and a clock icon for response time. One-line benefit statement beside each icon. White or light background. Brand colours for icons. No paragraph text.

---

**Slide 5 — What AI Cannot Do**
**Headline:** Human creativity, cultural intelligence, and relationships cannot be automated
**Bullets:**
- AI cannot read local cultural tensions or community sentiment — Kampala context requires human judgement
- AI cannot build trust; only consistent, human-authored engagement builds community over time
- AI cannot create genuinely surprising content; human insight and lived experience drive differentiation
**Speaker Notes:** This slide prevents the board from expecting AI to solve every marketing problem. Randazzo (2024): the human remains the strategist; AI is the production assistant. Schaefer: the "Proof of Human" is becoming a brand asset — audiences increasingly value content that is unmistakably human. This is particularly true in East African markets where relational trust is a primary driver of brand loyalty. Reassure the board: AI augments the team, it does not replace them.
**Visual Direction:** Simple list layout with a clear X or prohibition mark beside each item. Calming tone — use amber or grey, not alarming red. Subtext line at the bottom: "This is why your team remains the most important part of the system." White background.

---

**Slide 6 — Our AI Use Case Map**
**Headline:** We have identified [N] high-priority AI opportunities across 4 quadrants
**Bullets:**
- Internal Productivity: [Top 2 examples — e.g., AI caption drafting, automated monthly reporting]
- External Productivity: [Top 2 examples — e.g., WhatsApp chatbot for FAQs, email automation sequences]
- Internal Growth: [Top 1 example — e.g., AI audience segmentation from CRM data]
- External Growth: [Top 1 example — e.g., personalised promotional offers based on purchase history]
**Speaker Notes:** Walk through the use case map quadrant by quadrant. Emphasise that the top five quick wins are achievable within 30 days at low or zero cost. Reference `ai-use-case-mapping` for the full prioritised list. Randazzo (2024): begin with Internal Productivity use cases — they build team confidence and produce visible savings before the organisation commits to larger external deployments.
**Visual Direction:** 2×2 grid. X-axis: Internal / External. Y-axis: Productivity / Growth. Named use cases in each quadrant, colour-coded by priority tier (e.g., red = immediate, amber = 90 days, green = Year 2). Bold quadrant labels. Clean lines and adequate white space.

---

**Slide 7 — The Business Case**
**Headline:** AI marketing will deliver [X]% more output for [Y]% less cost within 12 months
**Bullets:**
- Current: [X hours/week] spent on content production by [N] staff at [UGX cost/month] — insert real figures
- AI-assisted: Same output with 30–50% less time; or double the output volume at the same cost
- Revenue impact: [Named campaign or channel] with AI targeting expected to improve conversion by [X]%
**Speaker Notes:** Apply the ROI formula — (TLV − COCA) ÷ COCA (Bodnar & Cohen, 2012). Fill with the client's actual staff costs and content production hours from the readiness diagnostic. If exact figures are unavailable, use conservative estimates from comparable East African cases and label them clearly as estimates. The board needs a number, even a conservative one, to approve a budget. For the full ROI model, reference `meta-social-media-roi-business-case`.
**Visual Direction:** Before/After comparison table in UGX. Two columns: Current State and AI-Assisted State. Rows: Staff hours/week, Cost/month, Output volume, Estimated conversion rate. Total row at the bottom with net improvement figure. Large, readable font — legible at the back of a boardroom.

---

**Slide 8 — Investment Required**
**Headline:** Year 1 AI marketing investment: UGX [X]/month in tools + [Y hours] of staff training time
**Bullets:**
- Tools: [List recommended tools with monthly cost in UGX — e.g., ChatGPT Plus UGX 180,000/month, FeedHive UGX 90,000/month]
- Training: AI Foundations programme (half-day) and AI Prompt Writing workshop — see `training-ai-foundations` and `training-ai-prompt-writing`
- Consultant support: Quarterly AI strategy review and canvas step assessment (if applicable)
**Speaker Notes:** Emphasise that most Step 2 tools are free or under UGX 500,000 per month. The primary investment is staff time for training and workflow adjustment — typically two to four weeks to establish new habits and integrate AI into the production process. Frame the training cost as a one-time investment that compounds in value over time. Reference `training-ai-foundations` for the full programme outline.
**Visual Direction:** Simple cost table with four columns: Tool / Monthly Cost UGX / Annual Cost UGX / Primary Purpose. Total row at the bottom with combined annual investment. Clean, no decorative elements. Font large enough to read from 4 metres.

---

**Slide 9 — Risk and Mitigation**
**Headline:** Three risks — all manageable with the right protocols
**Bullets:**
- Brand risk: AI-generated content sounds generic or off-brand → Mitigated by `ai-content-humaniser` quality control process and human editorial review
- Data risk: Customer data fed into AI tools without consent → Mitigated by Uganda Data Protection and Privacy Act 2019 compliance protocol
- Dependency risk: Over-reliance on a single AI tool or vendor → Mitigated by a diversified multi-tool stack and a mandatory human review gate before publication
**Speaker Notes:** Venkatesan and Lecinski (2026) document the Samsung/ChatGPT leakage incident as a cautionary case — employees inadvertently shared confidential source code via a public AI tool. The lesson is not to avoid AI; it is to define which data categories are permissible inputs. Also reference jailbreak risk and AI impersonation risk. None of these are reasons to avoid adoption — all are reasons to adopt with clear, documented protocols that the board approves today.
**Visual Direction:** Three-row table: Risk / Likelihood / Mitigation. Use Red-Amber-Green (RAG) coding in the Likelihood column. Bold risk names. Mitigation text in a lighter weight. Adequate row height for readability.

---

**Slide 10 — AI Ethics Policy**
**Headline:** We will use AI transparently, fairly, and accountably
**Bullets:**
- Transparency: AI involvement will be disclosed in content and to data subjects where required
- Fairness: AI tools will be monitored for bias, particularly in audience targeting and segmentation
- Privacy: No customer personal data will be input to AI tools without explicit consent under the Uganda Data Protection and Privacy Act 2019
**Speaker Notes:** Reference `policy-ai-content-ethics` for the full policy document. This slide signals to the board that the organisation is a responsible AI adopter — a growing reputational differentiator in East Africa as regulators and consumers become more aware of AI use in marketing. The five principles — transparency, fairness, nonmaleficence, accountability, and privacy — map to internationally recognised AI ethics standards. Adopting this policy now protects the organisation as regulation tightens.
**Visual Direction:** Five icons arranged horizontally, one per principle: transparency (open eye), fairness (scales), nonmaleficence (shield), accountability (tick in circle), privacy (padlock). Principle name above each icon, one-line description below. Clean, authoritative. White background with brand accent colour for icons.

---

**Slide 11 — 12-Month Roadmap**
**Headline:** From Step [X] to Step [X+1] in 12 months — here is the plan
**Bullets:**
- Q1 — Foundation: Data audit, full team AI Foundations training, 2 AI tool pilots with baseline metrics
- Q2 — Experimentation: Review pilot results, scale the one highest-performing experiment, document process
- Q3 — Expansion: Integrate AI into [second named function — e.g., email marketing or audience reporting], automate [named repetitive workflow]
- Q4 — Review: AI Marketing Canvas step-progress assessment, report to board, set Year 2 targets
**Speaker Notes:** Each quarter has a named deliverable and a named metric. Link this roadmap to the canvas assessment from `ai-marketing-canvas-assessment`. Reassure the board that the roadmap is designed to be iterative — if a Q2 experiment underperforms, the team pivots rather than accelerating into a failed approach. The Q4 review triggers the next planning cycle and sets the organisation up for the subsequent canvas step.
**Visual Direction:** Four equal columns labelled Q1 / Q2 / Q3 / Q4. Each column contains a quarter title (e.g., "Foundation"), 2–3 named actions, and a single headline metric. A horizontal progress arrow runs beneath all four columns from left to right. Brand accent colour for the current quarter (if presenting mid-year). Clean, no clutter.

---

**Slide 12 — Governance**
**Headline:** Clear ownership, clear accountability, clear review cadence
**Bullets:**
- AI Champion: [Named role — e.g., Marketing Manager] owns the AI programme and reports monthly to [board / CEO]
- Review cadence: Monthly tool performance review by the AI Champion; quarterly canvas step assessment with consultant
- Staff policy: All team members complete AI Foundations training before being granted access to any AI tool in the stack
**Speaker Notes:** Venkatesan and Lecinski (2026): the most successful AI programmes in comparable organisations have a named internal champion with explicit board-level support. Without a champion, AI adoption stalls at the pilot stage. In East African organisations, the AI Champion role is typically held by the Marketing Manager or a nominated Digital Lead who is already comfortable with digital tools. For the full staff training programme, reference `training-ai-foundations`.
**Visual Direction:** Simple reporting-line diagram. One box for the AI Champion with name and role. Arrow up to Board/CEO. Arrow down to Marketing Team. Beside the diagram, a two-row table: Review Type / Frequency / Owner. Clean, one box per role, no decorative elements.

---

**Slide 13 — What We Need from the Board**
**Headline:** Three decisions to unlock this strategy
**Bullets:**
- Decision 1 — Approve Year 1 tool budget: UGX [X]/month (annual: UGX [Y])
- Decision 2 — Designate AI Champion: Proposed appointment of [name/role]
- Decision 3 — Approve AI Ethics and Data Policy: Reference `policy-ai-content-ethics`
**Speaker Notes:** Keep this slide simple. Boards approve decisions — give them exactly three, clearly stated. Do not add supplementary requests or caveats. Each decision has a proposed owner and a one-line consequence if deferred. If the board wants to discuss before approving, offer to schedule a 30-minute follow-up within the week. Do not leave the room without a named decision-maker for each item.
**Visual Direction:** Three large numbered boxes arranged horizontally or vertically. Each box contains a bold decision number, a one-line decision statement, and a proposed owner. Sufficient white space between boxes. Brand accent colour for box borders or headers. No background imagery — decisions must be the only focal point.

---

**Slide 14 — Next Steps**
**Headline:** We can begin in Week 1 with zero additional budget
**Bullets:**
- Week 1: AI Foundations training for the full marketing team (half-day, internal facilitation)
- Week 2: Set up free and low-cost tool accounts — ChatGPT, Claude, FeedHive, Mailchimp AI features
- Week 3: Run the first AI-assisted content production week and record time savings against baseline
**Speaker Notes:** End with momentum, not approval-seeking. The first three steps cost nothing and require no board decision beyond today's presentation — they can begin immediately. This signals competence and confidence to the board. Record the time-savings figure at the end of Week 3 — this becomes the first data point in the ROI case for Year 2 budget. Thank the board and confirm the follow-up date for the Q1 progress report.
**Visual Direction:** Three-step horizontal timeline: Week 1 / Week 2 / Week 3. Each step has a label and one action sentence. A progress arrow runs left to right beneath the steps. Closing line at the bottom: "Thank you — questions welcome." Presenter contact details (email, WhatsApp number) in small text at the foot of the slide.

---

## Persuasion Frameworks

Apply frameworks from `references/presentation-frameworks.md` when generating this deck.

Key principles for AI strategy presentations:
- AI strategy decks face a heightened scepticism from audiences — lead with business outcomes, not technology features (Hatton: Empathy Model — the client cares about results, not tools)
- Apply the Executive 10% Rule strictly — the first two slides state what AI will deliver for this specific client in measurable terms; the technology explanation comes later (Duarte)
- Every slide title is a complete assertion: "AI content scheduling saves 8 hours per week and improves posting consistency by 40%" not "AI scheduling" (Duarte: Big Idea per slide)
- The Sparkline contrast is particularly powerful here: What Is (manual processes, current costs) vs. What Could Be (AI-assisted efficiency and scale) — make the gap concrete in time and money (Duarte: Sparkline)
- Answer Hatton's Two Strategic Questions before writing: Why should they adopt an AI strategy? and What will make this presentation memorable and different from every other "AI" pitch they have heard?

Read `references/presentation-frameworks.md` for the full framework guide.

---

## Quality Criteria

- Minto Pyramid structure is maintained: the conclusion — AI adoption is imperative — is stated on Slide 2, not buried in the roadmap or business case
- All 14 slides follow the exact Headline / Bullets / Speaker Notes / Visual Direction format without exception
- The business case on Slide 7 uses UGX figures throughout; no USD assumptions are used unless the client's operations are explicitly USD-denominated
- The risk slide (Slide 9) is honest and specific — the Samsung/ChatGPT leakage incident and the Uganda Data Protection and Privacy Act 2019 are named explicitly, not paraphrased
- The 12-month roadmap on Slide 11 is tied to the AI Marketing Canvas steps (Venkatesan & Lecinski, 2026), not to generic project milestones
- Slide 13 contains exactly three board decisions — no more, no fewer
- Visual Direction on every slide is specific enough for a designer or non-specialist to execute without further briefing — layout, colour treatment, and chart or table type are all named
- All client-specific placeholders in square brackets are either filled using the collected inputs or flagged clearly for the consultant to complete before presenting
