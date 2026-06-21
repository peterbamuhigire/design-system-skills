# Worked Example — Onboarding research: plan → sessions → synthesis → decisions

A real, end-to-end study for **Maduuka**, a B2B inventory app for small East-African retailers. New-account activation (first product added within 24h) had stalled at **38%**. The team was split: PM wanted to cut the 5-step onboarding to 1 step; design lead suspected the problem was trust/clarity, not length. This study broke the tie.

---

## 1. The research plan (one page)

| Field | Value |
|---|---|
| **Decision** | Ship the proposed 1-step "just add a product" onboarding, OR keep the guided 5-step setup and fix it. |
| **Question** | Where and *why* do new shop owners abandon onboarding before adding their first product? |
| **Current assumption** | "Onboarding is too long; fewer steps = more activation." (PM's hypothesis — untested.) |
| **Method** | Mixed: (a) **analytics funnel** to find *where* the drop is; (b) **5 moderated usability tests** on the live flow to find *why*; (c) **15 unmoderated** task runs to quantify step-2 failure rate. (Method choice per `references/research-method-selector.md`: behavioural where + qual why + quant how-many.) |
| **Participants** | Real shop owners in Kampala & Nairobi, 1–10 staff, currently tracking stock on paper or WhatsApp. Screened OUT: anyone already using inventory software, anyone employed in tech. Incentive: 50,000 UGX airtime. 1 participant low-vision (uses OS font scaling) for access coverage. |
| **Tasks** | (1) "You just heard about this app and want to try it — get to where you can start adding your shop's stock." (2) "Add the first product you'd actually sell." |
| **Success criteria (pre-stated)** | Task 1: reaches the add-product screen unaided. Task 2: one product saved, ≤ 3 min, ≤ 1 assist. |
| **Decision rule (pre-committed)** | If failures cluster at *step length* → cut steps (PM right). If failures cluster at *one specific step's clarity/trust* → fix that step, keep the flow (design lead right). |
| **Schedule** | Analytics: day 1. 5 moderated: days 2–4. 15 unmoderated: days 3–5. Synthesis: day 6. |

---

## 2. Analytics funnel (where)

| Step | % of new accounts reaching | Drop |
|---|---|---|
| 1. Create account | 100% | — |
| 2. **Verify phone (OTP)** | 61% | **−39%** ← the cliff |
| 3. Choose shop type | 55% | −6% |
| 4. Connect/skip payments | 49% | −6% |
| 5. Add first product | 38% | −11% |

The drop is **not spread across "too many steps."** Nearly all the loss is a single cliff at **step 2 (phone OTP)**, plus a smaller bleed at step 5. That already dents the "just make it shorter" hypothesis — but it doesn't say *why* step 2 fails. Moderated sessions next.

---

## 3. Raw observations (separated from interpretation)

Logged as: `[P#] what happened — verbatim`. Interpretation deliberately withheld until synthesis.

- **[P1]** Entered phone, waited at OTP screen ~90s, no SMS arrived, refreshed, lost progress, gave up. *"Did it send? I don't know if I should wait or type again."* (FAIL task 1)
- **[P2]** OTP arrived but on a second phone (dual-SIM); typed it, worked. Then at step 4 *"payments? I'm not paying yet, why does it want my Mobile Money?"* — skipped warily. (PASS, 1 assist)
- **[P3]** No SMS for 2 min; *"the network here is bad in the afternoon."* Used the "resend" link — it was greyed for 60s with no countdown shown, so she clicked repeatedly thinking it was broken. (PARTIAL)
- **[P4, low-vision]** OTP input boxes were tiny separate squares; with OS font scaling they overlapped and she couldn't tell which had focus. *"I can't see where my cursor is."* (FAIL task 1)
- **[P5]** Sailed through OTP (good network), but at step 5 *"add product… do I need a barcode? I just sell tomatoes by the heap."* — the form demanded a SKU and barcode. Abandoned. (FAIL task 2)
- Unmoderated (n=15): **step-2 task success = 9/15 (60%)**, matching analytics. Top written complaint (7/15): *"didn't get the code."*

---

## 4. Synthesis — affinity themes + severity

Clustered the observations; rated each issue by frequency × impact × persistence (`references/usability-test-protocol.md` §6).

| # | Theme | Evidence | Severity |
|---|---|---|---|
| T1 | **OTP delivery is unreliable & the UI gives no status** — users can't tell if the SMS is coming, sent, or failed; resend has no countdown. | P1, P3 + 7/15 unmoderated; the 39% analytics cliff | **4 — Catastrophe** (the single biggest activation loss) |
| T2 | **OTP input is not accessible** — tiny split boxes break under font scaling; focus invisible. | P4 (blocked) | **3 — Major** (blocks an entire access group; WCAG 2.5.8 target size + 2.4.7 focus) |
| T3 | **Payment step feels like a trust trap** — asking for Mobile Money before any value is delivered reads as a scam risk. | P2 | **2 — Minor** (recovered, but erodes trust) |
| T4 | **First-product form assumes formal retail** — SKU/barcode required; informal sellers (heaps, bunches) can't comply. | P5 + step-5 bleed | **3 — Major** (excludes the core segment) |
| — | **Step *count* itself** | No participant abandoned because there were "too many steps." | **0 — Not a problem** |

Affinity note: the binding theme is **trust + reliability under real East-African network and retail conditions**, not flow length. Several quotes ("is it broken?", "why does it want my money?", "I just sell tomatoes") are credibility/authored-fit signals — the product didn't feel *made for them* (`doctrine/design-doctrine.md` §0; slop/credibility tells per `doctrine/references/ai-slop-taxonomy.md`).

---

## 5. Research-to-decision table (the point of the whole study)

| Finding | Evidence | Recommended decision | Confidence |
|---|---|---|---|
| The activation loss is OTP reliability + status, **not** step count. | T1: analytics 39% cliff + 9/15 + P1/P3 | **Do NOT ship the 1-step redesign.** Keep the flow; fix step 2: add SMS-status states ("sending / sent / didn't arrive"), a visible resend countdown, and a WhatsApp-OTP fallback for bad-network areas. | **High** (triangulated: analytics + qual + quant agree) |
| OTP input fails accessibility. | T2: P4 blocked | Replace split boxes with one large field (≥44px target), visible focus ring. Re-test with the same participant. | **High** |
| Premature payment ask costs trust. | T3: P2 | Move payment setup to *after* first product is added (deliver value first); label the skip clearly. | **Medium** (1 participant; watch in next round) |
| First-product form excludes informal sellers. | T4: P5 + step-5 bleed | Make SKU/barcode optional; allow unit "heap/bunch/piece". | **High** (matches the target segment definition) |

**Outcome:** the team shelved the 1-step rewrite (it would have shortened the flow while leaving the OTP cliff untouched — activation would barely have moved). They shipped the four targeted fixes instead. The decision rule pre-committed in the plan made this conclusion non-negotiable rather than a debate.

> **Why this study was worth running:** it traced a stalled metric to a *specific, fixable* cause, prevented a costly redesign that would have missed the real problem, and every recommendation is traceable to participant evidence — opinion never entered the decision.
