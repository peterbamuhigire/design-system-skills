# Worked Agent-UX Spec — "Ledger" Invoicing Copilot

A complete UX specification for one sample agent, written the way this skill expects:
concrete copy, ASCII layouts, state machines, dated timestamps. Use it as a fill-in
template — swap the product facts, keep the structure and the gate discipline.

Type styling: UI text uses the host product's system stack (`-apple-system`,
`Segoe UI`, `Roboto`); monospace surfaces use `ui-monospace`/`SFMono-Regular`. No
decorative or banned display fonts (no Comic Sans, no Papyrus, no novelty faces).

---

## 0. Agent at a glance

| Field | Value |
|---|---|
| Name | Ledger |
| Surface | Embedded right-rail copilot inside a web invoicing app + mobile inbox card |
| Job | Drafts, reconciles, and (on approval) sends invoices and credit notes |
| Autonomy | Supervised — proposes every side effect, executes only past a gate |
| Tool tiers | Read-only (search ledger, fetch rates), Moderate (draft, save), Destructive (send email, void invoice, post to GL) |
| Audit | Every run keeps a checkpoint stream + Tier-3 log (SOC 2 / tax retention) |

The six sections below map 1:1 to the brief: status surface, approval UX,
uncertainty/confidence, interruption/stop, error recovery, and the human-in-the-loop
gates that tie them together.

---

## 1. Agent status surface

Status answers three questions at a glance: *is it working, on what, and does it need
me?* Default to one line; let the user expand only when they want depth.

### Resting → Running → Needs-you → Done state line (Tier 1)

```
[Running]  Reconciling 3 of 8 invoices · "Match payments"      00:01:42   ⏸ Stop
[Waiting]  Needs your approval — send 2 invoices               00:02:11   ▸ Review
[Done]     Sent 2 invoices, 1 needs review                     —          ▸ Open
[Paused]   You paused at step 4. Resume or roll back.          00:02:30   ▸ Resume
```

- Always visible while the agent runs; never more than one line.
- No raw reasoning, no JSON, no tool names at this tier.
- A pending approval is **never** demoted into a passive toast — it stays on the line
  with a live `▸ Review` affordance until resolved.

### Expanded activity (Tier 2)

Opens on click. Shows the live plan as a checklist, current step, and a single
chronological activity feed — one source of truth, errors and edits inline.

```
+--------------------------------------------------------------+
| Ledger · Run #4827 · started 2026-06-21 09:14                 |
|--------------------------------------------------------------|
|  Plan                                                         |
|   [OK]  1  Pull open invoices (8 found)                       |
|   [OK]  2  Fetch FX rates (UGX→USD)                           |
|   [..]  3  Match payments to invoices        ← here           |
|   [ ]   4  Draft reminders for unmatched                      |
|   [ ]   5  Send (needs approval)                              |
|                                                              |
|   > Reasoning  (collapsed — click to expand)                 |
|                                                              |
|  Activity                                                    |
|   09:14:02  [OK]    Pulled 8 invoices                         |
|   09:14:18  [OK]    FX rate 3,780 UGX/USD (BoU, 09:00)        |
|   09:15:30  [WARN]  INV-209 has 2 candidate payments          |
|                                                              |
|   [⏸ Stop]   [Pause]   [Roll back]   [View full log]          |
+--------------------------------------------------------------+
```

Reasoning is a collapsed accordion by default — most users don't want the stream; the
ones who do click once. "View full log" links the Tier-3 auditable record (every tool
call, payload, checkpoint, permission outcome). Tier 3 is never auto-shown.

### Mobile status card

```
┌────────────────────────────┐
│ Ledger                 ⏸   │
│ Reconciling · step 3 of 5  │
│ ▓▓▓▓▓▓░░░░  3/8 invoices    │
│ 1 item needs you   ▸ Review│
└────────────────────────────┘
```

Tappable progress, a stop control top-right always reachable by thumb, and the
needs-you count surfaced on the face of the card.

---

## 2. Approval / confirmation UX

Every side effect routes through a gate sized to its blast radius. Three tiers, and
each prompt answers the same three questions: **What, Why, How to revoke.**

### Tier routing

| Tier | Examples for Ledger | Default gate |
|---|---|---|
| Read-only | search ledger, fetch FX, list invoices | Auto-run, log only |
| Moderate | draft invoice, save to drafts | Prompt first time per session; "approve for session" allowed |
| Destructive | send email, void invoice, post to GL, charge card | Prompt **every** call; no "don't ask again" |

### Moderate prompt (reversible)

