# Component: Button (worked spec)

A complete, concrete component spec following `../references/component-doc-template.md`.
Every value is a **semantic token** (from `design-tokens-and-naming`) — no literals — so the
component themes, goes dark, and rebrands for free. The state matrix is **fully covered**:
4 variants × 3 sizes × 9 states. A11y contract cites `doctrine/references/wcag-2.2-criteria.md`.

**Atomic level:** Atom · **Status:** active · **Owns layout?** no (fills a slot; never sets margin)
**Consumes tokens from:** color/action, space, radius, type, motion, border semantic groups.

---

## 1. Purpose & when to use
Triggers a single action. The most-used atom in the library — get it right and the system's
interaction language is set.

- **Use when:** the user commits an action (Save, Delete, Continue, Add).
- **Do NOT use when:** navigating to a URL → use `Link` (a real `<a>`); toggling on/off → use
  `Switch`/`Toggle`; selecting one of a set → use `SegmentedControl`. A button that navigates is
  an a11y and semantics failure.

## 2. Anatomy
```
┌──────────────────────────────────────────┐
│ [2]⚙  [3] Label text  [4]▾                │   [1] container (the <button>)
└──────────────────────────────────────────┘
```
| # | Part | Required? | Slot/prop | Token(s) |
|---|------|-----------|-----------|----------|
| 1 | container `<button>` | yes | element | `--radius-control`, `--space-*` (padding), `--border-width-control` |
| 2 | leading icon | no | `leadingIcon` slot | `--size-icon-inline`, inherits `fg` |
| 3 | label | yes (unless `iconOnly`) | `children` | `--font-label`, `--font-weight-medium` |
| 4 | trailing icon | no | `trailingIcon` slot | `--size-icon-inline` |
| — | spinner (loading) | conditional | internal | `--color-current`, `--duration-slow` |

## 3. Variant model (orthogonal axes — never one combined string)
| Axis | Type | Values | Default | Notes |
|------|------|--------|---------|-------|
| `variant` | enum | `primary` · `secondary` · `ghost` · `destructive` | `secondary` | one intent per button; max **one** `primary` per view |
| `size` | enum | `sm` · `md` · `lg` | `md` | sets height + padding + type + icon size |
| `loading` | boolean | true/false | false | runtime; disables interaction, shows spinner |
| `iconOnly` | boolean | true/false | false | requires `aria-label`; enforces square min 44×44 |
| `fullWidth` | boolean | true/false | false | stretches to container; layout stays caller's job |

> `disabled` and the hover/focus/active states are **runtime states**, not props — they live in
> the state matrix (§4), not the variant model.

### Size axis (token-backed)
| size | height | padding-x | font | icon | min target |
|------|--------|-----------|------|------|-----------|
| sm | `--size-control-sm` (32px) | `--space-3` (12px) | `--font-label-sm` | 16px | 24×24 floor; pad to meet 2.5.8 |
| md | `--size-control-md` (40px) | `--space-4` (16px) | `--font-label-md` | 18px | ✅ ≥40px |
| lg | `--size-control-lg` (48px) | `--space-5` (20px) | `--font-label-lg` | 20px | ✅ ≥48px |

## 4. State matrix — FULL coverage (the gate)
Treatments are **semantic tokens**, shown per variant. Token names follow
`--color-action-<variant>-<role>-<state?>`. Focus ring is **variant-independent** (one branded ring).

