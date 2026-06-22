# Reference: Micro-Interaction Anatomy

The per-control feedback layer. The **global** motion law (durations, easing curves, spring
presets, the GPU-only property list, and the canonical `prefers-reduced-motion` strategy) lives in
`../motion-design/SKILL.md` and is **not** restated here — this file is what that law applies *to*.

Source basis: Dan Saffer, *Microinteractions* (the trigger/rules/feedback/loops model); Don
Norman, *The Design of Everyday Things* (signifiers / affordances); Material Design 3 states;
Apple HIG — Feedback & Haptics. Inoculations per `doctrine/references/ai-slop-taxonomy.md`.

---

## 1. The four-part anatomy (Saffer)

Every micro-interaction decomposes into four layers. Name all four *before* choosing any timing —
if you cannot, you are decorating, not designing feedback.

| Layer | Question it answers | Example (notification toggle) |
|---|---|---|
| **Trigger** | What starts it? (user action *or* system event) | User taps the switch; or a system event flips it (settings synced from another device). |
| **Rules** | What can/can't happen, and in what order? | Tapping flips on↔off; disabled while the first fetch is pending; cannot be on without permission granted. |
| **Feedback** | How does the user know what happened? | Thumb slides, track colour changes, light haptic, AT announces the new state. |
| **Loops & Modes** | What happens over time / on repeat / in special cases? | Stays on until changed (loop = persistent); "error" mode if the server rejects; long-loop = it remembers the last state next session. |

**Triggers come in two kinds.** *Manual* (user-initiated — tap, drag, key, focus) and *system*
(time, data arrival, another device). System triggers still need feedback, and that feedback must
not look identical to a user-initiated one or the user will think they did it.

**Rules are the logic you must surface.** If a rule forbids an action, the feedback layer shows it
(disabled state, inline message) — never let the control silently no-op.

---

## 2. Feedback principles

- **Feedback confirms the trigger fired and conveys the new state** — and nothing more. It is the
  least amount of signal that answers "did it work / what is it now."
- **Use the least-effort channel.** Visual is default; add haptic/sound only when it carries
  meaning the eye would miss (off-screen, hands-busy, accessibility).
- **Never colour-alone** (WCAG 1.4.1). On/off, valid/invalid, selected/unselected must also differ
  by position, shape, icon, fill, or text — colour is a reinforcement, never the sole carrier.
- **Honest latency.** Under ~80 ms feels instant — no loader. Past that, show progress. Never show
  a "done" state while the work is still in flight unless you are being *optimistic* (§4) and have
  a rollback.
- **Feedback per state.** Each state in the table below earns its own resolved feedback; the easy
  ones to forget are `focus-visible` (keyboard) and `disabled` (no motion, reduced opacity).

### Canonical control states
| State | Trigger | Feedback note |
|---|---|---|
| `rest` | — | The authoritative idle look. |
| `hover` | pointer enters | Pointer-only; never the *only* invitation (no hover-as-primary — see §6). |
| `focus-visible` | keyboard focus | Visible ring ≥ 3:1 contrast (WCAG 2.4.7/2.4.13). |
| `pressed`/`:active` | pointer/key down | Press feedback, e.g. `scale(0.96–0.97)`, 100 ms (motion-design §4.2). |
| `active`/`checked`/`on` | committed | The new persisted state; spring settle ζ ≥ 0.7. |
| `loading` | server round-trip > 80 ms | Inline progress, control stays in place. |
| `disabled` | rule forbids | ~40% opacity, no motion, still exposes state to AT (4.1.2). |
| `error` | rule violated / server reject | Non-spatial signal + recovery copy (§4). |

---

## 3. Feedback channels — pick semantically

| Channel | Strength | Use for | Never |
|---|---|---|---|
| **Visual (motion)** | precise, always available | state change, press, confirm | bouncy overshoot; animating everything |
| **Visual (static)** | accessible, reduced-motion-safe | the resting truth of each state | relying on colour alone |
| **Haptic** | eyes-free, intimate | discrete confirmations, selection ticks, success/warn/error | continuous buzz; decorative taps |
| **Sound** | eyes-free, ambient | optional reinforcement, accessibility | default-on; the only signal |

Channels must **reinforce one outcome**, not conflict. A success haptic with an error colour is a
bug. The control must stay fully usable with **haptics and sound disabled** (they are enhancements).

