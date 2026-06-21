# Reference: The State-Matrix Method — enumerate, fill, transition, certify

> The per-component **interactive-state fidelity** method, owned by
> `component-states-and-interaction-fidelity`. A component is not done when its `default` frame
> looks good; it is done when **every reachable interactive state** has a token-backed treatment
> **and** every move between states is specified. This is the control-level companion to the
> screen-level enumeration in `04…/empty-error-and-loading-states/references/state-matrix.md`.
> Cites `doctrine/references/wcag-2.2-criteria.md` and `doctrine/design-doctrine.md`.

---

## 1. The method in four moves

1. **Enumerate** the reachable states (§2). Mark non-reachable ones **N/A + the right alternative**.
2. **Fill** each reachable cell with a **token-backed** treatment naming the anatomy part that
   changes (§3).
3. **Transition** — specify the move between every adjacent pair: trigger, animated property,
   duration + easing token, reduced-motion path (§5).
4. **Certify** every state against the WCAG 2.2 AA floor (§4, §6).

> **Enumerate first, design second. An empty cell is a bug, not a default.**

---

## 2. The nine interactive states (the matrix rows)

Every interactive component is measured against these nine. Fill the ones it can reach.

| State | Trigger / condition | What it must communicate |
|---|---|---|
| **default (rest / enabled)** | idle, interactive | "this is operable" — clear affordance |
| **hover** | pointer over (pointer devices only) | "this responds" — subtle, not a layout shift |
| **focus-visible** | keyboard/AT focus (`:focus-visible`) | "you are here" — the **mandatory** ring (§4) |
| **active / pressed** | pointer/key down, mid-activation | "registered" — a momentary shift |
| **disabled** | not currently operable | "not available now" — perceivable, not by color alone |
| **loading / busy** | async work in flight | "working" — `aria-busy`, focus kept, no layout shift |
| **selected / checked / current** | persistent on-state (toggle, tab, option, row) | "this is chosen" — via `aria-pressed/checked/selected` |
| **error / invalid** | failed validation / bad value | "fix this" — color **+** text + `aria-invalid` |
| **read-only** | value shown, not editable (≠ disabled) | "view, can't change" — still focusable/selectable |

