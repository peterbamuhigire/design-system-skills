# Worked example — a contrast-checked palette ("Lake Bunyonyi", a SaaS dashboard UI)

A real palette, hardened and certified end to end. The anchor is the deep blue-green water of
Lake Bunyonyi (a real place — anchor-first, per `color-system-and-palette`). This skill did **not**
pick the base hues; it took the candidate palette and (a) measured every pair, (b) caught and
fixed a real failure, (c) made the status set colour-blind-safe with non-colour cues, and
(d) re-certified dark mode.

Ratios below are computed with the WCAG 2.x relative-luminance formula
(`references/apca-vs-wcag.md`); thresholds are WCAG 2.2 SC 1.4.3 / 1.4.11
(`doctrine/references/wcag-2.2-criteria.md`). Conformance target: **AA floor, AAA where reached.**

---

## 1. The roles (light mode)

| Role | Hex | Note |
|---|---|---|
| `surface` | `#FBFBFA` | slightly warm off-white — not `#fff` (avoids vibration) |
| `text` | `#1A1C22` | near-black with a trace of the brand hue — not `#000` |
| `text-muted` | `#565A66` | secondary text |
| `border` | `#C9CCD4` → **retuned to `#8A8F9C`** | see the FAIL in §2 |
| `accent` | `#0B5FB0` | brand blue (link, focus ring, primary button fill) |
| `on-accent` | `#FFFFFF` | text/icon on the accent fill |

## 2. Contrast matrix — light mode (design with APCA, **certify with these**)

| Foreground | Background | Ratio | Threshold | Verdict |
|---|---|---|---|---|
| `text` `#1A1C22` | `surface` `#FBFBFA` | **16.45:1** | 4.5:1 body | ✅ PASS (AAA) |
| `text-muted` `#565A66` | `surface` | **6.65:1** | 4.5:1 body | ✅ PASS (AAA) |
| `accent` `#0B5FB0` (link text) | `surface` | **6.19:1** | 4.5:1 body | ✅ PASS (AAA) |
| `on-accent` `#FFFFFF` | `accent` `#0B5FB0` (button) | **6.41:1** | 4.5:1 body | ✅ PASS (AAA) |
| **focus ring** `#0B5FB0` | `surface` | **6.19:1** | 3:1 (1.4.11) | ✅ PASS |
| `border` `#C9CCD4` *(state-bearing — e.g. input outline)* | `surface` | **1.55:1** | 3:1 (1.4.11) | ❌ **FAIL** |

### The fix (this is what the skill exists to catch)
`#C9CCD4` as a *decorative* card divider is exempt (1.4.11 covers only **meaningful** UI
boundaries). But the same token was also the **input-field outline**, which *conveys the control's
edge* — so it must clear **3:1**. Retuned to **`#8A8F9C` → 3.13:1 ✅**. Lesson: split the token —
keep a faint `border-subtle` for pure decoration, add a `border-strong` (`#8A8F9C`) for any border
that does perceptual work (inputs, focused/selected states, dividers that mean something).

## 3. Status set — colour-blind-safe + non-colour cue (light mode)

Each status carries an **icon and a text label**, never colour alone (WCAG 1.4.1;
`references/colorblind-safe-palettes.md`). Hues are separated by **lightness** too, so they
survive greyscale and deutan/protan/tritan.

| Role | Hex | On `#FBFBFA` | Thr. | Verdict | Non-colour cue |
|---|---|---|---|---|---|
| Success | `#0F7D3D` | **5.04:1** | 4.5 | ✅ PASS | ✓ icon + "Success" |
| Warning | `#9A6700` | **4.70:1** | 4.5 | ✅ PASS | ⚠ icon + "Warning" |
| Error | `#C0341D` | **5.41:1** | 4.5 | ✅ PASS | ✕ icon + "Error" |
| Info | `#1257A8` | **6.86:1** | 4.5 | ✅ PASS | ℹ icon + "Info" |

**Greyscale / CVD check:** Success (L≈0.20) vs Error (L≈0.22) are close in lightness, so under
deuteranopia they could converge — the **✓ / ✕ icon is the guarantee**, the colour is the
accelerator. Ran Coblis for deutan/protan/tritan: with icons present, every state stays
unambiguous. (Warning leans dark-amber, not yellow — yellow can't clear 4.5:1 on white.)

## 4. Dark mode — a **separate** certification (not an inversion)

`surface` `#16181D` (near-dark grey carrying brand hue, not `#000`). Accents lightened and slightly
desaturated to hold their floor on dark — re-measured independently (skill step 6).

| Foreground | On `#16181D` | Threshold | Verdict |
|---|---|---|---|
| `text` `#E8E9ED` | **14.64:1** | 4.5 body | ✅ PASS (AAA) |
| `text-muted` `#A2A7B4` | **7.38:1** | 4.5 body | ✅ PASS (AAA) |
| `accent` `#6FB3F2` | **7.95:1** | 4.5 / 3 | ✅ PASS |
| `border-strong` `#646A78` (state-bearing) | **3.28:1** | 3 (1.4.11) | ✅ PASS |
| Success `#46C57E` | **8.07:1** | 4.5 | ✅ PASS |
| Warning `#E0A23A` | **7.95:1** | 4.5 | ✅ PASS |
| Error `#F08066` | **6.75:1** | 4.5 | ✅ PASS |
| Info `#6CA8E8` | **7.11:1** | 4.5 | ✅ PASS |

The light-mode border (`#8A8F9C`) gives only **1.66:1** on the dark surface — another independent
FAIL, fixed with the dark-specific `border-strong` `#646A78` (3.28:1). Proof that **light passes
never carry over** (skill step 6).

## 5. The over-contrast note

`#000` on `#fff` measures **21.00:1** — the maximum — yet it vibrates and haloes. We deliberately
chose `text #1A1C22` on `surface #FBFBFA` (16.45:1): comfortably above the 4.5 floor, no halo.
APCA flags the pure-black case where the WCAG ratio (which would happily "pass" 21:1) cannot
(`references/apca-vs-wcag.md` §Don't over-contrast).

## 6. Verdict & handoff

- **Light + dark certified to AA; most pairs reach AAA.** Two real failures caught and fixed:
  the state-bearing border in light *and* dark.
- Status set is colour-blind-safe and every meaning-carrying colour has a stated non-colour cue.
- Token note for handoff: split `border` into `border-subtle` (decorative, exempt) and
  `border-strong` (state-bearing, ≥ 3:1), per mode.
- Categorical/sequential **data-series** colours → hand to the data-viz group with the
  Okabe–Ito / Viridis ramps from `references/colorblind-safe-palettes.md`.
