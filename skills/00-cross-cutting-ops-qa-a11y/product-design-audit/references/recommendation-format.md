# Reference: Scoring, Prioritizing, and Routing Findings

This file defines the **output discipline** of a product audit: how a finding is scored
(severity), how the hard gates **cap** a surface's number, how findings are **prioritized**
(P0/P1/P2 = user-impact × effort), and how every finding is **routed** to the exact engine skill
that remediates it. The 0–100 math itself is reused from
`design-audit/references/audit-rubric.md` — do not re-derive it.

---

## 1. Severity (per finding)

Same scale as `design-audit` §Severity Definitions:

| Severity | Meaning | Typical examples |
|---|---|---|
| **Critical** | Blocks users, fails an accessibility law, risks data loss, or triggers a hard gate | Body text 2.9:1; no keyboard path; banned font as primary; LCP 6.2s |
| **High** | Significant UX degradation or frequent confusion | No empty states; non-idiomatic platform nav; broken responsive at 320px |
| **Medium** | Noticeable quality issue, occasional friction | Inconsistent spacing scale; "Submit" buttons; weak dark mode |
| **Low** | Minor polish, edge case, aesthetic preference | Slightly tight measure; one missing hover state |

---

## 2. The three hard gates and their caps (per surface)

Run these per surface; a failure **caps the surface's 0–100 score** regardless of dimension
scores (exactly as `audit-rubric.md` §1). Never report ≥ 60 for a surface while slop or a11y fails.

| Gate | Source ref | Fail condition (any) | Cap if FAILED |
|---|---|---|---|
| **AI Slop** | `ai-slop-taxonomy.md` + `ai-slop-banned-fonts.md` | Reads machine-generated (banned font + generic palette + uniform cards); or feature-cramming/ungrounded-chatbot tell; or slop imagery (warped logo, gibberish signage, uncanny faces) | **≤ 59** |
| **Accessibility (WCAG 2.2 AA)** | `wcag-2.2-criteria.md` | Body < 4.5:1 or UI/graphics < 3:1; or not keyboard-operable / no visible focus order; or target < 24×24 CSS px (mobile: < 44/48 platform min) without spacing; or focus obscured (2.4.11); or drag with no single-pointer alternative (2.5.7); or control missing name/role/value | **≤ 59** |
| **Performance (CWV / app)** | `web-performance-budgets-2026.md` | Web: field p75 LCP > 2.5s, INP > 200ms, or CLS > 0.1; or over archetype budget. App: cold-start/jank beyond the platform budget | **≤ 74** |

Two gates failed → cap at the **lower** cap. Slop and a11y are non-negotiable.

---

## 3. Prioritization — P0 / P1 / P2 (user-impact × effort)

Severity describes the *finding*; priority describes **what to do first**. Priority is a 2-axis
call: **user-impact** (how many users, how badly, how often) × **effort** (engineering/design
cost to fix). Map onto three buckets:

| Priority | Rule of thumb | Meaning |
|---|---|---|
| **P0** | High impact, **and** it trips a hard gate OR is low/medium effort | Do now. Blocks shipping or trivially fixable high-impact wins. (All gate failures are at least P0 unless genuinely huge effort, in which case P0-with-a-plan.) |
| **P1** | High/medium impact, medium effort, no gate trip | Next sprint. Real UX gains, scoped work. |
| **P2** | Lower impact or high effort relative to gain | Backlog. Polish, edge cases, nice-to-haves, large refactors with modest payoff. |

Decision aid (impact × effort grid):

```
                 LOW effort        HIGH effort
HIGH impact      P0 (quick win)    P0 / P1 (gate? P0)
MED impact       P1                P1 / P2
LOW impact       P2                P2 (often "won't fix")
```

**A gate failure is always P0** even if effort is high — it just ships with a remediation plan
attached, never deferred to P2.

---

## 4. Routing — every finding names the skill that fixes it

This is the defining move of a product audit: a critique you cannot act on is worthless. **Every
finding** carries the **exact engine skill** that remediates it (glob-verify the name). Use the
dimension→skill and lens→skill maps in `audit-dimensions.md` and `platform-lenses.md`. Common
routes:

