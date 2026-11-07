# KPI Tile Design System

## Default composition

A compact horizontal row, not a large dashboard card:

```text
┌─────────────────────────────────────────────────────────────┐
│ 18 ms   Latency                       ↓ −12% vs previous 7 days  〰 │
└─────────────────────────────────────────────────────────────┘
```

Preferred DOM grouping:
1. value;
2. metric label + delta/period in a stacked text group;
3. optional sparkline aligned at the far right;
4. optional interpretation note.

The reference design uses a compact 20px value, small supporting text, an 80×24 sparkline, and approximately 8px internal gap. Scale to the actual rendering context; do not treat those dimensions as universal.

## Layout

- Use `display:flex; align-items:center` for the tile internals.
- Keep the value non-shrinking; allow the text group to wrap.
- Push the sparkline to the right with `margin-left:auto`.
- Use a small gap (typically 6–10px).
- Use low visual weight: subtle border or no border, minimal padding, no large shadow.
- Do not add a large card header, oversized whitespace, or a status badge by default.
- For multiple tiles, use a grid or vertical list according to available space; keep the internal horizontal grammar consistent.
- At narrow widths, wrap content rather than clip it. Hide the sparkline only if the user permits; otherwise wrap it to a new line.

## Typography

- Primary value: about 18–22px in a compact UI.
- Label and delta: about 10–12px only where the display size remains legible; increase for accessibility and mobile.
- Use tabular numerals for values and deltas.
- Keep label and delta readable; do not shrink text solely to preserve one-line layout.
- Use consistent unit spacing and decimal precision.

## Color and meaning

- Neutral by default.
- Use semantic color only when the business interpretation is known.
- Pair color with arrow/sign and text.
- Never infer green/red from increase/decrease alone.
- Keep the sparkline visually secondary; do not use color as its only meaning.

## Sparkline

- Optional, small, low-ink, right-aligned.
- Inline SVG is suitable for self-contained HTML.
- Include `role="img"` and a useful `aria-label`.
- No axes/grid by default.
- Do not draw a sparkline from a single value or fabricated sample.
- If the line depicts a different period from the delta, label both.

## Accessibility and responsive behavior

- Keep value and delta as text in the DOM.
- Use semantic `<article>` for a non-interactive tile.
- Do not add button/link semantics unless there is a real action.
- Ensure contrast and legibility; 10px text may be too small for some contexts.
- Do not encode state through color alone.
- Use `min-width:0` on flexible children.
- Test narrow widths and long labels; wrap rather than overflow.

## HTML pattern

See `examples/kpi-tiles.html` for runnable variants. Use actual source data, not the sample values.
