---
name: ai-output-design
description: Use when an AI answer surface needs structure, citations, grounding, editable refinement, or a chat-versus-canvas decision. Do not use for agent autonomy, approvals, or execution status; route those interaction controls to ai-agent-ux.
metadata:
  portable: true
  category: 04-web-and-ui-design
  compatible_with:
  - claude-code
  - codex
---

# AI Output Design
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Designing any AI output surface — chat bubbles, result panels, document drafts, canvas artifacts.
- The deliverable needs structure, verifiability, grounding, forward-actions, or inline refinement.

## Do Not Use When

- Designing the chrome around AI (loading, streaming, confidence states on input side) — use `ai-agent-ux` (its `ai-ux-patterns` reference module).
- Designing long-running agent control primitives — use `ai-agent-ux` (its `ai-agentic-ui` reference module).

## Required Inputs

| Input | Source | Evidence |
|---|---|---|
| User task and output decisions | Product brief or observed workflow | Ranked decisions and follow-up actions |
| Source/grounding payload | Retrieval or model contract | Citation identifiers and unavailable-evidence states |
| Output variability and error modes | Evaluation results or engineering | Representative good, weak, partial, and failed outputs |

- The output shape (prose, list, table, code, image, plan).
- The durability of the output: ephemeral (chat) or artifact (canvas).
- The source material the output will cite (if any).
- Available refinement controls and forward actions.

## Workflow

- Read this `SKILL.md` first, then load referenced deep-dives as needed.
- Apply the five principles in order; each failure mode maps to one principle.
- Decide canvas vs chat using the decision matrix.
- Draft the output template system prompt block.
- Specify source attribution, grounding metadata, forward actions, and inline refinement.

## Decision Rules

| Condition | Choice | Wrong-choice failure |
|---|---|---|
| Output supports ongoing editing | Persistent canvas with inline controls | Chat-only regeneration loses context and user changes |
| Claim can be sourced | Citation adjacent to the claim | Detached source lists make verification costly |
| Evidence is absent or conflicting | State the gap and verification action | Confidence percentages manufacture trust without proof |

## Capability Contract

- Must inspect representative outputs and grounding metadata; evaluation is read-only unless implementation is requested.
- May edit in-scope templates/components but must not fabricate sources, alter underlying evidence, or publish generated content without authority.

## Degraded Mode

- Without grounding metadata, label claims unverified and stop any verifiability sign-off.
- Without rendering, return the output schema and state matrix. Recover malformed or partial output with preserved user work, retry/edit controls, and a tested fallback.

## Quality Standards

- No confidence-percentage UI on LLM outputs. Ever.
- Every factual claim carries an inline source.
- Every output surface has 2–4 forward-action affordances.
- Refinement is inline; user never re-prompts from scratch.

## Anti-Patterns

- Confidence badges on LLM outputs (false authority).
- Unstructured wall of prose.
- Sources dumped at the bottom with no inline anchoring.
- Chat used for durable artifacts; canvas used for ephemeral chat.
- Requiring full regeneration for a local change. Correction: provide inline adjustment that preserves accepted work.

## Outputs

| Output | Consumer | Evidence and acceptance |
|---|---|---|
| AI output template and state matrix | Design and engineering | Clear, verifiable, grounded, actionable, adjustable states are mapped |
| Output quality review | Product and QA | Representative outputs show source proximity, failure handling, and forward actions |

- Output-template system prompt block.
- Source-attribution component spec.
- Grounding metadata component spec.
- Forward-action affordance list.
- Inline-refinement menu spec.
- Canvas-vs-chat decision for each AI feature.

## References

- `doctrine/design-doctrine.md` — the anti-slop charter; ungrounded, unverifiable, dead-end AI output is product slop.
- `doctrine/references/ai-slop-taxonomy.md` — the product/interface slop tells (output surfaced without verifiability, grounding, or an undo/adjust affordance) the five principles fix.
- `references/five-output-principles.md` — expanded treatment with UI mechanics.
- `references/verifiability-patterns.md` — why confidence % is wrong; inline-source patterns.
- `references/canvas-vs-chat.md` — decision matrix, versioning, collaboration.
- `references/inline-refinement.md` — on-select UI, buttons, knobs, version selectors.
## AI-assisted design workflow guard

When AI accelerates design or product artefact work, preserve source context,
ask for questions and options before generation, record decisions, manually
verify external/product facts, prototype early, and apply scoped delta changes
with human review after each material iteration. AI accelerates execution; it
does not own product judgement, prioritisation, competitor verification,
accessibility sign-off, or release approval.

Anti-patterns: an unverified context dump becoming source truth, or broad
regeneration that changes accepted work. Fix both with a source comparison,
decision log, numbered delta, and post-change diff check.

