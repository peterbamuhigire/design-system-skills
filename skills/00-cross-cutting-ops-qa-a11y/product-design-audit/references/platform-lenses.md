# Reference: Per-Platform Audit Lenses

The cross-platform dimensions (`audit-dimensions.md`) say *what* every surface is scored on. The
**lenses** below say *how each platform's idioms* are checked on top of that — the things that are
right or wrong only because of the platform. A faithful Material 3 layout and a faithful HIG layout
are both "correct"; flattening one rubric across both is the mistake this file prevents.

Each lens ends with the **engine skill that remediates** a finding in it. Skill names are
glob-verified against the engine.

Current as of 2026: **iOS/iPadOS/macOS Liquid Glass + SF Symbols 8**; **Android Material 3
Expressive + dynamic colour + predictive back**.

---

## Lens A — Marketing Website

**Idiom owner skill:** `webapp-gui-design`, `landing-page-and-conversion-design`,
`responsive-and-adaptive-layout`, `performance-as-ux-and-core-web-vitals`.

| Check | Standard / tell | Routes to |
|---|---|---|
| **Core Web Vitals (field p75)** | LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1; verify from CrUX/RUM, lab is a proxy | `performance-as-ux-and-core-web-vitals` |
| **Asset budget** | Within the marketing archetype budget (total ≤ ~1 MB gz; hero image weight; font count) | `performance-as-ux-and-core-web-vitals` |
| **Responsive / container queries** | Mobile-first, content-driven breakpoints; no horizontal scroll at 320px; container queries for reusable blocks; fluid type | `responsive-and-adaptive-layout`, `layout-grid-and-spacing` |
| **SEO-visual** | Real H1/heading hierarchy (visual ≠ DOM mismatch); meaningful titles; descriptive link text; LCP element is content not a spinner; no layout-shifting ads | `navigation-and-information-architecture`, `landing-page-and-conversion-design` |
| **Hero distinctiveness** | Not a purple gradient + centred card + Inter; the hero states an intentional voice | `distinctive-by-design`, `font-selection-and-pairing` |
| **Trust on the page** | Real proof (logos/testimonials with attribution), honest pricing CTA, support/contact visible | `landing-page-and-conversion-design`, `premium-ui-ux-design` |
| **Conversion path** | Primary CTA obvious; form friction low; no dead ends | `landing-page-and-conversion-design`, `form-ux-design` |

---

## Lens B — SaaS Web App

**Idiom owner skill:** `webapp-gui-design`, `dashboard-and-data-product-design`,
`navigation-and-information-architecture`, `form-ux-design`.

| Check | Standard / tell | Routes to |
|---|---|---|
| **App shell** | Persistent, predictable nav (sidebar/topbar); current location always clear; no full-page reloads where SPA is expected; responsive shell that collapses sanely | `navigation-and-information-architecture`, `webapp-gui-design` |
| **Data density** | Information-dense without clutter; comfortable/compact density modes; alignment of numerics (right-align, tabular figures); whitespace earns its place | `dashboard-and-data-product-design`, `layout-grid-and-spacing` |
| **Tables** | Sortable/filterable where needed; sticky header; readable row height; truncation with full-value access; bulk actions discoverable; empty/loading/error per table | `dashboard-and-data-product-design`, `data-visualization` |
| **States everywhere** | Every async surface has empty + loading (skeleton, not "Loading…") + error + success; partial/optimistic states honest | `empty-error-and-loading-states`, `interaction-design-patterns` |
| **Onboarding** | First-run is not a blank app; progressive disclosure; sample data or guided setup; time-to-first-value short | `ux-writing-and-microcopy`, `enterprise-ux-process` |
| **Forms** | Inline validation (what+why+how); no redundant entry (WCAG 3.3.7); accessible auth (3.3.8); keyboard-complete; logical tab order | `form-ux-design`, `accessibility-wcag-2-2-compliance` |
| **Keyboard power-use** | Shortcuts for frequent actions; focus management after modals/route changes | `interaction-design-patterns`, `accessibility-wcag-2-2-compliance` |

---

## Lens C — iOS / iPadOS / macOS (Apple platforms)

**Idiom owner skill:** `ios-ui-ux-design` (with `cross-platform-design-parity` for parity).
Standards: Apple HIG, **Liquid Glass**, **SF Symbols 8**, Dynamic Type.

### Shared Apple checks (all device classes)

| Check | Standard / tell | Routes to |
|---|---|---|
| **HIG conformance** | Native navigation (nav stack / tab bar / split view) used idiomatically; not a web layout in a wrapper | `ios-ui-ux-design` |
| **Liquid Glass** | System materials used per HIG (not faked, not over-applied); legibility preserved over glass; respects **Reduce Transparency** + **Increase Contrast** | `ios-ui-ux-design`, `accessible-color-and-contrast` |
| **SF Symbols 8** | System symbols (correct weight/scale, hierarchical/multicolor where apt); not random icon sets mixed with SF | `iconography-system-design`, `ios-ui-ux-design` |
| **Dynamic Type** | Layout survives the largest AX text sizes; no clipping/truncation; supports text scaling end-to-end | `ios-ui-ux-design`, `accessibility-wcag-2-2-compliance` |
| **VoiceOver** | All controls labelled, grouped, ordered; custom controls expose traits | `accessibility-wcag-2-2-compliance` |
| **Haptics & motion** | Haptics meaningful not gratuitous; respects **Reduce Motion**; system-consistent transitions | `motion-design`, `ios-ui-ux-design` |
| **Touch targets** | ≥ 44×44 pt | `ios-ui-ux-design` |
| **Dark mode + appearance** | Independently designed dark mode; respects appearance personalization | `dark-mode-and-theming` |

