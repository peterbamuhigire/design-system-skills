# Worked Example — Before / After: a SaaS landing page hero

One real screen, taken from convergent AI-slop default to an authored, human-made version. The
product is a genuine one: **Cadence** — a tool that auto-drafts the weekly status update for
engineering managers by reading their team's merged PRs and closed tickets. Audience: busy EMs at
mid-size software companies. The one feeling it must leave: *"this respects my time and was built
by people who sweat the details."*

Real content used throughout (no lorem):

- Headline: **"Your status update wrote itself. You just sign off."**
- Subhead: "Cadence reads the week's merged PRs and closed tickets, drafts the update in your
  voice, and waits for your edit. No standup archaeology."
- Primary action: **"Draft this week's update"**
- Proof line: "Drafting for 1,240 engineering managers at Linear, Ramp, and Vercel."

---

## BEFORE — the convergent AI-slop default

What a templating tool (or an unguarded prompt) produces, described specifically so the tells are
unmistakable:

- **Type:** Everything in **Inter** — headline, subhead, button, footer, all of it. Headline at
  48px/600, body at 16px/400. One font, two weights a half-step apart. (Banned default + monotype
  — `doctrine/design-doctrine.md` §2.2/§2.3.)
- **Colour:** Headline sits on the **indigo → blue diagonal gradient** (`#6366F1 → #3B82F6`),
  the exact SaaS-default palette. CTA is the same indigo. (Anti-pattern: the purple-to-blue
  gradient as a personality substitute.)
- **Layout:** Hero is **dead-centred** — centred headline, centred subhead, centred pair of
  buttons ("Get started" + "Watch demo"), then a **uniform three-card row** of rounded,
  drop-shadowed feature cards with identical padding, each topped by a thin-line icon. Everything
  symmetric; nothing leads the eye anywhere it couldn't guess.
- **Surface:** The cards are **frosted glassmorphism** panels with a soft blur and a 0/8/24
  shadow, decoration with no information job.
- **"AI" theatre:** A little **✨ "AI-powered"** sparkle badge pinned top-right of the headline,
  and a purple chatbot bubble bolted to the bottom-right corner.
- **Content & craft:** Placeholder energy — generic "Boost your productivity" subhead, browser-
  disc bullets in the feature cards, no thought given to the empty or loading state, no hover
  beyond the default. Stock "diverse team pointing at a laptop" photo with slightly **waxy skin**
  and a **melted background** (`ai-slop-taxonomy.md` visual tells).

