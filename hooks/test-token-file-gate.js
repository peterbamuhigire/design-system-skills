#!/usr/bin/env node
/**
 * test-token-file-gate.js — direct unit test of token-file-gate.js.
 * Runs the hook as a child process with a synthesized stdin payload and
 * checks the exit code, since that's the actual contract Claude Code uses
 * (exit 0 = allow, exit 2 = block). Run: node hooks/test-token-file-gate.js
 *
 * Each case gets its own CHWEZI_TOKEN_GATE_STATE_DIR so the deny-once-then-
 * allow-retry state from one case never leaks into the next (matches the
 * isolation destructive-bash-gate's own test suite relies on).
 */

'use strict';

const { spawnSync } = require('child_process');
const path = require('path');
const os = require('os');
const fs = require('fs');

const HOOK = path.join(__dirname, 'token-file-gate.js');

function freshStateDir(name) {
  const dir = path.join(os.tmpdir(), 'chwezi-token-gate-test-' + name + '-' + process.pid);
  fs.rmSync(dir, { recursive: true, force: true });
  return dir;
}

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
    name: 'New tokens/design-tokens.json — DENY (first attempt)',
    payload: { tool_input: { file_path: '/proj/tokens/design-tokens.json', content: '{"color":{"primary":"#123"}}' } },
    env: { CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case1') },
    expect: 2,
  },
  {
    name: 'Retry same path after denial — ALLOW',
    payload: { tool_input: { file_path: '/proj/tokens/design-tokens.json', content: '{"color":{"primary":"#123"}}' } },
    env: { CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case2') },
    expect: 'retry-allow', // handled specially below: deny once, then allow
  },
  {
    name: 'New *.tokens.json anywhere — DENY',
    payload: { tool_input: { file_path: '/proj/src/brand.tokens.json', content: '{}' } },
    env: { CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case3') },
    expect: 2,
  },
  {
    name: 'New design-tokens.css at repo root — DENY',
    payload: { tool_input: { file_path: '/proj/design-tokens.css', content: ':root { --color-primary: #123; }' } },
    env: { CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case4') },
    expect: 2,
  },
  {
    name: 'Non-token file (App.css) — ALLOW without even checking',
    payload: { tool_input: { file_path: '/proj/src/App.css', content: 'body { color: red; }' } },
    env: { CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case5') },
    expect: 0,
  },
  {
    name: 'Exempt glob covers target — ALLOW despite token path',
    payload: { tool_input: { file_path: '/proj/vendor/tokens/theme.tokens.json', content: '{}' } },
    env: { CHWEZI_TOKEN_EXEMPT_GLOBS: '**/vendor/**', CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case6') },
    expect: 0,
  },
  {
    name: 'CHWEZI_TOKEN_GATE=off — ALLOW despite token path',
    payload: { tool_input: { file_path: '/proj/tokens/design-tokens.json', content: '{}' } },
    env: { CHWEZI_TOKEN_GATE: 'off', CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case7') },
    expect: 0,
  },
  {
    name: 'Malformed stdin — fail open, ALLOW',
    payload: null, // handled specially below
    env: { CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case8') },
    expect: 0,
  },
  {
    name: 'Non-Write-shaped payload (no file_path at all) — ALLOW',
    payload: { tool_input: { command: 'ls tokens/' } },
    env: { CHWEZI_TOKEN_GATE_STATE_DIR: freshStateDir('case9') },
    expect: 0,
  },
  {
    name: 'Unwritable state dir — fail open, ALLOW',
    payload: { tool_input: { file_path: '/proj/tokens/design-tokens.json', content: '{}' } },
    // Point state dir at a path that cannot be created (a file, not a dir, as the "parent")
    env: { CHWEZI_TOKEN_GATE_STATE_DIR: (() => {
      const blocker = path.join(os.tmpdir(), 'chwezi-token-gate-blocker-file-' + process.pid);
      fs.writeFileSync(blocker, 'x');
      return path.join(blocker, 'nested', 'state');
    })() },
    expect: 0,
  },
];

let failures = 0;
for (const c of cases) {
  if (c.expect === 'retry-allow') {
    const first = run(c.payload, c.env || {});
    const passFirst = first.code === 2;
    const second = run(c.payload, c.env || {});
    const passSecond = second.code === 0;
    const pass = passFirst && passSecond;
    console.log(`${pass ? 'PASS' : 'FAIL'} — ${c.name} (first=${first.code}, retry=${second.code})`);
    if (!pass) failures++;
    continue;
  }

  let result;
  if (c.payload === null) {
    const rawResult = spawnSync(process.execPath, [HOOK], {
      input: 'not json {{{',
      encoding: 'utf8',
      env: { ...process.env, ...(c.env || {}) },
    });
    result = { code: rawResult.status, stderr: rawResult.stderr };
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
