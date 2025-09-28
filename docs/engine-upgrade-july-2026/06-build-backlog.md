# Concrete Build Backlog

| # | Filename/path | Purpose | Acceptance criteria | Effort |
| --- | --- | --- | --- | --- |
| 1 | tools/render-regression/README.md | Define render regression workflow for generated artefacts. | Can render and compare examples for DOCX/PDF/deck/web/mobile surfaces. | L |
| 2 | examples/before-after/ | Create before/after examples for typography, colour, layout, UI, data viz, and documents. | Each example includes diagnosis, changed tokens, screenshots/exports, and score delta. | L |
| 3 | packages/design-tokens/ | Publish sample tokens in JSON, CSS variables, Tailwind, React Native, Flutter, and DOCX theme mappings. | Tokens validate against schema and render in at least 3 target surfaces. | L |
| 4 | docs/flutter-depth-ceiling.md | Clarify when this engine stops and Flutter implementation skills begin. | Routing examples cover UI concept, tokens, widgets, animation, accessibility, and build verification. | S |
| 5 | scripts/check-consumer-style-contract.py | Validate consumer reports against typography and anti-slop rules. | Fails on banned primary fonts, missing type rationale, or unstructured visual handoff. | M |
