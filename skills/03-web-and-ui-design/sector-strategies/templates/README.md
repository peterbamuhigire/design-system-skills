# Sector Strategy Templates

This directory contains design templates for six different business sectors. Each sector has:

- **sector-brief-template.md** — Customization questionnaire (copy to `docs/sector-brief.md`)
- **design-tokens.md** — Reference color palette, typography, spacing, components
- **component-patterns.md** — HTML/Tailwind patterns optimized for that sector

## Available Sectors

### 🌍 Tour & Travel
*Wanderlust, discovery, authenticity, adventure*

Use when building sites for tour operators, travel agencies, adventure companies, eco-tourism. Key components: destination cards, itinerary timelines, booking widgets, destination galleries.

**Files**: ✅ Complete
- sector-brief-template.md
- design-tokens.md
- component-patterns.md

---

### 🎓 Education
*Credibility, structure, enrollment, student success*

Use when building sites for schools, universities, training institutes, online courses. Key components: course catalog, staff directory, event calendar, application CTAs.

**Files**: 🚧 In progress — Template structure ready, awaiting sector-specific content

---

### 🏥 Healthcare
*Trust, expertise, accessibility, appointment booking*

Use when building sites for hospitals, clinics, dental practices, specialist offices. Key components: specialty finder, doctor profiles, appointment button, insurance badges, hours of operation.

**Files**: 🚧 In progress — Template structure ready, awaiting sector-specific content

---

### 🛒 E-commerce
*Product trust, customer reviews, fast checkout, conversion*

Use when building sites for online shops, product sellers, local craftspeople. Key components: product cards with reviews, quantity selectors, checkout CTA, trust badges.

**Files**: 🚧 In progress — Template structure ready, awaiting sector-specific content

---

### 💼 Professional Services
*Expertise, credentials, client wins, established credibility*

Use when building sites for law firms, consulting, accounting, design agencies. Key components: service cards, team profiles, client logos, case studies, testimonials.

**Files**: 🚧 In progress — Template structure ready, awaiting sector-specific content

---

### 🎨 Hobbyist/Creator
*Authenticity, personal brand, niche expertise, community*

Use when building sites for artists, photographers, writers, makers, YouTubers, solopreneurs. Key components: portfolio grid, behind-the-scenes, subscribe CTA, community signals.

**Files**: 🚧 In progress — Template structure ready, awaiting sector-specific content

---

## How to Use These Templates

1. **Read the main SKILL.md** in the parent directory (`../SKILL.md`)
2. **Choose your sector** based on the client's business
3. **Copy the sector folder** template files into your client project:
   ```
   your-client-project/
   ├── docs/
   │   └── sector-brief.md  ← Copy from sector-strategies/templates/{sector}/sector-brief-template.md
   ```
4. **Customize** your sector-brief by answering all questions
5. **Run design-system** skill — it reads your brief and generates design tokens

---

## Creating New Sectors

If you're building for a sector not listed above:

1. Pick the closest existing sector as a starting point
2. Customize the template for your specific industry
3. After client delivery, document what you learned
4. Propose it as a new sector template via GitHub issue

---

## Contributing

Each sector template should include:

- **sector-brief-template.md**: ~50–70 lines, focused customization questions
- **design-tokens.md**: ~80–100 lines, color palette, typography, spacing, components
- **component-patterns.md**: ~100–150 lines, 6–8 HTML/Tailwind code examples

Keep templates focused and practical — avoid generic advice. Write from the perspective of "here's what works for this sector because..."

---

**Questions?** See the main SKILL.md for workflow and integration details.
