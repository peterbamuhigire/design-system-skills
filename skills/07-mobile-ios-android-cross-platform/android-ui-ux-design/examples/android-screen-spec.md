# Worked Example: Android Screen Spec — Maduuka "Today" dashboard

A worked Android screen specification produced by this skill. Brief: **Maduuka** (a retail/POS
product for African duka/shop owners) needs a **"Today" home dashboard** for the field/owner mobile
app — daily sales at a glance, the current shift's transactions, and one primary action (record a
sale). The owner uses a mid-range Android phone, often on patchy data. This is the artifact the
skill is meant to emit: the visual-quality intent stated against the doctrine first, then the
component/colour/type/motion/state decisions, then the gate.

> This is a **spec**, not production code. It shows *how decisions are made and stated*; the
> implementation skill (`jetpack-compose-ui` / your Android dev skill) turns it into Compose.

---

## 0. Visual-quality intent (stated before styling — doctrine §2)

- **Anti-slop stance:** This will not ship as stock Material 3 with default Roboto everywhere and a
  flat card grid — that is the convergent default. The authored signature here is **one expressive
  shape language + a container-transform into the sale flow + a fixed brand palette**.
- **Type:** Branded display/headline from an **approved font category** —
  `03-modern-product-grotesque` (a confident product display for the big "Today" + the money
  figure) paired with a body workhorse from `08-body-ui-workhorses` for dense numbers/labels. **Roboto
  is used only as the system fallback** for label/body roles if no body family is embedded — it is
  **not** the deliberate display face (Roboto-as-brand is banned, doctrine
  `ai-slop-banned-fonts.md`). Choice checked against the banned list; pairing, not monotype.
- **Colour:** **Fixed brand `ColorScheme`** seeded from Maduuka brand green (HCT-generated full tonal
  ramps, light + dark). Dynamic colour (Material You) is **deliberately NOT the default** — a
  commercial brand keeps colour control; we may later expose "match my wallpaper" as an opt-in.
- **Why this is defensible:** retail owners decide in seconds (doctrine: colour communicates primary
  meaning instantly) — the day's net figure is the single loudest element; everything else recedes.

---

## 1. Task, destinations, device classes

- **Primary task:** see today's money position and **record a sale** in ≤2 taps.
- **Top-level destinations (4 → bottom nav on Compact):** Today · Sales · Stock · More.
- **Device classes:** Compact (phone, primary) → bottom navigation bar. Medium (small tablet/foldable
  open) → **navigation rail**. Expanded → rail + **list-detail** (list of transactions ⟷ detail).
  Driven by `WindowSizeClass`, never a hardcoded tablet check.

---

## 2. Layout & components (Material 3 Expressive)

| Region | Decision |
|---|---|
| **App chrome** | Edge-to-edge (Android 15+); status/nav bar insets handled; large/expressive top app bar that collapses on scroll. |
| **Hero "Today" card** | `surfaceContainerHigh`, corner radius **28dp** (shape-scale `extraLarge`) — the one oversized, expressive container. Holds net sales figure (Display Large, brand display font) + delta chip vs yesterday. |
| **KPI row** | 3 tonal stat tiles (sales count, items sold, cash vs mobile-money) in `secondaryContainer`; radius 16dp. Monetary values via `CurrencyFormatter.formatStat()` (compact ≥1M). |
| **Recent transactions** | Dense **list** (not card wall) — would exceed 25 rows on a busy day, so list/table-first per the report-table policy. Each row tappable. |
| **Primary action** | **Extended FAB** "Record sale", `primary` role, anchored bottom-end above the nav bar. Shape-morphs on press (Expressive). This is the single loud action. |
| **Navigation** | Bottom nav (Compact) → rail (Medium) → drawer/list-detail (Expanded). |

Spacing: 16dp screen padding (Compact), 8–16dp between items; touch targets ≥48dp.

---

## 3. Colour roles (bound to tokens, not hex)

| Element | Role token |
|---|---|
| FAB / primary action | `primary` / `onPrimary` |
| Hero card surface | `surfaceContainerHigh` / `onSurface` |
| Net figure (positive) | `primary`; (negative day) `error` |
| KPI tiles | `secondaryContainer` / `onSecondaryContainer` |
| Delta chip (up) | `tertiaryContainer`; (down) `errorContainer` |
| Dividers / row outline | `outlineVariant` |

**Light + dark** both shipped (dark is a designed `ColorScheme`, not inverted). **Contrast certified
WCAG 2.2 AA:** net figure and body ≥ 4.5:1; FAB label, chips, and icons ≥ 3:1 (designed with APCA,
certified with the WCAG ratio — see `doctrine/references/wcag-2.2-criteria.md`).

---

## 4. Type roles

| Text | M3 role | Face |
|---|---|---|
| "Today" / screen title | Headline Large | Approved display (`03-modern-product-grotesque`) |
| Net sales figure | Display Large | Approved display |
| KPI numbers | Title Medium | Body workhorse (`08-body-ui-workhorses`) |
| Transaction rows / labels | Body Medium / Label Large | Body workhorse, **Roboto fallback** if unembedded |

All sizes in **sp**; layout verified at **200% font scale** without clipping.

---

## 5. Motion (see `references/android-motion.md`)

- **Container transform:** tapping a transaction row (or the FAB) morphs into the detail/record
  screen; **predictive back** morphs it back — outgoing screen scales toward ~0.9 and tracks the
  swipe via `PredictiveBackHandler`, springs back on cancel.
- **Spring tokens** from the M3 motion scheme; no ad-hoc `tween` durations.
- **List:** `animateItem()` on new sales so a fresh transaction slides in.
- **Loading:** M3 loading indicator + skeleton rows while today's data syncs — not a bare centred spinner.
- **Reduced motion:** with system animations off, container transform degrades to a cross-fade;
  predictive-back navigation still works; focus/selection feedback kept.

---

## 6. State matrix (every state designed)

| State | Treatment |
|---|---|
| **Loading** | Skeleton hero + skeleton rows; top app bar visible. |
| **Content** | As specified above. |
| **Empty** (no sales yet today) | Friendly empty state, 48dp icon, "Record your first sale" CTA = the FAB action. |
| **Error** (load failed) | Inline error with **Retry**; last-synced cached figure still shown if available. |
| **Offline** | Banner "Offline — showing last sync at HH:MM"; recording a sale **queues** and syncs later (offline-first). |
| **Syncing** | Subtle progress in app bar; queued-sale count chip. |
| **Permission denied** (e.g. notifications) | Non-blocking; explain value, offer settings deep-link. |

---

## 7. Accessibility & sign-off gate

- **TalkBack:** hero reads "Today, net sales 1.24 million shillings, up 8% on yesterday"; FAB has
  content description "Record sale"; rows expose name + role + state (4.1.2).
- **Touch targets** ≥ 48dp (> WCAG 2.2 §2.5.8 24px floor). **Dragging** (swipe-to-void a row) has a
  tap alternative (§2.5.7). **Focus** not obscured by the FAB/app bar (§2.4.11).
- **Font scaling** 200%, **dark mode**, **contrast**, **reduced motion** all verified on Compact +
  Expanded.
- **Premium UX gate:** each category (native feel, navigation, state handling, typography, colour,
  motion, accessibility) scored — all **≥ 8/10** before sign-off.

### What makes this *not* slop (one-line audit)
Fixed brand palette + an oversized 28dp expressive hero + a real container-transform-with-predictive-back
into the sale flow + branded display type — none of which a templating tool emits by default. Roboto
stays in its lane as a fallback, never the brand voice.
