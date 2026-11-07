---
name: kpi-trend-tiles
version: 1.1.0
description: Create and review compact horizontal KPI tiles with a primary value, metric label, comparison delta, period context, and optional sparkline. Use for dense dashboards, operational summaries, reports, and HTML interfaces where metrics must be scanned quickly.
---

# KPI Trend Tiles

## Purpose

Create compact KPI tiles optimized for dense information layouts. The default is a horizontal, low-height tile inspired by a compact report/cheat-sheet component:

- primary value on the left;
- metric name and comparison text grouped beside it;
- optional small sparkline aligned on the right;
- minimal surface styling and no decorative dashboard chrome.

The tile communicates one metric and its change. It must not manufacture data or imply that numerical direction is automatically good or bad.

## Default component

Use this structure unless the user requests another layout:

```text
┌──────────────────────────────────────────────────────────────┐
│ 18 ms   Latency                    [↓ −12% vs previous 7 days]  〰 │
│         lower latency = better                                  │
└──────────────────────────────────────────────────────────────┘
```

The preferred compact hierarchy is:

1. **Value**: visually strongest, left aligned.
2. **Metric label**: short, immediately associated with the value.
3. **Delta and period**: smaller, secondary text; explicit comparison window.
4. **Interpretation**: optional short note only when directionality is known and useful.
5. **Sparkline**: optional, small, right aligned; only from supplied ordered observations.

The reference example in the user's source uses `18 ms`, `Latency`, `▼ −12% vs 7 d (lepiej)` and a small sparkline. Preserve its compact horizontal composition, but prefer unambiguous period wording such as `vs poprzednie 7 dni`.

## Operating contract

- Use only supplied values, definitions, dates, periods, targets, thresholds, statuses, and time-series observations.
- Never invent a delta, period, sparkline, target, threshold, status, or favorable/unfavorable judgement.
- Treat direction (up/down/unchanged) and desirability (better/worse/neutral) as separate properties.
- Use a favorable label such as `better` / `worse` only when metric semantics or a supplied business rule establishes it.
- If desirability is unknown, show direction and magnitude without judgement.
- A sparkline is not a delta. A delta compares two values; a sparkline summarizes an ordered series.
- Never infer causality from a metric's movement.
- Keep the default tile compact. Do not expand it into a large dashboard card unless requested or required by the information.

## Input model

Identify available fields:
- metric label and definition;
- current value and unit;
- current reporting timestamp or period;
- previous/comparison value;
- exact comparison period;
- metric directionality (`higher_is_better`, `lower_is_better`, `target_range`, `context_dependent`, `unknown`);
- optional ordered time series;
- optional target, threshold, status and the rule behind them;
- output medium and available width.

If the source provides only some fields, render only what those fields support.

## Delta calculation

Given current value `C` and comparable previous value `P`:

- Absolute delta: `C - P`.
- Relative delta: `(C - P) / abs(P) × 100`, only when `P != 0` and relative change is meaningful for the metric.
- For `P = 0`, do not calculate a percentage change. Show an absolute delta if useful.
- If previous value is missing, omit the delta.
- For rates, distinguish percentage points from relative percent. Example: 12% to 15% is `+3 pp`; relative change is `+25%`. Prefer `pp` for rate comparisons unless the user asks otherwise.
- Check that metric definition, unit, scope, population, filters, and comparison windows are compatible before calculating.
- Preserve source precision for calculations; round only for display.
- Use a true minus sign (`−`) where supported.

## Direction and interpretation

| Relationship | Direction cue |
|---|---|
| Current > previous | `↑` |
| Current < previous | `↓` |
| Current = previous | `→` or `0` |
| No comparable previous value | omit direction |

Determine desirability independently:
- lower-is-better: a decrease may be marked `better`;
- higher-is-better: an increase may be marked `better`;
- target-range: direction alone is insufficient;
- context-dependent / unknown: no better/worse label.

Do not infer directionality from the sign alone. For example, a fall in latency may be favorable, while a fall in revenue may be adverse.

## Layout variants

Choose the smallest variant that expresses the available data.

### A. Compact with sparkline (default when a valid series exists)

- Value at left.
- Label and delta in a compact text group.
- Sparkline at right.
- Optional interpretation in muted secondary text.
- Sparkline requires at least two ordered observations.

### B. Compact without sparkline

