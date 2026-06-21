# Reference: Touch, Gesture, and Haptics

The canonical rules for the touch layer of a mobile UI: how big targets are, where the thumb reaches,
what each gesture means, the **legally required single-pointer alternatives**, and how haptics speak.
Source authority: W3C WCAG 2.2 (`doctrine/references/wcag-2.2-criteria.md`), Apple Human Interface
Guidelines (gestures, target sizing, playing haptics), Android Material 3 / Compose touch & haptics
guidance, governed by `doctrine/design-doctrine.md` §0 (an authored, discoverable gesture set is the
moat; a copied generic one is slop).

---

## 1. Hit / touch target sizing

**The floor is a floor, not a target.** Three numbers, used in this order:

| Standard | Minimum | When it governs |
|---|---|---|
| **WCAG 2.5.8 Target Size (Minimum, AA)** | **24 × 24 CSS px** | The legal floor for *any* pointer target on the web/responsive layer. Below this you need adequate spacing or an exception. |
| **Apple HIG** | **44 × 44 pt** | What you actually ship on iOS touch. |
| **Android / Material** | **48 × 48 dp** | What you actually ship on Android touch. |

Rules:

- **Ship the platform number, certify against the WCAG floor.** 44 pt / 48 dp both clear 24 px with
  margin; never design *down* to 24 just because it is legal.
- **Spacing:** keep **≥ 8 px/dp** of dead space between adjacent targets. WCAG 2.5.8 grants the small
  target an exception only when spacing makes mis-taps unlikely — prefer real size over relying on it.
- **Hit area ≠ glyph size.** A 24-pt visual icon is fine if its *touchable region* is expanded to
  44/48 (iOS: lay it out at the full size or set a larger content shape; Android: `minimumInteractive
  ComponentSize` / larger touch delegate). Extend the touch region, not the artwork.
- **Inline text links** in body copy are exempt from 2.5.8 but should still be comfortably tappable;
  prefer a button for any important action.
- Targets must hold their size at the **largest Dynamic Type / font-scale** — they must not shrink to
  make room for bigger text.

## 2. Thumb-zone ergonomics

A phone is mostly held and operated one-handed. Map the screen to the reach arc of the gripping thumb:

- **Natural zone** — the comfortable sweep, roughly the **bottom-center to bottom-near-side third**.
  Put **primary, frequent, positive** actions here: the main CTA, the send/confirm button, the
  active-row tap. Bottom bars / FABs / bottom sheets exist because this is the easy zone.
- **Stretch zone** — reachable with a small hand shift (mid-screen, far-bottom corner). Secondary
  actions, filters, occasional controls.
- **Hard zone** — top edge and the far-top diagonal corner. The thumb cannot reach it one-handed.
  Put **rare, non-urgent, or deliberately-guarded** things here: settings, close/X, and — importantly
  — **destructive** actions you do *not* want under a resting thumb.

Rules:

- Never place a **primary** action in the hard zone or a **destructive** action in the natural zone.
- Larger phones / foldables shrink the natural zone — test one-handed reach on the **biggest** target
  device; that is the worst case.
- Provide a way to bring far content down where the OS offers one (iOS Reachability), but never *rely*
  on it — design the default layout to be reachable.
- Bottom-anchored primary controls also keep the action clear of the **focus-not-obscured** rule
  (WCAG 2.4.11) and away from the top notch / Dynamic Island.

## 3. The gesture vocabulary

Use the smallest set that does the job. Standard, learned gestures and their canonical meaning:

| Gesture | Pointers / path | Canonical meaning | Notes |
|---|---|---|---|
| **Tap** | single, no path | Activate / select | The default; always available; never needs a fallback (it *is* the fallback). |
| **Double-tap** | single | Secondary activate (zoom, like) | Don't overload onto a single-tap target; slows everyone. |
| **Long-press** | single, time-held | Reveal context menu / enter edit/drag mode | Must have a visible alternative (overflow menu). |
| **Swipe** | single, **path-based** | Reveal row actions, page between views, dismiss | Path-based → **needs a single-pointer alternative (2.5.1)**. |
| **Drag** | single, **path + sustained** | Reorder, slide-to-confirm, drag-to-dismiss, slider | **Needs a non-drag alternative (2.5.7)**. |
| **Pinch / spread** | **multipoint** | Zoom / scale | Multipoint → **needs a single-pointer alternative (2.5.1)** (zoom buttons / double-tap). |
| **Rotate** | multipoint | Rotate object | Multipoint → needs single-pointer alternative. |
| **Edge-swipe** | single, from edge | Back / system | Often **system-reserved** — see §5; don't override. |

