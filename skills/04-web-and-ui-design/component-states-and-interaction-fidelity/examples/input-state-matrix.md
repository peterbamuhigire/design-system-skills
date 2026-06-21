# Worked example: Text Input — full state-fidelity spec

A complete, concrete **interactive-state fidelity** spec for one real component — a single-line
text Input / form field — built with `../references/state-matrix-method.md` and the anatomy/numbers
in `../references/component-anatomy.md` (Book 3). Every value is a **semantic token** (from
`design-tokens-and-naming`) — no literals — so the field themes, goes dark, and rebrands for free.
A11y cites `doctrine/references/wcag-2.2-criteria.md`. Never lorem.

**Atomic level:** Atom (the bare control) — composed *into* the `Field` molecule (Label + Input +
HelpText + Error) by `09…/component-library-architecture`. This spec owns the **states + transitions**;
the variant/API model is owned there; the field-level validation *content* is owned by `04…/form-ux-design`.

---

## 1. Anatomy (parts a state may change)
```
  Label                                  ← (in the Field molecule, above)
┌────────────────────────────────────────┐
│ [2]🔍  [3] value / placeholder   [4]✕  │   [1] field container (border + bg)
└────────────────────────────────────────┘
  Help text  /  Error text                ← (below; help replaced by error)
```
| # | Part | Token(s) | Number (Book 3) |
|---|------|----------|-----------------|
| 1 | container (border + bg) | `--color-field-bg`, `--color-field-border`, `--radius-control`, `--border-width-control` | height **40–56**, padding **12–16 H** |
| 2 | leading icon / affix (optional) | `--color-field-icon`, `--size-icon-inline` | 16–20 |
| 3 | value / placeholder text | `--color-field-fg` / `--color-field-placeholder`, `--font-body` | placeholder ≠ label |
| 4 | trailing slot (clear ✕ / reveal 👁 / status) | `--color-field-icon`, `--size-icon-inline` | hit area ≥44 |

> Cursor over the editable region is `text`; over the container chrome `default`.

---

## 2. Reachable states & N/A decisions
Reachable: **default(empty) · hover · focus-visible · filled · disabled · read-only · loading
(async validate) · error/invalid**, plus the compound **focus-visible + error** and **hover + filled**.
**N/A:** `selected/checked` → an input has no selection state; the on-equivalent is `filled`.
`active/pressed` → an input has no momentary press; the meaningful transient is **focus**.

---

## 3. State matrix — FULL coverage (the gate)
Treatments are **semantic tokens**, naming the anatomy part that changes. An empty cell would be a bug.

| State | Trigger | container bg | container border | value/placeholder | trailing | cursor | a11y |
|-------|---------|--------------|------------------|-------------------|----------|--------|------|
| **default (empty)** | idle, enabled | `--color-field-bg` | `--color-field-border` (1px) | placeholder `--color-field-placeholder` | — | text | placeholder ≥4.5:1 (1.4.3); not a substitute for `<label>` |
| **hover** | `pointerenter` | `--color-field-bg` | `--color-field-border-hover` (slightly stronger) | (unchanged) | clear ✕ may reveal | text | no layout shift; pointer-only |
| **focus-visible** | keyboard/AT focus (`:focus-visible`) | `--color-field-bg` | `--color-field-border-focus` + **ring** `--color-focus-ring` 2px / 2px offset | caret visible | — | text | ring ≥3:1 vs field **and** page (1.4.11, 2.4.7); not obscured by sticky chrome (2.4.11); ring appears **instantly** |
| **filled** | has a value | `--color-field-bg` | `--color-field-border` | value `--color-field-fg` | clear ✕ shown | text | value contrast ≥4.5:1 |
| **disabled** | `disabled` attr | `--color-field-bg-disabled` | `--color-field-border-disabled` | `--color-field-fg-disabled` | hidden | `not-allowed` | exempt from contrast but perceivable; **not color-alone** (1.4.1); removed from tab order |
| **read-only** | `readonly` attr | `--color-field-bg-readonly` (subtle) | `--color-field-border` | `--color-field-fg` | hidden ✕; copy still works | text | **still focusable & selectable** (≠ disabled); `aria-readonly` (4.1.2) |
| **loading (async validate)** | async check in flight | `--color-field-bg` | `--color-field-border-focus` | (value kept) | **spinner** (replaces ✕) | text | `aria-busy="true"`; field stays focusable; live "Checking…" (4.1.3); **no layout shift** (spinner occupies ✕ slot) |
| **error / invalid** | failed validation | `--color-field-bg` | `--color-field-border-error` | `--color-field-fg` | ⚠ error glyph | text | border **+** ⚠ icon **+** error text below — color-not-alone (1.4.1); `aria-invalid="true"` + `aria-describedby="…err"` (3.3.1) |
| **focus-visible + error** (compound) | focused while invalid | `--color-field-bg` | `--color-field-border-error` + **ring** `--color-focus-ring-error` (distinct, still ≥3:1) | `--color-field-fg` | ⚠ | text | error ring must remain ≥3:1; both invalid AND focused exposed to AT |