| Finding | Routes to |
|---|---|
| Low contrast / colour-only signalling | `accessible-color-and-contrast` |
| Banned font (Inter/Geist/Roboto/Space Grotesk…) used | `font-selection-and-pairing` (+ `ai-slop-typography-audit`) |
| Generic palette / no token system / weak dark mode | `color-system-and-palette`, `dark-mode-and-theming` |
| No empty / loading / error states | `empty-error-and-loading-states` |
| "Submit"/"OK" buttons, unhelpful errors | `ux-writing-and-microcopy`, `error-empty-and-system-messaging` |
| Broken / non-responsive layout, no container queries | `responsive-and-adaptive-layout`, `layout-grid-and-spacing` |
| Missing interaction states, weak forms | `interaction-design-patterns`, `form-ux-design` |
| Bounce easing / animation fatigue / no reduced-motion | `motion-design` |
| Slow CWV / over budget | `performance-as-ux-and-core-web-vitals` |
| Confusing IA, orphan screens, weak nav | `navigation-and-information-architecture` |
| Dense data / bad tables / dashboard | `dashboard-and-data-product-design`, `data-visualization` |
| Looks machine-generated / templated | `distinctive-by-design`, `visual-product-slop-audit` |
| iOS non-idiomatic (HIG/Liquid Glass/Dynamic Type) | `ios-ui-ux-design` |
| Android non-idiomatic (Material 3 / dynamic colour / predictive back) | `android-ui-ux-design` |
| Web-app shell / desktop chrome issues | `webapp-gui-design` |
| Same feature named/behaving differently across surfaces | `cross-platform-design-parity` |
| WCAG conformance generally | `accessibility-wcag-2-2-compliance` |
| Trust / premium-readiness / proof gaps | `premium-ui-ux-design`, `landing-page-and-conversion-design` |
| Iconography inconsistency | `iconography-system-design` |
| Sector-specific UX (health/legal/fintech…) | `healthcare-ui-design`, `legal-sector-ui-ux`, `sector-strategies` |

If no skill fits, **say so** and route to the relevant `doctrine/references/*` instead — never
leave a finding un-actioned.

---

## 5. The recommendation table shape

Group rows by priority (P0 first), and within priority by surface:

```
| # | Pri | Surface | Dimension | Severity | Finding (evidence) | Standard violated | Fix | → Skill |
|---|-----|---------|-----------|----------|--------------------|-------------------|-----|---------|
```

- **Evidence** = where + what you observed (a real measurement/screen, not "feels off").
- **Standard violated** = the canonical ref (WCAG criterion, banned-font rule, CWV threshold).
- **Fix** = the specific change.
- **→ Skill** = the engine skill (or doctrine ref) that owns the remediation.

---

## 6. The per-surface scorecard + product roll-up

Per surface, fill the rubric worksheet (`audit-rubric.md` §4), extended with the two
product-level dimensions (IA/Nav, Trust) reported alongside:

```
Surface: <name>
Gates:  AI Slop [PASS/FAIL] · A11y WCAG 2.2 AA [PASS/FAIL] · Perf [PASS/FAIL]
Caps applied: [none | ≤59 | ≤74]
Score: <n>/100  ·  Band: <Production-ready | Good foundation | Significant issues | Major redesign | Fundamental>
IA/Nav: <0–4>   Trust: <0–4>
```

**Product roll-up.** The product is only as shippable as its **weakest blocking gate**: if any
in-scope surface fails slop or a11y, the product verdict is "not ready — blocking issues on
<surface>", regardless of the average. Report (a) each surface score, (b) the lowest surface, and
(c) the overall verdict + the single highest-leverage P0.

---

## 7. Banding (after caps)

| Score | Band | Meaning |
|---|---|---|
| 90–100 | Production-ready | Minor polish only |
| 75–89 | Good foundation | Fix high-priority before shipping |
| 60–74 | Significant issues | Focused remediation sprint |
| 40–59 | Major redesign | Multiple dimensions failing |
| < 40 | Fundamental | Start with structure and hierarchy |

---

*Reuses `design-audit/references/audit-rubric.md` for the 0–100 math and gate caps; severity and
banding match `design-audit`. Priority (P0/P1/P2) is impact × effort. Routing names are
glob-verified engine skills; un-routable findings fall back to a named `doctrine/references/*`.*
