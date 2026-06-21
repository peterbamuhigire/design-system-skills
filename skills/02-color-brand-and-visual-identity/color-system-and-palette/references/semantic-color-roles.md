# Reference: Semantic Color Roles (the role layer)

Components must reference **roles**, never literal hexes. The role is the stable name; the ramp
step it points at can be retuned, and dark mode is just a second binding of the same role names.
This is the contract that lets the whole system be remapped in one place.

## The core role set

| Role | Typical light binding | What it is |
|---|---|---|
| `surface` | ramp **50** (near-white, brand-tinted) | The dominant background — the ~60% in 60-30-10. |
| `surface-raised` | ramp **0 / white-tinted** | Cards, popovers, sheets — *lighter* than surface in light mode. |
| `surface-sunken` | ramp **100** | Wells, insets, code blocks — slightly *darker* than surface. |
| `text` | ramp **900** (near-black, brand-tinted) | Primary body/heading text. |
| `text-muted` | ramp **600–700** | Secondary text, captions — must **still pass 4.5:1** on surface. |
| `border` | ramp **200–300** | Hairlines, dividers, input outlines — needs **3:1** if it conveys state. |
| `accent` | ramp **500–600** (the anchor) | The brand voice — the ~10%. Earns its scarcity. |
| `accent-text` | the readable pair *on* accent | Text/icon colour that sits on an `accent` fill at ≥4.5:1. |
| `focus-ring` | accent or a high-C sibling | The 2px focus indicator — **3:1 against adjacent colours** (1.4.11). |

## The status set (do not invent per-component)

| Role | Hue family | Light binding intent |
|---|---|---|
| `success` | green ~`145` | A *brand-tuned* green, not stock `#22c55e`. |
| `warning` | amber ~`75` | Amber/ochre; never the only signal (pair with icon/text). |
| `error` / `danger` | red ~`25` | Brand-tuned red; the destructive voice. |
| `info` | blue/cyan ~`230` | Neutral informational; distinct from `accent` if accent is also blue. |

Each status role needs **two bindings**: a `*-fg` (the saturated foreground, e.g. icon/text) and a
`*-bg` (the tinted surface behind it). Both must pass their contrast gate against what sits on them.

## Two rules that make roles real

1. **Never colour by meaning twice.** `error` is one role with one (light) + one (dark) binding;
   a component asks for `error`, not `red-600`. If two roles must look identical, that is a sign to
   merge them, not to duplicate a hex.
2. **Roles carry the contrast contract, not the components.** Because `text-muted` is *defined* as
   "≥4.5:1 on `surface`", any component using it inherits a passing pair for free. The gate
   (SKILL step 6) is applied **per role pairing**, once, here — not re-litigated per screen.

## Dark mode = re-bind, never invert

The role names are identical; only the ramp bindings change (see SKILL step 8 and the worked
example). In dark mode `surface` points *low* (≈ramp 900/`oklch(0.18 …)`), `surface-raised` becomes
*lighter* than surface (the elevation logic flips), `text` points *high*, and every `accent` /
status foreground is **lightened and slightly desaturated** to hold its meaning at 3:1 / 4.5:1.
Re-run the contrast gate on the dark bindings independently — passing light does not imply passing
dark.

## Cross-refs
- `references/oklch-ramp-construction.md` — building the ramp these roles point into.
- `examples/oklch-palette-worked.md` — both bindings, with measured contrast.
- `doctrine/references/wcag-2.2-criteria.md` — the 4.5:1 / 3:1 floors each role inherits.
