# Package and evidence model
Required root files: `execution.json`, `evidence.json`, `report.html`; reconstruction/comparison also `comparison.json`, `pair-ledger.json`; `visual-comparison.json` when visual screenshots are required. Optional `tokens.json`, `components.json`, `implementation/`, raw measurements and screenshots.

`evidence.json` includes `samples`, `evidence_registry`, `findings`, `asset_audit`/sample-level audits, `fidelity`, `results`. Registry items have unique ID, type, package-relative path or source_ref, timestamp, provenance, limitations. Observed claims require evidence; estimated claims require method. Paths must remain inside package after symlink resolution.

Samples include `sample_id,role,captured_at,viewport_id,theme,state_id,scroll_position_css_px,capture_status,capture_readiness,asset_audit,measurement_eligibility,evidence_ids`. Keep raw and normalized data separate. Store `results.execution_completeness`, `results.package_validation`, `results.task_acceptance` independently.

No private source code or copied assets if prohibited. Do not include credentials, session tokens, personal data, or secrets in artifacts.
