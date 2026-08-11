# Design-System Skills — Kaizen Wave 1 Report

Assessment date: 2026-08-11
Repository: `C:\wamp64\www\design-system-skills`
Owner: design-system-skills maintainer
Wave: 1
Scope: bounded P0 route/count repairs, dated design standards register, and one P1 delivery-evidence contract

## Verdict

Wave 1 is implemented and locally green for the changed scope. The repository is not a production
rendering pipeline and does not claim PPTX, DOCX, or PDF generation, reopenability, visual fidelity,
or accessibility conformance. The tracked design-delivery fixture is deliberately `CONDITIONAL`:
generation, reopen, render, visual QA, and accessibility are separate states and each is
`NOT ASSESSED` because the required native or target-application evidence was not available.

The exercise score remains a capped report value, not an achievement claim:

```text
baseline raw score = 59.1/100
exercise published baseline = min(59.1, 55) = 55/100
Wave 1 re-score = NOT ASSESSED as a complete re-audit
target = 95/100, not awarded without outcome evidence
```

The baseline raw score, maturity, and exercise cap are taken from
`C:\wamp64\www\KAIZEN-INITIAL-ASSESSMENT.md` (the `design-system-skills` row and exercise
scoring sections). The repository's permanent 65-point portfolio cap was not changed.

## Evidence index

| ID | Evidence | Result |
|---|---|---|
| E0 | Pre-edit local-route heuristic over active skill material | 23 missing-reference candidates; 21 local repairs were in scope and 2 were cross-engine references |
| E1 | Baseline `git status --short --branch` | `## main...origin/main`; no pre-edit changes were present |
| E2 | Baseline `python -X utf8 scripts/validate_engine.py --baseline tests/quality-baseline.json` | `skills=88 fully_compliant=88`; exit 0 |
| E3 | Baseline `python -X utf8 scripts/routing_smoke_test.py` | 54 fixtures, 87% top-one precision, 100% top-three precision; exit 0 |
| E4 | Baseline delivery validator and `pytest tests/test_design_delivery_evidence.py` | validator findings 0; 2 tests passed; both exit 0 |
| E5 | Final repository gates listed below | all exit 0; 5 tests passed |
| E6 | Final local route heuristic | 2 unresolved cross-engine references remain outside this repository's local route tree |
| E7 | Final bounded safety scan and required skill readback | no newly introduced remote execution, credential collection, or exfiltration instruction; repository-native source-ingestion guardrail unavailable |

## Baseline inventory and maturity

The pre-edit filesystem contained 88 active `SKILL.md` files plus the `_TEMPLATE` skill, across
16 group directories. The local zero-debt baseline contained 88 fully compliant skills. The
repository had 54 routing fixtures with 87% top-one and 100% top-three precision. The delivery
evidence validator returned zero findings and the baseline delivery test file passed 2 tests
([E2], [E3], [E4]; the filesystem count is independently rechecked by the final validator in
[E5]).

The diagnostic raw score was 59.1/100 and the maturity assessment was L3 — defined standards and
automated checks, with important visual and production proof still missing
(`C:\wamp64\www\KAIZEN-INITIAL-ASSESSMENT.md`, `design-system-skills` row). The main baseline
defects were:

- current entrypoints stated 82, 87, and 88 at different points;
- active documentation contained local references to the old group 04 for routes now owned by
  group 14, plus missing email and ethics example filenames;
- named standards did not have one design-engine register with source URL, applicability, owner,
  observed date, and review date; and
- the delivery manifest checked render-file presence and a combined check list, but did not keep
  generation, reopen, render, visual QA, and accessibility as separate lifecycle states.

No pre-edit user changes were observed ([E1]). No sibling repository was written.

## Files changed

### Counts, routes, and release wiring

