# Action Patterns: Making Commands Visible, Clear and Reversible

Parent skill: [interaction-design-patterns](../SKILL.md)

When to read: when deciding how people start, confirm, cancel or reverse an action — which control carries it, how it is labelled, and what happens if they change their mind.

An action control should look and behave like what it does: a control that looks pressable invites pressing, and a label that names the outcome removes the guess. Start from the task, choose the mechanism, then make the outcome predictable and reversible.

Each pattern block gives: **Problem**, **Use when**, **Do not use / caveats** (including touch and WCAG 2.2 accessibility), **How**, **Example** (original) and **Pairs with**.

---

## Task A — Choose how an action is reached

### Mechanism decision table

| Mechanism | Choose it for | Rule | If chosen wrongly |
|---|---|---|---|
| **Button** | Primary actions, calls to action, destructive actions | Large, obvious, always visible | A primary action styled as a link is overlooked |
| **Text link** | Navigation, secondary or inline actions | Link styling (underlined or clearly coloured) signals "goes somewhere" | Links that perform destructive actions surprise people |
| **Icon button** | Toolbars, compact repeated actions | Only widely recognised icons; accessible name plus a visible label or tooltip on hover and focus | Ambiguous icons are guessed at or ignored |
| **Hover / Pop-Up Tools** | Item-level actions in lists and tables | Reveal on hover or focus; never the only route | Touch users never see the actions |
| **Context menu (right-click, long-press)** | Expert shortcuts on objects | Supplementary only — every item must also exist elsewhere | Most people never discover the action |
| **Action Panel** | A persistent set of related actions on a complex screen | Always visible, text-labelled | Actions hidden in menus go unused |
| **Toolbar** | Frequent visual editing actions | Icon-first; suits actions with an obvious visual form | Abstract actions as icons become a guessing game |
| **Keyboard shortcut** | High-frequency actions for experienced users | Always a supplement, never the only path | Novices and pointer users are locked out |
| **Drag and drop** | "Move this here" or "apply this to that" | An enhancement; provide a click or keyboard alternative (WCAG 2.5.7) | Keyboard, switch and many touch users cannot complete the task |

**Rule:** visible actions teach; hidden actions are not discovered. An action reachable only by right-click or an unexplained gesture effectively does not exist for most users.

---

## Task B — Make the next step obvious

### Prominent Done Button
- **Problem:** when the main action does not stand out, people hesitate, choose the wrong button or abandon the form.
- **Use when:** every form, dialog, page section and wizard step.
- **Do not use / caveats:** one primary per context — a second "primary" dilutes the first. Keep the button enabled and report errors on submit; a disabled button gives no reason and is often skipped by screen readers. Target size at least 24×24 CSS px (WCAG 2.5.8), larger on phones.
- **How:**
  - Exactly one filled (solid) primary button per context.
  - Place it where the eye lands after reading: typically bottom-right of a form or dialog, or top-right of a page header; on phones, full width at the bottom within thumb reach.
  - Label it with the outcome — "Save", "Create invoice", "Send payment" — not "OK" or a generic "Submit".
  - Enter (or Ctrl+Enter in multi-line contexts) triggers it.
  - On error, keep the button active and show messages at the fields and in a summary (WCAG 3.3.1).
- **Avoid:** three equally weighted buttons side by side — people cannot tell which one moves them forward.
- **Example:** a SACCO loan-application step ends with a filled "Submit application" button; "Save draft" sits beside it as an outlined button.
- **Pairs with:** Button Groups, Smart Menu Items, Preview.

### Button Groups
- **Problem:** scattered related actions make people hunt; they learn where actions live only if the place is consistent.
- **Use when:** a set of actions applies to the same object or step (primary, secondary, destructive), or a set of filter options.
- **Do not use / caveats:** do not group destructive and safe actions tightly — distance prevents slips, especially on touch. Grouped buttons still need visible focus and a sensible tab order (WCAG 2.4.3, 2.4.7).
- **How:**
  - Group by relationship; show grouping by adjacency, a shared border or a subtle separator between groups.
  - Visual weight: primary filled, secondary outlined, destructive red (or ghost with a red hover) and never colour alone — the label carries the meaning (WCAG 1.4.1).
  - Set the destructive action physically apart from safe ones.
  - At four to five buttons, move the rest into an overflow menu or an Action Panel.
- **Example:** an invoice toolbar reads "Send" (filled), "Download PDF" (outlined), then after a gap "Void invoice" in red text.
- **Pairs with:** Prominent Done Button, Action Panel.