### Haptic pairing table (semantic, never decorative)
| Outcome | iOS (UIFeedbackGenerator / SwiftUI) | Android | Rule |
|---|---|---|---|
| Selection change (toggle, segment, picker tick) | `.selection` / `.impact(.light)` | `HapticFeedbackConstants.CLOCK_TICK` / light | One tick per discrete change, not per pixel. |
| Success (saved, sent, completed) | `.notification(.success)` | `CONFIRM` | Only on genuine success. |
| Warning (recoverable issue) | `.notification(.warning)` | `REJECT` (soft) | Pair with visible warning. |
| Error (action failed) | `.notification(.error)` | `REJECT` | Pair with visible error + recovery copy. |
| Impact / press landing | `.impact(.light/.medium)` | `KEYBOARD_TAP` | Match weight to the control's significance. |

Verify the experience with haptics off; never gate required feedback on a haptic alone.

---

## 4. Optimistic feedback (the contract)

For **server-backed** actions, don't make the user wait on the network to feel progress.

```
Trigger → apply new state INSTANTLY in UI  ┐
         fire request in background         │  user sees success immediately
         on success: reconcile (usually no-op)
         on FAILURE: roll back the state + non-spatial error signal + recovery copy
```

Rules:
- **Always define the rollback.** Optimistic-without-rollback silently diverges from server truth —
  banned. The failure path is part of the spec, not an afterthought.
- **Roll back visibly but calmly** — revert the state instantly (no spatial animation), show an
  inline error and a retry; under reduced motion, drop any shake and rely on colour+icon+text.
- **Only be optimistic when the success rate is high and rollback is cheap.** For destructive or
  rare-success actions, show a real pending state instead.
- Local, authoritative actions (a client-side toggle) are *not* optimistic — they are simply
  instant; no rollback path needed.

See `motion-design` §7 (Perceived Performance / Optimistic Updates) for the timing rationale.

---

## 5. Signifiers (hint animations) — sparingly, once

A **signifier** (Norman) makes an affordance *discoverable* — a small motion that says "this can be
acted on." It is the opposite of feedback (which follows an action); a signifier *precedes* it.

Rules:
- Fire **once** — on first visit, on idle, or after a dwell — never an infinite loop on a primary control.
- **Interruptible and non-blocking**: any real input cancels it immediately.
- **Subtle**: a small nudge, peek, or single pulse — `transform`/`opacity` only, inside the feedback timing band.
- Obeys `prefers-reduced-motion`: replace with a static affordance (visible handle, arrow, label).
- If a control needs a perpetual pulse to be found, the control is wrong — fix the affordance, don't loop motion.

---

## 6. Loops & Modes, and the inoculations

- **Loops** define duration/repetition: how long the state persists, what happens on the Nth
  interaction (long loops can change behaviour — e.g. an easter egg only after repeated use).
- **Modes** are special states (error mode, empty mode) — keep them rare; a mode the user enters by
  accident is a design smell.

**Inoculate explicitly** (`doctrine/references/ai-slop-taxonomy.md`):

| Tempting pattern (and where it's taught) | Why rejected | Doctrine-correct alternative |
|---|---|---|
| `ease-*-back` / bouncy overshoot interpolators (*App Design Apprentice*) | Violates ζ ≥ 0.7 no-bounce; #1 AI animation fingerprint | Spring in the no-bounce band; if a "pop" is wanted, ζ≈0.7–0.75, never elastic |
| Everything animates / perpetual pulse (animation fatigue) | Convergent slop tell; motion becomes noise | Motion only on state change + confirmation; rest is still |
| Colour-only on/off or valid/invalid | WCAG 1.4.1 failure | Pair colour with position/shape/icon/text |
| Decorative haptics on every tap | Cheapens the signal; ignores haptics-off users | Semantic haptics only; usable with haptics disabled |
| Hover-as-primary invitation (*Designing Web Interfaces*, 2009) | No touch equivalent | Visible tap-operable affordance first; hover is enhancement |

---

## 7. Delight moments (rare, additive, dismissible)

A celebratory flourish (success burst, achievement settle) is permitted **at most once per
meaningful milestone**:
- It is **additive** — the action already succeeded without it; removing it loses nothing functional.
- **≤ ~400 ms**, off the hot path, never blocking the next action.
- **Fully replaced under reduced-motion** (a quiet static confirmation, not a stripped blank).
- No flashing > 3×/s (WCAG 2.3.1).
- If users see it on every routine action, it is no longer delight — it is fatigue. Reserve it.
