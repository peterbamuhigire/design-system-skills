---
name: figma-and-tooling-workflow
description: Use when setting up, structuring, or standardising design work in current (2026) Figma for a design system or product — file/page architecture, component properties & variants, Figma variables with modes for theming (light/dark/brand) and breakpoints, auto-layout, the styles-vs-variables decision, Dev Mode handoff, and branching/library-publishing/naming conventions. Routes here for "Figma file structure", "Figma variables", "variable modes", "component properties", "auto layout", "Dev Mode", "publish library", "Figma branching", "Figma naming convention". Explicitly modern Figma — NOT Sketch, Adobe XD, Axure, or paper-prototyping workflows. Builds ON design-tokens-and-naming (Figma variables are where the token tiers live in-tool) and feeds design-handoff-and-dev-spec.
status: active
metadata:
  portable: true
  category: 09-design-systems-tokens-and-theming
  compatible_with:
    - claude-code
    - codex
---

# Figma And Tooling Workflow
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Standing up a new design-system or product Figma file and you need a deliberate file/page/section
  structure instead of one sprawling canvas of loose frames.
- Implementing the token tiers **in Figma** — turning the primitive → semantic → component tokens
  from `design-tokens-and-naming` into Figma **variables**, with **modes** carrying light/dark,
  brand/tenant, and density variation, plus breakpoint number modes.
- Building components properly: **component properties** (boolean / text / instance-swap / variant)
  and a **variant** matrix, on **auto-layout**, so one component serves every state and size.