### Action Panel
- **Problem:** complex actions need words to be understood; icon toolbars and menus hide them.
- **Use when:** a screen has several related actions that need text labels to be clear.
- **Do not use / caveats:** on phones, a persistent side panel takes too much width — collapse it to a labelled sheet or a sticky bottom bar. Only show actions valid for the current state, and do not leave invalid ones as unexplained disabled controls.
- **How:**
  - Position it as a sidebar, a card footer or a dedicated action column.
  - Filter by state (for example, "Approve" appears only for pending items).
  - Organise into labelled groups when there are more than five actions.
  - Put the primary action first and most prominent; put the destructive action last, set apart.
- **Example:** a clinic's referral record shows a side panel: "Accept referral", "Request more information", "Print referral letter", and at the bottom "Decline referral".
- **Pairs with:** Button Groups, Smart Menu Items.

---

## Task C — Say exactly what will happen

### Smart Menu Items
- **Problem:** generic labels ("Delete", "Undo") force people to remember context or guess, and errors follow.
- **Use when:** every menu item and button whose effect depends on a selection or a prior action.
- **Do not use / caveats:** keep labels short enough to fit on phones — truncate the object name, not the verb. The visible label must be contained in the accessible name (WCAG 2.5.3).
- **How:**
  - Include the object: "Delete invoice #1042", not "Delete".
  - Undo names what it reverses: "Undo rename".
  - For batches, include the count: "Delete 3 selected items".
  - For an unavailable item, either explain why ("Cannot delete: invoice has payments") or hide it; never leave a silent disabled item.
- **Example:** after a teller reverses a deposit, the menu reads "Undo reversal of deposit UGX 250,000 — member 0381".
- **Pairs with:** Multi-Level Undo, Preview.

### Preview
- **Problem:** actions with a significant visible result cause anxiety and mistakes when people cannot see the outcome first.
- **Use when:** applying templates, sending messages, generating documents or reports, changing settings, bulk or destructive operations.
- **Do not use / caveats:** a preview that differs from the real output is worse than none. Live previews that re-render constantly can stall low-end phones — debounce them. Announce preview updates politely, not on every keystroke (WCAG 4.1.3).
- **How:**
  - Offer a "Preview" button or panel, live or on demand.
  - For generated documents (PDF, email, report), render the result in a dialog before final confirmation.
  - For settings, show a live preview beside the controls.
  - For destructive actions, summarise what will be affected: "You are about to delete 3 invoices totalling UGX 4,200,000."
- **Example:** a school bursar previews the fee-reminder SMS as it will appear on a parent's phone, with the child's name and balance filled in, before sending to 600 parents.
- **Pairs with:** Cancelability, Multi-Level Undo, Safe Exploration (`01-behavior.md`).

---

## Task D — Let people stop and reverse

### Cancelability
- **Problem:** a long operation without a way out makes people think the application has frozen; they force-quit and lose work.
- **Use when:** any operation lasting more than one to two seconds; always for long-running work such as uploads, imports, bulk operations and long calculations.
- **Do not use / caveats:** if an operation cannot be stopped partway (a committed database transaction, a payment already sent to a provider), say so before it starts, not after Cancel is pressed. Progress must be exposed to assistive technology (a `progressbar` role or a status message, WCAG 4.1.3). Time limits must be adjustable (WCAG 2.2.1).
- **How:**
  - Show Cancel as soon as the progress indicator appears.
  - Cancel must actually stop the work and roll back cleanly — not just close the indicator.
  - For sending messages, offer a short "Undo send" window (about 5–10 seconds) before dispatch.
- **Example:** importing 12,000 member records into a SACCO system shows "Importing 4,210 of 12,000 — Cancel import"; cancelling leaves no partial records.
- **Pairs with:** Progress Indicator, Preview.

### Multi-Level Undo
- **Problem:** a single undo step is not enough for iterative work; each action people cannot reverse makes them less willing to explore.
- **Use when:** editors, forms, configuration, any authoring or data-entry tool.
- **Do not use / caveats:** actions with external effects (payment sent, SMS delivered) cannot be undone locally — use Preview and confirmation instead, and say so. Provide a visible Undo control as well as the shortcut; touch users have no Ctrl+Z.
- **How:**
  - Support unlimited undo, or a practical minimum of 50 steps.
  - Ctrl+Z / Cmd+Z undoes; Ctrl+Shift+Z or Ctrl+Y redoes. Never reassign these.
  - Show the undo history as a list (for example, by pressing and holding the Undo button).
  - Label each step with a Smart Menu Item ("Undo delete customer").
  - Saving must not empty the undo stack.
- **Example:** a district planner rearranging a vaccination-outreach schedule can step back through eight moves to the version before lunch.
- **Pairs with:** Command History, Smart Menu Items, Safe Exploration.