> **Coverage honoured:** every reachable state filled; `selected/checked` and `active/pressed`
> explicitly N/A (§2) with the right equivalent named, not silently dropped.

---

## 4. Transition table — the moves between states (not just the endpoints)
Durations/easing are **motion tokens** (`--duration-*`, `--ease-*`), aligned with `08-motion-and-interaction`.

| From → To | Trigger | Property | Duration | Easing | Reduced-motion path |
|-----------|---------|----------|----------|--------|---------------------|
| default → hover | `pointerenter` | `border-color` | `--duration-fast` (~140ms) | `--ease-standard` | identical (color only — already motion-safe) |
| hover → default | `pointerleave` | `border-color` | `--duration-fast` | `--ease-standard` | identical |
| any → focus-visible | keyboard focus | **ring opacity 0→1** + `border-color` | **instant** (ring) ; ~120ms border | — | **instant**, unchanged — focus feedback never fades |
| focus-visible → default/filled | blur | ring removal + `border-color` | instant ring; ~120ms border | `--ease-standard` | instant |
| empty → filled | first keystroke | trailing ✕ fade-in | `--duration-fast` | `--ease-out` | ✕ appears instantly (no fade) |
| focus-visible → loading | submit/blur triggers async | ✕→spinner swap (same slot) | instant swap; spinner rotates | linear (spinner) | spinner → **opacity pulse**, not rotation |
| loading → filled (valid) | async resolves OK | spinner→✓ then ✕ | ~200ms | `--ease-out` | instant swap, no spin |
| loading → error | async resolves bad | spinner→⚠ + border→error + error text reveals | ~160ms | `--ease-standard` | instant; text reveals without height-animate |
| error → default | user fixes value | border→default + ⚠/text remove | ~140ms | `--ease-standard` | instant |

**Rules applied:** focus ring is **never animated in** (instant feedback); the `loading`/`error`
**return** moves are specified, not only the forward direction; the ✕↔spinner↔⚠ swaps all occupy
the **same trailing slot** so there is **zero layout shift**; every animated move has a
`prefers-reduced-motion` fallback (2.3.3).

---

## 5. Focus-visible clause (WCAG 2.2 — `doctrine/references/wcag-2.2-criteria.md`)
- **Visible & contrasted (2.4.7, 1.4.11):** token ring `--color-focus-ring`, 2px width + 2px
  offset, **≥3:1** against both the field bg and the page. On error, `--color-focus-ring-error`
  (distinct) still ≥3:1.
- **Not obscured (2.4.11):** the focused field is fully visible — `scroll-margin` keeps it clear of
  sticky headers/footers when focus scrolls it into view.
- **`:focus` vs `:focus-visible`:** ring shown for keyboard/AT only; a mouse-click into the field
  gets the caret + border-focus but no keyboard ring (noise). Keyboard users always get the ring.
- **No naked `outline:none`:** the UA outline may be replaced **only** by this token ring — never removed.
- **Instant:** ring opacity 0→1 is immediate; no fade (see §4).

---

## 6. Per-state a11y certification
- [x] Contrast holds default/hover/focus/filled/error (value & placeholder ≥4.5:1; border/ring ≥3:1) — 1.4.3/1.4.11.
- [x] focus-visible ≥3:1, not obscured, instant, token ring — 2.4.7/2.4.11/1.4.11.
- [x] disabled perceivable beyond color (bg + cursor + removed from tab order) — 1.4.1.
- [x] read-only ≠ disabled: focusable, selectable, `aria-readonly` — 4.1.2.
- [x] loading: `aria-busy`, live "Checking…", focus kept, no layout shift — 4.1.3.
- [x] error: border **+** ⚠ icon **+** text + `aria-invalid` + `aria-describedby` — 1.4.1/3.3.1.
- [x] target: trailing controls (✕/reveal) hit area ≥44; field height 44–56 — 2.5.8.
- [x] name/role/value: real `<input>` + associated `<label>` (in the Field molecule) — 4.1.2.
- [x] every animated transition has a reduced-motion path — 2.3.3.
- [x] no empty cell; `selected`/`active` N/A with equivalents named.

---

## 7. Tokens consumed (theming contract)
`--color-field-{bg,fg,border,placeholder,icon}`, `--color-field-{bg,fg,border}-{hover,focus,disabled,readonly,error}`,
`--color-focus-ring`, `--color-focus-ring-error`, `--radius-control`, `--border-width-control`,
`--size-icon-inline`, `--font-body`, `--space-{3,4}`, `--size-control-md`,
`--duration-fast`, `--ease-standard`, `--ease-out`.

> `dark-mode-and-theming` redefines exactly these tokens for dark — the field body never changes.

---

### Why this is "authored, not templated" (`doctrine/design-doctrine.md` §0)
The convergent AI input is a flat grey box that turns blue on focus with a 1px ring and no real
error/loading fidelity. This spec makes specific, defensible moves — a distinct **error focus
ring**, a **same-slot** ✕↔spinner↔⚠ swap that guarantees zero layout shift, an **instant**
(never-fading) focus ring, and a real read-only-vs-disabled distinction — all routed through tokens
so one skilled hand shows across every state, transition, and theme.
