# Reference: Per-Component Documentation Template

The canonical spec sheet for one component. A component is **not "done" until this exists** —
undocumented variants get reinvented and the library forks. Copy this, fill every section, and
keep it beside the component. Every value referenced must be a **token** (see
`design-tokens-and-naming`), and the a11y contract must cite `doctrine/references/wcag-2.2-criteria.md`.

Filled worked example: `../examples/button-component-spec.md`.

---

## Template

````markdown
# Component: <Name>

**Atomic level:** Atom | Molecule | Organism   ·   **Status:** draft | active | deprecated
**Owns layout?** yes/no   ·   **Consumes tokens from:** <token set / semantic groups>

## 1. Purpose & when to use
One sentence: what it is for. Then:
- **Use when:** …
- **Do NOT use when:** … (name the sibling component to use instead)

## 2. Anatomy
A labelled breakdown of the parts (slots/regions). Number each part and describe it.
```
[1] container   [2] leading icon (slot)   [3] label (children)   [4] trailing icon (slot)
```
| # | Part | Required? | Slot/prop | Token(s) |
|---|------|-----------|-----------|----------|
| 1 | … | yes | — | --… |

## 3. Variant model (orthogonal axes)
List each independent axis as its own enum/boolean — never a combined string.
| Axis | Type | Values | Default | Notes |
|------|------|--------|---------|-------|
| variant | enum | … | … | |
| size | enum | … | … | |
| <modifier> | boolean | true/false | false | |

## 4. State matrix (FULL coverage — every reachable state)
Rows = states; give the token-backed treatment for each. Mark N/A only when unreachable.
| State | Trigger | bg | fg | border | other | a11y note |
|-------|---------|----|----|--------|-------|-----------|
| default | — | --… | --… | --… | | |
| hover | pointer over | --… | … | | | |
| focus-visible | kbd focus | (bg unchanged) | | | **ring** --… | ring ≥3:1 (1.4.11, 2.4.7) |
| active/pressed | pointer down | --… | | | | |
| disabled | `disabled` | --… | --… | | cursor not-allowed | not color-alone (1.4.1) |
| loading | `loading` | … | | | spinner; label hidden | `aria-busy`, live status |
| selected/checked | … | --… | | | | `aria-pressed`/`-selected` |
| error/invalid | `aria-invalid` | | | --… | error icon+text | `aria-describedby` |
| read-only | `readonly` | … | | | | distinct from disabled |

> Coverage rule: an **empty cell is a bug, not a default.** Only delete a row the component
> physically cannot enter.

## 5. API (props & slots)
| Name | Kind | Type | Default | Required | Description |
|------|------|------|---------|----------|-------------|
| variant | prop | enum | primary | no | |
| children | slot | node | — | yes | |
| onClick | prop | handler | — | no | |

**Composition:** state slots/compound usage and which parts are open-ended content.

## 6. Accessibility contract (cite WCAG 2.2)
- **Role/name/value (4.1.2):** …
- **Keyboard:** focusable; Enter/Space activate; focus order logical (2.1.1, 2.4.3).
- **Focus-visible (2.4.7, 1.4.11):** token-driven ring, ≥3:1, not obscured (2.4.11).
- **Target size (2.5.8):** ≥24×24 px hit area (aim 44×44 touch).
- **Motion (2.3.3):** transitions honour `prefers-reduced-motion`.
- **State not by color alone (1.4.1):** …

## 7. Do / Don't
| ✅ Do | ❌ Don't |
|------|---------|
| Use one `variant` enum | Use mutually-exclusive booleans |
| Token every value | Hard-code hex/px |
| Keep one primary action per view | Stack three primaries |

## 8. Tokens consumed
List the semantic tokens this component reads (so theming/dark-mode know the contract).
`--color-action-bg`, `--color-action-fg`, `--space-3`, `--radius-control`, `--duration-fast`, …

## 9. Changelog
- vX.Y — what changed and migration note.
````

---

## How to use this template

1. **Anatomy first** — naming the parts forces the slot/prop decision (`atomic-structure.md` §3).
2. **State matrix is the gate** — fill every reachable state with token values *before* writing
   any CSS; the matrix is your proof of full-state coverage.
3. **A11y contract cites criteria** — link the specific WCAG 2.2 numbers from
   `doctrine/references/wcag-2.2-criteria.md`; do not restate the rules, reference them.
4. **Tokens section is the theming contract** — `dark-mode-and-theming` and multi-brand work
   read this list to know what they must redefine. A component with literals here is broken.
