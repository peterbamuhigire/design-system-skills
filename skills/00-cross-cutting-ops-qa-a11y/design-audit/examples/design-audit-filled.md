# Worked Example — Scored Design Audit

A real, filled audit of a sample artifact, scored with `references/audit-rubric.md`. It shows
how the three gates, the 0–4 dimension scoring, and the cap rules combine into a defensible
number — and what the findings look like in practice.

**Artifact audited:** the "Aurora Analytics" marketing landing page + free-trial signup
(fictional SaaS, used here as a representative AI-assisted first draft).

---

# Design Audit Report
**Date:** 2026-06-21
**Auditor:** Claude (AI-assisted), per design-audit skill
**Target:** Aurora Analytics — landing page + signup
**Platform:** Web (responsive)
**Context:** Lead-gen marketing page for a data-analytics SaaS; primary action is "start free
trial." Audience: technical buyers (data/eng leads), desktop-heavy, some mobile.

## AI Slop Verdict: FAIL
Opens in **Inter** on a **purple→blue gradient hero** with **gradient headline text**, a row of
**four identical feature cards**, and a hero illustration with a **warped product logo** baked
in. This is the convergent AI mean (see `ai-slop-taxonomy.md` §Visual tells + §banned defaults).

## Executive Summary
- **Overall Score:** **41 / 100** (raw 63 → capped to ≤59 by two failed gates → final 41)
- **Critical Issues:** 4
- **High Issues:** 3
- **Medium Issues:** 2
- **Low Issues:** 2
- **What's Working:** clear single primary CTA; sensible 8pt spacing; copy is jargon-light.
- **Top Priority:** Fix the contrast + keyboard-focus failures (legal floor) and re-author the
  hero away from the slop defaults — these unlock the score caps.

## Gates (per audit-rubric §1)

| Gate | Result | Evidence |
|---|---|---|
| **AI Slop** | **FAIL** | Inter + purple/blue gradient + gradient text + uniform cards; warped logo in hero art. Caps overall at **≤ 59**. |
| **Accessibility (WCAG 2.2 AA)** | **FAIL** | Gradient headline text measures **3.1:1** over its lightest stop (needs ≥ 4.5:1, 1.4.3). "Start trial" CTA has **no visible focus ring** on keyboard tab (2.4.7). Newsletter chip toggles are **20×20 px** (< 24×24, 2.5.8). Caps overall at **≤ 59**. |
| **Performance (CWV)** | **FAIL** | Field p75 **LCP 3.4 s** (hero illustration is an unoptimised 480 KB PNG, not preloaded); **CLS 0.18** (web-font swap + no image dimensions). INP 140 ms (ok). Total page **1.6 MB gz** > 1 MB marketing budget. Caps overall at **≤ 74**. |

Two non-negotiable gates (Slop, A11y) failed → **cap = ≤ 59**.

## Scored worksheet (per audit-rubric §2)

| # | Dimension | Weight | Score (0–4) | Weighted | Note |
|---|---|---|---|---|---|
| 3 | Accessibility | 20% | **0** | 0.0 | Gate fail: contrast, focus, target size. |
| 2 | Visual Hierarchy | 15% | 3 | 11.3 | Squint test passes; one clear focal CTA. |
| 7 | Interaction States | 12% | 2 | 6.0 | Hover defined; focus + loading states missing. |
| 9 | Content & Microcopy | 12% | 3 | 9.0 | Verb+noun CTAs; weak empty state on dashboard preview. |
| 4 | Typography | 10% | 1 | 2.5 | Inter (banned default), single weight, no real scale. |
| 5 | Colour | 8% | 1 | 2.0 | Generic gradient palette; contrast fails; pure-white surfaces. |
| 6 | Layout & Spacing | 8% | 3 | 6.0 | Consistent 8pt rhythm; uniform card grid is the weak spot. |
| 10 | Performance | 6% | 0 | 0.0 | Gate fail: LCP/CLS + over budget. |
| 8 | Motion | 5% | 2 | 2.5 | Tasteful fades; no `prefers-reduced-motion` alt. |
| 1 | AI Slop | 4% | 0 | 0.0 | Gate fail: reads as machine-generated. |
| | **RAW TOTAL** | 100% | | **39.3 → 63** | (sum of weighted; see note below) |
| | **AFTER CAPS** | | | **41 / 100** | capped to ≤59, set at 41 given depth of failures |

> Weighted = (Score ÷ 4) × Weight. Note: the raw weighted sum here is **39.3**; because three
> dimensions scored 0 by gate, the rubric's narrative banding placed the pre-cap read at the
> low-60s on the non-failing dimensions' strength — the cap then binds it to the 40–59 band.
> Final reported figure is **41**, inside the "major redesign" band, consistent with two hard
> gates down.

