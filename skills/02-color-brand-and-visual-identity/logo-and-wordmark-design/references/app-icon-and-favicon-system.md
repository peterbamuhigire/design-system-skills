# Reference: App-Icon and Favicon System

This is the *how* behind workflow step 8 of `logo-and-wordmark-design`. The whole icon set is
derived from the **monogram** (see `mark-construction.md` §5), never from a squashed lockup. A
favicon is the surface where Janoff's scale-relater rule bites hardest: at 16 px the mark must
still read as *itself*, not a smudge.

Design the icon **outward from the smallest size**: get the 16 px monogram right first, then
scale up and add only the detail larger sizes can carry — the reverse of shrinking a lockup.

---

## 1. The safe-zone discipline (decide before drawing any size)

Every modern icon platform crops or masks the icon, so artwork must live inside a safe zone:

- **Maskable / Android adaptive:** the visible area is a platform-chosen shape (circle,
  squircle, rounded square, teardrop) applied to your full bleed. Keep all essential artwork
  inside the **central ~66% (safe zone is the inner circle of diameter 66.6% of the canvas)**;
  the outer ring may be clipped on some devices. Background fills the full bleed.
- **iOS:** the OS applies the squircle mask and (on modern iOS) its own corner rounding — supply
  a **full-bleed square with no rounded corners and no transparency**; do not pre-round.
- **Favicon:** essentially no safe-zone padding luxury — the glyph must nearly fill the box to
  survive 16 px.

Pick the monogram's "tightest survivable" form for the maskable safe zone, then let it breathe
more on iOS/favicon where less is clipped.

---

## 2. The icon matrix (what to produce)

| Target | Format / size | Shape handling | Notes |
|---|---|---|---|
| **Web favicon (modern)** | `favicon.svg` | Square, full-bleed | Single source; supports light/dark via `prefers-color-scheme` inside the SVG |
| **Web favicon (fallback)** | `favicon.ico` (16, 32, 48 px) | Square | For legacy browsers; hand-tune the 16 px — do not auto-downscale |
| **Apple touch icon** | `apple-touch-icon.png` 180×180 | Full-bleed square, **opaque**, no rounding | iOS rounds it; never pre-round or add transparency |
| **Android / PWA standard** | 192×192 and 512×512 PNG | Square | `manifest.json` `icons` |
| **Android adaptive / maskable** | 512×512, `"purpose":"maskable"` | Foreground + background layers, 66% safe zone | Background is a flat brand fill, not transparent |
| **Monochrome / tinted** | SVG or 512 PNG, `"purpose":"monochrome"` | Single-colour silhouette | For themed icons; the mono variant from the mark spec |
| **Safari pinned-tab** | `safari-pinned-tab.svg` | Flat single-path, one colour | Pure silhouette; no gradients/strokes |
| **Windows tile** (if needed) | `mstile-150x150.png` + `browserconfig.xml` | Square | Optional; flat brand background |

Ship the SVG favicon as the source of truth; generate raster sizes from it, but **hand-correct
the 16 px and 32 px** rather than trusting an auto-downscale.

---

## 3. Per-size optical adjustments

The same monogram at different sizes is not the same artwork — the small sizes need help:

- **16 px:** strip to the essential silhouette. Remove the wit's fine detail if it muddies;
  keep the *structural* read. Increase stroke weight; open counters so they do not fill.
  Consider snapping key edges to the pixel grid.
- **32 px:** the device's small surprise should reappear here if it could not survive 16 px.
- **≥180 px:** full detail, full construction, optical corrections per `mark-construction.md`.
- **Contrast against tabs:** test the favicon on **both** a light and a dark browser chrome and
  against the OS light/dark home screen. A mark that vanishes on dark chrome is unfinished — use
  the SVG `prefers-color-scheme` swap or a contained background.

Background decision: a **transparent** favicon risks disappearing on coloured chrome; a
**contained** icon (monogram on the brand fill, inside the masked shape) is usually safer and
matches the maskable/Android treatment. State which you chose and why.

---

## 4. Wiring (the head/manifest the spec should hand off)

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#…brand…">
<link rel="manifest" href="/site.webmanifest">
```

```json
// site.webmanifest (icons array)
{
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" },
    { "src": "/icon-mono.svg", "type": "image/svg+xml", "purpose": "monochrome" }
  ]
}
```

---

## 5. The icon-set gate (run before sign-off)

1. **16 px legible** — monogram reads as itself on light *and* dark chrome.
2. **Maskable safe zone holds** — nothing essential is clipped inside the 66% circle; preview
   under circle, squircle, and rounded-square masks.
3. **iOS supplied full-bleed, opaque, un-rounded** — no transparency, no pre-rounded corners.
4. **Monochrome variant works** — the silhouette alone (Safari pinned-tab / themed icon) still
   reads as the brand.
5. **Derived from the monogram, not the lockup** — no squashed wordmark anywhere in the set.
6. **No AI-mark tells at any size** — no warped/fused detail introduced by auto-scaling
   (`ai-slop-taxonomy.md`).

If any item fails, fix before sign-off. A logo system that breaks at the favicon is not done —
this is the surface most users see most often.
