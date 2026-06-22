---
name: inclusive-and-assistive-design
description: Use when you want to go BEYOND the WCAG 2.2 AA floor into genuinely inclusive, assistive-tech-friendly design — accommodating cognitive load and memory limits, low vision (zoom/spacing/dyslexia-friendly options), motor differences (large targets, switch/voice/dwell), screen-reader and magnifier compatibility, and situational or temporary impairments (one-handed, bright sun, noisy room, broken arm, slow connection). Triggers on "make this inclusive", "who are we excluding?", "plain-language pass", "reduce cognitive load", "support switch/voice/dwell users", "low-vision/dyslexia options", "persona spectrum", "exclusion audit", "inclusive design pass", or designing for ability ranges rather than a single able-bodied default. Pairs with `accessibility-wcag-2-2-compliance` (that skill certifies the legal floor; THIS one designs the experience above it).
status: active
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
    - claude-code
    - codex
---

# Inclusive & Assistive Design (Beyond the WCAG Floor)

WCAG 2.2 AA is the **floor, not the ceiling.** A product can pass every success
criterion and still exclude people: text that is technically contrast-compliant but
cognitively dense; targets that hit the 24px minimum but punish a tremor; flows that meet
3.3.7 but still overload working memory; markup that is screen-reader-valid but
screen-reader-*hostile*. This skill is the deliberate pass **above** the floor — it
designs for the full human range, using the **persona spectrum / exclusion** model from
Microsoft Inclusive Design.

The companion skill `accessibility-wcag-2-2-compliance` operationalizes and certifies the
**legal/technical floor** ([`doctrine/references/wcag-2.2-criteria.md`](../../../doctrine/references/wcag-2.2-criteria.md)).
**Run that to know you pass; run THIS to design something people with a range of abilities
can actually, comfortably use.** They are a pair — never substitute one for the other.

This is doctrine, not decoration: §0 of [`doctrine/design-doctrine.md`](../../../doctrine/design-doctrine.md)
says the moat is work that looks **authored by a skilled human**. Designing for the people a
templating tool forgets is exactly that signature — and §3 places accessibility/inclusion in
`00-cross-cutting-ops-qa-a11y` to **co-activate with every group, never skip.**

<!-- dual-compat-start -->
## Use When
- A request asks to go **beyond compliance**: "make it inclusive", "who can't use this?",
  "reduce cognitive load", "plain-language this", "support low-vision/dyslexic users",
  "make it work for switch/voice/dwell", "run an exclusion audit", "persona spectrum".
- Designing or reviewing a **flow** (onboarding, checkout, claim, booking, form-heavy task)
  where memory load, error recovery, reading level, or time pressure could exclude people.
- Deciding **accommodations and options** above the minimums — adjustable text spacing, a
  reading mode, a dyslexia-friendly toggle, large/comfortable targets, dwell/switch support,
  "save and resume", reduced-motion *and* reduced-cognitive-load modes.
- You need to think about **situational and temporary** impairments (one hand on a phone,
  glare outdoors, a noisy room, a sprained wrist, a new-parent's sleep-deprived attention,
  a slow/expensive connection) — not just permanent disability.
- Verifying real **assistive-technology compatibility** (screen readers, screen magnifiers,
  voice control, switch access, OS dyslexia/reading tools) as an *experience*, not a checkbox.

## Do Not Use When
- You only need to **certify the WCAG 2.2 AA floor** (focus order, ARIA, target-size minimum,
  audit sheet) → `accessibility-wcag-2-2-compliance`. This skill assumes that floor is met and
  builds on top of it.
- The work is purely **colour contrast ramps / colour-blind-safe palettes** →
  `02-color-brand-and-visual-identity/accessible-color-and-contrast` (this skill cites it for
  low-vision/contrast but does not own palette construction).
- The work is **microcopy/error wording mechanics** → `10-content-design-and-ux-writing`
  (this skill sets the *plain-language and cognitive-load targets*; that skill crafts the words).
- The work is **performance budgets / Core Web Vitals** → `performance-as-ux-and-core-web-vitals`
  (this skill flags *slow/expensive connection* as a situational exclusion and hands off).
- You need the **final pre-launch gate** that composes a11y + slop + perf →
  `design-qa-and-pre-launch-review`.

## Required Inputs
- The flow or screen under work, end to end, with its **real tasks and goals** (what is the
  user actually trying to finish, under what pressure, in what context).
- Who it serves: the realistic **range of abilities, contexts, devices, and connection quality**
  — including the people usually left out of the default "able-bodied, focused, fast Wi-Fi" persona.
