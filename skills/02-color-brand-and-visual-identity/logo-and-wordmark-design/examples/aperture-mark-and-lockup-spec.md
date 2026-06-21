# Worked example — mark + lockup spec: "Aperture"

A complete, applied mark+lockup specification produced by `logo-and-wordmark-design` for an
invented but realistic brand. It instantiates every output the skill requires and ends with a
filled Construction Gate. Use it as the shape your own deliverable should take — not as a
template to recolour.

**Brief (handed off from `brand-visual-identity`).** Aperture is a privacy-first photo-archive
app: your photos are stored end-to-end encrypted; *only you* can open them. Audience:
photographers and privacy-conscious families who distrust cloud galleries that scan their
images.
- **Essence:** *closed-to-everyone-but-you.*
- **Adjectives:** sealed · precise · quiet · optical · trustworthy.
- **Not-to-be-confused-with:** consumer cloud galleries (rainbow gradient flowers, AI-magic
  sparkles), generic camera apps (literal aperture-blade rings), security brands (shields and
  padlocks everywhere).
- **USP in one sentence:** *the archive is sealed — only the owner's key opens it.*
- **Surface set:** 16 px favicon → iOS/Android app icon → in-app UI → printed onboarding card →
  single-colour embroidery on a camera-strap. Must survive mono and dark.

---

## 1. The device (idea before execution)

**Chosen device: USP-encoded interactive wit (one device, two readings).**

The mark is a single ring whose opening is shaped as a **keyhole-aperture**: read one way it is
a camera aperture (photos); read the other way the same negative gap is a **keyhole** (only your
key opens it). The negative space *is* the surprise — invisible until seen, inevitable after
(the FedEx-arrow logic), and it encodes the USP directly: an aperture that is also a lock.

Rejected alternatives (silhouette iteration, "when in doubt leave it out"): literal aperture
blades (every camera app — fails not-to-be-confused), a padlock (every security brand), a
ring + sparkle (the AI-gallery cliché). All literal; none earned. Picked by conviction, not by
A/B test or an AI suggestion (`creative-selection-and-taste.md`, the "41 blues" rule).

---

## 2. Mark construction *(method → `references/mark-construction.md`)*

- **System:** circle-and-line, on a 24-unit modular grid.
- **Outer ring:** circle of radius 12 units, stroke weight 2.5 units (monoline). Counter radius
  9.5 units.
- **The keyhole-aperture (the device):** the ring is broken at the lower-right by a wedge cut at
  **45°**; into that gap the counter extends downward as a narrow 1.5-unit slot reaching 4 units
  past the inner counter — the slot reads as a keyhole's stem, the round counter as its head and
  as the lens opening. The wedge + slot together are the *one* surprise; nothing else is added.
- **Optical corrections:** ring overshoots top/bottom cap alignment by 1.5%; the wedge mouth is
  thinned 8% at the cut so the join does not pool; optical centre nudged up 1 unit.
- **Reproducible from:** base unit 24, radii (12 / 9.5), stroke 2.5, wedge angle 45°, slot width
  1.5 — a skilled hand redraws it from these alone (Rand).

```
        ╭───────╮
      ╱           ╲
     │   ╭─────╮   │      outer ring + lens counter
     │   │     │   │
      ╲  │     │  ╱
        ╲ ╲   ╱ ╱        45° wedge cut (lower-right)
          ╲ │ │          slot extends down = keyhole stem
            ╰─╯           (= the aperture-as-keyhole surprise)
```

---

## 3. Wordmark cut *(skeleton → `font-selection-and-pairing`)*

- **Source:** an approved modern-product grotesque (category 03), display weight, set as
  "Aperture" — chosen to share the brand display type's skeleton (one voice).
- **Modifications (one distinguishing detail, repeated logic):** the **lowercase "e" terminal**
  is redrawn as a small open slot echoing the mark's keyhole; tracking tightened 4% below the
  face default; the "rt" pair kerned bespoke to avoid a gap.
- **Fixed values:** cap-height = 12 units (matches ring diameter for alignment); the redrawn "e"
  is the only ownable letter — every other glyph stays true to the face.
- Never AI-lettered; never a banned face (`ai-slop-banned-fonts.md`).

---

## 4. Lockup family

