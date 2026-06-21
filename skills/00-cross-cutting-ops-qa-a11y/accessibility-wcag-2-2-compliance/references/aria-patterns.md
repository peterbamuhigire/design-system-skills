# Reference: ARIA Patterns (native-first, name/role/value)

Companion to [`doctrine/references/wcag-2.2-criteria.md`](../../../../doctrine/references/wcag-2.2-criteria.md)
(the canonical criteria). This file is the **how**: how to give real components a correct
accessible name, role, and state, and which WAI-ARIA Authoring Practices (APG) pattern to follow.
Source: W3C WAI-ARIA Authoring Practices Guide (w3.org/WAI/ARIA/apg/) + ARIA 1.2 spec.

---

## 0. The five rules of ARIA (apply before writing any `role=`)

1. **Use a native HTML element if one exists.** `<button>`, `<a href>`, `<input>`, `<select>`,
   `<dialog>`, `<details>/<summary>`, `<nav>`, `<table>` ship role, name, focus, and keyboard
   for free. A `<div role="button" tabindex="0">` re-implements — usually incompletely — what
   `<button>` already does.
2. **Don't change native semantics** unless you must. Don't put `role="heading"` on a `<button>`.
3. **All interactive ARIA controls must be keyboard-operable** (see `keyboard-and-focus.md`).
4. **Don't make a focusable element `aria-hidden="true"`** — it vanishes from AT but still takes
   focus, stranding screen-reader users.
5. **Every interactive element needs an accessible name** (see §1). No name = announced as just
   its role ("button") or nothing.

---

## 1. Accessible name — where it comes from (precedence order)

A control's name is computed (the "accname" algorithm) roughly in this priority:

1. `aria-labelledby` (points at the id(s) of visible text) — **preferred**, keeps name visible.
2. `aria-label` (string) — when no visible label exists (e.g. icon-only).
3. Native label association: `<label for>`, wrapping `<label>`, `<legend>`, `alt`, `<caption>`,
   `title` on some elements.
4. Element content (a `<button>`'s text).
5. `title` / `placeholder` — last resort; **placeholder is not a label** (disappears, weak contrast).

**Icon-only example.** A bare icon button is silent:
```html
<!-- FAIL: announces "button" or nothing -->
<button><svg>…</svg></button>

<!-- PASS: visible-text-first via labelledby is best; aria-label when icon-only -->
<button aria-label="Delete item"><svg aria-hidden="true" focusable="false">…</svg></button>
```
Mark decorative SVGs/icons `aria-hidden="true"` and `focusable="false"` so they don't leak.

---

## 2. Role & value (the rest of 4.1.2)

- **Role** = what it is. Native element or, if unavoidable, `role="…"`.
- **State/value** = its current condition, kept in sync with the UI on every change:

| State / property | Use on | Notes |
|---|---|---|
| `aria-expanded` | disclosure, menu/combobox triggers, accordion headers | true/false; toggle on open/close |
| `aria-selected` | tabs, options, grid cells | the active one in a set |
| `aria-checked` | checkbox/radio/switch (custom) | true/false/`mixed` |
| `aria-pressed` | toggle buttons | true/false |
| `aria-current` | nav: current page/step | `page`, `step`, `true` |
| `aria-disabled` | controls disabled but kept in tab order | prefer native `disabled` when you don't need it focusable |
| `aria-invalid` + `aria-describedby` | form fields in error | point describedby at the error text |
| `aria-haspopup` | triggers that open menu/dialog/listbox | `menu`, `dialog`, `listbox`… |
| `aria-controls` / `aria-owns` | relate trigger ↔ controlled region | improves some AT navigation |

**Hidden vs disabled vs busy:** `aria-hidden` removes from the tree; `aria-disabled` keeps it
announced as unavailable; `aria-busy` marks a region as updating.

---

## 3. Live regions (announce async change without stealing focus)

```html
<div aria-live="polite" aria-atomic="true" class="visually-hidden" id="status"></div>
```
- `polite` waits for a pause (status, "Saved", validation summaries); `assertive` interrupts
  (use sparingly — errors that block progress).
- The region must **exist in the DOM before** you write into it; injecting a pre-filled live
  region often doesn't announce.
- Use `role="status"` (polite) or `role="alert"` (assertive) as shorthands.
- Don't spam: announce meaningful changes, not every keystroke.

---

## 4. Per-pattern recipes (map the component, then build)

For each, follow the APG page for full keyboard maps; keyboard details live in
`keyboard-and-focus.md`.

### Dialog (modal)
- `role="dialog"` (or native `<dialog>`), `aria-modal="true"`, named by its title via
  `aria-labelledby`; optional `aria-describedby` for intro text.
- On open: move focus inside (first field or the dialog), **trap** focus, render the rest of the
  page `inert`/`aria-hidden`. On close (Esc or button): **return focus to the trigger**.
- Verify it isn't obscured by sticky chrome (2.4.11).

### Disclosure / Accordion
- Trigger is a `<button>` with `aria-expanded` and `aria-controls` pointing at the panel.
- Accordion = a set of disclosures; headings wrap the buttons (`<h3><button>…`).

### Tabs
- `role="tablist"` › `role="tab"` (one `aria-selected="true"`) › `role="tabpanel"`
  (`aria-labelledby` the tab). **Roving tabindex**: one tab stop, arrows switch tabs.

### Menu / Menu button
- Trigger: `<button aria-haspopup="menu" aria-expanded>`. Menu: `role="menu"` ›
  `role="menuitem"`. Arrow keys move, Enter/Space activate, Esc closes and returns focus.
- (A site nav of links is **not** a `menu` — use `<nav>` + `<ul>` of `<a>`.)

### Combobox / Autocomplete
- `role="combobox"` on the input, `aria-expanded`, `aria-controls` the listbox, and
  `aria-activedescendant` to mark the highlighted option (`role="option"` in `role="listbox"`).

### Data table
- Native `<table>` with `<caption>`, `<th scope="col|row">`. Don't fake tables with `<div>`s.
  For sortable headers, add `aria-sort` (`ascending`/`descending`/`none`).

### Toast / notification
- Render into a `role="status"` (polite) or `role="alert"` (assertive) live region; don't move
  focus for non-critical toasts; ensure they're dismissible and not solely time-limited.

### Carousel
- Provide prev/next **buttons** (not drag-only — 2.5.7), a pause control if it auto-advances
  (2.2.2), and announce slide changes politely.

---

## 5. Screen-reader smoke test (what "passes")

Walk the flow with **NVDA + Firefox/Chrome** (Windows) and **VoiceOver + Safari** (mac/iOS):
- Every control announces a sensible **name + role + state** (e.g. "Delete item, button";
  "Notifications, switch, on"; "Email, edit, invalid, Enter a valid email").
- Headings form a logical outline (use the rotor/elements list); landmarks present
  (`<header>/<nav>/<main>/<footer>` or roles).
- Dynamic changes are announced once, politely; nothing announces twice or floods.
- Decorative images are silent; meaningful images are described.
- Reading order matches visual order.

> Automated tools (axe/Lighthouse) find ~30–40% of issues — this manual pass is mandatory.
> See `wcag-2.2-criteria.md` §testing.
