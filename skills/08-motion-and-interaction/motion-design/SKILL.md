---
name: motion-design
description: Animation and micro-interaction standards for web, Android, and iOS.
  Covers timing rules (100/300/500), easing curves, GPU-accelerated animation, staggered
  entrances, state transitions, loading states, Apple haptics/Liquid Glass motion checks,
  and mandatory prefers-reduced-motion.
status: active
metadata:
  portable: true
  category: 08-motion-and-interaction
  compatible_with:
  - claude-code
  - codex
---

# Motion Design Skill
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Setting animation timing or easing: applying the 100/300/500 duration rule, picking exponential ease-out curves over the banned bounce/elastic, or deriving stagger delays (40-80ms, capped at 800ms).
- Choosing between a fixed cubic-bezier and a **physics spring** for interruptible/gesture-driven motion — tuning stiffness, damping, and damping ratio (ζ ≥ 0.7) so motion never overshoots into the bounce tell.
- Wiring **View Transitions** for route/state/shared-element swaps instead of hand-rolled FLIP, and gating them under reduced motion.
- Building or auditing a `prefers-reduced-motion` path: replacing vestibular triggers (parallax, large translate, scale, spring overshoot) with safe non-spatial equivalents per WCAG 2.3.3 / 2.3.1 / 2.2.2.
- Specifying GPU-only animation (transform/opacity), entrance/state/loading motion, optimistic-update feedback, or Apple haptics / Liquid Glass / SF Symbols motion checks.

## Do Not Use When

- The work is the static visual system (colour, type, spacing, layout) with no motion — use `practical-ui-design` or `webapp-gui-design`.
- You need a worked feedback/toggle spec end-to-end (all states, optimistic rollback) — start from sibling `micro-interactions-and-feedback`.
- The motion is platform-API implementation detail only (Compose `animateFloatAsState`, SwiftUI `.spring(duration:bounce:)`) — pair with `android-ui-ux-design` / `ios-ui-ux-design`.
- You only need to judge whether existing animation reads as AI slop — use `visual-product-slop-audit`.

## Required Inputs

- Platform target(s): web (CSS/JS), Android (Compose), iOS (SwiftUI) — these drive the spring API and reduced-motion hook.
- The animation category (feedback, state change, layout shift, entrance, loading) so the right 100/300/500 band and easing apply.
- Whether the motion can be interrupted/redirected (drag, gesture, re-tap) — decides cubic-bezier vs physics spring.
- The reduced-motion intent: which triggers need a non-spatial replacement vs which feedback must be preserved.
- Whether Apple haptics, Liquid Glass chrome, or SF Symbols animation are in scope (pulls in the iOS sensory/HIG references).

## Workflow

- Read this `SKILL.md` first, then load only the referenced deep-dive files that are necessary for the task.
- Apply the ordered guidance, checklists, and decision rules in this skill instead of cherry-picking isolated snippets.
- Produce the deliverable with assumptions, risks, and follow-up work made explicit when they matter.

## Quality Standards

- Keep outputs execution-oriented, concise, and aligned with the repository's baseline engineering standards.
- Preserve compatibility with existing project conventions unless the skill explicitly requires a stronger standard.
- Prefer deterministic, reviewable steps over vague advice or tool-specific magic.

## Anti-Patterns

- Treating examples as copy-paste truth without checking fit, constraints, or failure modes.
- Loading every reference file by default instead of using progressive disclosure.

## Outputs

- A concrete result that fits the task: implementation guidance, review findings, architecture decisions, templates, or generated artifacts.
- Clear assumptions, tradeoffs, or unresolved gaps when the task cannot be completed from available context alone.
- References used, companion skills, or follow-up actions when they materially improve execution.

## Evidence Produced

| Category | Artifact | Format | Example |
|----------|----------|--------|---------|
| UX quality | Motion audit | Markdown doc covering timing rules, easing curves, reduce-motion support, and per-platform parity | `docs/ux/motion-audit-checkout.md` |

## References

