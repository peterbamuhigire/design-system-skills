# Reference: Text-Pattern Notation & the Four-Phase Editing Curve

Two extracts the rest of this skill now leans on: a **spec-grade notation** for stating reusable
microcopy patterns (Podmajersky's 11-pattern convention), and the **four-phase editing curve**
that takes a draft from raw to final (Podmajersky's "UX writing is 90% editing", with Ben-David's
"concise ≠ short" guard built in). Provenance: Torrey Podmajersky, *Strategic Writing for UX* 2nd
ed. (O'Reilly, 2025); Yael Ben-David, *The Fundamentals of UX Writing* (Apress, 2026). See the
boundary note at the foot — textual AI-slop detection is **not** this skill's job.

---

## 1. The `{}` / `[]` pattern notation (house format)

When you state a *reusable* string pattern — not a one-off final string, but the shape a button,
title, or label takes across many instances — write it in this notation so it is unambiguous and
ready to hand to a design system or a localisation team.

| Token | Means | Example slot |
|---|---|---|
| `{curly}` | **Variable / replaceable** — a slot filled at runtime with real data. | `{object}`, `{count}`, `{name}` |
| `[square]` | **Optional / omittable** — included only when context warrants; the pattern is valid without it. | `[object]`, `[ — {price}]` |
| plain text | **Literal** — appears verbatim, exactly as written. | `Delete`, `Save`, `Sign in with ` |

**Read it as:** literal text is fixed, `{curly}` is always present but its *value* changes, and
`[square]` may or may not appear at all.

### Worked patterns

| Pattern | Notation | Renders as |
|---|---|---|
| Primary action button | `{verb} [{object}]` | `Create project` · `Save` (object dropped when obvious) |
| Quantified destructive button | `Delete [{count} ]{object}` | `Delete file` · `Delete 3 files` |
| Confirmation title | `{verb} this {object}?` | `Delete this invoice?` |
| Field label | `{data-name}` | `Work email` |
| Pay CTA | `Pay {amount}` | `Pay $49` |
| OAuth button | `Sign in with {provider}` | `Sign in with Google` |
| Pending button | `{verb-ing}…` | `Sending…` |
| Inline success | `{object} {past-verb}[ to {target}]` | `Invite sent` · `Invite sent to amina@…` |

Rules for writing patterns:
- Put **only** runtime-variable text in `{}` — never wrap literal words you always show.
- Use `[]` for the genuinely optional (the object you drop when space is tight, the `to {target}`
  you append only when you have a target). If it is always there, it is literal, not `[]`.
- A pattern is a contract: every variant it can render must still obey verb+object, sentence case,
  and one-term-per-concept. The notation makes the contract *checkable*.

---

## 2. The four-phase editing curve (run them in order)

UX writing is mostly editing, and the editing is **sequential, not simultaneous**. Each phase has
one job; do them **in this order**, because a later phase assumes the earlier one is done. The
word count follows a deliberate **curve — it balloons in phase 1, then contracts** through 2–4.

> **Purposeful → Concise → Conversational → Clear** (in that order)

| # | Phase | The one question | What you do |
|---|---|---|---|
| 1 | **Purposeful** | *Does every string carry the messaging this moment needs?* | Get all the meaning in first — even if it is long and clumsy. Count expands here; do not trim yet. |
| 2 | **Concise** | *Does every word earn its real estate?* | Cut words that survive deletion without loss. **Concise ≠ short** — see §3. Count contracts. |
| 3 | **Conversational** | *Does it read like a human taking a turn?* | Make it sound like one side of a real exchange: contractions, second person, natural rhythm. **Conversational ≠ casual** — turn-taking, not buddy-register; stay on-voice. |
| 4 | **Clear** | *Will a first-time, stressed, or non-native reader get it in one pass?* | Final clarity check: plain words, front-loaded meaning, no ambiguity. Clarity outranks all earlier phases when they fight. |

**Always propose up to three ranked options** with a one-line rationale each, rather than a single
"right" answer — the curve produces variants, and ranking them surfaces the trade-offs for review.

---

## 3. "Concise ≠ short" and "cutting words ≠ removing messaging"

The phase-2 guard, because over-cutting is the most common way editing goes wrong.

- **Concise = everything the user needs and nothing more** — *every word earns its real estate.*
  It is not a synonym for *short*. A concise string can be longer than a terse one if the extra
  words carry needed meaning (the consequence, the reason, the irreversibility).
- **Cutting words ≠ removing messaging.** Deleting filler ("please", "simply", "in order to") is
  *concision* — same message, fewer words. Deleting a clause that carried information ("…and this
  can't be undone") is a *content decision*, not an editing one. Never let a word-count target
  silently strip messaging the moment needs.

| Over-cut (lost messaging) | Concise (kept messaging) |
|---|---|
| `Delete?` | `Delete this invoice? This can't be undone.` |
| `Saved` (when the user needs to know *what*) | `Draft saved` |
| `Sent` | `Invite sent to amina@…` |

Decide messaging first (phase 1), *then* tighten the words (phase 2). If a cut would remove
meaning, that is a phase-1 question to raise explicitly — not something to do under cover of "being
concise".

---

## 4. Title ↔ CTA continuity

A view's **action title and its primary button must agree** — same action, same verb, each making
sense read on its own. The title frames the action; the button commits it. If the title says one
thing and the button another, the user re-reads to reconcile them.

| Broken continuity | Continuous |
|---|---|
| Title `Delete this project?` · Button `OK` | Title `Delete this project?` · Button `Delete project` |
| Title `Invite a teammate` · Button `Submit` | Title `Invite a teammate` · Button `Send invite` |
| Title `Ready to publish?` · Button `Done` | Title `Publish this post?` · Button `Publish` |

Test: cover the title and read only the button — does it still name the action? Cover the button
and read only the title — same action? Both must pass. This pairs with verb+object
(`button-and-cta-copy.md` §1) and with the confirmation-dialog structure (`microcopy-patterns.md`
§4), where title = consequence and buttons = the two verbs.

---

## Boundary note (do not absorb)

- **Textual AI-slop detection is not this skill's job.** Spotting *generic machine-written prose*
  — the em-dash tell, "delve"-class diction, hedged transitions, list-of-three padding — lives in
  the **digital-research engine's writing-slop skills**, not here. This skill decides *what the
  product's words should be* and whether they are on-voice; the research engine decides whether a
  passage reads as machine-generated. Cross-reference; never duplicate.
- **Voice/tone routing.** This skill currently consumes the voice definition from
  `02-color-brand-and-visual-identity/brand-style-guide`. **Once
  `voice-tone-and-content-style-guide` ships in group 10**, route voice/tone definition there (the
  operational content voice/tone system for interface copy), and keep brand-style-guide for the
  visual+verbal brand identity. They reference each other; they do not duplicate.
