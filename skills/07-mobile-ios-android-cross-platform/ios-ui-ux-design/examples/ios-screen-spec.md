# Worked Example: iOS Screen Spec — "Send Payment" (iOS 26, Liquid Glass)

A worked, applied iOS screen spec for the convention required by Phase 0.3 (every skill ships ≥1 worked
example). It exercises the injected 2026 standards — **Liquid Glass, SF Symbols, Dynamic Type, haptics** —
against the doctrine. It is illustrative, not a real product brief.

**Brief:** Maduuka (a Chwezi merchant app). Screen: confirm and send a mobile-money payment to a saved
payee. Device classes: iPhone (primary), iPad (split-view secondary). Must feel native, trustworthy,
App-Store-quality.

---

## 1. Typography intent (state before styling — anti-slop charter §2)

- **System UI / body / labels / amounts:** **SF Pro** (the Apple system face). Correct, native, no slop
  penalty. All of it via **Dynamic Type semantic styles** — `largeTitle` (amount), `headline` (payee),
  `body` (rows), `footnote` (helper/fees), `caption` (timestamps). No hardcoded point sizes.
- **Branded display (the "Maduuka" wordmark in the nav title + the confirmation hero):** a deliberate
  display face from an **approved group** — Editorial-Authoritative per
  `doctrine/references/font-groups-and-usage.md` — bound with `.font(.custom("…", relativeTo: .largeTitle))`
  so it **scales with Dynamic Type**, not frozen. Not on the banned list; SF carries everything functional.
- *Why:* trust-sensitive fintech surface — body must be maximally legible (SF), brand expressed only in
  the title/hero so it reads authored, not templated.

## 2. Layout & material

```
┌──────────────────────────────────────────┐  ← Liquid Glass NAV BAR (regular)
│  ‹ Back            Maduuka          ⓘ      │     branded wordmark; SF Symbol chevron + info
├──────────────────────────────────────────┤
│                                            │  CONTENT LAYER — plain, NOT glass
│        UGX 250,000                         │  .largeTitle, bold, monospaced digits
│        to  Aisha Nakato                    │  .headline + SF Symbol person.crop.circle
│                                            │
│   ┌──── card (system background) ────┐     │
│   │ From      Maduuka Wallet     ›    │     │  .body rows; chevron = SF Symbol
│   │ Fee       UGX 1,500               │     │  .footnote, secondary colour
│   │ Arrives   Instantly               │     │
│   └───────────────────────────────────┘     │
│                                            │
├──────────────────────────────────────────┤  ← Liquid Glass TOOLBAR (regular)
│        [  Slide / Tap to Send  ]            │     .glassProminent button, capsule
└──────────────────────────────────────────┘
```

- **Liquid Glass** is on the **nav bar and bottom toolbar only** (the chrome) — `regular` variant for
  legibility over scrolling content. The amount card and rows are on a **plain system background**, never
  wrapped in glass (charter: glass = chrome, not canvas). Built on `NavigationStack` + `.toolbar` so the
  material, **scroll-edge effect**, and a11y come automatically. The send button uses `.glassProminent`
  in a `.capsule`.
- **iPad:** `NavigationSplitView` — payee list in the sidebar, this confirm screen in the detail column.

## 3. SF Symbols

| Element | Symbol | Rendering | Notes |
|---|---|---|---|
| Back | `chevron.left` | Monochrome | weight-matched to nav title |
| Info | `info.circle` | Hierarchical | opens fee explainer sheet |
| Payee | `person.crop.circle.fill` | Hierarchical | tint = accent |
| Source row | `chevron.right` | Monochrome | disclosure |
| Success (post-send) | `checkmark.circle.fill` | Multicolor (green is semantic) | `.bounce` symbol effect, **respecting Reduce Motion** |

Custom glyphs (Maduuka mark) drawn on the SF Symbols template so they inherit weight/scale.

## 4. Dynamic Type behaviour

- All text uses semantic styles; **must survive AX5**. At accessibility sizes the three info rows
  (From / Fee / Arrives) switch from label-left / value-right to **stacked** via `ViewThatFits`.
- Amount never truncates — it wraps to two lines before it clips. Branded hero scales relatively.
- Tap targets stay **≥ 44×44 pt** at every text size (HIG; WCAG 2.5.8 floor 24×24, we exceed).

## 5. Haptics & sensory feedback

| Event | Feedback | Rule applied |
|---|---|---|
| Toggle source account | `.impact(weight: .medium)` | control engages |
| Confirm-slider crosses threshold | `.selection` | discrete value change, accompanies visible motion |
| **Payment succeeds** | `.success` | outcome haptic tells the truth; pairs with `checkmark` `.bounce` + short sound on same frame |
| **Payment fails** | `.error` | never `.success` on failure |
| Insufficient-funds warning | `.warning` | recoverable caution |

`.sensoryFeedback(.success, trigger: didSend)`. One feedback per event, coalesced. UI fully usable with
haptics **disabled** and under **Reduce Motion** (success still shown via the checkmark + copy).

## 6. State matrix (every state modelled)

| State | Treatment |
|---|---|
| Loading (fetching fee/balance) | skeleton on the card; button disabled (no glass prominence) |
| Content | as drawn above |
| Empty (no saved payee) | redirect to add-payee; not reachable here |
| Error (network) | inline banner + `.error` haptic; button returns to idle, amount preserved (WCAG 3.3.7 redundant entry — don't re-key) |
| Offline | "Will send when back online" affordance; queue, don't lose input |
| Permission denied (biometric) | fall back to passcode confirm; never dead-end |
| Syncing (post-send) | inline progress; success state on completion |

## 7. Accessibility checklist (WCAG 2.2 floor — `wcag-2.2-criteria.md`)

- Amount / payee / rows clear **4.5:1**; glass-bar glyphs and the send button clear **3:1**. Designed with
  **APCA**, certified with the WCAG ratio.
- **Reduce Transparency** verified — glass bars fall back to opaque; nothing relied on see-through.
- **Increase Contrast** + **Dark Mode** combos verified for the bars.
- **Reduce Motion** — checkmark `.bounce` and glass shimmer dampened; success still conveyed.
- VoiceOver: button name/role/state ("Send, button"), amount and payee read in logical order (4.1.2,
  2.4.3). Manual keyboard/switch traversal + VoiceOver smoke test before sign-off.
- Focus not obscured by the glass toolbar (2.4.11).

## 8. Sign-off gate

Liquid-Glass gate (`hig-liquid-glass.md` §5) ✓ · Haptics gate (`ios-sensory-and-haptics.md` §6) ✓ ·
Premium UX gate ≥ 8/10 · branded display face from an approved group, SF carries system UI ✓.
