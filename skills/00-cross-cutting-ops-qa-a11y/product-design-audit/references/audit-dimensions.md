# Reference: The Cross-Platform Audit Dimensions

These are the dimensions a **product** is scored on, on **every** surface it ships (website,
SaaS web app, iOS, Android, desktop). They are the ten `design-audit` dimensions
(`skills/00-cross-cutting-ops-qa-a11y/design-audit/SKILL.md` §2) **plus two product-level
dimensions** — IA/Navigation and Trust — that only surface when you audit a whole product
rather than one screen.

Score each 0–4 per surface (anchors in `design-audit/references/audit-rubric.md` §2). Three of
these dimensions feed the **hard gates** that can cap the surface score: Accessibility, Typography
+ Colour (slop/contrast), and Performance. See `recommendation-format.md` for caps.

The final column is the **engine skill a finding in that dimension routes to** — this is what
makes the audit executable. Names are glob-verified against the engine.

---

## The 11 dimensions

| # | Dimension | Weight | What it checks (cross-platform) | Routes findings to |
|---|---|---|---|---|
| 1 | **AI Slop / Distinctiveness** | 4% (gate) | Does the product read as machine-generated? Banned default font, convergent palette (cyan-on-dark, purple gradient), uniform cards, glassmorphism-for-its-own-sake, "Submit"/"Loading…" copy, slop imagery (warped logo, gibberish signage). Was the type/colour/layout choice **stated**? | `visual-product-slop-audit`, `ai-slop-typography-audit`, `distinctive-by-design` |
| 2 | **Visual Hierarchy** | 15% | Squint test passes; clear primary>secondary>tertiary; weight contrast (bold/regular, not medium-soup); one focal point per screen; brand colour reserved for interaction. | `practical-ui-design`, `premium-ui-ux-design` |
| 3 | **Accessibility (WCAG 2.2 AA)** | 20% (gate) | Contrast ≥4.5:1 body / ≥3:1 large+UI; keyboard operable + visible logical focus; name/role/value; alt text; reflow 320px + 200%; reduced-motion; **+ the nine 2.2 deltas** (2.4.11 focus-not-obscured, 2.5.8 target ≥24px, 2.5.7 drag alternative, 3.2.6 consistent help, 3.3.7 redundant entry, 3.3.8 accessible auth). Platform a11y too (VoiceOver/TalkBack, Dynamic Type, screen-reader). | `accessibility-wcag-2-2-compliance`, `accessible-color-and-contrast` |
| 4 | **Typography** | 10% (slop) | Intentional non-default face; consistent scale; body ≥16px; line-height 1.5–2.0; measure 40–80ch; regular+bold; left-aligned body; paired not monotype. No banned face (`ai-slop-banned-fonts.md`); routes to the right one of the 8 intent categories (`font-groups-and-usage.md`). | `font-selection-and-pairing`, `ai-slop-typography-audit`, `premium-font-scan` |
| 5 | **Colour & Contrast** | 8% (slop/a11y) | Tinted neutrals (no #000/#fff/#808080); primary+neutral+semantic+surface tokens; 60-30-10; semantic colour paired with icon; dark mode independently designed; brand colour for interaction only; contrast certified. | `color-system-and-palette`, `accessible-color-and-contrast`, `dark-mode-and-theming` |
| 6 | **Layout & Responsive** | 8% | Consistent spacing token scale (4/8pt); rhythm not uniformity; few alignment axes; constrained measure; Grid/Flex used correctly; mobile-first content-driven breakpoints; container queries for reusable components; adaptive layouts per device class. | `layout-grid-and-spacing`, `responsive-and-adaptive-layout` |
| 7 | **Interaction States** | 12% | Every interactive element ships the full set: default/hover/focus/active/disabled/loading/error/success. Focus uses `focus-visible`. Pressed ≠ hover. Disabled explained. | `interaction-design-patterns`, `empty-error-and-loading-states`, `form-ux-design` |
| 8 | **Motion & Interaction** | 5% (a11y) | Every animation has a job; 100/300/500 timing; exponential easing (no bounce/elastic); transform+opacity only; `prefers-reduced-motion`; 60fps mid-range; restraint (no animation fatigue). | `motion-design` |
| 9 | **Content & UX-Writing** | 12% | Verb+noun buttons (no "Submit"/"OK"); errors = what+why+how; empty states acknowledge+value+action; loading names the op; descriptive links; consistent vocabulary; tone fits the moment. | `ux-writing-and-microcopy`, `error-empty-and-system-messaging`, `empty-error-and-loading-states` |
| 10 | **Performance** | 6% (gate) | Web: field p75 LCP ≤2.5s, INP ≤200ms, CLS ≤0.1; within archetype KB budget; WebP/AVIF + srcset + dims; `font-display: swap` + preload + subset. App: cold-start, scroll jank, frame budget, asset weight. | `performance-as-ux-and-core-web-vitals` |
| 11a | **IA & Navigation** *(product-level)* | (folded into Hierarchy/Layout weighting; scored 0–4 and reported) | Is the product's structure learnable? Findable primary tasks; sane nav model per platform (web nav vs tab bar vs Material nav vs desktop menu); breadcrumbs/back behaviour; search where the IA is deep; no orphan screens; consistent labels across surfaces. | `navigation-and-information-architecture`, `cross-platform-design-parity` |
| 11b | **Trust & Credibility** *(product-level)* | (reported alongside; premium-readiness pass) | Does it feel safe to pay/commit? Real proof (not stock-only), visible support path, honest pricing CTAs, security/privacy cues, error honesty, no dark patterns, polish backed by speed+a11y+data quality. | `premium-ui-ux-design`, `landing-page-and-conversion-design`, `sector-strategies` |

> **Weighting note.** The first ten dimensions carry the `audit-rubric.md` weights (sum = 100%)
> and produce the 0–100 surface score. **IA/Navigation** and **Trust** are scored 0–4 and reported
> as product-level dimensions; their findings route like any other and a 0 on either is itself a
> high-severity finding even though they sit outside the 100% web rubric. Treat IA failures as
> Visual-Hierarchy/Layout debt for the number, and Trust failures as the premium-readiness flag.

## Which dimensions apply per surface

All 11 apply to every surface, but emphasis shifts:

| Surface | Heaviest dimensions | Lightest / N/A |
|---|---|---|
| **Marketing website** | Slop, Hierarchy, Performance (CWV), Trust, Content | Interaction-state depth (fewer stateful controls) |
| **SaaS web app** | Interaction States, IA/Nav, Accessibility, Content, Layout (data density) | Expressive display typography |
| **iOS app** | Accessibility (Dynamic Type/VoiceOver), platform idiom (lens), Motion (haptics), Hierarchy | Web CWV (use app perf instead) |
| **Android app** | Accessibility (TalkBack), platform idiom (Material 3), Colour (dynamic colour), Motion | Web CWV (use app perf instead) |
| **Desktop app** | IA/Nav (menus/shortcuts), Interaction States, Layout (density), Performance (cold-start) | Touch-target sizing (unless touch-capable); web CWV |

## How to use this file

1. Build the surface × dimension matrix (rows = in-scope surfaces, cols = these 11).
2. Run the slop gate first (dimension 1) product-wide — it can cap surfaces.
3. Score each cell 0–4 with the rubric anchors; layer the platform lens
   (`platform-lenses.md`) on top per surface.
4. Apply the a11y, perf, and content gates; apply caps (`recommendation-format.md`).
5. Every non-4 cell becomes a routed finding using the last column above.