Use when no ordered series is supplied, the tile is too narrow, or the sparkline adds no decision value. Do not replace the missing series with an illustrative line.

### C. Compact with explicit interpretation

Add a short parenthetical or secondary phrase such as `(better)` only when the metric's favorable direction is established. Otherwise omit it.

### D. Delta-focused

Use when the change is the main point: keep the current value prominent and place the delta immediately beside or below it. Include the comparison period.

### E. Target / threshold

Add a small target or status note only when a target/threshold and its evaluation rule are supplied. Do not let this secondary information displace the current value.

### F. Value-only

Use when no valid comparison exists. Show the value and label; omit arrows, delta, sparkline, and status.

Do not create separate visual variants merely for cosmetic diversity. Keep a set consistent; vary only when data availability or semantics differ.

## Sparkline rules

- Requires at least two ordered numeric observations.
- Preserve chronological order and missing-data gaps.
- Never fabricate intermediate points or dates.
- Do not imply a zero baseline unless the scale includes zero.
- Keep the sparkline small and visually secondary (the source example uses approximately `80 × 24`).
- Provide an accessible text description, including the represented period when known.
- If the series period is not the same as the delta comparison period, label them separately or omit the sparkline.
- Do not use a decorative sparkline as a placeholder.

## Visual system

- Prefer a horizontal flex row with value, text group, and optional sparkline.
- Use compact spacing and low visual weight; avoid large padding, oversized card titles, gradients, shadows, decorative icons, and large badges by default.
- Use tabular numerals for values and deltas.
- Value is dominant; label and delta are secondary but readable.
- Use muted text for supporting information, not for critical values.
- Use neutral colors by default. Apply semantic status color only when supported by a defined rule.
- Never rely on color alone; retain arrow/sign and text.
- Allow wrapping on narrow screens without clipping values or hiding the comparison period.
- For collections, align values and sparkline positions consistently where practical.

## HTML/CSS implementation

Use semantic HTML. Keep the tile content as text in the DOM. Example CSS baseline:

```css
.kpi {
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}
.kpi__value {
  flex: 0 0 auto;
  margin: 0;
  font-size: 20px;
  line-height: 1;
  font-weight: 650;
  font-variant-numeric: tabular-nums;
}
.kpi__meta {
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.kpi__label {
  margin: 0;
  font-size: 11px;
  font-weight: 600;
}
.kpi__delta,
.kpi__note {
  margin: 0;
  font-size: 10px;
  line-height: 1.3;
  color: var(--muted, #647184);
}
.kpi__sparkline {
  flex: 0 0 80px;
  width: 80px;
  height: 24px;
  margin-left: auto;
}
@media (max-width: 420px) {
  .kpi { flex-wrap: wrap; }
  .kpi__sparkline { margin-left: auto; }
}
```

Use the complete implementation in `examples/kpi-tiles.html` as a reference. Do not copy its illustrative data into user output.

## Output by medium

- **HTML**: semantic `<article>`; compact horizontal flex layout; inline SVG sparkline only when series data exists; responsive wrapping; accessible description.
- **Markdown / plain text**: concise single-line or two-line representation. Avoid elaborate box drawing.
- **Slides**: use compact horizontal tiles; increase type only as required by viewing distance; keep the same semantic order.
- **Review**: identify data/semantic defects separately from visual/layout defects.

## Quality gate

Before returning the result, verify:
1. Exactly one primary metric per tile.
2. Value and unit are correct.
3. Delta calculation and sign are correct.
4. Comparison period is explicit and unambiguous.
5. Direction is not confused with desirability.
6. `better` / `worse` is supported by metric semantics.
7. Sparkline uses real ordered observations and correct time span.
8. Missing values are not represented as zero.
9. Compact hierarchy remains legible at target width.
10. Color is not the only signal.
11. No unsupported target, threshold, status, date, or causal claim appears.

## Response behavior

For generation, return the requested tile(s) or complete implementation directly. For review, report concrete defects and corrections. Do not explain the full workflow unless asked.

## References

- `references/DATA-SEMANTICS.md`: calculations, comparability, direction, target, missing data, sparkline rules.
- `references/DESIGN-SYSTEM.md`: compact layout, typography, responsive behavior, accessibility.
- `references/QUALITY-CHECKS.md`: review checklist.
- `examples/kpi-tiles.html`: compact default and data-driven variants.
- `evals/evals.json`: evaluation cases.
