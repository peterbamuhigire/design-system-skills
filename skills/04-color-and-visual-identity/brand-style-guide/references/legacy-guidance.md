# Brand Style Guide Skill

Produce `docs/brand-style-guide.md` — a PDF-ready document the client receives, owns, and uses to maintain brand consistency across all future communications.

This document justifies premium project pricing. A tightly written style guide makes the brand feel reliable to customers and gives the client everything they need to brief future designers, copywriters, and partners without losing brand integrity.

## Purpose and Deliverable

The output is `docs/brand-style-guide.md`. It is:
- Written for the client, not for Claude or the development team
- Formatted so it converts cleanly to PDF (headings, tables, ruled sections)
- Self-contained — anyone reading it cold can apply the brand correctly
- Versioned and dated so the client can track revisions

This is not an internal design token file. It is a client-facing brand asset.

## Prerequisites

Read both files before starting. Do not proceed if either is missing — request them from the client first.

1. `docs/brand-brief.md` — produced by brand-strategy; contains mission, values, positioning statement, brand mantra, target audience, and archetype
2. `design-tokens.md` — produced by design-system; contains all colour hex codes, font names, spacing values, and breakpoints

Also read `docs/en/company-profile.md` for company name, sector, and contact details (for the document header and Document Control section).

## How to Write the Document

Use the template at `brand-style-guide/references/style-guide-template.md` as the structural scaffold. Fill every placeholder with real client data. Do not leave placeholder text in the final document.

Apply these rules throughout:
- Write in plain, direct English — the client is not a designer
- Explain the "why" behind each rule, briefly (one sentence)
- Use tables for anything that has more than three values
- Use bold for rules; use plain text for explanations
- Never fabricate brand decisions — every decision must come from `docs/brand-brief.md` or `design-tokens.md`

---

## Section 1: Brand Foundation

One page. A distilled summary of who the brand is and what it stands for.

Write these five elements, each as a short labelled block:

**Mission** — one sentence: what the company does and for whom.
**Values** — three to five values, each with a one-sentence explanation.
**Positioning Statement** — the brand's strategic position in the market. Use this format: "For [target audience] who [need], [Brand] is the [category] that [benefit]. Unlike [competitor], [Brand] [key differentiator]."
**Brand Mantra** — the two-to-four-word emotional essence of the brand (internal use; the distilled identity).
**Brand Archetype** — name the archetype and explain in two sentences how it shapes the brand's personality and visual choices. Reference the 12 archetypes from Leland's Brand Mapping framework (Hero, Ruler, Caregiver, Creator, Explorer, Innocent, Sage, Rebel, Lover, Jester, Everyman, Magician).

Pull all content from `docs/brand-brief.md`. Do not invent or embellish.

---

## Section 2: Logo System

Document every approved logo variant and every usage rule.

### Approved Variants
List all logo files provided by the client or created during the project:
- Primary (full colour, on light background)
- Reversed (white or light, on dark background)
- Monochrome (black)
- Icon-only / mark (if one exists)
- Horizontal layout and stacked layout (if both exist)

For each variant: state the filename, when to use it, and when not to use it.

### Clear Space Rule
State the minimum clear space around the logo using a unit derived from the logo itself (e.g., "x = the height of the logo letterforms; maintain x on all four sides").

### Minimum Size
State the minimum reproduction size in pixels (for digital) and millimetres (for print). Below this size the logo loses legibility.

### Colour Backgrounds
List which background colours the logo may appear on and which it may not. Include specific hex values.

### The 10 Logo Don'ts
Write exactly 10 rules covering the most common misuses. Examples of categories to cover: stretching, rotating, dropping shadow, applying gradient, using on a busy photographic background, changing colours, adding effects, rearranging elements, using old versions, using at prohibited sizes.

### File Format Guide
| Format | Use case |
|--------|----------|
| SVG | Website, digital, scalable at any size |
| PNG (transparent) | Presentations, documents, email signatures |
| PDF (vector) | Print production, large format |
| JPG | Last resort — only when transparency is not supported |

