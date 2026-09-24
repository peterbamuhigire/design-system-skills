# Behaviour Patterns: Designing Around How People Actually Work

Parent skill: [interaction-design-patterns](../SKILL.md)

When to read: before choosing any navigation, layout, action or data pattern — name the human behaviour first, then pick the interface pattern that serves it.

These patterns describe what people do with software whether or not the design allows for it. Identify which behaviours the surface must support, then use the map at the end of this file to reach the structural patterns in the other sections.

Each pattern block gives: **Problem** (what goes wrong if you ignore the behaviour), **Use when**, **Do not use / caveats** (including touch and WCAG 2.2 accessibility), **How** (concrete affordances), **Example** (original) and **Pairs with**.

---

## Task A — Let people learn by trying

### Safe Exploration
- **Problem:** people build their mental model by experimenting; fear of breaking something stops learning and engagement.
- **Use when:** first-time users, unfamiliar features, complex or branching workflows.
- **Do not use / caveats:** "safe" must be real — a reversible action that silently fails on reversal is worse than a warned irreversible one. Undo and cancel controls must be keyboard reachable (WCAG 2.1.1) and at least 24×24 CSS px on touch (WCAG 2.5.8).
- **How:**
  - Provide Undo and Redo backed by an action history.
  - Allow cancel at every step of a multi-step flow.
  - Make defaults reversible; give irreversible actions deliberate friction (confirmation, typed keyword).
  - Treat Back as sacred: it must restore the prior state.
  - Preview changes before commit (live preview, draft mode).
- **Avoid:** modal dead-ends, destructive actions without warning, state lost on navigation.
- **Example:** a Kampala clinic's appointment scheduler lets the receptionist drag a slot to try a new time; the change is a draft until "Confirm reschedule", and Ctrl+Z restores the original slot.
- **Pairs with:** Multi-Level Undo, Cancelability, Preview (`04-actions.md`); Escape Hatch (`02-navigation.md`).

### Incremental Construction
- **Problem:** people who author things think by making — build a piece, look, adjust, repeat. A slow or batched feedback loop breaks concentration.
- **Use when:** documents, spreadsheets, designs, code, forms, configurations — anything the user authors.
- **Do not use / caveats:** live re-rendering on every keystroke can starve low-end Android devices; debounce rather than drop the live view. Live regions that announce every change overwhelm screen-reader users — announce on pause or on request.
- **How:**
  - Live preview, autosave, instant render.
  - Granular undo at the step level, not per save.
  - Branching history (versions, design variants).
  - Zero-friction iteration: one-click duplicate, rename and revert.
- **Avoid:** a save-only commit model in authoring tools; batched recompilation between changes.
- **Example:** a SACCO loan-product builder shows the repayment schedule updating as the officer changes rate and term; "Duplicate product" lets them try a 12-month variant beside the 6-month one.
- **Pairs with:** Preview, Multi-Level Undo, versioning.

### Instant Gratification
- **Problem:** people decide within the first few interactions whether a product is worth their time; a slow reveal kills intent.
- **Use when:** onboarding, landing pages, a new user's first session, any acquisition-sensitive surface.
- **Do not use / caveats:** do not defer steps that are legally required (KYC for a mobile-money wallet) — instead let people explore in a clearly labelled demo mode first. Sample content must be marked as sample to avoid confusion for screen-reader users who cannot see the visual "demo" styling.
- **How:**
  - Put value in the empty state: sample content, quick templates, one-click setup.
  - Defer sign-up and permission requests until the user has tasted value.
  - Make the first screen a clear "do this now", not a tour.
  - Show progress towards value visually.
- **Avoid:** multi-step onboarding wizards before anything useful, a mandatory sign-up wall, forced tutorial videos.
- **Example:** a school-fees app for Ugandan parents opens on "Check a balance" using the child's student number; creating an account is offered only after the balance is shown.
- **Pairs with:** Good Defaults, progressive disclosure, Deferred Choices.

---

## Task B — Respect how people decide

