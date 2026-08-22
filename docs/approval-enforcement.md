# Approval enforcement adapter

Design-system actions are declared in [`approval-adapter.json`](approval-adapter.json)
and use the shared contract from `skills-web-dev/docs/approval-contract.md`.

## Checkpoint design

The approval checkpoint is itself a designed interaction. It must show what
the AI produced, what it proposes, what it will not do, target and scope,
risk, reviewer, evidence, correction, reject, edit, cancel, undo, escalation,
rollback, and expiry. Confirmation controls must be keyboard-accessible and
visible at mobile widths.

## Gated actions

Publishing live tokens, approving accessibility exceptions, releasing an agent
checkpoint, changing consent flows, or shipping a control that can cause a
side effect is L3. Accessibility exceptions, consent, financial actions, and
destructive controls require independent review where declared.

## Stop conditions

Missing rendered evidence, contrast, focus, state, recovery, asset provenance,
or reviewer identity is `NOT ASSESSED`, not PASS. Visual polish must never hide
an absent action state, review state, rejection path, or error recovery.

## Acceptance boundary

Design drafts may be generated. Live token changes and agent flows with
side-effect capability must pass the shared gate and the visual/accessibility
review before release.
