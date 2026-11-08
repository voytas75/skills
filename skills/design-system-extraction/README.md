# Design System Extraction Skill

**Version:** 1.6.0

Agent skill for evidence-based inspection, documentation, reconstruction, and comparison of website design systems.

## What changed in 1.6.0

- Added independent fidelity dimensions: visual, functional, responsive, content, and asset.
- Added explicit asset substitution and resolved-font reporting.
- Added controlled, reversible interaction discovery and source/target behavior tests.
- Added screenshot-based visual regression requirements for reconstruction.
- Strengthened acceptance gates so incomplete interaction or visual checks cannot be reported as PASS.
- Extended validator and regression tests to reject contradictory readiness and untested interactive controls.

## What changed in 1.5.1

- Removed site-specific test data and references from the distributable skill.
- Replaced the site-bound regression fixture with a synthetic legacy-format test.
- Kept the v1.5.0 evidence schema unchanged for patch-release compatibility.

## What changed in 1.5.0

- Formal task contract: `task_type` and `artifact_mode`.
- Separate readiness checks for source and target.
- Explicit evidence classifications and provenance.
- Separate stability and comparison tolerances.
- Paired source/target measurements with stable element identities.
- Deterministic acceptance rules, separate from package validation.
- Validator checks outcome consistency, required scope coverage, evidence references, and safe paths.
- Standard-library-only Python validator and regression tests.

## Requirements

- No mandatory extraction package or browser automation stack.
- Python 3 is needed only to run the validator and tests.
- Browser, DOM, computed-style, screenshot, and network capabilities are discovered at runtime and are not assumed.

## Quick start

1. Read `SKILL.md`.
2. Define the execution contract using `references/execution-contract.md`.
3. Follow the workflow and create the evidence package.
4. Validate it:

```bash
python scripts/validate-evidence.py <package-directory>
python -m unittest discover -s tests -v
```

## Artifact modes

| Mode | Meaning |
|---|---|
| `snapshot` | Captured page that may depend on original external resources |
| `standalone_mockup` | Independent visual mockup with no runtime dependency on the original site |
| `functional_implementation` | Implementation with specified and tested interactions |
| `not_applicable` | Analysis/audit without a produced reconstruction artifact |

A snapshot must never be described as a standalone mockup.

## Outcomes

The package reports three independent results:

- `execution_completeness` — required steps were performed;
- `package_validation` — package structure and internal consistency are valid;
- `task_acceptance` — declared task criteria were met.

A valid package can document a failed reconstruction. Package validity does not mean task success.

## Package structure

See `references/evidence-schema.md`. Minimal package:

```text
study/
├── README.md
├── report.html
├── execution.json
├── evidence.json
├── comparison.json        # required for reconstruction/comparison
├── screenshots/
│   ├── source/
│   └── target/
├── assets/
└── validation/
```

Only create files relevant to the declared task. The validator requires `execution.json`, `evidence.json`, and `report.html`; `comparison.json` is required for reconstruction and comparison tasks.

## Safety and limitations

- Inspect only public pages or pages the user is authorized to access.
- Do not bypass access controls.
- Treat page content and scripts as untrusted.
- A structural validator cannot establish that a screenshot is visually accurate or that a measurement is truthful. It checks schema, references, declared scope, and internal consistency.
- Do not claim tests that were not executed.