- Deciding **styles vs variables** for colour, type, effects, and grids (the in-tool seam that
  decides what can be themed and what can't).
- Preparing **Dev Mode** handoff — annotations, the inspect panel, variable/token names surfaced to
  engineering, statuses (Ready for Dev), and links into code.
- Setting team conventions: **branching** for safe edits, **library publishing** discipline, and a
  layer/page/component **naming** scheme that survives more than one designer.

## Do Not Use When

- You are deciding the *token tiers, names, OKLCH values, or export topology* themselves — that is
  `design-tokens-and-naming`. This skill is how those tokens are *expressed and operated in Figma*
  (as variables/modes); it does not invent the token model.
- You are writing the *measured redline / acceptance-criteria handoff sheet* for a screen — that is
  `design-handoff-and-dev-spec`. This skill sets Figma up *so* Dev Mode handoff is clean; it does not
  replace the written spec.
- You are designing a component's *variant/state/API model* as a system contract — that is
  `component-library-architecture`. This skill builds that model *in Figma* (properties + variants +
  auto-layout) but defers the architecture decisions to it.
- You are choosing palette, type, layout, or motion (groups 01–04, 08) — Figma is where resolved
  decisions are assembled, not where they are made.
- The tool in question is Sketch, Adobe XD, Axure, InVision, or paper prototyping. This skill is
  current Figma only; the older-tool workflows are out of scope and are not reproduced here.

## Required Inputs

- The resolved token model from `design-tokens-and-naming`: the three tiers and the semantic role
  map, the theme axes (which of light/dark, brand/tenant, density must coexist), and the
  breakpoint set. Figma variables *carry* these; they don't replace the decision.
- The component scope and each component's variant/state model from `component-library-architecture`.
- A namespace/prefix for the system (e.g. `mdk` for Maduuka) used consistently in variable
  collections, styles, components, and pages.
- Who consumes the library (which teams subscribe) and the WCAG 2.2 AA floor the themed pairs must
  hold (`doctrine/references/wcag-2.2-criteria.md`).

## Workflow

1. **Fix the file and page architecture before drawing anything.** Decide the *file split* first:
   typically a **Foundations/Tokens** library file, a **Components** library file, and per-product
   **Product** files that consume both as published libraries — so themes and components publish once
   and fan out, rather than being copied. Inside each file, use **pages** as top-level sections
   (e.g. `Cover`, `🧱 Foundations`, `🧩 Components`, `📐 Patterns`, `🚧 WIP`, `🗄 Archive`) and
   **sections** (the frame-grouping primitive) to chunk a page. One canvas of loose frames is the
   structural cause of un-findable, un-maintainable design. See `references/figma-conventions.md`
   §File & page structure.

2. **Build the token tiers as variable collections, with modes as the theming seam.** In current
   Figma, **variables** (not styles) are where tokens live and where theming happens:
   - Create **collections** mapped to the token tiers — a `Primitives` collection (raw ramps, the
     space/size scale, radii) and a `Semantic` collection (role aliases that *reference* primitives).
     Component-tier values usually live on the component as bound properties or a small per-component
     collection. This mirrors the primitive → semantic → component tiers exactly.
   - Put theme variation on **modes** of the *semantic* collection: a `Theme` axis with `Light` /
     `Dark` (and `Brand A` / `Brand B`, or `Tenant-X`, as separate modes or a second collection).
     Each mode re-points the *same* semantic variable at a different primitive — the components never
     change, only the alias targets. This is the in-tool form of "semantic tokens are the theming
     seam, never the primitives."
   - Use **number variables in modes for breakpoints/density**: a `Breakpoint` axis (`Compact` /
     `Regular` / `Expanded`) driving spacing, container width, and type-step numbers, so one frame
     adapts by mode-switch instead of three hand-built copies.
   - **Alias, don't duplicate:** semantic variables point at primitives; never paste a raw hex into a
     semantic variable. A semantic variable holding a literal is the Figma form of a component
     reaching past the semantic layer. See `references/figma-conventions.md` §Variables & modes.

3. **Decide styles vs variables deliberately — they are not interchangeable.** Use **variables** for
   anything that must theme or switch by mode: all colour fills/strokes, spacing, radius, and
   single-axis values. Use **styles** where Figma still needs a *bundled, multi-property* object:
   **text styles** (font, size, line-height, spacing, weight as one applied unit — back the size by a
   variable where possible), **effect styles** (shadows/blur, themed via variable-bound colours), and
   **grid styles**. The rule: a value that a theme re-points → variable; a composite the tool applies
   as one named bundle → style, with its themeable parts variable-bound underneath. Recording this
   seam is what keeps dark mode and multi-brand free. See `references/figma-conventions.md` §Styles vs
   variables.

4. **Build every component on auto-layout.** Auto-layout is non-negotiable for a system component:
   it gives real padding/gap (bound to space variables), hug/fill sizing, direction, and wrap, so the
   component reflows to content and breakpoint instead of being pixel-pushed. Bind padding and gap to
   the space variables; never type raw pixel padding into a system component. Nested auto-layout +
   min/max width is how one component handles the longest localized string and the empty state without
   a separate frame.

5. **Use component properties + variants for the API, not duplicated layers.** Express the component
   model from `component-library-architecture` with Figma's property types:
   - **Variant properties** for the orthogonal axes — `intent` (primary/secondary/ghost/destructive),
     `size` (sm/md/lg), `state` (default/hover/focus/active/disabled/loading/selected/error). Keep
     axes *separate* properties, not one `primary-lg-loading` variant name — the same orthogonality
     rule the component skill enforces.
   - **Boolean** properties for optional parts (leading icon, full-width), **instance-swap** for
     slotted content (the icon, an avatar), **text** properties for labels. This is composition over a
     wall of duplicated component copies.
   - Cover the **full state set** as variant values, including **focus-visible** with a real ring
     bound to a focus token (≥3:1, WCAG 2.4.7/1.4.11) — an empty state cell is a bug, per doctrine's
     a11y floor (`doctrine/references/wcag-2.2-criteria.md`).
   See `references/figma-conventions.md` §Component properties & variants.

6. **Name everything to one scheme and hold it.** Layers, components, variables, styles, pages, and
   branches all follow a stated convention: components and variant props in a `Group/Name`,
   slash-nested form (`Button`, property `size=md`); variables dot/slash-pathed to their tier and role
   (`color/text/default`, `space/inset/md`, `radius/200`) so the name *says its tier* exactly as the
   token naming rule requires; layers named by role not `Frame 47`. Auto-generated names
   (`Rectangle 12`, `Group 5`) in a published library are the Figma form of drift. See
   `references/figma-conventions.md` §Naming.

7. **Operate the library through branching and disciplined publishing.** Make non-trivial changes on a
   **branch** of the library file (review → merge), never live on `main` where every subscriber sees
   half-finished work. **Publish** deliberately: review the change list, write a publish description,
   bump a stated version, and let product files **update** the subscribed library on their own cadence.
   A token/variable rename ripples to every consumer — treat publishes as releases, not autosaves.
   See `references/figma-conventions.md` §Branching & publishing.

8. **Set the file up so Dev Mode handoff is clean.** Dev Mode is where engineering reads the design:
   - Mark frames **Ready for Dev**; add **annotations** (measurements, behaviour notes, the token/
     variable name on each value) and **dev resources** (links to the component in code, the PR, the
     spec). Use **Dev Mode focus / compare** for what changed.
   - Because values are **variable-bound**, the inspect panel surfaces the *semantic variable name*
     (`color/action/primary/bg`) rather than a raw hex — which is exactly the token reference the
     written handoff (`design-handoff-and-dev-spec`) cites. Hardcoded values inspect as bare hex/px
     and force the developer to hardcode too.
   - Keep **Code Connect** / component-to-code mapping where it exists, so the inspected Figma
     component names the real code component. Dev Mode does not replace the written redline + acceptance
     criteria — it makes them trivially accurate. See `references/figma-conventions.md` §Dev Mode.

9. **Keep the anti-slop posture in-tool.** The convergent default is a file full of detached
   instances, raw hexes, and a generic blue flat-fill Button. The authored alternative is one
   variable-driven system where the one strong choice (a deliberate radius, a brand focus ring) is set
   once in a semantic variable and inherited everywhere. Component instances stay *attached*;
   overrides are deliberate, not accidental detaches. (`doctrine/design-doctrine.md` §0, §2.)

## Anti-Patterns

- **One giant file of loose frames** with no page/section structure and no library split — un-findable,
  un-publishable, and impossible to theme as a unit.
- **Theming with styles instead of variable modes** (or duplicating the whole UI as a "dark" page).
  Modes on the semantic collection are the seam; copies drift the instant a token changes.
- **Semantic variables holding raw hex** instead of aliasing a primitive — the Figma form of a
  component reaching past the semantic layer; nothing re-themes.
- **One mega-variant** (`variant = primary-lg-loading`) instead of separate `intent` / `size` /
  `state` properties — combinatorial, un-composable, un-reviewable.
- **Pixel-pushed components with no auto-layout** — they break at the next content length and can't
  bind padding to space tokens.
- **Missing state variants**, especially **focus-visible**, disabled, loading, and error — an empty
  cell in the variant matrix is a defect, not a default (WCAG 2.4.7).
- **Auto-named layers/components** (`Rectangle 12`, `Component 4`) and ad-hoc variable names that don't
  encode their tier — drift made visible.
- **Editing the library live on `main`** and **publishing without a description/version** — subscribers
  inherit half-finished work and can't tell what changed.
- **Detached instances and hardcoded values** that inspect as bare hex/px in Dev Mode, forcing
  engineering to hardcode and forking the system.
- Reproducing a **Sketch/XD/Axure** workflow (shared symbol-only theming, plugin-driven redlines,
  paper-first) in Figma instead of using variables/modes, component properties, and Dev Mode.

## Outputs

- A **Figma file/page/library architecture**: the Foundations/Components/Product split, the page and
  section scheme, and the naming convention, all stated.
- **Variable collections and modes** implementing the token tiers — `Primitives` + `Semantic`, with a
  `Theme` mode axis (light/dark/brand) and a `Breakpoint`/density number-mode axis — aliased, not
  duplicated, with the themed pairs holding the WCAG gate.
- A **styles-vs-variables decision record** for colour/type/effect/grid.
- **Components on auto-layout** with the property/variant API (variant axes + boolean + instance-swap +
  text) covering the full state set including focus-visible.
- A **branching + publishing convention** and a **Dev-Mode-ready** setup (Ready-for-Dev statuses,
  annotations, variable-surfaced inspect, dev resources / Code Connect) that feeds the written handoff.

## Examples

- `examples/sample-design-system-figma-setup.md` — a complete worked setup for a sample design system:
  the file/page/library split, the `Primitives` + `Semantic` variable collections with a `Theme`
  (Light/Dark/Brand-B) mode axis and a `Breakpoint` number-mode axis, the styles-vs-variables split,
  a Button built on auto-layout with its component-property/variant API, and the naming + branching +
  Dev-Mode conventions — every value mapping to the tokens from `design-tokens-and-naming`. Never lorem.

## References

- `doctrine/design-doctrine.md` — Mission §0 (one authored system beats five hedged copies; attached
  variable-driven components over a detached, hardcoded canvas) and Anti-Slop Charter §2 (state the
  choice first; the sourcing-authority asymmetry — what we build in Figma traces to the token system
  and human design authority, never to an AI tool's defaults).
- `doctrine/references/wcag-2.2-criteria.md` — the contrast floors (4.5:1 / 3:1) the themed variable
  modes must hold per theme, and focus-visible (2.4.7, 2.4.11, 1.4.11) required as a state variant.
- `references/figma-conventions.md` — the canonical in-tool conventions: file/page structure,
  variables & modes (theming + breakpoints), styles vs variables, component properties & variants,
  auto-layout, naming, branching & publishing, and Dev Mode handoff.
- Upstream: `09-…/design-tokens-and-naming` — the token tiers and semantic role map that Figma
  variables and modes carry (a Figma variable *is* a token's in-tool home; the name encodes its tier).
- Feeds: `09-…/design-handoff-and-dev-spec` (Dev Mode surfaces the variable/token names its redlines
  cite) and `09-…/component-library-architecture` (the variant/state/API model this skill builds in
  Figma).
- Standards/tooling (named for provenance, not in-repo): current Figma — variables & modes, component
  properties, auto-layout, Dev Mode, Code Connect, branching, team libraries; W3C Design Tokens Format
  Module (the token model the variables mirror).
<!-- dual-compat-end -->
