# Reference: Interaction & UX Anti-Patterns (the detection checklist)

This is a **catalogue**, not a skill — a flat, checkable list of interaction and UX anti-patterns
to **detect and avoid**. Where `ai-slop-taxonomy.md` covers the *machine-generated* tells (visual
slop, feature-cramming), this covers the *human-authored-but-wrong* tells: the failures a competent
team still ships when it copies a dead idiom, hides the affordance, or interrupts the user for
nothing. Both are gates; this one is the behavioural half.

**Provenance.** Distilled from Theresa Neil's *Mobile Design Pattern Gallery* (2nd ed., 2014) —
her eight-item Anti-Patterns chapter — and Lisandra Maioli's *Fixing Bad UX Designs* (2018)
by-domain bad-UX taxonomy, **updated to 2026**: dead-platform specifics dropped, the timeless
patterns kept, every entry aligned to WCAG 2.2 and the Chwezi design doctrine (Mission: "the moat
is looking human-made"; Anti-Slop Charter: every choice deliberate, never a reflexive default).

**Who cites this.** The group-00 audits — `design-audit`, `product-design-audit`, and
`design-qa-and-pre-launch-review` — and the planned `ux-remediation-and-redesign` skill use this
file as their **interaction-detection checklist**. Each entry is written to be scannable against a
live UI: *name → what it looks like → why it's bad → the fix / right pattern.*

How to use: walk a screen or flow against each group. Any match is a finding. Severity is set by
the citing skill's own triage (red-route / difficulty / persistence) — this file only **detects**.

---

## A. Navigation & information architecture

### A1 — Square Peg, Round Hole
- **Looks like:** one platform's UI grammar forced onto another — a hamburger drawer cloned onto
  iOS where a tab bar belongs, Android's back semantics ignored, web breakpoints shoved into a
  native app, a desktop mega-menu transplanted to touch.
- **Why it's bad:** breaks platform muscle memory and conventions; users feel the app is "foreign"
  and mistrust it. Divergence between platforms has only widened (Liquid Glass vs Material 3),
  so the cost is rising, not falling.
- **Fix:** **Unify meaning, diverge mechanism** — keep the same conceptual model across platforms,
  but express it with each platform's native control. Honour the active HIG / Material guidance.

### A2 — Mystery Meat Navigation
- **Looks like:** unlabelled icon-only nav, gesture-only routes with no signifier, destinations
  whose names don't say where they go ("Discover", "More", "Hub").
- **Why it's bad:** users can't predict the result of a tap; findability collapses. Icon-only
  comprehension is ~60% vs ~88% with a text label.
- **Fix:** label the nav (icon **plus** text); use plain, mental-model-matching nomenclature; never
  make a primary route gesture-only. Provide visible signifiers for any gesture.

### A3 — Deep Nesting / Lost-in-the-Tree
- **Looks like:** four-plus taps to reach a common task, categories that don't match how users
  think, no breadcrumbs, no global "where am I."
- **Why it's bad:** every extra level sheds users; people can't form a map of the product.
- **Fix:** flatten the IA (validate with **tree testing** / card sorting); surface red-route tasks
  near the top; add breadcrumbs or a persistent location cue on deep screens.

### A4 — Needless Complexity (overloaded / hidden gestures)
- **Looks like:** a long-press, multi-finger, or custom swipe is the *only* way to do something
  important; controls overloaded with secondary meanings.
- **Why it's bad:** undiscoverable; fails keyboard and assistive-tech users (WCAG 2.2 **2.5.1
  Pointer Gestures**, **2.5.7 Dragging Movements** — a single-pointer alternative is required).
- **Fix:** every hidden gesture must have a **visible, single-tap equivalent**. Gestures are an
  accelerator, never the sole path.

---

## B. Sign-up, forms & conversion

### B1 — Forced Sign-Up (the wall before the value)
- **Looks like:** a registration/login wall that blocks the app's value before the user has seen
  any of it; "create an account to continue" on first launch.
- **Why it's bad:** "a long sign-up form = a deleted app." It is the single highest install-killer
  Neil documents; it asks for commitment before delivering worth.
- **Fix:** **value before auth** — let users try/browse first; gate only the action that genuinely
  needs identity. Offer guest mode, defer registration, support passkeys / OAuth, and ask for the
  minimum. Personalise *after* the user is in, not before.

