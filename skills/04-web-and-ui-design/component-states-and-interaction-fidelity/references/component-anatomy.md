# Reference: Component Anatomy & Numbers (Book 3 baseline)

> Per-component **anatomy parts + measurable numbers** so every state cell names a *real part with
> a real measure* ("focus: 2px ring offset 2px on the 44px-high container"), not a vague verb.
> Numbers banked from *How to Design Better UI Components 3.0* (2022, rev. 2024) — the most
> operationally specific of the engine's six study books (see `docs/book-study/01-ui-ux-craft.md`,
> Book 3). **Use the numbers; reject the era's look** — Book 3 carries a 2020–21 sensibility
> (Material 2, residual glassmorphism) the doctrine bans (`doctrine/design-doctrine.md` §2;
> `doctrine/references/ai-slop-taxonomy.md`). Every number below should be expressed as a **token**,
> never a literal, when it lands in a component (`design-tokens-and-naming`).
>
> **Book 3's gaps this skill fills** (per the study): it has *no* focus-visible spec, *no* keyboard
> model, *no* motion/transition specs, *no* reduced-motion. Those come from
> `state-matrix-method.md` + `doctrine/references/wcag-2.2-criteria.md`. Book 3 supplies the
> static anatomy; this skill supplies the **states + transitions** on top.

---

## 1. How to read the numbers
- All dimensions are CSS px unless noted. Treat ranges as design latitude, not slop.
- **Hit area ≥ 44×44** (Apple HIG) / **48dp** (Material) on touch; the WCAG 2.2 **floor is 24×24**
  (2.5.8). Where a visible control is smaller, extend the target with **invisible padding**, not a
  bigger visual.
- The **2× padding rule**: horizontal padding ≈ **2× vertical** padding (optical balance).
- Bind each number to a token: heights → `--size-control-*`, paddings → `--space-*`, radius →
  `--radius-control`, ring → `--focus-ring-*`.

---

## 2. Button
**Anatomy:** container ‹button› · [leading icon] · label · [trailing icon] · (spinner when loading).

| Property | Number | Note |
|---|---|---|
| Height | **32–60** | 48 Material · 44 iOS · 32–40 desktop |
| Horizontal padding | **2× vertical** | e.g. 16 H / 8 V |
| Min hit area | **44×44** | via invisible padding if visual is smaller |
| Hierarchy | filled / ghost / text | = primary / secondary / tertiary |
| Label | action verb | "Create account", not "OK" |

**States to fill:** default, hover, focus-visible, active/pressed, disabled, loading. N/A:
selected (→ ToggleButton), error, read-only.

---

## 3. Input / text field (the worked example component)
**Anatomy:** field container · [leading icon/affix] · value/placeholder text · [trailing icon /
clear / reveal] · border · (below: label, help text, error text).

| Property | Number | Note |
|---|---|---|
| Height | **40–56** | ~44–48 comfortable touch |
| Horizontal padding | **12–16** | +4–8 vertical for optical balance |
| Border | **1–1.5px** | boxed fields parse faster than underline-only (Book 2) |
| Label | **above the field** | label ≠ placeholder — placeholder-as-label is a failure |
| Help / error | below, persistent | error text replaces/with help, never tooltip-only |

**States to fill:** default(empty), hover, focus-visible, **filled**, disabled, read-only,
loading(async validate), error/invalid, plus compound `focus-visible+error`. N/A: selected.

---

## 4. Dropdown / Select
**Anatomy:** trigger (value + caret) · popover/listbox · option rows ([checkbox if multi] · label ·
[selected check]) · [search field] · scroll container.

| Property | Number | Note |
|---|---|---|
| Scroll container | at **5+ items** | cap visible height, then scroll |
| Multi-select | checkbox rows | nested via indentation |
| Mobile | search + modal overlay | native-feeling full-screen at small widths |
| Option row height | ~36–44 | comfortable target |

**Book-3 state list:** default / hover / open / selected / disabled — **extended by this skill** to
add focus-visible (trigger *and* roving focus across options), loading (async options), error, and
the keyboard model (↑/↓ move, Enter select, Esc close, type-ahead) Book 3 omits.

---

## 5. Checkbox / Radio / Switch
**Anatomy:** control box (square=checkbox, **round=radio**) or track+thumb (switch) · [check/dot
glyph] · label.

| Property | Number | Note |
|---|---|---|
| Control box | **18–24** visual | hit area padded to ≥44 |
| Shape lock | square=checkbox, round=radio | never round a checkbox (semantic) |
| Switch | track + thumb | on/off = `checked` state |

**States to fill:** default, hover, focus-visible, **checked**, **indeterminate** (checkbox),
disabled, error (e.g. required group). `checked` replaces generic `selected`.

---

## 6. Card
**Anatomy:** container · [media (uniform aspect ratio)] · content (title · body · meta) · [actions].

| Property | Number | Note |
|---|---|---|
| Internal padding | **16–24** | 12–20 H, +4–8 V optical balance |
| Between cards | **16–40** | the card-spacing triad … |
| Around card sections | **64–96** | … (16-24 / 16-40 / 64-96) |
| Heights / images | fixed min/max + uniform aspect | truncate overflow with ellipsis |

**States (if interactive):** default, hover (lift/elevate), focus-visible (whole card if it's one
target), active, selected (if a selectable card), disabled. Static cards need only default.

> **Concentric radius (Book 2 tell):** an inner element's radius ≈ outer radius − its padding —
> nested radii must be concentric, not equal. Relevant when a focus ring or inner control sits
> inside a rounded card/field.

---

## 7. Search
**Anatomy:** input (≥44 high) · [leading search icon] · [clear button] · [recent / autocomplete
popover] · designed **no-results** state (→ `empty-error-and-loading-states`).

Mostly inherits Input states (§3) + the listbox states of a Dropdown (§4) for suggestions.

---

## 8. Frameworks Book 3 names (use as scaffolding, not taste)
8-pt grid (4-pt refinement) · box model · vertical rhythm · Atomic Design · 60-30-10 · F/Z scan
patterns. WCAG contrast (3:1 large/UI, 4.5:1 small) is embedded throughout Book 3 — but its a11y
**stops at contrast**; raise everything to WCAG 2.2 via `doctrine/references/wcag-2.2-criteria.md`.

> Sourcing note (doctrine §2): these numbers are human craft-literature, admissible as guidance.
> The look/era around them is **not** endorsed — mine numbers, author the appearance.
