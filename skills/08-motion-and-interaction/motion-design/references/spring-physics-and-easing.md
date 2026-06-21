# Reference: Spring Physics & Easing

How to choose between **duration-based easing** (cubic-bezier) and **physics-based springs**, and
how to parameterise each so motion reads as authored, not defaulted. Source: Material Design 3
motion-physics spec; Apple HIG — Motion (`.spring`); WebKit/Chromium `linear()` easing; Framer
Motion / React-Spring physics docs. Cross-cuts `doctrine/design-doctrine.md` (bounce/elastic is the
#1 AI animation fingerprint — restraint outranks novelty).

---

## 1. Easing vs spring — pick deliberately

| Use **duration easing** (`cubic-bezier`) when… | Use a **spring** when… |
|---|---|
| The end state and timing are fixed (entrances, fades, modal in/out). | Motion can be **interrupted / redirected** mid-flight (drag, gesture, re-tap). |
| You want a guaranteed exact total duration. | The object should feel like it has mass/momentum (sheets, drag-to-dismiss). |
| Pure opacity/colour change. | Position/scale settling after a fling or release. |

Springs are **interruptible and velocity-aware**; easing curves are not. State the choice in the
spec — never reach for a spring "because it feels modern".

---

## 2. Spring parameterisation (the modern API: stiffness + damping)

A spring is defined by **stiffness** (how hard it pulls to target), **damping** (how fast it bleeds
energy), and **mass** (inertia, usually leave at 1). The derived quantity that matters is the
**damping ratio** ζ:

```
ζ = damping / (2 · √(stiffness · mass))
```

| ζ | Behaviour | Verdict |
|---|---|---|
| **ζ ≥ 1** (critically / over-damped) | Settles to target with **no overshoot** | ✅ Default for professional UI |
| **0.7 ≤ ζ < 1** (lightly under-damped) | One tiny, almost-imperceptible overshoot | ⚠️ Acceptable for playful brands only, stated intentionally |
| **ζ < 0.6** (under-damped) | Visible bounce / oscillation | ❌ Banned — the elastic/bounce slop tell (design-doctrine §2) |

**Recommended starting presets** (mass = 1):

| Intent | stiffness | damping | ζ | ~settle |
|---|---|---|---|---|
| Snappy feedback (toggle, press) | 700 | 38 | ~0.72 | ~150 ms |
| Standard UI (cards, sheets) | 400 | 40 | **~1.0** | ~300 ms |
| Gentle / heavy surface | 250 | 32 | **~1.0** | ~450 ms |

> Tuning rule: **fix ζ first** (start at 1.0 — no overshoot), then raise/lower stiffness together
> with damping to make it faster/slower while holding ζ. Don't drop damping alone — that's how you
> accidentally ship bounce.

### Platform spring APIs

- **SwiftUI:** `.spring(duration: 0.4, bounce: 0)` — `bounce: 0` ⇒ ζ = 1 (no overshoot). Keep
  `bounce ≤ 0.15`. `bounce` maps to under-damping; `0` is the professional default.
- **Jetpack Compose:** `spring(dampingRatio = Spring.DampingRatioNoBouncy /* 1.0 */, stiffness = Spring.StiffnessMedium /* 400 */)`. Avoid `DampingRatioMediumBouncy` (0.5).
- **Web (Framer Motion):** `{ type: "spring", stiffness: 400, damping: 40, mass: 1 }`.
- **Web (CSS `linear()`):** bake a spring into a `linear()` easing function for hardware-accelerated
  CSS without JS (Chromium 113+/Safari 17.2+). Generate via a spring-to-`linear()` tool, e.g.
  `transition: transform 0.4s linear(0, 0.18, 0.55, 0.83, 0.96, 1);`.

---

## 3. Duration-easing reference (carried from SKILL §2 — physics framing)

Exponential ease-out curves approximate a critically-damped spring's *deceleration*, which is why
they read as natural:

| Curve | cubic-bezier | Spring it mimics |
|---|---|---|
| ease-out-quart | `0.25, 1, 0.5, 1` | critically-damped, medium |
| ease-out-expo | `0.16, 1, 0.3, 1` | critically-damped, strong initial velocity |
| ease-in-out | `0.4, 0, 0.2, 1` | symmetric settle (position swaps) |

**Never** author a cubic-bezier whose curve overshoots the `[0,1]` range on the value axis (control
points with y > 1) — that is a synthetic bounce and is banned for the same reason as spring ζ < 0.6.

---

## 4. Checklist

- [ ] Easing vs spring choice is **stated** with its reason.
- [ ] Every spring has **ζ ≥ 0.7** (default ζ = 1.0 / `bounce: 0` / `NoBouncy`).
- [ ] No cubic-bezier overshoots y∈[0,1].
- [ ] Springs are used where motion can be interrupted; fixed easing where it can't.
- [ ] Settle time still respects the 100/300/500 budget for the category.
