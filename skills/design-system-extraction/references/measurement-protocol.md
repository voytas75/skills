# Measurement Protocol

This reference defines the common contract for quantitative website and content-density measurements. Apply it whenever results will be compared, ranked, aggregated, or used to support a quantitative claim.

## 1. Measurement contract

Define this before collecting data:

| Field | Required definition |
|---|---|
| `metric_id` | Stable metric name |
| `unit_name` | What one counted unit represents |
| `unit_selector` | Selector identifying candidate units |
| `title_selector` | Selector identifying titles, if counted separately |
| `include_rule` | Conditions for inclusion |
| `exclude_rule` | Conditions for exclusion |
| `visibility_rule` | Exact visibility and containment conditions |
| `viewport` | Width and height in CSS pixels |
| `content_region` | Element/selector and measured bounds |
| `scroll_position` | Exact scroll offset or named position |
| `theme_state` | Theme and interaction state |
| `denominator` | Viewport, content area, or another explicit base |
| `formula` | Exact calculation |

A missing field makes the metric non-comparable. Record `not_available` rather than guessing.

## 2. Unit definitions

Do not combine these counts:

- `title_count`: qualifying titles visible in the measurement region.
- `complete_item_count`: complete content units fully visible in the region.
- `text_word_count`: words within the defined units.
- `text_character_count`: characters within the defined units, with whitespace policy stated.
- `content_area_css_px`: width × height of the defined content region.
- `content_density`: a declared count divided by a declared denominator.

A title is not a complete item. A complete item must satisfy a site/task-specific completeness rule declared before measurement (for example, title plus required metadata and summary/body fields). Do not invent a universal definition of "complete".

## 3. Visibility and completeness

An element qualifies as rendered only when:
- it exists in the current document;
- it is not `display:none` or `visibility:hidden/collapse`;
- its effective opacity is greater than zero;
- its rendered bounding box has non-zero width and height;
- it is not an empty placeholder or a zero-size anchor.

For **fully visible** counts, require the element's relevant bounding box to be wholly contained within the declared measurement region and viewport. Exclude content obscured by overlays or clipped by an ancestor. For text completeness, also check for line clamping, ellipsis, clipping, or truncation. If full text cannot be verified, do not count it as a complete item.

Record separately:
- `matched_count`;
- `rendered_nonempty_count`;
- `fully_visible_count`;
- `complete_item_count`.

Do not substitute the first selector match when it fails. A missing valid match is `not_found`.

## 4. Sampling and representative elements

For repeated component families:
- inspect at least three distinct valid instances when available;
- include a multi-line/wrapped title or content case when one exists;
- record total selector matches and valid sample count;
- retain per-instance measurements where variation matters.

If fewer than three valid instances exist, record the actual count and restrict conclusions to those observed instances. A single element cannot establish a family-wide rule.

## 5. Density calculations

Choose one denominator and state it explicitly. Examples:

- `titles_per_viewport = title_count / 1 viewport`
- `complete_items_per_100k_css_px = complete_item_count / content_area_css_px * 100000`
- `words_per_100k_css_px = text_word_count / content_area_css_px * 100000`

Do not mix denominators or formulas in one ranking. If a study uses a different formula, treat it as a different metric.

A higher title count does not establish more complete content, more useful information, or better information architecture. Interpret counts alongside complete items, text volume, content type, and task relevance.

## 6. Comparability gate

Two measurements may be compared quantitatively only when all of the following match:
- unit definition and selectors' semantic role;
- visibility and completeness rules;
- viewport dimensions;
- content-region definition;
- scroll position;
- theme and interaction state;
- denominator and formula;
- accepted readiness status.

If any differ, label the values `not_comparable`. Do not normalize away differences without a documented method.

## 7. Stability tolerances

Before measurement, define which properties must stabilize and their tolerances. Geometry, text, and styles can have different tolerances. Use exact equality for discrete state/URL checks; use a declared numeric tolerance for continuous dimensions and values. Record the two sample values and the comparison result.

Do not choose tolerances after seeing the result to make a sample pass.
