## Why Sector Strategy Matters

Generic websites scream "AI-generated." Industry-specific design psychology makes sites trustworthy and distinctive.

A tour company's website needs wanderlust and discovery cues (but each tour operator needs DIFFERENT colors and fonts). A school's website needs credibility and safety (but each school needs UNIQUE visual identity). A hospital's website needs trust and accessibility (but each hospital needs DIFFERENT design choices).

**Key principle: No two websites built with these skills should look the same.**

Same build pipeline. Same component structure. Different psychology. Different trust signals. Different components. Different content order. **DIFFERENT VISUAL IDENTITY.**

This skill provides templates for ten core sectors to ensure sector-appropriate design psychology. But customization is REQUIRED to prevent homogeneity:
- **Design tokens** (reference palettes — not prescriptive)
- **Sector-brief template** (customization questionnaire — REQUIRED to answer)
- **Component patterns** (patterns to follow, with YOUR styling)
- **Trust signals framework** (what matters in that sector)

## Universal Guidelines

All sector templates are built on **Universal Design Guidelines** which cover:
- Purpose-driven design and visual hierarchy
- User-centered design and UX fundamentals
- Color theory, typography, spacing standards
- Accessibility requirements (WCAG 2.1 AA)
- Mobile-first responsive design
- Trust and credibility signals
- Navigation best practices
- Conversion optimization
- SEO fundamentals

Sector strategies LAYER ON TOP OF these universal principles, adding industry-specific trust cues, content architecture, and design psychology.

## How This Integrates

Sector-strategies is **step 0.5** in the build pipeline:

```
0. design-reference (optional)
→ 0.5 sector-strategies (YOU CHOOSE SECTOR) ← NEW
→ 1. design-system (reads docs/sector-brief.md)
→ 2. photo-manager
→ 3. page-builder
→ 4. deploy
```

Once you choose a sector and customize your brief, `design-system` uses it to generate tailwind.config.mjs and design-tokens.md with your sector's visual identity baked in.

## Available Sectors

**CRITICAL: Each sector template below is a CUSTOMIZATION STARTING POINT, not a final design. Your site must differentiate within your sector through:**
- Unique color palette (not the reference palette)
- Distinctive font pairing (not the example fonts)
- Your specific market positioning (budget vs. luxury, established vs. startup, etc.)
- Your competitor differentiation strategy

Read each sector description, then customize your sector-brief.md to reflect YOUR unique brand.

---

### Tour & Travel

**Trust cues**: Wanderlust, authentic experiences, booking confidence, guide expertise, cancellation flexibility, review social proof
**Visual identity**: Tour-type dependent (see travel-type-patterns.md: luxury=navy+gold+serif, adventure=bold+geometric, eco=green+organic, cultural=terracotta+warm). Distinctive brand colors per operator — never default sky blue + generic sans.
**Key components**: Search widget (above fold, 42% of bookings), destination cards, itinerary timelines, booking widget (sticky mobile), pricing display, review aggregate, trust badges, urgency signals, manual gallery/lightbox, guide profiles
**Content order**: Hero + search CTA → Featured destinations → Tour highlights → Testimonials → Trust signals → Booking CTA
**Distinctive traits**: Real photography, storytelling copy, "you could be there" language, transparent pricing, mobile-first (58%+ mobile bookings), YouTube-hosted destination videos

**Special note:** Tour & travel templates include 3 additional references: travel-branding.md (color psychology by tour type, typography pairing, photography direction, competitive differentiation), booking-conversion.md (3-second test, booking funnel, urgency/scarcity, trust architecture, pricing display, search widget, review design), travel-type-patterns.md (9 travel types with distinct design systems + branding personality framework).

### Corporate & Consulting

**Trust cues**: Leadership, expertise, client wins, market authority, thought leadership, industry credentials
**Visual identity**: Firm-type dependent (see corporate-type-patterns.md: strategy=navy+serif, tech=dark+geometric, financial=charcoal+gold, creative=bold+display, boutique=warm+personal). Distinctive brand colors per firm — never default corporate blue.
**Key components**: Hero with value prop, mega menu, leadership team, company stats with animated counters, case studies with metrics, thought leadership hub, investor relations, demo booking flow
**Content order**: Hero + demo CTA → Trust bar (client logos) → Solutions grid → Case studies → Leadership team → Insights hub → Contact
**Distinctive traits**: Professional photography, credential visibility, testimonials/client logos, downloadable resources, demo booking flow, thought leadership content

