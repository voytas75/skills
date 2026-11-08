# Readiness engine

Assess source and target independently. A source sample being ready does not make a target sample ready.

## Required controls

Each sample contains a non-empty `readiness` object. Every required control is represented by an object with `status`, `details`, and optionally `evidence_ids`.

| Control | Purpose |
|---|---|
| `url_identity` | Correct route or approved redirect |
| `content_identity` | Expected page landmarks/content present |
| `stylesheet_readiness` | Relevant stylesheets loaded and applied |
| `asset_readiness` | Relevant fonts, images, SVGs and icons loaded or explicitly missing |
| `render_stability` | Consecutive observations within declared stability tolerances |
| `state_integrity` | Viewport, theme, scroll, and component state match the contract |
| `obstruction_check` | No blocking loading/consent/modal/transition state invalidates measurement |
| `capture_integrity` | Capture is readable, non-empty, and has known dimensions |

Applicable controls use `PASS`, `FAIL`, or `NOT_TESTED`. Use `NOT_APPLICABLE` only with a non-empty rationale. Every control has a `details` string; evidence references are recommended and required for material observed claims.

## Sample admission

- `accepted` requires all applicable required controls to be `PASS`.
- A required `FAIL` or `NOT_TESTED` requires `rejected`.
- `rejected` samples remain in the record for diagnosis but are excluded from metrics and comparisons.
- A retry creates a new `sample_id`; do not rewrite history.
- Readiness of source and target is recorded on their respective samples.

## Stability tolerances

Declare `stability_tolerance` per metric/property before measuring. Examples may include subpixel geometry or exact text/state equality. Do not apply a single generic tolerance to unrelated properties.

Stability tolerance is not source-to-target comparison tolerance.
