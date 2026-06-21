---
name: deck-credentials
description: Generates an 8-slide agency credentials and capabilities presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill when pitching to a prospective client for the first time — in a discovery meeting, a networking follow-up, or a formal tender response. Tone is confident but not boastful — warm, professional, East African business register.
---
# Agency Credentials Deck

<!-- dual-compat:start -->
## Use when
- Generates an 8-slide agency credentials and capabilities presentation in structured markdown, ready to paste into PowerPoint, Canva, or Google Slides. Invoke this skill when pitching to a prospective client for the first time — in a discovery meeting, a networking follow-up, or a formal tender response. Tone is confident but not boastful — warm, professional, East African business register.
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

This skill generates an 8-slide credentials and capabilities presentation for pitching to prospective clients. The deck introduces the agency, demonstrates results, and invites the prospective client to take the next step.

Let the results do the talking. The deck is warm, professional, and grounded in the East African business register — direct but relational.

Output is paste-ready markdown. Transfer each slide into PowerPoint, Canva, or Google Slides.

---

## Required Input

Collect all of the following before generating the deck. Ask for any missing items.

- **Agency name** and tagline (one line that captures what the agency does and for whom)
- **Country/city** (default: Kampala, Uganda)
- **Primary goal** of this pitch (e.g. win a retainer, secure a project, open a conversation)
- **Founder name** and story — 3 sentences: origin (how the agency was founded), expertise (what qualifies the founder), purpose (why they do this work)
- **Team members** — for each: name, role, one-line expertise statement
- **3 core services** — each as a short headline (≤6 words) and 2 supporting bullets
- **Methodology** — 3–4 steps with a name and one sentence per step (e.g. Discover → Strategise → Execute → Report)
- **3 case study results** — for each: sector or anonymised client name, one-sentence challenge, one-sentence approach, one-sentence result with a specific metric
- **Client types served** — industries, business sizes, and any logos or sector names the agency can share (note confidentiality where applicable)
- **Onboarding process** — the 3 steps a new client goes through in the first 30 days
- **Communication rhythm** — how the agency communicates with clients (weekly updates, monthly reports, etc.)
- **Contact details** — phone, email, WhatsApp, website

---

## Slide Generation

Generate all 8 slides in full. Write every field. Use warm, confident, professional language throughout — East African business register (see east-african-english skill).

---

**Slide 1 — Cover**
**Headline:** [Agency Name] — [Tagline]
**Bullets:**
- [Consultant / Founder name]
- [City, Country — e.g. Kampala, Uganda]
- [Date]
**Speaker Notes:** Open warmly and directly. In the East African professional context, a brief personal connection before the formal presentation is appropriate — acknowledge any mutual contact, the prospective client's business, or the context in which you met. Keep this slide on screen for 30–60 seconds. Your opening words set the tone for everything that follows: confident, prepared, and genuinely interested in this client.
**Visual Direction:** Full-bleed brand colour — the agency's primary colour, applied boldly. Agency name in large white type. Tagline in slightly smaller type below. A subtle texture or abstract pattern in the background (not a stock photo — this is a brand slide). Founder or agency logo if available. The cover should be immediately recognisable as a professional agency — not a generic template.

---

**Slide 2 — Who We Are**
**Headline:** [Agency name] was founded to [founder purpose in brief — e.g. "give East African businesses the social media expertise that was previously only available to large corporations"]
**Bullets:**
- [Founder name]: [Sentence 1 — origin of the agency] [Sentence 2 — expertise that qualifies the founder.] [Sentence 3 — the "why" behind the work.]
- [Team member 1 name] — [Role] — [One-line expertise]
- [Team member 2 name] — [Role] — [One-line expertise]
- [Team member 3 name if applicable] — [Role] — [One-line expertise]
**Speaker Notes:** The founder story is the most human element of the deck — deliver it personally, not from the slide. Tell it in your own voice. The three sentences on the slide are a prompt, not a script. The team section signals that the client is buying a capability, not just one person. If the agency is a solo consultancy, frame this positively: "You work directly with me — no account managers, no juniors on your account."
**Visual Direction:** Left column: founder name, a professional headshot (if available), and the three-sentence founder story. Right column: team member cards — each card has name, role, and expertise line. If no photos are available, use illustrated professional avatars or simply name cards with coloured backgrounds. Warm, human, professional. Not a corporate org chart — this is an introduction.

---

