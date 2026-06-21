---
name: android-ui-ux-design
description: Specialized Android UI/UX design skill for premium Jetpack Compose apps. Use alongside android-development when Android screens must be beautiful, native, usable, accessible, and commercially credible.
status: active
metadata:
  portable: true
  category: 07-mobile-ios-android-cross-platform
  compatible_with:
  - claude-code
  - codex
---

# Android UI/UX Design
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Designing or reviewing Android app screens, Compose components, navigation, dashboards, forms, onboarding, or settings.
- The user asks for native Android UI polish, premium UX, mobile ergonomics, Material 3, or app pleasantness.
- An Android app is connected to a business backend and must feel trustworthy enough for real customers.

## Do Not Use When

- The task is not Android or Android-adjacent.
- The work is backend-only and has no user-facing Android surface.

## Required Inputs

- Target screens, user task, device classes, brand/product context, backend constraints, and any existing screenshots or Compose components.
- Confirm whether the deliverable is design guidance, implementation, review, QA, or documentation.

## Workflow

1. Load your platform's Android development/implementation skill for code and build standards.
2. State the typography and visual-quality intent against the Chwezi anti-slop charter — see `doctrine/design-doctrine.md` and `doctrine/references/ai-slop-banned-fonts.md` — before styling.
3. Define the primary mobile task, top-level destinations, and device classes.
4. Choose Material 3 components and adaptive navigation before custom patterns.
5. Model every Compose screen state: loading, content, empty, error, offline, permission denied, and syncing.
6. Apply the Android mobile quality gate before implementation or review sign-off.

## Android UX Standards

- Target **Material 3 Expressive** (the current 2026 standard) — not stock M3. State which expressive levers you use (shape scale up to 28dp `extraLarge`, spring motion, emphasis, containment, expressive components like button groups / FAB menu / loading indicators). See `references/material-3-expressive.md`.
- Bind colour to **M3 role tokens** (`MaterialTheme.colorScheme.*`), never raw hex. Ship a designed **light + dark** `ColorScheme`. **Dynamic colour (Material You)** is opt-in for branded products — default to a **fixed brand seed** (HCT-generated tonal ramps); state the choice. Certify contrast WCAG 2.2 AA regardless.
- Support **predictive back gestures** via `PredictiveBackHandler` / navigation predictive-back — interruptible, progress-tracked, reversible on cancel. Prefer M3 components that ship predictive-back dismissal. See `references/android-motion.md`.
- **Roboto is the Android system face** and is allowed **only as the platform default/fallback** — it is **banned as a deliberate Chwezi brand or display primary**. Branded display/headline type must come from an **approved font category** (`doctrine/references/font-groups-and-usage.md`), pass the banned-list check, and be paired (never monotype).
- Use Material 3, Compose, semantic tokens, and adaptive layout by default.
- Use bottom navigation for 3-5 primary destinations on compact screens; use navigation rail or pane layouts on larger screens.
- Minimum touch target is 48 dp.
- Respect edge-to-edge layout, system bars, back navigation, and platform permission flows.
- Use `WindowSizeClass`, not hardcoded tablet checks.
- Business reports over 25 rows should use table-first or dense list patterns, not endless cards.
- Every primary workflow must work offline or fail with a clear recovery path when the domain requires field use.
- Support TalkBack, font scaling, dark mode, contrast, and reduced motion.

## Quality Standards

- Android screens feel native to Material 3 and the app's domain.
- Navigation, state handling, touch targets, typography, and accessibility are verified on compact and expanded layouts where applicable.
- Premium UX gate categories must score at least 8/10 before sign-off.

## Anti-Patterns

- Squeezing web layouts into a phone UI.
- Building card walls for dense reports.
- Ignoring TalkBack, font scaling, offline states, or Android back behavior.

## Outputs

- Android UI brief, Compose component guidance, navigation model, state matrix, accessibility notes, or review findings.

## Examples

- `examples/android-screen-spec.md` — a worked Android screen spec (Maduuka "Today" dashboard): visual-quality intent stated against the doctrine, Material 3 Expressive component/colour/type decisions, predictive-back motion, full state matrix, and the accessibility sign-off gate.

## References

- `references/material-3-expressive.md` — the current Android visual standard: Material 3 Expressive levers, the M3 role-based colour system, dynamic colour (Material You) vs fixed brand seed, type-scale roles, predictive back, and adaptive layout.
- `references/android-motion.md` — Android motion: spring/motion-scheme tokens, predictive-back gesture motion, signature moments (container transform, shape morph, shared element), and the reduced-motion path.
- `doctrine/design-doctrine.md` — the always-load anti-slop charter governing typography, colour, and visual identity.
- `doctrine/references/ai-slop-banned-fonts.md` and `doctrine/references/type-scale-and-spacing.md` for type choices, scale, and spacing.
  - Mobile-platform font caveat: Android's **Roboto** is the OS/Material system face — it is allowed only **as the platform system default**, never as a deliberate Chwezi brand/display primary (it is banned for that). Any custom branded type must come from the approved font categories (`doctrine/references/font-groups-and-usage.md`) and avoid the banned list.
- `references/jetpack-compose-ui.md` for Compose-specific Material 3, layout, animation, navigation, and component patterns.
<!-- dual-compat-end -->
