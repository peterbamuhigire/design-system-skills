---
name: app-store-presence-and-aso
description: Use when designing an app's store listing AS a design surface — the App
  Store (iOS) and Google Play (Android) product page treated as a composed artifact,
  not a metadata form. Covers the app icon for both stores (masking, safe zones,
  rounding, no transparency/alpha rules, iOS Liquid Glass icon variants), the
  captioned device-framed screenshot set (narrative order, the first 2-3 that sell),
  the preview video/app preview, the listing copy hierarchy (name, subtitle/short
  description, promotional text, keywords, long description), localized assets, and
  current (2026) App Store Connect / Play Console asset specs and review constraints.
  Routes here for "design app store screenshots", "app icon for App Store and Play",
  "store listing", "ASO assets", "screenshot captions", "app preview video", "feature
  graphic", "localize store listing", "what size are App Store screenshots". Treats
  the listing as a designed conversion surface governed by the anti-slop doctrine.
status: active
metadata:
  portable: true
  category: 07-mobile-ios-android-cross-platform
  compatible_with:
    - claude-code
    - codex
---

# App Store Presence & ASO

<!-- dual-compat-start -->
## Use When
- Designing or auditing an **App Store (iOS/iPadOS) and/or Google Play** product page as a composed visual surface — icon, screenshots, preview video, and copy as one authored system.
- Producing the **app icon** for store delivery: the full-bleed master plus the platform masking/rounding behavior, safe zones, alpha/transparency rules, and the iOS **Liquid Glass** layered/variant icons (light/dark/tinted/clear).
- Building a **captioned, device-framed screenshot set** with a deliberate narrative order — the first 2-3 frames carrying the value proposition, captions in the app's approved type.
- Scripting and storyboarding an **App Preview (iOS)** / **promo or feature video (Play)** to current duration, resolution, and capture constraints.
- Writing the **listing copy hierarchy** to each store's field model (name/title, subtitle vs short description, promotional text, keyword field, long description) and the character limits that shape it.
- **Localizing** the asset set (text in captions, screenshot UI language, copy) across storefronts/locales without re-laying-out each one by hand.
- Pre-flighting assets against **2026 App Store Connect / Play Console** requirements and the common review/policy rejections.

## Do Not Use When
- You are designing the **in-app UI** itself — use `ios-ui-ux-design` / `android-ui-ux-design`. This skill consumes finished screens and stages them; it does not design them.
- You are constructing the **app-icon glyph/mark as an identity artifact** (grid, optical balance, metaphor) — use `iconography-system-design` for the mark, then return here for the **store delivery** of that mark (masks, safe zones, Liquid Glass variants, per-store export).
- You are choosing the **brand palette or typeface** — use `color-system-and-palette` / `font-selection-and-pairing`; this skill applies the already-approved brand type to captions and the approved palette to backgrounds.
- The task is **paid user acquisition / ad creative ops** (not the organic store listing) — that is a marketing-ops concern, out of this engine's scope.
- You only need **release notes / changelog copy** — that is content, not the listing design surface.

