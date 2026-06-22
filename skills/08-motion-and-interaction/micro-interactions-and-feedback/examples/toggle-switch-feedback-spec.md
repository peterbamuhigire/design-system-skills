# Worked Example: Micro-Interaction Spec — "Push Notifications" Toggle Switch

A fully specified per-control feedback spec — the artifact a designer hands engineering. It
exercises every rule this skill enforces: the **trigger → rules → feedback → loops** anatomy, every
state, a spring settle (no bounce), **optimistic feedback with rollback**, **haptic pairing**, and a
considered `prefers-reduced-motion` replacement. Timing/easing/spring law is inherited from
`../../motion-design/SKILL.md`; this spec applies it at the control level.

---

## Component
**Push-notifications switch** — a settings-row toggle that turns notifications on/off. The state is
**server-backed** (synced to the account), so it is optimistic with a rollback path. Targets: web
(CSS + WAAPI), parity notes for iOS/Android.

---

## Anatomy (the four layers — fill these in first)

| Layer | This control |
|---|---|
| **Trigger** | *Manual:* user taps/clicks/keys the switch. *System:* account sync flips it from another device (feedback must announce, not look self-triggered). |
| **Rules** | Tap flips on↔off. Disabled while the initial GET is pending. Cannot turn on if OS-level permission is denied → instead route to a permission prompt (a rule, surfaced, not a silent no-op). |
| **Feedback** | Thumb slides + track colour change (visual); light selection haptic; AT announces "Push notifications, on/off" (role=switch, aria-checked). |
| **Loops & Modes** | Persists until changed (long loop = remembered next session). Error mode if the server rejects the change. |

---

## States
| State | Visual | Notes |
|---|---|---|
| `rest-off` | thumb left, track `--surface-muted` | Default |
| `rest-on` | thumb right, track `--accent` + small check glyph | **Not colour-alone** — position + glyph also encode state (WCAG 1.4.1) |
| `hover` | track lightens 1 step | Pointer only; never the only affordance |
| `focus-visible` | 2 px ring, ≥ 3:1 contrast | Keyboard (WCAG 2.4.7 / 2.4.13) |
| `pressed` | thumb `scale(0.94)` | `:active`, both directions |
| `loading` | thumb shows 1.2 s shimmer, interaction blocked | Only if round-trip > 80 ms |
| `disabled` | 40% opacity, no motion | While first fetch pending; still exposes `aria-checked` (4.1.2) |
| `error` | reverts to prior state + inline message | Server rejected (see failure path) |

Hit target: **44×44 px** minimum (WCAG 2.5.8 min 24; Apple HIG 44 / Material 48dp).
Accessible: `role="switch"`, `aria-checked`, label "Push notifications".

---

## Motion timeline (happy path: tap to turn ON, optimistic)

| t (ms) | Channel | From → To | Duration | Curve / spring | Anatomy layer |
|---|---|---|---|---|---|
| 0 | press feedback (visual) | thumb scale 1 → 0.94 | 100 | ease-out-quint `cubic-bezier(0.22,1,0.36,1)` | Feedback |
| 0 | **optimistic state** | `aria-checked=true`; track colour → `--accent`; check glyph appears | instant | — (token swap, not animated) | Feedback |
| 0 | haptic | selection tick | — | `.selection` (iOS) / `CLOCK_TICK` (Android) | Feedback |
| 100 | thumb travel | translateX left → right | 150 | ease-in-out `cubic-bezier(0.4,0,0.2,1)` | Feedback |
| 100 | thumb settle | scale 0.94 → 1 | — | **spring** stiffness 700 / damping 38 (ζ≈0.72, no visible bounce) | Feedback |
| — | API fire | PUT /settings/push in background | — | — | Loops (reconcile) |

- **Total perceived feedback ≤ 250 ms** — inside the feedback band; nothing exceeds 400 ms.
- **Why a spring on settle, not `ease-back`:** the toggle is interruptible (fast double-tap should
  redirect mid-flight) and `ease-*-back`/elastic overshoot is the banned AI-slop bounce tell
  (`doctrine/references/ai-slop-taxonomy.md`). ζ≈0.72 gives a crisp landing with **no** oscillation.
