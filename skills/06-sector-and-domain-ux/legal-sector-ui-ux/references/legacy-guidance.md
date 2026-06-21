# Legal Sector Skill

## When to Use This Skill

Use this skill for any client who is a lawyer, law firm, solicitor, barrister, legal consultant, or legal aid organization. This skill replaces sector-strategies for legal clients — do not run both.

Run this skill before design-system and page-builder. The practice area matrix in this skill feeds directly into the sector-brief.md that design-system reads. After completing this skill, continue with the standard build pipeline: design-system → photo-manager → page-builder → seo → deploy.

This skill works alongside all cross-cutting skills: i18n, language-standards, content-writing, brand-alignment, sales-copywriting.

Output: completed `docs/sector-brief.md` populated with practice-area design direction, trust signal priorities, and ethics constraints specific to this firm.

---

## The Legal Client Psychology

Legal searches happen during some of the worst moments of a person's life. The visitor is frightened, often in pain or in crisis, and evaluating whether to trust a stranger with an outcome that could change everything. Every design and copy decision must account for this emotional state.

**The core insight**: Prospective legal clients approach a website the same way they approach a new doctor — they want reassurance before they want credentials. Credentials come second. Evidence that you understand their situation comes first.

**The above-the-fold test**: Within 3 seconds of landing on the homepage, a visitor must answer: "Does this firm handle my type of case?" If the answer is not immediately clear, they leave.

**The three-stage trust journey**:

1. **Search** — The visitor arrives, often from a mobile device, in a state of stress. The site must immediately signal: "You are in the right place."
2. **Evaluate** — The visitor reads practice area pages, attorney bios, and reviews. The site must answer: "Have they handled cases like mine? Are they competent and trustworthy?"
3. **Contact** — The visitor decides to reach out. The site must make the first step feel safe, easy, and low-risk: "What happens if I call? Will anyone respond?"

**The fatal error most law firm websites make**: They market to other lawyers, not to frightened people searching for help. Partner credentials, law school rankings, and legal terminology impress colleagues — they alienate the prospective client at the exact moment they need reassurance.

---

## The Five Key Messages

Every law firm website must communicate all five of these. If any is absent, the site underperforms.

1. **I understand your situation** — not generic legal services language; specific to the client's circumstances (injured in a car accident, facing a criminal charge, going through a divorce)
2. **I have successfully handled cases like yours** — social proof appropriate to practice area and jurisdiction ethics rules
3. **I am accessible** — phone number visible on every page, response time commitment stated, languages spoken listed if relevant
4. **Working with me is clear and simple** — plain English about what the process looks like, what happens at the first meeting, what documents are needed
5. **You can trust me** — bar memberships, peer review ratings, years in practice, community involvement; credentials presented in terms of what they mean for the client

Present all five on the homepage. Reinforce them on every practice area page.

---

## Practice Area Design Matrix

| Practice Area | Design Direction | Primary Emotion to Address | Hero Image Guidance | CTA Wording |
|---------------|-----------------|---------------------------|---------------------|-------------|
| Personal Injury | Trust blue + warm amber; serif heading + clear body; minimum 18px | Financial fear + pain + distrust of insurers | Attorney in natural setting, not a courtroom; empathy over authority | "Get Your Free Case Review" |
| Family Law | Teal + sage; warm serif heading + humanist body; generous whitespace | Heartbreak + fear for children + uncertainty | Warm, non-intimidating setting; avoid anything implying courtroom drama | "Talk to a Family Law Attorney" |
| Criminal Defense | Deep navy + charcoal; strong geometric sans; high contrast | Terror + shame + urgency | Attorney with direct eye contact; projects resolve and competence | "Call Now — 24/7 Defense" |
| Estate Planning | Deep blue + warm gold; classic serif throughout; unhurried layout | Responsibility + mortality + family protection | Families and mature professionals in warm settings | "Plan Your Family's Future" |
| Immigration | Warm blue + terracotta; highly readable body; multilingual options | Hope mixed with fear of deportation or family separation | Multicultural, warm; attorney in genuine consultation | "Start Your Immigration Journey" |
| Business/Corporate | Slate + dark teal; sharp modern sans; clean structured layout | Risk awareness + time pressure + deal certainty | Professional working environments; not posed studio shots | "Protect Your Business" |
| Employment | Strong blue + amber; clear readable body; validating tone | Anger + humiliation + financial vulnerability | Attorney in approachable professional setting; strength without aggression | "Tell Us What Happened" |
| Workers' Compensation | Dependable blue + warm neutral; high readability; working-class context | Injury + fear of job loss + confusion about rights | Working-environment context, not corporate boardrooms | "Know Your Rights. It's Free to Call." |