```
Permission needed

What:   Save 2 invoice drafts to "Drafts / June"
Why:    Step 4 of plan — stage reminders before you review.
Scope:  This session only.
Revoke: Settings → Permissions → Session grants.

[Approve once]   [Approve for session]   [Deny]
```

### Destructive prompt (irreversible) — money + external comms

```
Permission needed — DESTRUCTIVE

What:   SEND 2 invoices by email and POST to General Ledger
          • INV-211  Acme Ltd     USD 4,200   → ap@acme.example
          • INV-214  Bold Co      USD   980   → finance@bold.example
Why:    Step 5 of plan — issue reminders approved in step 4.
Scope:  This single action. Ledger will ask again next time.
Revoke: n/a — sends and GL posts are always confirmed individually.

[Review each]   [Send all 2]   [Deny]
```

Rules that make the gate trustworthy:

- Show the **concrete operation and exact recipients/amounts** — never "send the
  reminders." If the *Why* isn't obvious from the plan, the plan is too vague; fix the
  plan, not the copy.
- `Review each` expands per-item approval so the user can send INV-211 and hold INV-214.
- Destructive tier never offers "don't ask again," and approvals/denials are written
  into the checkpoint stream as auditable events.
- Batch actions show a **count in the button** so the magnitude is unmissable.

### Approval state machine

```
[proposed] --user opens--> [reviewing]
[reviewing] --approve all--> [executing]
            --approve some--> [executing subset] ----> [partial]
            --deny--------> [denied → activity log]
            --edit--------> [proposed*]   (edited payload re-gated)
[executing] --ok----------> [done, new checkpoint]
            --error-------> [error-surface]   (see §5)
```

---

## 3. Uncertainty + confidence display

Ledger never launders a guess as a fact. Confidence is shown where the decision is
made, scoped to the specific claim, and tied to the evidence behind it.

### Three confidence bands → three behaviours

| Band | Threshold (illustrative) | Surface | Default action |
|---|---|---|---|
| High | model self-score ≥ 0.85 and single matching source | quiet inline note | proceed, still gated for side effects |
| Medium | 0.6–0.85, or one weak source | amber chip + "why" | propose, ask before acting |
| Low | < 0.6, conflicting/absent source | block + ask | stop and request human input |

### Inline rendering on a specific claim

```
INV-209  →  Payment TRX-5567   ⚠ Medium confidence (0.71)
  Two payments fall within the matching window:
    • TRX-5567  UGX 3,780,000  21 Jun  ← proposed match (amount + memo)
    • TRX-5571  UGX 3,780,000  21 Jun     (amount only)
  Basis: memo string "INV209" present on TRX-5567.
  [Confirm TRX-5567]   [Pick the other]   [Leave unmatched]
```

Principles:

- **Per-claim, not per-run.** A run can be 90% routine and still flag one line as
  medium. Confidence rides the line item, not a global meter.
- **Verbal + numeric.** "Medium (0.71)" — the word for fast reading, the number for
  audit. Never a bare percentage with no basis.
- **Evidence is one click away.** Every confidence chip links the *Sources* it rests on
  (source name, access time, open-link). No grounding → it cannot claim High.
- **Low confidence is a stop, not a shrug.** The agent surfaces the choice to a human
  rather than picking and hoping (see §6 gate G3).

---

## 4. Interruption / stop

Stop is a first-class control, not buried in a menu. The user can always halt the
agent, and halting is safe — it lands on a checkpoint, never mid-write.

### Stop affordances

- Persistent `⏸ Stop` on the Tier-1 line and the mobile card (thumb-reachable).
- Keyboard `Esc` (web) / long-press the card (mobile).
- Stop is enabled in every running state; it is the one control that never greys out.

### Three stop modes

```
Stop Ledger?

  ○ Pause          Freeze after the current step. Resume keeps all progress.
  ● Stop safely    Finish the in-flight read, roll forward to the last checkpoint,
                   then halt. No half-written sends. (default)
  ○ Hard stop      Abort the current tool call now. May leave step 3 incomplete;
                   Ledger will mark it dirty and offer rollback.

[Cancel]                                        [Stop safely]
```

### Stop state machine — no side effect survives a stop

```
[running] --stop safely--> [draining]    (in-flight READ allowed to finish;
                                           pending WRITES cancelled, never sent)
[draining] --reached checkpoint--> [stopped @ cp_N]
[running] --hard stop--> [aborting] --> [stopped, step dirty] --> offer [Roll back]
[stopped] --resume--> [running @ next step]
          --roll back--> [confirm rollback] --> [restored @ cp_N]
```