### B2 — Form Friction
- **Looks like:** too many fields, fields in an illogical order, no autocomplete, no inline
  validation, no progress indicator on multi-step, asking for data you could infer or look up.
- **Why it's bad:** each unnecessary field measurably depresses completion; late "your password is
  invalid" errors waste effort and erode trust.
- **Fix:** cut to the minimum field set; logical order; **inline, solution-bearing validation**;
  autocomplete and correct input types/keyboards; show progress on wizards; labels **above** fields;
  honour autofill. Express checkout / guest checkout where money is involved.

### B3 — Vague CTAs
- **Looks like:** buttons that don't say what happens — "See Details", "Go", "Submit", "Click here"
  — or several competing primary buttons of equal weight.
- **Why it's bad:** the user can't predict the outcome and hesitates; competing CTAs destroy
  hierarchy and the conversion path.
- **Fix:** verb-led, outcome-naming labels ("Start free trial", "Send invite"); exactly **one**
  primary action per view, with secondaries visibly de-emphasised.

---

## C. Feedback, status & control

### C1 — Idiot Boxes (interrupting modals that say nothing)
- **Looks like:** a modal dialog that fires for a trivial event, confirms the obvious, or just
  reports "Done" — blocking the user to demand an "OK" for no decision.
- **Why it's bad:** modal interruption has a high attention cost; it stops flow to extract a tap
  that carries no information.
- **Fix:** prefer **non-blocking** feedback — a toast (auto-dismiss ≤5s), an inline status, a count
  update, a brief animation of the action itself. Reserve modals for genuine, destructive, or
  irreversible decisions.

### C2 — Silent System (no feedback)
- **Looks like:** a tap with no visible reaction; a save with no confirmation; a long operation
  with no progress; the user can't tell if anything happened.
- **Why it's bad:** unresponsiveness reads as broken; users re-tap, double-submit, or abandon.
- **Fix:** **React immediately** — every action gets immediate feedback. Optimistic UI for fast
  ops; **skeleton screens over spinners** ("avoid the spinner") for loads; **cancellable** progress
  for anything slow; explicit success/failure state.

### C3 — Dead End (no recovery, no undo)
- **Looks like:** an error state with no way forward; a destructive action with no undo; an empty
  state that just says "Nothing here" with no next step.
- **Why it's bad:** strands the user; turns a recoverable slip into a lost task or lost data.
- **Fix:** every error carries a **plain-language cause + a way out**; destructive actions get
  **undo** (or confirm) per WCAG 2.2 **3.3.4 / 3.3.6** for legal/financial/data actions; empty
  states offer a clear first action (the "blank-slate invitation").

### C4 — Trap / Forced Action
- **Looks like:** can't dismiss a dialog, can't skip onboarding, can't escape a flow; system gestures
  hijacked so the OS back/swipe stops working.
- **Why it's bad:** removes user agency; feels coercive; collides with platform navigation.
- **Fix:** always provide an exit / skip / back; never override system gestures; let users leave any
  flow without penalty.

---

## D. Content, hierarchy & legibility

### D1 — Flat Hierarchy (size/weight not matching importance)
- **Looks like:** the least-important element is the largest (logo bigger than the answer); the key
  datum is the same weight as its caption; reading order fights the F/Z scan pattern.
- **Why it's bad:** forces the user to *think* to find what matters; under stress they can't parse it
  at all (the canonical 2017 Oscars "La La Land" card failure).
- **Fix:** **re-order by criticality** — most important element largest/first; supporting detail
  smaller; chrome de-emphasised. Size, weight, and position must encode importance.

### D2 — Typographic Noise
- **Looks like:** more than ~3 typefaces, body text < 14px / 12pt, line length outside ~45–75
  characters, cramped line-height, inconsistent emphasis, serif body set badly on screen.
- **Why it's bad:** kills readability and signals an unconsidered system (and an anti-slop concern —
  drift toward generic, unpaired defaults).
- **Fix:** a disciplined scale and **a deliberate pairing** (per doctrine), 45–75ch measure,
  line-height ≥1.4 body, consistent emphasis tokens, screen-appropriate faces.