**How to use this table**: Identify the firm's primary practice area. Apply the design direction to the design-system skill. If the firm covers multiple practice areas, use the primary area's palette and adapt secondary areas through typography weight and content tone rather than repainting the entire site.

---

## Homepage Architecture

Every law firm homepage follows the same three-tier information model. Sequence matters — do not reorder.

### Tier 1: Above the Fold (Critical Zone)

All four elements must be visible without scrolling on both desktop (1280px) and mobile (375px):

1. Clear statement of who you serve and what problem you solve — not the firm name, not a tagline about excellence
2. Primary CTA button: "Free Consultation" or "Free Case Review" — highest contrast element on the page
3. One trust signal: years in practice, aggregate review rating, or a case outcome number with disclaimer
4. Navigation including practice areas — labelled in client language, not legal taxonomy

What must not occupy above-the-fold space: awards clients do not recognise, firm history that does not answer "will you help me?", generic legal stock photography.

### Tier 2: Primary Content (Body)

Section order, top to bottom:

1. Practice areas — card layout, client search language (not legal terms), each links to a dedicated page
2. Attorney preview — brief, approachable; full bio on separate attorney page
3. Social proof — testimonials or case results; ethics-compliant per jurisdiction
4. Contact section — phone (tap-to-call on mobile), short form, response time commitment

### Tier 3: Incidental (Footer)

- All practice area links (for SEO)
- All attorney names (for SEO)
- Office address with map link
- Phone number, clickable
- Attorney-client disclaimer
- General informational disclaimer
- State bar registration language if required by jurisdiction

Keep Tier 3 content from competing visually with Tier 1 or Tier 2.

---

## Attorney Profile Page

Build one profile page per attorney. Required elements, in this order:

1. **Professional photo** — warm, natural light, approachable expression; not posed formal headshot against white background; actual office preferred over studio
2. **Opening statement** — who the attorney helps and what they focus on (2–3 sentences); client-centered, not credential-first
3. **Why this area of law** — brief personal narrative about why the attorney chose this practice; humanises and builds connection
4. **Relevant experience** — in plain English; not a case list; what the attorney has done for clients like the reader
5. **Credentials** — law school, bar admissions, relevant certifications; comes after establishing relevance to the client's situation
6. **Personal note** — community involvement, outside interests; brief; humanises
7. **Direct contact CTA** — "Schedule a call with [First Name]" or "Email [Name] directly"; not a generic contact page link

Traditional attorney bios (third-person credential lists) convert poorly. Client-centered bios that open with the client's situation convert better.

**Ethics note on case results in bios**: Check jurisdiction rules before listing specific settlement or verdict amounts. Where permitted, always include the disclaimer: "Past results do not guarantee a similar outcome. Every case is different."

---

## Trust Signals by Tier

