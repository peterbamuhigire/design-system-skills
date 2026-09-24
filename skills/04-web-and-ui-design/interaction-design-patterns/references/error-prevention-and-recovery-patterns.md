# Error Prevention and Recovery Patterns

Parent skill: [`../SKILL.md`](../SKILL.md) (`interaction-design-patterns`).

**When to read:** when designing or reviewing any flow where a wrong action costs money, health,
records, reputation or time (transfers, payments, prescriptions, stock adjustments, payroll,
bulk edits, deletions, submissions); when support tickets or analytics show repeated "user
error"; when deciding between a confirmation dialog, undo, or a hard block; and when a product
has modes (offline/online, training/live, draft/posted, test/production).

This file covers the **interaction design** of prevention and recovery. The *wording* of error
messages lives in `10-content-design-and-ux-writing/error-empty-and-system-messaging`; the
undo-toast basics live in `interaction-principles-consistency-and-recoverability.md` section 6.

---

## 1. Classify the error before designing the fix

"User error" is a symptom. Classify what went wrong, because each class needs a different
countermeasure. A confirmation dialog, for example, catches some slips and almost no mistakes.

| Class | What happened | How it shows up in a product | Primary countermeasure |
|---|---|---|---|
| **Action slip: capture** | Right goal; a familiar, frequent action sequence took over from a rarer one that starts the same way | Cashier meant "Refund" but the habitual "Sale" path ran because both begin with the same two taps | Make the first steps of rare and frequent procedures look and feel different; put the rare one on a separate entry point |
| **Action slip: description-similarity** | Right goal; the action hit a neighbour that looks alike | Tapped "Delete" beside "Duplicate"; picked the wrong one of two identical account cards | Differentiate look, position and label; separate destructive controls; show distinguishing detail (last 4 digits, name, photo) |
| **Action slip: mode** | Right goal; the same control means something else in the current mode | Entries recorded in the training company; prices typed into quantity column after a toggle | Remove modes where possible; otherwise make the mode loud and persistent (colour band plus text), and reset to the safe mode |
| **Memory-lapse slip** | Right goal; a step was forgotten, often after an interruption | Card left in the reader; form abandoned half-way after a phone call; batch never posted | Keep state visible; save and resume; forcing function where a missed step is dangerous; reminders at the point of return |
| **Rule-based mistake** | Situation misread, so a sensible rule was applied in the wrong case, or a bad rule was followed | Clerk applies the standard VAT code to an exempt item; nurse follows the adult dose rule for a child | Make the situation obvious (show the distinguishing facts); build the rule into the system; flag exceptions |
| **Knowledge-based mistake** | Novel situation; the person reasoned from an incomplete or wrong model | New user thinks "Archive" deletes; first-time payer thinks the amount field is in thousands | Legible conceptual model, previews, worked defaults, plain explanations at the decision point |
| **Memory-lapse mistake** | The goal or plan itself was forgotten mid-task | Pharmacist resumes an interrupted order and dispenses without the pending interaction check | Show goal, progress and pending checks on resume; never discard in-progress state silently |

Novices tend to make mistakes; experts tend to make slips. Design for both on any screen used by
both populations.

## 2. The prevention and recovery ladder

Work down the ladder and stop at the first rung that controls the risk without taxing every
correct use. Higher rungs are stronger and cheaper for the user over time.

| Rung | Pattern | Use when | Cost if misused |
|---|---|---|---|
| 1. Eliminate | Remove the need for the risky action (automate the calculation, pre-fill from a trusted source, drop the mode) | The step exists only because the system could not do it | None; this is the best outcome |
| 2. Constrain | Offer only valid choices: pickers, masks, ranges, step gating, disabled-with-reason | Invalid input is knowable in advance | Over-constraint blocks legitimate edge cases; always provide an escalation path |
| 3. Forcing function | **Interlock** (step B impossible until A is done), **lock-in** (cannot leave while work would be lost), **lockout** (cannot enter a dangerous state without deliberate extra action) | A missed step or accidental entry causes serious harm | Users defeat annoying forcing functions (shared passwords, taped buttons); reserve for real hazards |
| 4. Sensibility check | Compare the request to what is normal for this user, account or context and ask when it is out of range | Values have a plausible range (amounts, doses, quantities, dates) | Checks that fire on normal values train people to click through |
| 5. Preview with object salience | Before commit, show the **object and the consequence** prominently, not only the verb ("Send UGX 250,000 to Namukasa Grace, 0772 ... 481") | Commit is costly and slow to reverse | Generic "Are you sure?" dialogs are dismissed by habit and catch nothing |
| 6. Undo | Act immediately and let the person reverse it; keep multi-level undo for editing tools | Reversal is technically possible, even if only for a window | An undo that silently expires or partially restores destroys trust |
| 7. Confirm | A deliberate second step for irreversible actions, naming the object and consequence, with the safe option as default | Reversal is impossible (external payment, legal filing, permanent deletion of shared data) | Confirmation for reversible actions adds friction and teaches dismissal |
| 8. Detect and recover | Make errors visible fast and repair them cheaply: reconciliation views, "did you mean", reversal requests, audit trails | Some errors will always get through | Recovery that needs a branch visit or a support call is a design failure for common errors |

Rules that follow from the ladder:

- **Prefer undo over confirmation** whenever reversal is possible. Confirmation interrupts every
  correct use to protect against a rare slip; undo costs nothing unless needed.
- **Confirm the object, not the action.** Slips happen because attention is on the verb; the
  confirmation must make the noun unmistakable.
