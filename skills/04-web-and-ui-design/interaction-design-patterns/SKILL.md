---
name: interaction-design-patterns
description: Use when designing interfaces, building UX flows, choosing layouts, or
  making navigation decisions. Covers Tidwell's 45+ proven interaction patterns for
  behavior, navigation, layout, actions, and data display. Load alongside webapp-gui-design...
status: active
metadata:
  portable: true
  category: 04-web-and-ui-design
  compatible_with:
  - claude-code
  - codex
---

# Interaction Design Patterns
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Choosing a navigation model — Hub & Spoke vs Flat vs Pyramid, Escape Hatch, Modal Panel, Breadcrumbs, Deep Links, Progress Indicator (`sections/02-navigation.md`).
- Structuring a page or screen — Visual Framework, Center Stage, Grid of Equals, Accordion, Collapsible Panels, Titled Sections (`sections/03-layout.md`).
- Wiring action flows — Prominent Done Button, Preview, Multi-Level Undo, Cancelability, Hover Tools, Smart Menu Items (`sections/04-actions.md`).
- Displaying dense or interactive data — Datatips, Data Spotlight, Dynamic Queries, Small Multiples, Multi-Y Graph (`sections/05-data.md`).
- Designing for real human behavior — Safe Exploration, Instant Gratification, Satisficing, Habituation, Spatial Memory, Microbreaks, Streamlined Repetition.
- Justifying *why* a pattern fits, or replacing an AI-generic layout with a behavior the user already has muscle memory for.

## Do Not Use When

- You need the visual system (color, type, spacing scales) rather than the interaction structure — use `practical-ui-design` / `premium-ui-ux-design`.
- The work is the empty/error/loading state of a single component — use `empty-error-and-loading-states` or `component-states-and-interaction-fidelity`.
- You are scoping a full site's nav tree and URL hierarchy — use `navigation-and-information-architecture`; this skill picks the *pattern*, that skill designs the *map*.
- The deliverable is animation timing and easing — use `motion-design`; this skill says *when* to give feedback, motion-design says *how* it moves.
- It is platform binding (React/Compose/SwiftUI) — pair with `webapp-gui-design`, `android-ui-ux-design`, or `ios-ui-ux-design`.

## Required Inputs

- The surface and its primary user goal — what is the ONE thing the user does first on this screen.
- Observed or assumed user behavior (expert vs first-run, repetitive vs one-off, mobile microbreak vs deep work).
- The platform target, so patterns map to real shortcuts and gestures (Ctrl-Z, swipe-to-delete, Back).
- Which companion skill carries the visual/platform layer, so this skill stays pattern-only.

## Workflow

- Start from the user behavior, not the UI: name the pattern from how people actually act (they scan and satisfice; they leave reminders; they pivot mid-task).
- Pull the matching pattern from the Quick Reference table below and load only that one `sections/` file.
- Wire each pattern as trigger to response with its full state list, and make undo/escape, data source, and save lifecycle shared across patterns on one screen (see `examples/pattern-applied-worked.md`).
- Hand off the visual and platform specifics to the paired companion skill; keep this output structural.

## Anti-Patterns

- Reaching for a novel "AI" interaction where a habituated standard (Back button, Ctrl-S, breadcrumb) would have been faster and invisible.
- Rearranging menus by usage frequency, auto-closing idle tabs, or auto-sorting user-placed items — this destroys Spatial and Prospective Memory.
- Relying on a confirmation dialog for critical protection when habituated OK-clicks bypass it; warn *before* an irreversible action instead.
- Loading all six `sections/` files at once instead of the one the task needs.

## Outputs

- A named set of interaction patterns per surface, each justified by the user behavior it serves and wired as trigger -> response with full states.
- A **Tidwell pattern usage register** when multiple surfaces or flows need a durable pattern inventory.
- Navigation/layout/action/data decisions traceable to Tidwell patterns, with the shared undo, data, and save lifecycle made explicit.
- The handoff note to the visual/platform companion skill, plus any pattern conflicts or open behavioral assumptions.

## References

- `doctrine/design-doctrine.md` — the anti-slop charter; grounding interaction choices in proven patterns is how this skill avoids the convergent AI-generic interface.
- `doctrine/references/ai-slop-taxonomy.md` — the product/interface slop tells (e.g. an AI feature where standard navigation was faster) these patterns guard against.
- Use the `sections/` directory for modular deep dives and load only the parts relevant to the task.
<!-- dual-compat-end -->
Grounded in Tidwell, Brewer & Valencia (2020) *Designing Interfaces*, 3rd ed. — the industry's definitive interaction design pattern library. These patterns describe how real humans behave with software and what interface structures consistently work.

## When to Use

Load this skill alongside any design skill when:
- Choosing a navigation model (Hub and Spoke? Flat? Pyramid?)
- Designing page layouts and information hierarchy
- Planning action flows (undo, preview, cancel, confirmation)
- Displaying complex or interactive data
- Understanding *why* users behave the way they do
- Avoiding AI-generic interfaces by grounding decisions in proven patterns

