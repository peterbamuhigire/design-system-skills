# Ledgerly — Content Voice & Tone Guide (worked)

**Version:** 1.0 | **Date:** June 2026 | **Prepared by:** Chwezi Core Systems
**Ratified by:** Content lead + 2 PMs (the "Content Council") | **Tiebreaker mode:** consensus,
falling back to **hierarchical** (Content lead decides) when consensus stalls past one review cycle.

A complete, no-placeholder content voice/tone system for **Ledgerly**, a small-business invoicing
app used by sole traders and tiny teams who are good at their craft and anxious about money admin.
This is the *operational* artifact the microcopy and error skills write against — not a brand
identity deliverable. Use it as the calibration target for specificity and the ratified-tiebreaker
discipline.

---

## 1. Product principles (the Voice Chart columns)

Ledgerly is designed around three ratified principles:

1. **Calm under money pressure** — money admin is stressful; the product lowers the temperature.
2. **Respects the user's expertise** — the user is an expert at *their* business; we never condescend.
3. **Gets out of the way** — the fastest path to "invoice sent", minimum ceremony.

---

## 2. The Voice Chart (six aspects × three principles)

| Voice aspect | **Calm under money pressure** | **Respects the user's expertise** | **Gets out of the way** |
|---|---|---|---|
| **Concepts** | Frame money events as facts the user controls, never alarms or threats. | Treat the user as the decision-maker; we inform, they decide. | Lead with the action, not an explanation of the action. |
| **Vocabulary** | "due", "sent", "declined", "overdue" — plain. Ban "URGENT", "failed!", "oops", "uh-oh". | Business words the user already uses ("invoice", "client", "VAT"); never baby-talk ("monies", "lil"). | Verbs first: "Send", "Add", "Mark paid". Ban "simply", "just", "easily". |
| **Verbosity** | One sentence of fact + one next step. No reassurance padding. | Enough to inform a competent adult; no over-explaining the obvious. | Shortest string that is still clear. Silence where the result is visible. |
| **Grammar** | Second person, active voice. Imperative for the next step ("Add a card"). | "You"/"your"; never the royal "we" deciding *for* the user. | Imperative, present tense. Drop articles in dense UI ("Invoice sent"). |
| **Punctuation** | Periods only. **No exclamation marks.** Em-dash allowed for a single aside. | No scare quotes, no ironic punctuation. | Minimal terminal punctuation in labels; no trailing ellipses as filler. |
| **Capitalization** | Sentence case everywhere. | Sentence case; product nouns ("Ledgerly") capitalised, generic nouns not. | Sentence case in buttons and labels; never Title Case Or ALL CAPS. |

**Designed tension (kept on purpose):** *Gets out of the way* (say less) pulls against *Calm under
money pressure* (reassure on scary events). At a payment decline this tension is resolved by the
**tiebreaker**: Calm wins on failure/billing screens (one extra reassuring clause is allowed); Gets-
out-of-the-way wins everywhere else. Recorded so no one re-litigates it per screen.

---

## 3. Voice Guide — "We are / We are not / Examples"

Every "We are not" names a *legitimate adjacent trait a writer might hit by accident* — not an
antonym, not a strawman, not an irrelevance.