- **Treat an unusual action as an approximation, not an offence.** Help the person reach what
  they meant (suggest the nearest valid date, the likely recipient, the corrected amount).
- **Never erase input on error.** Keep everything entered and point to the one thing to fix.

## 3. Interruption and resumption

Interruptions are a leading cause of memory-lapse errors and are normal in shops, clinics, agent
counters and field work. Design every multi-step task to survive one.

- Auto-save progress per step; resume at the exact point with a summary of what is done and what
  remains ("Items scanned: 14. Not yet: payment, receipt").
- Show pending safety checks on resume, never only at the original point.
- For long procedures, prefer an electronic checklist that tracks completion but allows safe
  reordering, over a rigid linear wizard.
- Protect critical phases: during commit, suppress non-urgent notifications and prompts.
- On shared devices, resumption must also confirm **who** is resuming (see
  `inclusive-and-assistive-design/references/low-literacy-low-bandwidth-and-emerging-market-design.md`).

## 4. Warnings and alarms

- One event, one channel, one message. Competing alerts cause the critical one to be missed.
- Rank alerts: blocking (needs action now), actionable (needs action soon), informational (no
  action). Only the first may interrupt.
- A warning must say what is wrong and what to do; attention without information is noise.
- If staff mute or dismiss an alert routinely, the alert is wrong. Fix the threshold, not the
  people.

## 5. Layered defences for high-stakes flows

Serious failures usually need several weaknesses to line up: a confusing screen, a missing check,
an interruption, a rushed operator. Design independent layers so that one failure is caught by
the next, and make the layers *different in kind* so they do not fail together:

1. Constraint at entry (valid formats and ranges).
2. Sensibility check against history or policy.
3. Salient preview of object and consequence.
4. Independent verification for the highest stakes (second approver, scan-to-match, recipient
   name lookup).
5. Reversal window or reconciliation after commit.
6. Audit trail that records what was shown to the person at each step.

Do not search for "the" cause of an incident. List every layer that let it through.

## 6. Turning "user error" reports into design changes

When support, audit or analytics show a repeated error:

1. Collect five or more concrete instances with screen state and context.
2. Classify each using section 1. A mixed picture means several fixes.
3. Ask "why" repeatedly until the answer is a design, policy or system property rather than a
   person's attention. Stop at the deepest cause you can change.
4. Pick the highest ladder rung that addresses it (section 2).
5. Define the measure that will show the fix worked (error count per 1,000 transactions,
   reversal requests, support contacts) and hand it to the product owner. Until measured, the fix
   is a hypothesis.

## 7. Worked example (original): mobile-money bulk payout for a Mbarara dairy cooperative

**Context.** A cooperative clerk pays 180 farmers monthly for milk delivered, from a web console
on a shared office laptop. Past incidents: one farmer paid twice; one payment sent to a
disconnected number; one batch left unposted for a week after the clerk was called away.

| Risk | Class | Countermeasure (ladder rung) |
|---|---|---|
| Duplicate farmer row after CSV import | Description-similarity slip | Detect duplicate phone numbers and names on import; block posting until resolved (rung 2) |
| Amount typed with an extra zero | Action slip | Compare each amount with that farmer's last six payouts and litres delivered; flag outliers above an agreed threshold (rung 4) |
| Wrong or recycled number | Knowledge-based mistake | Look up the registered name for each number before posting and show mismatches side by side (rung 5 and independent verification) |
| Batch forgotten after interruption | Memory-lapse slip | Draft batch banner on every screen with count and total; daily reminder to the approver; lock-in on logout while a batch is half-approved (rungs 3 and 8) |
| Clerk posts own batch | Rule-based risk | Interlock: a second user must approve batches over the policy limit (rung 3) |
| Payment already left | Irreversible | Final confirmation names total, count and largest single amount; safe default is "Back to review" (rung 7); post-run reconciliation lists failures with one-tap retry (rung 8) |

Measure after release: duplicate or misdirected payouts per 1,000 transactions, and median time
from batch creation to posting.

## 8. Premium versus generic output

| Generic | Senior |
|---|---|
| "Add a confirmation dialog for safety." | Classifies the error, chooses the highest effective rung, and reserves confirmation for the irreversible |
| "Are you sure you want to continue?" | "Send UGX 250,000 to Namukasa Grace? This cannot be reversed." with Back as default |
| Validation that clears the form | Validation that keeps input and points to the one field |
| Blames training | Treats repeated error as a design defect with a measurable fix |
| Same warning style for everything | Ranked alerts, one channel per event |

## Evidence and currentness

Concept inputs (durable): Norman (2013) *The Design of Everyday Things*, revised and expanded
edition, Basic Books (slip and mistake classes, forcing functions, sensibility checks, design for
error); Reason (1990) *Human Error*, Cambridge University Press (layered defences), as carried by
Norman; the engine's existing recoverability guidance. Current standard checked: W3C WCAG 2.2
Understanding SC 3.3.4 Error Prevention (Legal, Financial, Data), Level AA, requires that such
submissions be reversible, checked, or confirmed (page updated 2025-09-16; accessed 2026-09-24).
Platform-specific undo and alert guidance (Apple Human Interface Guidelines, Material Design 3)
was not retrievable in this pass and is `NOT_ASSESSED`; consult `ios-ui-ux-design` and
`android-ui-ux-design` before platform-specific specification. Sensibility thresholds in the
worked example are illustrative and must be set with the product owner.
