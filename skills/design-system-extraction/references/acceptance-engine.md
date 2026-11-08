# Acceptance engine

## Independent results

- `execution_completeness`: whether all steps required by the manifest were performed;
- `package_validation`: whether package structure, references, scope, and status consistency are valid;
- `task_acceptance`: whether the declared task criteria were met.

Do not infer one from another.

## Statuses

- `PASS`: all required criteria met with evidence.
- `PARTIAL`: useful result, but some criteria are incomplete or partially met.
- `FAIL`: at least one material requirement failed.
- `NOT_TESTED`: insufficient execution to assess.

## Aggregation

- A required `FAIL` blocks task acceptance `PASS`.
- A required `NOT_TESTED` blocks task acceptance `PASS`.
- A required `PARTIAL` blocks `PASS`, unless excluded in the manifest before execution.
- Missing required viewport/state or paired measurement blocks `PASS`.
- Outcome `PASS` cannot coexist with a required criterion `FAIL`.
- `package_validation: PASS` never upgrades task acceptance.
- A valid package may document a failed task.
- Package validation failure prevents delivery as a validated complete package, but does not erase recorded test outcomes.

## Profiles

For analysis/audit, assess source readiness, declared inspection coverage, provenance, and limitations.

For snapshot reconstruction, document dependencies and omissions; do not claim standalone independence.

For standalone reconstruction, require no runtime dependency on the source origin, complete required pairs, and all required checks passing.

For functional implementation, additionally require executed behavior tests for all required interactions.
