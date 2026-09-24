# Interaction Principles, Consistency and Recoverability

Parent skill: [`../SKILL.md`](../SKILL.md) (`interaction-design-patterns`).

**When to read:** when choosing how much of an interface to expose, when deciding whether to break
a convention, when designing destructive actions and multi-step tasks, and when porting desktop
patterns to touch. Paraphrased from: Scott, B. and Neil, T. (2009) *Designing Web Interfaces*,
O'Reilly; Neil, T. (2014) *Mobile Design Pattern Gallery*, 2nd edn, O'Reilly; Cao, J., Zieba,
K., Stryjewski, S. and Ellis, M. (2015) *Web UI Design for the Human Eye*, UXPin; Grant, W.
(2018) *101 UX Principles*, Packt. Book-era mechanisms (hover-first tools, Flash, 2014 platform
chrome) are deliberately not adopted.

---

## 1. Six rich-interaction principles (reframed for current platforms)

| Principle | Current meaning | Caveat |
|---|---|---|
| Make it direct | Let people act where they see the content (inline edit, direct selection) | Inline edit needs a clear edit affordance and keyboard path |
| Keep it lightweight | Reduce interaction cost with contextual tools and progressive disclosure | Never hide a primary action behind disclosure |
| Minimise context loss | Keep people in place (overlays, inlays, in-page steps) where a new page would break flow | On phones prefer bottom sheets or inline content to heavy modals |
| Provide an invitation | Signal what is possible (empty-state prompts, visible affordances, just-in-time hints) | **Hover invitations do not exist on touch; make the cue always visible or tap-based** |
| Use transitions | Animate to explain change (expand, move, fade) | Purposeful only; no bounce; honour reduced motion (`motion-design`) |
| React immediately | Acknowledge every action at once (live preview, autocomplete, optimistic update) | Debounce live search; show progress for long work |

**Hover warning:** hover-reveal tools, hover invitations, right-click menus and cursor changes
have no touch equivalent. Any desktop pattern that relies on them must be inverted for touch:
always-visible controls, explicit tap or long-press, with the same action reachable by keyboard.
Drag and drop is a specialised interaction (reorder, Kanban, upload), not a default mover, and
always needs a non-drag alternative.

## 2. Three layers of consistency (audit lens)

- **External consistency** - matches conventions users bring from other products (cart icon,
  logo returning home). Borrowing established signifiers reduces what you must explain.
- **Internal consistency** - your own pages and screens behave and look alike.
- **Tactical consistency** - pixel-level rules held everywhere (every H1 treated identically,
  logo always in the same place).

Rule: a deliberate inconsistency is powerful only on top of established consistency. In an audit,
ask of every inconsistency: earned and intentional, or drift? This pairs with the doctrine's
"restraint plus one strong choice": consistency is the floor, the authored choice is the ceiling.

## 3. Pattern classes

| Class | What it is | Example |
|---|---|---|
| Tactical | Near-universal rules with little context dependence | Checkboxes square, radios round; label above field |
| Strategic | "How" choices that depend on users and context | Sticky versus jump-to navigation; wizard versus single page |
| Site-specific | Patterns a domain's users expect | Agency site shows work; airline site leads with a booking form |

## 4. Obvious, easy, possible

Sort features by how often and how many people use them:
- **Obvious** - core, frequent tasks for most users: always visible on the main surface.
- **Easy** - frequent for some users: one step away (secondary toolbar, menu, tab).
- **Possible** - rare or advanced: tucked away but discoverable (settings, "more", search).

Use analytics or research to place each feature; do not let internal politics promote rare
features to "obvious".

## 5. Defaults that serve most journeys

Identify the top journeys (roughly the most-used fifth of paths in analytics or research) and set
defaults that serve them; offer an easy switch for the rest ("Not your first account? Change").

## 6. Recoverability

- Destructive actions: act, then show a toast with an **Undo** link for a short window (commonly
  about 5-10 seconds), then commit on the server. Use explicit confirmation only when undo is
  impossible (payments, legal submissions, permanent deletion of shared data).
- Auto-save non-destructive edits; show unsaved state visibly.
- Never clear a user's input on error.
- Pair with `empty-error-and-loading-states` for the state matrix.

## 7. Journey signposting

- Every task has a visible beginning, middle and end: step indicators, landmarks, breadcrumbs
  where hierarchy exists.
- **Explicit completion messages** ("Saved", "Sent to Amina", "Payment received - receipt
  sent by SMS") so people know the task is finished.
- Preserve context and entered data when people go back.

## 8. Mobile navigation vocabulary (for pattern discussions)

Persistent: tab bar (about five items plus More), list menu, cards, dashboard, gallery, springboard
(grid of launch icons). Transient: side drawer (overlay or inlay), toggle menu. Secondary: page
swiping with position dots, scrolling tabs, accordion. Current platform specifics (iOS, Android)
live in `ios-ui-ux-design` and `android-ui-ux-design`; skeuomorphic navigation is dated.

The eight mobile anti-patterns (novel controls, needless gesture complexity, metaphor mismatch,
interrupting dialogs, chart junk, oceans of buttons, one platform's UI forced onto another, forced
sign-up) are catalogued in `doctrine/references/interaction-anti-patterns.md`.