### 4a. `primary`
| State | Trigger | bg | fg | border | extra | a11y |
|-------|---------|----|----|--------|-------|------|
| default | — | `--color-action-primary-bg` | `--color-action-primary-fg` | none | — | contrast fg/bg ≥4.5:1 (1.4.3) |
| hover | pointer over | `--color-action-primary-bg-hover` | (same) | none | `transition: --duration-fast` | — |
| focus-visible | kbd focus | (bg unchanged) | (same) | none | **ring** `--color-focus-ring`, 2px, 2px offset | ring ≥3:1 vs both (1.4.11, 2.4.7); not obscured (2.4.11) |
| active/pressed | pointer down | `--color-action-primary-bg-active` | (same) | none | `scale .98` (skip if reduced-motion) | — |
| disabled | `disabled` attr | `--color-action-disabled-bg` | `--color-action-disabled-fg` | none | `cursor:not-allowed`; no hover/active | exempt from contrast, still perceivable; not color-alone (1.4.1) |
| loading | `loading` | `--color-action-primary-bg` | transparent label | none | centred spinner; label width reserved | `aria-busy="true"`; live "Loading…"; stays focusable, not activatable |
| selected | (N/A — buttons don't persist selection) | — | — | — | — | use `ToggleButton` with `aria-pressed` instead |
| error | (N/A for trigger button) | — | — | — | — | surface errors on the form, not the button |
| read-only | (N/A) | — | — | — | — | use `disabled` |

### 4b. `secondary` (token-tinted, bordered)
| State | bg | fg | border |
|-------|----|----|--------|
| default | `--color-action-secondary-bg` (subtle) | `--color-action-secondary-fg` | `--color-border-default` |
| hover | `--color-action-secondary-bg-hover` | (same) | `--color-border-strong` |
| focus-visible | (bg unchanged) | (same) | + **ring** `--color-focus-ring` |
| active | `--color-action-secondary-bg-active` | (same) | `--color-border-strong` |
| disabled | `--color-action-disabled-bg` | `--color-action-disabled-fg` | `--color-border-disabled` |
| loading | secondary-bg | transparent label + spinner | default border |

### 4c. `ghost` (no fill, no border until interaction)
| State | bg | fg | border |
|-------|----|----|--------|
| default | transparent | `--color-action-ghost-fg` | none |
| hover | `--color-action-ghost-bg-hover` | (same) | none |
| focus-visible | transparent | (same) | **ring** `--color-focus-ring` |
| active | `--color-action-ghost-bg-active` | (same) | none |
| disabled | transparent | `--color-action-disabled-fg` | none |
| loading | transparent | transparent label + spinner | none |

### 4d. `destructive` (irreversible/dangerous actions)
| State | bg | fg | border |
|-------|----|----|--------|
| default | `--color-action-danger-bg` | `--color-action-danger-fg` | none |
| hover | `--color-action-danger-bg-hover` | (same) | none |
| focus-visible | (unchanged) | (same) | **ring** `--color-focus-ring-danger` (distinct, still ≥3:1) |
| active | `--color-action-danger-bg-active` | (same) | none |
| disabled | `--color-action-disabled-bg` | `--color-action-disabled-fg` | none |
| loading | danger-bg | transparent label + spinner | none |

> **Coverage rule honoured:** every state a Button can *reach* is filled; `selected`/`error`/
> `read-only` are explicitly marked N/A with the correct component to use instead — not silently dropped.

## 5. API (props & slots)
| Name | Kind | Type | Default | Required | Description |
|------|------|------|---------|----------|-------------|
| `variant` | prop | `'primary'｜'secondary'｜'ghost'｜'destructive'` | `'secondary'` | no | intent axis |
| `size` | prop | `'sm'｜'md'｜'lg'` | `'md'` | no | size axis |
| `loading` | prop | boolean | `false` | no | shows spinner, blocks activation, keeps focus |
| `disabled` | prop | boolean | `false` | no | inert + not-allowed |
| `iconOnly` | prop | boolean | `false` | no | square; **requires** `aria-label` |
| `fullWidth` | prop | boolean | `false` | no | width:100% of container |
| `leadingIcon` | slot | node | — | no | icon before label |
| `trailingIcon` | slot | node | — | no | icon after label |
| `children` | slot | node | — | yes¹ | label (¹unless `iconOnly`) |
| `type` | prop | `'button'｜'submit'｜'reset'` | `'button'` | no | native form behavior |
| `onClick` | prop | handler | — | no | activation |

**Composition note:** Button stays a flat primitive (orthogonal enums + a few booleans, all
independent). It is composed *into* product buttons (`<Button variant="destructive">` inside a
`ConfirmDeleteButton` that owns the confirm logic) — the library button owns **no** domain logic.
See `../references/atomic-structure.md` §2–3.

## 6. Accessibility contract (WCAG 2.2 — cites `doctrine/references/wcag-2.2-criteria.md`)
- **Role/name/value (4.1.2):** native `<button>`; label from `children`; `iconOnly` → `aria-label`
  required (lint-enforced); `loading` → `aria-busy="true"` + visually-hidden live "Loading…".
- **Keyboard (2.1.1, 2.4.3):** focusable in DOM order; **Enter** and **Space** activate (native);
  no positive `tabindex`.
- **Focus-visible (2.4.7, 1.4.11):** token-driven ring (`--color-focus-ring`), 2px + 2px offset,
  **≥3:1** against both the button and the page; **`outline:none` is forbidden** without this
  replacement. Not hidden behind sticky chrome (2.4.11).
- **Target size (2.5.8):** `md`/`lg` exceed 44×44; `sm` (32px) meets the **24×24 floor** and is
  padded to 44×44 on touch / icon-only.
- **Motion (2.3.3):** hover/active transitions use `--duration-fast`; the pressed `scale .98` and
  spinner respect `prefers-reduced-motion` (reduce → no scale, opacity-only spinner).
- **Contrast (1.4.3):** every variant's default fg/bg verified ≥4.5:1; certify with the WCAG ratio,
  design with APCA (per the reference's method note).
- **State not by color alone (1.4.1):** disabled adds `cursor:not-allowed` + lowered affordance,
  not just a paler color; loading adds a spinner, not just a tint.

## 7. Do / Don't
| ✅ Do | ❌ Don't |
|------|---------|
| One `variant` enum + `size` enum | `isPrimary`/`isGhost`/`isDanger` booleans (boolean soup) |
| Exactly one `primary` per view | Three primaries competing for the eye |
| Token every color/space/radius | Hard-code `#2563eb` or `padding:12px` |
| Keep the branded focus ring | `outline:none` with no replacement (2.4.7 fail) |
| Use `<a>`/`Link` for navigation | Style a Button to navigate |
| `iconOnly` → `aria-label` | Icon-only button with no accessible name |
| Reserve label width when `loading` | Let the button resize on spinner swap (layout shift) |

## 8. Tokens consumed (the theming contract)
`--color-action-{primary,secondary,ghost,danger}-{bg,fg}[-{hover,active}]`,
`--color-action-disabled-{bg,fg}`, `--color-focus-ring`, `--color-focus-ring-danger`,
`--color-border-{default,strong,disabled}`, `--radius-control`, `--border-width-control`,
`--space-{3,4,5}`, `--size-control-{sm,md,lg}`, `--size-icon-inline`,
`--font-label-{sm,md,lg}`, `--font-weight-medium`, `--duration-fast`, `--duration-slow`.

> `dark-mode-and-theming` redefines exactly these tokens for the dark theme — the component
> body never changes. That is the payoff of binding every value to a token.

## 9. Changelog
- v1.0 — initial spec: 4 variants × 3 sizes × full state matrix; `loading`/`iconOnly`/`fullWidth`
  modifiers; WCAG 2.2 AA contract.

---

### Why this is "authored, not templated" (`doctrine/design-doctrine.md` §0)
The default AI Button is a flat blue fill with a generic radius and no real pressed or focus
state. This spec makes **specific, defensible** choices — a distinct destructive focus ring, a
considered pressed-state, a token-driven brand ring applied systematically — and routes all of
it through semantic tokens so one skilled hand shows across every variant and theme.