| We are | We are not | Examples |
|---|---|---|
| **Calm** | **not Soothing** (we state facts plainly; we don't coo "don't worry, it'll be okay") | ✓ "This invoice is 6 days overdue." ✗ "Eek, your invoice is super late!" |
| **Respectful of expertise** | **not Deferential** (we're confident, not grovelling or hedging every sentence) | ✓ "Add VAT at 20%?" ✗ "We think you might possibly want to maybe add VAT?" |
| **Efficient** | **not Curt** (terse, but never cold or robotic toward a stressed user) | ✓ "Invoice sent to Aria." ✗ "Done." |
| **Plain-spoken** | **not Folksy** (clear everyday words, not down-home slang or chumminess) | ✓ "Payment received." ✗ "Cha-ching! Money in the bank, partner." |

*(Trap check: "Soothing", "Deferential", "Curt", and "Folksy" are all traits a real product
legitimately wants — they are the cliff edges next to ours, where a well-meaning writer actually
falls. None is an antonym or a strawman.)*

---

## 4. Tone Map — one voice, variable tone

Voice is constant (the chart above). Tone flexes by **magnitude** and **direction**.

### 4a. Across a flow — sending an invoice

```
Create invoice    →  neutral, low magnitude        "New invoice"
Add line items    →  neutral, low                   "Add item"
Review & send     →  reassuring, +1                 "Send to {client} — they'll get a payment link."
Payment declined  →  calm-precise, steady (NOT −)   "{client}'s card was declined. They can try
                                                      another card from the same link."   ← voice tested hardest
Paid              →  warm, +1, then exit            "Paid in full. Nice."
```

### 4b. Across the user lifecycle

| Lifecycle stage | Tone direction | Magnitude | Sample string |
|---|---|---|---|
| **Onboarding** | warm, guiding | high | "Let's send your first invoice — it takes about a minute." |
| **Habitual use** | quiet, terse | low | "Invoice sent." (no celebration) |
| **Overdue / chasing** | calm, firm | medium | "This invoice is 6 days overdue. Send a reminder?" |
| **Billing failure (own card)** | calm, precise | steady | "We couldn't renew your plan. Update your card to keep sending invoices." |
| **Churn / cancel** | respectful | low | "Your plan ends 30 June. Your data stays available until then." |
| **Resurrection** | welcoming | medium | "Welcome back. Your clients and invoices are right where you left them." |

**Code-switch points (named):**
- **Habitual → high-warmth** at *resurrection* only (don't gush during daily use).
- **Any → calm-precise** the moment a money event fails — overrides the terse default; this is where
  *Calm under money pressure* takes the tiebreaker.

---

## 5. Casual ≠ Conversational ruling

**Ledgerly is conversational, not casual.** We write how a calm, competent human talks — positive
contractions ("you'll", "we couldn't"), plain words, turn-taking. We are **not** casual: no slang,
no jokes in money flows, no exclamation marks. *Conversational is always on; casual is off, by
ratified choice tied to "Calm under money pressure".*

Negative-contraction rule: prefer **"do not"** over "don't" where the negation is load-bearing in a
high-stakes string ("This cannot be undone"); "don't" is fine in low-stakes copy.

---

## 6. Terminology glossary & governance

**One term per concept** (rejected alternates struck through so drift is visible):

| Concept | Approved term | Rejected |
|---|---|---|
| A person you bill | **client** | ~~customer~~, ~~contact~~ |
| The billing document | **invoice** | ~~bill~~, ~~statement~~ |
| Past its due date | **overdue** | ~~late~~, ~~delinquent~~ |
| Money received | **paid** | ~~settled~~, ~~cleared~~ |
| The subscription | **plan** | ~~subscription~~, ~~membership~~ |

**Banned lexicon:** "simply", "just", "easily", "oops", "uh-oh", "URGENT", "leverage", "seamless".
**Inclusive-language bans:** never call input **"invalid"** or **"illegal"** — say what's expected
("Enter an amount over £0"); default to singular **"they"** for a client of unknown gender; no
internal jargon (`null`, `token`, raw codes) in user-facing prose.

**Governance rule:** the glossary is the single source of truth writers and engineering pull from. A
new term is proposed in the Content Council; **the Content lead approves or retires terms**; a
retired term is struck through here (not deleted) so the history of the decision survives. Reviewed
each release.

---

## 7. Boundary note (kept in the deliverable)

This guide defines **what Ledgerly's words should be and whether a string is on-voice.** It does
**not** judge whether a passage reads as **generic machine-written prose** — that textual AI-slop
detection is the **digital-research engine's writing-slop skills**, not this one. When auditing
AI-drafted copy: this guide answers *"is it on-voice?"*; the research engine answers *"does it read
as AI slop?"* Use both; duplicate neither.

---

## 8. Handoff

- `ux-writing-and-microcopy` and `error-empty-and-system-messaging` write against **this** guide;
  their "voice source" pointer is updated from `brand-style-guide` to here.
- `02-…/brand-style-guide` references this guide for the operational content voice/tone system and
  does not restate the Voice Chart or Tone Map.
- Any LLM that drafts Ledgerly copy is trained/prompted on this guide and held to **HAHAS**.
