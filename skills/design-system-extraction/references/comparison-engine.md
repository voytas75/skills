# Paired comparison engine

## Pairing conditions

A source/target pair is comparable only when viewport, theme, state, scroll, and capture conditions match or a documented mapping is approved. Pair samples by explicit IDs, not array order.

Each comparison entry requires:
- unique `comparison_id`;
- `viewport_id`, `theme`, `state_id`;
- stable `element_id`;
- `match_status` (`matched`, `unmatched`, `ambiguous`);
- source and target sample IDs;
- source and target measurement values;
- deltas;
- comparison tolerances;
- result status;
- evidence IDs.

An unmatched or ambiguous element cannot pass a required geometry/style comparison.

## Required reconstruction criteria

Unless explicitly excluded before execution:
- `content_state`;
- `geometry`;
- `important_styles`;
- `document_overflow`;
- `component_overflow`;
- `asset_completeness`.

All required viewport/theme/state combinations must be represented. Source-only measurements do not establish a comparison.

## Pixel difference

Pixel diff is optional. If used, record method/tool, normalization, masked regions, threshold, numeric result, and paired screenshots. Pixel diff does not replace semantic, geometry, or overflow checks.

## Deviations

Each material deviation should include severity, affected element/viewport, observed delta, expected tolerance, impact, and evidence references.