Discipline: one gesture = one meaning on a given surface. Don't invent a bespoke gesture where a
standard one (or a visible button) does the job — bespoke gestures cost discoverability (§7) and a
fallback (§4) for no gain unless they are a real distinctiveness moment.

## 4. The WCAG gesture-alternative rules (the legal core — apply every time)

Two success criteria make alternatives **mandatory**, not optional polish:

- **2.5.1 Pointer Gestures (AA):** any function that uses a **multipoint** gesture (pinch, two-finger
  rotate) **or** a **path-based** gesture (swipe, drag along a track, free-draw) must **also** be
  operable with a **single pointer without a path** — i.e. a plain tap/click on a control.
- **2.5.7 Dragging Movements (AA):** any function achieved by **dragging** must **also** be achievable
  **without dragging** — typically tap targets, +/− or up/down buttons, or a menu command. (A tap is
  not a drag, so the alternative cannot itself require dragging.)

**The rule table — for every gesture in your screen, fill the right column. A blank right column is a
defect, not a nicety:**

| Gesture you used | Why it triggers a rule | Required alternative (single-pointer / non-drag) |
|---|---|---|
| Swipe-to-delete on a list row | path-based (2.5.1) + reveals an action | Long-press / tap → menu with **Delete**; or a visible trailing **⋯** button. |
| Swipe to page between tabs/cards | path-based (2.5.1) | Tappable tab bar / page dots / next-prev buttons. |
| Drag to **reorder** a list | dragging (2.5.7) | **Move up / Move down** buttons, or a "Move to…" menu. |
| **Slide-to-confirm** / slide-to-pay | path-based (2.5.1) + dragging (2.5.7) | A plain **Confirm** button (optionally guarded by a normal tap-and-hold-to-confirm with a visible progress ring, which is single-pointer, no path). |
| **Pinch-to-zoom** image/map | multipoint (2.5.1) | **+ / −** zoom buttons and/or **double-tap** to zoom. |
| Drag-to-dismiss a sheet | dragging (2.5.7) | A visible **Close / X** button (≥ 44/48). |
| Drag a **slider** to set a value | path-based (2.5.1) + dragging (2.5.7) | Tappable track + **stepper (− / +)** buttons, or a number entry. |
| Pull-to-refresh | path-based (2.5.1) | A visible **Refresh** control (menu item or button). |
| Free-draw / signature | path-based — **essential exception** | 2.5.1 exempts gestures **essential** to the function (drawing's whole point is the path). Document the exception; still offer "type your name" where the law allows. |

Notes:

- **Essential exception:** 2.5.1 does not apply where the path *is* the function (drawing, handwriting,
  a piano keyboard). State the exception explicitly; don't use it as a loophole for swipe-to-delete.
- The alternative is usually **the same control that gives you discoverability** (§7) — one visible
  button satisfies both. Design them together.
- Keyboard/switch users and motor-impaired users depend on these; they are also better for everyone
  one-handed in a moving vehicle. Certify in the gate (§8).

## 5. Gesture conflicts & system-reserved gestures

Some gestures belong to the OS. Fighting them breaks the platform contract and your custom gesture
will lose or fire unpredictably.

| Reserved region / gesture | iOS | Android | Your rule |
|---|---|---|---|
| Screen-edge **back** | Left-edge swipe-back | Predictive back (both edges) | Don't put a conflicting custom horizontal swipe on the very edge; inset it, or accept that back wins. |
| Top edge | Control Center / Dynamic Island / status | Quick settings / notification shade | No custom pull-down from the top edge. |
| Bottom edge | Home indicator swipe-up | Home / gesture nav pill | Keep interactive controls clear of the home indicator inset. |
| System-wide | Reachability, App Switcher | Recents, one-handed mode | Don't replicate or block. |

Nesting conflicts (your-own-vs-your-own):

- A **horizontally-swiping row** inside a **horizontally-paging carousel** inside the **edge-back**
  region is three claimants on one drag. Resolve with explicit arbitration: give the innermost gesture
  a **direction + threshold** (row reveals only past a horizontal threshold, vertical scroll wins
  early), inset custom edge gestures away from the system edge, and prefer a visible button over a
  third nested gesture.
- Use the platform's gesture-recognizer precedence (iOS `require(toFail:)` / simultaneous recognition;
  Compose `pointerInput` consume rules / nested-scroll) deliberately — never leave arbitration to luck.

## 6. Haptic feedback — semantics map

Haptics confirm real, **discrete** events. They are an *augment*, never the sole signal. One haptic
per event; coalesce; never on a timer or per-scroll-tick.