- `AGENTS.md`
- `README.md`
- `docs/RESUME.md`
- `.github/workflows/skill-engine-quality.yml`
- `scripts/validate_route_existence.py`
- `tests/route-existence-fixtures.yml`
- `tests/test_route_existence.py`
- `skills/00-cross-cutting-ops-qa-a11y/design-ethics-and-anti-dark-patterns/SKILL.md`
- `skills/02-color-brand-and-visual-identity/brand-visual-identity/examples/identity-mini-guide.md`
- `skills/02-color-brand-and-visual-identity/brand-visual-identity/references/brand-consistency-gate.md`
- `skills/02-color-brand-and-visual-identity/brand-visual-identity/references/identity-system-spec.md`
- `skills/04-web-and-ui-design/component-states-and-interaction-fidelity/SKILL.md`
- `skills/06-sector-and-domain-ux/ecommerce-and-checkout-ux/SKILL.md`
- `skills/06-sector-and-domain-ux/ecommerce-and-checkout-ux/references/checkout-flow-patterns.md`
- `skills/10-content-design-and-ux-writing/ux-writing-and-microcopy/SKILL.md`
- `skills/10-content-design-and-ux-writing/ux-writing-and-microcopy/references/button-and-cta-copy.md`
- `skills/13-presentations-and-documents/email-and-newsletter-design/SKILL.md`
- `skills/14-conversion-and-web-page-patterns/navigation-and-information-architecture/SKILL.md`
- `skills/14-conversion-and-web-page-patterns/navigation-and-information-architecture/examples/sitemap-and-nav-spec.md`
- `skills/14-conversion-and-web-page-patterns/navigation-and-information-architecture/references/ia-patterns.md`
- `skills/14-conversion-and-web-page-patterns/onboarding-and-first-run-design/SKILL.md`
- `skills/14-conversion-and-web-page-patterns/onboarding-and-first-run-design/examples/first-run-flow-for-a-team-todo-app.md`
- `skills/14-conversion-and-web-page-patterns/onboarding-and-first-run-design/references/onboarding-patterns.md`

### Standards and delivery evidence

- `governance/standards-source-register.md`
- `scripts/validate_design_delivery_evidence.py`
- `templates/design-delivery-evidence.md`
- `tests/fixtures/design-delivery/manifest.json`
- `tests/test_design_delivery_evidence.py`

### Report

- `docs/continuous-improvement/kaizen-wave-1-2026-08-11.md`

## Improvement register

### P0-DS-01 — filesystem-truth counts and local routes

- **Gap:** The filesystem had 88 active skills, while current entrypoints still mixed 82, 87,
  and 88. A pre-edit local-route heuristic reported 23 missing-reference candidates in active
  skill material; 21 were local route or example defects and 2 were cross-engine references
  ([E0], [E2], [E6]).
- **Root cause:** Counts were repeated manually, and taxonomy/example relocations were not
  protected by a route-existence fixture. The old group 04 references and stale example names
  therefore survived structural conformance checks.
- **Exact change:** Updated current count statements in `AGENTS.md`, `README.md`, and
  `docs/RESUME.md`; repaired local group 04/group 14, group 06/group 00, group 02/group 04,
  relative typography, email-example, ethics-example, and split-reference paths; added
  `tests/route-existence-fixtures.yml`, `scripts/validate_route_existence.py`, and
  `tests/test_route_existence.py`; added the route validator to the GitHub Actions workflow.
- **Hypothesis:** If current entrypoints state the filesystem count and repaired routes are
  checked against real files, a fresh agent will receive fewer dead dispatches and taxonomy
  references will fail visibly when a later relocation breaks them.
- **Owner:** Design-system engine maintainer.
- **Measure:** Final filesystem validator reports 88 skills and 88 fully compliant; routing
  remains 54 fixtures at 87% top-one and 100% top-three; the new route validator reports 0
  findings ([E5]). The repaired-pattern scan reports no remaining matches. The broader heuristic
  retains 2 cross-engine references, which are recorded rather than falsely marked resolved
  ([E6]).
- **Risk:** A route rename can improve local truth while breaking a consumer that still uses an
  old path. The route fixture may also cover only known high-risk references, not every prose link.
- **Rollback:** Revert the route-text edits and the route validator/fixture as one reviewed patch;
  retain the filesystem-derived count wording if the route experiment is rolled back.