## Required Inputs
- **Target stores and primary device classes** (iPhone 6.9"/6.5", iPad 13", Android phone, 7"/10" tablet) — these fix the required screenshot dimensions and how many sets you must ship. See `references/aso-asset-specs.md`.
- The **approved brand type and palette** (from the type/color skills) — screenshot captions and frame backgrounds use the **app's approved typeface**, never a banned default (`doctrine/references/ai-slop-banned-fonts.md`). State the choice before composing.
- The **app-icon master** (full-bleed, no rounding baked in) at the largest required size (1024×1024 for App Store, 512×512 for Play), plus — for iOS — the layered source needed for Liquid Glass light/dark/tinted variants.
- **Finished, real in-app screens** (not mockup lorem) to stage, and the **single value proposition** that orders the screenshot narrative.
- The **locales** to ship and which fields/captions need translation.

## Workflow
1. **State the type and color intent before composing** (`doctrine/design-doctrine.md` §2 non-negotiable #1). Name the caption typeface (the app's *approved* face — not Inter/Roboto/SF-as-brand; per the mobile-platform font caveat the OS system face is fine *inside* a screenshot of native UI, but the **caption/marketing type** is a deliberate approved choice), the background palette, and the one signature compositional move (a consistent device angle, a continuous color field bleeding across frames, a fixed caption position). The default store page — three un-captioned raw screenshots on white — is the convergent AI/template mean; the authored set is what reads as a real product.
2. **Treat the listing as one surface, not four uploads.** Decide the through-line first: icon, the first screenshot, and the subtitle must tell **one** coherent story. Order the screenshot set as a **narrative** (§ below), not a feature dump.
3. **Design the app icon for store delivery.** Start from the identity mark (`iconography-system-design`), then apply **store** rules: full-bleed square master, **no transparency/alpha** (both stores reject it), **don't pre-round** (each store applies its own mask/superellipse), keep critical content inside the safe zone, and for iOS produce the **Liquid Glass** layered icon with **light / dark / tinted (mono) / clear** variants that read at every grid size. See `references/aso-asset-specs.md` §Icon.
4. **Compose the screenshot set, captioned and device-framed.** Lock dimensions per device class, frame in the correct current device (or a clean borderless bezel), add a **caption per frame** in the approved type with a fixed position and a strict hierarchy (one headline idea per frame, optional sub-line). The **first 2-3 frames** must stand alone and sell — most users never swipe past them. Keep captions legible at the **thumbnail** size the search results render. State the WCAG 2.2 contrast floor for caption-on-background (`doctrine/references/wcag-2.2-criteria.md`).
5. **Script the preview video / app preview.** Storyboard to the current duration window (App Preview 15-30s; Play promo video via YouTube link), open on the value proposition in the first ~3 seconds, capture from a **real device/recording** (App Store requires actual app footage — no pure motion-graphics ad), provide a deliberate **poster frame**, and assume **muted autoplay** (carry meaning without sound; caption on-screen).
6. **Write the copy hierarchy to each store's field model.** Map the value proposition to: iOS **app name (≤30) + subtitle (≤30) + promotional text (≤170) + keyword field (100 chars, comma-separated, no spaces) + description**; Play **title (≤30) + short description (≤80) + full description (≤4000)**. Front-load the first line of the description (the only part shown before "more"). Keywords/short-description carry ASO weight — state the target terms, never keyword-stuff the description (Play penalizes it). See `references/aso-asset-specs.md` §Copy.
7. **Localize as a system.** Translate captions/copy and, where it matters, screenshot UI language; keep the layout template fixed so each locale is a fill-in, not a redesign. Verify text doesn't overflow caption zones in longer languages (German/Russian) and that RTL locales mirror correctly.
8. **Pre-flight against current store requirements** (`references/aso-asset-specs.md` §Pre-flight): correct dimensions/aspect per device, no alpha in the icon, no device frames that misrepresent another platform, no placeholder/lorem, no pricing or "free" in the icon, accurate screenshots (review rejects screenshots that don't reflect the app), age-rating and privacy-label consistency.

## Screenshot Narrative Order (the conversion spine)
- **Frame 1 — the hook:** the single biggest value, one short caption, the strongest screen. Must work as a standalone thumbnail.
- **Frame 2 — the proof:** the core action/benefit in use.
- **Frame 3 — the differentiator:** the thing competitors don't have.
- **Frames 4-N — depth:** secondary features, social proof, breadth — for the minority who keep swiping.
- A **continuous design field** (color/shape bleeding frame-to-frame) signals one authored set; isolated raw screenshots signal a template.

## Anti-Patterns
- **The four-uploads mindset** — icon, screenshots, video, and copy designed separately so they tell four disconnected stories instead of one.
- **Raw un-captioned screenshots on white** — the template/AI-mean store page; no narrative, no value proposition, no authored field.
- **Feature-dump ordering** — screenshots in app-navigation order instead of value order; burying the hook at frame 5.
- **Banned/default caption type** — Inter/Roboto/the secondary escape fonts as the *marketing* caption face. The OS face is fine inside a screenshot of native UI; the caption layer is a stated, approved choice.
- **Pre-rounded or alpha icons** — baking the corner radius in (double-rounds under the store mask) or shipping transparency (auto-rejected). Ignoring the iOS Liquid Glass tinted/dark variants so the icon looks broken in those modes.
- **Mockup/lorem screenshots** — fake data or screens that don't match the shipped app; a review-rejection and a trust break.
- **Ad-style preview video** — pure motion graphics with no real app footage (App Store rejects), or meaning that only lands with sound (autoplay is muted).
- **Keyword-stuffed description** (Play policy hit) and **first description line wasted** on boilerplate instead of the value proposition.
- **One-locale-fits-all** or machine-translated captions that overflow the caption zone / break RTL.

## Outputs
- A **stated type/color intent** for the listing surface (caption face = approved app type, background palette, signature compositional move), named before production.
- An **app-icon store-delivery spec**: full-bleed master sizes per store, safe zone, no-alpha/no-pre-round rules, and the iOS Liquid Glass light/dark/tinted/clear variants.
- A **captioned, device-framed screenshot set** per required device class, in narrative order, with caption hierarchy, positions, and contrast verified.
- An **app-preview / promo-video storyboard** to current duration/capture/poster-frame rules, working muted.
- A **copy hierarchy** mapped to each store's exact fields and character limits, with ASO keyword targets.
- A **localization plan** (which fields/captions, layout-fixed template, overflow/RTL checks).
- A **pre-flight checklist** result against 2026 App Store Connect / Play Console requirements.

## Examples
- `examples/store-listing-asset-spec.md` — a complete worked store-listing asset spec for a sample app ("Maduuka", a merchant app): stated type/color intent against the doctrine, the dual-store app-icon delivery (masks, safe zone, no-alpha, iOS Liquid Glass variants), a 5-frame captioned device-framed screenshot set in narrative order with caption hierarchy and contrast, the App Preview storyboard, the full copy hierarchy mapped to both stores' fields with character counts and keyword targets, and a two-locale localization pass. Real numbers, real captions — never lorem. (See `CONTRIBUTING.md` — examples are mandatory and never lorem.)

## References
- `doctrine/design-doctrine.md` — the always-load anti-slop charter (§0/§2 "looks human-made"): name the caption type and palette first, make one authored compositional move, refuse the white-background-three-screenshots template mean.
- `references/aso-asset-specs.md` — the canonical 2026 asset specs: App Store & Play **icon** dimensions/masking/safe-zone/alpha rules and iOS Liquid Glass variants; **screenshot** dimensions per device class and aspect/count limits; **app preview / promo video** specs; the **copy field** model and character limits; and the **pre-flight / common-rejection** checklist.
- `doctrine/references/ai-slop-banned-fonts.md` — caption/marketing type must avoid the banned list; the OS system face is allowed only *inside* a native-UI screenshot, never as the deliberate caption/brand face.
- `doctrine/references/wcag-2.2-criteria.md` — the contrast floor (1.4.3) for caption-on-background legibility, including at thumbnail render size.
- `doctrine/references/type-scale-and-spacing.md` — caption type scale and spacing rhythm across the frame set.
- Siblings: `iconography-system-design` (the icon *mark* this skill delivers to stores), `ios-ui-ux-design` / `android-ui-ux-design` (the in-app screens this skill stages — incl. the Liquid Glass icon note), `internationalization-and-rtl-design` (localizing/mirroring the asset set).
<!-- dual-compat-end -->