**Special note:** Corporate templates include 3 additional references: corporate-branding.md (color psychology by firm type, competitive differentiation with real examples, typography pairing, brand voice), client-conversion.md (B2B funnel, 6-second test, trust architecture, case study design pattern, CTA hierarchy), corporate-type-patterns.md (6 firm types with distinct design systems + branding personality framework).

### Personal & Portfolio

**Trust cues**: Authenticity, personality, quality work, expertise, approachability, niche authority
**Visual identity**: Creator-type dependent (see portfolio-type-patterns.md: designer=bold+saturated, developer=dark+electric, writer=warm+serif, photographer=minimal+image-dominant). Distinctive brand colors per individual — never default slate.
**Key components**: Hero with personality, portfolio/projects grid (masonry/uniform/card), about section with personal story, skills/experience, case study detail pages, blog (optional), contact CTA
**Content order**: Hero + primary CTA → Featured projects → About/story → Skills or experience → Testimonials → Contact
**Distinctive traits**: Personal photo/branding, curated project showcase, authentic storytelling, unique visual identity, case study pages, blog (if applicable)

**Special note:** Personal templates include 3 additional references: portfolio-branding.md (color psychology, typography by creator type, photography direction, brand voice), portfolio-conversion.md (portfolio funnel, project showcase design, social proof, CTA hierarchy), portfolio-type-patterns.md (7 creator types with distinct design systems + branding personality framework).

### Education

**Trust cues**: Credibility, structure, student success, enrollment conversion, parent trust, accreditation
**Visual identity**: School-type dependent (see school-type-patterns.md: private=serif+premium, public=accessible+warm, international=global+sophisticated, religious=reverent+warm). Distinctive brand colors per school — never default blue+white.
**Key components**: Enrollment CTA hero, programme cards, faculty profiles, event calendar, trust stats banner, audience segmentation tabs, virtual campus tour, fee structure table, testimonial grid or manually controlled proof gallery, parent portal
**Content order**: Hero + enrollment CTA → Trust stats → Academics grid → Faculty profiles → Testimonials → Events → Apply
**Distinctive traits**: Clear hierarchy, accreditation badges, student testimonials, enrollment clarity, audience segmentation (parents/students/alumni/donors), transparent fee structure, mobile-first (52%+ school traffic), YouTube-hosted campus tour videos

**Special note:** Education templates include 3 additional references: school-branding.md (color psychology, typography pairing, competitive differentiation, brand voice), enrollment-design.md (conversion funnel, parent trust architecture, CTA hierarchy, form design), school-type-patterns.md (7 school types with distinct design systems + branding personality framework).

### Healthcare

**Trust cues**: Expert credentials, patient safety, accessibility, appointment availability, accreditation, doctor qualifications
**Visual identity**: Facility-type dependent (see healthcare-type-patterns.md: hospital=blue+authoritative, specialist=teal+focused, wellness=sage+organic, paediatric=warm+friendly, mental-health=lavender+calming). WCAG AAA mandatory for body text. 18px minimum body, 48px touch targets.
**Key components**: Specialty finder, doctor profiles (photo+credentials+specialties+reviews), appointment booking widget, insurance badges, hours/emergency info, patient portal, trust stats banner, accessibility toolbar
**Content order**: Hero + appointment CTA → Trust stats → Specialties grid → Doctor profiles → Patient testimonials → Hours/Insurance/Accessibility → Contact
**Distinctive traits**: Accessibility-first (WCAG AAA body text), credential visibility, frictionless appointment booking, mobile-first (52%+ healthcare traffic), calm colour psychology, emergency information prominent

**Special note:** Healthcare templates include 4 additional references — the most comprehensive sector in the library. premium-hospital-playbook.md ($5K+ hospital website complete guide: multi-audience architecture, provider directory, condition landing pages, booking flows, patient portal showcase, telemedicine, competitive analysis, accessibility audit). healthcare-branding.md (clinical color system with semantic roles, colour-blind safety, accessibility-first design). patient-trust-design.md (patient funnel, trust architecture, provider directory, appointment booking, portal showcase, telemedicine). healthcare-type-patterns.md (9 facility types + premium feature matrix). Incorporates clinical-grade UI patterns adapted from healthcare application design.

### E-commerce

**Trust cues**: Product quality, customer reviews, fast checkout, secure payment, return policy, shipping transparency
**Visual identity**: Store-type dependent (see store-type-patterns.md: luxury=black+gold+sparse, fashion=trend-forward+lookbook, food=warm+appetite, tech=dark+spec-heavy, handmade=earth+artisan, beauty=blush+elegant, kids=bright+safe). Distinctive brand per store — never generic white.
**Key components**: Product cards (image+price+rating+CTA), category filters, product gallery with zoom, size/variant selectors, add-to-cart (always visible), trust badges (secure checkout, free returns), review section with photos, related products
**Content order**: Hero + shop CTA → Featured products → Categories → Customer reviews → Trust badges → Policy clarity → Newsletter
**Distinctive traits**: Social proof (reviews with photos), urgency signals (honest stock levels), transparent pricing (no hidden fees), guest checkout, mobile-optimised (60%+ mobile traffic)