- **Acceptance evidence:** `validate_engine.py`, `routing_smoke_test.py`,
  `validate_route_existence.py`, the route pytest, and the final diff check all exit 0 ([E5]).
- **Standardisation:** The route fixture and CI command are now the discoverable release gate;
  `README.md` and `AGENTS.md` tell maintainers that the filesystem is the count source.
- **Re-audit:** 2026-08-18, with the Wave 1 repository gate; cross-engine references should be
  checked with their owning engine before closure.

### P0-DS-02 — dated primary-source standards register

- **Gap:** Design skills named WCAG, Microsoft Office accessibility guidance, and ISO PDF/UI
  references, but the repository had no consistent local register containing source URL,
  applicability limit, owner, observed date, and next review.
- **Root cause:** Standards provenance lived in distributed references and the workspace-level
  register without a design-engine applicability index.
- **Exact change:** Added [`governance/standards-source-register.md`](../../governance/standards-source-register.md) with 5 design-specific rows
  derived from the primary URLs and metadata in `C:\wamp64\www\KAIZEN-STANDARDS-SOURCE-REGISTER.md`.
  The register explicitly says that a URL does not prove artefact conformance and preserves the
  2026-11-11 review date recorded by the workspace register.
- **Hypothesis:** If current design claims have one dated, owned source index, maintainers can
  identify what to review without treating a named standard or live URL as conformance proof.
- **Owner:** Design-system engine maintainer, with the relevant accessibility, presentation,
  document, PDF, or UI owner for each row.
- **Measure:** [`tests/test_route_existence.py`](../../tests/test_route_existence.py) checks that all 5 register rows retain an HTTPS
  primary URL, an applicability/review field, and the registered review date. It does not test
  URL liveness or semantic claim support ([E5]).
- **Risk:** A register can become stale or become ceremony detached from changed skills. The
  applicability text also cannot determine jurisdiction-specific legal requirements.
- **Rollback:** Remove the local index only if the workspace register gains an equivalent,
  maintained design view; otherwise keep the file and mark overdue rows visibly.
- **Acceptance evidence:** Register field test passes; no live-source or semantic-support claim
  is made by the validator ([E5]).
- **Standardisation:** Each externally mutable design claim should point to a register row and
  review date. Changes follow the workspace register's source-change protocol.
- **Re-audit:** 2026-08-18 for integration with changed routes; scheduled currency review
  2026-11-11.

### P1-DS-01 — separate delivery-evidence lifecycle states

- **Gap:** The prior manifest could validate a tracked render path and a combined check list, but
  it did not distinguish generation, reopen, render, visual QA, and accessibility evidence. That
  left a structural pass vulnerable to being read as output proof ([E4]).
- **Root cause:** The validator schema had `renders` and `checks` but no required lifecycle-stage
  object and no rule forbidding `PASS` when a required stage was unassessed.
- **Exact change:** Extended `scripts/validate_design_delivery_evidence.py` with required
  `stages` for generation, reopen, render, visual QA, and accessibility; required a result and
  evidence/unavailable reason for every stage; and forbade a `PASS` verdict when any required
  stage is `FAIL` or `NOT ASSESSED`. Updated the tracked SVG fixture to `CONDITIONAL` with all
  5 lifecycle stages explicitly `NOT ASSESSED`; updated
  `templates/design-delivery-evidence.md`, the two original tests, and added a pass-with-unassessed
  regression test.
- **Hypothesis:** If each lifecycle stage has its own state and evidence field, missing native
  application or render tooling will remain visible instead of being converted into a false
  delivery pass.
- **Owner:** Design-system engine maintainer and the accountable artefact reviewer for each real
  delivery.
- **Measure:** Final validator returns 0 findings for the conditional fixture; pytest passes 5
  tests; the regression test proves a `PASS` verdict cannot hide an unassessed required stage
  ([E5]).
- **Risk:** Consumers may read `CONDITIONAL` as approval. Requiring stages may also break older
  manifests until they are migrated.
- **Rollback:** Restore the previous validator, fixture, and tests together if downstream schema
  compatibility is demonstrated to be more valuable than the false-pass protection; do not
  restore a `PASS` fixture without the missing evidence.
