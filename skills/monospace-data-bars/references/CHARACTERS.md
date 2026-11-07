# Character vocabulary for magnitude bars

All numeric examples here are synthetic. A glyph does not establish a real status, target, or measurement.

## Implemented renderer families

- `block`: filled `█`, empty `░`.
- `ascii`: filled `#`, empty `.`; the CLI does not add brackets.
- `thin`: filled `━`, empty `─`.
- `dots`: filled `●`, empty `○`; use for discrete slots or explicitly labeled quantization, not an implied object count for continuous data.
- `threshold`: `│` is inserted at a boundary independently of observed fill; it adds one character to the bar's displayed length.

Synthetic input: 80%, width 10, scale 0–100%. Corresponding bars:

```text
block  ████████░░  80%
ascii  ########..  80%
thin   ━━━━━━━━──  80%
dots   ●●●●●●●●○○  80%
```

These examples demonstrate character selection, not four different measurements.

## Optional annotations, not automatically generated

- Direction: `▲`, `▼`, `↑`, `↓`, `→`. Pair with signed numeric change and the supplied comparison period. Direction is not desirability. The current delta CLI prints the signed absolute delta without an arrow.
- Status: `✓`, `✗`, `⚠`, `ℹ`. Retain an explicit state word and source-backed meaning, for example `⚠ WARN` only when WARN is supplied or defined by a supplied rule. `⚠ Gateway` alone does not explain a state.

## Candidate families, not implemented CLI variants

- Geometric bars: `■ □`.
- Alternative shading: `▓ ░`.
- Fractional horizontal fill: `▏ ▎ ▍ ▌ ▋ ▊ ▉ █`, from one eighth to a full cell.

Do not pass `geometric`, `shaded`, or `fractional` to the current renderer or claim that it supports them. Manual examples require the same scale and semantic checks as implemented variants. Fractional fill needs a defined rounding policy, full-cell padding, exact-value labels, and tests for zero, full scale, fractional boundaries, and out-of-range inputs before becoming an implemented variant. It improves glyph resolution, not measurement precision.

## Compatibility

Unicode block elements and several geometric symbols have East Asian Width `Ambiguous`; terminal settings and fallback fonts can change their cell width. Warning/information symbols can receive emoji presentation. Do not infer uniform width from character count or a monospace declaration alone. Verify glyph coverage and alignment in the destination; use ASCII if the destination fails. In HTML escape input, use `pre`, and allow local horizontal scrolling for wide output.

## Separate visualization families

Vertical blocks `▁…█`, heatmap shading, trees, timelines, Gantt charts, and Braille plots require other data models. Use a structured text-chart workflow rather than extending a magnitude bar cosmetically. Rounded boxes `╭╮╰╯`, dashed separators `┄┅┈┉`, and arrows in relationship diagrams are layout aids, not measurements.