**Slide 3 — What We Do**
**Headline:** Three services — each designed to move your brand forward
**Bullets:**
- [Service 1 headline — e.g. "Social Media Strategy"]: [Bullet 1 — what it delivers] / [Bullet 2 — who it is for or when to use it]
- [Service 2 headline — e.g. "Content Creation and Management"]: [Bullet 1] / [Bullet 2]
- [Service 3 headline — e.g. "Performance Reporting and Analytics"]: [Bullet 1] / [Bullet 2]
**Speaker Notes:** Present each service as a solution to a problem the prospective client likely has — not as a list of tasks. "Our strategy service gives you a clear plan so you stop guessing what to post." Keep the descriptions simple — this is an introduction, not a full service menu. Reference biz-dev-pricing-menu or biz-dev-proposal for the detailed scope if the client asks for specifics. Note: do not list more than three services — a laundry list weakens the pitch.
**Visual Direction:** Three service cards in a horizontal row or 2+1 layout. Each card: service headline in bold at the top, two bullet points below, a clean icon representing the service. Use brand primary colour for card headers. White card bodies. Clean, confident, not cluttered. The layout should make three services feel like a complete, coherent offering.

---

**Slide 4 — How We Work**
**Headline:** Our four-step process turns your goals into measurable results
**Bullets:**
- Step 1 — [Name, e.g. "Discover"]: [One sentence — what happens and what the client gets — e.g. "We begin with a deep-dive brief and platform audit to understand your brand, audience, and competitive position."]
- Step 2 — [Name, e.g. "Strategise"]: [One sentence — e.g. "We translate the findings into a 90-day social media strategy with clear goals, platforms, content pillars, and KPIs."]
- Step 3 — [Name, e.g. "Execute"]: [One sentence — e.g. "We produce and publish content according to the strategy — every post is planned, approved, and scheduled in advance."]
- Step 4 — [Name, e.g. "Report"]: [One sentence — e.g. "Every month we measure results against targets, share a written report, and adjust the plan based on what the data tells us."]
**Speaker Notes:** The methodology slide answers the prospective client's implicit question: "How exactly does this work?" Walk through each step and connect it to a client benefit. "Discover" means they will be heard. "Strategise" means they will have a plan. "Execute" means they will not have to chase for content. "Report" means they will always know what is happening. If the client has had a bad experience with an agency before (common), the methodology demonstrates professionalism and structure.
**Visual Direction:** Horizontal process flow — four steps connected by arrows. Each step: step number and name in bold above a card, one-sentence description inside. Brand primary colour for step names and arrows. Clean, professional, reassuring. The layout should communicate "we have a system."

---

**Slide 5 — Results We Have Delivered**
**Headline:** Three examples of what we have achieved for clients
**Bullets:**
- [Sector or anonymised client — e.g. "Healthcare — Private Clinic, Kampala"]:
  - Challenge: [1 sentence — e.g. "Low social media presence — 280 followers, minimal engagement, no leads from social."]
  - Approach: [1 sentence — e.g. "Built a Facebook and Instagram strategy focused on patient education content and community trust."]
  - Result: [1 sentence with metric — e.g. "900 new followers in 90 days, 35 WhatsApp enquiries per month attributed to social — up from near zero."]
- [Sector or anonymised client 2]:
  - Challenge: [1 sentence]
  - Approach: [1 sentence]
  - Result: [1 sentence with metric]
- [Sector or anonymised client 3]:
  - Challenge: [1 sentence]
  - Approach: [1 sentence]
  - Result: [1 sentence with metric]
**Speaker Notes:** Case studies are the most persuasive element of a credentials deck. Results must be real and specific — no invented metrics. If client confidentiality prevents naming the client, anonymise by sector and city. Deliver each case study conversationally: "One of our clients — a private clinic in Kampala — came to us with [challenge]. Here is what happened." If the prospective client is in the same sector as one of the case studies, lead with that one. Note: if the agency is new and has limited case studies, use results from freelance work, pro-bono projects, or clearly labelled internal projects.
**Visual Direction:** Three case study cards in a column or grid. Each card has three rows: Challenge (amber-left border), Approach (blue-left border), Result (green-left border). The result line is bold and includes the metric prominently. Clean card design. Client name or sector label at the top of each card in bold. Metric numbers in brand accent colour.

---

**Slide 6 — Who We Work With**
**Headline:** We work best with [client type description — e.g. "growing businesses in Uganda and East Africa that are serious about building their brand online"]
**Bullets:**
- Industries: [list — e.g. Healthcare / Education / Retail / Hospitality / Financial Services / Professional Services / NGOs]
- Business sizes: [e.g. "Small and medium businesses (5–150 staff) and individual professionals"]
- Client logos or sector names: [list any clients who have given permission to be named; note "Additional clients: confidential on request" if applicable]
- Not a good fit: [optional but credible — e.g. "We do not take on clients whose values conflict with our own — we are selective about who we work with"]
**Speaker Notes:** The "who we work with" slide signals expertise and selectivity. Being selective is a strength — it signals that the agency has standards and a defined niche. In the East African professional context, naming recognisable local clients (with permission) is highly persuasive. If no clients can be named, lead with sector expertise: "We understand the [sector] market in Uganda specifically — the audience, the regulations, and the cultural nuances." The "not a good fit" bullet is optional but powerful — it demonstrates confidence.
**Visual Direction:** Left section: industry tags displayed as simple pills or badges. Right section: client logos if available, or sector icons if logos cannot be used. If fully confidential, a clean text statement: "Clients across [X] sectors in Uganda and East Africa — references available on request." Professional, understated — let the sectors speak.

