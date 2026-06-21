# App Landing Page Design Tokens

⚠️ **REFERENCE ONLY** — These are starting points, not final designs. Every app landing page must be uniquely designed to reflect your app's personality, target audience, and value proposition. Use this guide to understand the principles; customize extensively to avoid looking like every other landing page.

---

## Color Palette Strategy

### Primary Psychology

App landing pages need visual confidence to inspire downloads. The color strategy depends on your app category:

**Software/Productivity:** Deep blues, purples, or teals communicate professionalism and innovation.
**Lifestyle/Health:** Warm greens, oranges, or corals communicate wellness and energy.
**Entertainment:** Bold, vibrant colors (magenta, neon orange, electric blue) communicate fun.
**Finance:** Navy, dark grays, greens communicate trust and stability.
**Social:** Bright, energetic colors communicate connection and fun.

### Recommended Color Combinations by App Type

#### Productivity App Landing Page
```
Primary:    #3B82F6 (Professional Blue)
Secondary:  #F3F4F6 (Light Gray)
Accent:     #10B981 (Success Green)
Text:       #1F2937 (Dark Gray)
Background: #FFFFFF (White)
```

**Psychology:** Blue builds trust, green represents "go" (download), clean white maintains professionalism.

#### Health & Wellness App Landing Page
```
Primary:    #059669 (Health Green)
Secondary:  #F0FDF4 (Very Light Green)
Accent:     #EF4444 (Energy Red/Accent)
Text:       #1F2937 (Dark Gray)
Background: #FFFFFF (White)
```

**Psychology:** Green conveys health and growth, light backgrounds feel clean, red for urgency on CTA.

#### Entertainment App Landing Page
```
Primary:    #EC4899 (Playful Pink/Magenta)
Secondary:  #F3E8FF (Very Light Purple)
Accent:     #FBBF24 (Golden Yellow)
Text:       #1F2937 (Dark Gray)
Background: #FFFFFF (White)
```

**Psychology:** Bold colors create energy and excitement, playfulness invites exploration.

#### Finance App Landing Page
```
Primary:    #1E293B (Navy)
Secondary:  #F8FAFC (Off-White)
Accent:     #10B981 (Growth Green)
Text:       #334155 (Dark Slate)
Background: #FFFFFF (White)
```

**Psychology:** Navy and green communicate both stability and growth, minimalist approach reduces anxiety.

#### Social/Lifestyle App Landing Page
```
Primary:    #8B5CF6 (Modern Purple)
Secondary:  #F3E8FF (Very Light Purple)
Accent:     #FF6B6B (Coral)
Text:       #1F2937 (Dark Gray)
Background: #FFFFFF (White)
```

**Psychology:** Purple suggests creativity and modernity, coral accent adds warmth and approachability.

---

## Typography System

### Font Families

**Recommended combinations:**
- **Modern/Tech:** [Font Name] (headings) + [Font Name] (body) — clean, geometric
- **Friendly/Approachable:** [Font Name] (headings) + [Font Name] (body) — warm, humanistic
- **Premium/Luxury:** [Font Name] (headings) + [Font Name] (body) — elegant, serif

### Type Scale (Mobile-First)

| Element | Mobile | Desktop | Weight | Line Height |
|---------|--------|---------|--------|-------------|
| **Headline** | 28px | 48px | Bold (700) | 1.2 |
| **Subheadline** | 20px | 32px | Regular (400) | 1.3 |
| **Feature Title** | 18px | 24px | Semi-bold (600) | 1.4 |
| **Body Text** | 16px | 18px | Regular (400) | 1.6 |
| **Button Text** | 16px | 16px | Semi-bold (600) | - |
| **Small Text** | 14px | 14px | Regular (400) | 1.5 |

### Readable Sizes

- **Never use text smaller than 14px** (fails accessibility)
- **Button touch targets minimum 44x44px** (mobile)
- **Line height minimum 1.5** for body text (readability on screens)

---

## Component Patterns

### Hero Section Pattern

