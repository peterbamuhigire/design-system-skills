# Reference: Atomic Structure & Composition

How to classify a component on the atomic ladder, and how to choose composition over
configuration so the API stays small and authored. Pairs with `design-tokens-and-naming`
(the values components consume) and `doctrine/references/wcag-2.2-criteria.md` (the a11y floor).

---

## 1. The atomic ladder (the only four levels you need)

Brad Frost's atomic design, pared to what a working library actually uses. The level a
component sits at **dictates its responsibilities** — get the level right and the API follows.

| Level | Definition | Owns | Must NOT own | Examples |
|---|---|---|---|---|
| **Atom** | Indivisible UI primitive. Splitting it produces nothing usable. | Its own visuals + states, bound to tokens. | Layout of *other* components; business logic; data fetching. | Button, Input, Icon, Text/Label, Avatar, Badge, Spinner, Checkbox, Radio, Switch |
| **Molecule** | A small group of atoms bonded to do **one** job. | The arrangement of its atoms + the wiring between them (label↔input association, error display). | Page layout; domain logic. | Field (Label + Input + HelpText + Error), SearchBar (Input + Button), Pagination, Breadcrumb, MenuItem, FormGroup |
| **Organism** | A self-contained, recognisable section of an interface. | Internal layout; orchestration of its molecules/atoms; local interaction state. | Routing; global app state; server calls (takes them as props/handlers). | Header/Nav, Card, DataTable, Form, Modal/Dialog, Tabs, Toast region |
| **Template / Pattern** | A page-level arrangement of organisms (structure, no real content). | Slot positions and responsive behavior. | Real data. | Dashboard layout, Settings page, Auth screen |

**Classification test (apply in order):**
1. Can it be split into smaller *independently useful* pieces? If no → **atom**.
2. Is it a few atoms wired for **one** job? → **molecule**.
3. Is it a standalone section a user would name ("the card", "the table")? → **organism**.
4. Is it a page skeleton positioning organisms? → **template**.

**The cardinal rule:** responsibility flows **down**, never up. An atom never positions a
sibling; a molecule never fetches; an organism takes its data as props. Violations are the #1
architecture smell — they're why libraries fork and why "the Button" ends up with a margin.

---

## 2. What belongs in the library (vs product code)

Put it in the library when it is **reused across ≥2 features** and **owns no domain meaning**.
Keep it in product code when it encodes a specific feature's logic.

- Library: `Button`, `Field`, `DataTable` (generic), `Modal`.
- Product: `CheckoutSubmitButton` (composes `Button` + checkout logic), `InvoiceTable`
  (composes `DataTable` + invoice columns).

Rule: the library ships **unopinionated, composable primitives**; the product composes them.
This keeps domain churn out of the system and the system's surface small.

---

## 3. Composition over configuration (the API lever)

A component's API grows two ways. One scales; one doesn't.

| Configuration (props) | Composition (slots / compound / children) |
|---|---|
| Caller passes data, component decides layout | Caller passes *structure*, component provides behavior + tokens |
| Good for **finite, orthogonal** options (variant, size) | Good for **open-ended content** and many optional parts |
| Breaks down past ~5 booleans (boolean soup) | Stays flat as parts grow |

**Switch from props to composition when** you hit any of:
- More than ~5 boolean props, OR booleans that are really mutually-exclusive states
  (`isPrimary/isSecondary` → one `variant` enum).
- The caller needs to inject **arbitrary** content (then expose a slot, not a `content` prop).
- The component has many **optional parts** (header/footer/actions) → named regions.

### Three composition mechanics

1. **`children` slot** — the default content hole. `<Button>Save</Button>`.
2. **Named regions / slots** — for several optional parts:
   `<Card><Card.Media/><Card.Body/><Card.Footer/></Card>` (React compound) or Web Components
   `<slot name="footer">`. Each region is a documented part in the anatomy.
3. **Compound components** — parent shares state with children implicitly:
   `<Tabs value><Tabs.List><Tabs.Tab/></Tabs.List><Tabs.Panel/></Tabs>`. The parent owns
   selection state; children read it. This is how you avoid passing `selectedIndex` through
   five prop layers.

### The orthogonal-axes rule (kills the mega-enum)

A component's variants are the **product of independent axes**, each its own small enum/boolean:

```
Button = intent{primary|secondary|ghost|destructive}
       × size{sm|md|lg}
       × state{default|hover|focus|active|disabled|loading|…}  (runtime, not a prop)
       × modifier{iconOnly?, fullWidth?}
```

Express axes separately (`variant`, `size`, `loading`) — **never** collapse them into one
string (`variant="primary-lg-loading"`). Orthogonal axes are type-safe, composable, and keep
the state matrix finite and reviewable.

---

## 4. Why this serves the anti-slop mission

Per `doctrine/design-doctrine.md` §0, the moat is looking **authored, not templated**. A fat
configurable component pushed to its defaults *is* the convergent mean. A small composable
primitive forces the caller to make deliberate structural choices, and lets the **one strong
authored decision** (a specific radius, a branded focus ring, a considered pressed-state) live
in tokens and propagate through every composition. Composition is the anti-slop charter applied
to API design.

---

## 5. Accessibility is structural, not cosmetic (build it into the atom)

A11y belongs at the atom level so every composition inherits it (`doctrine/references/wcag-2.2-criteria.md`):

- **Name/Role/Value (4.1.2):** every interactive atom exposes an accessible name, correct role,
  and current state. Icon-only atoms require an `aria-label`.
- **Focus-visible (2.4.7) + contrast (1.4.11):** the focus indicator is owned by the atom, token-driven,
  ≥3:1 against its background, never removed.
- **Target size (2.5.8):** the atom's minimum hit area is ≥24×24 px (aim 44×44 touch).
- **State without color alone (1.4.1):** error/selected/disabled carry a non-color cue (icon, text, shape).

Build it once in the atom and the molecule/organism get it free — the alternative (bolting a11y
on per-screen) is exactly the audit failure `accessibility-wcag-2-2-compliance` exists to catch.
