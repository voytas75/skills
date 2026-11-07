# Renderer JSON contract

Run:

```bash
python scripts/render_bar.py input.json
```

Or pipe JSON to standard input:

```bash
cat input.json | python scripts/render_bar.py -
```

## Schema

```json
{
  "variant": "block",
  "width": 12,
  "min": 0,
  "max": 100,
  "unit": "%",
  "format": "unicode",
  "items": [
    {"label": "CPU", "value": 82},
    {"label": "Disk", "value": 73},
    {"label": "RAM", "value": 56}
  ]
}
```

Required:
- `items`: non-empty array;
- each item: non-empty `label`, finite numeric `value`.

Optional top-level:
- `variant`: `auto`, `block`, `ascii`, `thin`, `dots`, `status`, `delta`, `threshold`, `inline`, `table`;
- `width`: integer 1–80; default 12;
- `min`, `max`: finite numeric scale bounds; default 0 and 100 only when `unit` is `%`; both are required for other units or unitless values;
- `unit`: text appended to values; default empty;
- `format`: `unicode` or `ascii`; default `unicode`.

Optional per item:
- `status`: supplied status string, used by `status` and `table`;
- `previous`: finite numeric previous value, used by `delta`;
- `period`: comparison period text, appended by `delta`;
- `threshold`: finite numeric target/threshold, used by `threshold`.

## Behavior

- `auto` or omitted variant resolves to `block`.
- Values, previous values, and thresholds outside `[min, max]` cause a validation error; they are not silently clipped.
- Cell count uses nearest-integer rounding: `floor(normalized × width + 0.5)`.
- Exact numeric values are printed without forced rounding. JSON integer values remain integers; decimal values use compact decimal formatting.
- `delta` prints absolute difference. If `unit` is `%`, it labels the difference `pp` (percentage points); otherwise it uses the unit. The renderer does not calculate relative percent change.
- `status` requires `status` for every item.
- `delta` requires `previous` for every item.
- `threshold` requires `threshold` for every item or a top-level `threshold`.
- `table` includes status only if every row supplies one.
- The script is deterministic and does not infer statuses, targets, scales, or intent.