- Confirmation that the **WCAG 2.2 AA floor is already met or in progress** (this skill builds
  above it; it does not re-do it).
- Any constraints: brand voice, regulated content that limits plain-language rewrites, platform
  assistive-tech available for testing (VoiceOver/NVDA/TalkBack, OS magnifier, Voice Control/Voice
  Access, Switch Control/Switch Access, dwell control).

## Workflow

### A. Find the exclusions (persona spectrum first)
1. **Frame each ability as a spectrum, not a binary.** For every ability dimension —
   cognitive, vision, motor/dexterity, hearing, speech — Microsoft's model spans
   **permanent → temporary → situational**: e.g. one arm (permanent) · arm injury
   (temporary) · holding a baby (situational); blind · cataract/post-surgery · bright sun;
   non-verbal · laryngitis · heavy accent on voice control. **Designing for the permanent
   end serves the far larger temporary/situational population too.** See
   `references/inclusive-patterns.md` §Persona spectrum.
2. **Run an exclusion audit on the real flow.** Walk each step and ask, per dimension, *who
   gets stuck or shut out here, and why* — then record it. Mismatched interactions, not
   "disabilities", are the exclusions. Use the table in `references/inclusive-patterns.md`
   §Exclusion audit and the worked example.
3. **Recruit the spectrum, not the average.** Validate with people at the edges (a
   screen-reader user, someone with dyslexia, a switch user, someone on a 3G phone in
   sunlight) — solutions that work at the edges work for everyone in the middle.

### B. Accommodate above the floor (by ability dimension)
4. **Cognitive accessibility.** Reduce the three loads:
   - **Plain language** — short sentences, common words, active voice; target a reading age
     well below your audience's ceiling (often ~Grade 8 / lower secondary). Front-load the
     point. (Hand wording to `10-content-design-and-ux-writing`; set the *target* here.)
   - **Memory load** — don't make people hold things in their head. Persist entered data,
     show a summary before commit, keep instructions visible *next to* the step (not on a
     prior screen), prefill the known (extends WCAG 3.3.7 well past the minimum).
   - **Error tolerance** — make mistakes cheap and recoverable: confirm destructive actions,
     allow undo, **save-and-resume**, forgiving input parsing (accept spaces in card numbers,
     any phone format), inline help *before* the error, recovery guidance *in* the error.
   See `references/inclusive-patterns.md` §Cognitive.
5. **Low vision (beyond contrast minimums).** Passing 4.5:1 is not enough.
   - **Zoom/reflow past the floor** — usable not just at 200% (the WCAG floor) but at **400%**
     and OS text-enlargement; no truncation, no clipped controls, no horizontal scrolling of
     body text.
   - **Spacing as an affordance** — respect user text-spacing overrides (line-height ≥1.5,
     paragraph spacing, letter/word spacing) without breaking layout (WCAG 1.4.12 is the floor;
     design *comfortably* above it).
   - **Reading & dyslexia-friendly options** — offer a clean reading mode; let users pick a
     dyslexia-friendly face and looser spacing; never justify body text; avoid pure-black-on-
     pure-white glare (offer a softer/dark theme). Choose typefaces per the engine's font
     doctrine (no banned defaults).
   See `references/inclusive-patterns.md` §Low vision.
6. **Motor / dexterity.** Above the 24px minimum:
   - **Large, comfortable targets** with generous spacing; aim 44×44px (HIG) / 48dp (Material)
     as the *comfortable* norm, larger for primary actions and for tremor/one-handed use.
   - **Forgiving interactions** — no precision-required drags (always a tap/click/key path,
     extending WCAG 2.5.7); no hover-only reveals; generous click areas; no tight time limits.
   - **Switch, voice, and dwell** — ensure a logical single-switch scan order, that every
     action has a stable visible/spoken label voice control can target, and that nothing
     requires a sustained gesture a dwell user can't make.
   See `references/inclusive-patterns.md` §Motor.
7. **Assistive-tech compatibility as an experience.** Valid ARIA is necessary but not
   sufficient. Walk the flow with **screen readers** (sensible reading order, useful headings,
   announced changes, no chatter), a **screen magnifier** (does focus/important feedback appear
   where the zoomed viewport is looking?), **voice control** (is every control's visible name
   speakable and matched?), and **switch/dwell**. See `references/inclusive-patterns.md`
   §Assistive-tech.
