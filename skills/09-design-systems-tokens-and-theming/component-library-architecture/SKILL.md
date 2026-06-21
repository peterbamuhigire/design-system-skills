---
name: component-library-architecture
description: Use when architecting a reusable component library or design-system component set — deciding atomic levels (atom/molecule/organism), the variant/size/state model for a component (Button, Input, Card, Modal, Tabs), how components compose via slots/composition over prop-explosion, full interactive-state coverage (default/hover/focus/active/disabled/loading/selected/error), and the per-component documentation (anatomy, props/variant API, do/don't, a11y notes). Routes here for "design a Button component", "component API", "variant matrix", "component states", "atomic design structure", "component spec sheet", "slots vs props", "compound component". Builds ON token architecture (consume semantic tokens, never hard-code).
status: active
metadata:
  portable: true
  category: 09-design-systems-tokens-and-theming
  compatible_with:
    - claude-code
    - codex
---

# Component Library Architecture

<!-- dual-compat-start -->
## Use When
- Defining the **structure** of a component library: what is an atom vs molecule vs organism, and what belongs in the library at all vs in product code.
- Designing a single component's **API surface**: its variants (e.g. `primary | secondary | ghost | destructive`), sizes, and the props/slots that drive them.
- Specifying **full interactive-state coverage** for a component — every state in the matrix (default, hover, focus-visible, active, disabled, loading, selected, error, read-only) is named and given a token-backed treatment, not left to chance.
- Choosing a **composition strategy** — compound components / slots vs a flat prop list — to avoid prop-explosion and boolean-soup.
- Writing the **per-component documentation** so designers and engineers consume the component the same way (anatomy, when-to-use, do/don't, a11y, the variant API).

## Do Not Use When
- You are defining the **token tiers, naming, or export** (primitive → semantic → component tokens, CSS vars / Style Dictionary). Use `design-tokens-and-naming` — this skill *consumes* those tokens.
- You are producing **Figma-to-dev redlines / measured handoff sheets** for a specific screen. Use `design-handoff-and-dev-spec`.
- You are designing **dark-mode / multi-brand theming** of the same components. Use `dark-mode-and-theming` (this skill keeps every value token-referenced precisely so theming stays free).
- You are auditing **WCAG conformance** of a built UI. Use `accessibility-wcag-2-2-compliance`; here you *build a11y in* rather than audit it.
- You only need the copy inside a control (labels, button text). Use `ux-writing-and-microcopy`.

## Required Inputs
- A **token layer to consume** — at minimum semantic tokens for color, space, radius, type, elevation, motion (`design-tokens-and-naming`). If absent, stop and build tokens first; a component library built on hex literals cannot be themed and is not a system.
- The **target platform(s)** — web (HTML/CSS, React/Vue/Web Components), or cross-platform — because composition mechanics (slots, `children`, named regions) differ.
- The **scope**: which components, and the priority order (foundations first: Button, Input/Field, Icon, Text, then molecules: Field-with-label, Select, then organisms).
- An **accessibility floor** — WCAG 2.2 AA is the minimum (`doctrine/references/wcag-2.2-criteria.md`).

## Workflow
1. **Place the component on the atomic ladder before designing it.** Atom (indivisible: Button, Input, Icon, Text, Avatar), Molecule (a small bonded group with one job: Field = Label + Input + HelpText + Error; SearchBar = Input + Button), Organism (a self-contained section: Header, Card, DataTable, Form). The level dictates whether it owns layout or only fills a slot. See `references/atomic-structure.md`. Do not let an atom grow a layout or a molecule grow business logic — that is the #1 architecture smell.
2. **Define the variant model along orthogonal axes — never one mega-enum.** Separate the axes that vary independently: **intent/variant** (primary/secondary/ghost/destructive), **size** (sm/md/lg), **state** (interactive, below), and **modifiers** (icon-only, full-width, loading). A component's API is the *product* of independent axes, expressed as small enums + booleans, not a `variant="primary-large-loading-icon"` string. State the axes explicitly so the matrix is finite and reviewable.
3. **Cover the FULL interactive-state set — this is non-negotiable.** For every interactive component enumerate and give a token-backed treatment to: **default, hover, focus-visible, active/pressed, disabled, loading, selected/checked, error/invalid, read-only** (only the states the component can actually enter). Two rules from doctrine's a11y floor:
   - **focus-visible is mandatory and must be visible** — a real indicator with **≥ 3:1 contrast** against its background, and not obscured by sticky chrome (WCAG 2.2 **2.4.7**, **2.4.11**, **1.4.11**; see `doctrine/references/wcag-2.2-criteria.md`). Never `outline: none` without a replacement.
   - **disabled ≠ invisible** — disabled controls are exempt from contrast minimums but must still be perceivable; communicate state with more than color alone (1.4.1), and prefer not removing them from the tab/AX tree when their presence carries meaning. **loading** must expose `aria-busy`/a live status, and **error** must pair the color with text + `aria-invalid` + `aria-describedby`.
4. **Choose composition over configuration.** When a component accumulates >~5 booleans, or needs to inject arbitrary content, switch from props to **composition**: slots / named regions / compound components (`Card.Header`, `Card.Body`, `Select` + `Select.Option`). Expose layout regions as slots; keep behavior in the parent. See `references/atomic-structure.md` §Composition. This is the doctrine "authored, not templated" lever applied to APIs — a small composable primitive beats a fat configurable one.
5. **Bind every value to a semantic token.** Padding, color, radius, type, border, shadow, motion durations — all reference tokens (`--color-action-bg`, `--space-3`, `--radius-control`, `--duration-fast`), never literals. This is what makes the component themeable, dark-mode-ready, and multi-brand for free. Map per-component tokens to semantic ones (per `design-tokens-and-naming`); a hard-coded `#2563eb` in a component is a defect.
6. **Meet the interaction minimums.** Pointer target **≥ 24×24 CSS px** (aim 44×44 touch / 48dp) — WCAG 2.2 **2.5.8**; honour `prefers-reduced-motion` on any state transition (2.3.3); every drag affordance has a single-pointer alternative (2.5.7). All from `doctrine/references/wcag-2.2-criteria.md`. Motion durations come from motion tokens, not magic numbers.
7. **Document the component to the template.** Produce the per-component spec: anatomy diagram (named parts), when-to-use / when-not, the **variant × size × state matrix**, the prop/slot API table, a11y contract, and do/don't pairs. Use `references/component-doc-template.md`. A component without this doc is not "done" — undocumented variants get reinvented and the library forks.
8. **Resist anti-slop sameness (`doctrine/design-doctrine.md`).** The default-looking Button (flat fill, generic radius, blue) is the convergent AI mean. Make the *one* authored choice — a deliberate radius, a considered pressed-state shift, a focus ring that belongs to the brand — and apply it systematically through tokens so it reads as one skilled hand, not a template.

## Anti-Patterns
- **State gaps.** Shipping default + hover and forgetting focus-visible, loading, disabled, or error. The matrix exists so nothing is forgotten; an empty cell is a bug, not a default.
- **`outline: none` with no replacement** — a WCAG 2.4.7 failure and the single most common a11y regression in component libraries.
- **Prop-explosion / boolean soup.** A Button with `isPrimary`, `isSecondary`, `isGhost`, `isDanger` booleans (mutually exclusive states as separate flags) instead of one `variant` enum; switch to enums + composition.
- **The mega-variant enum.** `variant="primary-lg-loading"` collapses orthogonal axes into one string — un-typed, un-composable, combinatorially exploding.
- **Hard-coded values.** Any literal hex/px in a component body — it can't theme, can't go dark, can't rebrand. Token it.
- **Atomic-level creep.** An atom that owns page layout; a molecule that fetches data; an organism duplicated three ways because no one documented the first.
- **Disabled-by-color-only / error-by-color-only** — fails 1.4.1; pair with text, icon, or shape.
- **Undocumented component** — no anatomy, no API table, no do/don't → it forks the moment a second person touches it.

## Outputs
- An **atomic inventory** classifying each component (atom/molecule/organism) with composition relationships.
- A **variant model** per component — the orthogonal axes (variant × size × state × modifier) as small enums + booleans.
- A **full state matrix** per interactive component with a token-backed treatment for every reachable state.
- A **prop/slot API** table and composition contract (slots vs props decision recorded).
- A **per-component spec doc** following `references/component-doc-template.md`, with the a11y contract referencing WCAG 2.2 criteria.

## Examples
- `examples/button-component-spec.md` — a complete, concrete Button spec: 4 variants × 3 sizes × 9 states, every cell mapped to semantic tokens, the prop/slot API, the focus-ring and target-size a11y contract, and do/don't pairs. Use it as the pattern for any new component. (See `CONTRIBUTING.md` — examples are mandatory and never lorem.)

## References
- `doctrine/design-doctrine.md` — the anti-slop charter; §0 "looks human-made" applied to API design (composition over configuration, one authored choice applied systematically).
- `doctrine/references/wcag-2.2-criteria.md` — the a11y floor cited throughout: focus-visible & contrast (2.4.7, 1.4.11), focus-not-obscured (2.4.11), target size 24px (2.5.8), reduced motion (2.3.3), dragging alternative (2.5.7), name/role/value (4.1.2), color-not-alone (1.4.1).
- `references/atomic-structure.md` — the atomic ladder, classification rules, and composition (slots/compound) decision guide.
- `references/component-doc-template.md` — the per-component documentation template (anatomy, variant API, state matrix, a11y contract, do/don't).
- Sibling: `design-tokens-and-naming` (tokens this skill consumes), `dark-mode-and-theming`, `design-handoff-and-dev-spec`, `accessibility-wcag-2-2-compliance`.
<!-- dual-compat-end -->