---

**Slide 7 — What Working With Us Looks Like**
**Headline:** Onboarding takes [X] days — then we get to work
**Bullets:**
- Onboarding Step 1: [e.g. "Discovery session (Week 1) — we meet, complete the client brief, and review your current social presence"]
- Onboarding Step 2: [e.g. "Strategy delivery (Week 2–3) — we present your 90-day social media strategy for approval"]
- Onboarding Step 3: [e.g. "Content launch (Week 4) — first content calendar approved and first posts published"]
- Communication rhythm: [e.g. "Weekly content approvals via WhatsApp / Monthly report via email and video call / Quarterly review meeting in person"]
- What you receive: [e.g. "Monthly performance report / Content calendar (30 days in advance) / Quarterly strategy review presentation"]
**Speaker Notes:** This slide answers the operational question: "What does the relationship actually look like day to day?" Prospective clients who have worked with agencies before often worry about communication and responsiveness. The onboarding timeline sets a clear expectation: content starts within [X] weeks. The communication rhythm demonstrates that the client will always know what is happening. Confirm the typical turnaround on WhatsApp messages: "We respond within [X hours] on business days."
**Visual Direction:** Two sections divided by a subtle line. Top section: onboarding steps as a horizontal 3-step timeline (Step 1 → Step 2 → Step 3) with week labels. Bottom section: communication rhythm displayed as a simple table or icon-and-text row (Weekly / Monthly / Quarterly). Clean, reassuring, professional. The layout should communicate reliability and structure.

---

**Slide 8 — Let Us Talk**
**Headline:** Ready to build your brand's social media presence? Let us start the conversation.
**Bullets:**
- [Founder / Consultant name]
- Email: [email address]
- Phone / WhatsApp: [number]
- Website: [URL]
- The next step: [specific, low-friction CTA — e.g. "Send us a WhatsApp message with your business name and we will schedule a free 30-minute discovery call"]
**Speaker Notes:** Close with warmth and a direct invitation. In the East African business context, a personal WhatsApp message is a natural and comfortable first step — lower friction than an email and more personal than a website form. Make the next step as easy as possible: "All you need to do is send us a message." Repeat the tagline — it anchors the agency's identity as the final thing the prospective client sees and hears. If presenting in person, hand over a business card at this point.
**Visual Direction:** Full-bleed brand colour — consistent with the cover slide to create a visual bookend. Agency name and tagline repeated prominently. Contact details in white text — clearly legible. A QR code linking to the website or WhatsApp (if feasible) in the bottom corner. Warm, confident, inviting close. The prospective client should leave knowing exactly how to take the next step.

---

## Persuasion Frameworks

Apply frameworks from `references/pitch-psychology.md` and `references/storytelling.md` when generating this deck.

Key principles for credentials presentations:
- A credentials deck is a prize frame document — it demonstrates that the agency is a desirable, scarce resource, not a vendor seeking approval (Klaff: Prize Framing)
- Lead with client outcomes, not agency history — the credentials open with the most impressive result, not the founding year (Sant: Primacy Principle — evidence before biography)
- Every slide title is a complete assertion: "Our clients generate an average 3× return on their social media investment" not "Our results" (Duarte: Big Idea discipline)
- The deck must answer Hatton's Two Strategic Questions: Why should they say yes? and Why will they remember this agency? before the first slide is written
- Arrive as the authority being evaluated — not the agency seeking approval (Klaff: Status Principles)

Read `references/pitch-psychology.md` for Klaff's STRONG method and Prize Framing guide.
Read `references/storytelling.md` for Duarte's Big Idea and S.T.A.R. frameworks.

---

## Quality Criteria

- All 8 slides have complete Headline, Bullets, Speaker Notes, and Visual Direction — no field is empty
- The founder story on Slide 2 is exactly 3 sentences covering origin, expertise, and purpose — not a CV or a list of qualifications
- Each of the 3 services on Slide 3 is stated as a headline of ≤6 words with exactly 2 supporting bullets — not a paragraph
- Case study results on Slide 5 each include a specific numeric metric — no vague results such as "significant growth"
- The methodology on Slide 4 uses named steps (not just numbers) and each step describes what the client receives, not just what the agency does
- The "what working with us looks like" slide (Slide 7) states a specific onboarding timeline in weeks — not a vague description
- The CTA on Slide 8 is specific and actionable — it tells the prospective client exactly what to do next and how
- Tone throughout is warm, confident, and professional — no boasting, no corporate jargon, no hollow claims without evidence