- `references/spring-physics-and-easing.md` — easing-vs-spring decision, stiffness/damping/ζ params, platform spring APIs, CSS `linear()`.
- `references/view-transitions.md` — View Transitions API patterns (same-doc, shared-element morph, cross-doc MPA, directionality).
- `references/reduced-motion.md` — `prefers-reduced-motion` strategy, WCAG 2.3.3 contract, considered-replacement table.
- Pair with `../../07-mobile-ios-android-cross-platform/ios-ui-ux-design/references/ios-sensory-and-haptics.md` and `../../07-mobile-ios-android-cross-platform/ios-ui-ux-design/references/hig-liquid-glass.md` when Apple haptics, SF Symbols animation, or Liquid Glass chrome is in scope.
- `doctrine/design-doctrine.md` — the anti-slop charter; motion is a slop tell when overused or when bounce/elastic easing is applied.
- `doctrine/references/ai-slop-taxonomy.md` — the product/interface slop tells, including AI-fingerprint animation (bounce/elastic, animation fatigue).
- `doctrine/references/wcag-2.2-criteria.md` — the accessibility floor; motion must honour 2.3.3 (reduced motion) and 2.3.1 (≤3 flashes/s).

## Examples

- `examples/micro-interaction-spec.md` — a worked save/bookmark toggle spec: timing, spring params, all states, optimistic rollback, and a considered `prefers-reduced-motion` fallback. Use as the template for any motion spec.
<!-- dual-compat-end -->
## Plugins (Load Alongside)

| Companion Skill | When to Load |
|---|---|
| `practical-ui-design` | Visual system (colour, type, spacing) |
| `android-ui-ux-design` | Android Compose animation APIs |
| `ios-ui-ux-design` | SwiftUI animation/transition APIs |
| `webapp-gui-design` | Web app CSS/JS animation |
| `visual-product-slop-audit` | Validate animations aren't AI slop |

---

## 1. Duration Rules (The 100/300/500 Rule)

| Category | Duration | Use For |
|---|---|---|
| **Feedback** | 100-150ms | Button press, toggle, checkbox, hover |
| **State change** | 200-300ms | Accordion, tab switch, dropdown, modal appear |
| **Layout shift** | 300-500ms | Page transition, panel expand, reorder |
| **Entrance** | 500-800ms | Hero content, first-time reveal, onboarding |

### Exit Animations

Exit duration = **~75% of enter duration**. Users care less about things leaving than arriving.

### Key Principles

- Anything under 100ms feels instant (no animation needed)
- Anything over 400ms feels slow for micro-interactions
- Total staggered sequence should not exceed 800ms
- **80ms threshold**: if an operation takes < 80ms, skip the loading animation entirely
- Treat timing as a scale: derive related delays and durations from a base value, then cap the total sequence so the interface still feels responsive.

---

## 2. Easing Curves

### Recommended Curves

| Curve | CSS Value | When to Use |
|---|---|---|
| **ease-out-quart** | `cubic-bezier(0.25, 1, 0.5, 1)` | Default for most entrances and micro-interactions |
| **ease-out-quint** | `cubic-bezier(0.22, 1, 0.36, 1)` | Snappy feedback (toggles, checkboxes) |
| **ease-out-expo** | `cubic-bezier(0.16, 1, 0.3, 1)` | Dramatic entrances, hero content |
| **ease-in-quart** | `cubic-bezier(0.5, 0, 0.75, 0)` | Exit animations |
| **ease-in-out** | `cubic-bezier(0.4, 0, 0.2, 1)` | Toggles, state changes, position swaps |

### NEVER Use

| Curve | Why |
|---|---|
| `bounce` / `elastic` | Dated, tacky — the #1 AI animation fingerprint |
| `linear` | Mechanical, unnatural (except for continuous rotation) |
| `ease` (CSS default) | Too gentle, feels mushy |
| Custom springs with visible oscillation | Distracting, unprofessional |

### Easing vs Spring (when to leave cubic-bezier behind)

Use a **physics spring** instead of a fixed cubic-bezier when the motion can be **interrupted or
redirected** mid-flight (drag, gesture, re-tap) or should carry mass/momentum (sheets, drag-to-
dismiss). Parameterise by **stiffness + damping**, and keep the damping ratio **ζ ≥ 0.7** (default
ζ = 1.0 — no overshoot); **ζ < 0.6 is the banned bounce/elastic tell.** Good starting presets:
snappy `stiffness 700 / damping 38`, standard UI `400 / 40`. On the web you can bake a spring into a
hardware-accelerated CSS `linear()` easing function. Full decision table, per-platform spring APIs,
and tuning rules: `references/spring-physics-and-easing.md`.

