# Quality checks and edge cases

## Data integrity
- Are values finite numbers?
- Is the scale explicit or justified?
- Are all rows comparable?
- Are units consistent?
- Are thresholds/targets sourced from the user or a documented rule?
- Are statuses supplied or derived only from explicit rules?
- Is the difference between percentage points and relative percent change respected?

## Rendering
- Is the label column aligned?
- Is the bar width constant?
- Are zero and maximum values correct?
- Is the printed number exact enough for the source data?
- Does the selected glyph set render in the destination?
- Does the output survive copy/paste as plain text?
- Is a legend present for non-obvious symbols or bands?

## Boundary behavior
- Value = minimum → zero filled cells.
- Value = maximum → all cells filled.
- Value = midpoint → nearest-cell rounding.
- Value below minimum or above maximum → error; never silently clamp.
- Threshold at minimum or maximum → marker at boundary, with clear distinction from observed bar.
- Previous value = zero → absolute delta can be shown; relative percent change is undefined.
- Negative values → require a meaningful signed scale and an explicitly chosen representation; do not map them onto a zero-based bar without explanation.
- Missing status/previous/threshold → do not invent it; use another variant or report missing input.
- Mixed units or different denominators → separate groups or normalize explicitly.

## Evaluation cases

The machine-readable evaluation set is `evals/evals.json`. It includes positive, negative, and boundary cases. The bundled renderer tests are in `scripts/test_render_bar.py`.

## Non-goals
This skill does not:
- choose operational thresholds for a real system;
- diagnose why a metric changed;
- infer business or security impact from magnitude alone;
- replace charts when time-series shape, distribution, uncertainty, or multi-dimensional relationships matter;
- guarantee pixel-perfect alignment across all terminal emulators, fonts, or Unicode implementations.
