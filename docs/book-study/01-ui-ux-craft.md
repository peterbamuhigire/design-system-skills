# Book Study 01 — UI/UX Craft (6 books, critically mapped to the engine)

**Engine:** `C:\wamp64\www\design-system-skills` — 52 skills / 14 groups, anchored on `doctrine/design-doctrine.md`
(Mission: *the moat is looking human-made*; the Anti-Slop Charter; the sourcing-authority asymmetry rule).
**Date:** 2026-06-21 · **Author:** study pass for the hardening-june programme.

## How to read this document

This is a **critical study, not a summary.** For each book it states (a) the load-bearing,
*specific* material worth extracting; (b) a critical take — what is dated, what is thinner than our
doctrine already demands, and what is genuinely world-class and currently absent from our 52 skills;
and (c) engine impact — which existing skills to harden, which net-new skills/refs are justified, and
which Phase-2 plan items each book **CONFIRMS / CHANGES / makes REDUNDANT** (i.e. already covered).

**The standing filter.** Every one of these books is a *beginner-to-intermediate craft primer.* Our
doctrine already operates above their ceiling on three axes they all fail: (1) the anti-slop mission
(none of them push *away* from convergent defaults — several actively recommend the safe mean), (2)
sourcing authority (none distinguish human design authority from AI-vendor convergence), (3) 2026
standards (WCAG 2.2, container queries, fluid `clamp()`, design tokens/variables, dark-mode semantics,
motion as a system). So the extraction posture is **mine for specific numbers, named frameworks, and
checklists — never for taste, trend, or process spine.** Where a book contradicts the doctrine, the
doctrine wins and the contradiction is logged as an *anti-pattern to inoculate against.*

> **Provenance note.** The file named *"Master The UI UX Design Industry — From Beginner to Expert.md"*
> does **not** contain a career/industry survey; its body is **Will Grant's *101 UX Principles* (2018)** —
> a 101-rule UX-craft reference. This study treats it as that book (book 6 below) and ignores the
> misleading title. Any prior expectation that it would harden `enterprise-ux-process` /
> `design-handoff` from a *business* angle is void — its value is **UX craft + form/journey patterns.**

---

## Book 1 — *Web UI Design for the Human Eye* (UXPin; Cao, Zieba, Stryjewski, Ellis, 2015)

### (a) Load-bearing principles worth extracting
- **Three-layer consistency model — external / internal / tactical.** External = conformance to
  market conventions users import from other products; internal = cohesion across your own pages;
  tactical = pixel-level rules (logo always top-left, every H1 identically treated). **The
  load-bearing insight: "inconsistency is potent only atop consistency"** — you may break a pattern
  for emphasis *only* after establishing the pattern. This is a rigorous articulation most systems
  lack, and it is *exactly* the doctrine's "restraint plus one strong intentional choice" stated from
  the consistency side.
- **Pattern classification taxonomy — tactical / strategic / site-specific.** Tactical = atomic
  black-and-white rules; strategic = "how" choices (jump-to vs sticky nav) that depend on user + context;
  site-specific = domain-expected patterns (agency site expects portfolio; airline expects booking form).
  Clean three-level hierarchy; most pattern libraries are flat lists.
- **Affordance / signifier / perceived-affordance** grounding (Norman) for *why* conventions reduce
  explaining cost — "consistently-used signifiers from other sites cut down your own explaining" (a
  network-effect argument for borrowing established signifiers).