Guarantee: a **destructive call already approved but not yet executed is cancelled by
Stop, not flushed.** Stop must never become an accidental "send now." After stopping,
the user sees exactly what completed and what was cancelled, drawn from the same
activity feed.

---

## 5. Error recovery

Errors live in one chronological activity surface (the same feed as §1) — never split
across panels. Recovery is graded: retry transient faults quietly, escalate the rest to
a human with a concrete choice.

### Error taxonomy → response

| Class | Example | Agent response | User sees |
|---|---|---|---|
| Transient | 429 / timeout from FX API | auto-retry, backoff, cap 3 | `[RETRY] (1/3)` line, no interruption |
| Recoverable | invoice locked by another user | pause that item, continue others | item flagged, run proceeds |
| Ambiguous | 2 payment matches | surface choice (see §3) | medium-confidence prompt |
| Hard | GL post rejected: period closed | stop the step, escalate | error card + options |
| Permission | user denied a send | record denial, skip, continue | `[DENY]` line, no retry |

### Hard-error recovery card

```
✕ Couldn't post INV-214 to the General Ledger

  Reason: accounting period 2026-05 is closed (ERR_PERIOD_LOCKED).
  What happened: INV-211 posted OK. INV-214 was not sent or posted.
  Your ledger is unchanged for INV-214.

  [Retry in current period]   [Skip INV-214]   [Edit & re-draft]   [View full log]
```

Recovery principles:

- **State the blast radius first** — what *did* and *did not* happen. Partial success is
  shown explicitly (INV-211 done, INV-214 not), so the user never wonders if money moved.
- **Retries are visible but quiet.** Transient retries log a line; they don't throw a
  modal. Three strikes → escalate.
- **Every error offers a forward action**, not just an OK button: retry, skip, edit, or
  inspect. A dead-end error is a UX bug.
- **Rollback is always available** from the checkpoint stream; the error never corrupts
  earlier good work.

---

## 6. Human-in-the-loop gates

The gates are the spine that ties §§1–5 together. Each is a named, auditable
checkpoint where control passes to the human before the agent crosses a line of
consequence.

| Gate | Trigger | What's blocked until a human acts | Resolves to |
|---|---|---|---|
| G1 Plan approval | run start, before any side effect | drafting/saving | edit plan → run |
| G2 Pre-send review | before any Destructive call (send, void, GL post, charge) | the side effect itself | approve / deny / edit (§2) |
| G3 Low-confidence escalation | any claim below the Low band (§3) | the dependent step | confirm / override / leave |
| G4 Error escalation | Hard or Permission class (§5) | the failed step only | retry / skip / edit |
| G5 Post-run sign-off | run completes with money moved | nothing — review-after | acknowledge / dispute → rollback |

### Gate flow for one run

```
        G1 Plan approval
              │ approved
              ▼
   ┌──── read-only steps (auto) ────┐
   │   FX fetch · payment search    │
   └────────────┬───────────────────┘
                ▼
        G3? low-confidence match ──yes──► human picks (§3)
                │ no / resolved
                ▼
        moderate steps: draft, save (session-gated, §2)
                │
                ▼
        G2 Pre-send review  ──deny──► [logged, skipped]
                │ approve
                ▼
        destructive: send + GL post
                │
            error? ──► G4 escalation (retry/skip/edit, §5)
                │ ok
                ▼
        checkpoint + G5 post-run sign-off
```

Gate discipline:

- **Gates are checkpoints.** Each records who decided, when, and the outcome — the same
  stream Stop and Rollback land on. This is the audit trail (SOC 2, tax retention).
- **No silent escalation of autonomy.** Ledger cannot "earn" the right to skip G2 by
  succeeding before; destructive gates fire every time.
- **A gate must be answerable in the surface where it appears** — the §1 status line,
  the §2 prompt, or the §5 error card — never a separate tab the user has to hunt for.
- **Revocation in ≤ 3 clicks** from any screen: Settings → Permissions → Grants.

---

## Reuse checklist

When you adapt this for a different agent, confirm you still have all six:

- [ ] Status line states *working / on-what / needs-me* in one line, no raw JSON.
- [ ] Every side effect routes to a tier; destructive gates fire every call.
- [ ] Confidence is per-claim, verbal + numeric, links its evidence.
- [ ] Stop is always enabled, lands on a checkpoint, cancels un-flushed writes.
- [ ] Errors share one chronology; every error offers a forward action.
- [ ] HITL gates are named checkpoints in the audit stream, answerable in place.
