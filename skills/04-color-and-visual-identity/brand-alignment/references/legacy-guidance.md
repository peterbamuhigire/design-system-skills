# Brand Alignment Skill

The website is a brand experience, not just a marketing tool. Every choice — from layout to language to navigation — contributes to how the business is perceived. This skill ensures the site feels intentional and cohesive rather than generic or misaligned.

## Before Building: Brand Discovery

Read these files in order and extract the brand signals:

1. `docs/company-profile.md` — who they are, what they do, what makes them different
2. `docs/style-brief.md` — mood, personality, visual direction
3. `docs/services.md` — what they offer and how they describe it
4. All other `docs/*.md` — tone patterns, recurring themes, language choices

### Client Language Mining

Before writing anything, extract the client's vocabulary from their docs:

1. **Read every file in `docs/{lang}/`** — company profile, services, pages, style brief, all of them
2. **Write down the exact words they use** to describe: their business, their customers, their problems, their solutions, their industry
3. **Use those words in the website copy** — the site should sound like the business owner talking, not a copywriter describing the business from outside
4. **Note their natural register** — formal? semi-formal? technical? The site matches their voice, not yours

When the business owner reads the site, they should think "that's exactly how I would say it."

### Six Foundational Questions (Pre-Build Gate)

Before the client provides any content, they must be able to answer these six questions. If they cannot, the website will have structural problems no amount of design can fix.

1. Can you explain your offer in a couple of sentences?
2. What is your unique value proposition? Why should someone hire you and not your competitor?
3. Who is your ideal client — specifically?
4. What is your strategy for getting new clients through your website?
5. What are your current traffic sources (or expected sources)?
6. Who are your competitors?

If any answer is missing or vague, note it as a gap. The website must not paper over unclear positioning with pretty design.

Answer these questions before generating any page:

### Who Is the Ideal Customer?

The ideal customer determines everything. Identify from the docs:

- What questions do they need answered first?
- How much context or explanation do they need?
- What language feels accessible and appropriate to them?
- What kind of reassurance builds their trust?

**Build an audience profile from real data** — if the client's docs mention: testimonials from customers, subscriber messages, survey responses, or descriptions of who buys from them, extract:
- Their role, industry, company size, geography
- Specific challenges and aspirations they describe
- What triggers their decision to buy (pain points they mention)
- What words THEY use to describe their problems (mirror these)

A website that tries to speak to everyone ends up speaking clearly to no one. Every layout decision, content emphasis, and CTA should serve the identified audience.

### What Is the Brand Position?

Extract from the content:

- **What they do** — in one clear sentence
- **Who they do it for** — specific audience, not "everyone"
- **What makes their approach different** — the genuine differentiator
- **What feeling they want to create** — trust, warmth, authority, innovation, approachability

If the docs do not make these clear, note the gaps and work with what is available. Never fabricate a brand position.

### The StoryBrand Principle: Customer = Hero, Brand = Guide

The customer is the hero of the story, not the brand. The brand is the guide — like Yoda to Luke Skywalker. Every page must follow this principle:

- **Hero (customer):** Has a problem, desires a transformation, needs help
- **Guide (brand):** Understands the problem, has a plan, offers a clear path forward
- **The plan:** A named framework, process, or methodology that makes the path concrete

**Application:** Never position the business as the star. Headlines speak to the customer's problem, not the brand's achievements. The About page opens with the customer's world, not the company's history. CTAs frame the customer as the one taking action, with the brand as their support.

## Homepage: Set Expectations Immediately

The homepage is the most important brand moment. Visitors must quickly understand:

1. What the business does
2. Who it serves
3. What makes the approach different
4. What to do next

### Homepage Brand Checklist

- [ ] Headline communicates the core offering in the client's own language (from docs)
- [ ] Subheadline addresses the ideal customer directly
- [ ] The visitor does not have to scroll to understand the business
- [ ] First CTA is visible without scrolling and feels natural
- [ ] Visual hierarchy guides attention: offering → audience → differentiator → action
- [ ] No generic filler text ("We are a leading provider of solutions")

Brand clarity on the homepage reduces friction. When people do not have to work to understand the business, they stay and explore.

