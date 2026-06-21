# Color Selection for Websites

Transform brand colors into cohesive, psychologically-optimized website color palettes that look intentional, professional, and industry-authentic.

## When to Use This Skill

✅ User provides primary brand colors (hex, RGB, or description)
✅ Designing a new website color system
✅ Refining existing colors for better contrast or accessibility
✅ Need complementary accent colors for CTAs, alerts, or secondary elements
✅ Building color tokens for Tailwind config or design system
✅ Ensuring WCAG accessibility compliance (4.5:1 contrast ratio)

## Core Workflow

### 1. Assess Brand Colors

Ask for the user's brand colors. Accept:
- **Hex codes** (e.g., `#3B82F6`)
- **RGB values** (e.g., `rgb(59, 130, 246)`)
- **Color descriptions** (e.g., "deep ocean blue" → convert to hex)
- **Visual examples** (inspect color from uploaded image or screenshot)

Typically users provide 1-3 primary colors. If only one provided, generate complementary palette from it. If multiple provided, evaluate harmony.

### 2. Analyze Color Context

Determine:
- **Industry/sector** (healthcare, e-commerce, finance, creative, education, etc.)
- **Tone** (corporate/conservative, modern/tech, friendly/approachable, luxe/premium)
- **Target audience** (millennials, professionals, children, enterprise clients)
- **Existing brand associations** (does primary color already represent something in their industry?)

**Reference:** See `references/color-psychology.md` for industry-specific color guidance and psychological associations.

### 3. Generate Palette Using Color Theory

Select the most appropriate color scheme based on harmony principles:
- **Monochromatic** — variations of one color (cohesive, safe)
- **Analogous** — adjacent colors on wheel (harmonious, balanced)
- **Complementary** — opposite colors on wheel (high contrast, dynamic)
- **Split-Complementary** — primary + two neighbors of complement (balanced contrast)
- **Triadic** — three evenly-spaced colors (vibrant, playful)
- **Tetradic** — four colors in two complementary pairs (complex, rich)
- **Achromatic** — grays, blacks, whites (timeless, minimalist)

**Reference:** See `references/color-schemes.md` for detailed explanations, HSL adjustments, and scheme-specific guidance.

### 4. Apply 60-30-10 Rule

Distribute colors by visual weight:
- **60%** — Primary color (backgrounds, large surfaces)
- **30%** — Secondary color (supporting elements, sections)
- **10%** — Accent color (CTAs, highlights, alerts)

Example:
```css
--color-primary: #3B82F6;      /* 60% */
--color-secondary: #F3F4F6;    /* 30% */
--color-accent: #DC2626;       /* 10% */
```

### 5. Build Complete System

Generate 5-7 color tokens:
1. **Primary** — primary brand color
2. **Secondary** — supporting color
3. **Accent** — CTA and high-emphasis elements
4. **Success** — positive feedback (green-ish)
5. **Warning** — cautionary feedback (amber-ish)
6. **Error** — destructive/alert feedback (red-ish)
7. **Neutral** — text, borders, backgrounds (grays)

All must meet **WCAG AA standards** (4.5:1 contrast for text, 3:1 for UI components).

**Reference:** See `references/accessibility-contrast.md` for contrast ratio calculation and verification.

### 6. Verify Accessibility

Test each color pair that will be used together:
- **Text on background**: Must be 4.5:1 (normal) or 3:1 (large 18pt+)
- **UI components**: Must be 3:1 (borders, icons, outlines)

Use formula: `(lighter color luminance + 0.05) / (darker color luminance + 0.05)`

Flag any combinations failing WCAG AA. Suggest adjustments (lighten/darken) to achieve compliance.

### 7. Output as Configuration

Provide color tokens as:
- **Tailwind CSS variables** (for `tailwind.config.mjs`)
- **CSS custom properties** (for `global.css`)
- **Design tokens JSON** (for reference)

Example Tailwind:
```javascript
colors: {
  primary: '#3B82F6',
  secondary: '#F3F4F6',
  accent: '#DC2626',
  success: '#10B981',
  warning: '#F59E0B',
  error: '#EF4444',
  neutral: '#6B7280'
}
```

## Industry-Specific Guidance

Before finalizing palette, reference `references/industry-color-psychology.md` for sector-specific expectations:

- **Healthcare/Wellness** — trust blues, calming greens, avoid alarming reds
- **E-Commerce** — action-oriented reds/oranges, trust blues, warm accents
- **Finance/Corporate** — authoritative blues/grays, minimal accent, high contrast
- **Creative/Design** — bold, unexpected colors, high saturation
- **Education** — welcoming blues/greens, accessible contrast
- **Food/Hospitality** — appetite-stimulating warm tones, welcoming accents

## Modern Colour Space: OKLCH

**Prefer OKLCH over HSL** for perceptually uniform colour manipulation. OKLCH ensures that colours with the same lightness value actually *look* equally light — HSL does not (HSL yellow at 50% looks much brighter than HSL blue at 50%).