| Lockup | Composition | Rule |
|---|---|---|
| **Primary (horizontal)** | mark + "Aperture" right of it | gap = 1 ring-radius (12 units); shared optical centre, not baseline |
| **Stacked** | mark above "Aperture", centred | gap = 0.5 ring-radius; wordmark optical-width ≤ ring width |
| **Monogram / glyph-only** | the ring-keyhole mark alone | favicon, app icon, strap embroidery |
| **Reduced wordmark** | "Aperture" set, no mark | inline/running contexts where the mark would be too small |

One governed set, no one-offs (Vignelli).

---

## 5. Clear-space & minimum sizes

- **Clear-space:** = the ring radius (12 units / 0.5 mark-width) on all sides of any lockup.
  Expressed in mark-units, never px.
- **Minimum sizes (favicon-verified, the scale-relater test):**
  - Primary horizontal: 120 px wide / 30 mm.
  - Stacked: 64 px wide.
  - Monogram: **16 px favicon** — verified: the wedge+slot survive because they were widened for
    the small size (see §7); a hair-thin blade version did not, and was rejected.

---

## 6. Responsive logo ladder

| Trigger | Shown |
|---|---|
| ≥ 480 px container | Primary horizontal lockup (full detail) |
| 240–479 px | Stacked lockup |
| 64–239 px | Monogram (ring-keyhole) + "Aperture" only if width ≥ 160 px |
| < 64 px / browser tab / app icon | Monogram glyph alone |

Detail is *dropped* at each step, not uniformly shrunk ("edit for less").

---

## 7. Favicon + app-icon system *(matrix → `references/app-icon-and-favicon-system.md`)*

- **Source of truth:** `favicon.svg`, monogram on a **contained** Sealed-Ink fill (transparent
  vanished on dark chrome — rejected). `prefers-color-scheme` swaps ring colour for dark mode.
- **16 / 32 px:** wedge widened to 2 units and slot to 2 units so the keyhole does not fill in;
  hand-corrected, not auto-downscaled.
- **Apple touch icon:** 180×180, full-bleed, opaque, **un-rounded** (iOS masks it).
- **Android adaptive / maskable:** foreground = ring-keyhole; background = flat Sealed-Ink;
  artwork inside the **66% safe zone** — verified under circle, squircle, rounded-square masks.
- **Monochrome / Safari pinned-tab:** single-path silhouette of the ring + slot; reads as the
  brand alone.

---

## 8. Colour, mono, reversed, dark variants *(colour → `../color-system-and-palette`)*

| Variant | Spec |
|---|---|
| Full-colour | ring in **Key Amber** (owned signature) on Sealed-Ink; lens counter empty |
| Single-colour positive | Sealed-Ink ring on Bone |
| Reversed | Bone ring on Sealed-Ink |
| Dark-mode | Key Amber ring on `--surface-900` |

Owned signature **Key Amber** (a single warm metal-key amber) chosen by conviction — it rejects
the gallery-rainbow gradient and the security-blue cliché outright (doctrine §2). Construction +
contrast certification deferred to `color-system-and-palette`.

---

## 9. Misuse sheet

Don't: recolour the ring to a gradient · fill the lens counter · close the keyhole slot (kills
the device) · add a padlock or sparkle · outline or drop-shadow · rotate the wedge off 45° ·
stretch · set on a busy photo without the Sealed-Ink scrim · substitute a stock geometric-sans
for the wordmark cut · use an AI-regenerated version of the mark.

---

## 10. Construction Gate — filled

| Gate item | Result | Evidence |
|---|---|---|
| Device present and earned (wit + USP) | ☑ Pass | aperture-as-keyhole in negative space; encodes "sealed — only your key opens it" |
| Reproducible from rules | ☑ Pass | unit 24, radii 12/9.5, stroke 2.5, wedge 45°, slot 1.5 all recorded (§2) |
| Reduction-proof (16 px / maskable) | ☑ Pass | wedge+slot widened for small sizes; 16 px favicon legible; 66% safe zone holds |
| Variant-complete | ☑ Pass | full-colour / mono / reversed / dark all specified (§8) |
| Lockup-governed | ☑ Pass | primary/stacked/monogram/reduced + clear-space (12 units) + min sizes (§4–5) |
| Memory test | ☑ Pass | "ring with a keyhole notch, amber" is the recallable core |
| No AI-mark tells | ☑ Pass | hand-constructed; no warped/fused/melted glyphs |

All items pass — the mark is buildable and ready to hand to `brand-visual-identity` for the
full system tie-in. Had any failed, the rule is: fix before sign-off, do not ship a half-built
mark.
