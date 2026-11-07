---
name: unicode-text-charts
description: Create and review Unicode text sparklines, heatmaps, trees, timelines, Gantt charts, and Braille plots. Use for text-only reports or monospace output when relationships, time, or distributions matter more than a single magnitude bar.
metadata:
  version: "1.0.0"
---

# Unicode Text Charts

## Scope

Choose a text-native visualization for supplied data. This package covers structured charts, not single-value progress or magnitude bars; use `monospace-data-bars` for those.

Treat examples as synthetic. Never invent observations, dates, task durations, relationships, statuses, thresholds, or missing values. Do not infer causality from order or proximity.

## Workflow

1. Identify the question, audience, output medium, available width, and actual source data.
2. Choose one form: sparkline for ordered numeric observations; heatmap for a numeric matrix; tree for a hierarchy; timeline for dated events; Gantt for task intervals; Braille for high-resolution coordinate plots.
3. Establish the mapping before rendering: scale bounds, units, time axis, category boundaries, or parent-child relationships.
4. Preserve exact values and labels in a nearby text list or table. Glyphs are approximations, not the authoritative data.
5. Render in a fenced code block or HTML `pre` using a monospace font. Escape untrusted text in HTML.
6. Verify mapping, alignment, labels, missing data, and the target renderer. If unavailable, disclose that only static checks ran.

## Character families and contracts

### Sparkline: `▁ ▂ ▃ ▄ ▅ ▆ ▇ █`

Requires at least two ordered numeric observations. Declare units and represented period. State scale bounds when interpretation or cross-series comparison depends on them. Use the same bounds for comparable series. Do not fill missing observations; represent gaps explicitly and explain the gap marker. The smallest glyph has visible height, so a zero observation is not a blank cell. Retain the final value and exact source series nearby.

### Heatmap: `░ ▒ ▓ █`

Requires row labels, column labels, numeric cells, and an explicit mapping to ordered intensity bands. Define boundaries without overlap or gaps, including boundary inclusion. Use the same mapping across the matrix. Missing is not the lowest band: use a distinct marker such as `?` with a legend. Include exact cell values in a companion table. Shading encodes magnitude, not good/bad status unless a supplied rule establishes that meaning.

### Hierarchy: `├ └ │ ─`

Requires explicit parent-child relationships. Preserve names and sibling order unless sorting is requested. Show each child beneath its actual parent. Detect cycles; a cyclic relationship is a graph, not a tree, and must not be silently converted. For multiple parents, use a relationship list or an explicitly labeled duplicated reference. Provide an ASCII fallback using `+`, `|`, and `-`.

### Timeline: `● ◆ ─`

Requires dated events and a declared axis. Distinguish event markers from milestones through a legend. If positions encode elapsed time, use proportional spacing from actual timestamps and state resolution. If spacing is merely sequential, label it "event order, not proportional time". Do not infer dates from equal visual spacing.

### Gantt: `█` with a shared time grid

Requires a start and end for every task, axis origin, time unit, and boundary convention. Prefer half-open intervals `[start, end)` and state that convention. Render every task on the same grid; label coarsening or rounding when intervals do not align with cells. Do not invent dependencies or completion percentages. A zero-duration milestone is a distinct marker, not a filled duration cell.

### Braille: `U+2800–U+28FF`

Use only with an available reviewed encoder and real coordinate or signal data. Each cell represents a 2-column by 4-row dot matrix. Standard bit positions by row are `(1,4)`, `(2,5)`, `(3,6)`, `(7,8)`; the code point is `U+2800` plus the selected dot bit mask. Require explicit axes, bounds, sample-to-pixel mapping, and clipping policy. Do not concatenate decorative Braille characters and call them a measured plot. If no encoder is available, use a numeric table or simpler chart; this package supplies no Braille renderer.

## Layout aids and non-chart symbols

- Rounded frames: `╭ ╮ ╰ ╯`; dashed lines: `┄ ┅ ┈ ┉`. Use only when they clarify grouping, not as data or status. Keep line styles consistent and check column width.
- Relationship arrows: `← → ↑ ↓ ↗ ↘`. Require a stated edge meaning; an arrow must not imply causality unless established.
- Geometric nodes: `◆ ◇ ■ □ ▪ ▫`; dot markers: `● ○ ◉ ◌`. Define every relevant distinction in a legend. Filled/empty does not automatically mean active/inactive, success/failure, or complete/incomplete.
- Ratings/dot plots require a defined discrete denominator and exact value. For a simple filled-slot magnitude use `monospace-data-bars`; for coordinates use a reviewed plotting algorithm.
- Status symbols `✓ ✗ ⚠ ℹ` are annotations, not chart algorithms. Pair with an explicit state word and supplied meaning.

## Compatibility and accessibility

- Unicode coverage, fallback fonts, and cell width differ across terminals, browsers, and PDF exporters. Monospace alone does not prove alignment.
- Use ASCII if Unicode is unsupported or glyph widths fail the destination test.
- Keep labels, units, dates, scale, and a textual equivalent; color must not carry essential information.
- Do not add decorative borders, rounded frames, emoji, or separators that obscure structure.
- For HTML, allow horizontal scrolling within wide chart blocks without overflowing the whole page.

## Acceptance gate

- Every displayed observation, interval, event, and relationship traces to the supplied input.
- Scale and legends are explicit where required; comparison groups share mappings.
- Missing and zero remain distinct.
- Exact values or a text equivalent remain available.
- No invented causal, status, or favorable-direction interpretation appears.
- The output is legible at target width, or the rendering limitation is disclosed.

## Package boundaries

This is an instruction-only package. It does not provide chart generation scripts, statistical analysis, monitoring thresholds, a Braille encoder, or proof of cross-platform rendering. Read [the synthetic examples](references/EXAMPLES.md) for mapping fixtures, not operational data.
