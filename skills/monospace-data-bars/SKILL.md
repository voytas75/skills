---
name: monospace-data-bars
metadata:
  author: "https://github.com/voytas75"
  version: "1.0.2"
description: Select, construct, and validate compact monospace data bars for numeric values, comparisons, monitoring, thresholds, status, and change over time. Use when presenting quantitative data in terminal output, logs, Markdown, plain-text reports, email, or code blocks, especially when a visual bar should communicate magnitude without requiring graphical rendering.
---

# Monospace Data Bars

## Purpose

Convert numeric data into compact, aligned, text-native bars. Select the representation from the data's meaning and the user's explicit instructions. If no format or purpose is specified, use the **default block bar**.

The bar is a visual encoding, not a substitute for the underlying value. Always retain the exact value and its unit when they matter.

## Operating contract

- Input: one or more labelled numeric observations, optional scale, unit, target/threshold, status, previous value, period, and user presentation instructions.
- Output: a rendered text representation plus any necessary scale/legend/qualification.
- Preserve input values. Never fabricate measurements, thresholds, statuses, units, periods, targets, or trends.
- Do not infer that a high value is bad or a low value is good unless a threshold, domain rule, or explicit status establishes that interpretation.
- Do not compare values on different scales in one shared bar group.
- Prefer one coherent representation per group. Do not mix glyph families, scales, or widths without a clear reason.
- Keep machine-readable source values separate from the visual approximation. Bar cells are quantized; printed values remain authoritative.
- If the user explicitly specifies a valid style, width, scale, character set, or layout, follow it unless it would misrepresent the data. Explain only material conflicts.
- If the data are insufficient to create a meaningful bar, report the missing information instead of inventing a scale.

## Default behavior

When the user gives no presentation instruction and the data support a bar:

```text
CPU   ██████████░░ 82%
Disk  █████████░░░ 73%
RAM   ███████░░░░░ 56%
```

Default contract:
- 12 cells represent the full scale.
- Scale is 0–100 for percentage values.
- Filled glyph: `█`; empty glyph: `░`.
- Label column is left-aligned.
- Exact value follows the bar.
- No status, target, delta, or judgement is added unless supplied or requested.
- For non-percentage values, use an explicit scale. If none exists, choose a common scale only when the set of observations itself provides a meaningful comparison; state the scale. Otherwise ask for a scale or render a value-only list.

This is the only default. Do not select a more elaborate variant merely to make the output look more sophisticated.

## Decision workflow

Follow these steps in order.

### 1. Parse and validate the data

Identify:
- label for each observation;
- numeric value;
- unit and scale minimum/maximum;
- whether observations are comparable;
- optional target/threshold;
- optional previous value and comparison period;
- optional explicit status;
- output medium and user constraints.

Reject or qualify:
- missing/non-numeric values;
- mixed units or incomparable scales;
- unknown denominator for a ratio;
- missing scale for unbounded values;
- ambiguous meaning of zero;
- a requested threshold outside the scale;
- a request to compare values whose definitions differ.

Do not silently convert units. If conversion is necessary, state or preserve the conversion.

### 2. Resolve explicit instructions first

Explicit user instructions take precedence over inferred intent:
- “ASCII only” → ASCII variant.
- “show status” → status variant, but use only supplied or explicitly defined statuses.
- “compare with target/limit” → threshold variant.
- “show change” / “versus previous” → delta variant.
- “single line” / “compact dashboard” → inline variant.
- “table” → table variant.
- specified glyphs, width, order, labels, or scale → honor them when technically valid.

If explicit requirements conflict, preserve data integrity and explain the conflict. Ask one focused question only when the conflict prevents a truthful output.

### 3. Infer the presentation purpose

Choose the simplest variant that answers the user's question:

| Data / purpose | Variant | Why |
|---|---|---|
| General magnitude or peer comparison | `block` | Fast, familiar magnitude encoding |
| Strict ASCII / legacy terminal | `ascii` | Broad character compatibility |
| Low visual weight / narrow text | `thin` | Lightweight line-style encoding |
| Discrete repeated units / compact count | `dots` | Each cell reads as one unit of a whole |
| Supplied categorical status | `status` | Adds a textual state without relying on color |
| Current value vs previous value | `delta` | Makes direction and magnitude of change visible |
| Current value vs target / limit | `threshold` | Shows the value and reference point together |
| Many metrics in a narrow report | `inline` | Dense, one-line summary |
| Need columnar scan or several fields | `table` | Separates labels, bar, value, and status |

