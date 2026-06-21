# Worked Example — AI Output Surface Spec

**Feature:** "Lease Clause Explainer" inside a commercial-property SaaS. A tenant or broker
pastes a clause from a lease (or selects one already parsed in the document panel) and asks
what it means, whether it is standard, and what to do next. The answer must be trustworthy
enough to act on without a lawyer in the loop for routine clauses.

This walks the feature through all five output principles, the canvas-vs-chat decision, and
the anti-hallucination affordances — concrete enough to hand to a frontend engineer and a
prompt author.

---

## 0. Inputs (filled in)

| Required input | Value for this feature |
|---|---|
| Output shape | Structured prose + a short comparison table + a forward-action row |
| Durability | **Ephemeral by default (chat-style answer)**, promotable to canvas when the user saves the explanation to the deal file |
| Source material | The lease document itself (paragraph-anchored), plus a curated clause-library of "market-standard" reference clauses with jurisdiction tags |
| Refinement controls | Reading level (Plain / Legal), length (Brief / Full), jurisdiction toggle |
| Forward actions | Save to deal file, Flag for lawyer, Compare to market-standard, Copy with sources |

---

## 1. Clear — output structure / template

The answer renders into fixed, collapsible sections. The leanest template that carries the
job — no "Executive Summary / Introduction / Conclusion" bloat.

```
Verdict          one line: what this clause does, in plain language
Standard?        Market-standard | Above-market | Unusual — one phrase why
What it means    2-4 bullets, each anchored to a clause span [L]
Watch-outs       caveats / triggers (rent review dates, break conditions). Omit if none.
Compare          mini-table vs market-standard clause (only when "Compare" is invoked)
Sources          the exact lease paragraph(s) + clause-library entry used
```

Rendering rules:
- Sections render in a card; `What it means` and `Watch-outs` are collapsible once the answer
  exceeds ~8 lines.
- Section order is preserved on copy/export so a pasted answer is still legible.
- Empty sections are omitted, not shown as "N/A".

**Drop-in system-prompt block:**

```
Answer about the selected lease clause using exactly these sections, omitting any that are empty:
1. Verdict — one sentence, plain English, no legalese.
2. Standard? — one of {Market-standard, Above-market, Unusual} plus a half-sentence reason.
3. What it means — 2 to 4 bullets. Each bullet MUST end with a span marker [Ln] pointing at
   the lease text it is grounded in. Do not write a bullet you cannot anchor.
4. Watch-outs — dates, triggers, or conditions the reader must track. Omit if there are none.
5. Sources — list each [Ln] span and any clause-library entry id you relied on.
Never state a legal conclusion that is not supported by a cited span. If the clause is
ambiguous or you lack the surrounding context, say so in Verdict and recommend "Flag for lawyer".
```

---

## 2. Verifiable — citations / sources (NOT confidence %)

No "92% confident" badge. Confidence percentages on an LLM legal reading are exactly the false
authority the principle forbids.

Instead, **every bullet in `What it means` carries an inline span marker** that scroll-links to
the highlighted text in the document panel:

```
• The landlord may review rent every 5 years, upward-only. [L12]
                                                            └─ click → scrolls the lease
                                                               panel to ¶12 and highlights it
```

- `[L12]` is a superscript-style chip (Perplexity pattern): hover shows the quoted lease text;
  click scrolls + highlights the source paragraph in the side panel.
- The `Standard?` verdict cites a **clause-library entry** (`CL-RENT-UPWARD-ONLY`, jurisdiction
  `England & Wales`) — a retrieval match, not the model's self-assessment.
- A `Compare` table cell that has no matching library clause shows "No market reference" rather
  than inventing one.

Where a real number is legitimate, it is a **retrieval score, not LLM confidence**: the
clause-library match can surface "closest market clause (similarity 0.84)" because that comes
from the vector store, not the model judging itself.

---

## 3. Grounded — what lens did the model use

A single "Why this answer" affordance expands the grounding metadata:

