# Acceptance engine (v1.6.0)

## Independent outcomes

Report `execution_completeness`, `package_validation`, and `task_acceptance` independently. They are not interchangeable.

## Fidelity dimensions

For reconstruction, report `visual_fidelity`, `functional_fidelity`, `responsive_fidelity`, `content_fidelity`, and `asset_fidelity` independently. Each requires status, rationale, and evidence IDs. Read `fidelity-and-runtime.md`.

## Hard gates

- Required comparison criterion FAIL/PARTIAL/NOT_TESTED blocks task acceptance PASS.
- Missing required viewport/state or paired measurement blocks PASS.
- Missing screenshot visual-comparison pair blocks PASS.
- Missing source or target interaction test for an in-scope visible control blocks functional PASS.
- Asset readiness PASS with any substitution or unresolved asset is invalid.
- Resolved-font status cannot be inferred from a loaded font face alone.
- Any required fidelity dimension other than PASS blocks task acceptance PASS.
- Element ID coverage is not visual fidelity.
- Package validation PASS never upgrades task acceptance.
