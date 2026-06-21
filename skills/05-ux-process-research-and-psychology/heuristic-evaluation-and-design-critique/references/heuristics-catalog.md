# Reference: Heuristics Catalogue — Nielsen's 10 + Tognazzini's First Principles

The shared rule-set every heuristic evaluation and design critique is walked against. Two
authorities, used together: **Nielsen's 10** are the canonical usability heuristics (broad, fast,
the spine of any inspection); **Tognazzini's First Principles** are the deeper interaction-design
laws that explain *why* and catch what the 10 leave implicit. Each entry is written to be
**scannable against a live screen**: principle → what it means → what a violation looks like →
the heuristic-satisfying fix.

**Provenance.** Jakob Nielsen & Rolf Molich's heuristic-evaluation method and Nielsen's *10
Usability Heuristics for User Interface Design* (1994, periodically refined); Bruce Tognazzini's
*First Principles of Interaction Design* (revised edition). Updated here to **2026 / WCAG 2.2**
and aligned to `doctrine/design-doctrine.md` (Mission: "the moat is looking human-made";
Anti-Slop Charter). Where a heuristic violation also matches a behavioural anti-pattern, the
`doctrine/references/interaction-anti-patterns.md` code (A1–E3) is noted — that file is the
detection checklist; this file names the principle that the match breaks. Severity for any match
is set by `severity-scoring.md`.

---

## Part A — Nielsen's 10 Usability Heuristics

### N1 — Visibility of system status
- **Means:** the system always keeps users informed about what is going on, through appropriate,
  timely feedback. Users should never wonder whether an action registered.
- **Violation looks like:** a tap with no reaction; a save with no confirmation; a long operation
  with no progress; no "you are here" on deep screens. (Maps to anti-pattern **C2 Silent System**,
  **A3 Lost-in-the-Tree**.)
- **Fix / right pattern:** immediate feedback on every action; skeleton screens over spinners for
  loads; cancellable progress for slow ops; a persistent location cue; explicit success/failure.

### N2 — Match between the system and the real world
- **Means:** speak the users' language — words, phrases, concepts familiar to them — and follow
  real-world conventions so information appears in a natural, logical order.
- **Violation looks like:** internal jargon ("create customer record"), a metaphor that fights its
  function (a trash icon that archives), an unnatural ordering. (Maps to **E2 Metaphor Mismatch**.)
- **Fix:** human language ("add customer"); metaphors that match the mental model and the result;
  natural sequencing; drop dead skeuomorphism.

### N3 — User control and freedom
- **Means:** users pick functions by mistake and need a clearly marked "emergency exit" — support
  **undo** and **redo**; let them leave any unwanted state without penalty.
- **Violation looks like:** no undo on a destructive action; a flow you cannot skip or back out of;
  hijacked system back/swipe. (Maps to **C3 Dead End**, **C4 Trap / Forced Action**.)
- **Fix:** undo (toast + a 5–10 s window, then server-confirm) on destructive actions; an exit /
  skip / back on every flow; never override OS gestures. (WCAG 2.2 3.3.4 / 3.3.6 for legal/
  financial/data actions.)

### N4 — Consistency and standards
- **Means:** users should not wonder whether different words, situations, or actions mean the same
  thing. Follow platform and industry conventions (internal **and** external consistency).
- **Violation looks like:** the same concept labelled three ways; one platform's grammar forced
  onto another (hamburger on iOS where a tab bar belongs). (Maps to **A1 Square Peg, Round Hole**.)
- **Fix:** terminology lock (call it "cart" everywhere); honour the active HIG / Material guidance;
  **unify meaning, diverge mechanism** across platforms.

### N5 — Error prevention
- **Means:** even better than good error messages is a careful design that prevents problems from
  occurring in the first place — eliminate error-prone conditions or confirm before commit.
- **Violation looks like:** an irreversible action one tap away with no guard; a form that lets you
  submit obviously invalid data; no inline validation. (Maps to **B2 Form Friction**.)