### Satisficing
- **Problem:** people pick the first option that looks acceptable, not the best one; they scan rather than analyse, because careful reading is costly (Krug's "don't make me think" argument).
- **Use when:** every list, menu, search result, dropdown, form field and decision screen.
- **Do not use / caveats:** ordering by likelihood harms people who know the exact name (a district, a bank) — keep alphabetical or type-ahead there. The cap on visible options is a heuristic, not a law of memory; test rather than cut blindly.
- **How:**
  - Order items by likelihood, not alphabet, unless the user knows the exact name.
  - Highlight a recommended default.
  - Reduce visual noise with whitespace and a clear typographic hierarchy.
  - Write labels that make the right choice obvious on first guess.
  - Keep visible menu options to about seven before grouping or searching (the common reading of Miller's figure).
- **Avoid:** long alphabetical dropdowns, unclear defaults, heavy descriptions that slow scanning.
- **Example:** a mobile-money checkout lists the payer's last-used network (MTN MoMo or Airtel Money) first and pre-selected, with "Other method" below.
- **Pairs with:** Good Defaults, recommended options (forms), Smart Menu Items.

### Deferred Choices
- **Problem:** forcing decisions without enough context causes abandonment or wrong answers that must later be fixed.
- **Use when:** onboarding, account set-up, configuration, long forms, any moment of uncertainty.
- **Do not use / caveats:** never defer a choice whose default carries legal, financial or safety risk. Do not ask again for information already given in the same process (WCAG 3.3.7 Redundant Entry).
- **How:**
  - "Skip for now" / "Do this later" with a gentle nudge to return.
  - Save drafts so work can be finished asynchronously.
  - Editable placeholder values ("Untitled project").
  - Surface deferred items as reminders.
- **Avoid:** mandatory trivial fields up front; blocking calls to action that refuse a default.
- **Example:** a chama (savings group) set-up lets the chair create the group with just a name and first contribution date; meeting rules and penalty amounts appear as "Finish set-up" cards on the dashboard.
- **Pairs with:** Good Defaults, drafts, progressive sign-up.

### Other People's Advice
- **Problem:** people trust peers more than marketing; decisions without social evidence carry more anxiety.
- **Use when:** onboarding, product pages, empty states, plan selection, social and marketplace apps.
- **Do not use / caveats:** never fabricate counts or reviews; live "people viewing now" pressure is a dark pattern. Star ratings need a text equivalent ("4.2 out of 5, 318 reviews") for assistive technology.
- **How:**
  - Show counts, ratings and reviews near decision points.
  - Peer recommendations ("members like you also chose…").
  - Genuine testimonials or expert endorsement beside the decision.
  - Aggregate activity streams where they are true and useful.
- **Avoid:** fake social proof, forced testimonials, pressure tactics.
- **Example:** a Nairobi hardware marketplace shows "Bought by 42 fundis in Kiambu this month" beside a cement brand, with reviews from verified buyers.
- **Pairs with:** Personal Recommendations, editorial curation.

### Personal Recommendations
- **Problem:** generic lists get scrolled past; relevance converts.
- **Use when:** content, shopping, search, media and learning platforms — any catalogue.
- **Do not use / caveats:** recommendations built from sensitive data (health, finances) need explicit consent; explanations must be text, not an icon alone.
- **How:**
  - Explain each recommendation ("Because you read X").
  - Offer explicit feedback: more like this, not interested.
  - Let people see and edit what drives recommendations.
  - Mix in editorial and random discovery to avoid filter bubbles.
- **Avoid:** unexplained recommendations, uncorrectable filter bubbles, signals that feel intrusive.
- **Example:** an agricultural advisory app suggests "Maize stalk-borer control — because you logged maize in Masaka" with a "Not my crop" option.
- **Pairs with:** editorial mix; collaborative filtering (a systems concern, not UI).

---

## Task C — Let people stop, switch and come back

### Changes in Midstream
- **Problem:** real tasks branch; people change goal mid-task, and linear flows that assume a fixed goal force a restart.
- **Use when:** long wizards, checkout, multi-screen flows, any sequence longer than three steps.
- **Do not use / caveats:** some sequences genuinely must be ordered (identity check before payout) — keep the order but still save state. Session timeouts must warn and allow extension (WCAG 2.2.1).
- **How:**
  - Allow editing earlier steps without losing later data.
  - Show every step, visible and clickable, in the progress display.
  - Save partial state automatically so abandoned flows resume.
  - Offer "skip this step" or "come back later" on optional steps.
- **Avoid:** one-way wizards, lost state on Back, forced completion order that the task does not need.
- **Example:** a clinic patient-registration flow lets the nurse jump from "Next of kin" back to "Contact details" to fix a phone number without re-entering the insurance card.
- **Pairs with:** Progress Indicator, Deep Links (`02-navigation.md`), Deferred Choices.

### Microbreaks
- **Problem:** much mobile use happens in 30–90-second windows — a boda-boda wait, a queue at the bank. A session that needs more than a minute of focus before it gives value loses.
- **Use when:** mobile feeds, quick utilities, notifications, inbox triage, short media.
- **Do not use / caveats:** do not compress safety-critical work (drug dosing, large payments) into glanceable shortcuts. One-hand thumb zones must still meet 24×24 px targets with spacing (WCAG 2.5.8); nothing may require a path-based gesture without a single-pointer alternative (WCAG 2.5.1).
- **How:**
  - One-hand, thumb-zone interaction on mobile.
  - Transparent save and resume — leave mid-sentence, return without loss.
  - Surface the most common short-session action first.
  - Glanceable summaries on the home screen (counts, badges, digests).
- **Avoid:** deep flows on mobile, modal dialogs that trap attention, forced focus for non-critical tasks.
- **Example:** a field-agent app opens on "3 deposits to confirm" with a one-tap Confirm per row, so an agent can clear them between customers.
- **Pairs with:** Deferred Choices, Spatial Memory, Progress Indicator.

### Prospective Memory
- **Problem:** people are poor at remembering future intentions; they leave reminders (open tabs, starred items, drafts). An interface that hides or cleans these up destroys their memory system.
- **Use when:** follow-ups, scheduled tasks, commitments, drafts, partly completed actions.
- **Do not use / caveats:** reminders sent by SMS or push need an opt-out and quiet hours; do not auto-close tabs or auto-sort user-placed items to "tidy up".
- **How:**
  - "Remind me later" on any item.
  - Put drafts, saved items and in-progress work in plain sight.
  - Show unfinished tasks on the home or dashboard.
  - Integrate with calendars and notifications for deferred actions.
- **Avoid:** a hidden drafts folder, commitments that expire silently, no way to mark "deal with this later".
- **Example:** a procurement officer flags a supplier quotation "Revisit Friday"; on Friday the dashboard shows it at the top of "Waiting on you".
- **Pairs with:** Deferred Choices, drafts, reminders.

---

## Task D — Protect skill people have already learned

### Habituation
- **Problem:** frequent actions become reflex; moving or remapping them breaks muscle memory, costs productivity and angers loyal users.
- **Use when:** redesigns, feature updates, power-user flows, keyboard shortcuts, toolbar placement.
- **Do not use / caveats:** habit is no excuse to keep an inaccessible control — fix it and announce the change. Keep repeated help in the same relative place across pages (WCAG 3.2.6) and navigation in the same order (WCAG 3.2.3).
- **How:**
  - Keep high-frequency controls in stable places across releases.
  - Preserve keyboard shortcuts; add new ones rather than remap.
  - Offer a temporary "use previous layout" toggle during large redesigns.
  - Warn users in advance when a habitual element will move.
- **Avoid:** reshuffling menus in minor releases; changing shortcuts without a preference toggle.
- **Example:** a pharmacy point-of-sale keeps F2 for "New sale" across versions; the new "Returns" command gets F7 rather than taking F2.
- **Pairs with:** Keyboard Only, Spatial Memory.

### Spatial Memory
- **Problem:** people remember where things are faster than what they are called; rearranging the interface wipes that memory.
- **Use when:** toolbars, menus, maps, dashboards, document outlines, any visually consistent interface.
- **Do not use / caveats:** stable position must survive responsive reflow — the same control should keep the same relative order on phone and desktop. Consistent identification applies to icons as well as labels (WCAG 3.2.4).
- **How:**
  - Keep toolbar positions stable across sessions and contexts.
  - Respect user-arranged layouts (sidebars, pinned items).
  - Place icons consistently across similar screens.
  - Avoid adaptive menus that reorder by usage.
- **Avoid:** most-recently-used toolbars, random insertion of new items, ribbon reorganisation between versions.
- **Example:** a SACCO teller screen keeps "Deposit", "Withdraw", "Transfer" in the same three positions on every member record, even when a member has no loan.
- **Pairs with:** Habituation, stable navigation, Visual Framework (`03-layout.md`).

### Keyboard Only
- **Problem:** people who cannot use a pointer, and experts who will not, need every action from the keyboard; assistive technology depends on it.
- **Use when:** always for accessibility; especially in power tools (data entry, email, spreadsheets, command palettes).
- **Do not use / caveats:** single-key shortcuts must be remappable or disableable (WCAG 2.1.4). Sticky headers and chat widgets must not hide the focused element (WCAG 2.4.11).
- **How:**
  - Tab order follows reading order; Shift+Tab reverses (WCAG 2.4.3).
  - Visible focus ring on every interactive element — never `outline: none` without a replacement (WCAG 2.4.7).
  - Document shortcuts and make them discoverable (Ctrl/Cmd+K palette, "?" for help).
  - Escape cancels dialogs, Enter submits forms, arrow keys move within lists.
  - No mouse-only gestures: provide alternatives to hover-only menus and drag-only reordering (WCAG 2.5.7).
- **Avoid:** mouse-exclusive drag and drop, invisible focus, custom widgets that trap focus (WCAG 2.1.2).
- **Example:** a hospital records clerk enters 60 lab results an hour using Tab between fields, Enter to save and J/K to move between patients.
- **Pairs with:** screen-reader patterns (`ux-principles-101`), keyboard conventions table (`04-actions.md`).

---

## Task E — Cut repeated effort

### Streamlined Repetition
- **Problem:** repetition magnifies small inefficiencies into frustration and errors.
- **Use when:** the same action runs many times — data entry, triage, editing, bulk file operations.
- **Do not use / caveats:** bulk destructive actions need a count in the label and an undo or preview; bulk-select checkboxes need accessible names ("Select invoice 1042").
- **How:**
  - Bulk select plus bulk action on lists.
  - Keyboard shortcuts for primary actions.
  - Templates, snippets and saved searches.
  - Macro or record-a-sequence for complex tools.
  - "Apply to all" or "Repeat for next" in dialogs.
- **Avoid:** one-at-a-time loops, no bulk path, no keyboard path for frequent operations.
- **Example:** a district health officer marks 40 facility reports "Reviewed" in one action after filtering to "Submitted this week".
- **Pairs with:** Macros, Command History (`04-actions.md`).

---

## Behaviour-to-pattern map

| Behaviour | First-line interface patterns |
|---|---|
| Safe Exploration | Multi-Level Undo, Cancelability, Preview, Escape Hatch |
| Instant Gratification | Good Defaults, fill-in-the-blanks, sample content, Progress Indicator |
| Satisficing | Good Defaults, dropdown chooser, sorted lists, Smart Menu Items |
| Changes in Midstream | Progress Indicator, Deep Links (state in URL), Deferred Choices |
| Deferred Choices | Drafts, "Later" buttons, placeholder names |
| Incremental Construction | Preview, autosave, Multi-Level Undo |
| Habituation | Stable navigation, consistent toolbar, preserved shortcuts |
| Microbreaks | Bottom navigation, glanceable summary, autosave |
| Spatial Memory | Stable toolbar, no adaptive menus, Movable Panels with persistence |
| Prospective Memory | Drafts tray, reminders, pinned items |
| Streamlined Repetition | Bulk selection, Macros, Command History, keyboard shortcuts |
| Keyboard Only | Visible focus, logical tab order, shortcuts, command palette |
| Other People's Advice | Genuine counts, testimonials, leaderboards |
| Personal Recommendations | "Because you…" explanations, feedback controls |

## Checks

1. Each surface names at least one behaviour it supports and the pattern chosen for it.
2. Nothing irreversible happens without a warning before the action.
3. Partly completed work survives closing the tab, losing signal, or a device restart.
4. No control moves between pages or releases without a stated reason.
5. Every action is reachable and visible by keyboard, with touch targets meeting WCAG 2.5.8.

## Related

- `02-navigation.md` — wayfinding, escape hatches, signposting.
- `03-layout.md` — page structure that supports scanning and satisficing.
- `04-actions.md` — reversibility, commands, undo, shortcuts.
- `05-data.md` — data displays that respect cognitive limits.
- Companion skills: `ux-psychology`, `laws-of-ux` (Miller, Hick, Fitts, Jakob), `habit-forming-products`.

Sources: pattern names follow Tidwell, Brewer & Valencia, *Designing Interfaces* (3rd ed.); Krug, *Don't Make Me Think*; W3C, WCAG 2.2.
