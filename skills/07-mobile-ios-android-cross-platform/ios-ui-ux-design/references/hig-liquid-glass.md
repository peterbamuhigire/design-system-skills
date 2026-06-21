# Reference: Apple HIG - Liquid Glass, SF Symbols And Dynamic Type

The current Apple platform-design baseline for native Apple-platform work. Use this alongside
`doctrine/design-doctrine.md` (the anti-slop charter) and `doctrine/references/wcag-2.2-criteria.md`
(the accessibility floor). Source: Apple Human Interface Guidelines (developer.apple.com/design/),
"Adopting Liquid Glass," the WWDC26 Design guide, SF Symbols 8, and 2026 HIG updates.

Platform-face note: **SF Pro / SF Compact (San Francisco)** is the Apple **system face** — a
platform-native default, allowed and correct for native iOS UI, carrying **no slop penalty**. It is
*not* a Chwezi-chosen primary. A deliberate **branded display face** (titles, hero, splash, marketing
chrome) must still come from the approved groups in `doctrine/references/font-groups-and-usage.md`
and avoid the banned list. Body/labels/system controls stay on SF; brand expression rides on top.

---

## 1. Liquid Glass - the current Apple platform material

Liquid Glass is the dynamic material that unifies the look across Apple platforms.
It is a **real-time rendered material** that refracts and reflects the content behind it, with
specular highlights and a subtle lensing edge. It behaves like a physical pane of glass floating
above content, not a flat translucent fill.

**Where it belongs (the floating navigation layer):**
- Tab bars, toolbars, navigation bars, sidebars, sheets, alerts, menus, and controls — the
  **functional/navigation layer** that sits *above* content.
- Buttons and controls that need to read as elevated, tappable chrome.

**Where it does NOT belong:**
- **Not** on the content layer itself. Do not wrap article bodies, lists of data, or large content
  regions in Liquid Glass — it is for chrome, not canvas. Over-using it flattens the hierarchy and
  destroys the depth cue it exists to provide.
- **Not** stacked glass-on-glass. Two Liquid Glass surfaces overlapping muddies legibility.

**Two variants (pick by context):**
- **Regular** — the default; more opaque, adapts legibly over any content. Use for most chrome.
- **Clear** — more transparent, for media-rich contexts (e.g. over photos/video) where you want the
  content to dominate; requires a dimming/scrim layer behind text to protect contrast.

**Implementation anchors (SwiftUI/UIKit, current Apple SDKs):**
- `glassEffect(_:in:)` applies the material to a custom view; pair with a shape
  (e.g. `.glassEffect(.regular, in: .capsule)`).
- `GlassEffectContainer` groups multiple glass elements so they blend and morph as one — use it when
  several glass controls sit close together (e.g. a floating control cluster).
- `.buttonStyle(.glass)` / `.glassProminent` for glass buttons.
- Toolbars/tab bars adopt Liquid Glass automatically when you build on standard SwiftUI containers
  (`TabView`, `.toolbar`, `NavigationStack`) or system UIKit bars and link against the current SDK - **prefer standard
  containers** so the material, scroll-edge behaviour, and accessibility come for free.

**Scroll-edge effect:** content scrolling under glass chrome gets a soft gradient/blur at the edge so
text never collides with the bar. Use the system bars rather than hand-rolling, so this is automatic.

---

## 2. Accessibility settings that reshape Liquid Glass (must honour)

Liquid Glass is contrast- and motion-sensitive. The system adapts it, but **you must verify** under:
- **Reduce Transparency** — glass falls back to a more opaque/solid fill. Confirm text and controls
  still meet contrast and nothing relied on seeing through the glass.
- **Increase Contrast** — borders and separators strengthen; verify the glass edge reads as a control.
- **Reduce Motion** — the material's specular shimmer and morph animations are dampened; never tie a
  *required* affordance to a glass animation. (See `references/ios-sensory-and-haptics.md`.)
- **Reduce Transparency + Dark Mode** combinations - test both; legibility over busy content is the
  failure mode.
- **Appearance personalization** - verify app icons, controls, and chrome still read under current
  Apple appearance, tint, transparency, and icon variant settings.