---

## 3. What to Animate (GPU-Accelerated Only)

### ONLY Animate

| Property | Use For |
|---|---|
| `transform: translate()` | Position changes, slide in/out |
| `transform: scale()` | Grow/shrink, emphasis |
| `transform: rotate()` | Spin, flip, tilt |
| `opacity` | Fade in/out, reveal/hide |

These run on the GPU compositor — no layout recalculation, no jank.

### NEVER Animate

| Property | Why |
|---|---|
| `width`, `height` | Triggers layout recalculation every frame |
| `top`, `left`, `right`, `bottom` | Triggers layout recalculation every frame |
| `margin`, `padding` | Triggers layout recalculation every frame |
| `border-width`, `border-radius` | Triggers paint every frame |
| `font-size` | Triggers layout + paint + composite |
| `box-shadow` (animated) | Expensive paint operation |

**Alternative**: Use `transform: scale()` instead of animating width/height. Use `transform: translate()` instead of animating position.

---

## 4. Animation Categories

### 4.1 Entrance Animations

- Fade in: `opacity: 0 → 1` (200-300ms, ease-out-quart)
- Slide up: `translate(0, 16px) → translate(0, 0)` + fade (300-500ms)
- Scale in: `scale(0.95) → scale(1)` + fade (200-300ms)
- **Stagger children**: 50-80ms delay between items, cap total at 800ms

### 4.2 Micro-Interactions (Feedback)

- Button press: `scale(0.97)` on `:active` (100ms, ease-out-quint)
- Toggle: position swap (150ms, ease-in-out)
- Checkbox: check mark draw (200ms, ease-out-quart)
- Hover: subtle lift or colour shift (150ms, ease-out)

### 4.3 State Transitions

- Tab switch: cross-fade content (200ms)
- Accordion: height with `max-height` or CSS grid trick (250-300ms)
- Modal appear: backdrop fade + content scale from 0.95 (250ms, ease-out-quart)
- Modal exit: content fade + scale to 0.97 (180ms, ease-in-quart)

### 4.4 Navigation & Flow

- Page transition: fade + subtle slide in direction of navigation (300ms)
- Shared element: morph position/size between views (400ms, ease-out-expo)
- Back navigation: reverse the enter animation direction

**Use the View Transitions API for state/route/page swaps** instead of hand-rolling FLIP or
absolute-positioned clones. Same-document: feature-detect `document.startViewTransition(update)`
(instant fallback when unsupported). Shared-element morphs use matching `view-transition-name`s in
both states; cross-document MPA navigations opt in with CSS `@view-transition { navigation: auto; }`.
View Transitions are **not** reduced-motion-exempt — disable the `::view-transition-*` animations
under `prefers-reduced-motion`. Full patterns: `references/view-transitions.md`.

### 4.5 Loading & Feedback

- Skeleton screens: shimmer gradient animation (1.5s, infinite, ease-in-out)
- Progress bars: width transition (300ms, ease-out)
- Success: check mark draw + subtle scale bounce to 1.0 (400ms)
- Error: horizontal shake `translate(-4px) → translate(4px)` x2 (300ms)

### 4.6 Delight Moments

- Celebration: confetti, particle burst (use sparingly)
- Achievement: scale up + glow + settle (500ms)
- Easter eggs: only after repeated interaction, never blocking

---

## 5. Staggered Animations (CSS)

