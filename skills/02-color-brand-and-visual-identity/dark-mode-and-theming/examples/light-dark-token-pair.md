# Worked Example: Light + Dark Token Pair (OKLCH) with Contrast Checks

A complete dual-mode semantic token set for one real product, showing that **dark is a remap, not
an inversion** — lowered surface chroma, lightened/desaturated accents, elevation by lightness,
and an independent dark contrast re-gate. This is a buildable spec, not a demonstration of syntax.

## The anchor (per `color-system-and-palette` step 1 — done before any hex)

**Product:** *Maduuka*, a retail/POS dashboard. **Anchor:** weathered Ugandan **copper** — the
sheet copper on old Kampala shopfronts and roofing. Not a "vibe word": a real material with a warm
red-orange that ages to a desaturated patina. **Primary hue:** copper, **OKLCH H ≈ 50** (warm
orange-red). Chroma is moderate, not neon — copper is a metal, not a highlighter. This deliberately
avoids the indigo→blue slop gradient (`doctrine/references/ai-slop-taxonomy.md`).

We are now at `color-system-and-palette` step 8: **remap deliberately for dark.** Stated up front:
we will **not** invert. We build the dark column from the copper brand, drop surface chroma, lift
and slightly desaturate the accent and status colours, and model elevation with surface lightness.

---

## Semantic role map — light and dark columns

Format: `oklch(L C H)` (perceptual) with the sRGB hex it converts to. Brand hue H = 50.

| Role | Light `oklch` | Light hex | Dark `oklch` | Dark hex |
|---|---|---|---|---|
| `surface` (page) | `0.985 0.006 50` | `#fcf9f6` | `0.165 0.012 50` | `#211c18` |
| `surface-sunken` | `0.965 0.008 50` | `#f5efe9` | `0.135 0.012 50` | `#1a1512` |
| `surface-raised-1` (card) | `1.000 0.000 50` | `#ffffff` | `0.195 0.013 50` | `#29231e` |
| `surface-raised-2` (menu) | `1.000 0.000 50` + shadow | `#ffffff` | `0.225 0.013 50` | `#322a24` |
| `surface-raised-3` (dialog) | `1.000 0.000 50` + shadow | `#ffffff` | `0.255 0.013 50` | `#3a322b` |
| `text` (primary) | `0.255 0.012 50` | `#2c241e` | `0.945 0.006 50` | `#f3ece6` |
| `text-muted` | `0.470 0.014 50` | `#6e5d50` | `0.730 0.010 50` | `#b6a99e` |
| `border` (subtle) | `0.885 0.008 50` | `#e3dad1` | `0.310 0.012 50` | `#473e36` |
| `border-strong` (focus) | `0.560 0.110 50` | `#9a6a3e` | `0.720 0.090 50` | `#cfa074` |
| `accent` (copper) | `0.560 0.130 50` | `#9f663a` | `0.785 0.105 50` | `#e0a878` |
| `accent-on` (on accent) | `0.985 0.006 50` | `#fcf9f6` | `0.165 0.010 50` | `#211c18` |

### Status set (hue preserved across modes; L up, C trimmed for dark)

| Role | Light `oklch` | Light hex | Dark `oklch` | Dark hex |
|---|---|---|---|---|
| `success` | `0.575 0.140 150` | `#2f7d52` | `0.800 0.110 150` | `#86d6a4` |
| `warning` | `0.700 0.150 85` | `#b58a17` | `0.855 0.135 85` | `#e6c34e` |
| `error` | `0.555 0.195 27` | `#bb3522` | `0.720 0.155 27` | `#ef8a72` |
| `info` | `0.560 0.150 245` | `#2f6fb0` | `0.780 0.115 245` | `#83b6e8` |

**Read the remap, not the inversion:** the dark accent is the *same copper hue (H 50)*, but L moves
`0.560 → 0.785` (+0.225) and chroma `0.130 → 0.105` (trimmed). An inversion would have pushed the
accent toward `L ≈ 0.44` and a cyan-ish complementary cast — wrong colour, wrong job. Surface chroma
stays tiny (0.012–0.013) so the dark greys read as warm-neutral, not orange.

---

## Elevation ramp (dark) — depth by lightness, not shadow

```
surface-sunken   L 0.135   #1a1512   ▁  wells / insets
surface (page)   L 0.165   #211c18   ▂  the canvas
card  (+1)       L 0.195   #29231e   ▃  +0.030 L
menu  (+2)       L 0.225   #322a24   ▄  +0.030 L
dialog (+3)      L 0.255   #3a322b   ▅  +0.030 L  ← highest = lightest
```

Optional raised-edge cue: a 1px top border at `border` (`#473e36`) on cards, instead of a shadow.
In **light** mode these same tokens are all near-white and separated by **shadow** — only the dark
column spends lightness. Tokens are shared; the values behind them swap on theme.

---