## Quick Reference

| Category | Key Patterns | Reference |
|----------|-------------|-----------|
| **Behavioral** | Safe Exploration, Instant Gratification, Satisficing, Habituation, Spatial Memory, Prospective Memory | This file |
| **Navigation** | Hub & Spoke, Escape Hatch, Modal Panel, Deep Links, Breadcrumbs, Progress Indicator, Fat Menus | `sections/02-navigation.md` |
| **Layout** | Visual Framework, Center Stage, Grid of Equals, Accordion, Collapsible Panels, Titled Sections | `sections/03-layout.md` |
| **Actions** | Prominent Done Button, Preview, Multi-Level Undo, Hover Tools, Smart Menu Items, Cancelability | `sections/04-actions.md` |
| **Data Display** | Datatips, Data Spotlight, Dynamic Queries, Small Multiples, Multi-Y Graph | `sections/05-data.md` |
| **SaaS Web Apps** | Cards vs tables, skeletons, empty states, progressive disclosure, AI UI, pagination | `sections/06-saas-web-app-patterns.md` |

---

## 1. Behavioral Design Patterns

These describe how humans naturally interact with software. Design *with* them — not against them.

### Safe Exploration
*"Let me explore without getting lost or getting into trouble."*

Users learn more and feel more positive when they can try things without dire consequences. Exploration is the primary way users discover features. Support it by:
- **Multi-Level Undo** on all reversible actions — unlimited steps, not just one
- **Escape Hatch** always present — a reliable way back to a known-safe state
- **Preview** before committing to irreversible or impactful actions
- Never trapping users in modal flows without an obvious exit
- Back button works predictably on every page — never hijack or break it

**Design rule:** If an action can't be undone, warn explicitly *before* it happens — not after.

---

### Instant Gratification
*"I want to accomplish something now, not later."*

Users must get a success experience within the first few seconds. If they can't, they lose confidence in the product and in themselves.
- Predict the user's first action and make it obviously easy — put it on the first screen
- Never block first use with registrations, tutorials, or long-loading splash screens
- Provide value *before* asking for anything in return (email, payment, sign-up)
- First-time users should complete a meaningful action within 30 seconds

**Design rule:** Every new screen — ask: "What is the ONE thing users do first, and can they see and do it immediately?"

---

### Satisficing
*"This is good enough. I'll stop here."*

Users do not read every element. They scan, pick the first option that might work, and try it. This is rational: parsing a complex interface is cognitive work they'd rather avoid.
- Use **calls to action**: explicit, directive labels — "Start here," "Create invoice," "Upload image"
- Keep all labels **short, plainly worded, and unambiguous** — users guess at meaning before reading
- Use layout, size, and color to communicate importance — these are read before text
- Provide **easy recovery** from wrong choices (Escape Hatch, Undo)
- Visual complexity causes users to pick the first *visible* thing, not the best thing

**Design rule:** If your label requires reading to understand its meaning, rewrite it until a user's first guess is correct.

---

### Changes in Midstream
*"I changed my mind about what I was doing."*

Users change goals mid-task — they start to add an invoice but spot an overdue customer and pivot. Support this gracefully.
- Keep navigation accessible — don't lock users into linear flows without good reason
- Support **reentrance**: half-completed forms save state and resume where the user left off
- Persist draft state: turning off a device or closing a tab should not lose work
- Dialogs and forms should remember previously entered values

**Design rule:** Forcing users to finish a task before doing anything else causes abandonment.

---

### Deferred Choices
*"I don't want to answer that now; just let me finish!"*

Users want to complete their primary task without being interrupted by decisions they don't need to make yet.
- Don't front-load forms with questions the user can't answer or doesn't need to answer now
- Mark **required vs optional** fields clearly — mark optional as "(optional)", not required with asterisks
- Hide long configuration lists behind "Advanced" — show only the short, required list first
- Use **Good Defaults** to pre-answer non-critical decisions (see form-ux-design skill)
- Tell users: "You can always change this later" with a link to where

**Design rule:** Every required question that isn't truly necessary reduces form completion rate.

---

### Incremental Construction
*"Let me change this. That doesn't look right; let me change it again. That's better."*

Builders — writers, designers, coders — work in small iterative cycles. They build a piece, evaluate it, adjust it, and repeat. They don't work in a straight line.
- Support **immediate feedback** after every change — show the result instantly, no wait
- Keep **save and preview cycles fast** — any delay longer than 2 seconds breaks concentration
- Show the state of the whole while the user edits a part (live preview)
- Full Undo/Redo granularity — every small change should be reversible
- Let users have multiple incomplete projects open simultaneously

**Design rule:** Any delay between action and visible result risks breaking the creative flow state.

---

### Habituation
*"That gesture works everywhere else; why doesn't it work here?"*

