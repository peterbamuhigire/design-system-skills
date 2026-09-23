# Anchored design review verdict

Use the canvas response as the retained review record:

```json
{"status":"feedback","items":[{"kind":"annotation","text":"Clarify the primary action","anchor":{"selector":"button.cta-primary","tag":"button"}},{"kind":"verdict","verdict":"request-changes"}]}
```

The annotation goes to the owning remediation skill. A request-changes verdict keeps the gate
open; an approve verdict is recorded by the accountable release reviewer.
