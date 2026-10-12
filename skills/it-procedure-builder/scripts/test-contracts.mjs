#!/usr/bin/env node
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validate } from './validate-package.mjs';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const fixture = (...parts) => join(root, 'examples', 'fixtures', ...parts);
const load = async (name) => JSON.parse(await readFile(fixture(name), 'utf8'));

const packageData = await load('accepted-procedure-package.json');
const acceptedCritique = await load('accepted-critique-report.json');
const inconsistentCritique = await load('inconsistent-critique-report.json');

assert.deepEqual(validate(packageData, acceptedCritique), {
  accepted: true,
  average: 4.6,
  requestId: 'fixture-accepted-procedure'
});

assert.throws(
  () => validate(packageData, inconsistentCritique),
  /decision does not match the quality gate/
);

const unsupportedClaim = structuredClone(packageData);
unsupportedClaim.claims[0].evidenceIds = [];
assert.throws(
  () => validate(unsupportedClaim, acceptedCritique),
  /Confirmed claim lacks evidence IDs/
);

const missingClaims = structuredClone(packageData);
delete missingClaims.claims;
assert.throws(
  () => validate(missingClaims, acceptedCritique),
  /ProcedurePackage.claims must be an array/
);

console.log('builder contract tests: ok');