Frequent actions become reflex. Users stop thinking consciously about common gestures (Ctrl+S, swipe-to-delete, Back button). Breaking habituated patterns causes errors and frustration — especially for expert users.
- Use **universal keyboard shortcuts** exactly as the platform defines them — Ctrl-C, Ctrl-Z, Ctrl-S
- Never reassign a standard gesture or shortcut to a different action, even in a special mode
- Keep **menu items in the same position and order** across all pages and sessions
- Confirmation dialogs are bypassed by habituated OK/Return clicks — don't rely on them for critical protection
- On mobile: verify ALL gestures match the platform's standard behaviour

**Design rule:** Consistency within your app is as important as consistency with the platform. One inconsistent gesture erases expert confidence.

---

### Microbreaks
*"I'm waiting for the train. Let me do something useful for two minutes."*

Users access apps during short windows of available attention — queues, commutes, transitions. Design mobile features for completion in ≤2 minutes.
- App must be fast to start — no setup, no required re-login, no long loading sequences
- Show the **freshest, most relevant content on the first screen** — don't make users navigate to find value
- Support **reentrance**: restore exactly where the user left off, without asking
- Provide efficient triage: show enough data per item to act without opening it

**Design rule:** If your app takes more than 10 seconds from cold launch to primary content, it fails the microbreak test.

---

### Spatial Memory
*"I swear that button was here a minute ago. Where did it go?"*

Users find things by remembering *where* they are, not what they're named. This is powerful and fast — but only if the interface stays stable.
- Keep controls, menus, and navigation items in the **same position** across all pages and sessions
- The **first and last items** in any list are remembered more than the middle — place key items there
- Never "helpfully" rearrange menus based on usage frequency — users rely on position, not recency
- User-arranged layouts support spatial memory — respect user-defined organisation
- Changing navigation items between pages destroys the user's mental map

**Design rule:** Every time you move a UI element, you reset the user's spatial memory for it. Do this only when there's a strong reason.

---

### Prospective Memory
*"I'm putting this here to remind myself to deal with it later."*

Users leave intentional artifacts — open windows, starred items, items on the desktop — as self-made reminder systems. Software must *support*, not clean up, these systems.
- **Never auto-close** idle windows or tabs — they may be intentional reminders
- **Never auto-sort or rearrange** user-placed items unless asked
- Retain **half-finished form state** when the user navigates away and returns
- Provide bookmarking, pinning, starring, and list features for deferred items
- Show "recently visited" and "in-progress" items on return to help users pick up

**Design rule:** When you helpfully clean up after users, you erase their memory system.

---

### Streamlined Repetition
*"I have to do this how many times?"*

Power users often perform the same operation repeatedly. Reducing repetition from 10 clicks to 1 is the quality-of-life win that defines expert-grade tools.
- Provide **bulk/batch operations**: select multiple items, apply action once
- Support **Find and Replace** for repetitive text/value changes
- Enable **Macros**: users record a sequence of actions and replay it with one click
- Design keyboard-only paths for all high-frequency operations
- Offer **clipboard history** beyond just the last item

**Design rule:** Observe your power users for 30 minutes — they will reveal every repetitive task your UI fails to streamline.

---

### Social Proof
*"What did everyone else say about this?"*

People's decisions are shaped by what peers do and say. Social dynamics increase engagement, trust, and conversion.
- Show **user counts, ratings, and reviews** near conversion points
- Display **activity feeds** showing what peers have recently done
- Surface "trending," "popular," or "recommended by others like you" signals
- Build collaboration features: comments, shared views, @mentions

**Design rule:** One genuine peer review outweighs five brand marketing claims.

---

## Integration

```
interaction-design-patterns (this skill)
    |
    +-- webapp-gui-design ------> Apply patterns to React/Next.js or Bootstrap/Tabler web UI
    +-- android-ui-ux-design ---> Apply patterns to Android Compose mobile UI
    +-- ios-ui-ux-design -------> Apply patterns to iOS SwiftUI/UIKit mobile UI
    +-- practical-ui-design ----> Visual system (colour, type, spacing) for the chosen patterns
    +-- design-audit -----------> Validate pattern choices against the 10 quality dimensions
    +-- enterprise-ux-process --> Validate pattern choices with real users before building (Phase 9)
```

---

## Examples

- `examples/pattern-applied-worked.md` — one real screen (the invoice line-items editor in an SMB
  accounting SaaS) with three named patterns applied together: **Inline Edit**, **Optimistic Action**,
  and **Progressive Disclosure**. Shows how each pattern is selected from observed user behaviour, the
  trigger→response wiring and full state list for each, why each fits this screen specifically, and how
  the three share one undo/escape, one totals source, and one save lifecycle.

---

## Sources

- Tidwell, J., Brewer, C., Valencia, A. (2020). *Designing Interfaces*, 3rd ed. O'Reilly.
- Nielsen, J. (1994). Ten Usability Heuristics. Nielsen Norman Group.
- Krug, S. (2014). *Don't Make Me Think, Revisited.* New Riders.
- Csikszentmihalyi, M. (2009). *Flow: The Psychology of Optimal Experience.* Harper Row.
- Stanford Web Credibility Project (2002). Web Credibility Research. Stanford University.
