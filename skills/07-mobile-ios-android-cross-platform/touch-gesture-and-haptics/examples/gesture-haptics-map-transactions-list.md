# Worked Example: Touch + Gesture + Haptics Map — Transactions List

A worked, applied touch-layer spec for the convention required by the engine (every craft skill ships
≥1 worked example). It exercises target sizing, thumb-zone ergonomics, the gesture vocabulary, the
**WCAG 2.5.1 / 2.5.7 alternatives**, and iOS + Android haptics on **one real screen**. It is
illustrative, not a live product brief.

**Brief:** Maduuka (a Chwezi merchant app). Screen: the **Transactions list** — a scrolling list of
payment rows, each tappable to open detail; each row has *Flag* and *Delete* actions; a top **Filter**
control; pull-to-refresh; and a bottom **Record payment** primary CTA. Device classes: compact + large
phone, one-handed. Targets: iOS 44 pt, Android 48 dp. Type for labels is **SF Pro** (iOS) / **Roboto**
(Android) — system UI faces, allowed; no banned fonts, no branded display needed on this utility screen
(`doctrine/design-doctrine.md`, `doctrine/references/ai-slop-banned-fonts.md`).

---

## 1. Layout & thumb zones

```
┌──────────────────────────────────────────┐  HARD zone (top — one-handed thumb can't reach)
│  Transactions                  [Filter ▾] │   Filter lives here on purpose: occasional, not urgent
├──────────────────────────────────────────┤
│  ⟳  pull-to-refresh hint                   │   STRETCH zone
│  ┌────────────────────────────────────┐   │
│  │ Aisha Nakato        UGX 250,000  ›  │   │   ROW: tap = open · swipe-left = actions · long-press = menu
│  │ Today 14:02                         │   │
│  └────────────────────────────────────┘   │
│  ┌────────────────────────────────────┐   │   (more rows…)
│  │ John Okello         UGX  40,000  ›  │   │
│  └────────────────────────────────────┘   │
│                                            │
├──────────────────────────────────────────┤  NATURAL zone (bottom — easy thumb reach)
│        [  +  Record payment  ]             │   PRIMARY CTA here, capsule, full-width-ish
└──────────────────────────────────────────┘
```

- **Primary CTA** (`Record payment`) sits in the **natural zone**, bottom, ≥ 44/48, clear of the home
  indicator / nav pill.
- **Filter** is in the **hard zone** — fine, it is occasional. **No destructive action** lives in the
  natural zone; Delete is reached only via a swipe *or its menu fallback*, never under the resting thumb.
- Verified one-handed on the **large** phone (worst case).

## 2. Per-element touch & gesture map

| Element | Gesture(s) | Target size | Thumb zone | Single-pointer / non-drag alternative (WCAG) | Discoverability |
|---|---|---|---|---|---|
| Transaction **row** | **Tap** → open detail | 44 pt / 48 dp (full row height ≥ 56) | natural→stretch | Tap *is* the baseline — no fallback needed | `›` chevron signals tappable |
| Row **actions** (Flag, Delete) | **Swipe-left** reveals buttons (path-based → 2.5.1) | each revealed button ≥ 44/48, 8 px apart | natural | **Long-press the row → context menu** with Flag / Delete; plus the same menu via a `⋯` affordance | partial swipe **peek** on first load + `⋯` button |
| **Reorder** (pin favourites) | **Drag** handle (≡) to move (dragging → 2.5.7) | handle ≥ 44/48 | stretch | **"Move up / Move down"** items in the row's long-press menu | visible **≡** grabber |
| **Filter** | **Tap** → menu | 44 pt / 48 dp | hard (ok, occasional) | Tap baseline | labelled `Filter ▾` |
| **Refresh** | **Pull-to-refresh** (path-based → 2.5.1) | gesture region = list | stretch | **Refresh** item in the overflow/Filter menu (a plain tap) | spinner peek hint on pull |
| **Record payment** CTA | **Tap** | full-width capsule, height ≥ 44/48 | **natural** | Tap baseline | labelled + `+` icon |