**Special note:** E-commerce templates include 3 additional references: ecommerce-branding.md (color psychology for 8 hues, store type palettes, typography, photography, brand voice), shopping-conversion.md (shopping funnel, product page design, trust architecture, checkout optimisation, pricing display), store-type-patterns.md (7 store types with distinct design systems + branding personality framework). Cart abandonment is 70% — design must reduce friction at every step.

### Professional Services

**Trust cues**: Expertise, credentials, client wins, established track record, professional body memberships, years in practice
**Visual identity**: Service-type dependent (see services-type-patterns.md: accounting=green+gold+serif, legal=navy+burgundy+traditional, architecture=minimal+geometric, engineering=blue+technical, IT=teal+modern, real-estate=navy+gold+elegant, marketing=bold+creative). Distinctive brand per firm — never generic corporate.
**Key components**: Service cards with methodology, team profiles (credentials+specialisations+contact), client logos, case study cards (challenge+approach+results), testimonials (named+titled+company), consultation booking CTA
**Content order**: Hero + consultation CTA → Service grid → Trust bar (client logos) → Team bios → Case studies → Testimonials → Contact
**Distinctive traits**: Portfolio/case studies with quantified results, expert bios with credentials, premium photography, credential visibility, transparent process explanation

**Special note:** Professional services templates include 3 additional references: services-branding.md (color psychology for 7 hues, typography by 7 service types, brand voice), client-acquisition.md (trust-first test, client funnel, service page design pattern, testimonial strategy), services-type-patterns.md (7 service types with distinct design systems + branding personality framework). 82% of clients research providers online before making contact.

### Hobbyist/Creator

**Trust cues**: Authenticity, personal brand, niche expertise, behind-the-scenes process, community engagement, follower/subscriber counts
**Visual identity**: Creator-type dependent (see creator-type-patterns.md: artist=bold+saturated, developer=dark+terminal, writer=warm+literary, photographer=minimal+image-dominant, YouTuber=bold+energetic, craftsperson=warm+artisanal, educator=accessible+structured). Bold personality-driven fonts; high-saturation accent + authentic substrate.
**Key components**: Portfolio grid (masonry/uniform/card by type), process/behind-scenes gallery, subscribe/newsletter CTA with lead magnet, community links (Discord), social proof (follower counts, press mentions), shop/commission section, about story
**Content order**: Hero + personality → Best work → About teaser → Subscribe CTA → Social proof → Community/shop
**Distinctive traits**: Personal voice, authentic storytelling, niche focus, less corporate, more human, email capture priority, YouTube-hosted content videos

**Special note:** Hobbyist/creator templates include 3 additional references: creator-branding.md (color psychology for 8 hues, typography by 7 creator types, photography, brand voice, logo types), engagement-design.md (creator funnel, portfolio showcase, subscribe strategy, community building, monetisation), creator-type-patterns.md (7 creator types with distinct design systems + branding personality framework).

### Nonprofit / Charity / NGO

**Trust cues**: Mission clarity, impact proof, financial transparency, beneficiary dignity, credentials, partner logos
**Visual identity**: Sector-dependent (see sub-sector patterns: environment=green+gold, healthcare=blue+coral, humanitarian=red+navy, research=blue+gold, arts=bold+vibrant). Warm + professional, never generic "charity blue."
**Key components**: Impact-tied donation CTA, featured story grid or manually controlled story gallery, stat counters, trust bar (partner logos), team section, contact with multiple offices, multilingual support
**Content order**: Hero + mission CTA → Trust bar → Impact stats → Beneficiary stories → Programs/services → How to help → News/events → Contact
**Distinctive traits**: Authentic photography (never stock), dignity-first storytelling, impact-tied donation amounts ("$50 trains one farmer"), multiple audience paths (donors, volunteers, beneficiaries, partners, media), WCAG AA+ accessibility, mobile-first (52% nonprofit traffic), YouTube-hosted video embeds

**Special note:** Nonprofit templates include 3 additional references: color-psychology.md (hue-by-hue guide with competitive differentiation), storytelling-design.md (dignity principle, trust architecture, donation conversion), sub-sector-patterns.md (6 sub-sector design systems). Stories are remembered 22x more than facts — design must channel empathy into action.

