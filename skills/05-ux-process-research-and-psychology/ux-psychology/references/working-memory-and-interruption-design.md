# Working Memory, Interruption and Resumption in Task Design

Parent skill: [`../SKILL.md`](../SKILL.md) (`ux-psychology`).

**When to read:** when a multi-step task, form, back-office workflow or navigation scheme asks
people to hold information in their heads, or when users are routinely interrupted mid-task
(counter staff, field agents, call-centre operators, mobile users on the move). This file
supersedes the "7 plus or minus 2" item caps in `legacy-guidance.md`; where the two disagree,
follow this file.

---

## 1. The current position on capacity (read before quoting a number)

| Claim you may meet | Current position | What to do in design |
|---|---|---|
| "People hold 7 plus or minus 2 items" (Miller, 1956) | Miller's paper was about span tasks and the power of chunking, not a UI rule. When rehearsal and grouping are prevented, measured capacity is closer to three to five chunks, often summarised as about four (Cowan, 2001). | Never cite 7 as a design limit. Design as if people can actively hold very little, and remove the need to hold it. |
| "Menus must have at most 7 items" | Menus are *seen*, not memorised. Scanning a visible list uses recognition, not working memory. | Size menus by findability and grouping (card sort, tree test), not by a count cap. |
| "Chunking makes long strings manageable" | Holds. A chunk is a unit the person already knows (a word, a familiar prefix, a known acronym); grouping only helps when groups are meaningful or visually separated. | Format identifiers in the grouping users already use; never invent groupings that clash with the printed or spoken form. |
| "Memory fades after about 30 seconds" | Decay durations vary with rehearsal, interference and task; single figures are not reliable design constants. `NOT_ASSESSED` as a numeric rule. | Assume anything not on screen is at risk the moment attention moves. |

Treat all of the above as hypotheses to check in testing (see the parent skill's decision rule),
not as proof that a design works.

## 2. Decision rules

| Situation | Rule | Failure caused by the wrong choice |
|---|---|---|
| A later step needs a value from an earlier step | Carry it forward on screen (summary strip, read-only echo) | Users flip back, re-type, or guess; transcription errors |
| User must compare options | Put the options side by side with the deciding attributes aligned | Users memorise one option while viewing another and choose on a distorted recall |
| Long identifier must be copied (account, transaction or phone number) | Offer copy, paste, scan or auto-fill first; when it must be read, display in the familiar grouping | Mis-keyed digits that pass validation and fail silently later |
| Task is long and interruptions are common | Break it into steps that each end in a saved, recognisable state (closure) | Interruption discards unsaved work; users restart or abandon |
| First-time or infrequent use | Recognition: visible choices, examples, defaults | Blank fields that demand recall of codes and formats |
| Daily expert use of the same commands | Keep recognition paths, add accelerators (shortcuts, type-ahead, recent items, saved filters) | Experts slowed by menus; or novices locked out by command-only UI |
| Error message refers to an earlier input | Show the offending value next to the message and the field | "Invalid entry" forces users to reconstruct what they typed |

## 3. Procedure: memory-load walk-through

1. List the task steps in order, from the user's trigger to confirmation.
2. For each step, write what the user must *know* that is not visible on the current screen
   (a number, an earlier choice, a rule, a customer's answer).
3. Mark each item: **carry** (display it), **recognise** (offer a choice), **retrieve** (auto-fill
   or look up), or **justified recall** (the user genuinely knows it, such as their own PIN).
4. Mark every point where an interruption is likely (a customer arrives, a call comes in, the
   network drops, the phone locks).
5. At each interruption point, confirm the three resumption conditions in section 4.
6. Re-draw the flow so no step depends on unsupported recall; test with a task that includes a
   deliberate interruption and measure whether participants resume correctly without help.

## 4. Designing for interruption and resumption

A person who is interrupted parks their current goal and context; the longer and more demanding
the interruption, the less reliably it comes back. Design so the interface, not the person,
remembers.

**Three resumption conditions (all required on interruption-prone flows):**

1. **State is preserved.** Drafts save automatically and survive timeouts, app switching and
   connection loss; session expiry never silently discards entered data.
2. **Place is visible.** On return, the screen shows where the user is (step name, progress,
   the record being worked on) without reading body text.
3. **Next action is cued.** The last completed action and the next required action are both
   stated ("Collateral recorded. Next: attach guarantor ID").

**Closure.** End each sub-task with a clear, saved outcome. Frequent closure lets the user put
the whole context down safely; one monolithic form keeps everything "open" until the end.

## 5. Worked example (original): SACCO loan-officer back office, Kampala

A loan officer at a Kampala SACCO captures loan applications at a counter while members queue and
the branch phone rings. The current system is one long form: member details, loan terms,
guarantors, collateral, and a final submit. Observed failures: forms lost when the session times
out during a phone call; guarantor member numbers typed from memory after switching to a lookup
screen; officers unsure, after an interruption, whether collateral photos were uploaded.

Redesign applying the rules:

- Split into four saved steps (Applicant, Terms, Guarantors, Collateral); each ends with
  "Saved" and a timestamp. Drafts appear on the officer's home screen as "Resume: Nakato A., step
  3 of 4".
- Guarantor search sits inside the Guarantors step; selecting a result fills the member number,
  which is displayed in the SACCO's printed grouping on passbooks.
- A persistent summary strip shows applicant name, amount and term on every step, so the Terms
  values never need recalling.
- The officer's daily accelerators (recent members, keyboard entry of amounts, a saved filter for
  "awaiting collateral") sit beside, not instead of, the visible navigation.

Acceptance test: five officers each complete an application with a scripted two-minute
interruption at step 3; pass if all resume at the right step with no re-entry and no lost data.
Result: `NOT_ASSESSED` until run.

## 6. Checks

- [ ] No design rationale cites "7 plus or minus 2" as a limit.
- [ ] Every value needed on a later step is displayed, recognised or retrieved, not recalled.
- [ ] Each interruption point meets all three resumption conditions.
- [ ] Novice recognition paths and expert accelerators both exist where daily experts use the tool.
- [ ] A test task includes a deliberate interruption, with the result recorded or marked
      `NOT_ASSESSED`.

---

**Evidence/currentness (accessed 2026-09-24):** Cowan, N. (2001) "The magical number 4 in
short-term memory", *Behavioral and Brain Sciences* 24, 87-114 (Cambridge University Press record,
cambridge.org) - capacity of about three to five chunks when rehearsal and grouping are
controlled. Specific decay durations and interruption-cost timings: `NOT_ASSESSED`; not used as
rules.

Sources: Branson (2020) *UX/UI Design: Introduction Guide to Intuitive Design and User-Friendly
Experience*; Miller (1956) "The magical number seven, plus or minus two"; Cowan (2001) "The
magical number 4 in short-term memory"; Sweller (1988) "Cognitive load during problem solving".
