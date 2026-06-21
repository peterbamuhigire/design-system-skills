# Reference: iOS Sensory Feedback & Haptics (Core Haptics / SwiftUI sensoryFeedback)

How a native iOS app should *feel* in the hand: haptic feedback paired with sound and motion, used as
**confirmation and meaning**, never decoration. Use alongside `references/hig-liquid-glass.md` (the
visual material) and `doctrine/references/wcag-2.2-criteria.md` (Reduce Motion / motion safety).
Source: Apple HIG "Playing haptics," Core Haptics, UIFeedbackGenerator, and SwiftUI `sensoryFeedback`.

Haptics are the Taptic Engine's vocabulary. Done right, they make taps feel committed and state changes
feel real; done wrong (buzzing on every scroll tick, or firing on failure as if it were success) they
feel cheap and noisy — the tactile equivalent of slop.

---

## 1. The three feedback families (use the system patterns first)

Apple ships named, semantically-correct patterns. **Prefer these over custom Core Haptics** unless you
have a designed signature interaction. SwiftUI exposes them through `.sensoryFeedback(_:trigger:)`.

**Impact** — a physical collision / something locking into place. Weights:
- `.light` — small UI element snapping (e.g. a picker detent, a small toggle).
- `.medium` — a standard control engaging, a segmented switch.
- `.heavy` — a substantial element, a significant boundary hit.
- `.soft` / `.rigid` — texture variants (soft = cushioned, rigid = crisp) for fine-tuning feel.
- `.impact(weight:flexibility:)` / `.impact(intensity:)` for tuned cases.

**Notification** — the *outcome* of an operation. Three only:
- `.success` — operation completed (saved, sent, paid). Reassuring two-tap pattern.
- `.warning` — caution / recoverable problem.
- `.error` — operation failed. **Never** fire `.success` on a failed action — the haptic must tell the
  truth about the outcome, like the colour does.

**Selection** — a discrete value changed as the user moves through options:
- `.selection` — fires on each step of a picker/slider/segmented change. Light tick; do **not** fire on
  the *initial* value, only on change.

SwiftUI examples:
```swift
.sensoryFeedback(.success, trigger: didSubmit)        // on a successful save
.sensoryFeedback(.selection, trigger: selectedIndex)  // each picker step
.sensoryFeedback(.impact(weight: .medium), trigger: didToggle)
```

---

## 2. Mapping rules (semantics, not sprinkles)

- **Confirm meaningful state changes**, not every touch. A tap that does nothing structural (scrolling,
  hovering) gets no haptic. A commit (send, delete, pay, complete, lock) gets one.
- **Match the haptic to the truth of the event:** success→`.success`, failure→`.error`,
  caution→`.warning`. The haptic is a second, eyes-free channel of the same message the colour/copy carry.
- **Pair, don't double up.** One feedback per discrete event. Two generators firing together feel like a
  glitch. Coalesce.
- **Selection ticks accompany visible movement** (a value scrolling under the finger). Silent on first
  render.
- **Reinforce, never replace.** Haptics supplement the visual/auditory state — they are not the only
  signal (a user may have the phone on a table, or haptics disabled).

---

## 3. Custom Core Haptics (only for designed signatures)

For a branded, designed moment (a payment-complete flourish, a game beat), use Core Haptics:
- **Transient events** (`.hapticTransient`) — short taps; **continuous events** (`.hapticContinuous`) —
  sustained rumbles with envelopes.
- Parameters: `hapticIntensity` (0–1) and `hapticSharpness` (0 = dull/round → 1 = crisp/tight).
- Build patterns as `CHHapticPattern`; play via a `CHHapticEngine`. **Sync haptics with audio and visuals**
  on the same timeline so the three land together — Apple's "haptic + sound + motion" trinity.
- Check `CHHapticEngine.capabilitiesForHardware().supportsHaptics` and **degrade gracefully** on devices
  without a Taptic Engine (iPads, some hardware) — the visual state must stand alone.

---

## 4. Sound & motion partners

- **Sound:** keep it short, optional, and consistent with the haptic's meaning; never play sound without
  also respecting the silent switch and the user's volume. Sound is a partner to haptics, not a substitute.
- **Motion:** the visual confirmation (a check animating in, a row collapsing) should land on the **same
  frame** as the haptic. With Liquid Glass, the material's morph/shimmer can be the visual partner — but
  see Reduce Motion below.

---

## 5. Accessibility & system-setting rules (must honour)

- **Reduce Motion** — dampen or drop motion-tied flourishes. A haptic may still fire (it is not motion),
  but any required affordance must not depend on an animation. Cross-reference
  `wcag-2.2-criteria.md` (2.3.1 / `prefers-reduced-motion`).
- **System Haptics setting / disabled haptics** — the user can turn haptics off system-wide. Your UI must
  remain fully usable and legible with **zero haptics** — they are reinforcement, never the sole signal.
- **VoiceOver** — haptics complement, but the accessible name/role/value (4.1.2) and the visible/spoken
  state carry the actual meaning. Don't encode information only in a buzz.
- **Battery / overuse** — continuous haptics drain the Taptic Engine and annoy; reserve them for genuine
  signature moments.

---

## 6. Haptics quality gate (check before sign-off)

1. Every haptic maps to a **real, discrete event**; no haptics on inert taps or scroll.
2. **Outcome haptics tell the truth** — `.error` on failure, never `.success`.
3. **One** feedback per event; generators are coalesced, not stacked.
4. `.selection` fires on change only, accompanying visible movement.
5. Custom Core Haptics (if any) **sync with sound + motion** on one timeline and check hardware support.
6. UI is fully usable with **haptics disabled** and under **Reduce Motion**; no meaning lives only in a buzz.
7. Sound respects the silent switch and volume; motion partner respects Reduce Motion.