**Contrast still governs.** Text and glyphs on or behind glass must clear the WCAG floor: body
**≥ 4.5:1**, large text and UI/graphical objects **≥ 3:1** (`wcag-2.2-criteria.md`). Glass is never an
excuse to drop below it — add a scrim behind text over Clear glass or busy imagery. Design with **APCA**
for real legibility, certify with the WCAG ratio.

---

## 3. SF Symbols 8 (the system icon library)

SF Symbols is Apple's iconography system, weight- and size-matched to SF text. Using it is the native,
non-slop default for iconography in iOS chrome.

- **7,000+ symbols**, available across weights (Ultralight -> Black) and three scales
  (small/medium/large) that align to the surrounding Dynamic Type.
- **Rendering modes:** Monochrome, Hierarchical (one tint, layered opacities), Palette (multiple
  explicit colours), and Multicolor (built-in meaningful colour). Pick Hierarchical for most chrome;
  Multicolor only where the colour is semantic (e.g. status).
- **Animation (SF Symbols 5+):** symbol effects — `.bounce`, `.pulse`, `.wiggle`, `.rotate`,
  `.breathe`, `.variableColor`, plus `.replace` transitions between symbols. Use sparingly, as feedback
  — not decoration — and respect Reduce Motion.
- **Weight matching:** set the symbol's weight/scale to match the adjacent text style so glyph and label
  share an optical rhythm.
- **Custom symbols** must be drawn on the SF Symbols template so they inherit weights, scales, and
  rendering modes; ad-hoc PNGs break the system and read as slop.
- **SF Symbols 8 watch item:** use the current app to validate new symbols, annotations, animations,
  and rendering modes before exporting custom symbols.

---

## 4. Dynamic Type (text that scales)

Dynamic Type lets users pick their text size; supporting it is a hard iOS accessibility requirement.

- **Use the semantic text styles**, never hardcoded point sizes: `largeTitle`, `title`, `title2`,
  `title3`, `headline`, `subheadline`, `body`, `callout`, `footnote`, `caption`, `caption2`. In SwiftUI:
  `.font(.headline)` etc. These scale automatically with the user's setting.
- **Standard range:** xSmall → xxxLarge. **Accessibility range:** AX1 → AX5 — five larger steps that can
  push `body` well past 50pt. **Your layout must survive AX5** without clipping or truncating meaning.
- **Layout consequences:**
  - Prefer **vertical stacking** at large sizes — use `ViewThatFits` or check
    `@Environment(\.dynamicTypeSize)` to switch horizontal rows to vertical at accessibility sizes.
  - **Never cap a branded display face below the user's chosen size** for body content. A branded face
    is fine for a hero title, but it too must scale with Dynamic Type — pair a custom font with a
    relative text style (`.font(.custom("…", size: …, relativeTo: .largeTitle))`) so it tracks the
    user's setting instead of freezing.
  - Don't truncate critical labels; allow wrapping. Test the largest AX size as a release gate.
- **Minimum tap target stays 44×44 pt** regardless of text size (HIG; WCAG 2.5.8 floor is 24×24 CSS px —
  iOS aims higher).

---

## 5. Liquid-Glass quality gate (check before sign-off)

1. Glass is on the **chrome/navigation layer only** — never wrapping content.
2. No **glass-on-glass** stacking; close clusters share a `GlassEffectContainer`.
3. **Reduce Transparency, Increase Contrast, Reduce Motion** all verified; required affordances never
   depend on the glass shimmer/morph.
4. Text over **Clear** glass or imagery has a scrim and clears **4.5:1 / 3:1**.
5. Built on **standard system containers** (`TabView`, `.toolbar`, `NavigationStack`) so material,
   scroll-edge, and a11y are automatic — no hand-rolled bars unless unavoidable.
6. Icons are **SF Symbols 8** (or template-drawn custom symbols), weight-matched to adjacent text.
7. All text uses **semantic Dynamic Type styles** and survives **AX5**; branded display type scales
   relatively, body stays on SF.
8. Branded display face (if any) is from an **approved font category** — not the banned list; SF carries
   the system UI.
9. App icon variants and appearance personalization are reviewed for Liquid Glass attributes,
   legibility, and brand recognition.