- **Acceptance evidence:** `validate_design_delivery_evidence.py` exits 0 on the conditional
  fixture; the missing-render and pass-with-unassessed tests both exercise refusal paths; no
  PPTX, DOCX, or PDF binary was created ([E5]).
- **Standardisation:** The manifest schema and the Markdown template now teach the five-stage
  evidence contract. `NOT ASSESSED` is the required state when a check cannot be run.
- **Re-audit:** 2026-08-25 for the independent Wave 2 artefact-evidence review.

## Before/after measures

| Measure | Before | After | Evidence and interpretation |
|---|---:|---:|---|
| Active skills | 88 | 88 | No catalogue growth; final validator derives the count ([E2], [E5]) |
| Contract-compliant skills | 88/88 | 88/88 | No structural regression ([E2], [E5]) |
| Routing fixtures | 54 | 54 | Existing fixture set preserved ([E3], [E5]) |
| Routing precision | 87% top-one; 100% top-three | 87% top-one; 100% top-three | No routing-score regression ([E3], [E5]) |
| Explicit repaired-route fixtures | 0 | 7 | [`tests/route-existence-fixtures.yml`](../../tests/route-existence-fixtures.yml) targets all selected local route/example repairs; validator findings 0 |
| Delivery lifecycle states | Combined checks only | 5 separate required stages | All fixture stages are `NOT ASSESSED`; this is evidence of honest availability, not output conformance |
| Delivery verdict | Existing fixture `PASS` | `CONDITIONAL` | A pass is forbidden when a required stage is unassessed |
| Standards source register | No consistent local design index | 5 dated primary-source rows | Field presence is tested; liveness and semantic support are not assessed |

The unchanged routing precision is intentional. The patch repairs dead references and adds
existence proof; it does not claim that lexical top-one routing improved.

## Tests and validation

### Baseline commands and results

```text
python -X utf8 scripts/validate_engine.py --baseline tests/quality-baseline.json
skills=88 fully_compliant=88
exit=0

python -X utf8 scripts/routing_smoke_test.py
routing fixtures=54 precision@1=87% precision@3=100%
exit=0

python -X utf8 scripts/validate_design_delivery_evidence.py tests/fixtures/design-delivery/manifest.json
findings: 0
PASS: design delivery evidence is complete
exit=0

python -m pytest -q tests/test_design_delivery_evidence.py
2 passed
exit=0
```

These results are the pre-edit records in [E2], [E3], and [E4].

### Final commands and results

```text
python -X utf8 scripts/validate_engine.py --baseline tests/quality-baseline.json
skills=88 fully_compliant=88
exit=0

python -X utf8 scripts/routing_smoke_test.py
routing fixtures=54 precision@1=87% precision@3=100%
exit=0

python -X utf8 scripts/validate_route_existence.py
findings: 0
PASS: route targets exist and repaired references are present
exit=0

python -X utf8 scripts/validate_design_delivery_evidence.py tests/fixtures/design-delivery/manifest.json
- delivery verdict: CONDITIONAL
- stages: accessibility=NOT ASSESSED, generation=NOT ASSESSED, render=NOT ASSESSED, reopen=NOT ASSESSED, visual_qa=NOT ASSESSED
findings: 0
PASS: manifest structure is valid; delivery verdict is reported above
exit=0

python -m pytest -q
5 passed
exit=0

git diff --check
exit=0
```

The final combined exit summary was:

```text
validate_engine=0 routing_smoke=0 route_existence=0 evidence=0 pytest=0 diff_check=0
```

### Skill authoring and safety review

The 7 changed `SKILL.md` files were read back in full. The external skill-writing quick validator
reported `Skill is valid.` for each; the contract gate reported 0 errors and 0 warnings for each
invocation. The repository has no `skill_catalog_guardrails.py` or equivalent source-ingestion
script, so that repository-native check is `NOT ASSESSED`, not a pass. A bounded static scan of
changed surfaces found only ordinary domain words and the pre-existing approved `pip install
PyYAML` workflow dependency; it found no newly added remote script execution, secret collection,
or exfiltration instruction ([E7]).