Why it fails the Mission: it is indistinguishable from ten thousand other launches. It tells a
discerning EM that no one thought about design — which undercuts the very claim ("we sweat the
details") the product is trying to make. Sameness here is free *and* actively off-message.

---

## AFTER — the authored, distinctive version

### The ONE distinctive decision (stated before any markup)

> **This artifact's distinctive decision is an asymmetric editorial split hero — a narrow,
> left-hung content column carrying the headline, set against a wide right field that shows a
> real, scrolling draft-in-progress — because the product's whole promise is "the writing is
> already done, you just sign off," so the screen should *show the artifact being written*
> rather than centre a generic pitch; grounded in Massimo Vignelli's principle that a grid
> earns its power by placing tension deliberately, not by centring everything
> (`doctrine/references/pairing-principles.md`, Vignelli).**

Supporting moves, all subordinated to that one idea:

- **Signature typeface (approved, not a banned face).** Headline in **Bricolage Grotesque** —
  the 03 Modern Product / Grotesque OFL display anchor (`font-groups-and-usage.md`), an idiosyncratic grotesque whose
  uneven, *almost-hand-cut* terminals literally read as "made by a person." Body and the live
  draft in **Hanken Grotesk** (08 Body / UI Workhorse). Two faces, crossed display-vs-body — never
  one font for everything. Bricolage was chosen on type-design grounds (its deliberate
  irregularity suits a product about human sign-off), not because any tool recommended it.
- **Real weight + size extremes.** Headline Bricolage at **900** weight, 72px; the live-draft
  body at Hanken **300**, 17px. A 900-against-300 contrast and a >4× size jump — no timid
  400-vs-600 mid-weights.
- **Asymmetry + one focal point + an eye-path.** The off-centre headline (left, ~40% column) is
  the focal point; the eye drops to the single primary CTA directly beneath it, then crosses
  right to watch the draft assemble line by line. One path, designed, not defaulted. No card grid.
- **A custom motif.** A **slim left bracket-rule** (`⌐` weight, 2px, in ink) brackets the
  headline column and recurs as the marker before each generated bullet in the live draft —
  a single signature device tying hero and product together. It replaces every browser disc.
- **Colour with intent, not the gradient.** Warm near-black ink (`#1A1714`) on a bone paper
  (`#F4F1EA`), with a single **signal ochre** (`#C25A1B`) reserved *only* for the CTA and the
  bracket-motif. No indigo, no purple-to-blue, no glass.
- **Real photographic/illustrative POV — stated rule.** No stock people. The only image is a
  single, honest **over-the-shoulder photograph of an actual laptop showing the Cadence draft
  mid-edit**, shot in available window light, slightly desaturated — one consistent, authored
  image language, never a stock-grab + AI-fill collage. (Passes every `ai-slop-taxonomy.md`
  visual tell: no waxy skin, no melted background, no warped logos, no uncanny faces.)
- **Craft details (≥3).** (a) Custom bracket markers instead of discs. (b) A **considered empty
  state** for the draft pane — real copy: *"Nothing merged yet this week. Cadence is watching —
  the draft starts the moment your first PR lands."* (c) A **micro-interaction with intent**: the
  draft text types in at a calm 40ms/line with a single consistent ease-out, and the CTA's ochre
  deepens on hover with a 120ms transition — motion with a reason, routed through
  `08-motion-and-interaction/`. (d) **Optical alignment** — the bracket-rule is nudged 1px left
  of the text bounding box so it reads as touching the cap-height, not floating.
- **No AI theatre.** No sparkle badge, no bolted-on chatbot. The intelligence is *shown* (a real
  draft assembling itself), not *announced* with a decorative ✨.

### Human-Craft Signature Checklist — run against the AFTER

1. **One distinctive idea named and committed** — the asymmetric editorial split hero that shows
   the draft being written. ✅ (One idea, not a hedge of several.)
2. **Decision stated with a contextual reason, grounded in named human authority** — tied to the
   product's "you just sign off" promise; grounded in Vignelli (deliberate grid tension). Zero
   reliance on "an AI tool suggests it." ✅
3. **Real weight extremes / size jumps / intentional space** — Bricolage 900 vs Hanken 300, 72px
   vs 17px (>4×), generous air around the headline, packed density in the live draft pane. ✅
4. **Intentional asymmetry + single focal point + designed eye-path** — left-hung 40% column,
   one CTA, eye crosses to the draft. No centred-everything, no card grid. ✅
5. **At least three craft details** — custom bracket markers, considered empty state with real
   copy, intentional typing + hover micro-interactions, optical 1px alignment. (Four.) ✅
6. **Real content throughout** — genuine headline, subhead, CTA, proof line, empty-state copy. No
   lorem, no "No data." ✅
7. **No convergent default present** — type (Bricolage/Hanken, not Inter), colour (ink/bone/ochre,
   not indigo gradient), layout (asymmetric split, not card grid), badges (none). ✅
8. **No slop visual tell** — single authored available-light photo; no waxy skin, melted
   background, warped logo, or uncanny face. ✅

All eight pass → cleared to build.

---

### The one-line takeaway

The BEFORE and the AFTER carry the **same words**. The difference is entirely authorship: one
strong, stated, human-grounded decision (show the draft writing itself, in an asymmetric editorial
grid, set in Bricolage) — subordinating type, colour, layout, motif, image, and craft to it —
turns a screen that *claims* "we sweat the details" into one that *proves* it. That is the moat:
looking human-made.