```css
/* OKLCH: oklch(lightness chroma hue) */
--color-primary: oklch(0.55 0.25 250);    /* Perceptually accurate blue */
--color-primary-light: oklch(0.75 0.15 250); /* Same hue, lighter */
--color-primary-dark: oklch(0.35 0.30 250);  /* Same hue, darker */
```

**When to use:** Generating shade scales, adjusting lightness for hover/active states, creating tinted neutrals, and ensuring dark mode colour consistency.

**Fallback:** Pre-compute hex values from OKLCH for use in Tailwind config and CSS custom properties. OKLCH is for *design decisions*, hex is for *shipping code* (until browser support is universal).

## Tinted Neutrals — Never Pure Gray

**Never use pure gray** (`#808080`, `hsl(0, 0%, 50%)`). Pure grays look cold, lifeless, and disconnected from the brand. Always tint neutrals with a subtle hint of the primary brand colour.

**Rule:** Add **0.005–0.01 chroma** in OKLCH (or 3–8% saturation in HSL) using the primary colour's hue angle.

```css
/* BAD: pure grays */
--neutral-100: #f5f5f5;
--neutral-500: #737373;
--neutral-900: #171717;

/* GOOD: warm-tinted neutrals (for a warm brand) */
--neutral-100: oklch(0.96 0.005 60);   /* Barely warm off-white */
--neutral-500: oklch(0.55 0.008 60);   /* Subtly warm mid-gray */
--neutral-900: oklch(0.15 0.010 60);   /* Deep warm near-black */

/* GOOD: cool-tinted neutrals (for a cool brand) */
--neutral-100: oklch(0.96 0.005 240);  /* Barely cool off-white */
--neutral-500: oklch(0.55 0.008 240);  /* Subtly cool mid-gray */
--neutral-900: oklch(0.15 0.010 240);  /* Deep cool near-black */
```

**Never use pure black** (`#000000`) for text — use `oklch(0.15 0.01 hue)` or equivalent tinted near-black. Pure black on white creates harsh contrast that causes eye fatigue.

## Dark Mode Colour Rules

When generating dark mode palettes:

- **Desaturate accent colours** — bright saturated colours on dark backgrounds cause glare; reduce chroma by 15–25%
- **Different shadow approach** — dark mode shadows are darker (near-black with low opacity), not the same shadow lightened
- **Surface hierarchy flips** — lighter surfaces = higher elevation (opposite of light mode)
- **Background tints** — use very low chroma tinted darks, not pure `#000` or `#111`
- **Test contrast in both modes** — a colour pair that passes WCAG AA in light mode may fail in dark mode

## Common Mistakes to Avoid

❌ **Too many colors** — Use no more than 7 token colors; limit primary palette to 3
❌ **Insufficient contrast** — Always test; low contrast fails accessibility and looks cheap
❌ **Color psychology mismatch** — Red for healthcare trust, blue for energy drinks, etc.
❌ **Saturated text** — Never use pure saturated colors for body text; use neutral grays
❌ **Pure grays and pure black** — Always tint neutrals with brand hue (see Tinted Neutrals above)
❌ **Ignoring cultural context** — White = pure in West, mourning in Asia; red = luck in China, alert in US
❌ **No dark mode consideration** — Provide both light and dark palette variants with desaturated accents
❌ **Trend-only selection** — Balance 2026 trends with timeless choices for primary colors

## Testing Your Palette

1. **Contrast check**: Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
2. **Accessibility test**: Run palette through [WCAG Color Contrast Checker](https://www.tpgi.com/color-contrast-checker/)
3. **Real application**: Apply to actual website mockup — does it feel right?
4. **Mobile preview**: Colors appear different on different screens; test on actual devices
5. **Colorblind simulation**: Use [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) to see how ~8% of users perceive colors

## Integration with Design System

Once color palette is finalized:
1. Add to `design-tokens.md` (in project)
2. Generate `tailwind.config.mjs` using Design System skill
3. Apply to `src/styles/global.css`
4. Preview on actual pages to verify harmony across all elements

## Reference Files

- `references/color-theory-fundamentals.md` — HSL model, color wheel, temperature, harmony principles
- `references/color-psychology.md` — Color associations, cultural context, emotional impact (80+ associations)
- `references/color-schemes.md` — 7 color schemes with formulas, HSL adjustments, when to use each
- `references/industry-color-psychology.md` — Sector-specific expectations and recommendations
- `references/accessibility-contrast.md` — WCAG standards, contrast calculations, verification tools
- `references/practical-application.md` — Applying palettes to web components, light/dark modes, common UI patterns
- `references/tools-resources.md` — Color picker tools, generators, accessibility checkers

---

**Next Step:** Share your brand colors (hex, RGB, or description) and I'll generate your complete color palette with accessibility verification.
