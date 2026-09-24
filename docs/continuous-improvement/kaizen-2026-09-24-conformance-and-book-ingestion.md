# Kaizen 2026-09-24 — conformance accuracy and book ingestion

Portfolio report: `chwezi-engine-agents/docs/operations/kaizen-2026-09-24-four-engine-kaizen.md`.

## What changed

- Carried-over change set completed: the old book-notes folder removed; four new skills
  (`fine-typesetting-and-typesetting-qa`, `print-production-and-finishing`, `art-direction-routes`,
  `advertising-creative-art-direction`) reviewed against the authoring standard and fixtured.
- The book-content guard in `scripts/validate_engine.py` now scans the whole repository (banned
  folders and file names, links, legacy note citations, chapter-numbered headings) with
  `tests/test_book_extraction_guard.py`.
- Conformance accuracy: APCA is a design aid, not "the WCAG 3 method"; WCAG 2.2 AA is the
  certification target; `prefers-reduced-motion` honoured as a house rule (SC 2.3.3 is AAA);
  working memory stated as about four chunks, not "7 ± 2".
- `governance/design-quality-gate.md` labels each item `HEURISTIC`, `MEASURED` or
  `NOT_ASSESSED`, adds a full state matrix, keyboard/screen-reader, motion, reflow and
  cross-engine handoff sections.
- New task references: action-cycle and discoverability audit, error prevention and recovery,
  low-literacy / low-bandwidth / emerging-market design, cultural adaptation, field research in
  low-resource settings, human-AI trust calibration, experiment-aware design evaluation, site
  planning and page types, modern CSS capability baseline, mobile-web patterns, style-era
  vocabulary, perceived performance for streaming and navigation, plus five UX references folded
  in from the engineering engine's retired book notes.

## Evidence

`validate_engine.py --baseline`: skills=101 fully_compliant=101. `routing_smoke_test.py`:
68 fixtures, p@1 85%, p@3 100%. Route existence and cross-engine routes: PASS. pytest: 99 passed.
Render, device and assistive-technology proof: NOT_ASSESSED.