---

## Section 3: Colour Palette

The colour palette is the single most powerful brand recognition tool. Colour increases brand recognition by up to 80%. Document it completely so the client can reproduce exact colours in any medium.

### Colour Card Format

For each colour (primary, secondary, accent, neutral variants), produce a block with:

| Field | Example |
|-------|---------|
| Name | Forest Green |
| Role | Primary brand colour |
| Hex | #2D6A4F |
| RGB | 45, 106, 79 |
| CMYK | 58, 0, 25, 58 |
| Pantone | 7728 C (nearest match) |
| WCAG on white | AA (contrast ratio: 5.4:1) |
| WCAG on black | Fail (contrast ratio: 1.9:1) |
| Psychology note | Communicates growth, trust, environmental responsibility |
| Primary use | Headings, buttons, nav bar |
| Never use for | Body text on white (fails WCAG AA at small sizes) |

### Colour Psychology Note (per colour)
Draw from Nahai's colour-psychology framework. For each colour, write one sentence explaining what emotion or association it triggers in the target audience. This justifies the palette to the client and trains future designers.

### Usage Proportions
State the intended proportion of each colour in layouts:
- Primary: [percentage] of all branded surfaces
- Secondary: [percentage]
- Accent: [percentage] — used only for CTAs and highlights
- Neutral (white/off-white/grey): remainder

### Accessibility Rule
State this explicitly: "All body text must achieve WCAG AA (4.5:1 contrast ratio). All large text and UI components must achieve WCAG AA (3:1). Colour is never used as the sole means of conveying information."

---

## Section 4: Typography System

Typography communicates personality before a word is read. Serif signals authority and tradition. Sans-serif signals modernity and approachability. Document every typographic decision so the brand voice stays consistent across media.

### Font Specifications Table

| Role | Font Name | Style | Source |
|------|-----------|-------|--------|
| Heading (H1–H2) | [Name] | Bold / ExtraBold | Fontsource (self-hosted) |
| Heading (H3–H4) | [Name] | SemiBold | Fontsource (self-hosted) |
| Body | [Name] | Regular / Medium | Fontsource (self-hosted) |
| Accent (optional) | [Name] | Italic / Regular | Fontsource (self-hosted) |