| Tier | Signal | Notes |
|------|--------|-------|
| Tier 1 — Must Have | Peer review ratings (Martindale-Hubbell AV, Super Lawyers, Best Lawyers) | Only include verifiable ratings from the current cycle |
| Tier 1 — Must Have | State bar membership, specialty certifications | List exactly; no states where attorney is not admitted |
| Tier 1 — Must Have | Verified client reviews — Google aggregate rating | Link to live Google Business Profile |
| Tier 1 — Must Have | Years in practice | Simple, prominent |
| Tier 1 — Must Have | Case results (where ethics permits) | Always with disclaimer; accurate amounts only |
| Tier 2 — Should Have | Named testimonials with case type | Never anonymous; never composite clients; include required disclaimers |
| Tier 2 — Should Have | Media mentions — "As seen in" bar | Verifiable sources only |
| Tier 2 — Should Have | Free consultation offer | Lowers barrier to contact; state what happens during the call |
| Tier 2 — Should Have | Former government or prosecutor experience | Converts especially well for criminal defense |
| Tier 3 — Nice to Have | Community involvement and local bar activity | Humanises; builds local trust |
| Tier 3 — Nice to Have | Publications and speaking | More important for business/corporate practices |
| Avoid | Generic awards from organisations attorneys pay to join | Clients recognise pay-to-play awards; they harm credibility |
| Avoid | Anonymous testimonials | Low credibility; may violate bar rules in some jurisdictions |

---

## Ethics and Advertising Constraints

Bar association advertising rules govern everything that appears on a law firm website. Rules vary by jurisdiction. Violations can result in disciplinary action. **The attorney is responsible for compliance, not the developer.** The developer's role is to flag potential issues and build in required disclaimers by default.

### Universal Prohibitions (Most Jurisdictions)

- No "expert" or "specialist" claims unless the attorney holds a state bar-approved certification in that specialty. Use instead: "experienced in," "focused practice in," "extensive background in."
- No outcome guarantees or implied guarantees: "We win cases," "Get the maximum settlement," "100% success rate" are all prohibited.
- No unsupported superlatives: "best law firm in [city]" is only permissible if supported by a verifiable, credible award.
- No misleading comparisons to other attorneys without substantiation.

### Testimonials

Most jurisdictions allow testimonials with restrictions. Before publishing any testimonial:
- Check the state bar's advertising rules for the specific jurisdiction.
- Include a disclaimer: "Client testimonials do not guarantee, warrant, or predict results in your case."
- Never publish composite or anonymized testimonials in jurisdictions that prohibit them.
- Never publish testimonials that create unjustified expectations of specific results.

### Required Disclaimers (Build These into Every Template)

**Contact form disclaimer** (required on every contact form):
> "Submitting this form does not create an attorney-client relationship. Please do not include confidential information in your initial message."

**Footer informational disclaimer** (required in every footer):
> "The information on this website is for general informational purposes only. Nothing on this site should be taken as legal advice for any individual case or situation. This information is not intended to create, and receipt or viewing does not constitute, an attorney-client relationship."

**Case results disclaimer** (required wherever case outcomes appear):
> "Past results do not guarantee a similar outcome. Every case is different."

### Developer Pre-Launch Checklist

Before handing off the site for attorney review, verify:

- [ ] No "expert" or "specialist" language unless bar-certified
- [ ] No outcome guarantees anywhere on the site, including in headlines
- [ ] Contact form includes attorney-client relationship disclaimer
- [ ] Footer includes general informational disclaimer
- [ ] Case results include disclaimer (where results are displayed)
- [ ] Testimonials include disclaimer (where testimonials are displayed)
- [ ] Domain name does not imply guaranteed results
- [ ] Attorney credentials are stated accurately — no states listed where not admitted
- [ ] All copy drafted by the developer avoids outcome language and specific legal advice

Deliver this checklist to the attorney as a handoff item. The attorney must review all content before the site goes live.

Full ethics reference: `sectors/legal/references/ethics-constraints.md`

---

## Local SEO for Law Firms

### Google Business Profile

The highest-ROI local SEO action for any law firm. Set up before the site launches:

- Primary category: "Law Firm" — add relevant specialty categories
- Exact NAP (Name, Address, Phone): identical spelling and format to what appears on the website and all directories
- Service areas for practices that cover surrounding cities
- Attorney photos uploaded to the profile
- Regular posts (blog summaries, event announcements)
- Respond to every review — positive and negative — within 48 hours

### Page and URL Structure

One dedicated page per practice area per city the firm targets. Generic practice area pages do not rank for specific search queries.

- Bad: `/personal-injury/` alone
- Good: `/personal-injury/`, `/personal-injury/chicago/`, `/car-accident-attorney/chicago/`, `/truck-accident-attorney/chicago/`

