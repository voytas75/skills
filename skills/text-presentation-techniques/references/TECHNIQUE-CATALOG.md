# Technique Catalog

The catalog preserves the 47 techniques and their core use conditions from the supplied HTML reference. Examples below are schematic; technical commands and product UI paths must be verified before production use.

## Category: Conciseness

### 01. Definition → one sentence
**Use:** define a term with its function and scope in one sentence.
**Pattern:** `Term — signals/inputs → decision or function.`
**Limit:** retain the scope; do not compress away what the term governs.

### 02. Telegraphic syntax
**Use:** concise operational statements.
**Pattern:** `Restore: restart service → verify: Running.`
**Limit:** retain executor, condition, and success criterion where they matter.

### 10. Shared context once
**Use:** several items share one unambiguous scope.
**Pattern:** state the scope in a heading, then list common properties.
**Limit:** the heading must cover every item; do not let scope silently drift.

### 11. Cross-reference instead of repetition
**Use:** repeated prerequisites, definitions, or controls.
**Pattern:** `PRE-01` points to a single existing prerequisite block.
**Limit:** reference must resolve to an existing, easy-to-find item.

### 12. Abbreviation + legend
**Use:** repeated domain terminology.
**Pattern:** define the abbreviation at first use, then use it consistently.
**Limit:** no ad hoc abbreviations; do not assume all readers know the acronym.

### 13. Relation symbols
**Use:** compact logical or dependency expressions for a technically fluent audience.
**Pattern:** `A ⇐ (B ∧ C) ∨ D`.
**Limit:** define symbols; use only when the audience can decode the notation.

### 28. Footnotes instead of parenthetical overload
**Use:** preserve a readable main sentence while moving secondary explanations directly below the block.
**Limit:** keep notes close to the text; do not force readers to search at the end of a long document.

## Category: Flow

### 03. Procedure → verb + object
**Use:** ordered operational steps.
**Pattern:** `sign-in logs → applied policy → failed condition`.
**Limit:** order must be unambiguous; terse chains assume familiarity with terms.

### 07. Decision tree
**Use:** a condition changes the next action or path.
**Pattern:** condition with explicit yes/no branches.
**Limit:** include all material branches and terminal outcomes.

### 08. State transitions
**Use:** lifecycle and state changes.
**Pattern:** `Pending --approve--> Active`.
**Limit:** add transition conditions when not obvious.

### 09. Causal chain
**Use:** explain a known mechanism from cause to effect and action.
**Pattern:** `expired certificate → TLS validation failure → connection rejected ⇒ renew + retest`.
**Limit:** correlation is not causation; use only when the causal mechanism is established.

### 18. Timeline
**Use:** actions, propagation, events, or checks where elapsed time matters.
**Pattern:** `T0 policy · +5 min propagation · +15 min test`.
**Limit:** do not add timestamps or durations without evidence.

### 19. Frontloading
**Use:** put the result, status, or required action first.
**Pattern:** `DENIED. Cause: ... Action: ...`
**Limit:** do not omit security-critical context or caveats.

### 23. Navigation path
**Use:** show a route through a UI, menu, or hierarchy.
**Pattern:** `Start › Section › Subsection › Item`.
**Limit:** first element must identify the starting point; UI names can change and need version/context verification.

## Category: Structure

### 04. Parameters → label: value
**Use:** present configuration or attributes as compact labeled pairs.
**Limit:** labels should be shorter than values; preserve exceptions.

### 05. Comparison → table
**Use:** compare entities with the same attributes.
**Limit:** for one or two facts, a sentence may be shorter and clearer.

### 06. Dependency matrix
**Use:** compare permissions, capabilities, or relationships across roles and dimensions.
**Limit:** provide a legend for check, dash, or other symbols.

### 17. Semantic grouping
**Use:** group related fields under meaningful headings to improve retrieval.
**Limit:** grouping optimizes findability, not necessarily character count; the result may be longer.

### 29. Hierarchical numbering
**Use:** create stable references to sections and subsections.
**Pattern:** `1`, `1.1`, `1.2`, `2`, `2.1`.
**Limit:** use no more than two or three levels unless necessary.

## Category: Numbers and status

### 14. Aggregation
**Use:** summarize a distribution when individual records are not required.
**Pattern:** sample size, median, range, outliers.
**Limit:** do not aggregate when the underlying records are needed; consider median when outliers distort the mean.

### 15. Unit normalization
**Use:** compare values in a common unit and consistent precision.
**Limit:** state the unit, use the same unit across the series, and keep precision consistent.

### 16. Sparkline
**Use:** compactly show the shape of a time series.
**Limit:** it shows shape, not exact values; state period and final value. Do not fabricate points.

### 25. Stateful checklist
**Use:** track completion of prerequisites or operational steps.
**Pattern:** checked/unchecked items followed by an explicit completion criterion.
**Limit:** define what “done” means; verify that symbols render correctly in the target medium.

### 26. Status: symbol + word
**Use:** compact status reporting.
**Pattern:** `● OK`, `▲ WARN`, `✖ FAIL`, `○ N/A`.
**Limit:** do not encode status using color alone.