```css
/* Set index via inline style or CSS custom property */
.stagger-item {
  --i: 0; /* set per element: style="--i: 0", style="--i: 1", etc. */
  animation: fadeSlideUp 300ms ease-out both;
  animation-delay: calc(var(--i) * 60ms);
}

@keyframes fadeSlideUp {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Rules:**
- 40-80ms between items (60ms is sweet spot)
- Cap total stagger time at 800ms (for 10+ items, reduce per-item delay)
- First item appears immediately (no delay)
- Formula: `delay = min(index * 60ms, 480ms)` keeps long lists from becoming slow.

---

## 6. Reduced Motion (MANDATORY)

**35%+ of adults over 40 experience vestibular sensitivity.** This is not optional.

This satisfies **WCAG 2.3.3 Animation from Interactions** — treated here as a hard floor despite its
AAA label (see `doctrine/references/wcag-2.2-criteria.md`). The query means *"prefers safer motion,"*
not "zero motion": **replace** vestibular triggers (large translate, parallax, scale, spring
overshoot) with non-spatial equivalents (opacity-only ≤100ms, static) — don't strip feedback
wholesale. Also honour **2.3.1** (nothing flashes >3×/s) and **2.2.2** (auto-play >5s is pausable),
including inside the reduce path. Full replacement table, the `no-preference` opt-in pattern, and
JS/native hooks: `references/reduced-motion.md`.

### CSS Implementation

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

### What to Do Instead

| Normal | Reduced Motion |
|---|---|
| Slide + fade entrance | Instant appear (or very fast fade, 100ms) |
| Position transitions | Instant position change |
| Parallax scrolling | Static positioning |
| Auto-playing video/animation | Paused with play button |
| Continuous rotation/pulse | Static state |

### What to Keep

- Opacity transitions (under 200ms) — generally safe
- Colour transitions — no motion involved
- Essential progress indicators — use non-motion alternatives (progress bar fill)

---

## 7. Perceived Performance

### Preemptive Start

Start animations before data arrives. Show optimistic UI immediately, update when data loads.

### Early Visual Completion

Animate to ~90% quickly, slow the last 10%. Progress feels faster even if total time is the same.

### Active vs Passive Waiting

- **Active**: User-initiated (button click → action). Keep under 400ms or show inline progress.
- **Passive**: System-initiated (page load, sync). Use skeleton screens, not spinners.

### Optimistic Updates

Apply state changes immediately in the UI. Roll back only if the server rejects.

```
User taps "Like" → Heart fills instantly → API call fires in background
                                          → If fails, revert heart + show error
```

---

## 8. Platform-Specific Notes

### Web (CSS/JS)

- Prefer CSS animations/transitions over JS when possible
- Use `will-change` sparingly (only on elements about to animate)
- Use Web Animations API for complex JS-driven sequences
- Use `requestAnimationFrame` for frame-synced updates
- For JS-driven motion, calculate from elapsed time, not assumed frame count; compare decimals with a small tolerance when snapping to an end state.

### Android (Jetpack Compose)

- Use `animateFloatAsState`, `animateContentSize`, `AnimatedVisibility`
- `Animatable` for interruptible animations
- `spring()` for physics-based: `dampingRatio = DampingRatioNoBouncy` (ζ=1), tune via `stiffness`
- Check `LocalReducedMotion.current` (Compose 1.7+)

### iOS (SwiftUI)

- Use `.animation()` modifier or `withAnimation {}`
- `.spring(duration:bounce:)` — keep bounce at 0 (ζ=1) for professional feel; ≤0.15 max
- `matchedGeometryEffect` for shared element transitions
- Check `UIAccessibility.isReduceMotionEnabled`
- Keep haptics semantic: success only for success, warning/error for those outcomes, selection for selection changes. Verify the UI remains fully usable with haptics disabled.
- For Liquid Glass chrome and SF Symbols animation, verify Reduce Motion, Reduce Transparency, Increase Contrast, and VoiceOver. Required affordances cannot depend on shimmer, refraction, bounce, or symbol-only animation.

---

## 9. Quality Checklist

Before shipping animations:

- [ ] All animations use transform + opacity only (no layout properties)
- [ ] Timing follows the 100/300/500 rule for the animation category
- [ ] Easing uses exponential curves (ease-out-quart/quint), not bounce/elastic
- [ ] Stagger delays are 40-80ms with total capped at 800ms
- [ ] `prefers-reduced-motion` provides meaningful alternative
- [ ] Animations run at 60fps on mid-range devices
- [ ] Exit animations are ~75% of enter duration
- [ ] No animation fatigue (not everything animates)
- [ ] Animations serve purpose (guide attention, show relationships, provide feedback)
- [ ] Apple haptics/Liquid Glass/SF Symbols animation paths pass Reduce Motion and accessibility checks when iOS is in scope
- [ ] Tested on real devices (not just DevTools)

---

*Sources: Impeccable motion-design reference (Bakaus, 2025); Material Design 3 motion-physics spec; Apple Human Interface Guidelines — Motion; W3C CSS View Transitions Module L1/L2 (MDN); WCAG 2.2 (2.3.1 / 2.3.3 / 2.2.2). Deep-dives in `references/`.*
