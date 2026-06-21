---
name: dark-mode-and-theming
description: Use when building, adding, or auditing a dark mode — or any multi-theme (light/dark/high-contrast/dimmed) system — for a website, app/web UI, dashboard, or themed document. Builds a true dual-mode semantic palette where dark is a deliberate remap (lowered chroma, lightened/desaturated accents, dark-grey surfaces carrying the brand hue, NOT #000), models elevation with surface lightness instead of drop shadows, re-gates every pair on WCAG contrast independently, and keeps contrast parity across modes. Routes here whenever the request mentions "dark mode", "theme switch", "light/dark tokens", "prefers-color-scheme", or "we just inverted it and it looks wrong".
status: active
metadata:
  portable: true
  category: 02-color-brand-and-visual-identity
  compatible_with:
    - claude-code
    - codex
---

# Dark Mode And Theming
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Adding a dark mode to an artifact that already has (or is getting) a light palette, or
  building light + dark together from the start.
- Designing a multi-theme system (light, dark, dimmed, high-contrast) that must share one set
  of semantic roles and switch cleanly via `prefers-color-scheme` or a manual toggle.
- Auditing or fixing a dark mode that was produced by inverting the light theme and now reads
  as muddy, vibrating, washed-out, or flat (no sense of depth).
- Defining the dark-side values of design tokens — the dark column of a light/dark token pair.

## Do Not Use When

- You have no base palette yet and need to choose the anchor, primary hue, and light ramp
  first — start at `02-color-brand-and-visual-identity/color-system-and-palette`, then return
  here for the dark remap. This skill *builds on* that one; it does not re-derive the palette.
- The only question is whether a specific pair passes contrast or which contrast tool to use —
  use `02-color-brand-and-visual-identity/accessible-color-and-contrast`.
- The task is the token *architecture/naming/export* (tiers, JSON, Style Dictionary), not the
  dark values themselves — use `09-design-systems-tokens-and-theming/design-tokens-and-naming`
  and feed it the role→value map this skill produces.

## Required Inputs

- The existing (or just-built) **light semantic role map** and tonal ramp, ideally in OKLCH —
  `surface`, raised/sunken surfaces, `text` (primary + muted), `border`, `accent`, and the
  status set `success / warning / error / info`.
- The **brand hue** and its chroma, so dark surfaces can carry a trace of it rather than going
  neutral grey or pure black.
- Which **themes** are required (dark only, or also dimmed / high-contrast) and how they switch
  (system `prefers-color-scheme`, manual toggle, or both).
- The smallest text size and thinnest UI stroke the dark values must survive (drives the
  contrast gate), and whether **elevation** is expressed (cards, menus, modals, popovers).

## Workflow

1. **Treat dark as a remap, never an inversion.** Do not flip lightness (`L → 1−L`) or invert
   the hex values. Inversion produces over-bright, over-saturated, vibrating colour and breaks
   semantic meaning (your "danger" red can land on a near-white that no longer reads as danger).
   Build the dark column role by role from the brand, exactly as `color-system-and-palette`
   step 8 directs — this skill is that step, expanded. State up front that you are remapping.

2. **Anchor dark surfaces in a brand-tinted dark grey, not `#000`.** Pure black surfaces with
   light text over-contrast and smear (halation) — text appears to bleed, especially at small
   sizes and for readers with astigmatism. Use a near-dark grey carrying a trace of the brand
   hue: in OKLCH, base surface around **L 0.14–0.20**, very low chroma (**C ≈ 0.01–0.03**) on
   the brand hue. This keeps the dark theme feeling *authored* in the brand, not a default void
   (Mission §0, `doctrine/design-doctrine.md`). See `references/dark-mode-semantic-roles.md`.

3. **Lower chroma across the whole dark palette.** Saturated colours that read as confident in
   light mode glow and buzz against dark surfaces (simultaneous contrast / chromatic aberration
   at the eye). Pull chroma down for surfaces, borders, and especially large filled areas. The
   accent and status colours keep *more* of their chroma than surfaces but still less than their
   light-mode values — see step 4. This is the single biggest tell of a real dark mode versus a
   naive one.

4. **Lighten and slightly desaturate accents and status colours so they hold meaning at depth.**
   A mid/dark accent that passed 4.5:1 on a light surface will fail badly on a dark one. Raise
   each accent's and status colour's lightness (and trim its chroma a little) until it clears the
   gate against the dark surface it actually sits on — typically the light-mode L moves *up* by
   ~0.15–0.30 in OKLCH. The hue is preserved so `error` still reads red, `success` still green;
   only L and C move. This is where "not just inversion" becomes concrete.

5. **Express elevation with surface lightness, not drop shadows.** In light mode, raised
   surfaces use shadow; on dark surfaces shadows are nearly invisible, so the convention flips:
   **higher elevation = lighter surface.** Build an elevation ramp where base/sunken is darkest
   and each raised layer (card → menu → dialog → popover/toast) steps **L up by ~0.02–0.04**.
   Keep chroma low and constant so the steps read as depth, not as a different colour. Optionally
   add a faint *lighter* top border (a 1px highlight) instead of a shadow to imply a raised edge.
   Material's "elevation overlay" is the same idea; implement it as explicit surface tokens.

6. **Hold contrast parity across modes — match the *experience*, not the numbers.** Body text in
   dark mode should feel as legible as in light, which usually means **not** maxing it out: pure
   white body text (`L 1.0`) on dark over-contrasts and shimmers exactly as `#000`-on-white does.
   Target a near-white primary text around **L 0.92–0.96** and a muted text that still clears
   4.5:1 (or 3:1 where it is genuinely large/secondary). Parity means each role does the same job
   with comparable comfort in both modes — not that the ratios are identical.

7. **Re-gate every dark pair on WCAG independently — passing in light proves nothing.** This is a
   hard gate, not advice. Body and small text **≥ 4.5:1**; large text (≥24px, or ≥18.66px bold)
   and meaningful UI components / icons / focus rings / borders that convey state **≥ 3:1**
   (WCAG 2.2 §1.4.3, §1.4.11 — `doctrine/references/wcag-2.2-criteria.md`). Check the accent and
   each status colour against **every** elevation surface it can appear on, not just base. Design
   with APCA for real legibility, certify with the WCAG ratio (same ref, "Contrast method note").
   Any failing pair sends you back to step 4 to retune L/C.

8. **Map the status set deliberately for dark.** `success / warning / error / info` must each stay
   distinguishable from one another *and* hold ≥3:1 (≥4.5:1 if they carry text) against dark
   surfaces. Warning (yellow/amber) is the usual casualty — it goes muddy or illegible; lighten
   it well and verify. Never rely on hue alone to carry status (colour-blind safety) — keep the
   icon/label that `accessible-color-and-contrast` mandates.

9. **Define theming as a token swap, not duplicated components.** Components reference semantic
   roles only; switching theme swaps the *values* behind the roles (e.g. `[data-theme="dark"]`
   or an `@media (prefers-color-scheme: dark)` block re-binding the CSS custom properties).
   Support a manual toggle that overrides the system preference, and persist the choice. Honour
   `prefers-color-scheme` as the default. Hand the final role→value map to
   `09-design-systems-tokens-and-theming/design-tokens-and-naming` for architecture/export.

10. **State the dual-mode system and hand off.** Output both columns of the role map (light +
    dark, in OKLCH with hex), the elevation ramp, the recorded contrast results for *both* modes,
    and the switch mechanism. See `examples/light-dark-token-pair.md`.

## Anti-Patterns

- **Inversion** — `filter: invert()`, flipping lightness, or swapping hex pairs. The textbook
  slop dark mode: over-bright, vibrating, semantically broken.
- **`#000` surfaces and pure-white (`#fff`/`L 1.0`) body text** — both over-contrast and smear
  (halation). Use brand-tinted dark grey and ~`L 0.92–0.96` text.
- **Full-chroma accents carried straight over from light mode** — they glow and buzz; lower
  chroma and raise lightness instead.
- **Shadows for elevation on dark** — invisible; use lighter surfaces (and optional top
  highlight) to signal depth.
- **Skipping the dark contrast re-gate** because the light theme passed — the most common real
  accessibility regression a dark mode ships.
- **Maxed-out white text** assumed to be "more accessible" — it is less comfortable; parity is
  about equal comfort, not maximum ratio.
- **Muddy or illegible warning/amber** in dark — verify the whole status set, not just text.
- **Duplicating components per theme** instead of swapping token values behind shared roles.

## Outputs

- A dual-mode semantic role map (light + dark columns, OKLCH + hex), a brand-tinted dark surface
  and dark ramp, an elevation-by-lightness ramp, lightened/desaturated accents and a verified
  status set, recorded WCAG results for **both** modes, and the theme-switch mechanism
  (`prefers-color-scheme` + manual toggle) — handed off to token export.

## Examples

- `examples/light-dark-token-pair.md` — a complete worked OKLCH light **and** dark token set for
  a real anchor, with the elevation ramp, the accent/status remap, and the contrast checks for
  both modes. Not lorem; a buildable spec.

## References

- `02-color-brand-and-visual-identity/color-system-and-palette` — the entry skill that selects
  the anchor, primary hue, light ramp, and semantic roles; **build on it, do not re-derive.**
  This skill is its step 8 ("dark mode is a deliberate remap, not an inversion") fully expanded.
- `02-color-brand-and-visual-identity/accessible-color-and-contrast` — the contrast tool
  (WCAG vs APCA), non-colour status cues, and colour-blind-safe ramps the status set relies on.
- `references/dark-mode-semantic-roles.md` — the role → light value / dark value mapping with
  OKLCH targets and the elevation ramp.
- `doctrine/references/wcag-2.2-criteria.md` — the contrast floor (§1.4.3, §1.4.11) re-applied to
  dark, and the "design with APCA, certify with WCAG" method note. **Hard gate.**
- `doctrine/design-doctrine.md` — Mission §0 (authored over convergent; a brand-tinted, crafted
  dark theme is the moat, the inverted default is the slop), Anti-Slop Charter §2 (state the
  remap choice before producing the artifact).
- Human authority (named for provenance, not citable in-repo): Josef Albers, *Interaction of
  Color* (simultaneous contrast — why saturation must drop on dark); Material Design elevation
  overlay model (elevation as surface lightness).
<!-- dual-compat-end -->
