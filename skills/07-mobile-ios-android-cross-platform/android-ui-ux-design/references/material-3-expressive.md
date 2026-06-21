# Reference: Material 3 Expressive (the current Android visual standard)

What "current, native, premium Android" means in 2026. Source: Google Material Design 3 /
Material 3 Expressive (m3.material.io), the Android 16 / Android Developers Compose guidance,
and the Jetpack Compose Material3 library (`androidx.compose.material3`, the stable M3 line plus
the expressive additions). Use this when stating the visual-quality intent and when choosing
components. **AA contrast remains the floor — see `doctrine/references/wcag-2.2-criteria.md`.**

---

## 1. What Material 3 Expressive is (and is not)

Material 3 Expressive is **not a new design system** — it is the emotive, motion-and-shape-forward
layer on top of Material 3 (M3). M3 gives the tokens, components, and dynamic colour; Expressive
turns up **shape, motion, emphasis, and containment** so a screen reads as intentional and
branded rather than a flat default grid. It is the answer to the doctrine's anti-slop mission on
Android: a stock M3 screen with default shapes and no motion is the convergent "AI mean" — Expressive
is how you push toward the *authored* look.

Expressive ships through the same `androidx.compose.material3` artifacts (use the current stable
release; the expressive APIs arrived in the 1.4.x line). Adopt it deliberately, screen by screen —
not as blanket decoration.

### The five Expressive levers (state which you are using, and why)
1. **Shape & morph** — components carry distinct corner shapes from the **shape scale**
   (`extraSmall` 4dp → `extraLarge` 28dp), and key controls (FAB, buttons, loading indicators)
   **morph shape** on press/interaction instead of only changing colour. Shape is a primary
   brand signal, not decoration.
