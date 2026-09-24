# UI Numeric Baselines

Parent skill: [`../SKILL.md`](../SKILL.md) (`practical-ui-design`).

**When to read:** when a screen needs starting numbers for spacing, targets, radii, shadows and
type steps. These are baselines to express as tokens and then tune; they carry no aesthetic
authority. Paraphrased from Pixsel Academy, *101 Dos and Don'ts of UI Design*; Kodeco, *App Design
Apprentice*; *How to Design Better UI Components 3.0* (per-component anatomy numbers already live
in `component-states-and-interaction-fidelity/references/component-anatomy.md`). Take the numbers,
never the books' safe-default look; bounce interpolators and glassmorphism from these sources are
rejected (see `doctrine/references/ai-slop-taxonomy.md`).

| Item | Baseline | Note |
|---|---|---|
| Spacing unit | 8 (with 4 for fine steps) | Every gap a multiple |
| Content inset (mobile) | 16 | Section and call-to-action spacing about 32 |
| Button padding | Horizontal about 2 × vertical (for example 16 × 8) | Optical balance |
| Nested radii | Inner radius ≈ outer radius − padding between them | Concentric, not equal |
| Radii scale | 4 / 8 / 16 | Bottom sheets: top corners only |
| Soft shadow | Offset about 8, blur about 24, low opacity (around 15 per cent) | Tool defaults (small offset, high opacity) read harsh; dark mode uses surface lightness, not shadow alone |
| Touch targets | At least 44 (iOS) / 48 (Android); generous 56-60 for primary mobile actions | WCAG 2.2 target-size minimum applies; see accessibility skill |
| Type scale | Ratio about 1.25-1.33, rounded to even sizes | Engine scale rules in `doctrine/references/type-scale-and-spacing.md` |
| Line height (body) | About 1.4-1.6 | Tighter for display sizes |
| Numeric columns | Right-aligned, tabular figures | Text columns left-aligned |
| Pure black or white text on backgrounds | Avoid; use near-black and off-white | Reduces halation for many readers |
| Bottom navigation | About 56 high; icon plus label | Never icon-only |
| Contrast | 4.5:1 body, 3:1 large text and UI parts | Check with `accessible-color-and-contrast` |
| Shadows (layered) | Larger blur, low opacity, light from above, no upward shadow | White "glow" shadows on dark surfaces are wrong; use surface tint |
| Line height by size | Inversely proportional: about 1.6 for small text, 1.1-1.3 for large headings | Paduraru, *Fundamentals of Creating a Great UI/UX* |

Screen brief check (CUBI, from Paduraru): name the **content**, the **user goals**, the
**business goals** and the **interactions** before styling a screen.