```
┌─────────────────────────────┐
│  HEADLINE (Big, Bold)       │
├─────────────────────────────┤
│  Subheadline                │
│  (Supporting context)       │
├─────────────────────────────┤
│  [HERO IMAGE/VIDEO]         │
│  (App mockup or demo)       │
├─────────────────────────────┤
│  [PRIMARY CTA BUTTON]       │
└─────────────────────────────┘
```

**Design Rules:**
- Headline: 28-36px, bold, benefit-focused
- Subheadline: 18-22px, supporting context
- Hero visual: High-quality app screenshot or video
- CTA: Contrasting color, minimum 44px height, action-oriented text

### Feature Cards Pattern

```
┌──────────────────┐
│  🎯 [Icon]       │
├──────────────────┤
│  Feature Title   │
├──────────────────┤
│  Benefit-focused │
│  description     │
│  (2-3 sentences) │
└──────────────────┘
```

**Design Rules:**
- Use 3-5 feature cards (not more)
- Icons: Consistent style, 32-48px
- Title: 18-24px, semi-bold
- Description: 14-16px, benefit-focused
- Spacing: 20-30px padding, gaps between cards

### Testimonial Card Pattern

```
┌─────────────────────────┐
│  ★★★★★                  │
├─────────────────────────┤
│  "Great app that really  │
│   saved me time..."     │
├─────────────────────────┤
│  [Photo] Name           │
│           Title         │
└─────────────────────────┘
```

**Design Rules:**
- Real photo (not stock)
- Star rating above quote
- Short quote (2-3 sentences)
- Name, title, company below
- Background: Subtle color (secondary palette)

### CTA Button Patterns

**Primary CTA (High Contrast):**
```css
button.primary {
  background: var(--accent-color);
  color: white;
  padding: 14px 28px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
}

button.primary:hover {
  opacity: 0.9;
  transform: scale(1.02);
}
```

**Secondary CTA (Lower Emphasis):**
```css
button.secondary {
  background: transparent;
  color: var(--primary-color);
  padding: 12px 24px;
  font-size: 16px;
  border: 2px solid var(--primary-color);
  border-radius: 8px;
  cursor: pointer;
}

button.secondary:hover {
  background: var(--secondary-color);
}
```

**Sticky CTA (Mobile):**
```css
.cta-sticky {
  position: fixed;
  bottom: 0;
  width: 100%;
  padding: 12px;
  background: var(--primary-color);
  box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

@media (min-width: 768px) {
  .cta-sticky {
    display: none;
  }
}
```

---

## Layout Patterns

### Mobile Layout (320px - 767px)

- Single column
- Full-width sections
- Stacked features (vertical)
- Sticky CTA at bottom
- Maximum width: 100% (minus safe margins)

### Tablet Layout (768px - 1023px)

- Two-column grids for features
- Wider card layouts
- Side-by-side hero image + text
- Fixed CTA button (not sticky)

### Desktop Layout (1024px+)

- Multi-column grids (3-4 columns)
- Hero can be split left/right
- Feature cards in rows
- Generous whitespace
- Maximum content width: 1200px

---

## Spacing System (8px Grid)

| Size | Value | Usage |
|------|-------|-------|
| **xs** | 8px | Small gaps, icon padding |
| **sm** | 16px | Component internal padding |
| **md** | 24px | Section margins |
| **lg** | 32px | Section gaps |
| **xl** | 48px | Large section spacing |
| **2xl** | 64px | Page sections |

**Rule:** Always use multiples of 8px for alignment and spacing.

---

## Visual Hierarchy

### Information Hierarchy

```
1. Headline (28-48px, bold)
   ↓
2. Hero Visual (300-400px height)
   ↓
3. Primary CTA (Contrasting color)
   ↓
4. Key Benefits (18-24px, 3-5 items)
   ↓
5. Social Proof (Testimonials, ratings)
   ↓
6. Feature Details (14-16px, expandable)
   ↓
7. FAQ Section (12-14px)
   ↓
8. Footer (Minimal links)
```

### Visual Emphasis Techniques

- **Size:** Larger = more important
- **Color:** High contrast = emphasis
- **Whitespace:** More space = focus
- **Position:** Top and center = priority
- **Animation:** Subtle movement draws eyes