### D3 — Colour-Only Signalling
- **Looks like:** status, validity, or required-ness conveyed by colour alone (red = error, green =
  ok) with no icon, label, or shape backup; decorative non-strategic colour.
- **Why it's bad:** invisible to colour-blind and low-vision users; **WCAG 2.2 1.4.1 Use of Colour**
  failure.
- **Fix:** pair colour with a second channel (icon, text, pattern); meet contrast floors (4.5:1 body,
  3:1 large/UI); use colour-coding consistently and strategically.

### D4 — Icon Soup
- **Looks like:** unlabelled non-standard icons, a mixed-style icon set, more than 7±2 icons in one
  group, purely decorative icon load.
- **Why it's bad:** ~60% vs ~88% comprehension without labels; inconsistent sets read as amateur;
  overload defeats scanning.
- **Fix:** label non-obvious icons; one consistent icon family; cap a group near 7±2; drop decorative
  icons that carry no meaning.

### D5 — Chart Junk
- **Looks like:** 3D pies, gratuitous gridlines, drop-shadows and gradients on data, decoration that
  distorts the value.
- **Why it's bad:** ornament misleads or hides the signal; data-ink wasted on noise.
- **Fix:** strip to the data; flat, honest encodings; sparklines/clean bars; legend integrated, scale
  truthful.

### D6 — Oceans of Buttons
- **Looks like:** every possible action exposed at once as a wall of equal-weight controls.
- **Why it's bad:** no prioritisation; the primary action drowns; cognitive overload.
- **Fix:** prioritise — a small set of primary actions on the toolbar, the rest behind **More** /
  overflow; bulk/contextual actions revealed in context.

---

## E. Novelty, metaphor & platform fit

### E1 — Novel Notions (creative at the control level)
- **Looks like:** reinventing a standard control — a bespoke scrollbar, a custom-physics picker, a
  "clever" new gesture for a job a standard widget already does.
- **Why it's bad:** novelty belongs in the *experience and flow*, not in the *controls*; a surprising
  control just makes users relearn the basics and fail.
- **Fix:** **be creative in the UX, conventional in the controls.** Use the platform's standard
  components; spend the inventiveness budget on the journey, not the scrollbar.

### E2 — Metaphor Mismatch
- **Looks like:** a control, icon, or gesture whose metaphor fights its function — a "trash" icon that
  archives, a switch that looks like a button, a skeuomorphic shelf that confuses (the iBooks
  bookshelf), a real-world mapping that no longer holds.
- **Why it's bad:** the signifier lies about the action; users predict the wrong outcome.
- **Fix:** make the metaphor match the mental model and the result; drop dead skeuomorphism; if a
  metaphor needs explaining, it's wrong.

### E3 — Desktop-Hover Dependency (the no-touch-equivalent trap)
- **Looks like:** functionality revealed only on **hover** (hover-reveal tools, hover menus, tooltip-
  only information, cursor-affordance cues) — invisible and unreachable on touch, and often on
  keyboard.
- **Why it's bad:** hover has **no touch equivalent**; the affordance simply doesn't exist for most
  users. Also a WCAG 2.2 **1.4.13 Content on Hover or Focus** concern (must be dismissable, hoverable,
  persistent).
- **Fix:** invert to **always-visible** or an explicit tap/long-press with a visible signifier; never
  hide essential content or actions behind hover; ensure keyboard-focus parity.

---

## How the engine uses this

- `design-audit` and `product-design-audit` run these groups as the **interaction-detection pass**
  behind their scored dimensions; a match feeds the prioritised-recommendations list.
- `design-qa-and-pre-launch-review` uses it as a **pre-launch go/no-go checklist** — any unaddressed
  A1–E3 finding is a gate item.
- `ux-remediation-and-redesign` (planned) uses it as the **diagnosis vocabulary** for the
  *detect → triage → fix → re-validate* loop; each entry's "fix" is its target right-pattern.
- Read alongside `ai-slop-taxonomy.md` (the machine-generated tells) and `design-doctrine.md`
  (the Mission + Anti-Slop Charter). Together they define what we must never ship.

*Companion to `doctrine/references/`. Patterns are evergreen; sources (Neil 2014, Maioli 2018)
refreshed to 2026 — dead-platform specifics removed, WCAG 2.2 and doctrine alignment added.*
