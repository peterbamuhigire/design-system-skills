# Worked Example: Micro-Interaction Spec — "Save / Bookmark" Toggle

A fully specified single micro-interaction, the artifact a designer hands to engineering. It
exercises every rule the skill enforces: timing budget, easing **and** spring choice, all states,
and a considered `prefers-reduced-motion` fallback. Use as the template for any
`docs/ux/motion/*.md` spec.

---

## Component
**Bookmark toggle** — a 24×24 icon button in an article header that toggles saved / not-saved, with
optimistic update and a brief confirmation flourish.

Targets: web (CSS + View Transitions optional), parity notes for iOS/Android.

## States
| State | Visual | Notes |
|---|---|---|
| `rest-unsaved` | outline bookmark, `--icon-muted` | Default |
| `hover` | icon lifts, colour → `--icon-default` | Pointer only |
| `pressed` | icon `scale(0.92)` | `:active`, both states |
| `rest-saved` | filled bookmark, `--accent` | Persisted |
| `focus-visible` | 2 px focus ring, 3:1 contrast | Keyboard (WCAG 2.4.7 / 2.4.13) |
| `disabled` | 40% opacity, no motion | While first fetch pending |

Hit target: **44×44 px** tap area around the 24×24 glyph (WCAG 2.5.8 min 24, Apple HIG 44).

---

## Motion timeline (the happy path: tap to save)

| t (ms) | Channel | From → To | Duration | Curve / spring | Category (SKILL §1) |
|---|---|---|---|---|---|
| 0 | press feedback | scale 1 → 0.92 | 100 | ease-out-quint `cubic-bezier(0.22,1,0.36,1)` | Feedback |
| 0 | **optimistic state** | icon swaps outline → filled, colour → `--accent` | instant | — | — |
| 100 | release settle | scale 0.92 → 1 | — | **spring** stiffness 700 / damping 38 / mass 1 (ζ≈0.72, no visible bounce) | Feedback |
| 100 | confirm flourish | filled icon scale 1 → 1.12 → 1 | 240 | spring stiffness 400 / damping 30 (ζ≈0.75) | Micro-interaction |
| — | API fire | POST /bookmarks in background | — | — | — |

- **Total perceived flourish ≤ 260 ms** — well inside the feedback/micro budget; nothing exceeds 400 ms.
- **Why a spring on settle, not easing:** the press is interruptible — a fast double-tap should
  redirect mid-flight; a spring is velocity-aware (see `references/spring-physics-and-easing.md` §1).
  ζ≈0.72–0.75 gives a barely-perceptible "pop" without crossing into banned bounce (ζ<0.6).
- **What we animate:** `transform: scale()` and `opacity` only — no width/height/colour-layout. The
  colour swap is an instant token change, not an animated property (GPU-only rule, SKILL §3).

### Failure path (API rejects)
| t (ms) | Action |
|---|---|
| 0 | Revert icon → outline, colour → `--icon-muted` (instant) |
| 0 | Error shake: `translateX(-4px → 4px)` ×2, 300 ms, ease-in-out (SKILL §4.5) |
| 0 | Inline toast "Couldn't save — retry" |

Roll back optimistically-applied state only on rejection (SKILL §7).

---

## Reduced-motion fallback (`prefers-reduced-motion: reduce` — WCAG 2.3.3)

Per `references/reduced-motion.md`: **replace** spatial motion, keep the state signal.

| Channel | Normal | Reduced |
|---|---|---|
| Press scale 0.92 | spring | **none** — icon stays at scale 1 |
| Confirm flourish 1→1.12→1 | spring pop | **opacity-only** flash: filled icon fades in over 90 ms |
| Error shake | translateX ×2 | **none** — colour revert + toast only |
| Colour/fill swap | instant (kept) | instant (kept — no motion) |

```css
.bookmark__icon {
  transition: transform 120ms cubic-bezier(0.22,1,0.36,1), opacity 90ms ease-out;
}
.bookmark__icon[data-saved="true"] { transform: scale(1); } /* spring applied via WAAPI on toggle */

@media (prefers-reduced-motion: reduce) {
  .bookmark__icon { transition: opacity 90ms ease-out; transform: none !important; }
  .bookmark--error { animation: none !important; } /* no shake */
}
```

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
function confirmSave(el) {
  el.dataset.saved = 'true';
  if (reduce) return;                 // colour swap already done; skip the pop
  el.animate(
    [{ transform: 'scale(1)' }, { transform: 'scale(1.12)' }, { transform: 'scale(1)' }],
    { duration: 240, easing: 'cubic-bezier(0.16,1,0.3,1)' } // spring-approx ease-out-expo
  );
}
```

> Optional: if saving navigates to a "Saved" view, morph the icon with a `view-transition-name`
> (see `references/view-transitions.md` §2) — same reduced-motion rule applies.

---

## Platform parity
- **iOS (SwiftUI):** `withAnimation(.spring(duration: 0.24, bounce: 0.1)) { isSaved.toggle() }`;
  gate on `@Environment(\.accessibilityReduceMotion)`; haptic `.impact(.light)` on toggle.
- **Android (Compose):** `animateFloatAsState(targetValue, spring(dampingRatio = 0.75f, stiffness = 400f))`;
  check `LocalReducedMotion.current`; `performHapticFeedback` on toggle.

## Acceptance (maps to SKILL §9 checklist)
- [x] transform + opacity only — no layout properties
- [x] timing within feedback/micro budget (≤ 260 ms flourish, 100 ms press)
- [x] spring ζ ≥ 0.7 (no visible bounce); no bounce/elastic easing
- [x] every state defined incl. focus-visible (44×44 target, 3:1 ring)
- [x] optimistic update with rollback on failure
- [x] considered `prefers-reduced-motion` path (replace, not just disable)
- [x] verified by toggling the OS reduce-motion setting on real devices
