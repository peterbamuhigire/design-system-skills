---
name: motion-react-implementation
description: Use when implementing motion in React or Next.js with the motion/react (Framer Motion) library — SSR/hydration safety, drag and gesture interactions, useAnimate imperative sequences, SVG path drawing, custom motion hooks, and the API decision tree (transition vs spring vs useAnimate vs motion values). Use motion-design for platform-agnostic timing/easing/spring tokens and the reduced-motion contract — this skill implements those decisions in React, it does not redefine them.
metadata:
  portable: true
  category: 08-motion-and-interaction
  compatible_with:
  - claude-code
  - codex
---

# Motion — React Implementation
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com. React/`motion` (Framer Motion)
implementation layer adapted from ECC's `motion-foundations`/`motion-advanced` skills — imported
narrowly: this engine's `motion-design` skill already owns tokens, spring stiffness/damping/ζ, and
the `prefers-reduced-motion` WCAG contract platform-agnostically, so none of that is repeated here.

<!-- dual-compat-start -->
## Use When

- Implementing an approved motion spec (from `motion-design`) in React/Next.js using the `motion`
  package (the successor/rename of Framer Motion; import from `motion/react`).
- Wiring drag, swipe, or long-press gesture interactions in a React component.
- Building an imperative, multi-step animation sequence (`useAnimate`) instead of declarative
  `animate` props.
- Animating SVG paths, building custom motion hooks (`useScrollReveal`, cursor followers), or a
  loading/skeleton/progress component.
- Debugging a hydration mismatch that traces to an animated component's `initial` state.
- Choosing between `transition`, `useSpring`, `useAnimate`, and raw `animate()` for a given
  interaction and not sure which API fits.

## Do Not Use When

- The decision is **what** duration, easing curve, spring damping ratio, or reduced-motion
  substitution to use — that is `motion-design` (platform-agnostic; do not re-derive tokens here).
- The target is not React/Next.js (SwiftUI, Jetpack Compose, vanilla CSS/JS) — `motion-design` §8
  covers platform-specific API notes for those; this skill is `motion/react`-specific.
- You only need a standard, already-catalogued UI pattern (button press, modal open/close, toast,
  stagger list, page transition) with no drag/gesture/imperative-sequence complexity — those are
  declarative `animate`/`variants` usage directly off `motion-design` tokens; this skill's
  additional API surface (drag, `useAnimate`, custom hooks, SVG) is for the harder cases.
- The work is CSS-only animation or Tailwind `animate-*` classes with no `motion/react` import.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| Approved motion spec (durations, springs, reduced-motion substitutions) | `motion-design` | yes | This skill implements a decision, it does not make one |
| Rendering target (SSR/SSG Next.js, or CSR-only) | Project | yes | Determines whether the hydration-safety rules in Workflow step 1 apply |
| The specific interaction shape (drag/gesture/sequence/SVG/hook) | User or component spec | yes | Selects the right API off the decision tree |

## Workflow

1. **Confirm SSR/hydration safety before writing any `motion.*` component.** If the app renders
   on the server (Next.js App Router, SSG), the `initial` prop **must match what the server
   renders** — if the server renders `opacity: 1`, `initial` must also be `opacity: 1`, with no
   exceptions. Use a `mounted` guard (`useState` + `useEffect`) to defer the "pre-entrance" state
   to the client only, rather than mismatching server/client output. Never read `window` or
   `navigator` at module scope — guard with `typeof window !== "undefined"`. Every file importing
   from `motion/react` needs `"use client"`. See `references/ssr-and-hydration.md`.

2. **Pull tokens and reduced-motion handling from `motion-design`, don't redefine them.** Duration,
   easing, spring stiffness/damping, and the `prefers-reduced-motion` substitution table are owned
   by `motion-design`/`references/spring-physics-and-easing.md` and `references/reduced-motion.md`.
   Wire `useReducedMotion()` from `motion/react` into whatever safe-motion hook the project uses,
   and never hardcode a duration/spring value inline in a component — import it.

3. **Pick the right API off the decision tree** (full table in
   `references/api-decision-tree.md`):
   - Discrete state change, not interruptible → `animate` prop + `transition` (spring or tween).
   - Interruptible / gesture-driven / continuous value → `useMotionValue` + `useSpring` /
     `useTransform`.
   - Drag interaction → `drag` prop (+ `dragConstraints`, `dragElastic`, `onDragEnd` checking
     **both** offset and velocity, never velocity alone).
   - Ordered drag-to-reorder → `Reorder.Group` / `Reorder.Item`.
   - Multi-step imperative sequence → `useAnimate` (interrupt-safe `async/await`; the scope ref
     must be attached to a mounted DOM element — calling `animate()` before mount throws silently).
   - SVG path draw-on → `pathLength` 0→1; SVG morph requires **equal path command counts** between
     start and end `d` or it snaps instead of interpolating.
   - Text reveal → stagger on `inline-block` spans via `variants` + `staggerChildren`.

4. **Handle gestures with explicit, combined thresholds.** Swipe/drag-to-dismiss intent must check
   **offset AND velocity**, never velocity alone (a fast short drag and a slow long drag are both
   legitimate "yes" signals; either alone under-fires). Test drag/gesture interactions on an actual
   touch device or emulator, not mouse-only — feel and default thresholds differ.