- **What we animate:** `transform: translateX()` + `transform: scale()` + `opacity` only. The track
  colour and glyph are **instant token changes**, not animated layout/paint (GPU-only rule,
  motion-design §3).
- **Not colour-alone:** thumb *position* and the *check glyph* carry the state independent of hue.

### Failure path (server rejects the change)
| t (ms) | Action |
|---|---|
| 0 | Revert `aria-checked=false`, thumb → left, track → `--surface-muted` (**instant**, no spatial animation) |
| 0 | Error haptic `.notification(.error)` / `REJECT` |
| 0 | Inline message under the row: "Couldn't update — tap to retry" (colour + icon + text, never colour-alone) |

This is the **optimistic rollback contract** (`references/micro-interaction-anatomy.md` §4): apply
instantly, reconcile in the background, roll back visibly-but-calmly on rejection.

---

## Reduced-motion replacement (`prefers-reduced-motion: reduce` — WCAG 2.3.3)

Per `motion-design/references/reduced-motion.md`: **replace** spatial motion, **keep** the state signal.

| Channel | Normal | Reduced |
|---|---|---|
| Thumb travel (translateX) | 150 ms ease-in-out | **instant** position change |
| Thumb settle | spring | **none** |
| Press scale 0.94 | spring back | **none** — thumb stays at scale 1 |
| Track colour + check glyph | instant (kept) | instant (kept — no motion) |
| Error revert | instant + (no shake) | identical — colour + icon + text only |
| Haptic | selection / error tick | unchanged (non-visual, safe) |

```css
.switch__thumb {
  transition: transform 150ms cubic-bezier(0.4,0,0.2,1);
}
.switch[aria-checked="true"] .switch__thumb { transform: translateX(20px); }

@media (prefers-reduced-motion: reduce) {
  .switch__thumb { transition: none !important; } /* position still changes, just not animated */
}
```

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
function setPush(on) {
  el.setAttribute('aria-checked', String(on)); // optimistic state, instant
  haptic(on ? 'selection' : 'selection');
  if (reduce) return;                           // skip the spring settle
  thumb.animate(
    [{ transform: 'scale(0.94)' }, { transform: 'scale(1)' }],
    { duration: 150, easing: 'cubic-bezier(0.22,1,0.36,1)' } // spring-approx, no overshoot
  );
}
```

---

## Platform parity
- **iOS (SwiftUI):** `Toggle` with `withAnimation(.spring(duration: 0.15, bounce: 0))`; gate on
  `@Environment(\.accessibilityReduceMotion)`; `.sensoryFeedback(.selection, trigger: isOn)` for the
  tick and `.error` on rejection. Verify usable with haptics off.
- **Android (Compose):** `Switch` with `animateFloatAsState(spring(dampingRatio = 0.75f, stiffness = 700f))`;
  check `LocalReducedMotion.current`; `performHapticFeedback(CLOCK_TICK)` on change, `REJECT` on error.

---

## Acceptance checklist
- [x] Anatomy named — trigger / rules / feedback / loops all explicit
- [x] Every state defined incl. `focus-visible` (44×44 target, 3:1 ring) and `disabled` (no motion)
- [x] `transform` + `opacity` only — colour/glyph are instant token swaps (no animated layout)
- [x] Spring settle ζ ≥ 0.7 (no visible bounce); **no** `ease-back`/elastic
- [x] State is **never colour-alone** — position + glyph + AT state
- [x] Haptics semantic (selection on change, error on reject) and usable with haptics off
- [x] Optimistic update **with** rollback on failure
- [x] Considered `prefers-reduced-motion` path (replace, not strip) — state signal preserved
- [x] No flashing > 3×/s; AT exposes `role=switch` + `aria-checked` (4.1.2)
- [x] Verified by toggling OS reduce-motion + VoiceOver/TalkBack on real devices
