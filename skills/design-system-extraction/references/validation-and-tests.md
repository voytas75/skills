# Validation and tests

## Validator scope

The validator checks JSON structure, required fields, enums, identifiers, evidence references, file paths, readiness/sample consistency, manifest coverage, paired comparisons, artifact dependency rules, and status aggregation.

It does not establish that screenshots are visually accurate, that browser measurements are truthful, or that an implementation is aesthetically equivalent. Those require actual inspection and test evidence.

## Commands

```bash
python scripts/validate-evidence.py <package-directory>
python -m unittest discover -s tests -v
```

Exit codes:
- `0`: package schema and consistency checks passed;
- `1`: package validation errors;
- `2`: usage or execution error.

The validator writes `validation/validator-report.json` when possible.

## Regression requirements

Test valid analysis, snapshot, standalone, and functional packages. Test invalid readiness, contradictory outcomes, missing viewport/state pairs, missing evidence, unsafe paths, source-origin dependencies in standalone mode, and invalid tolerance declarations.

Retain historical fixtures without rewriting their original results. A legacy package is not silently migrated to a new schema.

## Limitations

Validation is a structural and logical gate, not visual QA. The skill must not claim that validator success proves reconstruction quality.
