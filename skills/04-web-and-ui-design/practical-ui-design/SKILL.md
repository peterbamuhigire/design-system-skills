---
name: practical-ui-design
description: Rules-based visual UI design system covering colour, typography, spacing,
  layout, buttons, forms, and visual consistency. Load alongside any platform skill when
  the work needs a deliberate interface system instead of ad hoc styling.
status: active
metadata:
  portable: true
  category: 04-web-and-ui-design
  compatible_with:
  - claude-code
  - codex
---

# Practical UI Design Skill
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- You need to build a colour palette: pick a single brand hue and derive a monochromatic 1-hue + 5-variation scale in HSB (or OKLCH for perceptually even brightness), tint all neutrals 2-5% toward the brand hue, and reserve brand colour for interactive elements only.
- You are deciding light/dark mode tokens, system colours (red/amber/green/blue), or checking WCAG 2.1 AA contrast (4.5:1 small text, 3:1 large text and UI components) or APCA values for a real screen.
- You are designing or auditing buttons and forms — states, brand-colour-as-affordance, border rules for low-contrast brand colours — and want them governed by tokens, not ad hoc CSS.
- You need typography, spacing rhythm, or 12-column layout rules grounded in `doctrine/references/type-scale-and-spacing.md` and a deliberate (non-banned) typeface from `doctrine/references/font-groups-and-usage.md`.
- An existing UI has token drift, duplicated components, or inconsistent states and you want a system-level fix rather than per-screen patches.

## Do Not Use When

- You need platform implementation code or layout chrome — load `webapp-gui-design`, `android-ui-ux-design`, or `ios-ui-ux-design`; this skill supplies the visual system, not the framework code.
- The job is choosing a typeface or pairing from scratch — that lives in the `doctrine/references/*` font and pairing docs, not this entrypoint.
- You want behaviour/navigation/action patterns (`interaction-design-patterns`), animation timing (`motion-design`), or a pass/fail generic-AI-UI quality gate (`visual-product-slop-audit`, `design-audit`) — those are companion siblings, not this skill.
- Clinical-grade accessibility is the core requirement — start from `healthcare-ui-design` and load this for the colour/type/spacing layer.

## Required Inputs

- The brand colour (or permission to choose one) plus target mode(s) — light, dark, or both — so the palette and contrast pairings can be fixed.
- The concrete surface under design or audit: which screens, components (buttons, forms, cards), and states need tokens.
- Existing tokens, palette, or component inventory when retrofitting, so token drift and duplicated/inconsistent states can be reconciled instead of re-invented.
- The chosen (non-banned) typeface and pairing, or a go-ahead to select one from `doctrine/references/*` before applying the type and spacing rules.

## Workflow

- Read this `SKILL.md` first, then load only the referenced deep-dive files that are necessary for the task.
- Apply the ordered guidance, checklists, and decision rules in this skill instead of cherry-picking isolated snippets.
- Produce the deliverable with assumptions, risks, and follow-up work made explicit when they matter.
- When a product already exists, audit token drift, duplicated components, and inconsistent states before proposing new styling.

## Quality Standards

- Keep outputs execution-oriented, concise, and aligned with the repository's baseline engineering standards.
- Preserve compatibility with existing project conventions unless the skill explicitly requires a stronger standard.
- Prefer deterministic, reviewable steps over vague advice or tool-specific magic.
- Prefer system-level fixes over per-screen decorative fixes.
- Treat the design system as a living product with documented tokens, components, and usage rules.

## Anti-Patterns

- Treating examples as copy-paste truth without checking fit, constraints, or failure modes.
- Loading every reference file by default instead of using progressive disclosure.

## Outputs

- A concrete result that fits the task: implementation guidance, review findings, architecture decisions, templates, or generated artifacts.
- Clear assumptions, tradeoffs, or unresolved gaps when the task cannot be completed from available context alone.
- References used, companion skills, or follow-up actions when they materially improve execution.

## Evidence Produced

| Category | Artifact | Format | Example |
|----------|----------|--------|---------|
| UX quality | Practical UI audit | Markdown doc covering colour palette, typography scale, spacing, button states, and form patterns per Dannaway | `docs/ux/practical-ui-audit-checkout.md` |

## References

- `doctrine/design-doctrine.md` — the anti-slop charter; this visual system exists to push UI away from the convergent AI mean.
- `doctrine/references/ai-slop-banned-fonts.md` — banned primary typefaces; pick a deliberate face from `doctrine/references/font-groups-and-usage.md` before applying the type rules below.
- `doctrine/references/pairing-principles.md` — always pair a distinctive display face with a refined body face; never monotype.
- `doctrine/references/type-scale-and-spacing.md` — the canonical type scale, line-height, weight, tracking, and spacing-rhythm numbers behind the typography and spacing sections (replaces the former `math-for-web-design` reference, which did not migrate to this engine).
- Use the `references/` directory for deep detail after reading the core workflow below.
- Use `references/visual-consistency.md` when pattern coherence, affordances, or user expectations are part of the task.

## Examples

- `examples/ui-before-after-worked.md` — a pricing card taken from a weak (AI-slop) version to a fixed version, with every change mapped to the rule it satisfies (spacing, hierarchy, contrast, colour restraint, button design, shadow/border).
<!-- dual-compat-end -->
## Plugins (Load Alongside)

