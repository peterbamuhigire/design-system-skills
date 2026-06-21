# iOS vs Android Idioms — element-by-element

The reference behind the Unify/Diverge decision. Each row: what the element is, the **iOS (HIG /
Liquid Glass)** native resolution, the **Android (Material 3 Expressive)** native resolution, and
the **parity call**. "Unify" = same value/behaviour both sides. "Diverge" = use each platform's
native form. Brand layers stay unified throughout (`doctrine/design-doctrine.md` §0).

Version gates: **Liquid Glass** is the iOS 26+ HIG material (translucent, refractive layered
surfaces); on older iOS fall back to standard HIG materials/vibrancy. **Material 3 Expressive** is
the M3 evolution (larger/looser shapes, springy motion, expanded tonal + shape tokens); requires
the M3 Expressive token set, else fall back to baseline Material 3.

---

## 1. Navigation

| Element | iOS (HIG / Liquid Glass) | Android (Material 3 Expressive) | Parity call |
|---|---|---|---|
| Primary destinations (3–5) | Tab bar, bottom, Liquid Glass material; SF Symbols | Bottom navigation bar (compact) → navigation rail (medium) → navigation drawer/pane (expanded) | **Diverge** — same destinations, native container per platform |
| Back navigation | Top-left chevron + **edge-swipe-back** gesture (system) | System **back gesture/button** (OS-owned, predictive back) + up-affordance in top app bar | **Diverge** — never put an iOS chevron on Android as the only back path |
| Hierarchical drill-in | `NavigationStack` push (slide-in from right) | Navigate within nav host; container-transform or shared-axis transition | **Diverge** (mechanism); **Unify** the hierarchy itself |
| Modal / focused task | Sheet (detent: medium/large), grabber; full-screen cover only for true takeover | Bottom sheet (modal/standard) or full-screen dialog; FAB may launch create flows | **Diverge** — both modal, different physics & affordances |
| Title / header | Large title that collapses to inline on scroll | Top app bar: center/small/medium/large, collapses on scroll | **Diverge** (form); **Unify** the title text |
| Search | Search bar in nav, or `.searchable`; often pull-to-reveal | `SearchBar` → `SearchView` (docked/full-screen); or search icon in app bar | **Diverge** |

## 2. Controls

| Control | iOS | Android | Parity call |
|---|---|---|---|
| On/off toggle | `Toggle` (green pill switch) | M3 `Switch` (tracked thumb, icon when on) | **Diverge** — same state, native widget |
| Selection from list | Picker / wheel / menu; context menu on long-press | Dropdown menu, `SegmentedButton`, or bottom-sheet chooser | **Diverge** |
| Date / time | Native `DatePicker` (wheel/calendar/compact) | M3 date picker (calendar) / time picker (clock dial) | **Diverge** — always native; calendar metaphors differ |
| Primary action | Filled/prominent button, or bar button; no FAB | **FAB** / extended FAB for the screen's primary create action | **Diverge** — FAB is Android-idiomatic, absent on iOS |
| Destructive confirm | Action sheet (red destructive role) | M3 dialog with text buttons, or bottom sheet | **Diverge** |
| Lists / rows | Inset-grouped `List`, disclosure chevrons, swipe actions | `ListItem`, dividers, swipe-to-dismiss, leading/trailing icons | **Diverge** (chrome); **Unify** row content |
| Pull-to-refresh | `.refreshable` (system spinner) | M3 `PullToRefresh` indicator | **Unify** behaviour, native indicator |
| Segmented control | `Picker(.segmented)` | M3 `SegmentedButton` | **Diverge** form |

## 3. Typography

| Aspect | iOS | Android | Parity call |
|---|---|---|---|
| System UI face | **SF Pro** (Dynamic Type styles: LargeTitle…Caption2) | **Roboto** (M3 type scale: Display/Headline/Title/Body/Label) | **Diverge** for *system* text only — both are allowed system defaults (see `doctrine/references/ai-slop-banned-fonts.md` caveat) |
| Branded display face | From approved font groups, embedded | Same approved face, same files | **Unify** — brand type is identical both sides |
| Scaling | Dynamic Type (respect user setting) | Font scale (sp units; respect setting) | **Unify** the intent: never hardcode, always scale |
| Type scale mapping | LargeTitle ≈ Display, Title ≈ Headline, Body ≈ Body, Footnote ≈ Label | per `doctrine/references/type-scale-and-spacing.md` | **Unify** the hierarchy; map names per platform |
| Min touch text/target | 44 pt | 48 dp | **Diverge** value; both satisfy `wcag-2.2-criteria.md` 24px floor |

## 4. Motion

| Moment | iOS | Android (Expressive) | Parity call |
|---|---|---|---|
| Screen-to-screen | Push slide / sheet present (UIKit/SwiftUI spring) | Shared-axis or container-transform; M3 Expressive **spatial springs** | **Diverge** — do not impose iOS slide on Android |
| Element emphasis | Subtle spring, scale-on-press | Expressive springy overshoot, larger displacement | **Diverge** — Expressive is intentionally bouncier |
| Loading | System activity indicator; skeletons | M3 circular/linear progress; skeletons | **Unify** the *strategy* (skeleton vs spinner), native renderer |
| Reduce Motion | Honour `Reduce Motion` | Honour `Remove animations` / reduced-motion | **Unify** — both must degrade gracefully |
| Ripple / feedback | No ripple; subtle highlight + haptic | M3 state-layer ripple on touch | **Diverge** — ripple is Android-only |

## 5. Gestures & system chrome

| Element | iOS | Android | Parity call |
|---|---|---|---|
| Edge back | Edge-swipe-back (must preserve) | System predictive-back gesture | **Diverge**, both must work — never disable |
| Status / nav bars | Safe-area insets, notch/Dynamic Island, home indicator | Edge-to-edge, system bars, gesture nav insets | **Diverge** — use each platform's inset API |
| Long-press | Context menu / preview (peek) | Context menu / selection mode | **Diverge** form, **Unify** that long-press is meaningful |
| Haptics | `UIFeedbackGenerator` (rich taxonomy) | `HapticFeedback` (more limited) | **Diverge** — match intensity to platform capability |
| Share | Share sheet (`UIActivityViewController`) | Android share sheet (`Intent.ACTION_SEND`) | **Diverge** — both system-owned, never custom |

---

## Quick rule

If the element carries **meaning, content, or brand** → **Unify**.
If the element is **how the user touches the OS** → **Diverge** to native.
When in doubt, ask: "Would a native-only user of this platform find this surprising?" If yes, diverge.
