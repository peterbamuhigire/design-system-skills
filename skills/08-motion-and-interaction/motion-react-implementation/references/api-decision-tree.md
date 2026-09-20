# Reference: motion/react API Decision Tree

Source: ECC `motion-advanced` decision tables, mechanics only.

## Choosing the right API

| Scenario | API | Why |
|---|---|---|
| Discrete state change, not interruptible | `animate` prop + `transition` | Simplest declarative form; React drives it |
| Interruptible / gesture-driven / continuous value | `useMotionValue` + `useTransform` | Updates every frame without triggering a re-render |
| Value should smooth toward a target over time | `useSpring` (wrapping a `useMotionValue`) | Physics-based follow, picks up velocity on interrupt |
| Drag with physics on release | `drag` + `dragTransition: <spring>` | Native gesture recognition + spring settle |
| Ordered drag-to-reorder list | `Reorder.Group` + `Reorder.Item` | Handles list reflow during drag automatically |
| Dismiss on drag offset | `drag="y"` + `onDragEnd` checking offset AND velocity | Single-pointer alternative already built in |
| Swipe left/right | `drag="x"` + `onDragEnd` checking offset AND velocity | Same mechanism, horizontal axis |
| Long press | Custom `useLongPress` hook (`onPointerDown`/`onPointerUp`/`onPointerLeave` + `setTimeout`) | Not a built-in gesture; needs manual timer with cleanup on early release |
| Multi-step sequence, imperative | `useAnimate` with `async/await` | Interrupt-safe; calling `animate()` mid-flight cancels the previous run automatically |
| One-shot imperative animation, no component | `animate()` from `motion` (not `motion/react`) | For animating a DOM node reference directly, outside JSX |
| Text entering word/character by word | Stagger on `inline-block` spans via `variants` + `staggerChildren` | Each span is an independently animatable target |
| SVG drawing on | `pathLength` 0 → 1 | Native SVG stroke property, GPU-friendly |
| SVG morph between two shapes | `d` attribute tween — **only if both paths have equal command counts** | Framer/motion interpolates command-by-command; mismatched counts snap instead of morphing |
| Circular/ring progress | `strokeDashoffset` tween against a fixed `strokeDasharray` | Standard SVG progress-ring technique |

## `useSpring` vs a spring `transition`

| | `useSpring` | `transition: <spring>` |
|---|---|---|
| Use for | Continuously updating values (cursor follower, pointer-tracked position) | Discrete state changes (open/closed, on/off) |
| Updates | Every frame, driven by the underlying motion value | Triggered once per state change |
| Interrupt behaviour | Smooth — physics picks up from current velocity | Restarts the spring from the current rendered value |

## `useAnimate` mechanics

Returns `[scope, animate]`. `scope` is a ref that must be attached to a **mounted** DOM element —
calling `animate()` before that element mounts throws silently (no error surfaced, animation
simply does nothing). Sequential `await animate(...)` calls run in order; an un-awaited `animate()`
call fires and continues without blocking the next step ("fire and forget").

```tsx
const [scope, animate] = useAnimate()

async function play() {
  await animate(".step-1", { opacity: 1 }, { duration: 0.3 })
  await animate(".step-2", { x: 0 },       { duration: 0.4 })
        animate(".step-3", { scale: 1 },    { duration: 0.25 })  // fire and forget
}

return <div ref={scope}>...</div>
```

## Gesture threshold rule

Never infer swipe/drag-dismiss intent from `offset` or `velocity` alone — combine both:

```tsx
onDragEnd={(_, info) => {
  if (info.offset.y > 120 || info.velocity.y > 500) onClose()
}}
```

A short, fast flick and a long, slow drag are both legitimate "yes" signals; either check alone
misses one of them.

## Cleanup and visibility rules

- Every `window`/`document` listener added in a custom motion hook's `useEffect` needs the matching
  `removeEventListener` in the effect's cleanup return.
- Any `repeat: Infinity` animation controlled via `useAnimation()` should stop on
  `document.visibilitychange` to `"hidden"` and restart on visible, so background tabs are not
  animating continuously.