**Reachability examples (mark N/A explicitly):**
- Trigger **Button** → no `selected` (use ToggleButton/`aria-pressed`), no `read-only` (use `disabled`).
- **Link** → no `loading`, no `disabled` (links don't disable — remove or replace with a button).
- **Checkbox/Radio/Switch** → `selected` becomes `checked`; also `indeterminate` for tri-state.
- **Tab / nav item / menu option / table row** → `selected` = `current`/`aria-selected`.
- **Input** → all nine *except* `selected` (it has `filled` instead) — see the worked example.

Combinations matter: `hover` + `selected`, `focus-visible` + `error`, `disabled` while `selected`.
Decide which **compound** cells are reachable and define the ones that are (the example shows
`focus-visible + error` and `hover + filled`).

---

## 3. Filling a cell (what a treatment must name)

Each cell answers: **which anatomy part changes, to which token, with what cursor.**

- **Anatomy part** — name it from `component-anatomy.md` (container, fill, border, label, leading
  icon, caret, indicator…). "hover darkens" is not a spec; "hover: container bg →
  `--color-action-secondary-bg-hover`" is.
- **Properties** — bg, fg, border (width/color), shadow, radius (rarely), cursor, opacity.
- **Token, never literal** — `--color-…-{state}`, `--border-width-control`, `--radius-control`.
  A hex/px literal in a cell defeats theming/dark mode/rebrand (`09…/component-library-architecture`
  §5; doctrine §2). Map per-component tokens onto semantic ones.
- **Cursor** — `pointer` (operable), `not-allowed` (disabled), `wait`/default (loading), `text`
  (editable input), `default` (read-only).

---

## 4. Focus-visible — the mandatory specification (WCAG 2.2)

The single most-failed state. Spec it explicitly for every focusable component.

- **Visible & contrasted:** a real indicator (ring/outline/underline) with **≥ 3:1 contrast**
  against **both** the component and the adjacent background — **1.4.11** (non-text contrast) and
  **2.4.7** (focus visible). A 1px hairline that disappears on the brand color fails.
- **Not obscured:** the focused control is **not hidden** behind sticky headers/footers/toolbars —
  **2.4.11 Focus Not Obscured (Minimum, AA)**; aim for none-hidden (2.4.12 AAA). Add scroll-margin
  so focus scrolls fully into view.
- **`:focus` vs `:focus-visible`:** show the ring for keyboard/AT (`:focus-visible`); suppress it on
  deliberate mouse-press where it is noise — but **never** suppress it for keyboard users.
- **No naked `outline:none`:** removing the UA outline **requires** a token-driven replacement.
  This is the canonical 2.4.7 regression and is **forbidden** here.
- **Token + offset:** `--color-focus-ring`, typically 2px width + 2px offset so it reads on filled,
  ghost, and bordered variants alike. `destructive`/danger → a distinct ring (`--color-focus-ring-danger`)
  that is still ≥3:1.
- **Appears instantly:** the focus ring is **not** animated in (no slow fade) — focus feedback must
  be immediate even when other transitions animate.
- **Aim AAA where feasible:** 2.4.13 Focus Appearance (large enough, high-contrast) is the stretch.

---

## 5. Specifying transitions (the moves, not just the endpoints)

Static frames hide where fidelity is lost. For each adjacent state pair, fill a transition row:

| Column | What it pins | Example |
|---|---|---|
| **From → To** | the move | default → hover |
| **Trigger** | the event | `pointerenter` |
| **Property** | what animates | `background-color` |
| **Duration** | from a motion token | `--duration-fast` (~120–160 ms) |
| **Easing** | from a motion token | `--ease-standard` (ease-out-ish) |
| **Reduced-motion** | the `prefers-reduced-motion` path | same color change, **no** transform |

**Rules of thumb (all token-backed, never magic numbers):**
- **Hover / leave:** ~120–160 ms, ease-out in, slightly faster out. Color/opacity only — no layout
  shift, no size change that reflows neighbours.
- **Press (active):** near-instant down (~80–120 ms), a small `scale .98` or inset shadow. The
  press is the canonical **reduced-motion casualty** — keep the state, drop the transform (2.3.3).
- **Focus-in:** the ring appears **instantly** (no fade). Focus-out: instant removal.
- **Selection toggle:** the `checked`/`pressed` change may animate the indicator (~150–200 ms) but
  the semantic state flips immediately for AT.
- **loading → done / error → recovered:** specify the **return** move too — don't only design the
  forward direction. Reserve label width on `loading` so the swap causes no layout shift.
- **Easing:** UI state moves use ease-out / standard curves; avoid bouncy/elastic on controls.

Every duration/easing is a **token** (`--duration-*`, `--ease-*`), aligned with
`08-motion-and-interaction`. A bare `200ms` in a transition is the motion equivalent of a hex
literal.

---

## 6. The per-state a11y certification (run on every reachable cell)

- [ ] **Contrast holds** in hover & active, not just default (text ≥4.5:1, UI/large ≥3:1 — 1.4.3/1.4.11).
- [ ] **focus-visible** present, ≥3:1, not obscured, instant, with a token ring (2.4.7/2.4.11/1.4.11).
- [ ] **disabled** perceivable beyond color (1.4.1); decide tab/AX-tree presence deliberately.
- [ ] **loading** sets `aria-busy`, exposes a live status (4.1.3), keeps focus, blocks activation, no shift.
- [ ] **error/invalid** = color **+** text + `aria-invalid` + `aria-describedby` (1.4.1, 3.3.1).
- [ ] **selected/checked/current** exposes `aria-pressed`/`aria-checked`/`aria-selected` (4.1.2).
- [ ] **target ≥ 24×24 CSS px** in every state (2.5.8); aim 44×44 touch / 48dp.
- [ ] **name/role/value** correct per state (4.1.2); read-only ≠ disabled in the AX tree.
- [ ] **reduced-motion path** exists for every animated transition (2.3.3).
- [ ] **no empty cell** — every reachable state filled; every non-reachable one N/A + alternative.

---

## 7. Division of labour (so skills don't overlap)

- **This skill** — control-level interactive states (the nine) **and the transitions between them**.
- `09…/component-library-architecture` — the **variant/size/API** model; its state column is filled
  *by this method*.
- `04…/empty-error-and-loading-states` — **content/region** states (zero-data, 404/500, skeleton vs
  spinner, offline). This skill's `loading`/`error` cells link there for region treatment.
- `design-tokens-and-naming` — the **tokens** every cell and transition consumes.
- `08-motion-and-interaction` — the product **motion language**; transitions here pull its tokens.
