---
name: micro-interactions-and-feedback
description: Use when designing or reviewing per-control feedback — button press, toggle/switch,
  text input, checkbox/radio states, signifier (hint) animation, and the occasional delight moment.
  Covers the trigger → rules → feedback → loops anatomy, optimistic feedback with rollback, haptic
  pairing, and how to keep feedback honest and non-AI-slop. Pairs with `motion-design` (which owns
  the global timing/easing/spring/reduced-motion law); this skill owns the control-level feedback layer.
status: active
metadata:
  portable: true
  category: 08-motion-and-interaction
  compatible_with:
    - claude-code
    - codex
---

# Micro-Interactions & Feedback

<!-- dual-compat-start -->
## Use When
- Specifying the feedback for a single control: button, toggle/switch, text input, checkbox/radio, segmented control, slider, like/save action.
- Designing a **signifier animation** — a small hint that makes an affordance discoverable (a nudge, a pulse, a peek).
- Adding a **delight moment** (success burst, achievement settle) and you need to keep it sparing and dismissible.
- Wiring **optimistic feedback** (apply state instantly, reconcile with the server later) and its rollback path.
- Pairing motion with **haptics / sound** so the channels reinforce one outcome rather than fight.
- Reviewing an interaction for the trigger → rules → feedback → loops anatomy and for the bounce / animation-fatigue slop tells.

## Do Not Use When
- You need the **global motion law** — duration tables (100/300/500), easing-vs-spring decision, GPU-property list, or the canonical `prefers-reduced-motion` strategy. That is `../motion-design/SKILL.md` (this skill defers to it and never restates it).
- The work is **page/route/view transitions or staggered entrances** → `../motion-design` (§4.3–4.4, View Transitions).
- The work is **microcopy / error-message wording** → `../../10-content-design-and-ux-writing/`.
- The work is **visual styling of the control at rest** (colour, type, spacing, shape) → `../../04-web-and-ui-design/` or the token/theming group.

## Required Inputs
- The control and its **complete state set** (rest, hover, focus-visible, pressed, active/checked, disabled, loading, error).
- Whether the action is **local** (instant, authoritative) or **server-backed** (needs optimistic + rollback).
- Target platforms (web / iOS / Android) and whether **haptics** are available and appropriate.
- The motion budget and tokens already set by `motion-design` (timing scale, spring presets, easing curves).

## Workflow
1. **Map the anatomy.** For the control, write out the four layers — **Trigger → Rules → Feedback → Loops & Modes** — before any timing. See `references/micro-interaction-anatomy.md`. If you cannot name the trigger and the rule, you are decorating, not designing feedback.
2. **Inherit the motion law.** Pull duration/easing/spring/reduced-motion from `../motion-design/SKILL.md`. Feedback sits in the **100–150 ms** band (press/toggle/hover); settle/confirm uses a **spring with ζ ≥ 0.7 (no visible bounce)**, default ζ = 1.0. Animate `transform` + `opacity` only.
3. **Define every state's feedback**, including `focus-visible` (keyboard) and `disabled` (no motion). Feedback must never be **colour-alone** — pair it with shape/icon/position/text (WCAG 1.4.1).
4. **Pick the feedback channel(s)** — visual, haptic, sound — and make them **semantic and redundant**: success haptic only for success, selection haptic only for selection changes. The control must remain fully usable with haptics/sound disabled (`doctrine/references/wcag-2.2-criteria.md`).
5. **Decide optimistic vs. confirmed.** Server-backed actions apply state instantly, fire the request in the background, and **roll back only on rejection** with a non-spatial error signal + recovery copy. Local actions skip the round-trip.
6. **Signifiers, sparingly.** A signifier animation may run **once** (or on idle/first-visit), must be interruptible, must never block input, and must obey reduced-motion. Never loop a "look-at-me" pulse on a primary control.
7. **Delight, even more sparingly.** At most one celebratory flourish per meaningful milestone; it is additive (the action already succeeded without it), ≤ ~400 ms, never on the hot path, and fully replaced under reduced-motion.
8. **Write the spec** as a state table + motion timeline + reduced-motion replacement + platform parity (see `examples/`). Run the acceptance checklist.

## Anti-Patterns
- **`ease-*-back` / bouncy overshoot interpolators** (the App Design Apprentice habit). They violate the engine's **ζ ≥ 0.7 no-bounce** rule and are the #1 AI animation fingerprint (`doctrine/references/ai-slop-taxonomy.md`). Use a spring in the no-bounce band; if you want a "pop", cap it at ζ≈0.7–0.75 (barely perceptible), never elastic.
- **Animation fatigue** — every control pulsing, bouncing, or flourishing. Feedback that is always on is noise; reserve motion for state change and confirmation.
- **Colour-only feedback** (green = on, red = error with no other cue). Fails WCAG 1.4.1 and colour-blind users.
- **Decorative haptics / fake loaders** — buzzing on every tap, or a spinner that runs after the work is already done. Haptics must map to outcomes; loaders only appear past the ~80 ms threshold.
- **Optimistic feedback with no rollback** — showing success then silently diverging from server truth. Always define the rejection path.
- **Looping signifiers** that never stop, or delight that blocks the next action.
- **Feedback that lies about latency** — instant "done" checkmark while the request is still in flight with no reconciliation.

## Outputs
- A per-control **micro-interaction spec**: anatomy (trigger/rules/feedback/loops), state table, motion timeline (timing + easing/spring), channel map (visual/haptic/sound), optimistic + rollback path, reduced-motion replacement table, platform parity, and an acceptance checklist.

## Examples
- `examples/toggle-switch-feedback-spec.md` — a worked notification-toggle spec: full anatomy, every state, spring settle (ζ≈0.75, no bounce), optimistic update with rollback, haptic pairing, and a considered `prefers-reduced-motion` replacement. Never lorem.

## References
- `references/micro-interaction-anatomy.md` — the trigger → rules → feedback → loops model, the feedback-channel decision, signifier rules, optimistic-feedback contract, and the haptic-pairing table.
- `../motion-design/SKILL.md` — **the owning motion law**: timing (100/300/500), easing vs spring, ζ ≥ 0.7 no-bounce, GPU-only properties, and the canonical `prefers-reduced-motion` strategy. This skill defers to it.
- `doctrine/design-doctrine.md` — the anti-slop charter; over-animated or bouncy feedback is a slop tell.
- `doctrine/references/ai-slop-taxonomy.md` — `ease-*-back`/overshoot and animation-fatigue tells to inoculate against.
- `doctrine/references/wcag-2.2-criteria.md` — accessibility floor: 2.3.3 (reduced motion), 2.3.1 (≤3 flashes/s), 1.4.1 (never colour-alone), 2.5.8 (target size), 4.1.2 (state exposed to AT).
<!-- dual-compat-end -->
