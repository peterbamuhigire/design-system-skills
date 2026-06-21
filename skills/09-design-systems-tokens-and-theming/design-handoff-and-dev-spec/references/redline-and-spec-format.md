# Reference: Redline & Spec Format — Token-Referenced Redlines and Testable Acceptance Criteria

How to *write* a handoff so it is buildable and signable. Two halves: (1) the redline/annotation
format, and (2) acceptance criteria that are binary and testable. Provenance: Figma Dev Mode,
redline-annotation conventions (Zeplin/Specify/Spectrum specs), Gherkin / Given-When-Then
acceptance criteria, and the Chwezi doctrine (`doctrine/design-doctrine.md`).

---

## Part 1 — The redline format

### Rule 1: reference tokens, show values only in parentheses

A redline is a set of **token references**, never raw values. The resolved value may appear in
parentheses as a build-time sanity check, but the *authority* is the token name — when the token
moves, the build moves with it.

| ✅ Token-referenced (correct) | ❌ Raw value (forks the system) |
|---|---|
| `padding: space.inset.md (→16px)` | `padding: 16px` |
| `fill: color.action.primary.bg` | `fill: #3B5BDB` |
| `text: text.body.md` | `font: 14px/20px, 400` |
| `radius: radius.200 (→8px)` | `border-radius: 8px` |
| `shadow: elevation.raised` | `box-shadow: 0 2px 8px rgba(0,0,0,.12)` |
| `motion: motion.duration.fast + motion.ease.standard` | `transition: 150ms ease` |

If a needed value has **no token**, that is a finding for `09-…/design-tokens-and-naming`, not a
licence to hardcode. Flag it; don't paper over it.

### Rule 2: spec the box model, not just the looks

Per element, in this order: **role → size → spacing → layout → type → colour → radius/border →
elevation → icon**. Always give *behaviour*, not just a number:

```
Element: Submit button (Button / primary / md @ lib v2.3)
  size:    height = hug (→40px via component); width = fill container, min 96px
  spacing: inset = space.inset.md (→16px) horizontal, component default vertical
           gap-to-sibling = space.inline.sm (→8px)
  layout:  parent = inline flex, justify=end, align=center, wrap=no
  type:    text.label.md (component-owned)
  colour:  bg color.action.primary.bg; fg color.text.on-action; (states below)
  radius:  radius.200 (→8px)   elevation: none at rest
```

### Rule 3: states as deltas from default

Don't re-spec the whole element per state. State the **delta** in tokens:

```
hover:    bg → color.action.primary.bg.hover
active:   bg → color.action.primary.bg.active
focus:    + 2px color.border.focus ring, offset space.50 (→2px); ≥3:1 vs surface
disabled: bg → color.action.disabled.bg; fg → color.text.disabled; cursor not-allowed; no hover
loading:  fg → spinner (icon.spinner, color.text.on-action); label hidden; control aria-busy=true; not clickable
```

### Rule 4: annotate behaviour, motion, and a11y on the same sheet

- **Behaviour:** action, validation rule + timing, async path, success/error outcome, focus move.
- **Motion:** duration token + easing token + trigger + meaning + **reduced-motion fallback**.
- **A11y (inline):** element/role, accessible name + source, focus order, keyboard map,
  live-region, target size (≥24px, WCAG 2.5.8), non-colour signalling
  (`doctrine/references/wcag-2.2-criteria.md`).

---

## Part 2 — Acceptance criteria (the merge gate)

### The test: could a reviewer mark this pass/fail with no opinion?

If yes, it's a criterion. If it needs interpretation, it's a wish. Every criterion is **binary**
and **token-specific**.

| ❌ Not a criterion | ✅ Acceptance criterion |
|---|---|
| "Matches the Figma." | "Resting bg = `color.action.primary.bg`; hover bg = `…bg.hover`." |
| "Button looks right." | "Height 40px; horizontal inset = `space.inset.md` (16px); radius `radius.200`." |
| "Accessible." | "Focus-visible: 2px `border.focus` ring, 2px offset, ≥3:1 vs adjacent surface." |
| "Responsive." | "At ≤containerSm the two actions stack vertically, gap `space.stack.sm`." |
| "Handles errors." | "On invalid submit, field border = `border.error`, message in `aria-live=polite`." |
| "Animates nicely." | "Enter: 150ms `motion.ease.standard`, opacity 0→1 + 4px rise; none under reduced-motion." |

### Recommended shapes

- **Token assertion:** `<element>.<property>` uses `<token>` in `<state/theme>`.
- **Behaviour (Given/When/Then):** *Given* the form is invalid, *When* the user clicks Submit,
  *Then* Submit stays disabled and the first invalid field receives focus.
- **Responsive:** At `<breakpoint/container>`, `<element>` does `<reflow/stack/hide/step>`.
- **A11y:** `<control>` is reachable by keyboard, has accessible name `<source>`, target ≥24px.

### Grouping

Group criteria as: **Visual (tokens) · States · Responsive · Behaviour · Motion · Accessibility.**
The fidelity review (Workflow step 9) walks this list against the build and logs each delta:

```
| # | Criterion | Expected (token/behaviour) | Actual | Status | Triage |
|---|-----------|----------------------------|--------|--------|--------|
| 4 | Focus ring | 2px border.focus, 2px offset, ≥3:1 | 1px, no offset | FAIL | blocker |
```

Triage = **blocker** (fails spec, must fix) / **polish** (minor, can follow up) /
**accept-with-note** (deliberate deviation, recorded). Parity is measured against *this list*, not a
fresh re-read of the design — which is why the list is written before the build starts.
