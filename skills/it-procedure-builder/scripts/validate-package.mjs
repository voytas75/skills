#!/usr/bin/env node
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';

const requiredSections = [
  'executiveSummary', 'scope', 'assumptions', 'dependencies',
  'rolesAndResponsibilities', 'phasedImplementationPlan',
  'detailedExecutionSteps', 'deliverables', 'riskRegister',
  'validationPlan', 'rollbackPlan', 'successMetrics',
  'mermaidDiagram', 'openQuestions'
];

const requiredScores = [
  'completeness', 'executability', 'safety', 'evidenceAlignment',
  'validationAndRollback'
];

function fail(message) {
  throw new Error(message);
}

async function readJson(path) {
  try {
    return JSON.parse(await readFile(path, 'utf8'));
  } catch (error) {
    fail(`Cannot read JSON at ${path}: ${error.message}`);
  }
}

export function validate(packageData, critique) {
  if (packageData?.schemaVersion !== '1.0' || critique?.schemaVersion !== '1.0') {
    fail('Unsupported or missing schemaVersion.');
  }
  if (!packageData.requestId || packageData.requestId !== critique.requestId) {
    fail('ProcedurePackage and CritiqueReport must have the same requestId.');
  }
  if (typeof packageData.title !== 'string' || packageData.title.trim() === '' ||
      typeof packageData.sourceRequestSummary !== 'string' || packageData.sourceRequestSummary.trim() === '') {
    fail('ProcedurePackage title and sourceRequestSummary are required.');
  }
  if (!packageData.sections || typeof packageData.sections !== 'object') {
    fail('ProcedurePackage.sections is required.');
  }

  const missingSections = requiredSections.filter((key) => {
    const value = packageData.sections[key];
    return typeof value !== 'string' || value.trim() === '';
  });
  if (missingSections.length > 0) {
    fail(`Missing required procedure sections: ${missingSections.join(', ')}.`);
  }

  if (!Array.isArray(packageData.claims)) {
    fail('ProcedurePackage.claims must be an array.');
  }
  for (const claim of packageData.claims) {
    if (!claim || typeof claim.text !== 'string' || !['confirmed', 'assumption', 'unknown'].includes(claim.status) ||
        !Array.isArray(claim.evidenceIds)) {
      fail('Each claim requires text, a supported status, and an evidenceIds array.');
    }
    if (claim.status === 'confirmed' && claim.evidenceIds.length === 0) {
      fail(`Confirmed claim lacks evidence IDs: ${claim.text ?? '<unnamed claim>'}.`);
    }
  }

  for (const field of ['missingRequiredSections', 'criticalIssues', 'requiredFixes']) {
    if (!Array.isArray(critique?.[field])) fail(`CritiqueReport.${field} must be an array.`);
  }
  if (!['accepted', 'revision_required', 'needs_human_input'].includes(critique.decision)) {
    fail('CritiqueReport decision is invalid.');
  }

  const scores = requiredScores.map((key) => {
    const value = critique?.scores?.[key];
    if (typeof value !== 'number' || value < 0 || value > 5) {
      fail(`Invalid critique score: ${key}.`);
    }
    return value;
  });

  const average = scores.reduce((sum, value) => sum + value, 0) / scores.length;
  const accepted = Math.min(...scores) >= 4 && average >= 4.2 &&
    (critique.missingRequiredSections?.length ?? 0) === 0 &&
    (critique.criticalIssues?.length ?? 0) === 0;

  if (accepted !== (critique.decision === 'accepted')) {
    fail('Critique decision does not match the quality gate.');
  }

  return { accepted, average: Number(average.toFixed(2)), requestId: packageData.requestId };
}

const isCli = process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isCli) {
  const [packagePath, critiquePath] = process.argv.slice(2);
  if (!packagePath || !critiquePath) {
    console.error('Usage: node validate-package.mjs <procedure-package.json> <critique-report.json>');
    process.exit(64);
  }

  try {
    console.log(JSON.stringify(validate(await readJson(packagePath), await readJson(critiquePath))));
  } catch (error) {
    console.error(`Validation failed: ${error.message}`);
    process.exit(1);
  }
}
