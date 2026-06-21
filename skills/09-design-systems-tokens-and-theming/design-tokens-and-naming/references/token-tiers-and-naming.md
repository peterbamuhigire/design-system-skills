# Reference: Token Tiers and the Naming Scheme

The structural rules that keep a token system theme-able and drift-proof. Provenance: Salesforce
Lightning / Adobe Spectrum / Atlassian / GitHub Primer token architectures, Nathan Curtis'
"Naming Tokens in Design Systems," and the W3C Design Tokens Community Group format. Aligned to the
Chwezi colour and type-scale doctrine (`doctrine/references/`).

---

## 1. The three tiers (every token lives in exactly one)

```
Component token   →   Semantic token   →   Primitive token   →   literal value
button.primary.bg     color.action.        color.brand.600        oklch(0.55 0.17 255)
                      primary.bg
```

A token may reference **only the tier immediately above it**. The arrow never skips a tier and
never reverses. This single constraint is what makes a system theme-able.

### Tier 1 — Primitive (a.k.a. global / option / base / core)
- Raw, context-free values. The complete colour ramps, every type size, the full space scale,
  radii, raw shadow values, raw durations.
- Named by **what the value is**, never where it is used. A primitive has no opinion about role.
- Examples: `color.blue.500`, `color.neutral.50`, `space.400`, `font.size.300`,
  `radius.200`, `duration.fast`.
- **Rule:** components and app code must NEVER reference a primitive directly. Primitives are the
  raw material; only semantic tokens consume them.

### Tier 2 — Semantic (a.k.a. alias / system / decision / applied)
- Role names that point at primitives and carry **intent**. This is the *only* tier a theme
  re-points. It is the public contract of the system.
- Named by **what the value is for**: surface vs text vs border vs action vs status.
- Examples: `color.text.default`, `color.text.muted`, `color.surface.default`,
  `color.surface.raised`, `color.border.default`, `color.action.primary.bg`,
  `color.feedback.error.fg`, `space.inset.md`, `elevation.raised`.
- **Rule:** if two semantic tokens always resolve to the same primitive *by coincidence*, keep
  them separate — they may diverge in a future theme. Shared *meaning* is what merits a shared token,
  not a shared current value.

### Tier 3 — Component
- The most specific tier, scoped to one component, pointing at semantic tokens.
- Exists so a single component can be retuned without disturbing the shared semantic layer.
- Examples: `button.primary.bg → color.action.primary.bg`, `card.padding → space.inset.lg`,
  `input.border.focus → color.border.focus`, `tooltip.bg → color.surface.inverse`.
- **Rule:** create a component token only when the component genuinely needs to diverge or when a
  handoff is clearer for it. Do not mint a component token that is a pure 1:1 passthrough of a
  semantic token with no reason — that is noise. Prefer referencing the semantic token directly.

---

## 2. The naming convention

One shape, applied everywhere. Drop segments that don't apply; never reorder them.

```
[namespace].[category].[concept].[property].[variant].[state]
```

| Segment | Question it answers | Examples |
|---|---|---|
| namespace | Which system/brand? (optional once, prefix to avoid collisions) | `mdk`, `sys` |
| category | What kind of value? | `color`, `space`, `font`, `size`, `radius`, `elevation`, `duration`, `easing`, `border` |
| concept | What role/object? | `text`, `surface`, `border`, `action`, `feedback`, `inset`, `size` |
| property | Which property of it? | `bg`, `fg`, `border`, `ring` |
| variant | Which variant? | `primary`, `secondary`, `danger`, `muted`, `raised`, `md` |
| state | Which interaction state? | `default`, `hover`, `active`, `disabled`, `focus`, `selected` |

Examples that parse cleanly:
- `color.action.primary.bg.hover`
- `color.text.muted`
- `space.inset.md`
- `color.feedback.error.surface`
- `button.danger.border.focus`

### Hard rules
1. **The name must reveal the tier.** A reader tells a primitive (`color.blue.500`) from a
   semantic token (`color.text.default`) from a component token (`button.primary.bg`) by the name
   alone. If you can't, the name is wrong.
2. **Never bake the literal value into a role name.** `color.text.blue` is banned — when the brand
   recolours, the name lies. Roles are named by *job*, not by *current colour*.
3. **No positional or accidental cruft.** `color.box-2`, `spacing-thing-3`, `gray-new` are banned.
4. **Pick ONE scale-step vocabulary and hold it system-wide.** Either numeric `50 100 … 900`
   (good for ramps, infinitely extensible) OR t-shirt `xs sm md lg xl 2xl 3xl` (good for space/size,
   human-readable). Don't mix within a category. Numeric for colour ramps + t-shirt for space is a
   common, acceptable split *as long as it's consistent per category*.
5. **Decide singular vs plural once** (`color` not `colors`) and apply it everywhere.
6. **Abbreviations only from a written glossary.** `bg`/`fg` are fine because they're listed here;
   inventing `clr` or `bkgnd` ad hoc is not.
7. **Lower-kebab inside a segment, dot between segments** (`action.primary.bg`). When emitted to a
   platform that can't take dots, transform deterministically (see `token-export-formats.md`):
   dots → `-` for CSS (`--color-action-primary-bg`).

---

## 3. The standard semantic colour role set (start here, extend deliberately)

A minimal, sufficient role vocabulary. Most systems need only these plus a few component tokens.

| Role group | Roles |
|---|---|
| Surface | `surface.default`, `surface.subtle`, `surface.raised`, `surface.sunken`, `surface.inverse` |
| Text | `text.default`, `text.muted`, `text.subtle`, `text.on-action`, `text.inverse`, `text.link` |
| Border | `border.default`, `border.subtle`, `border.strong`, `border.focus` |
| Action (×variant) | `action.primary.bg`, `action.primary.bg.hover`, `action.primary.fg`, `action.secondary.*`, `action.danger.*` |
| Feedback (×status) | `feedback.{success,warning,error,info}.{surface,fg,border}` |
| Focus | `border.focus` / `ring.focus` (must clear 3:1 against both adjacent surfaces) |

Type, space, radius, elevation, motion follow the same tiered/named pattern — see the SKILL
workflow step 6 and `doctrine/references/type-scale-and-spacing.md` for the underlying numbers.

---

## 4. Why three tiers (the payoff, stated plainly)

- **Theming is a re-point, not a rewrite.** Dark mode, each brand, each density mode change only
  the semantic→primitive aliases. Components never change. (See `examples/semantic-mapping.md`.)
- **One place to retune.** Change `color.action.primary.bg` once; every button, link, and accent
  updates, and the WCAG gate is re-checked in one place.
- **Drift becomes detectable.** A primitive referenced from a component, or a raw hex in a
  component, is now a *visible* rule violation a linter can catch — not an invisible time-bomb.