### Law Firms / Legal

**Trust cues**: Attorney credentials, peer review ratings (Martindale, Super Lawyers), case results with disclaimers, named client testimonials, geographic specificity, free consultation offer, clear practice area coverage, response time commitment
**Visual identity**: Practice-type dependent (see legal-type-patterns.md: personal-injury=trust-blue+warm-amber, family=teal+sage, criminal=deep-navy+charcoal, estate=heritage-blue+gold, immigration=warm-blue+terracotta, business=slate+dark-teal). Never generic navy+gold scales-of-justice.
**Key components**: Hero with specific problem statement + CTA, practice area cards (client language, not legal terms), attorney profiles (client-centered bios, not credential CVs), trust signals bar, named testimonials with disclaimer, contact section with phone (tap-to-call) + form + response time commitment, footer with all practice areas + disclaimer language
**Content order**: Hero + free consultation CTA → Practice areas → Trust signals → Attorney profiles (brief) → Social proof → Contact (phone + form)
**Distinctive traits**: Client-centered copy (not credential-first), separate page per practice area (local SEO), attorney-client disclaimer on all forms, ethics-compliant trust claims, mobile-first (most legal searches happen on mobile during crisis), no guaranteed outcome language, no "expert" claims without bar certification

**Special note:** Legal templates include 4 additional references — the most ethics-sensitive sector in the library. legal-branding.md (color psychology by practice area, the Client-Centered vs. Traditional design split, Value Proposition Framework, One Great Thing differentiation, banned phrases, voice by practice area). client-trust-design.md (client psychology, above-the-fold architecture, attorney profile structure, three tiers of information, trust signals by tier, contact form design with disclaimer, local SEO checklist, conversion killers). legal-type-patterns.md (8 practice area types with distinct design systems: personal injury, family law, criminal defense, estate planning, immigration, business law, employment law, workers' comp). ethics-constraints.md (bar advertising rules, prohibited claims, required disclaimers, developer responsibilities, pre-launch review checklist). Law firm websites must balance conversion optimization with bar ethics compliance — both are mandatory.

### App Landing Pages

**💡 For app developers building their own landing pages**

**Trust cues**: App store badges, user/download count, star ratings, press mentions, security badges (for finance/health), named testimonials with specific results
**Visual identity**: App-type dependent (see app-type-patterns.md: SaaS=blue+professional, consumer=warm+inviting, dev-tools=dark+terminal, health=green+calm, finance=navy+trust, gaming=bold+neon, education=warm+structured). CTA button must be highest contrast element on page.
**Key components**: Hero with sticky CTA + app screenshot, social proof bar (user count + rating + press logos), benefit cards (3-4 max), how-it-works steps, feature deep-dive with screenshots, named testimonials, pricing tiers (3 max), FAQ, app store badges, sticky mobile CTA bar
**Content order**: Hero + CTA + screenshot → Social proof bar → Key benefits → How it works → Feature deep-dive → Testimonials → Pricing → FAQ → Final CTA
**Distinctive traits**: Mobile-first design (70%+ traffic), conversion optimization focus, clear problem-solution narrative, A/B testing strategy, YouTube-hosted demo videos

**Special note:** App landing pages include 3 additional references: app-branding.md (color psychology for 8 hues, CTA color strategy, typography by app type, screenshot strategy, copy frameworks), app-conversion.md (download funnel, hero design, CTA strategy, pricing page design, trust architecture, A/B testing), app-type-patterns.md (7 app types with distinct design systems + branding personality framework). Conversion frameworks (AIDA, PAS, FAB, BAB) guide copy structure.

## How to Use This Skill

### Step 1: Choose Your Sector

Read the sector descriptions above. Which best matches your client's business?

If multiple apply, choose the **primary customer intent**:
- Eco-tourism education? → Tourism (primary) with education trust signals
- Specialty clinic in hospital? → Healthcare (primary) with professional services polish
- Creator selling courses? → Hobbyist/Creator (primary) with professional services credibility

### Step 2: Customize Your Sector Brief (REQUIRED — Do Not Skip)

**CRITICAL: This step determines whether your site looks generic or distinctive.**

Copy the sector template into your client project:

```
your-client-project/
├── docs/
│   ├── company-profile.md    (client provides)
│   ├── services.md           (client provides)
│   ├── style-brief.md        (client provides)
│   └── sector-brief.md       ← COPY TEMPLATE HERE & CUSTOMIZE
```

Template location: `sector-strategies/templates/{sector}/sector-brief-template.md`

**Answer EVERY question thoroughly:**
1. **What is your ONE unique difference** compared to competitors?
2. **Define YOUR brand colors** (not the sector reference palette)
3. **Choose YOUR fonts** (not the example fonts — use Fontsource for distinctive options)
4. **What is your visual style?** (photography approach, vibe, distinctive traits)
5. **How do you build trust?** (rank trust elements by importance)
6. **What is your ideal customer's pain point?** (this shapes emotional design)

**Do NOT:**
- Use the reference colors directly
- Use example fonts without customizing
- Skip the differentiation questions
- Default to the sector template — customize it for YOUR brand

Save as `docs/sector-brief.md`. The design-system skill will read this brief and generate YOUR unique visual identity.

### Step 3: Run design-system

The design-system skill now has three inputs:
1. `docs/sector-brief.md` (from this skill)
2. `docs/style-brief.md` (from client)
3. `sector-strategies/templates/{sector}/design-tokens.md` (reference palette)

It generates:
- `tailwind.config.mjs` (sector-optimized colors, typography, spacing)
- `design-tokens.md` (your sector's visual language)
- `src/styles/global.css` (animations, utilities, reset for sector)

### Step 4: Continue Pipeline

photo-manager → page-builder → deploy

---

## What's in the Templates

Each `sector-strategies/templates/{sector}/` contains files to guide customization:

**sector-brief-template.md** ⭐ CRITICAL
Customization questionnaire for your client. Copy to `docs/sector-brief.md` and fill in EVERY answer.
- This questionnaire drives differentiation
- Your answers shape the design-system output
- Skipping this results in generic design
- REQUIRED: Answer all sections fully

**design-tokens.md** (REFERENCE ONLY)
Reference palette showing ONE example of how this sector could be designed.
- Example colors (NOT to be used as-is)
- Example typography (NOT to be used as-is)
- Color psychology (to inform YOUR choices)
- DO NOT use these directly — customize them via your sector-brief
- Anti-homogeneity principle: Every site needs different colors/fonts

**component-patterns.md**
HTML/Tailwind examples for sector-specific UI patterns: buttons, cards, CTAs, forms.
- Use these as pattern inspiration
- Style them with YOUR brand colors/fonts
- Do not copy directly — adapt to your visual identity

## Common Questions

**Q: Will all sites in the same sector look the same?**
A: NO — if you customize your sector-brief properly. Each site will have unique colors, fonts, and visual identity. The sector framework ensures trust signals are appropriate to the industry. Customization ensures differentiation.
- Bad: Use tour-travel template defaults → all travel sites look similar
- Good: Answer your sector-brief with unique colors/fonts → distinctive travel site

**Q: Can I skip the sector-brief customization?**
A: NO. This results in generic design. The sector-brief is REQUIRED to drive differentiation.

**Q: Can I mix sectors?**
A: No. Choose one primary sector and lean into it. Mixing dilutes trust signals. If your business is hybrid (e.g., eco-tourism education), choose the PRIMARY sector and customize the sector-brief to address secondary aspects.

**Q: My sector isn't listed. What do I do?**
A: Start with the closest sector template. Customize the sector-brief fully. After delivery, document what worked and propose it as a new sector template for the library.

**Q: When do I customize sector-brief.md?**
A: Before running design-system. The design-system skill reads your sector-brief to generate YOUR unique visual identity.

**Q: How do I ensure my site doesn't look like another site?**
A:
1. Complete your sector-brief with genuine differentiation answers
2. Choose unique colors (not the reference palette)
3. Choose distinctive fonts from Fontsource
4. Have design-reference analyze your competitors (so you know what to avoid)
5. Let design-system generate unique output based on your inputs

## The 80/20 Prototypicality Rule

~80% of your website patterns should match niche conventions — navigation structure, colour schemes, homepage layout, content hierarchy. This is what visitors in your sector expect. Prototypical feels familiar, and familiarity evokes trust.

Uniqueness comes from the remaining ~20%: distinctive fonts, accent colours, brand personality, copywriting voice, and the specific visual identity generated from your sector-brief.

**Don't compare your site to famous companies** (Amazon, Apple) unless your business is at the same scale with the same audience. Only compare to websites in the same niche, similar size, with similar target audiences. Large companies A/B test their choices — their patterns are data-driven, not arbitrary.

## Next Steps

1. Choose your sector from the list above
2. Copy `sector-strategies/templates/{sector}/sector-brief-template.md` → `docs/sector-brief.md`
3. Answer all customization questions in your brief
4. Run the `design-system` skill
5. Proceed with photo-manager, page-builder, deploy
