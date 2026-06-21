# Reference: Dark-Mode Semantic Roles (role → light value / dark value)

The canonical mapping this engine uses to remap a light semantic palette into a true dark theme.
Every value is a **role**, never a literal hex sprinkled per component (per
`color-system-and-palette` step 4). Targets are given in **OKLCH** — `oklch(L C H)` where L is
0–1 lightness, C is chroma (~0–0.37 in sRGB gamut), H is hue in degrees — because OKLCH lightness
is perceptually uniform, so "move L up by 0.2" means the same perceived step everywhere. Hex is a
convenience; tune in OKLCH and convert.

These are **targets and directions**, not fixed colours — the exact values depend on your brand
hue. The rules (lower chroma on dark, lighten accents, elevation by lightness, re-gate contrast)
are the invariant part. Cite the hard contrast gate from `doctrine/references/wcag-2.2-criteria.md`
(§1.4.3 body text ≥ 4.5:1; §1.4.11 UI/large text/borders-that-convey-state ≥ 3:1).

---

## The remap rules (why dark ≠ inverted light)

| Property | Light mode | Dark mode | Why |
|---|---|---|---|
| Base surface L | high (~0.97–0.99) | **low, NOT 0** (~0.14–0.20) | `#000` causes halation; light text smears on pure black. |
| Surface chroma | low | **even lower** (~0.01–0.03) | Saturated darks read as a colour cast, not a neutral. |
| Brand hue in surface | trace | **trace, kept** | A brand-tinted dark grey looks authored; flat grey looks default. |
| Accent / status L | mid/dark | **raised ~+0.15 to +0.30** | A mid accent fails contrast on dark; lift L until it clears the gate. |
| Accent / status chroma | full | **trimmed** | Full chroma glows and vibrates on dark (simultaneous contrast). |
| Primary text L | low (~0.20) | **high, NOT 1.0** (~0.92–0.96) | Pure-white body text over-contrasts and shimmers like #000-on-white. |
| Elevation | drop shadow | **lighter surface** | Shadows are invisible on dark; depth = lightness. |
| Hue of any role | preserved | **preserved** | `error` must stay red, `success` green — only L and C move. |

---

## Role → light / dark value map (neutral template, brand hue = H)

Substitute your brand hue for `H` (e.g. a slate-blue brand might use H ≈ 250). Chroma values
assume a low-chroma brand; scale up for a vivid brand but re-gate.

| Semantic role | Light `oklch(L C H)` | Dark `oklch(L C H)` | Notes |
|---|---|---|---|
| `surface` (base/page) | `0.98 0.005 H` | `0.16 0.012 H` | Brand-tinted near-white / brand-tinted dark grey. Never `#fff` / `#000`. |
| `surface-sunken` (wells, insets) | `0.96 0.006 H` | `0.13 0.012 H` | Slightly *darker* than base in both modes. |
| `surface-raised-1` (card) | `1.00 0.000 H` | `0.19 0.012 H` | Dark: base **+0.03 L** → reads as raised. |
| `surface-raised-2` (menu/dropdown) | `1.00 0.000 H` (shadow) | `0.22 0.012 H` | Dark: **+0.03 L** again. Light uses shadow, not lightness. |
| `surface-raised-3` (dialog/popover/toast) | `1.00 0.000 H` (shadow) | `0.25 0.012 H` | Highest layer = lightest dark surface. |
| `text` (primary) | `0.22 0.01 H` | `0.94 0.005 H` | Dark ≈ L 0.92–0.96, NOT 1.0. |
| `text-muted` (secondary) | `0.45 0.01 H` | `0.72 0.006 H` | Must still clear 4.5:1 on its surface (or 3:1 if genuinely large). |
| `border` (subtle) | `0.88 0.008 H` | `0.30 0.012 H` | Low-contrast divider; need ≥3:1 only if it conveys state. |
| `border-strong` (focus ring, active) | `0.55 0.10 H` | `0.70 0.09 H` | Must hit ≥3:1 vs adjacent surface (1.4.11). |
| `accent` (brand voice) | `0.55 0.15 H` | `0.78 0.11 H` | **Lifted ~+0.23 L, chroma trimmed** — the headline remap. |
| `accent-on` (text/icon on accent fill) | `0.99 0.005 H` | `0.16 0.01 H` | Often dark text on the lightened dark-mode accent. |

### Status set (hue preserved; L up, C trimmed for dark)

| Role | Light `oklch` | Dark `oklch` | Watch |
|---|---|---|---|
| `success` (green, H≈145) | `0.58 0.15 145` | `0.80 0.12 145` | Easiest; still re-gate. |
| `warning` (amber, H≈85) | `0.70 0.15 85` | `0.85 0.14 85` | **The usual casualty** — goes muddy; lighten hard, verify ≥3:1 / ≥4.5:1. |
| `error` (red, H≈27) | `0.55 0.20 27` | `0.72 0.16 27` | Must still read as danger; don't let it pink out. |
| `info` (blue, H≈245) | `0.55 0.16 245` | `0.78 0.12 245` | Keep distinct from `accent` if accent is also blue. |

> Never rely on these hues alone to carry status — pair with an icon/label
> (`accessible-color-and-contrast`). Colour-blind users and greyscale rendering must still parse it.

---

## Elevation ramp (dark mode — depth by lightness)

Base is darkest; each layer up adds **~+0.02 to +0.04 L**, chroma held constant so the steps read
as depth, not a hue shift. Optional 1px *lighter* top border (e.g. `oklch(0.30 0.012 H)`) instead
of a shadow to imply a raised edge.

```
sunken        L 0.13   ▁
base/page     L 0.16   ▂
card  (+1)    L 0.19   ▃
menu  (+2)    L 0.22   ▄
dialog(+3)    L 0.25   ▅   ← highest = lightest
```

In light mode, the same elevation tokens resolve to `#fff`-ish surfaces differentiated by
**shadow**; only the dark column uses lightness. This is the Material "elevation overlay" model,
made explicit as surface tokens so it survives token export.

---

## The dark contrast re-gate (mandatory, per WCAG 2.2)

Passing in light proves **nothing** for dark — re-run the gate on the dark column independently.

1. Body / small text vs its surface → **≥ 4.5:1** (1.4.3).
2. Large text (≥24px or ≥18.66px bold), icons, focus rings, state-conveying borders → **≥ 3:1**
   (1.4.3 large / 1.4.11).
3. Check `accent` and **each** status colour against **every elevation surface** it can land on
   (base, card, menu, dialog) — a colour can pass on base and fail on the lighter dialog surface.
4. Design with **APCA** for perceived legibility, **certify with the WCAG ratio**
   (`doctrine/references/wcag-2.2-criteria.md`, "Contrast method note").
5. Any fail → raise L / trim C on the foreground (or adjust the surface) and re-check. Never ship
   a failing pair because "it looks fine."