- **Pre-design research tripod:** open/closed **card sorting**; **behavioural** user-interview questions
  ("what do you like about your current tool?") over micro-UX preference questions; **heuristic
  competitive evaluation** scored by ~5 evaluators and visualised as an **overlapping radar / spider-web**
  to expose where *all* competitors converge (don't break) vs where *none* solved it (innovation gap).
- **Vertical rhythm rule:** line-spacing = **1.4–1.6× font size**, set via global CSS, treated as a system.

### (b) Critical take — dated vs 2026 / vs our doctrine
- **Dated / absent:** zero accessibility (no WCAG, no contrast maths — and it cheerfully advises
  "occasional red keeps it in the background" with no contrast floor), zero responsive/breakpoint
  strategy, zero dark mode / tokens, no component variants or state taxonomy, no motion as a system
  (treats animation as 2015 novelty). The "0.7 % of visual input is conscious / 50 ms judgment"
  neuroscience is loosely sourced — keep the *claim that first impressions are pre-rational*, drop the
  fake precision.
- **Weaker than our doctrine:** its consistency philosophy is good but it never reaches the *anti-slop*
  conclusion — it would happily ship a consistent, conventional, utterly templated page. Our doctrine
  demands consistency **plus** one authored, convergence-breaking choice. The book gives us the
  consistency floor; the doctrine supplies the ceiling it never climbs to.
- **Genuinely world-class and currently under-articulated in our engine:** the **external/internal/tactical
  consistency model** and the **tactical/strategic/site-specific pattern taxonomy** — two clean mental
  models we don't name anywhere — and the **competitive heuristic spider-web** as a *pre-design* artifact.
  These are the book's real contribution.

### (c) Engine impact
- **Harden** `04…/navigation-and-information-architecture` and `04…/interaction-design-patterns` with the
  **tactical/strategic/site-specific** pattern taxonomy and the affordance/signifier vocabulary.
- **Harden** `00…/design-audit` (and `visual-product-slop-audit`) with the **three-layer consistency
  model** as an audit lens (is the inconsistency *intentional and earned*, or just drift?).
- **Harden** `05…/ux-research-and-usability-testing` with the **competitive heuristic spider-web** as a
  named pre-design technique, and behavioural-over-preference interview framing.
- **CONFIRMS** Phase-2 `heuristic-evaluation-and-design-critique` (the spider-web is a perfect worked
  example for it) and `journey-mapping-and-service-design` (pre-design research feeds it).
- **REDUNDANT now:** the book's vertical-rhythm and palette-locking advice is already exceeded by
  `doctrine/references/type-scale-and-spacing.md` + `02…/color-system-and-palette`. Do **not** create any
  "consistency" skill — fold the two taxonomies into existing audit/IA skills as references.

---

## Book 2 — *101 Dos and Don'ts of UI Design* (Pixsel Academy)

### (a) Load-bearing rules worth extracting (the sharp, non-obvious ~quarter of 101)
- **Button side-padding = 2× top/bottom padding** (optical balance, e.g. 16 H / 8 V). Precise, durable.
- **Border-radius hierarchy: an inner element's radius ≈ outer container radius − its padding** (nested
  radii must be concentric, not equal). A real design-system tell most juniors miss.
- **Soft shadow defaults:** the tool default (Y 2 / blur 4 / 50 %) reads harsh; use Y 8 / blur 24 / ~15 %.
- **Right-align numeric columns** (decimal alignment for prices/metrics); left-align text.
- **Checkboxes are square, radios are round** — never round checkboxes (semantic shape lock).
- **Label ≠ placeholder** (placeholder-as-label is a usability failure); **show password rules inline,
  never only in a tooltip**; **boxed form fields** parse faster than underline-only.
- **Line length 45–75 chars (safe 55–65)**, measured in characters not pixels; **≥14 pt body, 16 safer**;
  **2–3 discrete type sizes**; avoid pure #000/#FFF (≥ ~#333 floor).
- **Skeletons > spinners** for perceived performance; **progress visualisation** lowers perceived friction;
  **specific button copy** ("Create account", not "OK"/"Next"); **dark overlay** behind text on imagery.