- **Fix:** constrain inputs; inline, solution-bearing validation; confirm or make destructive
  actions undoable; remove the error-prone path. (WCAG 2.2 3.3.7 redundant-entry, 3.3.8 auth.)

### N6 — Recognition rather than recall
- **Means:** minimise memory load — make objects, actions, and options **visible**; the user should
  not have to remember information from one part of the dialogue to another.
- **Violation looks like:** unlabelled icon-only nav; an action available only via a hidden gesture;
  a value you must remember and re-type. (Maps to **A2 Mystery Meat**, **A4 Hidden Gestures**.)
- **Fix:** label nav (icon **plus** text); surface options instead of hiding them; pre-fill known
  data; every hidden gesture gets a visible single-tap equivalent.

### N7 — Flexibility and efficiency of use
- **Means:** accelerators — unseen by novices — speed expert interaction, so the system serves both;
  allow tailoring of frequent actions.
- **Violation looks like:** no shortcuts/keyboard support for power users; no way to repeat or
  customise a frequent action; one path that serves neither novice nor expert.
- **Fix:** keyboard shortcuts and accelerators *alongside* the visible path; smart defaults from the
  top ~20% of journeys; let users tailor frequent actions. (WCAG 2.2 2.5.7 dragging alternatives.)

### N8 — Aesthetic and minimalist design
- **Means:** dialogues should not contain irrelevant or rarely needed information; every extra unit
  of information competes with the relevant units and diminishes their relative visibility.
- **Violation looks like:** an interrupting modal that says nothing; a wall of equal-weight buttons;
  decorative chart junk; feature-cramming. (Maps to **C1 Idiot Box**, **D6 Oceans of Buttons**,
  **D5 Chart Junk**.) Also an **anti-slop** flag: convergent decoration without purpose.
- **Fix:** non-blocking feedback (toast) over modals; prioritise — primary actions visible, the rest
  behind *More*; strip ornament to the data; one strong intentional choice over five hedged ones.

### N9 — Help users recognise, diagnose, and recover from errors
- **Means:** error messages in plain language (no codes), precisely indicating the problem, and
  constructively suggesting a solution.
- **Violation looks like:** "Error 0x0007"; "Invalid input" with no cause; a red field with no text;
  an error state with no way forward. (Maps to **C3 Dead End**, **D3 Colour-Only Signalling**.)
- **Fix:** plain-language **cause + a way out**; pair colour with icon + text; never strand the user.

### N10 — Help and documentation
- **Means:** ideally the system needs no documentation, but where help is necessary it should be
  easy to search, focused on the user's task, list concrete steps, and not be too large.
- **Violation looks like:** no help where a task is genuinely complex; help that is a wall of text,
  unsearchable, or not task-focused; inconsistent help placement. (WCAG 2.2 3.2.6 consistent help.)
- **Fix:** contextual, task-focused, searchable help with concrete steps; consistent placement.

---

## Part B — Tognazzini's First Principles of Interaction Design

Deeper laws that explain the *why* and catch what the 10 leave implicit. Walk the relevant ones
per screen; they overlap with Nielsen by design (a strong evaluation cites both).

### T1 — Anticipation
- Bring to the user everything needed at each step of the journey — anticipate wants and needs; do
  not expect users to search elsewhere for what the moment requires.
- **Violation:** the user must leave the flow to find a value the screen could have supplied.

### T2 — Autonomy
- Keep users in control: keep status visible and up to date, keep them informed, and let *them*
  make decisions. Control breeds confidence; over-automation that hides state erodes it.
- **Violation:** the system decides silently; the user cannot see or change state. (Overlaps N1.)

### T3 — Colour (use, never rely)
- Use colour to communicate, but **never rely on colour alone** — design for the ~1 in 12 men /
  1 in 200 women with colour-vision deficiency.
- **Violation:** status by colour only. (Maps to **D3 Colour-Only Signalling**; WCAG 2.2 1.4.1.)

### T4 — Consistency
- Be consistent — but Tognazzini's nuance: consistency matters most for things that **look the
  same** (they must act the same) and things that **look different** (they must act differently).
  Visible, fixed elements (navigation) should stay put.
