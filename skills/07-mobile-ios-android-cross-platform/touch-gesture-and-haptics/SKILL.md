---
name: touch-gesture-and-haptics
description: Use when a mobile screen needs touch-target sizing, thumb reach, tap/press/swipe/drag/pinch rules, gesture alternatives, discoverability, conflict resolution, or truthful iOS/Android haptics. Do not use for navigation architecture or motion choreography; pair with platform and motion skills.
metadata:
  portable: true
  category: 07-mobile-ios-android-cross-platform
  compatible_with:
  - claude-code
  - codex
---

# Touch, Gesture, and Haptics
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Sizing and spacing **hit/touch targets** for a phone, tablet, or foldable, or auditing why
  controls feel "fiddly" or mis-fire.
- Designing **thumb-zone ergonomics** — placing primary actions where a one-handed thumb actually
  reaches, and demoting destructive actions out of the easy-reach arc.
- Specifying a **gesture vocabulary** for a screen (tap, double-tap, long-press, swipe, drag,
  pinch, edge-swipe) and the **single-pointer fallback** every path/drag gesture legally needs.
- Mapping **haptic feedback** to real events with correct semantics on iOS (impact / notification /
  selection) and Android (view-level `HapticFeedbackConstants` / predictive-back progress).
- Resolving **gesture conflicts** (a swipe row inside a swipe carousel inside a back-swipe edge) and
  making non-obvious gestures **discoverable** rather than hidden.

## Do Not Use When

- You need the broad native screen pattern (navigation container, components, state matrix) — start
  at `ios-ui-ux-design` or `android-ui-ux-design`; come here for the touch/gesture/haptic detail.
- The parity decision (which gestures unify vs diverge across iOS/Android) is the question — use
  `cross-platform-design-parity`; return here to specify each side's gesture + haptic.
- The work is animation choreography of the transition itself (timing curves, container transform) —
  use `08-motion-and-interaction`; this skill owns the *input* gesture and its *haptic*, not the
  visual transition physics.
- It is backend/API work with no touch surface.

## Required Inputs

| Input | Source | Evidence |
|---|---|---|
| Screen, actions, frequency, consequence, and one-handed task | Product/design | Interactive-element inventory and priority/destructive classification |
| Platform/device/input contexts | Support policy and platform teams | iOS/Android, phones/tablets/foldables, assistive input needs |
| Existing gestures, system reservations, and haptic support | Current build/platform contract | Gesture recognisers, conflicts, APIs, and disabled/reduced settings |

- The screen(s) and the primary one-handed task; target device classes and the largest reachable
  canvas (big-phone one-handed reach is the worst case).
- Which actions are **primary / frequent**, which are **destructive / rare** (drives thumb-zone
  placement), and which gestures (if any) are **the only way** to do something (drives the
  WCAG 2.5.1 / 2.5.7 fallback audit).
- Platform: iOS, Android, or both (haptic API and system-gesture reservations differ).
- Whether haptics are core to the experience or decorative (they must never be load-bearing).

## Workflow

1. **Inventory every interactive element and its gesture.** One row per element: what it is, the
   gesture(s) that operate it, and whether that gesture is the *only* path to the action.
2. **Size and space the targets.** Floor is **WCAG 2.5.8: 24×24 CSS px**; the touch platform floor is
   higher and is what you actually ship — **iOS 44×44 pt**, **Android 48×48 dp** — with ≥ 8 px/dp
   between adjacent targets. Small visual glyphs get an expanded *hit area* (extend the touch region,
   not the pixels). See `references/gesture-and-haptics.md` §1 and `doctrine/references/wcag-2.2-criteria.md`.
3. **Place by thumb zone.** Map the screen to the reach arc (natural / stretch / hard) for a
   one-handed grip. Primary actions land in the natural arc (bottom-center to bottom-side); destructive
   or rare actions go to the hard zone or require deliberate confirmation. See §2.
4. **Define the gesture vocabulary and resolve conflicts.** Pick from the standard vocabulary
   (tap, long-press, swipe, drag, pinch, edge-swipe), and check each against the **system-reserved**
   gestures you must not fight (iOS edge-back / Control Center / Dynamic Island; Android predictive
   back / edge-to-edge / quick-settings). Nest gestures only with a clear arbitration rule. See §3, §5.
5. **Apply the WCAG gesture-alternative rules (mandatory).** For **2.5.1 Pointer Gestures**, every
   multipoint (pinch/rotate) or path-based (swipe-to-delete, slider drag, draw) gesture has a
   **single-pointer** equivalent (a button, a tap-target, a menu item). For **2.5.7 Dragging Movements**,
   every drag (reorder, slide-to-confirm, drag-to-dismiss) has a **non-drag** alternative (tap targets,
   up/down buttons, a menu). Write the fallback in the same row as the gesture — never leave it implicit.
   See `references/gesture-and-haptics.md` §4 (the rule table).
6. **Map haptics to discrete, truthful events.** One haptic per real event, semantically correct:
   iOS `.selection` on value change, `.impact` on engagement, `.notification(.success/.warning/.error)`
   on outcomes (never `.success` on a failure); Android `CONFIRM` / `REJECT` / `LONG_PRESS` /
   `GESTURE_*` and predictive-back progress. The UI must be **fully usable with haptics off**, and
   haptics never substitute for a visible/audible confirmation. See §6.