### (b) Critical take
- **Format weakness (structural):** 101 flat, equal-weight rules with **no thresholds where they exist
  no interdependencies, no edge cases, no "when the rule breaks."** Some "rules" are simply wrong by 2026:
  hamburger-menu "increases conversion" (false as a universal), "red = destructive / blue = normal" colour
  psychology (context beats inherent semantics), shadows-as-elevation as the *only* dark-mode depth cue
  (modern dark mode uses surface tint + scale, per our `dark-mode-and-theming`). The "saturation 200–500
  tone level" rule is non-standard and unmeasurable — replace with WCAG/APCA contrast.
- **vs doctrine:** it is a *safe-mean* generator — it optimises for "correct," never for "authored." It will
  never trip the anti-slop mission. Treat it as a **lint ruleset**, not a design philosophy.
- **World-class/rare:** the **concentric border-radius rule** and the **2× button-padding ratio** are the
  two genuinely non-obvious numeric tells worth banking — neither is currently stated in our engine.

### (c) Engine impact
- **Harden** `04…/practical-ui-design` (deep-dive: buttons/forms) with the **2× button padding** and
  **concentric border-radius** rules, and the **soft-shadow default** numbers.
- **Harden** `12…/data-visualization` + `13…/docx`/`xlsx` table guidance with **right-align numerics**.
- **Harden** `04…/form-ux-design` with **boxed-fields-parse-faster** and **inline password rules** (it
  already nails label≠placeholder — see below).
- **REDUNDANT now (do not re-extract):** label-vs-placeholder, single-column forms, ≥14 pt body, line-length
  45–75, avoid pure black/white, skeleton>spinner, specific CTA copy — **all already in
  `form-ux-design`, `practical-ui-design`, `empty-error-and-loading-states`, and the type-scale ref.**
- **Net:** this book justifies **no new skill.** Its only durable contribution is ~4 numeric tells folded
  into `practical-ui-design`. Consider a small `references/ui-numeric-tells.md` under that skill so the
  concentric-radius and padding-ratio rules are citable.

---

## Book 3 — *How to Design Better UI Components 3.0* (2022, rev. 2024)

### (a) Load-bearing principles — component-by-component
This is the **most operationally specific** of the six. Per-component craft worth banking:
- **Buttons:** height 32–60 (48 Material / 44 iOS / 32–40 desktop); **horizontal padding = 2× vertical**;
  **44 px minimum hit area via "invisible padding"**; filled/ghost/text = primary/secondary/tertiary;
  align multiple buttons by importance; action-verb labels.
- **Cards:** internal padding **16–24 (12–20 H, +4–8 V for optical balance)**; **between cards 16–40**;
  **around card sections 64–96**; fixed min/max heights + uniform image aspect ratios; truncate with ellipsis.
- **Dropdowns:** scroll container at **5+ items**; multi-select via checkbox rows; nested via indentation;
  search + modal overlay on mobile; states default/hover/open/selected/disabled.
- **Search:** ≥44 px height; recent searches; autocomplete; designed **"no results"** state.
- **Modals:** close via X / outside-click / Esc; **avoid double-negatives** in confirm copy; progress for
  long ops; confirmation for destructive actions.
- **Hero:** **F-pattern (text-heavy, left) vs Z-pattern (visual, centred)** scanning; emotion-driven
  headline; primary vs subtle-secondary CTA; social-proof placement; "tease continuation" past the fold.
- **Pricing:** highlight popular plan (size/border/tag); sticky comparison headers; **charm pricing
  (9.95/9.99)**; scarcity; hover tooltips.
- **Frameworks named:** 8-pt grid (4-pt refinement), box model, vertical rhythm, Atomic Design,
  60-30-10, F/Z patterns. WCAG contrast (3:1 large / UI, 4.5:1 small) embedded throughout.

### (b) Critical take
- **Strength:** the **anatomy + numeric padding/spacing + per-component state lists** are genuinely
  useful and more precise than most primers. This is the book to mine for **component-states fidelity**.
