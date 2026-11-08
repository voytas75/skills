# design-system-extraction

Version: **1.6.1** · Schema: **1.6.1** · Python standard library only for validator/tests.

General-purpose agent skill for evidence-backed website design-system extraction, reconstruction, comparison and audit. The normative instructions are in `SKILL.md`; compact technical contracts are in `references/`; JSON contracts are in `schemas/`.

## v1.6.1
- Separates capture readiness, asset audit, and modality-specific measurement eligibility.
- Resource substitutions no longer invalidate otherwise stable screenshots/DOM/geometry.
- Adds mandatory pair ledger: every required viewport × theme × state × modality has a record, including `FAIL`, `NOT_TESTED`, `NOT_COMPARABLE`, and `BLOCKED`.
- Makes package validity independent from task acceptance: validly recorded failures do not invalidate the package.
- Supports shared semantic anchors for footer/document-end comparisons when absolute scroll positions differ.
- Permits rejected/partial legacy samples in modality-specific comparisons only when that modality is explicitly eligible.
- Adds synthetic regression tests; no site-specific artifacts are distributed.

## Run
```bash
python scripts/validate-evidence.py <package-directory>
python -m unittest discover -s tests -v
```
