# Navigation Patterns: Helping People Move, Orient and Return

Parent skill: [interaction-design-patterns](../SKILL.md)

When to read: when choosing how people move between areas of a product, how they know where they are, and how they get back to safety.

Principle: keep navigation distances short. Every page transition carries a reorientation cost, so design each task to need as few transitions as possible.

---

## Task A — Choose the overall map first

This is an architectural decision, made before any visual navigation design.

| Model | Structure | Use when | Wrong-choice consequence |
|---|---|---|---|
| **Hub and Spoke** | Central home leading to separate workspaces | Mobile apps, self-contained task areas, wizard launchers | People who need to cross between spokes bounce through home repeatedly |
| **Fully Connected** | Every section reachable from every other | Small products where cross-navigation is common | In a large product the menu becomes unmanageable |
| **Multilevel / Tree** | Parent → child sections | Large content sites, enterprise apps with many modules | Without breadcrumbs, people lose their place below level two |
| **Step-by-Step** | Linear A → B → C | Checkout, registration, onboarding | Used for non-linear work, it blocks Changes in Midstream |
| **Flat** | Three to five top-level sections, no nesting | Simple apps, mobile apps, tools with few areas | Forced onto a deep catalogue, sections become overloaded |
| **Pyramid** | Home → category → item → detail, with sideways next/previous | E-commerce, document libraries, content sites | Without sideways links, people pogo up and down |

**Decision rule:** frequent jumps between unrelated areas → Fully Connected. Self-contained tasks → Hub and Spoke. Deeply categorised content → Tree. Onboarding or a regulated sequence → Step-by-Step.

**Example:** a Kampala clinic system uses Hub and Spoke on the nurse's tablet (Triage, Vitals, Queue) but a Tree for the administrator's desktop (Settings → Departments → Wards → Beds).

---

## Task B — Help people find their place

### Wayfinding fundamentals
- **Signage:** a label at every decision point that predicts its destination. Weak information scent ("Data" instead of "Order history") makes people abandon a path.
- **Environmental clues:** learned conventions — logo top-left (top-right in right-to-left scripts), close top-right, account avatar top-right. Breaking them forces people to stop and reorient.
- **Maps:** Progress Indicators, Breadcrumbs and site maps show where the current page sits in the whole.
- **Accessibility:** mark the current location programmatically (`aria-current="page"`), keep navigation in the same order on every page (WCAG 3.2.3), and provide more than one way to reach a page (WCAG 2.4.5).

### Breadcrumbs
- **Problem:** in deep hierarchies people lose track of where they are and how to go up.
- **Use when:** hierarchies deeper than two levels.
- **Do not use / caveats:** breadcrumbs show structure, not click history — history-style trails mislead about the product's shape. On narrow screens collapse the middle segments ("Home › … › Invoice 1042") or show only the parent link; keep each link a usable touch target (WCAG 2.5.8).
- **How:** every segment except the last is a link; the last (current page) is plain text with `aria-current`; one consistent separator (›, / or >); place at the top of the content, below the main navigation; wrap in a `nav` landmark labelled "Breadcrumb".
- **Example:** Home › Members › Kato Joseph › Loan 2026-114 in a SACCO back office.

### Progress Indicator
- **Problem:** in a multi-step process people abandon when they cannot tell how far they have to go.
- **Use when:** wizards, checkout, onboarding, any multi-step task.
- **Do not use / caveats:** avoid percentages for wizard steps — "Step 2 of 4" is clearer than "50%". More than six steps overwhelms; group into phases. Twelve or more visible steps signals "too long" and drives abandonment. State must not be conveyed by colour alone (WCAG 1.4.1) — use a tick, text or shape as well.
- **How:** show number and label ("Step 2 of 4: Payment"); mark completed steps (tick, filled circle); mark the current step as active; show future steps as pending (hollow, muted); place at the top of the step content, not in a sidebar.
- **Example:** a national-ID-linked SIM registration flow: Step 1 of 3 ID details, Step 2 of 3 Photo, Step 3 of 3 Confirm.

### Annotated Scroll Bar
- **Problem:** in very long content people cannot tell where the relevant parts are.
- **Use when:** content longer than roughly 2,000 px where people need to jump to specific places — heading markers, search matches, errors, bookmarks.
- **Do not use / caveats:** markers on the scroll track are invisible to screen readers and tiny on touch; always pair them with a heading list or "Next match / Next error" buttons.
- **How:** heading markers for navigation-heavy documents; search-hit positions on the track; error locations in long forms, with focus moved to the first error on submit.
- **Example:** a 90-field land-title application marks its three validation errors on the scroll track and offers "Go to first error".

---

## Task C — Help people start

### Clear Entry Points
- **Problem:** several equal-weight options on a starting screen make people freeze or satisfice on the wrong one.
- **Use when:** home screens, dashboards, empty states, first-run screens.
- **Do not use / caveats:** a single dominant action must not hide other essential tasks from screen-reader users — keep a logical heading structure so every entry is findable.
- **How:** one dominant visual entry point per starting screen; supporting entries clearly secondary; outcome labels ("Create your first invoice", not "Get started"); for returning users, show where they left off (recent and in-progress items).
- **Avoid:** five equally sized cards or buttons on the home screen.
- **Example:** a mobile-money merchant app opens on a large "Receive payment" button, with "Statements" and "Withdraw" as smaller secondary actions.