For each font: state the brand personality it conveys (one sentence using Nahai's typography psychology principles).

### Type Scale

| Tag | Size (rem) | Size (px) | Weight | Line Height | Letter Spacing |
|-----|-----------|-----------|--------|-------------|----------------|
| H1 | 3.5 | 56 | 800 | 1.1 | -0.02em |
| H2 | 2.5 | 40 | 700 | 1.15 | -0.01em |
| H3 | 1.875 | 30 | 600 | 1.2 | 0 |
| H4 | 1.5 | 24 | 600 | 1.25 | 0 |
| Body | 1 | 16 | 400 | 1.6 | 0 |
| Small | 0.875 | 14 | 400 | 1.5 | 0.01em |
| Label | 0.75 | 12 | 600 | 1.4 | 0.05em |

Fill with actual values from `design-tokens.md`.

### Web vs Print
State which fonts are licensed for web (self-hosted via Fontsource) and which are available for print. If print equivalents differ, name them explicitly.

### Maximum Fonts Rule
State this explicitly: "A maximum of two typefaces are used on the website. Every additional font increases cognitive load and weakens brand cohesion." (Nahai, processing fluency principle.)

---

## Section 5: Spacing and Grid

Consistent spacing creates visual rhythm. It is the invisible structure that makes layouts feel organised and professional.

### Base Unit
State the base spacing unit (8px or 4px grid system). All spacing values are multiples of this unit.

### Spacing Scale

| Token | Value | Use case |
|-------|-------|----------|
| space-1 | 4px | Fine-grained internal padding |
| space-2 | 8px | Icon-to-label gaps, inline spacing |
| space-3 | 16px | Default padding inside components |
| space-4 | 24px | Component internal sections |
| space-6 | 48px | Between related content blocks |
| space-8 | 64px | Major section gaps |
| space-12 | 96px | Large section breaks |
| space-16 | 128px | Hero padding, major page divisions |

Fill with actual values from `design-tokens.md`.

### Layout Grid

| Screen | Columns | Gutter | Max Width |
|--------|---------|--------|-----------|
| Mobile (375px) | 4 | 16px | 100% |
| Tablet (768px) | 8 | 24px | 100% |
| Desktop (1280px+) | 12 | 32px | 1280px |

### Responsive Breakpoints
List the three breakpoints with their pixel values and the design intent at each.

---

## Section 6: Photography Style

Professional photography is proof of brand quality. Inconsistent or generic photography undermines every other brand investment. Document the visual language of approved photography so the client can brief photographers and evaluate stock images without consulting the agency.

### Mood Words
List five to seven words that describe the photographic tone: e.g., "warm, candid, high-contrast, editorial, documentary, vibrant, intimate."

### Subject Guidelines
Describe what the photography should show: people (and if so, who), environments, products, activities. Be specific about the demographic of people shown — they should resemble the target customer (Nahai: liking is triggered by similarity).

### Technical Standards
| Attribute | Requirement |
|-----------|-------------|
| Minimum resolution | 2000px on the long edge for web; 3000px for print |
| Colour treatment | [e.g., warm-toned, natural white balance, consistent grade] |
| Aspect ratios | 16:9 for hero images; 1:1 for team portraits; 4:3 for editorial |
| File format | JPG for photographs; max 500KB after compression |

### The 10 Photography Do/Don'ts
Write five dos and five don'ts. Dos: authentic moments, natural lighting, real team and customers, consistent colour grade, high resolution. Don'ts: generic stock photography with posed models (this destroys trust — Nahai), heavy filters, watermarks, inconsistent colour temperatures, low-resolution images.

### Stock Photo Policy
State the client's position on stock photography: approved with conditions (authentic-looking, matches brand mood, no obvious stock clichés), or banned entirely. Explain the trust rationale.

### AI-Generated Image Policy
State clearly: AI-generated images are not approved for use in client-facing materials without explicit client consent and disclosure. This protects brand authenticity.

---

## Section 7: Iconography

State the icon library used (Lucide Icons for all projects built with these skills).

### Style Rules
| Rule | Standard |
|------|----------|
| Weight | Stroke-based, 1.5px default stroke |
| Size | 16px (inline), 24px (UI standard), 32px (feature icons), 48px (large feature) |
| Colour | Inherit from the surrounding text colour, or use the primary brand colour |
| Background | Icons do not use background shapes unless part of a specific component |
| Meaning | Every icon must reinforce, not replace, a text label in navigation |

State this explicitly: "Icons are never used as the sole means of conveying information. Every icon appears with a text label or accessible aria-label."

---

## Section 8: Voice and Tone

The brand's visual identity is what people see. The voice is what they hear. Both must be consistent.

### Brand Personality in Words
List five adjectives that describe how the brand sounds: e.g., "confident, warm, direct, expert, never condescending."

### Three Voice Principles
Write three principles — each with a name, a one-sentence definition, and a brief explanation. These are the rules writers follow when creating any content for the brand.

Example format:
**[Principle name]:** [One-sentence definition.] [Two-to-three sentences of explanation and guidance.]

### Tone by Context

| Context | Tone | Example phrase |
|---------|------|----------------|
| Website headlines | [e.g., Bold, direct, benefit-first] | [Example] |
| Email subject lines | [e.g., Conversational, curiosity-driven] | [Example] |
| Social media captions | [e.g., Warm, community-focused] | [Example] |
| Error messages | [e.g., Calm, helpful, never blaming] | [Example] |
| Sales pages | [e.g., Persuasive, evidence-based, urgency through value] | [Example] |
| Support responses | [e.g., Empathetic, solution-oriented] | [Example] |

### Banned Words and Phrases
List at least 15 words or phrases the brand never uses, with a one-word reason for each ban. Common examples: "revolutionary" (overused), "world-class" (unverifiable), "synergy" (jargon), "leverage" as a verb (corporate), "solutions" alone (meaningless), "passion" in marketing copy (cliché).

### Before/After Rewrite Examples
Provide five rewrites showing the brand voice applied:

| Before (off-brand) | After (on-brand) |
|--------------------|-----------------|
| [Weak or generic phrase] | [Rewritten in brand voice] |

Draw on the client's actual language from `docs/brand-brief.md`. Mine their own words wherever possible.

---

## Section 9: Usage Rules — Always and Never

A tight style guide is built around two lists: what the brand always does and what it never does. These make the brand feel reliable and consistent to customers. (Drew/Williams, Brand Strategy 101.)

### Always (10 rules)

Write 10 "always" rules — non-negotiable standards. Cover: logo placement, colour usage, tone, photography type, accessibility compliance, language standard, legal notices, CTA style, spacing rules, social media profile consistency.

Format: **Always [verb phrase].** [One-sentence explanation of why.]

### Never (10 rules)

Write 10 "never" rules — things that are prohibited without exception. Cover: logo misuse, off-brand colours, generic stock photography, informal or slang language (if not part of the brand voice), mixing typefaces outside the system, accessibility violations, claims that cannot be substantiated.

Format: **Never [verb phrase].** [One-sentence explanation of why.]

---

## Section 10: Document Control

Close the document with a formal control block. This makes the style guide feel like a professional deliverable, not a draft.

| Field | Value |
|-------|-------|
| Document title | [Company Name] Brand Style Guide |
| Version | 1.0 |
| Date issued | [Project completion date] |
| Prepared by | [Agency name] |
| Approved by | [Client name / role] |
| Next review | [12 months from issue date] |
| Scope | All branded communications in English, French, and Kiswahili |

State: "This document supersedes all previous brand guidelines. Questions about interpretation should be directed to [agency contact]."

---

## Output Format

Write `docs/brand-style-guide.md` as clean, structured markdown:
- Use H1 for the document title only
- Use H2 for each section number and name
- Use H3 for subsections within sections
- Use tables for all multi-column data (colours, typography, spacing, do/don't comparisons)
- Use bold for all rules and requirements
- Use plain text for explanations
- Add a horizontal rule (`---`) between each major section
- Do not use emojis, icons, or decorative characters — they do not survive PDF conversion reliably
- Keep line lengths under 100 characters for clean PDF wrapping

When converting to PDF, the client should use a markdown-to-PDF tool such as Pandoc with a custom CSS stylesheet, or paste into a design tool such as Notion, Craft, or Google Docs and export. Recommend this to the client at the end of the document.

---

## Quality Gate: The 3 Cs

Before marking this skill complete, verify the style guide passes Leland's 3 Cs measurement framework:

**Consistency** — Does every section of the guide present the same brand? Check that the colour used in the typography section matches the colour card. Check that the voice principles align with the archetype. Check that the photography mood words match the brand personality words.

**Constancy** — Does the guide give the client enough rules to show up consistently over time? Every major communication channel must be covered in the tone-by-context table. Photography standards must be specific enough that the client can brief a photographer independently.

**Congruency** — Do the external expressions (logo, colour, typography, voice) match the internal brand reality documented in `docs/brand-brief.md`? If the brand claims to be "approachable and warm" but the typography system uses a cold geometric sans-serif, flag the mismatch and resolve it before finalising.

If any of the three Cs fails, revise the relevant section before outputting the file.

---

## Integration

**Reads from:**
- `docs/brand-brief.md` (brand-strategy output)
- `design-tokens.md` (design-system output)
- `docs/en/company-profile.md` (company name, sector, contact)
- `brand-style-guide/references/style-guide-template.md` (structural scaffold)
- `brand-style-guide/references/design-decisions.md` (colour/typography psychology, Keller audit)

**Produces:**
- `docs/brand-style-guide.md` — client deliverable

**Referenced by:**
- `brand-alignment/SKILL.md` — uses the always/never table and voice principles as quality gate criteria
- `page-builder/SKILL.md` — applies typography system and spacing scale
