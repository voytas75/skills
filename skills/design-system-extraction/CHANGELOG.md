# Changelog

## 1.5.1 — 2026-11-08

- Removed site-specific QA artifacts from the distributable package.
- Replaced the site-bound regression test with a synthetic legacy-format test.
- Kept schema version 1.5.0 unchanged; this is a skill/validator patch release.

## 1.5.0 — 2026-11-08

- Introduced formal execution, evidence, and comparison contracts.
- Separated `task_type` from `artifact_mode`.
- Added independent source/target readiness requirements.
- Added paired measurements and stable `element_id` matching.
- Separated sample stability tolerances from comparison tolerances.
- Separated package validation, execution completeness, and task acceptance.
- Replaced presence-only validation with consistency and scope validation.
- Added safe path resolution, including symlink escape detection.
- Added standard-library regression tests.
