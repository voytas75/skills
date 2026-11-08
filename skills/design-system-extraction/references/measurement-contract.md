# Measurement contract

Before collecting a metric, declare its meaning and method.

## Required metric definition

- `metric_id`, `metric_type`, `unit`;
- element/selector/role definition;
- inclusion and exclusion rules;
- visibility and completeness rule;
- viewport, theme, state, scroll;
- acquisition method;
- `stability_tolerance`;
- `comparison_tolerance` when comparing source and target;
- evidence reference;
- aggregation rule, if any.

## Measurement families

- Geometry: x, y, width, height, center, alignment.
- Typography: declared family stack, resolved family where available, size, weight, line height, letter spacing.
- Color: original value, alpha, and compositing context.
- Spacing: margin, padding, gap.
- Components: count, visibility, semantic role, variant, state.
- Overflow: axis, scroll dimensions, clipping/scrolling behavior, affected element.
- Assets: fonts, images, SVGs, stylesheets.
- Responsive behavior: layout changes across declared viewports.

## Tolerance separation

`stability_tolerance` compares repeated reads of the same page/state. `comparison_tolerance` compares source and target. They are different fields and must not be copied into one another automatically.

Do not compare measurements with different contracts. Do not aggregate rejected samples.
