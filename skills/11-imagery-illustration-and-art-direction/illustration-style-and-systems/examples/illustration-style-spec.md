# Worked Example: Illustration Style Spec — "Maduuka Merchant Tools"

A complete, concrete illustration-style spec for a sample brand. Reusable as a template — fill the
brackets for your own brand. Every value here is a spec (a number or a rule), not adjectives, per
`references/illustration-system.md` and `doctrine/design-doctrine.md` §2.

**Brand:** Maduuka Merchant Tools — point-of-sale + inventory + payments for small East-African
shopkeepers ("maduuka" = shops). Positioning: *capable, warm, on-your-side — built for a real
duka, not a Silicon-Valley demo.*
**Audience:** shop owners, market traders, micro-retailers.
**The one idea the illustration must carry:** *"running your shop, made lighter — by people who
get it."*

---

## 1. The five style attributes (stated first)

> **Line:** 2.5px variable-weight ink line (thins to ~1.5px at curve tails), round terminals,
> round joins, a deliberate slight hand-wobble. Outline colour is `ink-800` (#23201C), never pure
> black — softens the whole set.
> **Shape:** organic-rounded forms built from **three primitives** — pill, disc, and a soft
> "kanga-corner" quarter-arc; 8px minimum corner; flat fill plus **one** offset shadow tone per
> form (no gradients except the defined ramp below).
> **Colour:** a **5-step ramp** off the brand terracotta + one indigo accent. Light→shadow logic:
> shadow = same hue at −18% lightness. The indigo accent appears on ≤10% of any frame (the eye's
> single resting point). No other hues. Outline always `ink-800`.
> **Perspective:** **flat front-on only.** Depth is implied by overlap and the single shadow tone —
> never isometric, never vanishing-point. Held across the entire set.
> **Finish:** a light **6% halftone dot texture** on fills only (never on the line), giving a
> printed-poster, screen-printed-by-hand feel rather than a rendered-vector feel.

(If this paragraph couldn't be written, production does not start.)

---

## 2. The ownable motif (the one signature move)

**The kanga-corner + halftone print finish.** Every form resolves to the three primitives, but the
**quarter-arc "kanga-corner"** (borrowed from the rounded corner of a kanga cloth print) recurs as
the set's shape DNA — on shop awnings, receipt corners, speech bubbles, the cart. Combined with the
**6% halftone** finish, the work reads as *locally screen-printed*, not stock-vector. Crop the logo
off and the kanga-corner + halftone still says Maduuka. No corporate-Memphis blob set has a motif
like this — that's the point (`doctrine/design-doctrine.md` §0).

---

## 3. Spot vs scene — the density ladder

| Surface | Band | Background | Halftone | Characters | Detail |
|---|---|---|---|---|---|
| Feature tiles, empty states, list rows | Spot ≤120px | none / single kanga-corner shape | dropped | ≤1 | silhouette-clear single object |
| Onboarding steps, blog inline | Inline 200–480px | simple ground (counter line) | optional | 1–2 | medium, one prop |
| Homepage hero, "how it works" | Scene full-bleed | full duka environment | full 6% | 2–3 | foreground shop + background shelves |

A spot is **never** a shrunk hero — the empty-cart spot is redrawn as one clean object, not the
hero scaled down.

---

## 4. Character / object construction rules

- **Proportion:** 1:4.5 head-to-body, friendly-stylised — **explicitly not** the corporate-Memphis
  tiny-head/giant-noodle-limb caricature. Hands are simplified four-finger forms (never mittens,
  never the AI six-finger), feet implied by simple shoes.
- **Anatomy:** consistent elbow/knee bend logic; limbs taper into the body, no floating
  disconnected parts. Figures **have faces** — dot eyes, a single-line brow, a simple mouth that
  carries the expression. Faces are mandatory (the faceless dodge is banned).
- **Diversity with dignity:** real variation — different skin tones from the ramp's warm neutrals,
  a range of ages, body types, and dress (kitenge, kanzu, jeans, a hijab, a market apron). People
  are **specific**, not interchangeable blobs.
- **Objects from the same primitives:** a phone, a cash box, a sack of rice, and a shelf are all
  built from pill/disc/kanga-corner, the same 2.5px line, and the same halftone — so object and
  person read as one hand.

---

## 5. The consistency kit

- **Characters:** 4 reusable shopkeepers + 3 customers, on-model.
- **Objects:** phone, POS terminal, cash box, sack, shelf, receipt, cart.
- **Grounds:** counter line, shelf wall, open-air market stall.
- **Motif pieces:** kanga-corner arc, halftone swatch, speech bubble.

New illustrations are assembled from this kit — not improvised — so the set cannot drift into the
mixed-marketplace look (`references/illustration-system.md` §5).

---

## 6. Illustration vs photography — per surface

| Surface | Choice | Reason |
|---|---|---|
| Homepage hero | **Illustration** | Owns a signature look no stock can match; warmth without a stock-people cliché |
| "How it works" / concept (sync, offline, payments) | **Illustration** | Abstract/schematic, no literal subject — illustration wins (`§6`) |
| Empty states, feature tiles, 404 | **Illustration** | Spot system, on-motif, infinitely cheaper than photographing each |
| "Real shops using Maduuka" / testimonials | **Photography** | **Truth claim** — must be real shopkeepers; illustrating it would mislead → `photography-art-direction` |
| Team / about | **Photography** | Real people, credibility surface |

---

## 7. The sample set (4 frames, each on-system)

1. **Empty-cart spot (≤120px):** a single kanga-corner cart, terracotta fill + −18% shadow tone,
   2.5px ink-800 line, no background, halftone dropped (spot band). Reads clearly at 64px. `alt`:
   *"Empty cart — add items to start a sale."*
2. **"Sync" feature tile (inline ~320px):** a shopkeeper (1:4.5, faced, kitenge) holding a phone,
   a single arc of motion linking phone↔shelf; indigo accent only on the sync arc (≤10%); simple
   counter ground; optional halftone. `alt`: *"Inventory syncs between your phone and shelf."*
3. **Onboarding scene (full-bleed hero):** two shopkeepers at a market stall, full duka background
   (shelf wall + open stall), full 6% halftone, foreground/background layers, kanga-corner awning
   as motif, indigo accent on one signage element. Text overlaid on a deliberate quiet zone with a
   light scrim for contrast (WCAG 1.4.1 / contrast). `alt` describes the scene's point.
4. **404 page (inline):** a single shopkeeper looking at an empty shelf with a kanga-corner
   "?" speech bubble; meaning carried by the bubble shape + copy, **not colour alone**. `alt`:
   *"This page wasn't found."*

All four share line, shape, colour ramp, flat-front perspective, and the kanga-corner+halftone
motif — audited side by side before any single frame was refined.

---

## 8. Corporate-Memphis rejection (stated explicitly)

This set **refuses** the corporate-Memphis / blob-people default: no faceless figures, no tiny
heads on giant noodle limbs, no floating confetti shapes, no flat saturated purple/coral, no
rainbow palette. Faces are mandatory; the palette is the constrained 5-step terracotta ramp + one
indigo accent; every form carries the kanga-corner + halftone motif. The work is meant to be
recognisable as Maduuka with the logo cropped off (`doctrine/design-doctrine.md` §0).

## 9. AI reject gate (if AI assists)

AI may render *inside this stated system* on non-truth surfaces only, then a human cleans it onto
the motif. Reject any output showing (`doctrine/references/ai-slop-taxonomy.md` §Visual tells):
melted/incoherent detail, gibberish baked-in text, warped/misspelled signage, six-finger or fused
hands, mismatched lighting — **or** the AI's default blob-people regurgitation. Never ship
"because it's close." Truth surfaces (testimonials, team) are photographed, never AI-illustrated.

## 10. Export & a11y

Ship spots and inline frames as **optimised SVG** (themeable via `currentColor` for the ink line;
normalised viewBox; editor cruft stripped). Rasterise only the full halftone hero scene as AVIF/
WebP inside the LCP budget (`doctrine/references/web-performance-budgets-2026.md`). Every meaningful
frame has point-conveying `alt`; decorative motif flourishes use empty alt; no meaning by colour
alone (WCAG 2.2 1.4.1).
