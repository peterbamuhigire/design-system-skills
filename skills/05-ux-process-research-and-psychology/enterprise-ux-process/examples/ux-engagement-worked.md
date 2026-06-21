# Worked Example — Enterprise UX Engagement

**Client (sample):** *Meridian Trust Bank* — a mid-tier commercial bank launching a redesign of its **corporate treasury portal** ("Meridian Treasury") used by ~4,200 corporate clients to manage cash positions, initiate wires, and reconcile statements.

**Engagement context:** The legacy portal predates responsive design, fails WCAG, and drives a 31% support-ticket rate on wire initiation. The bank wants a premium, audit-defensible redesign. This engagement is declared at **UX Maturity Level 3 (UX Design)**, targeting selected Level 4 activities (Experience Maps) where the wire-initiation flow warrants them.

> **Maturity-level declaration:** *This engagement operates at UX Maturity Level 3, per Synechron's 5-level model, with two Level-4 activities (Experience Maps, Mood Boards) scoped for the wire-initiation flow only.*

---

## Part 1 — UX Maturity Assessment (scored dimensions)

Assessment performed against the 5-level model. Each dimension scored 1–5 (1 = absent/ad hoc, 5 = institutionalized). The score is the **current** state; the gap drives engagement scope.

| # | Dimension | Current | Target | Evidence for current score |
|---|---|---|---|---|
| 1 | Research practice | 2 | 4 | Occasional ad-hoc client calls; no contextual inquiry, no analytics instrumentation on the portal |
| 2 | Personas & journeys | 1 | 4 | No personas exist; "the corporate client" treated as one undifferentiated user |
| 3 | Information architecture | 2 | 3 | Navigation mirrors the bank's internal org chart, not client tasks |
| 4 | Interaction & prototyping | 2 | 3 | Developers build straight from tickets; no wireframe or prototype stage |
| 5 | Visual design system | 2 | 3 | Inconsistent components; no token library; three button styles in production |
| 6 | Heuristic & usability discipline | 1 | 3 | No structured evaluation has ever been run on the portal |
| 7 | Accessibility (WCAG/ADA/508) | 1 | 5 | Automated scan: 47 Level-A failures; keyboard traps in the wire form |
| 8 | Stakeholder alignment | 3 | 4 | Treasury product owner engaged, but risk & compliance not yet at the table |

**Composite maturity index:** 14 / 40 = **1.75 → Level 2 (Usability)** currently. The redesign must move the portal to a defensible **Level 3** with the wire flow reaching **Level 4** characteristics.

**Top three gaps driving scope:**
1. **No personas/journeys (dim. 2 = 1)** — premium pricing cannot be defended without persona-validated "Useful."
2. **Accessibility (dim. 7 = 1)** — a regulated bank with 47 Level-A failures carries legal exposure; this is a launch blocker at all levels.
3. **No evaluation discipline (dim. 6 = 1)** — the 31% wire-ticket rate has never been diagnosed against heuristics.

---

## Part 2 — Engagement Plan (phases, deliverables, gates)

14-week engagement. Each phase maps to the skill's 9-phase workflow. **Gates** are go/no-go checkpoints; a failed gate stops the phase clock until evidence is produced.