Each city-level page must contain city-specific content — not boilerplate with the city name substituted.

### Title Tag Formula

`[Practice Area] Attorney | [City, State] | [Firm Name]`

- 45–65 characters; front-load the practice area keyword, not the firm name
- Example: `Car Accident Attorney | Chicago, IL | Smith Law Group`

### Schema Markup

Implement both `LocalBusiness` and `Attorney` schema on every page. Full schema template: `sectors/legal/references/local-seo.md`

### Legal Directory Citations

Build and maintain consistent NAP listings on, in priority order: Google Business Profile, Avvo, FindLaw, Martindale-Hubbell, Justia, Lawyers.com, state bar directory, LinkedIn (individual attorney profiles).

### Review Acquisition

Reviews on Google Business Profile and Avvo are the most valuable for conversion and local SEO. Request reviews by email after case closure. Ethics-compliant request template: `sectors/legal/references/local-seo.md`

---

## Conversion and Intake

### Primary CTA Strategy

"Free Consultation" outperforms "Contact Us" in every A/B test on legal sites. Be specific about what happens: "30-minute free consultation — we'll review your case and tell you your options."

Place the primary CTA in: the hero section, mid-page after social proof, end of every practice area page, and as a sticky element in the mobile header.

### Contact Form Requirements

Optimal fields for maximum completion (do not add more without a specific reason):

1. Full name (required)
2. Phone (required — most legal clients prefer to be called)
3. Email (required)
4. Practice area or matter type selector (required — helps intake routing)
5. Brief description of their situation (optional text field — increases quality of leads)
6. How they heard about you (optional — for marketing tracking)

Do not ask for: date of incident, insurance information, case-specific details. Ask these on the consultation call, not the intake form. More than 6 fields measurably reduces completions.

### Emergency Availability

Criminal defense firms must display a 24/7 emergency phone line prominently — above the fold on mobile, in the navigation bar on desktop. Clients facing arrest or booking cannot wait until business hours.

### Response Time Commitment

State a specific response time in the contact section and on the form confirmation page:

> "We respond to all inquiries within [X] hours on business days. For urgent matters, call [phone]."

This commitment alone increases form completions by reducing the visitor's implicit fear that no one will respond.

---

## What Not to Do

Ten specific mistakes found on most law firm websites:

1. Opening the homepage with the firm name or founding year instead of the client's problem
2. Using "Fighting for your rights," "Aggressive representation," or "Dedicated to excellence" — meaningless overused phrases
3. Publishing attorney bios in credential-first order (law school → clerkships → awards) instead of client-centered order
4. Using generic stock photography of gavels, scales of justice, or empty courtrooms
5. Building one broad practice area page instead of separate pages per specific practice sub-area
6. Hiding the phone number below the fold or omitting it from mobile navigation
7. Contact forms with more than 6 fields
8. No stated response time commitment on the contact form
9. Publishing "expert" or "specialist" claims without checking bar certification requirements
10. Omitting the attorney-client disclaimer from the contact form

---

## Integration with Build Pipeline

This skill produces `docs/sector-brief.md`. All subsequent skills read that file.

**design-system** reads the practice area design direction from the matrix above to select fonts, colour palette, and spacing. Do not use generic navy + white + gold — every law firm uses it. Differentiate within the trust colour spectrum.

**page-builder** reads the homepage architecture section and attorney profile structure. Apply the client-centered bio format, not the traditional credential-list format. Build one page per practice area — never combine multiple practice areas onto one page.

**seo** implements the title tag formula, LocalBusiness + Attorney schema, and hreflang tags. For multi-language law firms (especially immigration practices), ensure each language version has its own practice area pages.

**brand-alignment** enforces the Five Key Messages across every page. Flag any page that fails to address the client's emotional state before presenting credentials.

Reference files in `sectors/legal/references/`:
- `content-templates.md` — hero copy formulas, practice area page structure, attorney bio template, meta title/description formulas
- `local-seo.md` — full JSON-LD schema, GBP optimization checklist, citation building, review acquisition templates
- `ethics-constraints.md` — complete bar advertising rules, jurisdiction variation table, developer checklist
