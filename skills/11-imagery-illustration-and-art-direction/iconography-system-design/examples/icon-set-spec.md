# Worked example — "Maru" icon system spec (v1.0)

A complete, concrete icon-system spec applied to a single product ("Maru", a fintech dashboard).
It shows every decision the skill requires: the stated style, the grid, the keylines, the
stroke system with hinting, the metaphor/perspective rules, the optical-balance compensation
table, and a worked **8-glyph sample set** drawn to the system. This is the pattern to copy for
any new set — not lorem; real numbers, real glyphs, real compensations.

---

## 0. Stated style choice (named before drawing — doctrine §2)

> **Maru icons:** 2px **outline**, **round cap**, **round join**, **2px outer corner radius**,
> **geometric-with-soft-corners** character, on a **24px grid**. Signature move: **all outer
> corners share one 2px radius and every diagonal is 45°** — this is the authored, repeatable
> move that keeps the set off the generic-Feather mean. Active/selected states use the **solid**
> companion (same silhouette, filled) — the only sanctioned outline→solid switch.

Why: Maru is a money product — it needs *precise but not cold*. Pure-sharp reads austere;
fully-rounded reads toy-like. The 2px soft corner + 45° rule is the deliberate middle.

---

## 1. Grid

| Element | Value | Notes |
|---|---|---|
| Artboard / viewBox | 24 × 24 | export base |
| Outer padding | 2 px | nothing critical in the trim |
| Live area | 20 × 20 | drawing zone |
| Pixel grid | 1 px | edges & stroke centers snap |

**Keylines** (live area 20×20):

| Keyline | Size | Glyphs assigned (sample set) |
|---|---|---|
| Square 18×18 | 18 | `image`, `settings` |
| Circle 20Ø | 20 | `user`, `warning` |
| Rect landscape 20×16 | 20×16 | — |
| Rect portrait 16×20 | 16×20 | — |
| Special (mass-balanced) | — | `play`, `chevron`, `search`, `trash` (balanced by mass, §4) |

---

## 2. Stroke system

- **Nominal:** 2 px, constant across every glyph at 24px. Busy glyphs are simplified, never
  thinned.
- **Corner:** 2px outer radius, inner sharp where notched.
- **Cap / join:** round / round.

**Per-size hinting:**

| Size | Hinted stroke | Action |
|---|---|---|
| 24 (master) | 2 px | — |
| 20 | 1.5 px | snap to half-pixel |
| 16 | 1.5 px | **redrawn master** (drop detail) |

---

## 3. Metaphor, perspective & direction rules

- **Perspective:** all glyphs **flat / front-on**. No isometric, no shadow.
- **Fill:** outline default; **solid** companion only for active/selected.
- **Direction:** arrows/chevrons share the **45° / single-angle** set; all directional glyphs
  (`chevron`, future `arrow`, `share`) **RTL-mirror** (see `internationalization-and-rtl-design`).
- **One concept ↔ one glyph:** `settings` = gear (never also "processing"); `trash` = delete
  (never a second "remove" glyph); `warning` ≠ `info` ≠ `error` (distinct glyphs).

---

## 4. Optical-balance compensation table

| Glyph | Keyline / box | Compensation applied |
|---|---|---|
| `image` | square 18 | reference size; corners 2px radius |
| `settings` (gear) | square 18 → simplified to 6 teeth | kept 2px stroke by widening teeth gaps |
| `user` | circle 20Ø | **+11%** vs square (head circle overshoots live area edge by ~0.5px) |
| `warning` (triangle) | circle keyline, triangle inside | **triangle apex overshoots +13%**; centered on visual mass, not bbox |
| `play` (triangle) | mass-balanced | **nudged +1.25px right**; apex sits on optical center |
| `chevron` | mass-balanced | arms balanced by weight; 45° arms; 2px gap to live edge |
| `search` (magnifier) | mass-balanced | **lens centered**, handle overhangs lower-right at 45° |
| `trash` | mass-balanced | lid + body centered as one mass; bin tapers; even slot spacing |

---

## 5. Worked sample set (8 glyphs)

Each glyph below is specified by construction, not just named. (Paths illustrative on the 24px
viewBox; stroke 2, round cap/join, `currentColor`.)

### `action-search`
- Lens: circle Ø10 centered at (10.5, 10.5). Handle: 45° line from circle edge (≈14.8, 14.8) to
  (19, 19), round cap. Lens centered, handle overhangs — optical center holds.
- a11y: in an icon-only search button → button target ≥ 24×24; `aria-label="Search"`.

### `action-settings`
- Gear simplified to **6 teeth** (not 8) so 2px stroke + 2px gaps fit the 18 square keyline;
  central counter Ø6 (≥2px so it doesn't fill at 16px). Front-on, no perspective.

### `media-play`
- Equilateral-ish triangle inside the live area, **apex right**. Centered at bbox + **1.25px
  right** so optical mass sits on center. Solid companion used for the "playing" active state.

### `user-account`
- Head: circle Ø8 at top (centered x=12), shoulders: arc below. Head on the **circle keyline
  (+11%)** so it doesn't read small next to `image`. Front-on.

### `action-trash`
- Lid bar (width 12) + handle tab on top; body trapezoid tapering down; **2 vertical slots**
  evenly spaced with equal end-padding. One glyph for delete — no separate "remove".

### `nav-chevron`
- Two 2px arms meeting at 45°, point right. Mass-balanced center; **RTL-mirrors** to point left.
  Reused (rotated) for up/down/expand — one source glyph, four orientations.

### `media-image`
- Square frame 18×18 (square keyline), 2px outer radius; inside: a small circle (sun, Ø3
  upper-left) + a 45° "mountain" polyline. The 45° diagonal obeys the global angle rule.

### `status-warning`
- Triangle (rounded 2px corners), apex up, **+13% overshoot** and **optically centered**;
  exclamation stem + dot inside. Distinct from `info` (circle) and `error` (octagon/x) — no
  metaphor collision. Color is **not** the only signal (pairs with text) — WCAG 1.4.1.

---

## 6. Export & naming

- Single **SVG sprite**, viewBox `0 0 24 24`, `fill="none"` + `stroke="currentColor"`,
  `stroke-width="2"`, round cap/join. Editor metadata stripped.
- Names (kebab, namespaced): `action-search`, `action-settings`, `action-trash`,
  `media-play`, `media-image`, `user-account`, `nav-chevron`, `status-warning`. Solid
  companions add `-fill` (`media-play-fill`).
- **Governance:** v1.0; new glyphs reviewed against this grid + stroke before merge, so the set
  doesn't fork.

---

## Why this beats the default (doctrine §0)
A reviewer can see one hand: every corner is the same 2px, every diagonal is 45°, every glyph
sits on a keyline, the gear was *simplified* rather than thinned, and the triangle was
*optically* (not mathematically) placed. That consistency — not any single clever glyph — is the
"looks human-made" signal. Borrowing 8 icons from 3 libraries would have none of it.