## Messaging Consistency Across Pages

The brand voice must remain consistent even as content changes. Every page should feel like it belongs to the same business.

### Check Consistency Across

| Page Type | Brand Voice Must Convey |
|-----------|------------------------|
| Services | Competence, clarity about what is included and who benefits |
| About | Authenticity, human connection, credibility |
| Team | Warmth, professionalism, approachability |
| Testimonials | Social proof that reinforces the brand promise |
| FAQ | Helpfulness, transparency, respect for the visitor's time |
| Contact | Accessibility, willingness to engage, clear next steps |

### Voice Drift Warning Signs

Stop and correct if you notice:

- A service page sounds corporate while the about page sounds casual
- CTAs shift between aggressive and passive across pages
- Some pages use industry jargon while others use plain language
- Tone becomes impersonal on pages with less source content

When a `docs/*.md` file has thin content, maintain the established voice rather than filling gaps with generic language.

## Visual Branding: Consistency and Restraint

Visual branding works best when it supports readability and understanding. Restraint is more effective than decoration.

### Visual Consistency Rules

Apply uniformly across every page:

- **Colours** — use the design-system palette consistently; do not introduce new colours per page
- **Typography** — same heading/body fonts everywhere; consistent sizing hierarchy
- **Spacing** — uniform section padding, card gaps, and content margins
- **Image treatment** — same border-radius, same hover behaviour, same aspect ratio approach
- **Component patterns** — buttons, cards, and sections should look identical in style across all pages

### Visual Restraint Rules

- Do not add decorative elements that do not serve comprehension
- Do not use more than one accent colour for emphasis on a single page
- Do not vary section layouts dramatically between pages without reason
- Let whitespace do the work — generous spacing communicates confidence
- Fewer visual ideas executed consistently outperform many ideas applied inconsistently

## Navigation and User Flow

How people move through the website is part of the brand experience. Clear navigation communicates confidence and respect for the visitor's time.

### Navigation Brand Standards

- **Primary navigation** — only pages that matter most to the ideal customer; typically 4-6 items
- **Page ordering** — reflects the visitor's decision journey, not the business's internal structure
- **Labels** — use language the visitor would use, not internal terminology
- **Contact/CTA** — always accessible, never buried

### User Flow Validation

For each page, verify the visitor can easily:

- [ ] Find key information without hunting
- [ ] Understand the business's process or approach
- [ ] Reach the contact page or primary CTA within one click
- [ ] Navigate back or to related content without confusion

Overly complex menus or buried information creates frustration. If the business has many services, group them logically rather than listing everything in the main navigation.

## Calls to Action: Guide, Do Not Pressure

CTAs should feel natural to the brand, not forced or aggressive.

### CTA Language by Brand Personality

| Brand Feels | CTA Style | Examples |
|-------------|-----------|---------|
| Professional, established | Confident and clear | "Schedule a Consultation", "Request a Proposal" |
| Warm, approachable | Inviting and supportive | "Get in Touch", "Let Us Help You" |
| Innovative, forward-thinking | Action-oriented | "Start Your Project", "Explore Our Approach" |
| Community-focused | Inclusive and welcoming | "Join the Programme", "Become a Member" |

### CTA Placement Rules

- Every page must have at least one clear CTA
- The primary CTA should appear above the fold and again at the page bottom
- Secondary CTAs (e.g., "Find Out More") can guide exploration within the site
- CTA wording must be consistent — do not use "Contact Us" on one page and "Reach Out" on another for the same action
- Never use manipulative language ("Don't miss out!", "Last chance!", "Act now!")

## Content Emphasis: What to Prioritise

Not all information is equally important. Brand alignment means choosing what to emphasise based on what the ideal customer needs.

### Prioritisation Framework

For each page, rank content by:

1. **What builds understanding** — what they do, how it works
2. **What builds trust** — credentials, testimonials, track record, team
3. **What enables action** — how to contact, what happens next, pricing clarity
4. **What provides depth** — detailed descriptions, case studies, FAQs

Lead with understanding, then trust, then action. Depth supports but does not lead.

