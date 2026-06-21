# Book Study 02 — Interaction Patterns (Scott & Neil; Neil; Kodeco)

**Engine:** `C:\wamp64\www\design-system-skills`
**Date:** 2026-06-21
**Scope:** Critical study of three interaction-pattern books against the design engine —
groups 04 (web/UI craft), 07 (mobile), 08 (motion), plus doctrine. Verdict-first: these books
are a **pattern-vocabulary and anti-pattern goldmine** whose *principles* are timeless but whose
*era assumptions* (desktop+hover 2009; skeuomorphism + dead platforms 2014; beginner Figma 2021)
must be flagged HARD before any pattern is lifted into a skill.

**Books studied**
1. **Designing Web Interfaces — Principles and Patterns for Rich Interactions** — Bill Scott & Theresa Neil, O'Reilly, **2009**. (Ajax/Flash "RIA" era.)
2. **Mobile Design Pattern Gallery — UI Patterns for Smartphone Apps** — Theresa Neil, O'Reilly, **2nd ed. 2014**. (iOS 6→7 transition; Windows Phone / BlackBerry still alive.)
3. **App Design Apprentice — A Non-Designers Guide to Making Better Mobile UI/UX** — raywenderlich.com / Kodeco, **~2021**. (Figma-centric beginner mobile course.)

---

## How this maps to what the engine already has

| Engine surface | Already covers | The books' relevance |
|---|---|---|
| `04/interaction-design-patterns` | Tidwell 3rd-ed behavioural + nav/layout/action/data patterns | Scott&Neil is the **rich-interaction complement to Tidwell** — direct-manipulation, transition, and feedback vocabulary Tidwell touches more lightly |
| `04/empty-error-and-loading-states` | states matrix, skeletons-over-spinners, recovery affordances | Neil's **Feedback** + **System Status** ("Avoid the Spinner", skeleton screens) and **Idiot Boxes** anti-pattern directly reinforce it |
| `04/form-ux-design` | field anatomy, validation, wizard, labels-above | Neil's **Forms** chapter + **forced-registration** anti-pattern; Kodeco's concrete mobile form sizing |
| `07/*` (ios, android, cross-platform) | HIG/Liquid Glass, M3 Expressive, Unify/Diverge | Neil's mobile nav taxonomy + **Square Peg Round Hole** anti-pattern *is* the cross-parity argument, vintage 2014 |
| `08/motion-design` | 100/300/500, easing, reduced-motion, springs | Scott&Neil "Use Transitions" principle is the *why* behind the engine's *how*; Kodeco's interpolators are weaker and partly contradict doctrine |

---

# BOOK 1 — Designing Web Interfaces (Scott & Neil, 2009)

## (a) Load-bearing principles & patterns