| Wk | Phase (skill ref) | Key activities | Deliverable | Gate (exit criterion) |
|---|---|---|---|---|
| 1 | P1 Problem Definition | Workshop with treasury product owner + 2 RMs | Signed problem-definition doc | **G1:** Funder signs vision/fears statement |
| 1–2 | P2 Stakeholder Interviews | 8 interviews: treasury, ops, risk, compliance, 3 corporate clients | Transcripts + summary brief | **G2:** Risk & compliance confirmed as stakeholders (closes dim. 8 gap) |
| 2 | P3 Success Criteria | Acceptance checklist co-authored | Signed success-criteria doc | **G3:** All stakeholders sign; criteria are measurable |
| 3–5 | P4 User Research | 6 contextual inquiries (clients reconciling live), portal analytics instrumented, 40-response survey | Research report (qual + quant) | **G4:** Wire-abandonment root causes evidenced, not assumed |
| 4 | P5 Competitor Analysis | Levy 19-column matrix; 5 direct (bank treasury portals) + 3 indirect (fintech cash tools) | Filled matrix + 1-page brief | **G5:** Differentiation thesis stated |
| 5–7 | P6 Personas + Journeys + IA | 3 personas (Treasury Manager, AP Clerk, CFO-approver); task-based IA; **Experience Map (L4)** for wire flow | Persona + journey + IA decks | **G6:** Personas pass Branson Mechanics floor; IA card-sort validated |
| 7–10 | P7 Wireframes + Prototype + Visual | Lo-fi → hi-fi wireframes; clickable prototype of wire-initiation + reconciliation; mockups + **Mood Board (L4)** + token library | Wireframe pack, prototype, mockup set | **G7:** Prototype walks the 3 critical scenarios end-to-end |
| 10–11 | P8 Heuristic Evaluation | Nielsen 10 review + Branson 4-stage affordance audit on "Initiate Wire" and "Approve" CTAs | Heuristic evaluation report | **G8:** Every flaw has a paired improvement |
| 11–13 | P9 Usability + Accessibility | 8 moderated sessions (5 remote, 3 in-person); WCAG 2.1 AA audit + remediation | Usability report + accessibility audit | **G9:** Zero unresolved Level-A failures; first-task success ≥ 70% |
| 14 | Pre-launch declaration | Compile evidence pack; score 5 outcomes | Maturity declaration + 5-outcomes gate | **G10:** 5-of-5 outcomes = Yes |

**Critical-scenario set** (drives prototype, heuristic, and usability scope):
- S1: Initiate a domestic wire with dual approval.
- S2: Reconcile a prior-day statement against an ERP export.
- S3: Investigate and act on a flagged exception.

---

## Part 3 — Value / ROI Framing

Premium pricing is defended by tying each phase to a measurable business outcome. The bank's baselines come from Phase 4 instrumentation.

### Baseline costs (current state)
| Metric | Baseline | Source |
|---|---|---|
| Wire-initiation support tickets | 31% of wire sessions | Phase 4 analytics |
| Avg. cost per support ticket | $18 (loaded) | Bank ops data |
| Wire sessions / month | ~9,500 | Portal logs |
| Annual wire-support cost | **9,500 × 0.31 × 12 × $18 ≈ $636,000** | Derived |
| Corporate client churn attributable to portal friction | ~2.5% / yr of 4,200 clients | Exit-survey estimate |

### Projected value (target state)
| Lever | Mechanism | Conservative annual value |
|---|---|---|
| Ticket reduction | Cut wire-ticket rate 31% → 12% via redesigned dual-approval flow (S1) | ~$390,000 saved |
| Reconciliation time | Cut avg. reconcile task time 40% (S2); RM hours redeployed | ~$120,000 capacity recovered |
| Churn avoidance | Halve portal-attributable churn (2.5% → 1.25%); avg. client value $14k/yr | ~$735,000 retained revenue |
| Accessibility risk | Remove 47 Level-A WCAG failures; avoid regulatory/legal exposure | Risk-avoidance (uncosted, board-visible) |

**Indicative first-year value:** ~$1.24M quantified + risk avoidance.
**Engagement fee:** $180,000.
**Indicative ROI:** ~6.9× on quantified value alone, excluding risk avoidance and brand value.

### ROI framing rules used
- Only **measurable** levers are counted; brand and risk-avoidance are named but not summed into ROI.
- Each lever traces to a **critical scenario** and a **phase deliverable** — no value claim without an artifact behind it.
- The ROI case is re-validated at **G9** against actual usability results before being stated to the board.

---

## Five-Outcomes Pre-Launch Declaration (G10)

| Outcome | Verdict | Evidence |
|---|---|---|
| Useful (persona-validated) | **Yes** | All 3 personas complete their primary journey in the prototype (P6/P7) |
| Easy to use (first-task success, no coaching) | **Yes** | 78% first-task success on S1 in usability testing (P9) |
| Efficient (task time benchmarked) | **Yes** | Reconcile task time down 43% vs. legacy baseline (P9) |
| Pleasing (≥ 4/5 first-impression) | **Yes** | Mean first-impression 4.3/5 across 8 participants (P9) |
| Accessible (WCAG 2.1 AA / ADA / 508) | **Yes** | Zero Level-A/AA failures on final audit (P9) |

**Result:** 5-of-5 = Yes → launch approved, premium pricing defensible.
**Rule applied:** 4-of-5 would have disqualified premium pricing; one No = no launch.