- **Violation:** two controls look identical but behave differently; inconsistent navigation.

### T5 — Defaults
- Make defaults intelligent and easy to change; let users wipe a field with a single action. Smart
  defaults serve the common path (the top ~20% of journeys) without trapping the rest.
- **Violation:** no defaults, or defaults that serve no one and are hard to override.

### T6 — Efficiency of the user (not the machine)
- Optimise for the user's productivity, not the system's. Look at people's throughput, not the
  computer's; minimise the steps and the thinking the user must do.
- **Violation:** needless steps; the user does work the system could do. (Overlaps N7, N8.)

### T7 — Explorable interfaces & protect the user's work
- Give users well-marked roads and landmarks, then let them explore without penalty (sense of
  control). **Never lose the user's work** — at no fault of their own should data evaporate.
- **Violation:** exploration is punished (no undo / dead ends); a crash or back-button loses input.
  (Overlaps N3; maps to **C3 Dead End**.)

### T8 — Fitts's Law
- The time to acquire a target is a function of distance to and size of the target. Make clickable
  targets large and place frequent ones near where the pointer/thumb already is; screen edges and
  corners are "infinitely large" (pinned targets).
- **Violation:** tiny tap targets; the primary action far from the thumb zone. (WCAG 2.2 2.5.8
  target size ≥ 24×24 CSS px; design floor 44×44.)

### T9 — Human-interface objects & learnability
- Interface objects should be visible, have standard behaviours, and be learnable; minimise the
  *total* learning the product demands. Be conventional in the controls.
- **Violation:** a bespoke reinvented control (custom scrollbar/picker) for a job a standard widget
  does. (Maps to **E1 Novel Notions** — be creative in the UX, conventional in the controls.)

### T10 — Latency reduction
- Reduce or disguise latency; acknowledge every action within ~50 ms even if the work is not done;
  use the wait productively; multi-thread so the UI never freezes.
- **Violation:** the UI freezes during work; no acknowledgement of a tap. (Overlaps N1; maps to
  **C2 Silent System**.)

### T11 — Visible navigation (avoid getting lost)
- Keep users oriented: minimise the perception of having "gone somewhere"; provide visible, stable
  navigation and a clear sense of place. Most users do not build mental maps from invisible nav.
- **Violation:** no breadcrumbs / location cue on deep screens; navigation that disappears.
  (Maps to **A3 Deep Nesting / Lost-in-the-Tree**.)

### T12 — Readability & the rest
- Text must be legible: sufficient contrast, adequate size, and — Tognazzini's emphasis — high
  contrast for the ageing eye. (Pairs with N8 minimalism and the doctrine type rules: line length
  45–75ch, body ≥ 16px, deliberate pairing.) Also covers protecting against destructive operations
  and respecting the user's time and attention as finite resources.
- **Violation:** low-contrast or sub-16px body; cramped measure. (Maps to **D2 Typographic Noise**;
  WCAG 2.2 1.4.3 contrast.)

---

## How to use this catalogue in an evaluation

1. Walk each red-route flow twice (feel, then inspect) — see `SKILL.md` Workflow Step 2.
2. For each screen/element, test it against **all of N1–N10** and the **relevant Tx principles**.
3. Cross-check `doctrine/references/interaction-anti-patterns.md` (A1–E3); each match is a
   violation — record the heuristic it breaks (the maps above give the link).
4. For every violation, capture **location · heuristic · issue · evidence**, then rate **0–4** per
   `severity-scoring.md`. A single finding may cite **both** a Nielsen heuristic and a Tognazzini
   principle (e.g. a silent save = N1 + T2 + T10) — that is a stronger, not a redundant, finding.

*Companion to `severity-scoring.md` and `doctrine/references/interaction-anti-patterns.md`.
Principles are evergreen; sources (Nielsen 1994, Tognazzini revised) aligned to WCAG 2.2 and the
Chwezi design doctrine.*