### iPhone-specific

| Check | Tell | Routes to |
|---|---|---|
| **Safe areas** | Content respects notch/home indicator; no clipped corners; bottom controls above the indicator | `ios-ui-ux-design` |
| **Dynamic Island** | Live Activities / Island used correctly if present; not abused | `ios-ui-ux-design` |
| **Reachability / one-hand** | Primary actions in thumb reach | `ios-ui-ux-design` |

### iPad-specific

| Check | Tell | Routes to |
|---|---|---|
| **Multitasking** | Split View / Slide Over / Stage Manager handled; layout adapts to arbitrary window sizes (not just full screen) | `ios-ui-ux-design`, `responsive-and-adaptive-layout` |
| **Pointer** | Pointer hover states, precise targets, keyboard + trackpad support | `interaction-design-patterns`, `ios-ui-ux-design` |
| **Sidebar/columns** | Three-column / split layouts used where the content warrants | `navigation-and-information-architecture` |

### Mac-specific (Catalyst / native / designed-for-iPhone)

| Check | Tell | Routes to |
|---|---|---|
| **Menu bar** | Real menu commands (File/Edit/View…), not iOS-only gestures; commands have shortcuts | `ios-ui-ux-design`, `interaction-design-patterns` |
| **Window management** | Resizable windows, sensible min size, multi-window, restoration | `ios-ui-ux-design` |
| **Density & pointer** | Mac-appropriate density (tighter than iPhone); hover; right-click menus | `ios-ui-ux-design` |
| **Designed-for-iPhone** | If shipped as iPhone-on-Mac, window behaves acceptably; not a stretched phone screen passed off as a Mac app | `cross-platform-design-parity`, `ios-ui-ux-design` |

---

## Lens D — Android

**Idiom owner skill:** `android-ui-ux-design`. Standards: **Material 3 Expressive**, dynamic
colour, predictive back, foldables, edge-to-edge.

| Check | Standard / tell | Routes to |
|---|---|---|
| **Material 3 Expressive** | M3 components, shapes, typography, elevation, motion used idiomatically; not an iOS layout ported verbatim (tab bar on top, iOS back chevrons) | `android-ui-ux-design` |
| **Dynamic colour** | Material You dynamic colour (wallpaper-derived) supported; brand colour still distinguishable; tonal palette correct | `android-ui-ux-design`, `color-system-and-palette` |
| **Predictive back** | Predictive back gesture supported (Android 14+); back behaviour previews/cancels correctly | `android-ui-ux-design`, `interaction-design-patterns` |
| **Edge-to-edge** | Draws edge-to-edge; insets handled (status/nav bars, gesture areas); no content under the system bars | `android-ui-ux-design`, `responsive-and-adaptive-layout` |
| **Foldables / large screens** | Adapts to fold/unfold and tablet widths; uses canonical layouts (list-detail, supporting pane); no letterboxed phone UI | `responsive-and-adaptive-layout`, `android-ui-ux-design` |
| **TalkBack** | Content labelled, traversal order correct, custom views accessible | `accessibility-wcag-2-2-compliance` |
| **Touch targets** | ≥ 48×48 dp | `android-ui-ux-design` |
| **Navigation** | Bottom nav / nav rail / nav drawer per breakpoint; system back consistent with in-app back | `navigation-and-information-architecture`, `android-ui-ux-design` |

---

## Lens E — Desktop App (native or Electron)

**Idiom owner skill:** `webapp-gui-design` (Electron/web-tech UIs),
`interaction-design-patterns`, `navigation-and-information-architecture`.

| Check | Standard / tell | Routes to |
|---|---|---|
| **Native vs Electron** | If Electron, does it still respect the OS (native menus, traffic-light/window controls, fonts, accent colour) — or does it feel like a website in a frame? Note the trade-off explicitly | `webapp-gui-design`, `cross-platform-design-parity` |
| **Window chrome** | Correct title bar / traffic lights / window controls per OS; resizable with sane min size; remembers size/position; multi-window if the task needs it | `webapp-gui-design` |
| **Density** | Desktop-appropriate density (tighter than mobile; pointer not thumb); not a stretched mobile layout | `layout-grid-and-spacing`, `responsive-and-adaptive-layout` |
| **Keyboard & shortcuts** | Full keyboard operability; standard shortcuts (Cmd/Ctrl+S, etc.) honoured per OS; visible focus; tab order | `interaction-design-patterns`, `accessibility-wcag-2-2-compliance` |
| **Menus & context menus** | Real menu bar with logical command grouping; right-click context menus; commands discoverable, not gesture-only | `navigation-and-information-architecture`, `interaction-design-patterns` |
| **OS integration** | Notifications, dock/taskbar badges, dark-mode following the OS, accent-colour following the OS | `dark-mode-and-theming`, `webapp-gui-design` |
| **Performance** | Cold-start time; idle CPU/memory (Electron tax); scroll/resize smoothness | `performance-as-ux-and-core-web-vitals` |

---

## Cross-platform parity (when one product spans surfaces)

After the per-platform lenses, run the parity lens — owner skill `cross-platform-design-parity`:

- **Shared** across surfaces: IA, terminology, brand identity, colour intent, the state model
  (what an error/empty/loading looks like conceptually), and core flows.
- **Divergent** by design: navigation chrome, gestures, controls, density, motion — each surface
  uses its **own** platform idiom. Forcing an iOS tab bar onto Android, or a desktop menu onto a
  phone, is a parity *failure*, not parity.
- A parity gap (e.g. "billing" on web vs "payments" on iOS for the same feature) is a finding
  routed to `cross-platform-design-parity`.