---

## Motion & Animations

### Subtle Micro-Interactions

**Hover states:**
- Button: 2% scale up, slight shadow
- Card: 4px lift, shadow increase
- Link: Color change, underline

**Scroll animations:**
- Fade-in as elements enter viewport
- Slide-up from bottom
- Scale from 0.9 to 1.0

**Loading states:**
- Gradient shimmer effect
- Pulsing animation
- Progress indicators

### Performance Considerations

- Use CSS animations (not JavaScript where possible)
- Respect `prefers-reduced-motion` for accessibility
- Keep animations under 400ms
- Avoid animations on initial page load

---

## Responsive Design Breakpoints

```css
/* Mobile-first approach */
/* Default: 320px and up */

@media (min-width: 640px) {
  /* Tablet: 640px and up */
}

@media (min-width: 768px) {
  /* Tablet+: 768px and up */
}

@media (min-width: 1024px) {
  /* Desktop: 1024px and up */
}

@media (min-width: 1280px) {
  /* Large desktop: 1280px and up */
}
```

---

## Dark Mode Support

### Dark Mode Color Mapping

For every light mode color, define dark equivalent:

```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #1F2937;      /* Light mode: #FFFFFF */
    --bg-secondary: #111827;    /* Light mode: #F3F4F6 */
    --text-primary: #F3F4F6;    /* Light mode: #1F2937 */
    --text-secondary: #9CA3AF;  /* Light mode: #6B7280 */
  }
}
```

### Dark Mode Considerations

- Never use pure black (#000000) — use dark gray (#111827)
- Increase text lightness by 20-30% in dark mode
- Reduce opacity of shadows (less visible on dark)
- Test all colors for sufficient contrast in dark mode

---

## Accessibility Checklist

- [ ] **Contrast:** All text 4.5:1 (AA) or 7:1 (AAA)
- [ ] **Touch targets:** All buttons/links minimum 44x44px
- [ ] **Color not alone:** Don't use color only to convey meaning
- [ ] **Alt text:** All images have descriptive alt text
- [ ] **Keyboard navigation:** All interactive elements accessible
- [ ] **Focus indicators:** Clear focus states on all buttons/links
- [ ] **Skip links:** Skip to content link present
- [ ] **Form labels:** All inputs have associated labels
- [ ] **Semantic HTML:** Proper heading hierarchy, semantic elements
- [ ] **Reduced motion:** Respect `prefers-reduced-motion`

---

## Performance Targets

| Metric | Target | How to Achieve |
|--------|--------|----------------|
| **Page Load** | < 3 seconds | Image optimization, minification, CDN |
| **LCP** | < 2.5s | Optimize hero image, defer JS |
| **CLS** | < 0.1 | Specify image dimensions, font loading |
| **FID** | < 100ms | Defer non-critical JS, reduce main thread work |
| **File Size** | < 500KB | Compress images, minify code |

---

## Customization Guidelines

To make your app landing page unique:

1. **Color palette:** Choose 1-2 colors different from this template
2. **Typography:** Select fonts that reflect your brand personality
3. **Imagery:** Use authentic screenshots and real user photos
4. **Tone:** Develop unique voice/messaging for your app
5. **Layout:** Rearrange sections based on your key benefits
6. **Animation:** Add personality through subtle micro-interactions
7. **Content:** Tell your app's unique story, not generic benefits

Remember: This template is a starting point. The best landing pages differentiate themselves through thoughtful customization and unique positioning.

---

## Related References

- **app-branding.md** — Color psychology for 8 hues, CTA color strategy, typography by app type, screenshot strategy, brand voice
- **app-conversion.md** — Download funnel, hero design, CTA strategy, pricing pages, trust architecture, A/B testing
- **app-type-patterns.md** — 7 app types with distinct design systems + branding personality framework

---

**Last Updated:** February 2026
**Framework:** Mobile-first, WCAG AA accessible, performance-optimized
**Tested on:** iOS Safari, Android Chrome, Desktop Chrome/Firefox/Safari
