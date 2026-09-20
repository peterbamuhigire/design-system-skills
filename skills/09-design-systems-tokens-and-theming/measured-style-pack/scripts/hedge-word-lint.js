#!/usr/bin/env node
/**
 * hedge-word-lint.js
 *
 * Enforces the hedging-word ban IN CODE (not just in prompt text) on any
 * generated prose that describes a measured-style-pack (spec.json,
 * handoff notes, grounding descriptions).
 *
 * Rationale (measured-style-pack SKILL.md, "Statistical Hygiene Rules"):
 * a prompt instruction not to use hedging words ("varied", "mixed", ...)
 * is violated in practice a meaningful fraction of the time. A script
 * that greps generated text and fails the build is not.
 *
 * Usage:
 *   node hedge-word-lint.js <file...>
 *   node hedge-word-lint.js stylepacks/acme/spec.json
 *
 * Exit code 0 = clean. Exit code 1 = at least one banned word found.
 * No dependencies. CommonJS, Node >=14.
 */

'use strict';

const fs = require('fs');
const path = require('path');

// Banned hedging words: describe a distribution instead of stating it.
// A model (or a human writing a spec quickly) cannot render "varied
// lighting" or "a balanced type scale" -- these words are a tell that
// the measurement was not actually consulted.
const BANNED_WORDS = [
  'varied',
  'variety',
  'mixed',
  'dynamic',
  'some',
  'often',
  'neutral',
  'roughly',
  'generally',
  'somewhat',
  'fairly',
  'balanced',
  'a mix of',
];

// Word-boundary regex per term, case-insensitive. "or" is handled
// separately below because as a bare word it collides with too much
// normal prose (e.g. inside JSON key names) -- only flag it as a
// standalone conjunction between two candidate values, a much rarer
// and more genuinely hedgy pattern ("dark or muted").
const WORD_PATTERNS = BANNED_WORDS.map((w) => ({
  word: w,
  re: new RegExp(`\\b${w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b`, 'gi'),
}));

const OR_HEDGE_RE = /\b(\w+)\s+or\s+(\w+)\b/gi;

function lintText(text) {
  const hits = [];
  for (const { word, re } of WORD_PATTERNS) {
    const matches = text.match(re);
    if (matches) {
      hits.push({ word, count: matches.length });
    }
  }
  const orMatches = text.match(OR_HEDGE_RE);
  if (orMatches) {
    hits.push({ word: 'or (hedged alternative)', count: orMatches.length });
  }
  return hits;
}

function main(argv) {
  const files = argv.slice(2);
  if (files.length === 0) {
    console.error('Usage: node hedge-word-lint.js <file...>');
    process.exit(2);
  }

  let anyFailed = false;

  for (const file of files) {
    const resolved = path.resolve(file);
    let text;
    try {
      text = fs.readFileSync(resolved, 'utf8');
    } catch (err) {
      console.error(`SKIP (unreadable): ${file} -- ${err.message}`);
      anyFailed = true;
      continue;
    }

    const hits = lintText(text);
    if (hits.length === 0) {
      console.log(`CLEAN: ${file}`);
      continue;
    }

    anyFailed = true;
    console.error(`HEDGE WORDS FOUND: ${file}`);
    for (const hit of hits) {
      console.error(`  - "${hit.word}" x${hit.count}`);
    }
  }

  process.exit(anyFailed ? 1 : 0);
}

if (require.main === module) {
  main(process.argv);
}

module.exports = { lintText, BANNED_WORDS };