### Fat Menus
- **Problem:** in sites with many sections, a plain dropdown hides options and forces repeated hunting.
- **Use when:** products with many sections that people browse.
- **Do not use / caveats:** not for products with fewer than about seven sections, nor where touch is primary — hover-opened panels are touch-hostile. Panels that open on hover must be dismissible, hoverable and persistent (WCAG 1.4.13) and open on keyboard focus or Enter.
- **How:** group options under section headers; show roughly 10–30 options at most; add short descriptions or icons for scent; highlight the most important options; keep the style consistent with the rest of the navigation.
- **Example:** a university portal's "Students" menu groups Admissions, Fees, Timetables and Results with one-line descriptions.

---

## Task D — Get people out safely

### Escape Hatch
- **Problem:** people who feel lost or trapped abandon the task.
- **Use when:** everywhere — every page, wizard and modal chain.
- **Do not use / caveats:** Cancel in a flow that has already committed data must say what will and will not be undone. Keyboard focus must never be trapped (WCAG 2.1.2).
- **How:** a link to Home or the dashboard on every page; breadcrumbs as intermediate exits; Back works predictably on every page; wizards have a visible Cancel returning to the previous state; deep modal chains offer a way to collapse all the way back.
- **Rule:** if Back does nothing, or something unexpected, the escape hatch is broken.
- **Example:** in a fuel-card top-up flow, "Cancel top-up" returns the fleet manager to the vehicle list with nothing charged.

### Modal Panel
- **Problem:** some sub-tasks need exclusive focus, but modals used carelessly block reference material and trap people.
- **Use when:** confirmations, critical data entry, previews, short focused sub-tasks.
- **Do not use / caveats:** not for information people must read while continuing — use an inline message or toast instead. On phones a full-screen sheet is acceptable; on desktop leave context visible around the panel. Move focus into the modal on open, contain Tab within it, return focus to the trigger on close, and give it an accessible name.
- **How:** an obvious close control (top-right ×, Escape, Cancel); Escape always dismisses; Tab cycles through the modal's controls.
- **Example:** "Reverse this transaction?" in a SACCO teller screen, showing member, amount and reason field, with Cancel and "Reverse UGX 250,000".

---

## Task E — Let people return and share

### Deep Links
- **Problem:** people share and bookmark views; if the address changes on every load, they cannot.
- **Use when:** every meaningful view — records, filtered lists, dashboards, tabs.
- **Do not use / caveats:** never place personal or clinical data in the URL; share identifiers, not contents. Links sent by SMS or WhatsApp must survive login.
- **How:** readable, stable URL structures (not raw UUIDs as slugs where avoidable); reflect filters, search queries and sort order in the URL; a shared link restores the full view state, not just the page; authenticated pages send the recipient through login and then to the intended page.
- **Example:** a district education officer shares `/schools?district=gulu&status=late-returns` with head teachers.

---

## Task F — Explain movement

### Animated Transition
- **Problem:** abrupt view changes leave people unsure how the new view relates to the old.
- **Use when:** modals sliding up, panels expanding, list-to-detail transitions.
- **Do not use / caveats:** never animate to mask slow loading; respect `prefers-reduced-motion` and avoid large motion for people with vestibular disorders (WCAG 2.3.3). If you cannot say what the animation tells people about position, remove it.
- **How:** 150–300 ms; eased (ease-in-out or deceleration), never linear; direction reinforces the model (slide in from the right = deeper, to the right = back).
- **Example:** tapping a patient in the ward list slides the record in from the right; Back slides it away.
- **Pairs with:** `motion-design` skill for easing and timing detail.

---

## Navigation failures to test for

| Failure | Consequence |
|---|---|
| No visible current-location indicator | People cannot tell where they are and navigate inefficiently |
| Navigation items that move between pages | Spatial memory is destroyed; people re-locate controls constantly |
| Primary navigation hidden behind a menu icon on desktop | Navigation that needs a click to reveal goes unused |
| Icon-only primary navigation | Icons are not universally understood; pair with text on desktop |
| Links opening new tabs without warning | People lose context and Back stops working |
| Modals with no escape | Anxiety and abandonment |
| Nesting deeper than three levels without breadcrumbs | People lose their place and stop exploring |

## Checks

1. The navigation model is named and justified against the decision rule.
2. Every page has an escape route to a known safe place, and Back behaves predictably.
3. Every meaningful view has a shareable URL that restores its state.
4. Current location is shown visually and via `aria-current`.
5. Hover-opened menus and modals pass keyboard and focus tests (WCAG 1.4.13, 2.1.2, 2.4.11).

Sources: pattern names follow Tidwell, Brewer & Valencia, *Designing Interfaces* (3rd ed.); W3C, WCAG 2.2.