| Companion Skill | When to Load |
|---|---|
| `webapp-gui-design` | Web app dashboards, admin panels, SaaS UIs |
| `android-ui-ux-design` | Android native (Kotlin/Compose) |
| `ios-ui-ux-design` | iOS native (SwiftUI/UIKit) |
| `healthcare-ui-design` | Clinical-grade interfaces with strict accessibility |
| `visual-product-slop-audit` | Quality gate to catch generic AI-generated UI patterns |
| `motion-design` | Animation timing, easing, and micro-interaction standards |
| `design-audit` | Comprehensive UI quality audit with severity ratings |
| `interaction-design-patterns` | Tidwell behaviour/navigation/layout/action patterns |

**Usage:** This skill provides the *visual system* (colour, type, spacing, components). Platform skills provide *implementation code*. Load both. Font, pairing, and type-scale rules trace to `doctrine/references/*` — do not restate them here.

---

## 1. Colour System (HSB-Based)

### 1.1 Why HSB, Not RGB/HEX

Use HSB (Hue 0-360, Saturation 0-100, Brightness 0-100) for all design decisions. HSB maps to how humans perceive colour: pick a hue, adjust richness with saturation, adjust lightness with brightness. Convert to HEX/RGB only at implementation time.

### 1.2 OKLCH Alternative

For perceptually uniform colour manipulation, consider **OKLCH** (`oklch(L C H)`) instead of HSB. OKLCH ensures equal perceived brightness across hues (unlike HSB where blue looks darker than yellow at the same B value). Use OKLCH for generating palettes, ensuring consistent visual weight. Convert final values to HEX/RGB for implementation. **Tint all neutrals** — add 2-5% of brand hue to greys; never use pure grey.

### 1.3 Start with Black and White

Design the interface without colour first. Focus on spacing, size, layout, and contrast. Colour is added last, purposefully.

- **Avoid pure black** (#000000) -- high contrast against white causes eye strain. Use a dark grey with a tinge of brand hue instead.
- **Avoid pure white text on dark** -- same eye strain problem in reverse.

### 1.3 One Brand Colour

Choose a single distinctive brand colour. Apply it **only to interactive elements** (buttons, text links, active states). Do not apply brand colour to headings or non-interactive elements -- users will mistake them for links.

- If brand colour has a strong existing meaning (e.g. red = error), use the darkest palette variation for interactive elements, or switch interactive colour to blue.
- If brand colour is too light (e.g. yellow): use darkest variation for button text and links; add a border to buttons for 3:1 contrast.

### 1.4 Monochromatic Palette (1 Hue + 5 Variations)

All you need: **1 brand colour + 5 tonal variations** sharing the same hue.

#### Light Palette (example hue 230)

| Token | HSB | Purpose | Contrast Req. |
|---|---|---|---|
| **Primary** | 230, 70, 80 | Buttons, links, interactive | >= 4.5:1 vs Lightest |
| **Darkest** | 230, 60, 20 | Heading text | >= 4.5:1 vs Lightest |
| **Dark** | 230, 30, 45 | Secondary/body text | >= 4.5:1 vs Lightest |
| **Medium** | 230, 20, 66 | Non-decorative borders, icons | >= 3:1 vs Lightest |
| **Light** | 230, 10, 95 | Decorative borders, dividers | Decorative -- no req. |
| **Lightest** | 230, 2, 98 | Alternate backgrounds | Base surface |
| **White** | 0, 0, 100 | Main background | Base surface |

#### Dark Palette (example hue 166)

| Token | HSB | Purpose | Contrast Req. |
|---|---|---|---|
| **Primary** | 166, 50, 90 | Buttons, links, interactive | >= 4.5:1 vs Dark |
| **White** | 0, 0, 100 | Heading text | >= 4.5:1 vs Dark |
| **Lightest** | 166, 4, 80 | Secondary/body text | >= 4.5:1 vs Dark |
| **Light** | 166, 6, 65 | Non-decorative borders | >= 3:1 vs Dark |
| **Medium** | 166, 8, 33 | Decorative borders | Decorative -- no req. |
| **Dark** | 166, 10, 23 | Alternate backgrounds | Base surface |
| **Darkest** | 166, 12, 15 | Main background | Base surface |

### 1.5 System Colours

| Colour | Meaning | Usage |
|---|---|---|
| **Red** | Error | Negative messages, failures, urgent alerts |
| **Amber** | Warning | Caution, risky actions |
| **Green** | Success | Positive messages, completed actions |
| **Blue** | Info | Neutral informational messages |

- System colour text: >= 4.5:1 contrast. Icons/components only: >= 3:1.
- Always pair system colour with an icon -- never rely on colour alone (colour-blind users).

### 1.6 Contrast Rules (WCAG 2.1 AA)

| Element | Min. Ratio |
|---|---|
| Small text (<= 18px regular, <= 14px bold) | **4.5:1** |
| Large text (> 18px bold or > 24px regular) | **3:1** |
| UI components (fields, radios, checkboxes) | **3:1** |
| Decorative-only elements | No requirement |

**APCA (WCAG 3 draft):** 90 preferred body, 75 minimum body, 60 other text, 45 large text + UI, 30 placeholders, 15 non-text.

---

## Additional Guidance

Extended guidance for `practical-ui-design` was moved to [references/skill-deep-dive.md](references/skill-deep-dive.md) to keep this entrypoint compact and fast to load.

Use that deep dive for:
- `2. Typography Rules`
- `3. Layout and Spacing`
- `4. Copywriting for UI`
- `5. Buttons`
- `6. Forms (Quick Reference)`
- `7. Component Patterns (Kuleszo)`
- `8. Dark Mode Rules`
- `9. Anti-Patterns`
- `10. Design Checklist`