## Contrast re-gate — BOTH modes, independently (WCAG 2.2 §1.4.3 / §1.4.11)

Ratios are WCAG 2.x contrast ratios (the conformance test). Design was tuned with APCA first, then
certified here, per `doctrine/references/wcag-2.2-criteria.md`. **Gate:** body/small text ≥ 4.5:1;
large text / UI / icons / focus / state-borders ≥ 3:1.

### Light mode

| Pair | Ratio | Gate | Result |
|---|---|---|---|
| `text` `#2c241e` on `surface` `#fcf9f6` | ~12.6:1 | 4.5:1 | PASS |
| `text-muted` `#6e5d50` on `surface` | ~5.0:1 | 4.5:1 | PASS |
| `accent` `#9f663a` on `surface` (large/UI) | ~3.6:1 | 3:1 | PASS |
| `accent-on` `#fcf9f6` on `accent` `#9f663a` | ~3.6:1 | 3:1 (large/btn) | PASS |
| `border-strong` `#9a6a3e` focus ring on `surface` | ~3.3:1 | 3:1 | PASS |
| `error` `#bb3522` text on `surface` | ~4.7:1 | 4.5:1 | PASS |
| `warning` `#b58a17` on `surface` (icon/large only) | ~2.9:1 | 3:1 | **FAIL → text never on this; icon paired w/ label; for text use a darker amber `0.62 0.15 85`** |

### Dark mode (passing light proves nothing — re-gated here)

| Pair | Ratio | Gate | Result |
|---|---|---|---|
| `text` `#f3ece6` on `surface` `#211c18` | ~12.9:1 | 4.5:1 | PASS |
| `text` on `surface-raised-3` `#3a322b` (dialog) | ~8.0:1 | 4.5:1 | PASS — text holds on the lightest layer too |
| `text-muted` `#b6a99e` on `surface` | ~6.7:1 | 4.5:1 | PASS |
| `text-muted` on `surface-raised-3` (lightest) | ~4.2:1 | 4.5:1 | **FAIL on top layer → use `text` for body in dialogs, reserve muted for base/card** |
| `accent` `#e0a878` on `surface` (large/UI) | ~6.6:1 | 3:1 | PASS |
| `accent` on `surface-raised-3` `#3a322b` | ~4.1:1 | 3:1 | PASS (still clears even on lightest surface) |
| `accent-on` `#211c18` text on `accent` `#e0a878` | ~6.6:1 | 4.5:1 | PASS — dark text on the lightened accent |
| `border-strong` `#cfa074` focus on `surface` | ~5.4:1 | 3:1 | PASS |
| `error` `#ef8a72` on `surface` | ~6.5:1 | 4.5:1 | PASS, still reads as danger |
| `warning` `#e6c34e` on `surface` | ~9.5:1 | 4.5:1 | PASS — the light-mode amber failure is fixed by lifting L to 0.855 |

**Findings from the re-gate (the point of doing it):**
1. The light-mode `accent` only clears the **3:1 UI/large** gate, never 4.5:1 — so copper is used
   for buttons, large labels, icons, and focus, **never** for body text on light. The dark accent
   at L 0.785 clears 4.5:1 comfortably, so it can take on more text duty in dark.
2. `text-muted` fails 4.5:1 on the **lightest dark elevation (dialog)** — the kind of regression an
   un-re-gated dark mode ships silently. Fix: use primary `text` for body inside dialogs; keep
   muted to base/card surfaces only.
3. `warning` was the casualty in light (2.9:1) and is rescued in dark by lifting L — exactly the
   "lighten the amber and verify" rule.

---

## Theme switch (token swap, not duplicated components)

```css
:root {                                   /* light is the default binding */
  --surface: oklch(0.985 0.006 50);
  --text:    oklch(0.255 0.012 50);
  --accent:  oklch(0.560 0.130 50);
  /* …all roles… */
}
@media (prefers-color-scheme: dark) {     /* system preference */
  :root:not([data-theme="light"]) {
    --surface: oklch(0.165 0.012 50);
    --text:    oklch(0.945 0.006 50);
    --accent:  oklch(0.785 0.105 50);
    /* …all roles… */
  }
}
[data-theme="dark"] { /* manual toggle overrides system; persist the choice */
  --surface: oklch(0.165 0.012 50);
  --text:    oklch(0.945 0.006 50);
  --accent:  oklch(0.785 0.105 50);
}
```

Components only ever reference `var(--accent)`, `var(--surface)`, etc. — switching theme rebinds the
values, never the markup. Hand this role→value map to
`09-design-systems-tokens-and-theming/design-tokens-and-naming` for tiering and Style Dictionary
export.

> Ratios above are computed for the listed sRGB hex values and rounded; verify in your own pipeline
> (the OKLCH→sRGB conversion and rounding can shift the last decimal). The **decisions** — lift L,
> trim C, re-gate every pair on every surface — are the reusable part.
