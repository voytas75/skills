# Evidence schema and package layout

## Evidence classes

Use:
- `observed`: directly read or measured;
- `inferred`: conclusion based on identified evidence;
- `estimated`: approximate value, e.g. inferred from pixels;
- `unknown`: insufficient evidence;
- `recommendation`: proposed change, not a claim about the source.

An `observed` finding requires at least one valid evidence reference. An `estimated` finding must disclose its estimation method. Never present screenshot-derived color or geometry as exact computed CSS.

## Evidence registry

Each `evidence_registry` entry has:
- unique `evidence_id`;
- `type` (`screenshot`, `dom`, `computed_style`, `stylesheet`, `asset`, `network`, `manual_note`, `test_result`);
- package-relative `path` or a non-file `source_ref`;
- `captured_at`;
- optional `sample_id`, `viewport_id`, `state_id`;
- `provenance`;
- `limitations`.

File paths must remain inside the package, including after symlink resolution.

## Samples

Every sample has:
- `sample_id`, `role` (`source` or `target`), `captured_at`;
- `status` (`accepted` or `rejected`);
- `viewport_id`, `theme`, `state_id`, `scroll_position_css_px`;
- non-empty `readiness` object;
- `evidence_ids` array.

Each `readiness` control is an object: `{ "status": "PASS", "details": "..." }`.

## Findings

Each finding has unique `finding_id`, non-empty `claim`, `classification`, and `evidence_ids`. An `observed` finding must cite evidence. Findings should state scope and limitations where material.

## Results

`results` contains `execution_completeness`, `package_validation`, and `task_acceptance`. These are separate outcomes and must be reconciled by the validator. `outcomes` contains named task dimensions, each with status and rationale.

## Recommended package

```text
study/
├── README.md
├── report.html
├── execution.json
├── evidence.json
├── comparison.json
├── tokens.json
├── components.json
├── implementation/
├── screenshots/source/
├── screenshots/target/
├── assets/
└── validation/validator-report.json
```

Create only applicable files. Reconstruction and comparison require `comparison.json`; analysis/audit do not. Tokens/components files are optional unless requested by scope.
