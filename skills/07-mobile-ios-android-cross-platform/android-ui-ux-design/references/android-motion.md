# Reference: Android Motion (Material 3 Expressive motion + predictive back)

How motion should behave on a premium Android app. Source: Material 3 motion guidance
(m3.material.io/styles/motion), the Jetpack Compose animation APIs
(`androidx.compose.animation`, `androidx.compose.material3` motion tokens), and the Android
platform **predictive back** guidance. Motion is part of the anti-slop signature: stock,
linear, or absent motion reads as the convergent default; **spring-physics, shared-element,
and interruptible gesture motion read as authored.** Honour `prefers-reduced-motion` —
see `doctrine/references/wcag-2.2-criteria.md` (§2.3 motion).

---

## 1. Motion principles (Expressive)

Material 3 Expressive motion is **spring-physics first**. Replace fixed-duration linear/ease
curves with springs defined by **damping** and **stiffness** so motion has natural mass and can be
**interrupted and redirected** mid-flight (essential for gestures). Three jobs of motion:

1. **Orient** — show where things come from and go to (enter/exit, container transform).
2. **Express emphasis** — the primary action and state changes get the most energetic spring;
   secondary chrome moves less.
3. **Track the finger** — gesture-driven motion (back, swipe, drag, pull-to-refresh) follows input
   progress exactly and reverses cleanly on cancel.

### Motion tokens (use the system scale, don't invent durations)
M3 defines **easing + duration tokens** in tiers — short (≈50–200ms) for small utility changes,
medium (≈250–400ms) for component transitions, long (≈450–600ms) for full-screen / shared-element.
In Compose prefer `MaterialTheme.motionScheme` springs (the Expressive **spring-based motion
scheme**, e.g. fast/default/slow spatial & effects springs) over hand-typed `tween` durations.

| Need | Use |
|---|---|
| Two states of one value | `animate*AsState` with a **spring** spec |
| Appear / disappear | `AnimatedVisibility` (enter/exit transitions) |
| Swap content | `AnimatedContent` (with a sensible `SizeTransform`) |
| Reorder / shared element | **Shared-element transitions** (`SharedTransitionLayout`) and `Modifier.animateItem()` in lazy lists |
| Screen ↔ screen | Navigation transitions + predictive back (below) |
| Continuous / looping | `rememberInfiniteTransition` (loaders, skeletons) |

---

## 2. Predictive back motion (the headline gesture)

Predictive back lets the user **preview the destination during the swipe** and cancel before
commit. The motion contract:

- **Track progress.** Use `PredictiveBackHandler`; it streams a `BackEventProgress` (0→1) plus
  swipe edge and touch point. Drive the outgoing screen's **scale (down toward ~0.9), translation,
  and corner-radius** from that progress so the live frame shows the destination underneath.
- **Interruptible & reversible.** If the user releases below threshold, **spring back** to the
  original state; above threshold, **complete** the transition. Never snap instantly — the whole
  point is the smooth, cancellable preview.
- **Three scopes:** (a) **back-to-home** (system animates your app toward the launcher — you mainly
  declare support), (b) **cross-activity**, and (c) **in-app** back between Compose destinations
  (you own the animation via the nav predictive-back support).
- **Material components** (bottom sheets, side sheets, search, nav drawer) ship predictive-back
  dismissal — adopt the M3 component versions instead of custom dismiss logic so you get it free.
- **Anti-pattern:** a legacy non-predictive `OnBackPressedCallback` that blocks the animation, or a
  destination with no reveal (back that just hard-cuts) — both read as un-modern.

---

## 3. Signature motion moments worth getting right

- **Container transform** — a tapped card/list item morphs into the detail screen (and morphs back
  on predictive back). The single highest-value "authored" moment.
- **FAB / button shape morph** — Expressive controls change **shape** on press (M3 shape morph), not
  just colour.
- **List item motion** — `animateItem()` for insert/remove/reorder so data changes feel physical.
- **Loading** — M3 **loading indicators** and contained/wavy progress over a static spinner; skeletons
  via `rememberInfiniteTransition`. Never block the UI with a bare centred ProgressBar if a skeleton
  or shimmer is feasible.
- **Pull-to-refresh** — the M3 `PullToRefresh` indicator, tracking drag progress.

---

## 4. Reduced motion & accessibility (non-negotiable)

- Respect the system **"Remove animations"** setting (`Settings.Global.ANIMATOR_DURATION_SCALE` ≈ 0)
  and reduced-motion intent: when set, **drop large translate/scale/parallax** and substitute simple
  cross-fades or instant state changes — but **keep essential feedback** (focus, selection, progress).
- This satisfies WCAG 2.2 **2.3.1** (no >3 flashes/sec) and the reduced-motion expectation.
- Predictive back must still function with animations reduced — the **navigation** works; only the
  decorative reveal is minimized.
- Don't gate meaning on motion alone (doctrine: visible affordances over discovery) — a control must
  read as interactive while static.

---

## 5. Motion checklist (state at sign-off)

- [ ] Transitions use **spring / motion-scheme tokens**, not ad-hoc `tween` durations.
- [ ] **Predictive back** is interruptible, progress-tracked, and reversible on cancel.
- [ ] At least one **authored** moment (container transform / shape morph / shared element) on the key flow.
- [ ] List mutations animate (`animateItem`); loading uses M3 indicator/skeleton, not a bare spinner.
- [ ] **Reduced-motion** path verified: large motion dropped, essential feedback kept, navigation intact.
