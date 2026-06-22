# Figma Conventions (current, 2026)

Canonical in-tool conventions for operating a design system in **current Figma** — variables &
modes, styles vs variables, component properties & variants, auto-layout, naming, branching &
publishing, and Dev Mode handoff. This is the Figma-operating layer beneath the skill; the *what*
of the token model lives in `design-tokens-and-naming`, and the *written* handoff spec lives in
`design-handoff-and-dev-spec`. Explicitly modern Figma — no Sketch/XD/Axure equivalents are
reproduced here.

> Provenance: built against current Figma capabilities (variables with modes, component properties,
> auto-layout, Dev Mode, Code Connect, branching, team libraries). The older-tooling workflows the
> beginner UI/UX primers assume (Axure/Sketch/Adobe XD, paper-first) are deliberately out of scope.

---

## File & page structure

**Split into library files, not one mega-file.** A maintainable system is at least:

| File | Holds | Published as |
|---|---|---|
| **Foundations / Tokens** | Variable collections (primitives, semantic), text/effect/grid styles, colour & type specimens | Library (subscribed by everything) |
| **Components** | The component set, built on Foundations | Library (subscribed by product files) |
| **Product / Feature** files | Screens & flows that *consume* both libraries | Usually not a library |

This keeps theming and components published **once** and fanned out, rather than copied — a copied
theme is a theme that will drift.

**Pages are top-level sections.** A consistent page spine, e.g.:

- `Cover` — file purpose, owner, status, version, links.
- `🧱 Foundations` — variables/styles specimens (Foundations file).
- `🧩 Components` — one section per component (Components file).
- `📐 Patterns` — composed patterns/templates.
- `🚧 WIP` — in-progress, not for consumption.
- `🗄 Archive` — deprecated, kept for reference.

**Sections** (the frame-grouping primitive) chunk a page — one section per component, per flow, or
per state group — so the canvas is navigable. **One page of loose ungrouped frames is the structural
defect**: nothing is findable, nothing publishes cleanly.

---

## Variables & modes (theming + breakpoints)

Variables are where tokens live in-tool and where theming happens. Map them to the token tiers.

### Collections = tiers

- **`Primitives`** collection — raw, context-free values: the full colour ramps, the space/size
  scale, the radius set. Named by what they are (`color/blue/500`, `space/400`, `radius/200`).
  Components must never bind to these directly.
- **`Semantic`** collection — role aliases that **reference** primitives and carry intent
  (`color/text/default`, `color/surface/raised`, `color/action/primary/bg`, `space/inset/md`). This
  is the only tier a theme re-points; it is the contract.
- **Component tier** — usually expressed as the component's bound properties (or a small
  per-component collection) pointing at semantic variables. A component is retuned here without
  touching the shared semantic layer.

Each tier references **only the tier above it**: component → semantic → primitive → literal. A
semantic variable that holds a raw hex (instead of aliasing a primitive) is the Figma form of a
component reaching past the semantic layer — and nothing re-themes. **Alias, never duplicate.**

### Modes = the theming seam

Put theme variation on **modes** of the **semantic** collection. Each mode is a column; each
semantic variable resolves to a (possibly different) primitive per mode.

- **`Theme` axis:** modes `Light`, `Dark`, and brand/tenant modes (`Brand-B`, `Tenant-X`). Switching
  the mode on a frame re-skins it; the components are byte-identical across modes — **only the alias
  targets change**. This is "semantic tokens are the theming seam, never the primitives," in-tool.
- **Dark is a deliberate re-point, not a lightness inversion.** Dark modes alias to lower-chroma
  surfaces and a near-dark grey carrying the brand hue; accents usually lighten and slightly
  desaturate. Re-check contrast per mode (below).
- **Mode limits & structure:** mode count per collection is bounded on paid plans and tighter on
  free — so model orthogonal axes (theme *and* breakpoint) as **separate collections**, not one
  collection with a combinatorial explosion of modes. Apply each collection's mode independently on a
  frame.

### Breakpoints/density as number modes

Use **number variables in modes** for responsive/density variation: a `Breakpoint` axis with modes
`Compact` / `Regular` / `Expanded` driving spacing, container width, and type-step numbers. One frame
adapts by switching the breakpoint mode instead of maintaining three hand-built copies. Density
(comfortable/compact) is another number-mode axis if the system needs it.

### The WCAG gate is a per-mode invariant

Any sanctioned foreground/surface pairing must clear **4.5:1** (body/small text) and **3:1** (large
text ≥24px or ≥18.66px bold, and meaningful UI/icons/focus) — **in every mode**
(`doctrine/references/wcag-2.2-criteria.md`, WCAG 1.4.3/1.4.11). Light passing does not imply dark
passing; verify each mode and record the result. A variable mode that can produce a failing pair is a
bug, not a style.

---

## Styles vs variables

They are not interchangeable. The seam decides what themes and what doesn't.

| Use a **variable** for | Use a **style** for |
|---|---|
| Any single value that themes/mode-switches: all colour fills & strokes, spacing, radius, sizing, individual type values, breakpoint numbers | A bundled, multi-property object the tool applies as one named unit |
| → re-points per mode automatically | **Text styles** (font + size + line-height + spacing + weight) |
| | **Effect styles** (shadow/blur) — theme the colour via a variable-bound fill |
| | **Grid styles** (column/row layout grids) |

