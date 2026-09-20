# Reference: Discover and Rehearse Phases

## Phase 1 — Discovery DOM dump

Run for each page in the flow **before** writing any script:

```javascript
const fields = await page.evaluate(() => {
  const els = [];
  document.querySelectorAll('input, select, textarea, button, [contenteditable]').forEach(el => {
    if (el.offsetParent !== null) {
      els.push({
        tag: el.tagName,
        type: el.type || '',
        name: el.name || '',
        placeholder: el.placeholder || '',
        text: el.textContent?.trim().substring(0, 40) || '',
        contentEditable: el.contentEditable === 'true',
        role: el.getAttribute('role') || '',
      });
    }
  });
  return els;
});
console.log(JSON.stringify(fields, null, 2));
```

What to look for:
- **Form fields**: native `<select>` vs a custom dropdown/combobox component.
- **Select options**: dump value AND text (`Array.from(el.options).map(o => ({ value: o.value, text: o.text }))`).
  Skip options whose text includes "Select" or whose value is `"0"`/`""` — those are placeholders
  that look like real data.
- **Rich text**: does a comment box support `@mentions`, `#tags`, markdown, emoji?
- **Required fields**: check `required`, `*` in labels, and try submitting empty to see the
  validation error text.
- **Dynamic content**: do fields appear only after other fields are filled?
- **Exact button label text** — "Submit" vs "Submit Request" vs "Send" matters for the selector.
- **Table columns**: for table-driven modals, map each `input[type="number"]` to its column
  header rather than assuming every numeric input means the same thing.

Output a field map per page, e.g.:

```text
/purchase-requests/new:
  - Budget Code: <select> (first select on page, 4 options)
  - Desired Delivery: <input type="date">
  - Context: <textarea> (not input)
  - Submit: <button> text="Submit"

/purchase-requests/N (detail):
  - Comment: <input placeholder="Type a message..."> supports @user and #PR tags
  - Send: <button> text="Send" (disabled until input has content)
```

## Phase 2 — Rehearsal helper

```javascript
async function ensureVisible(page, locator, label) {
  const el = typeof locator === 'string' ? page.locator(locator).first() : locator;
  const visible = await el.isVisible().catch(() => false);
  if (!visible) {
    const msg = `REHEARSAL FAIL: "${label}" not found - selector: ${typeof locator === 'string' ? locator : '(locator object)'}`;
    console.error(msg);
    const found = await page.evaluate(() => {
      return Array.from(document.querySelectorAll('button, input, select, textarea, a'))
        .filter(el => el.offsetParent !== null)
        .map(el => `${el.tagName}[${el.type || ''}] "${el.textContent?.trim().substring(0, 30)}"`)
        .join('\n  ');
    });
    console.error('  Visible elements:\n  ' + found);
    return false;
  }
  console.log(`REHEARSAL OK: "${label}"`);
  return true;
}
```

Rehearsal script structure:

```javascript
const steps = [
  { label: 'Login email field', selector: '#email' },
  { label: 'Login submit', selector: 'button[type="submit"]' },
  { label: 'New Request button', selector: 'button:has-text("New Request")' },
  { label: 'Submit button', selector: 'button:has-text("Submit")' },
];

let allOk = true;
for (const step of steps) {
  if (!await ensureVisible(page, step.selector, step.label)) allOk = false;
}
if (!allOk) {
  console.error('REHEARSAL FAILED - fix selectors before recording');
  process.exit(1);
}
console.log('REHEARSAL PASSED - all selectors verified');
```

When rehearsal fails: read the visible-element dump, find the correct selector, update the
script, re-run. Only proceed to recording once every step passes.
