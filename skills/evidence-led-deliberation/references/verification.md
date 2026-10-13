# Candidate verification and repair branches

Read this reference at step 5 of `SKILL.md` when verifying a candidate, and at step 6 when verification is failed or inconclusive.

## Evidence selection

Use the strongest available tool evidence: focused tests, build, lint, schema validation, deterministic calculation, source inspection, or a requirements-to-artifact check. Record the command or method, result, and remaining gaps in `evidence.md`; mark the candidate `verified`, `failed`, or `inconclusive`.

Run generated code only through the established execution policy in a disposable isolated environment. If one is unavailable, do not execute it; mark runtime verification inconclusive.

When a broad suite fails at collection or global lint/type checks exposes unrelated debt, record that result separately. Run or add a focused regression test for the changed contract plus scoped checks. Do not call the broad failure a candidate failure unless the evidence links it to the candidate.

## Tool-using application acceptance

For an agent/tool-interface change, first qualify the contract with provider-free checks. Add one real model task with independently computed expected output only after explicit approval of the provider, request budget or cost, and data to be sent. Do not load credentials or dispatch a live request before that approval. Without approval, report live acceptance as unverified; do not treat provider-free success as model qualification. A passing suite, exit 0 or successful dispatch proves execution, not that the user's requested outcome was achieved. Inspect the actual model arguments and compare returned data to ground truth before accepting synthesis. If a model repeatedly emits the string `"null"` for a nullable filename-only search argument, compare direct tool calls with JSON null and the literal string: a correct direct result localizes the failure to the model-facing contract. Use an explicit operation mode and nonnullable arguments rather than silently converting searchable text; retain a test for literal `"null"` content searches.

When CLI tests fail only under long temporary paths, reproduce with the default test path and a deliberately narrow console before changing application code. Rich can wrap inside a filename. Assert the failure exit and the complete selected path with rendering whitespace normalized, and provide a valid alternative config to verify that selection still fails closed. Run both the default full suite and the short-path variant; the latter alone must not be called unconditional suite success.

## Python package branches

For package build/import checks:

1. Build from a disposable copy.
2. Install dependencies separately, then install the wheel with `--no-deps`.
3. Import from a non-repository working directory; do not install the target repository editable, because source exposure can make a wheel check pass.
4. For launcher compatibility, invoke both the corresponding installed module and a copied launcher with `--help` from that non-repository directory. For configuration-dependent CLIs, also run the documented first-start flow offline with isolated HOME/CWD and no editable import hooks: check the pre-setup error, explicit initialization, subsequent validation and refusal to overwrite. Verify required templates are actually loaded from the installed package; `--help` and wheel inventory alone do not establish startup. Export the current candidate bytes when changes are uncommitted; `git archive HEAD` would test the old version. After publication, separately test an export of the published commit without ignored operator config, credentials or runtime state.

If an import first fails because declared dependencies or required configuration are absent, record it as inconclusive. Have the reviewer prescribe a dependency-complete, non-sensitive test before changing the candidate.

For Python optional-dependency metadata, inventory imports used by affected tests. Keep base and `dev` profiles free of application extras unless the contract says otherwise. Document a full-test installation as an explicit extras composition, because PEP 621 extras do not compose each other. Verify relevant profiles in fresh environments; use prerelease resolution only when the tested dependency requires it and record that choice.

## Repair rounds

If verification fails or is inconclusive, spawn one isolated native reviewer subagent with the failure evidence and candidate artifact. Require exactly one prioritized repair task or a justified switch of approach. Do not repeat an unchanged task. Create a new candidate version and repeat verification.

Stop after three repair rounds. Confirm each round added distinct evidence or changed the approach.
