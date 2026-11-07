# Variant catalogue

All examples use illustrative values. Unless stated otherwise, the scale is 0–100%, width is 12 cells, and values are exact labels rather than estimates.

## 1. Block (default)

```text
CPU   ██████████░░ 82%
Disk  █████████░░░ 73%
RAM   ███████░░░░░ 56%
```

Use for ordinary magnitude and comparison. Filled `█`, empty `░`. Do not add status or target unless supported.

## 2. ASCII

```text
CPU   [##########..] 82%
Disk  [#########...] 73%
RAM   [#######.....] 56%
```

Use when Unicode is unsupported, output is machine-constrained, or ASCII is explicitly requested. `#` = filled; `.` = empty.

## 3. Thin

```text
CPU   ━━━━━━━━━━── 82%
Disk  ━━━━━━━━━─── 73%
RAM   ━━━━━━━───── 56%
```

Use when a lighter visual weight is useful and the target font renders these glyphs consistently. Do not use if glyph-width uncertainty causes misalignment.

## 4. Dots

```text
CPU   ●●●●●●●●●●○○ 82%
Disk  ●●●●●●●●●○○○ 73%
RAM   ●●●●●●●○○○○○ 56%
```

Use for discrete units, repeated slots, or intentionally granular representations. Avoid for continuous measurements where dots imply countable objects.

## 5. Status

```text
CPU   ██████████░░ 82%  HIGH
Disk  █████████░░░ 73%  WARN
RAM   ███████░░░░░ 56%  OK
```

Use only when status values are supplied or derived from explicit thresholds/rules. A numeric value alone does not establish `HIGH`, `WARN`, or `OK`. Use text in addition to any symbol or color.

## 6. Delta

```text
CPU   ██████████░░ 82%  ▲ +12 pp
Disk  █████████░░░ 73%  ▼  -4 pp
RAM   ███████░░░░░ 56%  ─   0 pp
```

Use when a previous value is available and change is relevant. For percentages, distinguish percentage points (`pp`) from relative percent change (`%`). Use `pp` for simple subtraction of two percentage values. For relative change, calculate `(current - previous) / previous × 100`; if previous is zero, relative change is undefined. Always identify the comparison period when known.

## 7. Threshold / target marker

```text
Scale: 0–100%; marker = target 70%
CPU   ██████████│░░ 82%
Disk  █████████│░░░ 73%
RAM   ███████│░░░░░ 56%
```

The bar encodes the observed value; `│` marks the threshold/target. They are independent. For each row, the marker position is calculated from the same scale. If the target differs by row, state it per row or include it in the label. Do not label a target as a limit unless it is one.

## 8. Inline dashboard

```text
CPU ██████████░░ 82% │ DISK █████████░░░ 73% │ RAM ███████░░░░░ 56%
```

Use for compact one-line summaries. Keep metric labels and exact values. Use only when line length is acceptable for the destination; do not force this into narrow mobile or terminal widths.

## 9. Table

```text
RESOURCE  BAR           VALUE  STATUS
CPU       ██████████░░  82%    HIGH
Disk      █████████░░░  73%    WARN
RAM       ███████░░░░░  56%    OK
```

Use when several attributes must be scanned together or when table semantics matter. Status is optional and must be grounded.

## 10. Segmented bands (optional specialized pattern)

```text
CPU   ░░░░░░▓▓▓▓██ 82%
      LOW   WARN HIGH
```

Use only when band boundaries and meanings are explicitly defined. The example is schematic, not a universal encoding. Do not use this pattern to imply that the individual segments represent equal-value categories unless that is true.

## Selection notes

- `block` is the default and general-purpose choice.
- `ascii` is the compatibility choice, not a different semantic scale.
- `thin` and `dots` are stylistic alternatives; choose only when requested or when the medium/use case clearly benefits.
- `status`, `delta`, and `threshold` add meaning. Use them only when the required supporting data exists.
- `inline` and `table` change layout rather than the underlying measurement.
- Do not stack multiple variants (for example, threshold + delta + status) unless the user explicitly needs all of those dimensions and the result remains readable. Prefer a primary variant plus concise textual metadata.