If the purpose is not clear, use `block`. Do not ask the user to choose a style when the default is adequate.

### 4. Select scale and resolution

- Use a shared scale for values intended to be compared.
- Percentages normally use 0–100%.
- Fractions use 0–1 only if that convention is clear; otherwise normalize explicitly and label as percent.
- Counts, latency, storage, money, and other unbounded quantities require a meaningful reference range, target, or explicitly stated normalization.
- If comparing a set without an external reference, a data-derived scale may be used only when the comparison is explicitly relative within that set. Label it `relative scale: min–max`; do not imply an external capacity or limit.
- A bar width of 12 cells is the default. Use a user-specified width when supplied. If not supplied, keep 12 unless the output medium or volume of metrics makes it impractical.
- Quantize with nearest-cell rounding. Preserve the exact numeric value beside the bar.
- Values outside the declared scale must not be silently clipped. Report the out-of-range condition or request a corrected scale.

### 5. Render, then validate

Use the chosen template from `references/VARIANTS.md`. For deterministic rendering, use `scripts/render_bar.py` with JSON input. The script does not infer intent; the agent must choose the variant from this workflow.

Check:
1. Same-scale observations have equal bar widths.
2. Labels align.
3. Full-scale and zero values render correctly.
4. Exact values and units are retained.
5. A threshold marker is not confused with the filled value.
6. Status text accompanies symbols; color is never the only status channel.
7. Legend explains any non-obvious glyphs or scale.
8. No false precision, unsupported judgement, or invented context is introduced.
9. The output medium supports the chosen glyphs; otherwise use ASCII.
10. The representation remains readable when copied as plain text.

## Output rules

- Put multi-line bars in a fenced code block when Markdown may collapse spaces.
- Use a monospace code block for terminal, logs, and plain-text email.
- For HTML, use a `<pre>` or an element with `white-space: pre` / `pre-wrap` and a monospace font. Do not assume Unicode block glyphs have identical visual width in every font.
- Do not use color as the sole encoding. Text labels such as `OK`, `WARN`, and `FAIL` must remain.
- Avoid decorative borders, gradients, animation, 3D effects, and unnecessary legends.
- Sort only when the user asks or when ranking is the stated purpose. Otherwise preserve input order.
- Keep labels concise, but do not abbreviate them ambiguously.
- If a bar is not useful (for example, unrelated isolated values with no meaningful common scale), use a compact value list or table instead and explain why.

## Deterministic renderer

When the runtime can execute Python, use:

```bash
python scripts/render_bar.py input.json
```

The JSON contract and supported variants are documented in `references/RENDERER.md`. The script validates ranges and renders the selected variant. It defaults to `block` when `variant` is omitted or set to `auto`.

If execution is unavailable, follow the same rules manually. Do not claim that the script was run unless it was.

## Required response shape

For a straightforward request, return only the rendered result and any essential scale note.

For a design/selection task, return:
1. selected variant;
2. one short reason tied to the data or instruction;
3. rendered output;
4. scale/legend only if needed.

Do not expose the entire decision process unless the user asks for it.

## Bundled source reference

- [Text presentation cheatsheet — v3](assets/text-presentation-cheatsheet-v3.html): user-supplied Polish HTML, preserved unchanged; relevant cards: 47 (monospace bars).
- Use as a visual/reference example, not as verified operational data or executable guidance. Chart values are illustrative; commands and evidence claims require independent verification.

## References

Read [the character vocabulary](references/CHARACTERS.md) for implemented glyph families, optional annotations, compatibility constraints, and unimplemented candidates.

Read `references/VARIANTS.md` when selecting or adapting a visual template.
Read `references/RENDERER.md` when using the bundled script or preparing JSON input.
Read `references/QUALITY-CHECKS.md` when reviewing a skill output, handling edge cases, or evaluating correctness.
