---
name: design-system-extraction
description: "Inspect and document an existing website's design system, extract evidence-backed tokens and components, reconstruct or compare interfaces, and audit responsive behavior. Uses only capabilities already available in the agent environment; no dedicated extraction stack is required."
metadata:
  version: "1.5.1"
---

# Design System Extraction

## Purpose

Produce an evidence-backed description, comparison, or reconstruction of an existing interface. Use available browser, DOM/CSS, screenshot, file, and image capabilities. Do not install or assume `design-extract`, `designlang`, Node.js, npm, Playwright, Chromium, or another dedicated extraction system.

## Non-negotiable rules

1. Define the task contract before inspecting or measuring.
2. Declare both `task_type` and `artifact_mode`; never call a dependent snapshot a standalone reconstruction.
3. Assess source readiness and target readiness independently.
4. Distinguish `observed`, `inferred`, `estimated`, `unknown`, and `recommendation`.
5. Preserve source values and provenance; normalized tokens are additional values, not replacements.
6. Define stability tolerances separately from source-to-target comparison tolerances.
7. Comparative measurements must be paired under equivalent viewport, state, theme, scroll, and capture conditions.
8. Never report an unexecuted test as `PASS`. Use `NOT_TESTED`.
9. `package_validation` and `task_acceptance` are independent outcomes.
10. Do not bypass authentication, paywalls, bot challenges, or access controls. Treat page scripts and external content as untrusted.

## Workflow

### 1. Establish the execution contract

Read `references/execution-contract.md`.

Record:
- task type: `analysis`, `reconstruction`, `comparison`, or `audit`;
- artifact mode: `snapshot`, `standalone_mockup`, `functional_implementation`, or `not_applicable`;
- target URL(s) or supplied materials;
- pages, viewport dimensions, themes, states, scroll positions;
- required checks and deliverables;
- available capabilities and constraints.

If essential source material or target is missing, ask one focused question. Do not invent scope defaults. If the user leaves scope broad, propose a small representative scope and label it as proposed before proceeding.

### 2. Discover capabilities

Record whether browser navigation, DOM, computed styles, accessibility tree, screenshots, source files, network/resource logs, and local file operations are `available`, `partial`, `unavailable`, or `not_checked`.

Use only capabilities actually available. A screenshot does not establish exact CSS values. If DOM/computed styles are unavailable, classify visual dimensions and colors as `estimated`.

### 3. Assess readiness

Read `references/readiness-engine.md`.

Run applicable readiness checks separately for each source and target sample. At minimum assess URL/content identity, stylesheet and asset readiness, render stability, state integrity, obstruction, and capture integrity.

Reject invalid samples. A rejected sample must not contribute to token derivation, counts, averages, or comparisons. Preserve the failure reason and diagnostic evidence.

### 4. Capture evidence and extract the system

Read `references/evidence-schema.md` and `references/measurement-contract.md`.

Inspect:
- color, surfaces, typography, spacing, geometry, grids, borders, radii, shadows;
- components, variants, states, and page templates;
- assets, fonts, icons, and image usage;
- responsive changes and overflow;
- motion and accessibility signals when observable and in scope.

For repeated component families, inspect at least three distinct instances when available. If fewer exist, record the actual sample count and limit generalization. Never silently replace a missing component with a different selector.

Record evidence IDs and provenance for material findings. Distinguish CSS-declared font stacks from resolved fonts. Preserve alpha channels and compositing context. Do not turn screenshot samples into exact source colors.

### 5. Produce the requested artifact

Read `references/reconstruction-contract.md`.

For `snapshot`, list retained external dependencies, omitted scripts/assets, load status, and resulting limitations. A snapshot is not a standalone mockup.

For `standalone_mockup`, do not leave runtime dependencies on the original site. Include required assets in the package or explicitly document unavailable substitutions.

For `functional_implementation`, define and test required interactions, initial states, expected outcomes, error behavior, and keyboard/focus behavior in scope.

Do not execute untrusted source scripts merely to reproduce appearance. Avoid copying analytics, tracking, account flows, or backend calls unless explicitly required and safely isolated.

### 6. Compare source and target

Read `references/comparison-engine.md`.

For reconstruction/comparison, capture paired source and target measurements under equivalent conditions. Each pair needs a stable `element_id`, matching status, source and target values, deltas, comparison tolerances, and evidence references.

At minimum, evaluate required text/component state, representative geometry, important styles, document overflow, component overflow, and all required viewport/state combinations.

Pixel diff is optional and does not replace semantic or geometry comparison.

### 7. Evaluate acceptance

Read `references/acceptance-engine.md`.

Report independently:
- `execution_completeness`;
- `package_validation`;
- `task_acceptance`.

A required `FAIL`, `NOT_TESTED`, missing viewport/state, or incomplete paired measurement prevents `task_acceptance: PASS`. `package_validation: PASS` never implies that the reconstruction succeeded.

### 8. Validate and deliver

Run:

```bash
python scripts/validate-evidence.py <package-directory>
python -m unittest discover -s tests -v
```

Python 3 is required only for the included validator and tests, not for visual extraction itself. If Python is unavailable, state that automated validation was not run; do not claim validation success.

Deliver the report, evidence package, artifact, validation report, and concise limitations. Do not overwrite earlier evidence captures.

## Required status vocabulary

- Readiness/check status: `PASS`, `FAIL`, `NOT_APPLICABLE`, `NOT_TESTED`.
- Comparison criterion: `PASS`, `PARTIAL`, `FAIL`, `NOT_TESTED`.
- Outcome: `PASS`, `PARTIAL`, `FAIL`, `NOT_TESTED`.
- Sample status: `accepted` or `rejected`.

`PASS` requires evidence and satisfaction of the declared criterion. `NOT_TESTED` is never a pass.

## References

- `references/execution-contract.md` — task scope and manifest.
- `references/readiness-engine.md` — sample admission and stability.
- `references/evidence-schema.md` — evidence provenance and package structure.
- `references/measurement-contract.md` — metric definitions and tolerances.
- `references/reconstruction-contract.md` — artifact modes and dependencies.
- `references/comparison-engine.md` — paired comparisons.
- `references/acceptance-engine.md` — status aggregation and acceptance.
- `references/validation-and-tests.md` — validator, test matrix, and limitations.