Practitioner cross-check: [Eleken AI design workflow](https://www.eleken.co/blog-posts/ai-design-workflow). Use its workflow controls only; exclude time-saved figures and tool claims.

<!-- dual-compat-end -->

## Why AI Outputs Fail

Most AI output surfaces fail for one of five reasons:

- Unstructured slab of prose — **Clear fail**.
- No way to verify claims — **Verifiable fail**.
- User can't tell what context the AI used — **Grounded fail**.
- Reading ends with a dead end — **Actionable fail**.
- Any refinement requires re-prompting from scratch — **Adjustable fail**.

The five principles below map to fixes for each.

---

## Principle 1 — Clear

Every output has a structure template in the system prompt. Enforce structure but use the **leanest template that works**; over-styling suppresses flexibility.

**Baseline template:**

```
Title -> Intro (1-2 sentences) -> Key Concepts -> Steps (if procedural) -> Notes (caveats) -> Sources
```

UI side: render the template as collapsible sections when long; preserve the sections on copy/export.

---

## Principle 2 — Verifiable

**REJECT confidence-percentage UI for LLMs.** LLMs are bad at self-confidence; internal token probabilities do not map to truth. A "87% confident" badge on a hallucinated answer is worse than no badge — it confers false authority.

**Instead: inline sources per claim.** Perplexity superscript pattern. Each claim links to a specific passage in a source. Multiple claims without sources is a structural smell.

**Exceptions where a confidence number IS OK:**

- Calibrated non-LLM models (a CV model that reports softmax).
- RAG retrieval score (distinct from LLM self-assessment).
- A/B test predictions with real backtests.

See `references/verifiability-patterns.md`.

---

## Principle 3 — Grounded

Users trust an output when they know **the lens the model used**. Surface:

- Model + version ("Codex Sonnet 4.6").
- Agent / tool used ("Used Web Search").
- Locale / jurisdiction ("Answer framed for UK law").
- Mode ("Fast mode vs Thinking mode").
- Session history ("Based on 3 earlier docs in this chat").

Implement as a "Why we suggested this" affordance — one click expands the grounding metadata.

---

## Principle 4 — Actionable (Forward Verbs)

The output is not the goal; the action after the output is. Design the onward journey. Every output surface should expose obvious forward affordances:

- Save / Export.
- Buy / Book / Register.
- Cite / Quote.
- Navigate to related.
- Refine (see Adjustable).

Rule: a response that ends "…and that's it" without an action button is a design failure. Default to 2–4 forward affordances even for pure Q&A (copy, save, share, refine).

---

## Principle 5 — Adjustable (Inline Refinement Beats Re-prompt)

- **On-select UI** (Notion pattern): user highlights text → inline menu: "Shorter / Longer / Simpler / Formal / Translate". Runs a scoped prompt on just the selection. The user does not type a new prompt.
- **Prompt augmentation** (Elaborate button): user clicks "Elaborate" → system appends a directive to the last prompt and re-runs. Avoids re-prompt-from-scratch.
- **Knobs** (QuillBot Fluency/Formal sliders): exposed as persistent controls above the output. Changing them regenerates.
- **Version selector** (Codex Artifacts pattern): every regeneration is a versioned sibling, not a destructive overwrite. Users compare and pick.

See `references/inline-refinement.md`.

---

## Canvas vs Chat Selection

Two distinct output paradigms.

| Paradigm | When to use | Prescriptions |
|---|---|---|
| Chat | Ephemeral Q&A, conversational iteration, short outputs | Linear transcript, streaming tokens, recent history visible |
| Canvas | Output is durable artifact (doc, plan, image, code) — shareable, storable, returnable | Editable workspace, version history (Codex Artifacts), undo/redo, node-based iteration for generative media (Runway) |

Rule: move output to canvas the moment it becomes shareable. A 3-page policy draft in chat is friction; the same draft in canvas is a deliverable.

See `references/canvas-vs-chat.md`.

---

## Starter Prompts as Positioning

Starter prompts are not examples — they are product positioning. Generic starters ("Write a poem about autumn") are lazy. Good starters reflect the product's specific integrations, tone, and differentiators. Make them **context-aware**: Monday-morning vs Friday-afternoon, document-type-open-in-editor, user-plan-tier.

---

## Output Template System Prompt Snippet (Drop-in)

```
Structure every response as:
1. One-sentence title
2. 1-2 sentence introduction
3. Key concepts as a bulleted list if appropriate
4. Step-by-step instructions if procedural
5. Notes section for caveats, limits, or edge cases
6. Sources section with inline citations
If a section has no content, omit it.
```

---

## Anti-Patterns

- Confidence-percentage badges on LLM outputs (false authority).
- Unstructured wall of prose with no headings.
- Sources listed at the bottom with no inline anchoring.
- Output ends with no next-action affordance.
- Refinement requires user to re-type the prompt.
- Over-styled template so rigid that edge cases render badly.
- Canvas used for ephemeral chat or chat used for durable artifacts.

---

**See also:**

- `ai-agent-ux` — sibling skill covering streaming/loading/feedback patterns (`ai-ux-patterns` module), long-running agent surfaces (`ai-agentic-ui` module), and AI trust/transparency principles.
- `doctrine/references/ai-slop-taxonomy.md` — product/interface slop tells for AI surfaces.
## Examples

- [examples/ai-output-surface-worked.md](examples/ai-output-surface-worked.md) — a full worked AI output-surface spec (a "Lease Clause Explainer" feature) running through all five principles, canvas-vs-chat, and the anti-hallucination affordances.

For high-consequence outputs with mixed evidence or changing information, load
[uncertainty and evidence message design](references/uncertainty-and-evidence-message-design.md).

## Consolidated Child References

- Load [references/routing.md](references/routing.md) to map retired AI child skill slugs to their reference modules.