**Rule:** a value a theme re-points → **variable**; a composite the tool applies as one bundle →
**style, with its themeable parts variable-bound underneath** (back a text style's size by a number
variable; back an effect style's shadow colour by a colour variable). This keeps dark mode and
multi-brand free. Pure colour/spacing styles with no variable behind them are legacy — migrate them
to variables.

---

## Component properties & variants

Express the component model from `component-library-architecture` with Figma's property types — not
duplicated layers.

- **Variant properties** = the orthogonal axes, each a **separate property**:
  - `intent` = primary / secondary / ghost / destructive
  - `size` = sm / md / lg
  - `state` = default / hover / focus / active / disabled / loading / selected / error
  Keep them separate — **never** one mega-property `primary-lg-loading`. The API is the *product* of
  small independent enums (same orthogonality rule the component skill enforces).
- **Boolean** properties for optional parts: `has-leading-icon`, `full-width`.
- **Instance-swap** properties for slotted content: the icon, an avatar — composition over
  duplication.
- **Text** properties for editable labels.

**Cover the full state set** as `state` variant values, including **focus-visible** with a real ring
bound to a focus colour variable (≥3:1 vs adjacent surface; WCAG 2.4.7 / 2.4.11 / 1.4.11). An empty
cell in the variant matrix is a defect, not a default. Bind every value (padding, gap, fill, stroke,
radius, type) to a variable — a hardcoded hex/px in a component is a defect that can't theme.

Keep instances **attached**; make overrides deliberate. Accidental detaches are how a system forks.

---

## Auto-layout

Every system component is built on **auto-layout**:

- **Padding & gap bound to space variables** (`space/inset/md`, `space/stack/sm`) — never raw pixels.
- **Direction, wrap, and alignment** set so the component reflows; **hug** vs **fill** vs fixed
  sizing chosen per child; **min/max width** so the same component handles the longest localized
  string and the empty state without a separate frame.
- Nested auto-layout for composite components (a Field = Label + Input + Help + Error stacked with a
  gap variable). Pixel-pushed frames break at the next content length and can't bind to space tokens.

---

## Naming

One scheme, everywhere, held:

- **Variables:** dot/slash-pathed to tier + role so the **name says its tier** —
  `color/text/default`, `color/action/primary/bg`, `space/inset/md`, `radius/200`,
  `elevation/raised`. Primitives read as primitives (`color/blue/500`); semantics read as roles.
- **Components & variants:** `Group/Name` slash-nesting for organisation; variant properties as
  `prop=value` (`size=md`, `intent=primary`). No `Component 4`.
- **Layers:** named by role (`label`, `icon-leading`, `container`), never `Frame 47` / `Rectangle 12`
  in a published library.
- **Styles:** pathed like variables (`text/body/md`, `effect/shadow/raised`).
- **Pages, sections, branches:** the stated spine above; branches named for the change
  (`feat/button-loading-state`), not `Branch 2`.

Auto-generated names in a published library are drift made visible.

---

## Branching & publishing

- **Branch for non-trivial change.** Edit on a **branch** of the library file, review the diff, then
  merge to `main`. Never make in-progress edits live on `main` where every subscriber sees them.
- **Publish deliberately, as a release.** Review the change list, write a **publish description**,
  bump a **stated version**, and let product files **update** the subscribed library on their own
  cadence. A variable/token rename ripples to every consumer — treat publishes as releases, not
  autosaves. Communicate breaking renames.
- **Subscription hygiene:** product files pull library updates intentionally and review the change
  before accepting, so a publish can't silently break a screen.

---

## Dev Mode (handoff)

Dev Mode is where engineering reads the design; set the file up so it is clean.

- **Statuses:** mark frames **Ready for Dev** when specced; keep WIP out of the dev surface.
- **Annotations:** add measurement/behaviour annotations and surface the **token/variable name** on
  each value. Because values are variable-bound, the **inspect panel shows the semantic variable
  name** (`color/action/primary/bg`) — which is exactly the token reference the written redline
  cites. Hardcoded values inspect as bare hex/px and force the developer to hardcode too.
- **Dev resources:** attach links — the component in code, the PR/branch, the written spec.
- **Compare / focus:** use Dev Mode's change-comparison so engineering sees what changed between
  versions.
- **Code Connect:** where set up, map the Figma component to the real code component so inspection
  names the actual import. 
- **Boundary:** Dev Mode does **not** replace the written redline + acceptance criteria
  (`design-handoff-and-dev-spec`) — it makes them trivially accurate by surfacing real token names.

---

## Cross-references

- `design-tokens-and-naming` — the token tiers, naming, OKLCH values, and export topology these
  variables/modes carry. A Figma variable is a token's in-tool home; the variable name encodes the
  token's tier.
- `component-library-architecture` — the variant/state/API model that becomes component properties
  + variants here.
- `design-handoff-and-dev-spec` — consumes the Dev-Mode-ready setup; its redlines cite the variable
  names the inspect panel surfaces.
- `doctrine/design-doctrine.md` §0/§2 — authored, variable-driven, attached-instance systems over a
  detached, hardcoded canvas; state the choice first.
- `doctrine/references/wcag-2.2-criteria.md` — the per-mode contrast gate and focus-visible
  requirement.