- **Weakness vs 2026 / our engine:** **no motion specs** (no duration/easing/choreography), **no design
  tokens / variant-prop API / compound components**, **dark mode is one paragraph**, **accessibility stops
  at contrast** (no ARIA, no focus-visible spec, no focus order/trap, no keyboard model for dropdowns/
  modals), responsive is just two extremes (1440 / 375) with no intermediate strategy. Visuals carry a
  2020–21 sensibility (Material 2, residual glassmorphism/neumorphism).
- **vs doctrine:** component anatomy is taste-neutral and safe — it will not produce slop, but it will not
  produce *distinctiveness* either. Mine the **numbers and states**, not the look.

### (c) Engine impact — **the highest-yield book for Phase-2**
- **CONFIRMS and supplies the worked content for the Phase-2 P1 item
  `component-states-and-interaction-fidelity`** (group 04, ref `state-matrix-method.md`, ex
  `input-state-matrix.md`). This book's per-component state lists + anatomy numbers are the ideal raw
  material; **add to that spec the gaps the book misses** — focus-visible, focus order/trap, keyboard model,
  loading/skeleton, reduced-motion — sourced from `accessibility-wcag-2-2-compliance` + `motion-design`.
- **Harden** `04…/practical-ui-design` (component patterns), `04…/form-ux-design`, and
  `09…/component-library-architecture` with the **card spacing triad (16-24 / 16-40 / 64-96)** and the
  **dropdown/modal/search anatomy + keyboard/focus additions.**
- **Harden** `04…/landing-page-and-conversion-design` with the **F vs Z hero scanning** model + tease-past-
  fold (sourcing authority caveat: present F/Z as eye-tracking heuristics, not laws).
- **CONFIRMS** Phase-2 `ecommerce-and-checkout-ux` (pricing/charm/scarcity → `checkout-flow-patterns.md`).
- **REDUNDANT now:** 8-pt grid, 60-30-10, Atomic Design, contrast minimums — already in
  `layout-grid-and-spacing`, `color-system-and-palette`, `component-library-architecture`,
  `accessible-color-and-contrast`. Do **not** create a "components" skill — `component-library-architecture`
  + the new `component-states-and-interaction-fidelity` cover the territory; this book *fills* them.
- **Suggested new ref:** `references/component-anatomy-numbers.md` under
  `component-states-and-interaction-fidelity` (or `component-library-architecture`) banking the per-
  component padding/height/spacing numbers as a citable table.

---

## Book 4 — *Fundamentals of Creating a Great UI/UX* (Elisa Paduraru, 2022)

### (a) Load-bearing principles
- **Atomic-component anatomy with numbers** (its real value): grid 12-col / 8-pt, 16 px margins/gutters
  floor; **line-height inversely proportional to size** (~1.6× small → 1.1–1.3× large); ≥12 px text,
  14–16 base; **60-30-10** colour; shadow blur >30 / opacity <20 / no top-shadow (light from above) /
  layered; buttons 32 H / 18 V padding, 16 pt text, 36–48 hit area; tables right-align numerics, 48 px
  mobile tap; charts: no 3D, tooltips, keep gridlines, legends, no Lorem.
- **Named laws used correctly:** golden ratio for a type scale, rule of thirds, F/Z patterns, **halation**
  (pure-black/white edge shimmer → avoid pure values), cognitive-load argument for rounded corners,
  **CUBI** (Content / User goals / Business goals / Interactions) named once.
- Dedicated **dark-mode contrast / "white shadow" mistakes** coverage — rare for 2022.

### (b) Critical take
- **Trend-as-principle hazard:** presents 2021 trends (glassmorphism, neumorphism, 3D) as best practice —
  **directly contradicts our `ai-slop-taxonomy` / `distinctive-by-design`**, which flag glassmorphism/
  frosted-blur as decoration-without-purpose slop tells. **Log as an inoculation target**, not an extract.
- **Accessibility is performative** (a stated goal, never operationalised — no WCAG levels, ARIA, SR,
  keyboard), **research is near-absent** ("collect feedback" ≠ method), **no tokens/variants/governance**,
  **no motion principles**, **CUBI named but never executed.** Case studies are "big brand uses X" →
  legitimacy by association, not rationale.