8. **Situational & temporary design.** Make the default robust: one-handed reach zones, works
   in glare (don't rely on subtle contrast), works muted (don't rely on sound alone),
   works on a slow/expensive connection (lightweight, resilient, offline-tolerant — hand the
   budget to `performance-as-ux-and-core-web-vitals`), works when tired/distracted (low memory
   load, clear next step). See `references/inclusive-patterns.md` §Situational.

### C. Decide, document, hand off
9. **Prefer one robust default over a pile of toggles.** Bake inclusion into the baseline
   (large targets, plain language, persisted data); add *options* (reading mode, dyslexia
   face, theme) only where one default genuinely can't serve everyone. Honour OS/user settings
   (reduced motion, larger text, high contrast, dark mode) rather than reinventing them.
10. **Record exclusions found → accommodations made**, and route each to its owner
    (contrast → `accessible-color-and-contrast`; wording → content design; budget → perf;
    floor criteria → `accessibility-wcag-2-2-compliance`). Use `examples/inclusive-design-pass.md`
    as the template.

## Anti-Patterns
- **Treating WCAG AA as "done".** Passing the floor while the flow is still dense, forgetful,
  precision-demanding, or screen-reader-hostile. The floor is the start of this skill, not the end.
- **Binary thinking** ("disabled vs not") instead of the spectrum — ignoring the huge
  temporary/situational population that the permanent-end fix would also serve.
- **Accessibility-overlay / toggle theatre** — a widget that claims to "make the site
  accessible" instead of fixing the underlying design; a wall of switches no one finds.
- **Cognitive overload dressed as features** — jargon, walls of text, multi-step flows that
  demand holding values in your head, dead-end errors with no recovery.
- **Contrast-compliant but unreadable** — meeting 4.5:1 while justifying text, cramming
  line-height, glare-white backgrounds, and ignoring text-spacing overrides.
- **Minimum-size targets crammed together** — hitting 24px on paper but punishing a tremor or
  a thumb; hover-only or drag-only interactions with no forgiving path.
- **"Screen-reader valid" ≠ usable** — correct ARIA that still reads as noise, with no headings,
  no announced changes, or a nonsensical order. Magnifier/voice/switch never tested.
- **Designing only for the able-bodied, focused, fast-connection persona** — the convergent
  default this skill exists to break.
- **Banned default fonts / lorem** in any inclusive option (reading mode, dyslexia face) —
  still subject to the Anti-Slop Charter.

## Outputs
- An **exclusion audit** of the flow (per ability dimension, across permanent/temporary/
  situational), naming who is shut out and where.
- A matched set of **accommodations above the floor** — cognitive, low-vision, motor,
  assistive-tech, situational — baked into the default where possible, offered as options
  where necessary, each routed to its owning skill.
- A short **inclusive-design pass record** (exclusions found → accommodations made) suitable
  for handoff to `design-qa-and-pre-launch-review` alongside the WCAG audit sheet.

## Examples
- `examples/inclusive-design-pass.md` — a **worked inclusive-design pass on a real flow**
  (a utility-bill payment / account top-up). Runs the persona spectrum, finds concrete
  exclusions per ability dimension, and lists the accommodation made for each — going above
  the WCAG floor that `accessibility-wcag-2-2-compliance` certifies.

## References
- [`doctrine/design-doctrine.md`](../../../doctrine/design-doctrine.md) — the cross-cutting
  charter; §0 (authored-by-a-human moat), §2 (Anti-Slop Charter — applies to any inclusive
  font/option), §3 (this skill lives in `00-cross-cutting-ops-qa-a11y`, co-activates with every group).
- [`doctrine/references/wcag-2.2-criteria.md`](../../../doctrine/references/wcag-2.2-criteria.md)
  — the **floor** this skill builds above (target-size 24px, reflow at 200%/320px, 3.3.7
  redundant entry, 2.5.7 dragging, contrast minimums). We exceed these, not restate them.
- `references/inclusive-patterns.md` — the accommodation playbook organised **by ability
  dimension** (cognitive, low vision, motor, assistive-tech, situational), plus the persona
  spectrum and exclusion-audit method.
- **Pairs with** `00-cross-cutting-ops-qa-a11y/accessibility-wcag-2-2-compliance` — that skill
  certifies the floor (run it first/alongside); this skill designs the experience above it.
- Hands off to `02-color-brand-and-visual-identity/accessible-color-and-contrast` (low-vision
  contrast/themes), `10-content-design-and-ux-writing` (plain-language wording),
  `performance-as-ux-and-core-web-vitals` (slow-connection budget), and
  `design-qa-and-pre-launch-review` (final gate).
<!-- dual-compat-end -->
