# Worked Example: Palette *Generation* for a Named Brief

This is palette **generation** — arriving at a deliberate *starting* palette from a brand/concept
anchor, a mood, and a harmony method. It stops at a candidate palette plus a 60-30-10 framing and a
quick contrast sanity check, then **hands off** to the sibling
`color-system-and-palette` to derive the full tonal ramps, semantic roles, and the hard WCAG gate.
It does **not** build ramps or assign roles here — that is the sibling's lane.

Every hex is the sRGB rendering of the stated `oklch()` value. Contrast figures are WCAG 2.x
relative-luminance ratios, used here only as a *go/no-go sanity check* on the candidate — not the
binding gate (that is re-run per role pairing downstream).

## Brief

- **Client / artifact:** *Marrow & Ember* — a Texas craft barbecue restaurant's website + menu.
- **Audience:** weekend diners and pit-curious foodies; warm, tactile, unpretentious.
- **Mood word:** *smoked* — slow heat, charred oak, brisket bark. Earthy and appetising, never neon.
- **Viewer action:** book a table / view the menu (one clear CTA).

## Anchor (a real thing, stated before any hex)

Not a vibe — a physical reference: **the bark on a smoked brisket** — deep mahogany-brown crust with
a glowing **smoke-ring red** just under the surface, against pale butcher paper. This anchor
deliberately rejects the indigo→blue slop gradient: barbecue is warm, low-chroma earth, not cool tech.

- **Primary hue:** warm brown, **H ≈ 55°** (oklch), anchored at `oklch(0.42 0.06 55)` ≈ `#6b4a2f`
  (charred-oak mahogany). Chroma kept low — bark is muddy-rich, not orange-bright.

## Harmony method

Mood (*warm, earthy, one appetising pop*) → the brief-to-harmony table points to **analogous +
one warm accent** (a near-complementary spark), not triadic or tetradic. Analogous browns/ambers
hold the smoked register; a single smoke-ring red is the 10% pop that reads as "appetite."

- Analogous neighbours of H 55°: amber **H ≈ 70°** and oak **H ≈ 40°**.
- Accent: **smoke-ring red, H ≈ 28°** — adjacent-warm, so it harmonises rather than clashes,
  but high enough chroma to pop against the browns.

## Candidate palette (OKLCH + hex)

| Token | Role intent | OKLCH | ~sRGB hex |
|---|---|---|---|
| Anchor — charred oak | primary brand | `oklch(0.42 0.060 55)` | `#6b4a2f` |
| Amber — analogous warm | secondary | `oklch(0.74 0.110 70)` | `#cf9a4e` |
| Oak — analogous cool-side | supporting | `oklch(0.55 0.070 40)` | `#9a6849` |
| **Smoke-ring red — accent** | the 10% pop | `oklch(0.55 0.150 28)` | `#b34a32` |
| Butcher paper — surface | dominant ground | `oklch(0.96 0.012 80)` | `#f6f1e7` |
| Char — near-black text | text | `oklch(0.26 0.018 55)` | `#2b2017` |

The surface is a warm off-white (butcher paper), not `#fff`; the text is a warm near-black, not
`#000` — keeping the whole palette inside the smoked register and pre-satisfying the
no-pure-black/no-pure-white rule before the system stage even begins.

## 60-30-10 framing

- **~60% butcher-paper surface** `#f6f1e7` — the quiet ground the food photography sits on.
- **~30% charred-oak + oak browns** `#6b4a2f` / `#9a6849` — headers, nav, structural chrome.
- **~10% smoke-ring red** `#b34a32` — the CTA ("Book a table"), active states, key menu marks only.
  Amber `#cf9a4e` is held as a sparing highlight inside the 30%, not a second accent.

This is a *balance gauge* for the candidate, not a literal three-colour cap — the accent earns its
scarcity.

## Quick WCAG sanity check (not the binding gate)

A fast go/no-go on the load-bearing pairs, to confirm the candidate is *worth* handing off — the
sibling re-runs the real gate per role:

| Pair | Ratio | Floor | Sanity verdict |
|---|---|---|---|
| Char text `#2b2017` on surface `#f6f1e7` | **12.1:1** | 4.5 | OK (ample headroom) |
| White `#fff` on accent `#b34a32` | **4.0:1** | 4.5 | **borderline-low** — flag for downstream |
| Charred oak `#6b4a2f` on surface `#f6f1e7` | **6.8:1** | 4.5 | OK (body/links on paper) |
| Amber `#cf9a4e` on surface `#f6f1e7` | 1.8:1 | 4.5 | text-fails — amber is a highlight/fill only, never body text |

**The one flag:** white-on-accent at 4.0:1 misses 4.5:1 for body text. Per the SKILL rule, the fix
is to **move the accent's shade down the scale, not re-pick the hue** — a slightly darker
smoke-ring red (≈ `oklch(0.50 0.150 28)` `#a23f29`) clears it while preserving brand identity.
Noted, not resolved here — resolving it is a ramp-step decision for the system stage.

## Hand off to the system sibling

The candidate is anchored, on-mood, harmonious, and roughly contrast-viable. Hand it to
**`color-system-and-palette`** to: build the perceptual OKLCH tonal ramps (50–900) for the brown
primary and the red accent, derive low-chroma warm neutrals from H 55°, assign the full semantic
role set, **run the hard WCAG gate** per pairing (including the flagged accent), and produce the
deliberate dark-mode remap. Generation ends here; the *system* is the sibling's job.