### Cross-Pollination: Mix Content Across Pages

Don't silo content by page type like a department store. Relevant information should appear wherever the visitor needs it:
- Homepage: include service overview + testimonials + credibility + about snippet
- Service pages: include relevant testimonials and case studies inline
- About page: mention how you help, not just who you are
- Every page making claims: include social proof next to those claims

### What to Omit or De-emphasise

- Internal company milestones that do not matter to the visitor
- Awards or certifications the audience would not recognise
- Technical details that belong in a conversation, not a homepage
- History sections that are longer than the service descriptions
- Self-serving adjectives ("hard-working", "pragmatic", life mottos, "passionate about coffee") — replace with specific expertise and problem-solving evidence

## Common Brand Misalignment Pitfalls

Watch for and correct these patterns:

| Pitfall | Problem | Correction |
|---------|---------|------------|
| Trying to look bigger than they are | Creates distrust when reality does not match | Present the business honestly; small and focused is a strength |
| Aesthetics over usability | Beautiful pages that confuse visitors | Prioritise clarity; design serves understanding |
| Generic messaging | "We are passionate about delivering excellence" | Use specific language from the client's own docs |
| Visual inconsistency | Each page feels like a different website | Apply the same component patterns and spacing everywhere |
| Buried CTAs | Visitors cannot figure out how to take action | Primary action visible on every page, above the fold |
| Speaking to everyone | Vague value propositions that resonate with no one | Address the identified ideal customer directly |
| Condescending phrases | "Research suggests..." or "If you're a business owner..." | State fears and benefits directly; don't lecture your audience |
| Self-serving team bios | "Hard-working, pragmatic, passionate about coffee" | Replace with specific expertise and how they solve problems |

## Validation: The Brand Coherence Check

After building all pages, review the complete site against these questions:

1. **Could a visitor describe what this business does after 10 seconds on the homepage?**
2. **Does every page feel like it belongs to the same business?**
3. **Is the tone consistent from the first heading to the last footer link?**
4. **Would the ideal customer feel that this site was made for them?**
5. **Are CTAs clear, consistent, and easy to find on every page?**
6. **Does the visual treatment support the content, or compete with it?**
7. **Can a visitor reach the contact page or primary action from any page in one click?**

If any answer is no, identify the specific pages or sections that break coherence and correct them before proceeding to the deploy skill.

### Voice Authenticity Check

After the coherence check, verify the site sounds like the business — not like AI, not like a template:

1. **Does the copy use the client's own vocabulary?** Words and phrases should come from their docs, not from a copywriter's toolkit. Read the client's `docs/{lang}/` files and check the site mirrors their language.
2. **Zero AI vocabulary across all pages?** Scan every page for Tier 1 banned words (delve, tapestry, landscape, leverage, navigate, foster, realm, harness, robust, vibrant, pivotal, testament, bolster, etc.). See `blog-writer/references/human-voice-standards.md` for the full three-tier blacklist.
3. **Would the business owner recognise their own voice?** The ultimate test. If the copy sounds like it could belong to any business in any country, it hasn't been personalised enough.
4. **Is the voice consistent across pages?** The about page and the services page should sound like the same person wrote them. Check tone, formality, and sentence style across at least 3 pages.
5. **Are opinions present where appropriate?** The site should take clear positions, not hedge with "could potentially" and "might consider". Measured confidence, not vague diplomacy.

For individual article voice checks (burstiness, sentence rhythm, structural patterns), see the blog-writer's Human Voice Self-Check in `blog-writer/references/human-voice-standards.md`.

## How This Skill Relates to Others

- **language-standards** governs the language and tone of the words
- **design-system** governs the visual identity (fonts, colours, spacing)
- **sales-copywriting** — Persuasion techniques must align with brand voice. Level 2 persuasion (confident, professional) is the default ceiling. Hard-sell tactics (Level 3) require explicit client approval in the style brief.
- **brand-alignment** (this skill) ensures both work together to create a coherent brand experience that serves the ideal customer

This skill validates the decisions made by design-system and the content generated by page-builder. It is a quality gate — read the brand signals first, then verify alignment throughout the build.
