# Independent delivery-evidence validator review

Scope: current malformed-field changes in `scripts/validate_design_delivery_evidence.py` and `tests/test_design_delivery_evidence.py`. Implementation and other workers' documentation were not edited. Root instructions, doctrine, local improvement skill, its Kaizen contract and quality gate informed the evidence boundaries. This is a code review, not a scored engine or rendered-product audit. NO_TIME_SENSITIVE_CLAIMS.

## Verdict and actionable finding

The changed type guards reject the exercised malformed values without a false structural pass. A malformed render-path crash remains (synthesis).

**Medium — escaped NUL in a render path escapes normal error reporting.** A nonblank JSON string containing an escaped NUL passes the updated render-path type guard. The subsequent filesystem check raises `ValueError` outside any handler. Reproduced through `validate_manifest` and the CLI entrypoint. The process does not falsely succeed, but the normal findings report is lost. This is a residual gap adjacent to the changed guard, not a newly introduced filesystem operation. [Affected path handling](../../scripts/validate_design_delivery_evidence.py#L67)

Suggested acceptance: reject invalid path strings with a render-specific finding; handle expected path-resolution/stat failures without traceback. Add function and CLI regression coverage. The new parametrisation does not exercise render paths or surface entries despite changes to their guards; include these fields and verify the relevant finding, not merely any finding. [New tests](../../tests/test_design_delivery_evidence.py#L12)

## Dated disposition — 2026-09-07

The escaped-NUL render-path defect identified here was repaired before resumed verification; the design suite then recorded 80 passing tests. The requested direct render-path and CLI regression breadth, actual rendering, accessibility, evidence authenticity and visual-quality checks remain **NOT ASSESSED**. Retain the residual finding as backlog until directly evidenced. Next review: 2026-09-13 ([log](../../skills-web-dev/docs/audits/2026-09-06-kaizen/resume-2026-09-07/design-system-skills-tests.log)).

## Reproducible checks and primary execution evidence

Executed from the repository root:

```powershell
python -B -m pytest -q -p no:cacheprovider tests/test_design_delivery_evidence.py
```

Observed: the focused suite passed. No full-engine or render-quality verdict is implied.

In-memory reproduction, with no manifest writes:

```python
import json, sys
from pathlib import Path
from unittest.mock import patch
from scripts import validate_design_delivery_evidence as m
p = Path('tests/fixtures/design-delivery/manifest.json').resolve()
d = json.loads(p.read_text(encoding='utf-8'))
d['renders'][0]['path'] = 'bad\x00.svg'
with patch.object(Path, 'read_text', return_value=json.dumps(d)):
    try:
        print(m.validate_manifest(p))
    except Exception as exc:
        print(type(exc).__name__, str(exc))
    with patch.object(sys, 'argv', ['validator', str(p)]):
        try:
            print(m.main())
        except Exception as exc:
            print(type(exc).__name__, str(exc))
```

Observed execution evidence: the function and CLI each raised `ValueError` with message `stat: embedded null character in path`.

Additional executed probes: blank, object and list render paths returned path findings; null, object, list, boolean and blank surface entries returned surface findings. An injected `UnicodeDecodeError` returned a manifest-read finding. These are synthetic input/error-path checks, not evidence of actual inaccessible-file or link behaviour.

No new false pass was reproduced in the changed guards. Evidence authenticity, referenced-record content, actual reopening/rendering, accessibility and visual quality remain NOT_ASSESSED. Existing fixture tests create and remove their own temporary manifests; no operational commands, external research, source-register edits or implementation changes were performed by this review.
