# Reference: Reduced Motion (`prefers-reduced-motion` / WCAG 2.3.3)

The accessibility contract for motion. **35%+ of adults over 40 report vestibular sensitivity**;
large-area or parallax motion can trigger nausea, dizziness, and migraine. This is a **conformance
requirement, not a nicety** — see `doctrine/references/wcag-2.2-criteria.md` (Motion row).

## Governing criteria
- **WCAG 2.3.3 Animation from Interactions (AAA):** motion triggered by interaction can be disabled
  unless the motion is *essential* to the function. This is the criterion `prefers-reduced-motion`
  satisfies. **We treat it as a hard floor**, despite its AAA label.
- **WCAG 2.3.1 Three Flashes (A):** no content flashes more than **3× per second** — applies even
  in the reduced-motion path.
- **WCAG 2.2.2 Pause/Stop/Hide (A):** any auto-playing motion lasting > 5 s must be pausable.

---

## 1. The query is a *signal*, not an off-switch

`prefers-reduced-motion: reduce` means **"prefers less / safer motion"**, not "zero motion". The
correct response is to **replace** vestibular-triggering motion with a non-vestibular equivalent —
not to strip all feedback (removing feedback harms usability for everyone).

| Trigger class | Normal | Reduced-motion replacement |
|---|---|---|
| **Large-area translate** (slide-in panels, page slides) | translate + fade | **opacity-only fade ≤ 100 ms**, no translate |
| **Parallax / scroll-jacking** | depth motion | static layers |
| **Scale/zoom transitions** | scale 0.9→1 | opacity-only |
| **Auto-play / loops** (carousels, shimmer, video) | continuous | paused; static skeleton; explicit play control |
| **Spring/bounce settle** | physics overshoot | instant or critically-damped, no oscillation |
| **Confetti / particle delight** | burst | suppress entirely |

| Safe to KEEP under reduced-motion |
|---|
| Opacity transitions < 200 ms |
| Colour / background transitions (no spatial motion) |
| Non-motion progress (determinate bar fill, % text) |
| Tiny in-place feedback (≤ ~2 px), e.g. focus ring fade |

---

## 2. The baseline CSS (global safety net)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

This is the **floor**, not the finish. It nukes everything — including useful colour/opacity fades.
Layer a *considered* path on top:

```css
/* Considered path: keep gentle opacity, drop spatial motion */
.card { transition: opacity 90ms ease-out, transform 300ms cubic-bezier(0.25,1,0.5,1); }

@media (prefers-reduced-motion: reduce) {
  .card { transition: opacity 90ms ease-out; transform: none !important; }
}
```

### Prefer `no-preference` to opt motion *in* (progressive enhancement)

Default to no motion; add motion only when explicitly safe:

```css
.hero { opacity: 1; }                 /* static by default */
@media (prefers-reduced-motion: no-preference) {
  .hero { animation: fadeSlideUp 500ms cubic-bezier(0.16,1,0.3,1) both; }
}
```

---

## 3. JS & platform hooks

```js
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
if (reduce.matches) { /* skip the animation; jump to end state */ }
reduce.addEventListener('change', applyMotionPrefs); // react live
```

- **View Transitions:** disable `::view-transition-*` animations (see `view-transitions.md` §5).
- **iOS / SwiftUI:** `UIAccessibility.isReduceMotionEnabled`; SwiftUI `@Environment(\.accessibilityReduceMotion)`.
- **Android / Compose:** check the system *Remove animations* setting; `LocalReducedMotion.current` (Compose 1.7+) / `Settings.Global.ANIMATOR_DURATION_SCALE == 0`.

---

## 4. Checklist
- [ ] Global `@media (prefers-reduced-motion: reduce)` safety net present.
- [ ] Each non-trivial animation has a **considered** reduced-motion path (replace, don't just kill feedback).
- [ ] No large-area translate, parallax, scale, or spring overshoot survives in the reduce path.
- [ ] Auto-playing motion is paused / has a play control (2.2.2); nothing flashes > 3×/s (2.3.1).
- [ ] JS reads `matchMedia` and reacts to live changes; native code reads the platform flag.
- [ ] Verified by toggling the OS setting (macOS Reduce Motion, Windows Show animations off, Android Remove animations) — not just DevTools emulation.