7. **Make non-obvious gestures discoverable.** Any gesture that is not the platform-standard tap needs
   an affordance: a visible handle, a peek/overshoot hint, a first-run coachmark, OR a redundant
   visible control (which doubles as the WCAG fallback). A hidden-only gesture is a defect. See §7.
8. **Run the gesture + haptics gate** (`references/gesture-and-haptics.md` §8) before sign-off.

## Decision Rules

| Condition | Choice | Wrong-choice failure |
|---|---|---|
| Gesture is path-based, multipoint, or dragging | Provide visible single-pointer/non-drag alternative | Gesture-only action fails accessibility and discoverability |
| Gesture collides with system back/edge reservation | Relocate or change gesture; preserve system behaviour | Arbitration becomes unreliable and users lose navigation |
| Haptic reports an outcome | Map truthful success/warning/error semantics plus visible cue | Lying or load-bearing haptics miscommunicate state |
| Small visual control is required | Expand hit region without inflating glyph | Tiny target causes misses; oversized icon harms hierarchy |

## Capability Contract

- Must inspect the interactive build/prototype and test representative touch/accessibility paths; review is read-only unless remediation is requested.
- May edit in-scope gesture/haptic UI. Do not override system-reserved gestures, collect sensor data, or release without device evidence and authority.

## Degraded Mode

- If actions, consequences, platform, or gesture ownership are unknown, stop final mapping and request the missing contract.
- Without device/haptic access, provide a gesture map marked tactile behaviour unverified. Recover conflict or inaccessible gestures by enabling the visible alternative, removing the collision, and retesting with haptics disabled.

## Quality Standards

- Every action has an adequate target, discoverable operation, system-conflict result, accessible alternative where required, and truthful non-load-bearing feedback.
- Evidence records devices, input methods, target measurements, gesture conflicts, alternatives, haptic-off operation, and failures corrected.

## Anti-Patterns

- **Sub-floor or crowded targets** — 32-px icons jammed edge-to-edge, or a real tap target smaller
  than 44 pt / 48 dp because the *glyph* is small (extend the hit area instead).
- **Primary action in the dead zone** — the main CTA top-left where a one-handed thumb cannot reach,
  while a destructive action sits under the resting thumb.
- **Gesture-only actions with no visible alternative** — swipe-to-delete, pinch-to-zoom, or
  drag-to-reorder as the *only* path. This fails WCAG 2.5.1 / 2.5.7 and is the #1 violation here.
- **Fighting system gestures** — putting a custom swipe on the screen edge that collides with iOS
  back-swipe / Android predictive back, or a pull-down that fights Control Center / quick settings.
- **Haptic spam / lying haptics** — buzzing every scroll tick, firing `.success` on an error, or
  using a haptic as the *only* signal that something happened.
- **Hidden gestures** — a long-press menu or swipe action with zero affordance, discoverable only by
  accident, and no fallback control.
- **Pixel-cloning gestures across platforms** — porting iOS swipe-back to Android instead of using
  predictive back, or vice-versa (route that decision through `cross-platform-design-parity`).

## Outputs

| Output | Consumer | Evidence and acceptance |
|---|---|---|
| Touch/gesture/haptic map | Mobile design and engineering | Element, target, reach zone, gesture, alternative, conflict, haptic, and affordance are explicit |
| Interaction gate | Accessibility and platform QA | Representative devices verify targets, alternatives, system gestures, and haptic-off usability |

- A **touch & gesture map** for the screen: a per-element table (element · gesture · target size ·
  thumb zone · single-pointer / non-drag alternative · haptic · discoverability affordance), the
  thumb-zone diagram, the system-gesture conflict notes, and the WCAG 2.5.1 / 2.5.7 / 2.5.8 sign-off.

## Examples

- `examples/gesture-haptics-map-transactions-list.md` — a worked touch+gesture+haptics map for one
  real mobile screen (Maduuka transactions list + row actions): every gesture sized, thumb-zoned,
  given its single-pointer / non-drag WCAG alternative, and mapped to an iOS and Android haptic, with
  the discoverability affordances and the gate end to end.

## References

- `references/gesture-and-haptics.md` — the canonical rules: target sizing (WCAG 2.5.8 / platform
  floors), thumb-zone ergonomics, the gesture vocabulary, the **WCAG 2.5.1 / 2.5.7 gesture-alternative
  rule table** (the legal core of this skill), the iOS + Android haptic semantics map, gesture
  discoverability, conflict/system-gesture reservation table, and the sign-off gate.
- `doctrine/references/wcag-2.2-criteria.md` — the accessibility floor: **2.5.1** pointer gestures,
  **2.5.7** dragging movements, **2.5.8** target size (24×24 CSS px minimum; aim 44 pt / 48 dp on
  touch), plus reduced-motion and name/role/value rules these targets must clear.
- `doctrine/design-doctrine.md` — the always-load anti-slop charter; §0 (looking authored) is why a
  deliberate, discoverable, native gesture set beats a copied generic one.
- `doctrine/references/ai-slop-banned-fonts.md` for any on-screen label type, and the SF Pro / Roboto
  system-font caveat (allowed as platform UI text only).
- Pair with `ios-ui-ux-design` and `android-ui-ux-design` (same group) for the full native screen, and
  `cross-platform-design-parity` to decide which gestures unify vs diverge before specifying each side.
<!-- dual-compat-end -->
