# Reference: Pairing Catalog (real display+body pairings, by context)

Concrete, named pairings you can adopt directly — every face checked against
`doctrine/references/ai-slop-banned-fonts.md` (none banned) and drawn from the approved baselines
in `doctrine/references/font-groups-and-usage.md`. This is the *menu*;
`doctrine/references/pairing-principles.md` is the *theory* (cross categories, contrast weight,
match x-heights, don't mix moods). Each row states **why it works** so the choice stays defensible,
never reflexive.

> Stating rule still applies: name the display face, the body face, and a one-line reason **before**
> producing the artifact. This catalog gives you the pairing and the reason; you supply the context fit.

---

## Group 1 — Editorial / Authoritative (reports, proposals, plans, whitepapers)

| # | Display / Header | Body | Why it works (principle) |
|---|---|---|---|
| E1 | **Fraunces** (900, `opsz`/`WONK` on) | **Source Serif 4** (400) | Two serifs, but *radically* different — Fraunces is a high-contrast "old-style with teeth," Source Serif is quiet and even. Concord of mood, contrast of weight (900 vs 400). The variable `opsz`+`WONK` give the headline character a body face can't compete with. |
| E2 | **Newsreader** (700, `ital` for decks) | **Public Sans** (400) | Serif display ↔ neutral sans body = the golden cross-category combination (Bonneville 25). Newsreader's news-serif warmth leads; Public Sans recedes. Matched x-heights. |
| E3 | **Spectral** (600) | **Public Sans** (400) | Spectral's narrow, literary serif against a plain grotesque body — strong style contrast, neutral body lets dense report text breathe. |
| E4 | **Crimson Pro** (700) | **Source Serif 4** (400) | When an all-serif, book-like register is wanted: pair only because the two are clearly distinct (Crimson is calligraphic, Source Serif is rational). Push weight to 700/400 to keep hierarchy obvious. |

Avoid: two *similar* serifs (Crimson Pro + Spectral) — muddy middle, fails Bonneville 2–3.

---

## Group 2 — Developer / Technical (dashboards, admin, API docs)

| # | Display / Header | Body | Code / data accent | Why it works |
|---|---|---|---|---|
| D1 | **IBM Plex Sans** (700) | **IBM Plex Sans** (400) | **IBM Plex Mono** (labels, code) | Superfamily pairing — designed to harmonise, so "two typefaces" come from one system. Contrast lives in **weight** (700 vs 400), per the principle "two typefaces, many fonts." Mono stays in its lane (code/data only). |
| D2 | **IBM Plex Serif** (600) | **IBM Plex Sans** (400) | **IBM Plex Mono** | A serif accent for long-form passages inside a technical product, still one superfamily — coherent and engineered-feeling. |
| D3 | **JetBrains Mono** (700, headings only) | **IBM Plex Sans** (400) | **JetBrains Mono** (code) | Monospace *display* gives a deliberately "engineered" headline; proportional body keeps reading fast. Never let the mono drift into body (Bonneville 24). |

Avoid: mono in body text; mixing IBM Plex Mono **and** JetBrains Mono in one product (two mono
moods clash).

---

## Group 3 — Startup / Product (landing pages, SaaS marketing, pitch decks)

| # | Display / Header | Body | Why it works | Note |
|---|---|---|---|---|
| S1 | **Bricolage Grotesque** (800) | **Hanken Grotesk** (400) | Bricolage's quirky, contrasty grotesque is the expressive face; Hanken is the calm geometric body. Both OFL — fully shippable. Weight extremes (800/400). | Baseline, no premium needed. |
| S2 | **Clash Display** (700, premium) | **Hanken Grotesk** (400) | Clash's confident, slightly condensed display reads as branded; Hanken recedes. | Clash is Fontshare — free to use/embed, not redistributable; scan `fonts/3-Startup-Product/`. |
| S3 | **Bricolage Grotesque** (800) | **Public Sans** (400) | When body must be maximally neutral (long marketing copy) under an expressive head. | All OFL. |
| S4 | **Cabinet Grotesk** (700, premium) | **Hanken Grotesk** (400) | Cabinet's tighter, modern-grotesque display for a sharper, more corporate startup tone. | Fontshare premium. |

Avoid the reflex: **Space Grotesk** here is the named AI convergence trap (`ai-slop-banned-fonts.md`)
— Bricolage Grotesque is the deliberate, non-slop distinctive grotesque instead.

---

## Group 4 — Body Workhorse layer (paired beneath a display face from 1–3)

These are body partners, never the headline. Use when the display face comes from another group.

| Display source | Workhorse body | Why |
|---|---|---|
| Any Group-1 serif | **Public Sans** (400) | Neutral grotesque body under a literary serif — maximum cross-category contrast. |
| Any Group-3 grotesque | **Hanken Grotesk** (400) | Warm, legible geometric — matches startup mood without competing. |
| Editorial, all-serif feel | **Source Serif 4** (400) | Quiet serif body that holds long passages. |
| Constrained / overused-OK | **Source Sans 3** (400, **paired only**) | Permitted *only* as a quiet body face beneath a distinctive display — never standalone, never the display (see banned list §3). |

---

## Cross-group "house" defaults (safe starting points)

| Context | Pairing | One-line reason to state |
|---|---|---|
| Business plan / proposal / SRS (DOCX/PDF) | Fraunces → Source Serif 4 | "Authoritative high-contrast serif head over a calm reading serif — reads considered and institutional." |
| Dashboard / admin UI | IBM Plex Sans 700 → IBM Plex Sans 400 + Plex Mono | "One engineered superfamily; weight carries hierarchy; mono confined to data." |
| SaaS landing / pitch deck | Bricolage Grotesque 800 → Hanken Grotesk 400 | "A distinctive grotesque headline that no template would pick, over a calm geometric body." |
| App / web UI body layer | Bricolage Grotesque → Hanken Grotesk | "Expressive display + quiet workhorse body; both OFL and embeddable." |

---

## Banned-face guard (run before committing any pairing)

Neither face may be: Inter · Geist · Roboto · Open Sans · Lato · Arial · bare system stack ·
Space Grotesk · Instrument Serif · Poppins · Montserrat · Nunito/Nunito Sans · Source Sans 3 *as a
display/standalone*. (Full reasons + labels in `doctrine/references/ai-slop-banned-fonts.md`.)

---

## References

- `doctrine/references/pairing-principles.md` (the 12 core moves these rows apply).
- `doctrine/references/font-groups-and-usage.md` (the approved baseline faces & premium folders).
- `doctrine/references/ai-slop-banned-fonts.md` (the guard list above).
- `skills/01-typography-and-fonts/font-selection-and-pairing/references/type-scale-recipes.md` (scale to apply once paired).
- `skills/01-typography-and-fonts/font-selection-and-pairing/examples/applied-type-scale.md` (a full worked brief).