### The Six Principles (verbatim, the book's spine)
1. **Make It Direct** — allow input wherever there is output; manipulate content in place (Cooper's direct manipulation).
2. **Keep It Lightweight** — minimise interaction cost via contextual placement + progressive disclosure.
3. **Stay on the Page** — avoid page-refresh breaks that interrupt flow.
4. **Provide an Invitation** — cure discoverability with prompts, cues, signifiers (just-in-time hints).
5. **Use Transitions** — animate purposefully to communicate change; without it users wonder what happened.
6. **React Immediately** — give immediate feedback to every action; responsiveness reads as intelligence.

### Pattern groups (load-bearing names only)
- **Make It Direct** → *In-Page Editing* (Single-Field / Multi-Field / Overlay / Table / Group Inline Edit), *Drag and Drop* (Module/List/Object/Action/Collection), *Direct Selection* (Toggle/Collected/Object/Hybrid).
- **Keep It Lightweight** → *Contextual Tools* (Always-Visible / **Hover-Reveal** / Toggle-Reveal / Multi-Level / Secondary right-click menus).
- **Stay on the Page** → *Overlays* (Dialog/Detail/Input), *Inlays* (Dialog/List/Detail/Tabs), *Virtual Pages* (Virtual Scrolling, Inline Paging, Scrolled Paging/Carousel, Virtual Panning, ZUI), *Process Flow* (Interactive single-page, Inline Assistant, Dialog-Overlay, Configurator, Static single-page).
- **Provide an Invitation** → *Static* (Call-to-Action, Tour), *Dynamic* (**Hover** Invitation, Affordance, Drag-and-Drop, Inference, More-Content).
- **Use Transitions** → Brighten-and-Dim (lightbox), Expand/Collapse, **Self-Healing Fade**, Animation, Spotlight.
- **React Immediately** → *Lookup* (Auto Complete, Live Suggest, Live Search, Refining Search), *Feedback* (Live Preview, Progressive Disclosure, Progress Indicator, Periodic Refresh).

## (b) DATED — flag HARD

- **Hover is load-bearing and it is dead on touch.** *Hover-Reveal Tools* and *Hover Invitation* are two of the book's headline ideas; **neither has a touch equivalent**. Any port to mobile must invert them to always-visible or explicit tap/long-press. **This is the single biggest hazard in the book** — do not let it leak into a mobile skill.
- **Cursor affordances** (I-beam on edit, grab cursor on drag) — vanish on touch; no signifier remains.
- **Drag-and-drop as a hero pattern** (two whole chapters, "interesting moments", spring-loaded pause-to-open) — over-weighted for 2026; on touch it's a *specialised* interaction (Kanban, file upload, reorder), not a default mover, and carries real a11y cost.
- **"Stay on the Page" as a *revelation*** — in the SPA/React era it is table stakes, not a principle to argue for. Reframe as "minimise context loss."
- **Flash/Ajax framing** and **"Loading…" text** idioms — superseded by fetch/streaming and **skeletons-over-spinners** (which the engine already mandates).
- **Lightbox/modal as "lightweight"** — modals now read as *high-friction* on mobile; bottom sheets / popovers / inline are the lighter answers.
- **Secondary (right-click) menus** — no reliable touch analogue; long-press differs in discoverability and conflicts with system gestures.

## (b) What still holds
**All six principles survive**, three of them stronger than ever: **Make It Direct** (inline edit is everywhere — Notion/Gmail), **React Immediately** (optimistic UI, live validation = expectation), **Use Transitions** (motion-to-explain-change — exactly the engine's `motion-design` thesis). Also timeless: **Progressive Disclosure**, **Live Preview**, **Auto Complete / Live Search** (with debounce), **Self-Healing Fade** (toast auto-dismiss), and **Invitations/signifiers** (now delivered as empty-state copy + coachmarks, *not* hover).

## (b) Contradicts our doctrine?
No hard contradiction — but the book's hover/drag/lightbox defaults are precisely the kind of **convergent-desktop idiom** the doctrine tells us to avoid reflexively. The book is a *vocabulary*, not a style; keep the principles, discard the 2009 mechanisms.

---

# BOOK 2 — Mobile Design Pattern Gallery (Neil, 2014)

## (a) Load-bearing patterns

**Chapter taxonomy:** Navigation · Forms · Tables · Search/Sort/Filter · Tools · Charts · Tutorials & Invitations · Social · Feedback & Affordance · Help · **Anti-Patterns**.

- **Navigation** — *Persistent:* Springboard, Cards, List Menu, Dashboard, Gallery, Tab Menu, Skeuomorphic. *Transient:* Side Drawer (overlay vs inlay), Toggle Menu, Pie Menu. *Secondary:* Page Swiping (dot indicators), Scrolling Tabs, Accordion.
- **Forms** — Sign In (unmask, social, PIN), Registration (+personalization), Multi-Step wizard, Checkout (express/guest/1-click), Calculator, Long Form (inline validation).
- **Search/Sort/Filter** — Implicit/Explicit/Auto-Complete/Dynamic/Scoped/Saved-Recent-Popular search; On-screen / Overlay / Form / Drawer / Gesture variants for sort & filter.
- **Tables** — Basic, Headerless, Fixed-Column, Overview-plus-Data, Grouped Rows, Visual-Indicator, Editable.
- **Tools** — Toolbar, Toolbox, CTA Button, Inline Actions, **Multi-State Button** (Download→Downloading→Open), Contextual Tools, Bulk Actions, Lock-Screen Controls.
- **Charts** — Filters, Interactive Timeline, Data-Point Details, Drill Down, Dashboard, Zoom, **Sparklines**, Integrated Legend, Thresholds, Pivot.
- **Invitations** — Tips (sticky-note + one CTA), Persistent, Discoverable (pull-to-refresh label).
- **Feedback** — Error Messages (inline, plain, solution-bearing), Confirmation (animate / toast ≤5s / count update), System Status (**skeleton screens; "Avoid the Spinner"**; cancellable progress).
- **Affordance** — Tap (contrast/weight/shadow), Swipe/Flick (dots, overflow hint), Drag (handles, drop zones).

### The Anti-Patterns chapter (the gold — all 8 still valid)
**Novel Notions** (be creative in UX/flows, not in controls) · **Needless Complexity** (overloaded/hidden gestures) · **Metaphor Mismatch** (control / icon / gesture / mental-model) · **Idiot Boxes** (modal dialogs that interrupt for nothing) · **Chart Junk** (3D pies, decorative gridlines) · **Oceans of Buttons** (prioritise; Toolbar + More) · **Square Peg, Round Hole** (one platform's UI forced on another) · **Forced Sign-Up/Sign-In** ("long sign-up form = deleted app").

## (b) DATED — flag HARD

- **Skeuomorphic navigation** as a first-class pattern — **dead** since iOS 7 (2013). Keep only as a cautionary example (the iBooks bookshelf confusion the book itself flags).
- **Dead platforms covered in depth:** **Windows Phone** (Pivot/Panorama/App Bar/live tiles) and **BlackBerry/WebOS/Symbian**. Historical only — ignore the WP-specific guidance entirely.
- **iOS 6-era chrome** (thick glossy tab bars, dock styling) — visuals dated; the *structure* (≤5 tabs, More overflow) survives.
- **"Flat design hurts affordance" framing** — a real 2013 problem now 13 years solved; designers layer weight/contrast/elevation. The warning is dated though the underlying point (signal tappability) holds.
- **Pull-to-refresh as near-universal** — now in **decline** (background/auto-refresh common); still valid where a manual refresh is meaningful.
- **Cross-platform parity optimism inverted by the book itself** — and the divergence has only widened (Liquid Glass / SF Symbols 8 vs Material 3 Expressive, foldables). This makes **Square Peg Round Hole** *more* relevant, not less.
- **Native-control screenshots** (pickers, segmented controls, spinners) predate M3 and current HIG — patterns sound, visuals stale.

## (b) What still holds
**The entire navigation/form/search/feedback taxonomy and all eight anti-patterns are current.** Prescient calls that landed: **skeleton screens** over spinners, **single-CTA transparent onboarding** beats multi-step tours (Intuit Snap Payroll), tutorials-that-let-you-*do* beat passive tours, **forced registration kills installs**, cross-device sync is non-negotiable (Audible "Forget-Me-Not"). These align cleanly with the engine's `empty-error-and-loading-states`, `form-ux-design`, and the planned `onboarding-and-first-run-design`.

## (b) Contradicts our doctrine?
No — it *reinforces* it. The anti-patterns are a 2014 articulation of the anti-slop instinct (don't be novel at the control level; don't bury affordance; respect each platform). One nuance: the book's "be consistent across platforms" optimism is **explicitly recanted** in its own 2nd-ed preface, matching `cross-platform-design-parity`'s **Unify-meaning / Diverge-mechanism** rule.

---

# BOOK 3 — App Design Apprentice (Kodeco, ~2021)

## (a) Load-bearing principles & concrete rules
Beginner Figma course; the value is **concrete mobile numbers**, not theory.
- **8pt spacing grid** (all margins/padding in multiples of 8); 16pt content inset; 32pt section/CTA spacing.
- **Touch target ~60×60** used for buttons (conservative vs HIG 44pt / Material 48dp — and correct to be conservative).
- **Modular type scale 1.3×** rounded to even (e.g. 32/24/18/14/12); 14pt body; separate text styles per use even when visually identical.
- **WCAG contrast** 4.5:1 body, 3:1 large/UI, 7:1 AAA — stated correctly.
- **Bottom navigation** 56pt, active/inactive colour states, icon 24–36pt + 12pt label.
- **Modal bottom sheet** with top-only 16pt corner radius; card radii 4/8/16.
- **Process:** wireframe-before-hi-fi, design-with-real-data, components→variants→pages, involve engineers early, prototype before kickoff, **Smart Animate** + interpolators (ease-in/out/back).

## (b) DATED & TOO-BASIC — flag HARD

- **iOS 11 UI kit / Material icons of its day / Figma build 85** — tool and asset references moved on; ignore version specifics.
- **No dark mode, no Dynamic Type, no notch/Dynamic Island, no safe-area/foldable, no gesture-nav, no haptics** — a serious omission set for 2026 mobile (the engine's `07/*` skills already cover all of these; the book does not).
- **"Non-designer / safe defaults" framing directly tensions the doctrine.** The book optimises for *generic correctness*; the doctrine optimises for *authored distinctiveness*. Its triadic-"saturation-to-eleven" palette and stock-kit reliance are exactly the convergent-mean output the anti-slop charter exists to beat. **Use its numbers, reject its taste.**
- **Interpolator advice partly contradicts `motion-design`:** the book teaches **ease-in-back / ease-out-back (anticipation/bounce)** as default feel. The engine **bans visible overshoot/bounce/elastic** (ζ<0.6) as the #1 AI-animation tell. Flag this as a **direct contradiction** — the engine wins.
- **No design tokens, no handoff tooling depth, no micro-interactions, no a11y beyond contrast** — below premium-studio bar.

## (b) What still holds
The **numbers are evergreen and worth extracting as a cited baseline**: 8pt grid, 16/32 insets, 44/48/60 target sizing, 1.3× scale, 4.5:1/3:1/7:1 contrast, 4/8/16 radii, 1.5×+ line-height. The *process* (wireframe→hi-fi, real-data, component/variant discipline) is sound and matches the planned `05/wireframing-and-prototyping`.

---

# ENGINE IMPACT

## Harden existing skills

| Skill | Harden with | As |
|---|---|---|
| `04/interaction-design-patterns` | Scott&Neil **Six Principles** + the direct-manipulation / lookup / feedback pattern names; **explicit "hover is desktop-only — touch invert" caveat** | new `references/rich-interaction-principles.md`; add the hover→touch inversion note to Anti-Patterns |
| `04/empty-error-and-loading-states` | Neil **System Status** ("Avoid the Spinner", skeletons, cancellable progress) + **Confirmation** (toast ≤5s, count update, animate-the-action) | add as confirming citations in `references/state-matrix.md`; example reinforcement |
| `04/form-ux-design` | Neil **forced-registration** anti-pattern + Kodeco mobile field sizing/spacing numbers | add to `references/` (gateway-before-long-form already exists — cite the anti-pattern explicitly) |
| `07/cross-platform-design-parity` | Neil **Square Peg, Round Hole** as the canonical historical anti-pattern; the book's own recanted "parity optimism" | cite in Anti-Patterns / rationale for Unify-meaning-Diverge-mechanism |
| `07/ios` + `07/android` | Neil mobile-nav taxonomy (Springboard/List/Tab/Side-Drawer/Page-Swiping) as named vocabulary; **skeuomorphism = dead** note | reference vocabulary; reinforce flat-era affordance |
| `08/motion-design` | Scott&Neil **"Use Transitions"** as the *why*; **flag Kodeco ease-*-back as the banned-bounce contradiction** | strengthen the "NEVER bounce/elastic" section with the named external contradiction |

## New skill / reference justified?
- **New reference, not a new skill** — fold a `references/anti-patterns-catalog.md` into `00-cross-cutting-ops-qa-a11y` (or the planned `design-qa-and-pre-launch-review`) seeded with Neil's **eight anti-patterns** as a QA checklist. They are evergreen and cross every group; this is the single highest-value extraction.
- **No net-new skill is warranted.** Every pattern domain in all three books is already owned by an existing or Phase-2-planned skill. The books supply *vocabulary, citations, and anti-patterns*, not an uncovered domain.

## Phase-2 items: CONFIRMED / CHANGED / REDUNDANT

| Phase-2 item | Verdict | Why |
|---|---|---|
| `07/touch-gesture-and-haptics` | **CONFIRMED** | Neil's Affordance (Tap/Swipe/Drag) + the hover-has-no-touch-equivalent gap from Book 1 make this clearly needed; cite both. |
| `08/micro-interactions-and-feedback` | **CONFIRMED + sharpened** | Scott&Neil feedback/transition patterns + Neil Multi-State Button are textbook source material; **must inherit motion-design's bounce ban to neutralise Kodeco's ease-*-back advice.** |
| `04/onboarding-and-first-run-design` | **CONFIRMED** | Neil's Tutorials/Invitations chapter (single-CTA transparency > tours; let-user-*do*) is strong, citable backbone. |
| `04/component-states-and-interaction-fidelity` | **CONFIRMED** | Scott&Neil hover/active/feedback states feed the state-matrix method directly. |
| `05/wireframing-and-prototyping` | **CONFIRMED** | Kodeco's wireframe-first + Smart-Animate process is a usable (if basic) source. |
| `04/trust-credibility-and-social-proof` | **CONFIRMED (partial source)** | Neil's Social chapter (Profiles/Following/Gamification) supplies some pattern vocabulary; not a primary source. |
| A dedicated "rich-interaction" or "mobile-pattern-gallery" skill | **REDUNDANT** | Covered by existing `interaction-design-patterns` (Tidwell) + the `07/*` set; books become *references*, not a skill. |

---

# Extract-into table

| Source (book · locus) | Extract | Into (engine path) | Form | Caveat to encode |
|---|---|---|---|---|
| Scott&Neil · Six Principles | Make-Direct / Lightweight / Stay-on-Page / Invitation / Transitions / React-Immediately | `04/interaction-design-patterns/references/rich-interaction-principles.md` | new reference | "Stay-on-Page" now table-stakes; reframe as minimise-context-loss |
| Scott&Neil · Contextual Tools + Invitations | Hover-Reveal / Hover-Invitation | `04/interaction-design-patterns` Anti-Patterns | inline caveat | **desktop+mouse only — invert to always-visible/tap on touch** |
| Scott&Neil · Use Transitions | transitions communicate change | `08/motion-design` rationale | citation | keep purposeful; bounce/elastic still banned |
| Neil 2014 · Anti-Patterns ch. | 8 anti-patterns as QA checklist | `00-cross-cutting` → `references/anti-patterns-catalog.md` (or design-qa skill) | new reference | refresh 2010–14 screenshots; patterns evergreen |
| Neil 2014 · Feedback/System Status | Avoid-the-Spinner, skeletons, ≤5s toast, cancellable progress | `04/empty-error-and-loading-states/references/state-matrix.md` | confirming citation | already engine policy — adds provenance |
| Neil 2014 · Forms + forced-reg | gateway-before-long-form, value-before-auth | `04/form-ux-design` + `04/onboarding-and-first-run-design` | citation | OAuth/passkey now default; book examples dated |
| Neil 2014 · Navigation taxonomy | Springboard/List/Tab/Side-Drawer/Page-Swiping names | `07/ios` + `07/android` | vocabulary ref | skeuomorphic = dead; WP/BlackBerry = ignore |
| Neil 2014 · Square Peg Round Hole | platform-forcing anti-pattern | `07/cross-platform-design-parity` Anti-Patterns | citation | strengthens Unify-meaning/Diverge-mechanism |
| Neil 2014 · Affordance (Tap/Swipe/Drag) | gesture affordance signifiers | `07/touch-gesture-and-haptics` (Phase-2) | source material | hover has no touch analogue (from Book 1) |
| Kodeco · spacing/type/contrast numbers | 8pt grid · 16/32 · 44/48/60 · 1.3× · 4.5/3/7:1 · 4/8/16 radii | `07/*` + `03/layout` + `doctrine/references/type-scale-and-spacing.md` | cited baseline | numbers only — reject the "safe-default" taste |
| Kodeco · interpolators | ease-in/out-**back** (anticipation/bounce) | `08/motion-design` "NEVER use" table | **negative example** | **direct contradiction — engine bans visible overshoot (ζ<0.6)** |
| Kodeco · process | wireframe-first, real-data, components/variants | `05/wireframing-and-prototyping` (Phase-2) | source | basic; supplement with senior craft |

---

*Companion to `docs/book-study/` series. No code changed; this is an analysis artifact. All
extractions are advisory inputs to the Phase-2 hardening wave, gated by the anti-slop charter:
take the books' vocabulary and numbers, never their convergent-default taste.*