```
Why this answer
  Model        Codex Sonnet 4.6
  Read from    This lease (12 paragraphs) + clause-library
  Jurisdiction England & Wales  [change ▾]
  Reading      Plain English  ·  Full length
  Tools used   Document parser, Clause-library search
```

- The **jurisdiction chip is live** — changing it re-grounds the "Standard?" verdict against a
  different reference set, because "market-standard" is jurisdiction-specific.
- "Read from" makes the context window explicit: the user sees the model did NOT pull in the
  whole portfolio, only this lease — bounding what the answer can and cannot know.

---

## 4. Actionable — forward verbs

The answer never dead-ends. A persistent action row sits under the card (2–4 affordances, here 4):

```
[ Save to deal file ]  [ Flag for lawyer ]  [ Compare to market-standard ]  [ Copy with sources ]
```

- **Save to deal file** — promotes the ephemeral answer into a stored artifact (see §6, canvas).
- **Flag for lawyer** — routes the clause + explanation into the review queue; the primary
  "escape hatch" forward-action for anything the model itself marked ambiguous.
- **Compare to market-standard** — triggers the `Compare` table section inline.
- **Copy with sources** — copies the structured text *with* the `[Ln]` spans resolved to quoted
  lease text, so the answer stays verifiable outside the app.

---

## 5. Adjustable — inline refinement / regenerate

No re-prompting from scratch. Three adjustment surfaces:

- **Knobs (persistent, above the answer):** `Reading: Plain ⇄ Legal` and `Length: Brief ⇄ Full`.
  Flipping a knob regenerates the same answer at the new setting; the scope (this clause) is
  unchanged, so the user never restates the question.
- **On-select menu:** highlighting any sentence in `What it means` opens
  `Simpler · Define this term · Show the exact lease text`. "Define this term" runs a scoped
  sub-prompt on the selection only.
- **Version selector:** every regeneration is a versioned sibling, not an overwrite.
  `v3 ▾` lets the user compare the Plain vs Legal reading side by side and keep the one they
  paste into the deal file. Switching jurisdiction also produces a new sibling version, so the
  "England & Wales" and "Scotland" readings coexist for comparison.

---

## 6. Canvas vs Chat

| Stage | Paradigm | Why |
|---|---|---|
| Asking + iterating on one clause | **Chat** | Ephemeral, conversational, short; user is exploring |
| "Save to deal file" pressed | **Canvas** | Now a durable, shareable artifact attached to the deal; needs version history, undo, and is returned to by colleagues |

The rule applied: the explanation lives in chat while it is being shaped, and moves to canvas
the moment it becomes shareable (saved to the deal file other team members open).

---

## 7. Anti-hallucination affordances (the load-bearing part)

This feature gives legal-adjacent answers, so the affordances that *prevent acting on a
fabrication* are first-class, not decoration:

1. **No unanchored claims.** The template forbids a `What it means` bullet without a `[Ln]`
   span. A bullet the model cannot ground is a structural error, not a stylistic one — the
   renderer surfaces any unanchored bullet with a "source missing" warning chip rather than
   showing it as fact.
2. **Retrieval-gated "Standard?" verdict.** The market-standard judgement must cite a
   clause-library entry. If retrieval returns nothing above the similarity threshold, the verdict
   renders as **"No market reference found"** and the model is instructed not to guess.
3. **Abstain path is built in.** The system prompt requires the model to say so when the clause
   is ambiguous or depends on un-provided context, and to recommend **Flag for lawyer** — which
   is a real button, so abstention has somewhere to go.
4. **Span hover = ground truth.** Because every `[Ln]` chip reveals the *verbatim* lease text on
   hover, the user can catch a misparaphrase in one second without leaving the answer.
5. **Jurisdiction is never assumed silently.** The grounding panel always shows the jurisdiction
   used; a mismatch is visible before the user acts, not buried.
6. **Copy preserves sources.** "Copy with sources" prevents the most common downstream
   hallucination-laundering failure — a confident-looking paragraph pasted into an email with
   its citations stripped.

Together these mean: the surface makes it *harder to act on an ungrounded claim than on a
grounded one* — which is the whole point of the five principles applied to a high-stakes output.