2. **Emphasis via size + colour roles** — Expressive uses bolder size jumps and saturated
   role colours to make the single primary action unmistakable (ties to the doctrine's "one
   strong intentional choice").
3. **Motion physics** — spring-based, not linear; see `references/android-motion.md`.
4. **Containment** — grouping with filled/tonal containers and clear surfaces rather than hairline
   dividers, so hierarchy is read by surface, not by lines.
5. **New/updated components** — e.g. **button groups**, **split button**, **FAB menu**, **loading
   indicators**, expressive **toolbars** and **navigation** — prefer these over hand-rolled custom
   controls.

---

## 2. The M3 colour system — roles, not raw hex

M3 colour is **role-based**. You never paint a component with a literal hex in app code; you bind
it to a **colour role token** so light/dark and dynamic theming work automatically.

| Role family | Tokens (examples) | Use |
|---|---|---|
| **Primary** | `primary`, `onPrimary`, `primaryContainer`, `onPrimaryContainer` | The one main action / brand anchor |
| **Secondary** | `secondary`, `secondaryContainer`, … | Less-prominent accents, chips, filters |
| **Tertiary** | `tertiary`, `tertiaryContainer`, … | Contrasting accent to balance primary/secondary |
| **Error** | `error`, `errorContainer`, `onError…` | Validation, destructive, alerts |
| **Surface tiers** | `surface`, `surfaceContainerLowest/Low/…/Highest`, `surfaceVariant`, `inverseSurface` | Elevation-by-tone: M3 expresses depth through **surface tone tiers**, not heavy shadows |
| **Outline** | `outline`, `outlineVariant` | Borders, dividers, focus rings |

In Compose: read these as `MaterialTheme.colorScheme.primary`, `…surfaceContainerHigh`, etc. Never
hardcode `Color(0xFF…)` for themable surfaces.

### Dynamic colour (Material You) — current rule
- **Dynamic colour** derives the full tonal palette from a seed — on Android 12+ that seed is the
  user's **wallpaper** (`dynamicLightColorScheme(context)` / `dynamicDarkColorScheme(context)`),
  via the HCT (Hue-Chroma-Tone) colour space and the tonal-palette generator.
- **Decision rule for branded products:** dynamic colour makes the app feel native to *the user's
  device*, but it **surrenders brand control**. For a Chwezi-branded commercial app, the default is
  a **fixed brand `ColorScheme` seeded from the brand colour** (HCT-generated tonal palettes for
  light + dark), and dynamic colour is offered only as an **opt-in theme** where personalization is
  a feature. State which you chose. Either way the palette is generated as full tonal ramps, not
  ad-hoc swatches — this is the Android analogue of the engine's OKLCH ramp discipline.
- Always ship a **light and a dark** `ColorScheme`; never derive dark by naive inversion.
- Whatever the source, **certify contrast against WCAG 2.2 AA** (4.5:1 body, 3:1 large/UI) — dynamic
  colour does not guarantee it.

---

## 3. Typography — the system face vs. the brand face

- The M3 **type scale** has 15 named roles across Display / Headline / Title / Body / Label
  (each Large/Medium/Small). Use these roles (`MaterialTheme.typography.headlineMedium`, etc.) — do
  not invent ad-hoc sizes.
- **Roboto is the Android system face** and the M3 default. Under the Chwezi anti-slop charter,
  Roboto is **allowed only as the platform system default / fallback** — it is **banned as a
  deliberate Chwezi brand or display primary**, because shipping stock Roboto everywhere is exactly
  the unconsidered, convergent default the doctrine exists to remove. Any **branded display/heading
  type must come from an approved font group** (`doctrine/references/font-groups-and-usage.md`),
  pass the banned-list check (`doctrine/references/ai-slop-banned-fonts.md`), and be paired — never
  monotype. A common, defensible split: branded display/headline from an approved group, Roboto (or
  the chosen body workhorse) for dense body/label roles.
- Respect **font scaling** (sp units, up to 200%) and per-app/system Dynamic-Type-equivalent text
  size — never lock text to fixed dp.

---

## 4. Predictive back (mandatory on modern Android)

**Predictive back gestures** show the user where a back swipe will take them *before they commit*:
the current screen scales/translates to reveal the destination (or the launcher) under the
in-progress swipe.

- It is **system-wide and opt-in per app**: declare support, then it animates back navigation,
  cross-activity, and custom in-app transitions.
- In Compose, use the **`PredictiveBackHandler`** API (and the Material3/navigation predictive-back
  support) so back is interruptible and reversible — the user can drag partway and release to cancel.
- **Never** consume the back gesture with a plain non-predictive handler that blocks the animation,
  and never trap the user (back must always have a defined destination or a confirmed exit).
- Pair the destination reveal with the system's **back-progress** value so the animation tracks the
  finger — this is a motion concern; see `references/android-motion.md`.

---

## 5. Adaptive & layout (unchanged baseline, restated)

- Drive layout from **`WindowSizeClass`** (Compact / Medium / Expanded) — never hardcoded device or
  orientation checks.
- **Navigation adapts to width:** bottom navigation bar (3–5 destinations) on Compact → **navigation
  rail** on Medium → **navigation drawer / list-detail or supporting panes** on Expanded. Use the
  adaptive navigation-suite and canonical layouts (list-detail, supporting-pane, feed).
- **Edge-to-edge is the default** on Android 15+ (apps draw behind system bars); handle insets with
  the window-insets APIs so content is never occluded.
- Minimum touch target **48 × 48 dp** (Material), comfortably above the WCAG 2.2 §2.5.8 24 px floor.

---

## 6. Quick adoption checklist (state each before sign-off)

- [ ] Colour bound to **role tokens**, not raw hex; **light + dark** `ColorScheme` both shipped.
- [ ] Brand vs. **dynamic colour** decision stated (default: fixed brand seed; dynamic = opt-in).
- [ ] Type uses M3 **type-scale roles**; branded display from an **approved font group**, Roboto only
      as system/body fallback (never the deliberate display primary).
- [ ] **Expressive levers** named (shape scale, motion, emphasis, containment, expressive components).
- [ ] **Predictive back** supported via `PredictiveBackHandler` / nav predictive-back, interruptible.
- [ ] **Edge-to-edge** with insets handled; `WindowSizeClass`-driven adaptive navigation.
- [ ] Contrast **certified WCAG 2.2 AA**; touch targets ≥ 48dp; font scaling to 200%.
