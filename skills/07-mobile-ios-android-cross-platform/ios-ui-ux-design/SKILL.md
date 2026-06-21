---
name: ios-ui-ux-design
description: Specialized iOS UI/UX design skill for premium SwiftUI apps. Use alongside ios-development when iPhone or iPad screens must be beautiful, native, usable, accessible, and commercially credible.
status: active
metadata:
  portable: true
  category: 07-mobile-ios-android-cross-platform
  compatible_with:
  - claude-code
  - codex
---

# iOS UI/UX Design
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Designing or reviewing iOS/iPadOS screens, SwiftUI components, navigation, dashboards, forms, onboarding, or settings.
- The user asks for native iOS polish, premium UX, pleasantness, or App Store-quality experience.
- A business app must feel trustworthy, fast, accessible, and Apple-native.

## Do Not Use When

- The task is not iOS, iPadOS, or Apple-platform adjacent.
- The work is backend-only and has no user-facing iOS surface.

## Required Inputs

- Target screens, user task, device classes, brand/product context, backend constraints, and any existing screenshots or SwiftUI components.
- Confirm whether the deliverable is design guidance, implementation, review, QA, or documentation.

## Workflow

1. Load your platform's iOS development/implementation skill for code and build standards.
2. State the typography and visual-quality intent against the Chwezi anti-slop charter — see `doctrine/design-doctrine.md` and `doctrine/references/ai-slop-banned-fonts.md` — before styling.
3. Define the primary iOS task, top-level destinations, navigation hierarchy, and device classes.
4. Choose SwiftUI-native patterns before custom controls.
5. Model every screen state: loading, content, empty, error, offline, permission denied, and syncing.
6. Apply the current platform material and feedback standards — **Liquid Glass** chrome, **SF Symbols**, **Dynamic Type**, and **haptics** — per `references/hig-liquid-glass.md` and `references/ios-sensory-and-haptics.md`.
7. Apply the iOS mobile quality gate before implementation or review sign-off.

## iOS UX Standards

- Use SwiftUI, platform-native navigation stacks, tab bars, sheets, forms, lists, menus, and toolbars.
- Minimum touch target is 44 pt.
- Preserve swipe-back and native gesture expectations.
- Support Dynamic Type, VoiceOver, Reduce Motion, Increase Contrast, Dark Mode, and SF Symbols consistency.
- **Liquid Glass (iOS 26):** apply the Liquid Glass material to the **chrome/navigation layer only** (tab bars, toolbars, nav bars, sheets, controls) — never to content; never glass-on-glass; build on standard system containers so it adapts and stays accessible. Verify under Reduce Transparency / Increase Contrast / Reduce Motion. See `references/hig-liquid-glass.md`.
- **SF Symbols 7:** use system (or template-drawn custom) symbols, weight-matched to adjacent Dynamic Type styles; animate as feedback only.
- **Dynamic Type:** use semantic text styles (`body`, `headline`, …), never hardcoded sizes; layouts must survive the largest accessibility size (**AX5**) — stack at large sizes, never clip critical labels. A branded display face must scale relatively, not freeze.
- **Haptics:** map feedback to real, discrete events with correct semantics (`.success`/`.warning`/`.error` for outcomes — never `.success` on failure; `.selection` on change). UI stays fully usable with haptics disabled. See `references/ios-sensory-and-haptics.md`.
- Use sheets for focused tasks; avoid full-screen covers unless the workflow truly requires takeover.
- Avoid Android-style components, web-like navigation, and cramped desktop tables on phones.
- For iPad, use split views, sidebars, and multi-column layouts where they improve productivity.

## Quality Standards

- iOS screens feel native to SwiftUI and Apple platform conventions.
- Navigation, state handling, touch targets, Dynamic Type, VoiceOver, and iPad adaptations are verified where applicable.
- Premium UX gate categories must score at least 8/10 before sign-off.

## Anti-Patterns

- Squeezing web layouts into a phone UI.
- Copying Android component patterns into iOS.
- Ignoring VoiceOver, Dynamic Type, swipe-back, offline states, or sheet/navigation conventions.

## Outputs

- iOS UI brief, SwiftUI component guidance, navigation model, state matrix, accessibility notes, or review findings.

## References

- `doctrine/design-doctrine.md` — the always-load anti-slop charter governing typography, colour, and visual identity.
- `doctrine/references/ai-slop-banned-fonts.md` and `doctrine/references/type-scale-and-spacing.md` for type choices, scale, and spacing.
  - Mobile-platform font caveat: iOS's **San Francisco / SF Pro** is the Apple system face — a platform-native default, allowed (and correct) for native iOS UI; it is not a Chwezi-chosen primary and carries no slop penalty. A deliberate branded display face should still come from the approved font groups (`doctrine/references/font-groups-and-usage.md`) and avoid the banned list.
- `references/hig-liquid-glass.md` for the iOS 26 **Liquid Glass** material, **SF Symbols 7**, and **Dynamic Type** — the current Apple platform-design baseline (and the SF-Pro-vs-branded-display rule).
- `references/ios-sensory-and-haptics.md` for **haptics** / sensory feedback semantics (Core Haptics, SwiftUI `sensoryFeedback`) and the accessibility rules around them.
- `references/swiftui-design.md` for SwiftUI-native layout, navigation, forms, accessibility, and visual polish.
- `references/swiftui-pro-patterns.md` for advanced SwiftUI layout, identity, animation, and performance patterns.
- `references/ios-uikit-advanced.md` for UIKit diffable data sources, compositional layout, custom transitions, and UIKit interop.
- `doctrine/references/wcag-2.2-criteria.md` for the accessibility floor (contrast, target size, reduced motion) that all of the above must clear.

## Examples

- `examples/ios-screen-spec.md` — a worked iOS screen spec (a "Send Payment" confirm screen) applying Liquid Glass, SF Symbols, Dynamic Type, haptics, the full state matrix, and the WCAG 2.2 checklist end to end.
<!-- dual-compat-end -->