### Command History
- **Problem:** in power tools people lose track of what they have done and cannot repeat or review it.
- **Use when:** data entry, document editing, configuration, anything needing an audit trail.
- **Do not use / caveats:** histories that record personal or financial data need access control and a retention rule. The history list must be a navigable list with text entries, not icons alone.
- **How:**
  - Show a scannable list: action, timestamp, object affected.
  - Let people select an entry to return to that state (combined with Multi-Level Undo).
  - Use it for auditing, troubleshooting and learning one's own shortcuts.
  - Keep it distinct from undo: history is informational, undo is functional.
- **Example:** a pharmacy stock screen lists "10:42 Adjusted Amoxicillin 500 mg: −20 (expired)", which a supervisor can review at close of day.
- **Pairs with:** Multi-Level Undo, Macros.

---

## Task E — Keep item actions close without clutter

### Hover / Pop-Up Tools
- **Problem:** rendering every action on every row clutters a list that people mostly scan.
- **Use when:** lists and tables with per-row actions on pointer devices.
- **Do not use / caveats:** never on touch alone — use a visible overflow ("⋯") button or a swipe action with a button alternative. Revealed tools must also appear on keyboard focus, and pop-up content must be dismissible, hoverable and persistent (WCAG 1.4.13).
- **How:**
  - Reveal Edit, View and Delete on row hover or focus.
  - Fade or slide in over roughly 100–150 ms; respect reduced-motion settings.
  - Make the same actions available through a context menu or Action Panel.
- **Example:** a patient queue shows "Call in" and "Move to triage" when the nurse hovers or tabs to a row; on the tablet, each row has a "⋯" button.
- **Pairs with:** Action Panel, Keyboard Only (`01-behavior.md`).

---

## Task F — Cut repeated work

### Macros
- **Problem:** people repeat the same multi-step sequence many times, and each repetition invites error.
- **Use when:** repetitive workflows in data tools, editors and administration screens.
- **Do not use / caveats:** a macro that runs destructive steps needs a preview and an undo point. Recording controls and playback need keyboard access and clear status.
- **How:**
  - A "Record" mode captures a named sequence; playback runs it on the current selection or context.
  - Simple forms have high value: "Find and replace all", saved filter presets, saved searches, "Duplicate with these defaults".
  - Offer scripted macros only for expert users who need them.
- **Example:** a cooperative's accounts clerk saves "Month-end: filter unpaid, sort by village, export CSV" and runs it in one step each month.
- **Pairs with:** Command History, Streamlined Repetition (`01-behavior.md`).

---

## Keyboard conventions

Every action reachable by pointer must be reachable by keyboard (WCAG 2.1.1). Tab order follows the visual reading order (WCAG 2.4.3).

| Key | Action |
|---|---|
| Tab / Shift+Tab | Move focus between controls |
| Enter / Space | Activate the focused button or checkbox |
| Escape | Close a dialog, cancel, dismiss pop-up tools |
| Arrow keys | Move within lists, menus and radio groups |
| Ctrl+Z / Cmd+Z | Undo |
| Ctrl+S / Cmd+S | Save |
| Ctrl+K / Cmd+K | Global search or command palette (common convention) |
| Ctrl+Enter | Submit a form or send a message |

---

## Anti-patterns and their consequences

| Anti-pattern | Consequence |
|---|---|
| No undo for destructive actions | People avoid acting; engagement falls |
| Generic labels ("Submit", "OK", "Yes") | People learn the effect only after clicking |
| Irreversible action without confirmation | Unrecoverable mistakes and anxiety |
| Cancel that only closes the dialog | Trust is lost; the operation continues silently |
| Long operation with no progress and no Cancel | People assume a crash and force-quit |
| Primary action with the same weight as secondary | People do not know what to do next |
| Hover-only actions on touch screens | Actions are invisible to touch users |
| Double-click as the only way to open an item | Undiscoverable; breaks keyboard access |

## Checks

1. Each screen or dialog has exactly one visually dominant, outcome-labelled primary action.
2. Every action has a visible route; shortcuts, context menus and gestures are supplements.
3. Destructive actions are set apart, previewed or confirmed, and undoable where the effect is local.
4. Any operation over two seconds shows progress and a Cancel that truly stops it.
5. Every action works by keyboard with visible focus, and every touch target is at least 24×24 CSS px.

## Related

- `01-behavior.md` — Safe Exploration, Streamlined Repetition, Keyboard Only.
- `02-navigation.md` — Escape Hatch, Progress Indicator.
- `05-data.md` — bulk actions on tables, Overview + Detail.

Sources: pattern names follow Tidwell, Brewer & Valencia, *Designing Interfaces* (3rd ed.); Norman, *The Design of Everyday Things* (affordance); W3C, WCAG 2.2.
