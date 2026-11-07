# KPI Data Semantics

## Minimum data model

```json
{
  "label": "Latency",
  "value": 18,
  "unit": "ms",
  "previous": 20.45,
  "comparison_period": "previous 7 days",
  "directionality": "lower_is_better",
  "series": [
    {"period": "day 1", "value": 25},
    {"period": "day 2", "value": 23},
    {"period": "day 3", "value": 22},
    {"period": "day 4", "value": 21},
    {"period": "day 5", "value": 20},
    {"period": "day 6", "value": 19},
    {"period": "day 7", "value": 18}
  ]
}
```

Illustrative schema only. Do not treat values or periods as facts.

## Delta

For current `C` and comparable previous `P`:

- Absolute delta: `C - P`.
- Relative delta: `(C - P) / abs(P) × 100`, only when `P != 0` and meaningful.
- If `P = 0`, relative percentage is undefined; show absolute change if useful.
- If `P` is missing, omit delta.
- Preserve source precision for calculation; round only for display.
- Name the comparison period explicitly. Prefer `vs previous 7 days` to `vs 7 d`.
- Do not call a change “growth” unless the metric supports that interpretation.

## Rates and percentage points

For a rate changing from 12% to 15%:
- absolute rate difference: `+3 percentage points` (`+3 pp`);
- relative change: `+25%`.

Prefer percentage points for rate comparisons unless relative change is explicitly requested. Never display `+3%` when the intended quantity is `+3 pp`.

## Comparability

Before calculating, verify same:
- metric definition;
- unit and scale;
- population and scope;
- filters and methodology;
- comparable reporting windows.

If not comparable, do not calculate the delta. Show the current value and state the limitation only if needed.

## Direction versus desirability

Direction is mathematical:
- `↑`: current > previous;
- `↓`: current < previous;
- `→`: unchanged.

Desirability is contextual:
- lower-is-better: a decrease may be favorable;
- higher-is-better: an increase may be favorable;
- target-range: assess distance to the defined range;
- context-dependent / unknown: no favorable/unfavorable judgement.

Use `better` / `worse` only when supported by an explicit objective or metric semantics. The arrow alone must not encode desirability.

## Target and threshold

- Include a target or threshold only when supplied.
- Show target and current value as distinct quantities.
- Status requires a defined rule and boundary behavior.
- Do not invent green/amber/red bands.
- Do not use “percent of target achieved” when the ratio is not meaningful.

## Missing and zero values

- Missing is not zero.
- Zero is a valid numeric value.
- Do not invent a previous value or fill gaps in a series.
- Mark partial/in-progress periods only when supplied.

## Sparkline

- Requires at least two ordered numeric observations.
- Preserve order and missing-data gaps.
- Do not interpolate without explicit instruction and justification.
- Do not imply a zero baseline unless present in the scale.
- A sparkline is a visual summary, not an exact delta.
- Label its time span when known.
- If sparkline and delta periods differ, distinguish them explicitly.
- Omit it when the series is absent or the tile is too small.

## Formatting

- Keep units attached to values: `18 ms`, `430 ms`, `4.8%`.
- Use consistent precision across comparable tiles.
- Use true minus sign `−` where supported.
- Do not use compact abbreviations such as `7 d` if the target audience may interpret them ambiguously.