### iOS (UIFeedbackGenerator / SwiftUI `.sensoryFeedback`)

| Family | API | Use for | Hard rule |
|---|---|---|---|
| **Selection** | `UISelectionFeedbackGenerator` / `.selection` | A value *changed* (picker tick, segmented control, slider step crossing) | Only on an actual change; pairs with visible motion. |
| **Impact** | `UIImpactFeedbackGenerator` (.light/.medium/.heavy/.soft/.rigid) / `.impact` | A control engaged, a snap, a boundary, a toggle | Match weight to perceived mass; don't use for outcomes. |
| **Notification** | `UINotificationFeedbackGenerator` / `.success` `.warning` `.error` | The **outcome** of a task (saved, caution, failed) | **Never `.success` on a failure.** `.warning` = recoverable; `.error` = failed. |

Core Haptics (`CHHapticEngine`) only for bespoke custom patterns — rare, justified moments.

### Android (`View.performHapticFeedback` / `HapticFeedbackConstants`, Compose `LocalHapticFeedback`)

| Constant / type | Use for | Note |
|---|---|---|
| `CONFIRM` | Positive outcome / commit | The success analogue. |
| `REJECT` | Failure / invalid | The error analogue; never use `CONFIRM` on failure. |
| `LONG_PRESS` | Long-press recognized | Confirms the gesture fired. |
| `CLOCK_TICK` / `TEXT_HANDLE_MOVE` | Discrete value change / selection | The selection analogue. |
| `GESTURE_START` / `GESTURE_END` | A gesture boundary | E.g. drag begin/commit. |
| Predictive-back progress | Back-gesture commit point | Couple to the predictive-back animation, not a constant buzz. |
| Compose `HapticFeedbackType.LongPress` / `TextHandleMove` | Compose-native equivalents | Prefer these in Compose code. |

### Cross-cutting haptic rules

- **Off-switch safe:** the UI must be 100% usable with system haptics disabled. A haptic may
  *accompany* a confirmation; it may never *be* the confirmation (also satisfies WCAG name/role/value
  and non-text-content expectations — outcome must be visible/announced too).
- **Truthful:** the haptic semantic must match the event (success vibe only on success).
- **Sparse:** discrete events only; no continuous/scroll-tick spam; coalesce duplicates.
- **Respect Reduce Motion / system settings** and battery — don't run the haptic engine idle.

## 7. Gesture discoverability

A gesture nobody can find is a feature nobody has. Anything beyond a plain tap needs at least one
affordance:

- **Visible handle / grabber** — a drag handle bar on a sheet, a reorder grip (≡) on a row.
- **Peek / overshoot hint** — reveal a sliver of the swipe action on load, or a one-time bounce.
- **First-run coachmark** — a single, dismissible hint; never a recurring nag.
- **Redundant visible control** — a ⋯ / button that does the same thing. **This is the preferred
  affordance because it doubles as the WCAG 2.5.1 / 2.5.7 alternative (§4)** — design once, satisfy
  both discoverability and the law.

Rule: a gesture that is *the only way* to do something **and** has no affordance is a defect on two
counts (discoverability + WCAG). Fix it with a visible control.

## 8. The gesture + haptics sign-off gate

Do not sign off a touch surface until all pass:

1. **Targets:** every interactive element ≥ 44 pt (iOS) / 48 dp (Android), clears WCAG 2.5.8 (24 px),
   ≥ 8 px/dp spacing; small glyphs have expanded hit areas. ✓
2. **Thumb zone:** primary actions in the natural arc; no destructive action under the resting thumb;
   verified on the biggest target device one-handed. ✓
3. **Gesture vocabulary:** standard gestures used for standard meanings; bespoke gestures justified. ✓
4. **WCAG alternatives:** every multipoint/path/drag gesture has a single-pointer / non-drag
   alternative written in its row (2.5.1, 2.5.7); essential-path exceptions documented. ✓
5. **System gestures:** no collision with iOS edge-back / Control Center / home indicator or Android
   predictive-back / shade / nav pill; nested gestures have explicit arbitration. ✓
6. **Haptics:** semantically correct (no `.success`/`CONFIRM` on failure), discrete, sparse, and the
   UI is fully usable with haptics off; outcome is also visible/announced. ✓
7. **Discoverability:** every non-tap gesture has an affordance, preferably the redundant visible
   control that also serves as the WCAG fallback. ✓
8. **Accessibility floor:** name/role/value on every control (4.1.2), reduced-motion respected,
   contrast clears 3:1 for the control/glyph (`doctrine/references/wcag-2.2-criteria.md`). ✓