Safety status: **Needs Review** for the unavailable repository-native source-ingestion guardrail;
no unsafe finding was observed in the changed skill/reference content. A future safety review
should run the canonical guardrail if it is restored or supplied by the owning engine.

## Evidence classification and unavailable checks

| Evidence type | Result |
|---|---|
| Structural | **ASSESSED:** 88/88 contract validator, fixture schema, route target existence, diff check |
| Behavioural | **PARTIALLY ASSESSED:** deterministic refusal tests cover missing renders and an unassessed-stage false pass; no user journey is exercised |
| Render | **NOT ASSESSED:** no PPTX/DOCX/PDF generation or target render command was available |
| System/platform | **NOT ASSESSED:** no native Office reopen, Word Accessibility Assistant, PDF/UA tool, or cross-client visual matrix was executed |
| Production | **NOT ASSESSED:** no client delivery, field usage, deployment, or stakeholder review evidence was supplied |
| Standards liveness | **NOT ASSESSED:** the local register preserves workspace-provided primary URLs and dates; no live URL or semantic claim-support run was performed |
| Cross-engine routing | **NOT ASSESSED:** two enterprise UX references point outside this repository; one target path was found in `srs-skills`, while the premium-software path had no source found in the inspected sibling tree. No sibling was modified |
| Universal source-ingestion guardrail | **NOT ASSESSED:** no repository-native guardrail was present |

## Remaining backlog

### P0

- Close the two unresolved cross-engine references through the owning engine rather than inventing
  a local alias. The missing premium-software route is a gap: no source found in the inspected
  `srs-skills` tree.
- Keep count and route gates in the release workflow as group taxonomy evolves.

### P1

- Produce one fictional/test-labelled editable PPTX, DOCX, and PDF fixture only when the required
  generation tools and target applications are available. Record generation, reopen, render,
  visual QA, and accessibility independently; do not promote `NOT ASSESSED` to `PASS`.
- Add format-specific reopen/render checks and a retained page/slide inspection record. This
  report does not claim those checks exist.
- Review the semantics of each registered standard against the affected claim. The current
  register proves provenance fields, not conformance or claim support.

### P2

- Run the first scheduled source-currency review on 2026-11-11 and update only claims whose
  authoritative source changed.
- Add a small cross-model discovery smoke matrix for `AGENTS.md`, `CLAUDE.md`, canonical
  `SKILL.md`, and a generic manual route; current vendor auto-loading behaviour is not assessed.
- Revisit the two remaining cross-engine route owners after their catalogues change.

## Claude, Codex, and generic-agent compatibility

- **Canonical logic:** the changed route and delivery rules live in model-neutral `SKILL.md`,
  validator, fixture, template, and governance files. No model name or model-specific command was
  added to a skill body.
- **Claude:** the repository has `CLAUDE.md` as a route entrypoint and `AGENTS.md` as the mirrored
  repository contract. Automatic vendor loading was not executed in this wave.
- **Codex:** the repository has `AGENTS.md`; the canonical skills declare `claude-code` and
  `codex` compatibility. Automatic runtime loading was not independently tested.
- **Generic agent:** use `README.md`, `doctrine/design-doctrine.md`, the relevant
  `skills/**/SKILL.md`, and the explicit validator commands. This manual route is the portable
  fallback; no universal automatic instruction-file mechanism is claimed.

## Git and unrelated changes

The baseline was clean on `main...origin/main` ([E1]). The final working tree contains only the
files listed in this report and this report itself. No pre-existing or unrelated repository change
was observed. No commit, push, fetch, pull, reset, deletion, or sibling-repository write was made.

## Standardisation and next review

The successful learning is now in the filesystem-derived count rule, route-existence fixture and
CI gate, repo-local standards register, five-stage delivery manifest, and delivery-evidence
template. The next Wave 1 gate is 2026-08-18. The independent Wave 2 artefact-evidence review is
2026-08-25. The first source-currency review is 2026-11-11. These dates are review controls, not
claims that a source or artefact will change on those dates.

Required files were available and read. No mandatory file was unavailable.
