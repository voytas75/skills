# Fidelity and acceptance
Report independent dimensions: `visual_fidelity`, `functional_fidelity`, `responsive_fidelity`, `content_fidelity`, `asset_fidelity`; each `{status:PASS|PARTIAL|FAIL|NOT_TESTED,rationale,evidence_ids}`. Do not calculate a composite score by default.

`execution_completeness`: all declared steps/modalities attempted and documented? `package_validation`: structural/schema/reference/coverage consistency? `task_acceptance`: does artifact meet frozen quality gates? A package may validate PASS while acceptance FAIL/PARTIAL.

Required gates for reconstruction: all declared viewports/states/modality ledger entries exist; every required modality is MEASURED and PASS; visual screenshot comparisons pass when visual is required; functional interactions pass when in scope; responsive/content/asset fidelity pass; no required unresolved/untested criterion. `FAIL`, `PARTIAL`, `NOT_TESTED`, `NOT_COMPARABLE`, or `BLOCKED` in a required modality blocks task acceptance PASS. An entry with status FAIL is valid package evidence, not a package validation error.

Exclusions must be frozen before capture. No retroactive waivers. If a required metric cannot be measured, record NOT_COMPARABLE/NOT_TESTED with reason; package can validate while task acceptance fails. Never alter thresholds after seeing results.

For analysis/audit, use task-specific gates; do not require reconstruction artifacts. `package_validation: PASS` never upgrades `task_acceptance`.