- **vs doctrine:** it teaches the *safe contemporary look*, the precise mean the doctrine exists to escape.
  Mine the anatomy numbers and the named optical effects; reject the trend framing wholesale.
- **World-class/rare:** the **halation** note (avoid pure #000/#FFF because of edge shimmer) is a specific,
  correct optical rule we state only as "avoid pure black/white" — worth the physical *reason*.

### (c) Engine impact
- **Harden** `04…/practical-ui-design` (already says "avoid pure black/white") with the **halation reason**;
  harden `02…/color-system-and-palette` likewise.
- **Harden** `02…/dark-mode-and-theming` with the **"white shadow on dark is wrong / use surface tint"**
  mistake catalogue (book corroborates our existing stance).
- **Feeds** Phase-2 `composition-and-visual-hierarchy` (rule of thirds, F/Z, visual-weight factors) — as
  *heuristics under* the doctrine's asymmetry/focal-point rules, never as a substitute.
- **CHANGES nothing; CONFIRMS** the anatomy numbers already in the engine.
- **REDUNDANT now / inoculation:** its glassmorphism-neumorphism advocacy is **explicitly counter-doctrinal**
  — add a one-line citation in `ai-slop-taxonomy.md` examples ("primers of this era recommend the very
  decorative surfaces we ban"). No new skill justified.

---

## Book 5 — *2022 Guide to UX/UI Design in 45 Minutes for Beginners*

### (a) Load-bearing principles
- **NN/g process spine:** Discovery → Design → Develop → Evaluate; qual/quant × attitudinal/behavioural;
  deliverable chain persona → journey map → user flow (flowchart notation: rect=screen, circle=action,
  diamond=decision).
- **Numbers worth noting:** **60-30-10** colour; golden-ratio type stepping; WCAG **4.5:1 / 3:1**; mobile
  tap **≥40 pt**; leading ~30 % over cap-height; ≤2–3 typefaces; **5 users × ≥3 rounds** usability testing;
  8th-grade reading level (12th for expert audiences); personas 1–2 pp.

### (b) Critical take — be honest
- **Thinnest of the six.** ~20–30 % directly usable; the rest is filler, dated tooling (Axure/Balsamiq/
  Sketch/Adobe XD over Figma; paper-prototyping over-weighted), and a **persuasion-psychology chapter that
  is marketing copy dressed as UX** (Maslow/scarcity listicle, zero integration). The "45 minutes" claim is
  false. No interaction states, no IA depth, no synthesis rigor, no responsive depth.
- **vs doctrine:** offers *nothing* on distinctiveness, sourcing authority, or 2026 craft. Its process spine
  is real but **our `enterprise-ux-process` already carries Double Diamond / 5-planes / deliverable chains
  at higher fidelity** (corroborated by book 6's better treatment).
- **World-class/rare:** none. It is a vocabulary primer.

### (c) Engine impact
- **CONFIRMS** (does not extend) `05…/enterprise-ux-process`, `05…/ux-research-and-usability-testing`, and
  the Phase-2 `wireframing-and-prototyping` item — the fidelity ladder (paper→lo→hi→HTML) is a fine *example*
  for that skill, nothing more.
- **CHANGES:** its tool list is **stale** — when `figma-and-tooling-workflow` (Phase-2, group 09) is built,
  ensure it is **Figma-variables/modes/dev-mode-current**, explicitly *not* the Axure/Sketch/XD world this
  book assumes.
- **REDUNDANT now:** everything operational here is already met or exceeded. **No extraction beyond the
  5-users/3-rounds and reading-grade numbers** (which can sit as citations in the research skill).
- **No new skill. Lowest-yield book of the set.**

---

## Book 6 — *101 UX Principles* (Will Grant, 2018) — *(mislabelled "Master The UI/UX Design Industry")*

### (a) Load-bearing principles — the strongest *UX-pattern* source of the six
- **Form conversion framework (the book's gold, ch. 44–57):** minimise fields (signup = email + password +
  optional name); **validate on blur, not submit**; **don't clear the field on error**; inline + field-
  highlighted errors; **pre-fill known data** (username in password-reset); **forgiveness** — strip spaces,
  accept flexible phone formats, case-insensitive except passwords.
- **Payment-form distillation:** **single card-number field** with visual 4-digit grouping + auto-spacing;
  expiry + CV2 only; one-tap autofill; HTTPS-only.
- **Obvious / Easy / Possible** three-tier feature-visibility model: core = always visible; frequent =
  secondary toolbar/menu; rare/advanced = tucked but discoverable. A genuinely durable decision framework.
- **Journey signposting:** every task has beginning/middle/end; visual landmarks per context; breadcrumbs;
  progress indicators; **explicit completion messages** ("saved/sent/posted"); preserve context on back.
- **Undo / recoverability:** destructive action → **toast + undo link with a 5–10 s window**, then server-
  confirm; auto-save non-destructive edits; show unsaved state in title bar.
- **Defaults intelligence:** Pareto — pull the top ~20 % of journeys from analytics and set defaults to
  serve them (Slack's "Not your first team?" toggle as the worked example).
- **Control selection:** match control to task (numeric input for numbers, native device pickers for dates,
  radios for 2–3 options, dropdowns only when many); **device-native controls** ease both UX and dev build.
- **Copy discipline:** active voice, **terminology lock** (call it "cart" everywhere; "sign in/out",
  "sign up"), human language ("add customer" not "create customer record").
- **Icon discipline:** consistent set **+ text label always**, never text inside an icon, test ambiguity.
- **Testing:** **5 users surface ~85 % of issues** (Nielsen), test early with paper, re-test payment flows.

### (b) Critical take
- **~60 % operational gold, ~30 % dated/preachy, ~10 % gaps.** The form / journey / defaults / copy /
  obvious-easy-possible material is **still world-class and largely absent-as-a-named-framework from our
  engine.** Dated/filler: "mobile-first is novel," splash-screen and brand-doesn't-matter sermons,
  password-managers-are-rare. Gaps (2026): no tokens, no component API, no AI/agent UX, accessibility is
  contrast + labels only (no WCAG 2.2, focus-visible, target-size 2.5.8, reduced-motion, cognitive).
- **vs doctrine:** like all six, silent on distinctiveness and sourcing authority — but **uniquely strong on
  interaction *correctness* patterns** our engine under-specifies as *named* frameworks. The dark-pattern
  chapter is moral, not operationalisable — but it **CONFIRMS** the ethics direction of Phase-2's
  `design-ethics-and-anti-dark-patterns`.

### (c) Engine impact — second-highest yield after book 3
- **Harden** `04…/form-ux-design` with the **payment-form distillation** (single card field + auto-space)
  and the **forgiveness rules** (strip spaces / flexible formats / case-insensitivity). The skill already
  has validate-on-blur, label-above, error-message-triad — book 6 *adds the payment + forgiveness layer.*
- **Harden** `04…/interaction-design-patterns` with **Obvious/Easy/Possible** (a clean companion to the
  Tidwell set we already carry) and the **undo + toast (5–10 s)** recoverability spec (extends Tidwell
  "Safe Exploration / Multi-Level Undo").
- **Harden** `04…/navigation-and-information-architecture` + (Phase-2) `journey-mapping-and-service-design`
  with **journey signposting + completion messages + stage awareness.**
- **Harden** `10…/ux-writing-and-microcopy` with **terminology lock + active voice + human-language**;
  harden `11…/iconography-system-design` with **icon + always-a-label, test ambiguity.**
- **CONFIRMS** Phase-2 `ecommerce-and-checkout-ux` (the products→basket→checkout standard + guest checkout),
  `journey-mapping-and-service-design`, and `design-ethics-and-anti-dark-patterns`.
- **CHANGES:** lift every accessibility claim in anything this book touches from "contrast + labels" to the
  **WCAG 2.2** bar already owned by `accessibility-wcag-2-2-compliance` (target-size 2.5.8, focus-visible,
  redundant-entry 3.3.7, accessible-auth 3.3.8, reduced-motion).
- **REDUNDANT now:** typography hierarchy (2 faces / 16 px / 1.5), 5-users testing, contrast minimums,
  validate-on-blur, label-above — **already in the engine.**
- **No new skill** — but justifies a `references/payment-and-forgiveness-patterns.md` under `form-ux-design`
  and an `Obvious/Easy/Possible` section in `interaction-design-patterns`.

---

## Cross-cutting verdicts

- **Net-new skills justified by these six books: zero.** Our 52 skills already span every territory the
  books touch; the gap-analysis (doc 04) and Phase-2 P1 wave already name the only genuinely missing pieces
  (`component-states-and-interaction-fidelity`, `journey-mapping`, `ecommerce-and-checkout-ux`,
  `figma-and-tooling-workflow`, etc.). **These books *supply worked content* for those planned items —
  they do not expand the plan.**
- **Highest-yield → lowest-yield:** **Book 3 (components)** and **Book 6 (101 UX principles)** carry almost
  all the durable extract; **Book 1** contributes two clean mental models; **Books 2, 4** contribute a
  handful of numeric tells (and one inoculation target each); **Book 5** contributes effectively nothing
  new.
- **Inoculation targets (contradict the doctrine — cite as "what primers wrongly recommend"):** Book 4's
  glassmorphism/neumorphism advocacy; Book 2's "red=destructive/blue=normal," hamburger-boosts-conversion,
  and shadow-only dark-mode elevation; the whole set's "ship the safe convergent look" default and their
  silence on sourcing authority.
- **Universal upgrade applied on every extract:** raise accessibility to **WCAG 2.2**, add **motion/reduced-
  motion + focus model**, express spacing/colour as **tokens**, and require the **anti-slop + distinctive-by-
  design pre-flight** the books never reach.

---

## Consolidated "extract-into" table

| # | Book | Extract (specific) | Engine target | Action |
|---|------|--------------------|---------------|--------|
| 1 | Web UI for the Human Eye | External/internal/tactical **consistency model** | `00…/design-audit`, `…/visual-product-slop-audit` | Harden (new audit lens; ref) |
| 2 | Web UI for the Human Eye | Tactical/strategic/site-specific **pattern taxonomy** + affordance/signifier vocab | `04…/navigation-and-information-architecture`, `04…/interaction-design-patterns` | Harden |
| 3 | Web UI for the Human Eye | Competitive **heuristic spider-web** (pre-design) | `05…/ux-research-and-usability-testing`; Phase-2 `heuristic-evaluation-and-design-critique` | Harden / CONFIRMS |
| 4 | 101 Dos & Don'ts | **2× button padding**, **concentric border-radius**, soft-shadow defaults | `04…/practical-ui-design` → new `references/ui-numeric-tells.md` | Harden (ref) |
| 5 | 101 Dos & Don'ts | Right-align numerics | `12…/data-visualization`, `13…/docx`+`xlsx` tables | Harden |
| 6 | 101 Dos & Don'ts | Inoculation: hamburger-conversion, red/blue semantics, shadow-only dark elevation | `doctrine/references/ai-slop-taxonomy.md` (cite) | Inoculate |
| 7 | Better UI Components | Per-component **anatomy numbers** (button/card/dropdown/modal/search/hero/pricing) | new `references/component-anatomy-numbers.md` under `09…/component-library-architecture` | Harden (ref) |
| 8 | Better UI Components | Per-component **state lists** | Phase-2 `04…/component-states-and-interaction-fidelity` | **CONFIRMS + supplies content** |
| 9 | Better UI Components | **Card spacing triad** 16-24 / 16-40 / 64-96 | `03…/layout-grid-and-spacing`, `04…/practical-ui-design` | Harden |
| 10 | Better UI Components | **F vs Z hero scanning**, tease-past-fold | `04…/landing-page-and-conversion-design` | Harden (as heuristic) |
| 11 | Better UI Components | Charm pricing / scarcity / sticky compare | Phase-2 `06…/ecommerce-and-checkout-ux` | CONFIRMS |
| 12 | Fundamentals of UI/UX | **Halation** (physical reason to avoid pure #000/#FFF) | `04…/practical-ui-design`, `02…/color-system-and-palette` | Harden |
| 13 | Fundamentals of UI/UX | Dark-mode "white-shadow" mistake catalogue | `02…/dark-mode-and-theming` | Harden (CONFIRMS) |
| 14 | Fundamentals of UI/UX | Rule-of-thirds / F-Z / visual-weight factors | Phase-2 `03…/composition-and-visual-hierarchy` | Feeds (as heuristic under doctrine) |
| 15 | Fundamentals of UI/UX | Inoculation: glassmorphism/neumorphism as "best practice" | `doctrine/references/ai-slop-taxonomy.md` (cite) | Inoculate |
| 16 | 45-Minute Guide | Tool list is stale (Axure/Sketch/XD) | Phase-2 `09…/figma-and-tooling-workflow` | **CHANGES** — build Figma-variables/dev-mode-current |
| 17 | 45-Minute Guide | 5-users×3-rounds, reading-grade levels | `05…/ux-research-and-usability-testing` | CONFIRMS (citation only) |
| 18 | 101 UX Principles | **Payment-form distillation** + **forgiveness rules** | `04…/form-ux-design` → new `references/payment-and-forgiveness-patterns.md` | Harden (ref) |
| 19 | 101 UX Principles | **Obvious / Easy / Possible** framework | `04…/interaction-design-patterns` | Harden (section) |
| 20 | 101 UX Principles | **Undo + toast (5–10 s)** recoverability spec | `04…/interaction-design-patterns`, `04…/empty-error-and-loading-states` | Harden |
| 21 | 101 UX Principles | **Journey signposting + completion messages** | `04…/navigation-and-information-architecture`; Phase-2 `journey-mapping-and-service-design` | Harden / CONFIRMS |
| 22 | 101 UX Principles | **Terminology lock + active voice + human language** | `10…/ux-writing-and-microcopy` | Harden |
| 23 | 101 UX Principles | Icon **+ always a label**, ambiguity-test | `11…/iconography-system-design` | Harden |
| 24 | 101 UX Principles | **Defaults intelligence** (Pareto top-20 % journeys) | Phase-2 `05…/journey-mapping-and-service-design`, `06…/ecommerce-and-checkout-ux` | CONFIRMS |
| 25 | 101 UX Principles | Dark-pattern stance (moral) | Phase-2 `00…/design-ethics-and-anti-dark-patterns` | CONFIRMS |
| 26 | All six | Raise a11y → **WCAG 2.2**; add **motion/reduced-motion + focus model**; express as **tokens**; require **distinctive-by-design pre-flight** | every hardened skill above | **CHANGES** (universal upgrade) |

**Plan-status summary:** the six books **CONFIRM** Phase-2 items `component-states-and-interaction-fidelity`,
`ecommerce-and-checkout-ux`, `journey-mapping-and-service-design`, `heuristic-evaluation-and-design-critique`,
`composition-and-visual-hierarchy`, and `design-ethics-and-anti-dark-patterns` (and supply their worked
content); they **CHANGE** `figma-and-tooling-workflow` (must be Figma-variables/dev-mode-current, not the
books' Axure/Sketch/XD era) and impose a **universal WCAG-2.2 + motion + tokens upgrade** on every extract;
and they make **no Phase-2 item REDUNDANT** while themselves justifying **no net-new skill** — their craft is
already covered by the existing 52.