Every path/drag gesture above has a filled right column → **2.5.1 and 2.5.7 satisfied** (no blanks).

## 3. Gesture conflict resolution

- **Row swipe-left vs system back:** iOS left-edge swipe-back and Android predictive back own the
  screen edge. The row's reveal gesture is **swipe-*left*** (trailing edge) and only commits past a
  **horizontal threshold**, so vertical scroll wins early and the leading-edge system back is never
  contested. Custom horizontal gestures are inset from the very edge.
- **Swipe-row vs vertical scroll:** the row recognizer requires a dominant-horizontal direction +
  threshold (iOS `pan` direction gate / Compose `pointerInput` consume on horizontal); otherwise the
  list scrolls. No third nested horizontal gesture is added — the `⋯` button covers that need.
- **Pull-to-refresh vs top notch / Dynamic Island / shade:** the pull starts from the list content,
  not the screen top edge, so it doesn't fight Control Center / quick-settings.

## 4. Haptics map

| Event | iOS | Android | Rule applied |
|---|---|---|---|
| Swipe reveals row actions | `.impact(.light)` | `GESTURE_START` | control engaged; light, not an outcome |
| Long-press opens menu | `.impact(.medium)` | `LONG_PRESS` | confirms the gesture fired |
| Reorder picks up / drops a row | `.impact(.rigid)` on lift, `.selection` on each slot crossed | `GESTURE_START` / `CLOCK_TICK` per slot | discrete change ticks; pairs with visible motion |
| **Delete succeeds** | `.notification(.success)` | `CONFIRM` | outcome haptic tells the truth |
| **Delete fails** (offline) | `.notification(.error)` | `REJECT` | **never `.success`/`CONFIRM` on failure** |
| Filter applied (no results) | `.notification(.warning)` | (subtle) | recoverable caution |
| Pull-to-refresh completes | `.impact(.soft)` | `CONFIRM` | one event, not per frame |

- **Off-switch safe:** with haptics disabled, every outcome is still shown — Delete animates the row
  out + a toast; failure shows an inline banner. Haptics never the sole signal.
- Sparse: no haptic per scroll tick; the reorder `.selection` ticks are discrete slot crossings only.

## 5. State matrix (touch-relevant)

| State | Touch behaviour |
|---|---|
| Loading | rows are skeletons, **not tappable**; CTA disabled (no false affordance) |
| Content | as mapped above |
| Empty | "No transactions yet" + the **Record payment** CTA stays in the natural zone |
| Error (load) | inline retry button (tap, ≥ 44/48) — not a hidden gesture; `.error` / `REJECT` haptic |
| Offline | row actions queue; Delete shows "will sync"; input never lost (WCAG 3.3.7 redundant entry) |
| Permission denied | n/a here |
| Syncing | per-row progress; success haptic only on actual commit |

## 6. Sign-off gate (`references/gesture-and-haptics.md` §8 + `doctrine/references/wcag-2.2-criteria.md`)

1. Targets ≥ 44 pt / 48 dp, clear WCAG **2.5.8** (24 px), ≥ 8 px/dp spacing; chevron/handle hit areas
   expanded. ✓
2. Primary CTA in natural zone; no destructive action under resting thumb; large-phone one-handed
   verified. ✓
3. Standard gestures for standard meanings; no bespoke gesture without justification. ✓
4. **2.5.1 / 2.5.7:** swipe-actions, reorder-drag, pull-to-refresh each have a single-pointer / non-drag
   alternative (long-press menu / move buttons / refresh menu item) — no blank rows. ✓
5. No collision with iOS edge-back / Android predictive back / shade / home indicator; swipe threshold
   + direction arbitration set. ✓
6. Haptics truthful (`.error`/`REJECT` on failure, never success), discrete, sparse; UI usable with
   haptics off; outcomes also visible. ✓
7. Every non-tap gesture has an affordance; the `⋯` / menu controls double as the WCAG fallback. ✓
8. Name/role/value on row, buttons, menu items (4.1.2); reduced-motion respected; control glyphs clear
   3:1 contrast. ✓