### 27. Thresholds and ranges
**Use:** classify values using explicit ranges.
**Limit:** ranges must be mutually exclusive and cover the intended scale; thresholds must come from the actual environment or policy.

### 31. Right-aligned numbers
**Use:** compare numeric columns.
**Limit:** unit in header where shared; align numeric values consistently; use fixed precision.

### 32. Recommended-option marker
**Use:** distinguish one recommended/default choice in a comparison.
**Limit:** one marker per list and a mandatory legend; the recommendation basis must be known.

### 34. Choose a mini-chart for the question
- Trend over time → sparkline or line.
- Compare categories → sorted bars.
- Part-to-whole → waffle or 100% bar.
- Distribution/outliers → min–median–max or distribution plot.
- Result versus target → bullet graph.
- State over time → status strip.
- Change between two points → slopegraph.
- Two dimensions → heatmap with numeric labels.

**Limit:** one analytical question per chart; avoid 3D and decoration.

### 35. Sparkline with markers
**Use:** show series shape and selectively mark min/max/final point.
**Limit:** state period and unit; identify only meaningful points; show final numeric value in text.

### 36. Sparkbar (mini columns)
**Use:** compact trend across discrete periods or categories.
**Limit:** baseline starts at zero; accent only one bar when emphasis is needed.

### 37. Small multiples (shared scale)
**Use:** compare several related series in repeated small charts.
**Limit:** same axes and scale across all charts; use accent only for the relevant deviation.

### 38. Direct-labeled bars
**Use:** compare a small set of categories without a separate legend.
**Limit:** sort bars where ranking matters; label category and value; use a zero baseline for bars.

### 39. Bullet graph (result vs target)
**Use:** show one measure against a target and optional performance bands.
**Limit:** target is a marker; bands require explicit definitions and legend.

### 40. Min–median–max range
**Use:** summarize a distribution and expose outliers.
**Limit:** include numeric summary alongside the visual; do not imply a distribution from insufficient observations.

### 41. Slopegraph (A → B)
**Use:** show change between exactly two time points or states across entities.
**Limit:** label both ends; use a consistent scale and units.

### 42. Heatmap with numbers
**Use:** reveal patterns across two dimensions.
**Limit:** include the numeric values in cells; one coherent color scale; color is not the sole carrier.

### 43. Status strip over time
**Use:** show status intervals along a time axis.
**Limit:** label the axis and status intervals; use symbols or text for anomalies and provide a legend.

### 44. Chart annotation
**Use:** attach an event or explanation to a meaningful point.
**Limit:** annotate only events relevant to interpretation or decision; do not imply causation without evidence.

### 45. Waffle 10×10 (part-to-whole)
**Use:** show a simple proportion with a visible denominator.
**Limit:** denominator must be explicit; provide exact value or percentage when precision matters.

### 46. KPI tile with trend
**Use:** combine current value, metric label, comparison delta/period, and optional sparkline in a compact horizontal tile.
**Limit:** say whether the direction is favorable or unfavorable only when metric semantics support that judgement. Keep the period explicit; do not draw a sparkline without real series data.

### 47. Monospace text bar
**Use:** show approximate relative magnitudes in terminal output, logs, or plain-text messages.
**Pattern:** fixed-width bar with a consistent scale, e.g. 12 cells = 100%.
**Limit:** define scale; align labels; use a monospace font; do not use as a substitute for exact numeric values.

## Category: Commands and code

### 20. Description → pipeline
**Use:** replace a prose description with an executable command pipeline for readers who know the command language.
**Limit:** command syntax must be tested; code is not self-explanatory for an unfamiliar audience.

### 21. Syntax notation
**Use:** document command parameters and allowed alternatives.
**Conventions:** `<x>` required; `[x]` optional; `{a | b}` one choice; `…` repeatable.
**Limit:** define notation once and use it consistently.

### 22. Task → command index
**Use:** map user-language tasks to exact commands.
**Limit:** task labels should match how the reader searches; commands need environment/version verification.

### 24. Keyboard shortcuts
**Use:** distinguish key combinations visually from the action description.
**Pattern:** keycaps followed by the action.
**Limit:** use platform-correct shortcuts and distinguish keys from prose.

### 30. Code → meaning (monospace)
**Use:** align codes, event IDs, error numbers, or identifiers with short explanations.
**Limit:** fixed-width code column; sort by code or frequency.

### 33. Command + expected output
**Use:** pair an executable command with the decisive success/failure evidence.
**Limit:** distinguish input from output; show only output lines relevant to validation; do not invent expected results.

## Cross-cutting rules

- A technique may belong to more than one practical workflow, but keep one dominant category in a categorized reference sheet.
- Do not use a chart if a table or sentence answers the question more accurately.
- Do not use color to compensate for weak labels or unclear hierarchy.
- Do not let visual compression conceal uncertainty, exceptions, or missing data.
- Treat all numerical examples in the source sheet as illustrative, not live operational facts.
