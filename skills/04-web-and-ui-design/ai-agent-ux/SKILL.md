---
name: ai-agent-ux
description: Use when an AI agent or copilot interface needs status, plans, approvals, uncertainty, interruption, or trust controls across web or mobile. Do not use for formatting a single AI answer; route output structure and citations to ai-output-design.
metadata:
  portable: true
  category: 04-web-and-ui-design
  compatible_with:
  - claude-code
  - codex
---

# AI Agent UX
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use When

- Design agentic UI patterns, approval moments, progress status, uncertainty handling, and explainability surfaces.
- Adapt agent UX for mobile and web workflows without exposing raw JSON or implementation detail.
- Shape user trust, control, recovery, and human handoff in AI agent experiences.

## Do Not Use When

- The work is not AI-specific or agentic-AI-specific.
- A narrower retained AI parent skill fits the request better.

## Required Inputs

| Input | Source | Evidence |
|---|---|---|
| User goal, agent powers, and prohibited actions | Product owner and capability policy | Enumerated actions and permission boundary |
| Agent lifecycle, failure modes, and latency | Engineering contract | State/event list and recovery paths |
| Human approval and audit requirements | Risk, legal, or operations owner | Approval thresholds and log requirements |

- Product, tenant, user, data, risk, and operational context relevant to the AI workflow.
- Target artifact: design, implementation plan, audit, test strategy, UX flow, commercial policy, or runbook.
- Constraints from security, privacy, reliability, billing, support, and compliance stakeholders when relevant.

## Workflow

1. Read this SKILL.md first.
2. Load `references/routing.md` to select the absorbed child reference that matches the task.
3. Load only the selected child reference files needed for the current request.
4. Produce execution-oriented output with assumptions, risks, evidence, and next actions where relevant.

## Decision Rules

| Condition | Choice | Wrong-choice failure |
|---|---|---|
| Action is consequential or irreversible | Preview plus explicit approval | Silent autonomy causes harm and destroys trust |
| Work is long-running | Persistent progress with pause/cancel | Spinner-only feedback looks stalled and removes control |
| Confidence is uncertain | Show evidence, limits, and next verification | Invented certainty misleads users |

## Capability Contract

- Must inspect capability and event contracts; review is read-only unless implementation is requested.
- May prototype or edit in-scope UI, but may not grant the agent new powers, execute consequential actions, or publish without explicit authority.

## Degraded Mode

- If powers or approval thresholds are unknown, stop the interaction specification and return the missing-policy questions.
- Without a runnable agent, produce a state/event prototype marked simulated. Recover failed states with retry, edit, cancel, or human escalation and retest the path.

## Quality Standards

- Keep routing explicit: name which reference files were used when the work depends on absorbed material.
- Preserve tenant isolation, auditability, cost controls, safety gates, and operational evidence when they matter.
- Prefer concrete contracts, checklists, tables, schemas, runbooks, and decision records over broad summaries.

## Anti-Patterns

- Loading every absorbed reference by default.
- Treating AI-specific billing, compliance, safety, or UX concerns as generic SaaS work without checking AI failure modes.
- Hiding retired skill names; old slugs must remain discoverable through `references/routing.md`.
- Hiding plans or actions behind a personality animation. Correction: expose task, state, evidence, and controls.
- Auto-executing a consequential step after ambiguous consent. Correction: preview scope and require explicit approval.
- Showing an endless spinner with no cancel path. Correction: persist progress, elapsed state, pause, and cancellation.

## Outputs

| Output | Consumer | Evidence and acceptance |
|---|---|---|
| Agent interaction specification | Product and engineering | State, approval, interruption, error, and recovery paths are explicit |
| Trust/control review | Risk and QA | Consequential actions have preview, consent, audit, and cancellation evidence |

- A concrete deliverable matched to the request: architecture, implementation plan, audit, policy, runbook, UX flow, test strategy, or operating model.
- The selected consolidated reference files and any assumptions, risks, evidence requirements, or follow-up actions that affect execution.
## References

- `doctrine/design-doctrine.md` — the anti-slop charter; agent UX must avoid "AI hammer looking for a nail" feature-cramming.
- `doctrine/references/ai-slop-taxonomy.md` — the product/interface slop tells (AI feature where search was faster; ungrounded output; "AI" badges as decoration) that agent surfaces must not exhibit.
- `ai-output-design` — sibling skill for the AI output surface (verifiability, grounding, forward-actions) these agent flows render into.
- `references/routing.md` maps retired child skill slugs to their consolidated reference folders.
- `references/generative-ai-ui-ux.md` covers generative-AI prompt, streaming, confidence, source, review, recovery, and human-override UI patterns.

## Consolidated Child References

- Load `references/routing.md` to map retired AI child skill slugs to their reference modules.

## Examples

- `examples/agent-ux-spec-worked.md` — a full worked agent-UX spec for a sample copilot ("Ledger"): status surface, approval/confirmation UX, uncertainty + confidence display, interruption/stop, error recovery, and the human-in-the-loop gates that tie them together. Use as a fill-in template.
<!-- dual-compat-end -->
