#!/usr/bin/env node
/**
 * test-banned-font-gate.js — direct unit test of banned-font-gate.js.
 * Runs the hook as a child process with a synthesized stdin payload and
 * checks the exit code, since that's the actual contract Claude Code uses
 * (exit 0 = allow, exit 2 = block). Run: node hooks/test-banned-font-gate.js
 */

'use strict';

const { spawnSync } = require('child_process');
const path = require('path');

const HOOK = path.join(__dirname, 'banned-font-gate.js');

function run(payload, env = {}) {
  const result = spawnSync(process.execPath, [HOOK], {
    input: JSON.stringify(payload),
    encoding: 'utf8',
    env: { ...process.env, ...env },
  });
  return { code: result.status, stderr: result.stderr };
}

const cases = [
  {
    name: 'CSS primary Inter — BLOCK',
    payload: { tool_input: { file_path: '/proj/src/App.css', content: 'body { font-family: Inter, sans-serif; }' } },
    expect: 2,
  },
  {
    name: 'CSS primary Geist — BLOCK',
    payload: { tool_input: { file_path: '/proj/src/App.scss', content: '.h1 { font-family: "Geist", sans-serif; }' } },
    expect: 2,
  },
  {
    name: 'CSS fallback-only Inter (not primary) — ALLOW',
    payload: { tool_input: { file_path: '/proj/src/App.css', content: 'body { font-family: "Canela", Inter, sans-serif; }' } },
    expect: 0,
  },
  {
    name: 'Approved font Canela — ALLOW',
    payload: { tool_input: { file_path: '/proj/src/App.css', content: 'body { font-family: "Canela", serif; }' } },
    expect: 0,
  },
  {
    name: 'python-docx quoted literal Roboto — BLOCK',
    payload: { tool_input: { file_path: '/proj/gen/report.py', content: 'run.font.name = "Roboto"' } },
    expect: 2,
  },
  {
    name: 'MultiEdit new_string with Poppins — BLOCK',
    payload: { tool_input: { file_path: '/proj/src/App.tsx', edits: [{ new_string: 'fontFamily: "Poppins"' }] } },
    expect: 2,
  },
  {
    name: 'Non-relevant extension (.md) — ALLOW without even checking',
    payload: { tool_input: { file_path: '/proj/README.md', content: 'font-family: Inter' } },
    expect: 0,
  },
  {
    name: 'Exempt glob covers target — ALLOW despite banned font',
    payload: { tool_input: { file_path: '/proj/node_modules/theme/App.css', content: 'font-family: Inter;' } },
    env: { CHWEZI_FONT_EXEMPT_GLOBS: '**/node_modules/**' },
    expect: 0,
  },
  {
    name: 'CHWEZI_FONT_GATE=off — ALLOW despite banned font',
    payload: { tool_input: { file_path: '/proj/src/App.css', content: 'font-family: Inter;' } },
    env: { CHWEZI_FONT_GATE: 'off' },
    expect: 0,
  },
  {
    name: 'Malformed stdin — fail open, ALLOW',
    payload: null, // handled specially below
    expect: 0,
  },
  {
    name: 'Source Sans 3 as primary — BLOCK (conditional-primary-only ban)',
    payload: { tool_input: { file_path: '/proj/src/App.css', content: 'h1 { font-family: "Source Sans 3", sans-serif; }' } },
    expect: 2,
  },
];

let failures = 0;
for (const c of cases) {
  let result;
  if (c.payload === null) {
    const raw = spawnSync(process.execPath, [HOOK], { input: 'not json {{{', encoding: 'utf8' });
    result = { code: raw.status, stderr: raw.stderr };
  } else {
    result = run(c.payload, c.env || {});
  }
  const pass = result.code === c.expect;
  console.log(`${pass ? 'PASS' : 'FAIL'} — ${c.name} (expected exit ${c.expect}, got ${result.code})`);
  if (!pass) {
    failures++;
    if (result.stderr) console.log(`       stderr: ${result.stderr.split('\n')[0]}`);
  }
}

console.log(`\n${cases.length - failures}/${cases.length} passed`);
process.exit(failures > 0 ? 1 : 0);