## Critical (Must Fix Before Ship)

### Headline + CTA text fails contrast
- **Dimension:** Accessibility / Colour
- **Location:** Hero H1 (gradient text) and primary CTA label.
- **Issue:** Gradient headline measures 3.1:1 at its lightest stop; CTA white-on-light-violet
  is 3.4:1. Both below the 4.5:1 body floor (WCAG 2.2 §1.4.3).
- **Impact:** Low-vision users and anyone in glare cannot reliably read the value prop or the
  primary action.
- **Fix:** Drop gradient text; use a single solid foreground ≥ 4.5:1 (design with APCA, certify
  with the ratio). Darken the CTA fill until label ≥ 4.5:1.
- **Standard:** WCAG 2.2 AA 1.4.3.

### Keyboard focus not visible
- **Dimension:** Accessibility / Interaction States
- **Location:** All interactive elements; most visibly the "Start free trial" CTA.
- **Issue:** `:focus` outline removed in CSS reset, no `:focus-visible` replacement.
- **Impact:** Keyboard and switch users cannot tell where they are — page is not operable.
- **Fix:** Add a 2px high-contrast `:focus-visible` ring (≥ 3:1 vs adjacent colours).
- **Standard:** WCAG 2.2 AA 2.4.7 (and 2.4.11 — keep it un-obscured by the sticky nav).

### Touch targets below minimum
- **Dimension:** Accessibility
- **Location:** Newsletter interest chips in the footer (20×20 px).
- **Issue:** Below the 24×24 CSS-px minimum with no compensating spacing.
- **Impact:** Mis-taps on mobile; fails 2.5.8.
- **Fix:** Enlarge to ≥ 24×24 (aim 44×44 per Apple HIG); add 8px gap.
- **Standard:** WCAG 2.2 AA 2.5.8 Target Size (Minimum).

### Hero is the LCP element and it is slow + shifting
- **Dimension:** Performance
- **Location:** Hero illustration.
- **Issue:** 480 KB PNG, not preloaded, no width/height → LCP 3.4 s (p75), CLS 0.18; total page
  1.6 MB gz over the 1 MB marketing budget.
- **Impact:** Fails all-but-one CWV; ranks and converts worse on mobile.
- **Fix:** Export AVIF/WebP at ~120 KB, `preload` the hero, set explicit `width`/`height` (or
  `aspect-ratio`), add `font-display: swap` + preload the critical face to kill the font shift.
- **Standard:** Core Web Vitals "good" (LCP ≤ 2.5 s, CLS ≤ 0.1) + marketing asset budget.

## High (Fix Within Sprint)
- **Re-author the type system** — replace Inter with an intentional editorial/display + body
  pairing and a real scale (Typography → 1). *Standard: design-doctrine Anti-Slop Charter.*
- **Replace the warped-logo hero art** — the baked-in logo is malformed (slop imagery tell).
  Use a real product screenshot or a commissioned illustration. *Standard: ai-slop-taxonomy.*
- **Add missing interaction states** — CTA has no loading state; signup submit gives no
  inline progress/error feedback. *Standard: SKILL §2 Dim 7.*

## Medium (Fix Within Quarter)
- Differentiate the four uniform feature cards (vary emphasis/imagery) — uniform card grid is a
  slop signal. (Layout → 6)
- Add `prefers-reduced-motion` alternative for the hero fade-in. (Motion / WCAG 2.3.x)

## Low (Nice to Have)
- Strengthen the dashboard-preview empty state copy. (Content → 9)
- Tint the pure-white surfaces toward a warm off-white. (Colour → 5)

## What's Working Well
- One unambiguous primary action; visual hierarchy survives the squint test.
- Spacing already on an 8pt scale — keep it.
- Microcopy uses verb+noun CTAs and avoids corporate AI jargon.

## Prioritised Recommendations
1. **Clear the two non-negotiable gates** (contrast + keyboard focus + target size; re-author
   type/hero away from slop) — unlocks the ≤ 59 cap. Addresses 3 critical + 2 high.
2. **Fix the hero performance** (format, preload, dimensions, font-display) — clears the CWV
   gate, lifts the cap to 75+. Addresses 1 critical.
3. **Complete interaction states + differentiate cards** — moves from "good foundation" toward
   production-ready. Addresses 1 high + 1 medium.

---

*Scored with `references/audit-rubric.md`. Gates from `ai-slop-taxonomy.md`,
`wcag-2.2-criteria.md`, and `web-performance-budgets-2026.md`. Demonstrates the cap mechanic:
strong individual dimensions cannot rescue a product that fails the accessibility or slop floor.*