5. **Cost-gate infinite/continuous animation.** Any `repeat: Infinity` animation (shimmer, pulse,
   spinner) must pause when `document.visibilityState === "hidden"` — a background tab must not
   keep animating and consuming GPU/CPU. Every `window`/`document` event listener added for a
   custom motion hook needs a matching removal in the `useEffect` cleanup.

6. **Write custom motion hooks as motion values, not re-render loops.** `useMotionValue` +
   `useTransform` computes derived values without triggering a React re-render on every frame —
   use this for scroll-reveal, cursor followers, and any continuously-updating derived value.
   Create motion values with `useMotionValue(...)` inside the component body (once per instance);
   never `new MotionValue(...)` during render.

7. **Verify against the platform-agnostic contract before shipping.** Run the finished component
   through `motion-design`'s reduced-motion and performance checks (transform/opacity only, no
   layout-property animation) — this skill's job is correct React wiring of those decisions, not a
   second, competing set of rules.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Component may render on the server | `initial` matches server-rendered state; defer pre-entrance state behind a mount guard | Hydration mismatch warning, visible flash/jump on load |
| Drag or swipe interaction | Check both `info.offset` and `info.velocity` in `onDragEnd` | A fast-but-short drag or slow-but-long drag is missed |
| Infinite/looping animation (shimmer, pulse, spinner) | Pause on `visibilitychange` to hidden | Background tabs burn GPU/CPU indefinitely |
| Multi-step sequence needed | `useAnimate`, scope ref attached post-mount | Calling `animate()` pre-mount throws silently |
| SVG morph between two path states | Confirm equal command counts first | Paths snap instead of smoothly interpolating |
| Any duration/spring value needed | Import from the project's `motion-design`-derived token/spring map | Inline literals drift from the approved motion language |

## Capability Contract

Read access to the component tree and the project's motion-token module is required. Editing is
allowed once an approved motion spec exists. Execution (running the app, a touch-emulated browser)
is preferred to verify drag/gesture thresholds and hydration behaviour; without it, mark those
checks unverified rather than asserting them.

## Degraded Mode

Without a runnable app to test hydration or gesture behaviour, deliver the component code with the
SSR-safety and gesture-threshold rules applied by inspection, and explicitly mark hydration
matching and touch-device gesture feel as unverified. Without an approved `motion-design` spec to
implement, stop and request one rather than inventing timing/spring values here.

## Anti-Patterns

- **`initial={{ opacity: 0 }}` on a component that renders on the server** with no mount guard —
  the single most common hydration-mismatch cause in this API.
- **Importing from `framer-motion` and `motion/react` in the same tree** — pick one (`motion/react`
  is the current package) and never mix them.
- **Inline `transition={{ duration: 0.4 }}` or `{ stiffness: 300, damping: 30 }`** instead of the
  project's token/spring map from `motion-design`.
- **`onDragEnd` checking only `offset`**, missing fast short swipes that never accumulate distance.
- **`animate={{ repeat: Infinity }}` with no visibility pause** — background tabs keep animating.
- **`useAnimate()`'s `animate()` called before the scope ref is mounted** (e.g. in a module-level
  effect that races mount) — throws silently, animation appears to do nothing.
- **`const x = new MotionValue(0)` inside a render body** instead of `useMotionValue(0)` — breaks
  React's render model.
- **SVG morph between paths with different command counts** — produces a snap, not a tween.
- **A custom `window`/`document` listener with no cleanup** in a motion hook's `useEffect`.
- **Redefining duration/easing/spring/reduced-motion rules here** instead of importing them from
  `motion-design` — creates two competing sources of motion truth.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| React motion component(s) implementing an approved `motion-design` spec | Engineering | SSR-safe `initial`, token/spring values imported not inlined, `"use client"` present |
| Gesture/drag interaction wiring | Engineering, QA | Offset+velocity threshold documented; tested on touch device or explicitly marked unverified |
| Custom motion hook(s) | Component library | Cleanup verified for every added listener; motion values created per-instance, not per-render |

## Examples

- `examples/dismissible-sheet.md` — a worked drag-to-dismiss bottom sheet combining
  `useMotionValue`/`useTransform`, a reduced-motion-safe entrance from `motion-design`'s contract,
  `AnimatePresence`, and a shimmer-skeleton loading state with visibility-pause — the end-to-end
  pattern this skill's API surface composes into.

## References

- `references/ssr-and-hydration.md` — the mount-guard pattern, module-scope `window`/`navigator`
  guards, and the `"use client"` requirement, with before/after code.
- `references/api-decision-tree.md` — the full API selection table (`transition` vs `useSpring` vs
  `useTransform` vs `useAnimate` vs raw `animate()`) with the reasoning for each row.
- `../motion-design/references/spring-physics-and-easing.md` — the stiffness/damping/ζ values this
  skill's springs must be imported from, not redefined.
- `../motion-design/references/reduced-motion.md` — the substitution table this skill's
  `useReducedMotion()` wiring must satisfy.
- `doctrine/references/wcag-2.2-criteria.md` — 2.3.3/2.3.1/2.2.2, enforced via `motion-design`,
  implemented via this skill's SSR-safe reduced-motion wiring.
- Provenance: React/`motion` API surface (SSR safety, `useAnimate`, drag/gesture mechanics, custom
  hooks, SVG path drawing) adapted narrowly from ECC's `motion-foundations`/`motion-advanced`
  skills — the token/spring/reduced-motion content in those sources was NOT imported, because it
  duplicates this engine's existing `motion-design` skill (confirmed by direct read, not assumed).
<!-- dual-compat-end -->
