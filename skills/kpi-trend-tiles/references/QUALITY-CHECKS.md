# KPI Tile Quality Checks

## Data integrity
- [ ] Metric label and definition are clear.
- [ ] Current value and unit match the source.
- [ ] Previous value is comparable.
- [ ] Delta calculation and sign are correct.
- [ ] Comparison period is explicit.
- [ ] Percentage points are not confused with relative percent.
- [ ] Zero previous value is handled correctly.
- [ ] Missing data is not represented as zero.
- [ ] No unsupported target, threshold, status, or judgement is introduced.

## Trend integrity
- [ ] Direction is distinct from favorable/unfavorable meaning.
- [ ] Favorable interpretation has a defined basis.
- [ ] Sparkline uses at least two real ordered observations.
- [ ] Sparkline period matches or is distinguished from delta period.
- [ ] Missing intervals are preserved.
- [ ] No causal claim is inferred.

## Compact visual quality
- [ ] Value is the most prominent element.
- [ ] Label and delta form one readable text group.
- [ ] Optional sparkline is small and right-aligned.
- [ ] Layout is compact and horizontal by default.
- [ ] No unnecessary large card header, padding, badge, or decoration.
- [ ] Comparable tiles use consistent alignment and formatting.
- [ ] Narrow layouts wrap without clipping.
- [ ] Text remains legible at actual display size.
- [ ] Color is not the only signal.

## Output quality
- [ ] HTML is semantic and self-contained when requested.
- [ ] SVG sparkline has an accessible description.
- [ ] No unnecessary dependency is introduced.
- [ ] Example values are not copied as user facts.
