---
name: design-system-extraction
description: "Analyze and document the visual design system of an existing website or supplied interface materials. Use to inspect colors, typography, spacing, layout, components, responsive behavior, interaction states, motion, accessibility signals, and design tokens; compare pages or implementations; and produce evidence-based design documentation. Works with the agent's available browser, inspection, file, and image capabilities without requiring a dedicated extraction package."
metadata:
  version: "1.4.0"
  upstream-reference: "https://github.com/Manavarya09/design-extract"
---

# Design System Extraction

## Purpose

Analyze an existing website or supplied interface materials and produce an evidence-based description of its design system. Use capabilities already available in the agent's environment. Do not require, install, or assume `design-extract`, `designlang`, Node.js, npm, Playwright, Chromium, or any other dedicated extraction system.

The skill defines the analysis method, not a fixed toolchain. Discover which browser, DOM/CSS, screenshot, image, source-file, and local-file capabilities are actually available.

## Operating principles

1. **No mandatory package:** use capabilities already available; never install a dedicated extraction system just to execute this skill.
2. **Readiness before measurement:** reject samples that fail the readiness gate; do not downgrade invalid samples to low-confidence evidence.
3. **Comparable metrics:** define the unit, selector, visibility rule, viewport, region, and scroll position before collecting comparative measurements.
4. **Evidence first:** distinguish direct observations, interpretations, and unknowns.
5. **Scope honesty:** state which pages, viewports, themes, and states were actually inspected.
6. **Preserve source values:** retain original values and provenance before normalizing tokens.
7. **Respect access controls:** inspect only public pages or pages the user is authorized to access. Never bypass authentication, bot challenges, paywalls, or other restrictions.

## 1. Establish scope

Identify:
- target URL(s) or supplied files/screenshots;
- requested outcome (understanding, documentation, implementation, comparison, audit, or redesign reference);
- representative pages and components;
- relevant viewports and responsive states;
- themes and interaction states;
- desired deliverables and format.

If the URL or source material is missing, ask for it. If breadth is unspecified, begin with the landing page and a small representative sample; do not imply whole-site coverage.

For multi-page work, prioritize distinct page templates and shared patterns. Avoid exhaustive crawling unless requested or necessary.

## 2. Discover available inspection capabilities

Use only capabilities actually available:
- browser navigation and screenshots;
- DOM inspection and computed styles;
- accessibility tree or element metadata;
- page source, linked CSS, assets, SVG, and font files;
- user-provided screenshots, HTML, CSS, or design exports;
- local scripts or parsing tools already available.

Do not assume browser access exposes DOM or computed CSS. Do not assume screenshots reveal exact CSS values. If only visual inspection is available, label measurements as estimates.

Prefer direct evidence in this order when available:
1. computed styles and rendered DOM;
2. source CSS, design tokens, and linked assets;
3. screenshots at known viewport dimensions;
4. visual inference from rendered pages.

## 3. Measurement readiness gate

**No quantitative sample may be accepted until it passes every applicable readiness check.** Run this gate after navigation and again whenever the route, viewport, theme, scroll position, or interaction state changes.

### Required checks

1. **URL identity:** record requested URL and final URL. Confirm the final URL is the intended page or an expected redirect. Reject `about:blank`, browser error pages, unexpected login pages, and unrelated redirects.
2. **Expected content:** verify that the expected page landmark and task-relevant content are present. A non-empty document or generic body text is insufficient.
3. **Stylesheet readiness:** verify that applicable stylesheets have loaded and styles are applied. Where DOM access exists, inspect stylesheet/link load state and computed styles on representative elements. If CSS readiness cannot be established, reject CSS-derived measurements; screenshot-only visual observations may be separately reported as estimates.
4. **Render stability:** capture two consecutive samples of the selected elements. Compare their bounding boxes and task-relevant computed styles. The values must remain within tolerances declared before measurement. Do not use one universal tolerance for every property; define tolerances appropriate to the metric and record them.
5. **Obstruction and transition check:** ensure the measurement region is not in a loading, skeleton, transition, consent-overlay, error, or modal state that invalidates the requested measurement.

### Rejection behavior

If any required check fails:
- mark the sample `rejected`;
- record the failed condition and observed evidence;
- do not use it in counts, averages, rankings, token derivation, or comparisons;
- retry only after a meaningful corrective action, such as waiting for expected content or navigating to the correct page;
- if it still fails, report the measurement as unavailable.

Do not relabel a failed readiness check as merely `low confidence`. An invalid sample is not a weak sample; it is excluded.

Read `references/quality-gates.md` for the acceptance record and detailed checks.

## 4. Define the measurement contract

Before collecting any metric intended for comparison, define:
- metric name and purpose;
- unit of content and its selector;
- inclusion/exclusion rules;
- visibility and completeness criteria;
- viewport width and height in CSS pixels;
- measurement region and its bounds;
- scroll position or scroll offset;
- theme and interaction state;
- denominator and formula for density metrics.

Do not compare values produced under different contracts. If definitions differ, label results as non-comparable and do not produce a shared ranking.

For content-density studies, distinguish at minimum:
- `title_count`: visible qualifying titles;
- `complete_item_count`: fully visible qualifying content units;
- `text_count`: words or characters, if measured;
- `content_area`: measured content region;
- `content_density`: explicitly defined count per area or per viewport.

A higher title count is not evidence of more complete items or more information. Read `references/measurement-protocol.md` before quantitative density analysis.

## 5. Inspect the interface

### Visual foundations

Inspect:
- **Color:** backgrounds, surfaces, text, borders, accents, gradients, overlays, and theme variants.
- **Typography:** declared font stacks, resolved font, weight, size, line height, letter spacing, and hierarchy.
- **Spacing:** margins, padding, gaps, section spacing, and recurring scale.
- **Geometry:** content widths, grids, columns, alignment, radii, borders, shadows, layering, and local overflow.
- **Assets:** logos, icons, illustrations, imagery, and font sources.

Record exact values only when directly available from source or computed styles. For screenshot-only analysis, label measurements and color estimates as approximate.

Preserve local overflow behavior as a component-level property. Do not infer page-level overflow from one child or infer absence of overflow from the absence of a visible scrollbar. Record the affected element, axis, scroll dimensions, clipping/scrolling behavior, and viewport context when measurable.

Preserve font stacks in their declared order. Distinguish the CSS-declared family list from the font actually resolved/rendered for a particular text run. Do not collapse a fallback stack into a single font name.

Preserve alpha channels in color values. Do not convert translucent colors to opaque hex without recording the original alpha and compositing context. If a displayed color is sampled from a screenshot, identify it as a composited appearance rather than the source color.

### Components and representative elements

Identify recurring structures and their anatomy:
- navigation, headers, footers, sidebars;
- buttons, links, inputs, selects, checkboxes;
- cards, panels, dialogs, menus, tabs, accordions;
- tables, lists, alerts, badges, pagination;
- content sections and page templates.

Do not use the first selector match as the representative example by default. For each selected role:
1. count all selector matches;
2. filter for elements that are rendered, non-empty, and have a non-zero bounding box;
3. confirm the element has the intended semantic/visual role;
4. inspect multiple instances when the component repeats;
5. include a wrapping or multi-line example when available;
6. record the selected element's identity/provenance and why it qualifies.

Use at least three distinct instances when available for a repeated component family. If fewer exist, record the actual sample count and do not generalize beyond the observed instances. If no valid match exists, record `not_found`; do not silently substitute a different selector or element.

For repeated text elements, distinguish:
- element visibility;
- full containment in the measurement region;
- text completeness (not clipped, line-clamped, truncated, or ellipsized).

### Responsive behavior

Inspect at declared viewport dimensions. Record exact viewport width and height.

Look for:
- changes in navigation and content hierarchy;
- grid/column transitions;
- container width and spacing changes;
- typography scaling;
- hidden, reordered, or collapsed elements;
- local and page-level overflow;
- touch-target behavior.

Infer breakpoints only when supported by source CSS or observations close enough to bound the transition. Otherwise report the observed interval or mark the breakpoint unknown.

### Interaction and motion

Inspect only interactions that can be exercised safely:
- hover, focus, active, disabled, selected, expanded, and error states;
- menus, dialogs, tabs, accordions, forms, and navigation;
- transitions, animation duration, easing, stagger, and scroll effects.

Do not claim runtime behavior was inspected merely because a CSS selector exists. Do not perform consequential actions without explicit authorization.

### Accessibility signals

Where available, inspect semantic HTML, accessible names, keyboard focus, contrast pairs, labels, landmarks, heading hierarchy, alternative text, reduced-motion behavior, and visible focus indicators.

Report specific observed issues. Partial inspection is not a WCAG audit or certification.

## 6. Build an evidence ledger

For every material conclusion, classify it:
- **Observed:** directly read from DOM, computed style, source file, asset metadata, or measured screenshot.
- **Inferred:** interpretation supported by multiple observations but not explicitly declared.
- **Unknown:** unavailable, ambiguous, inaccessible, or not inspected.

Maintain provenance:
- page/route and requested/final URL;
- timestamp;
- viewport dimensions;
- theme, state, and scroll position;
- evidence type;
- exact value or estimated range;
- readiness status;
- selector and sample count where applicable.

Examples:
- `#172033` read from computed CSS → Observed.
- Assigning it the role `text.primary` → Inferred unless source-defined.
- Claiming it is site-wide after inspecting one route → Unknown.

Do not turn an inferred role into a fact through repetition.

## 7. Separate extraction, reconstruction, and functionality

Treat these as three independent outcomes. Correct extraction does not prove a faithful mockup; visual fidelity does not prove working interactions. Record each outcome as `PASS`, `PARTIAL`, `FAIL`, or `NOT_TESTED`, with a rationale:
- **Extraction:** correctness and coverage of source observations, measurements, and inferred tokens.
- **Reconstruction:** fidelity of the implementation to the inspected source at tested viewports and states.
- **Functionality:** behavior of menus, forms, navigation, controls, and other tested interactions.

When reconstruction is requested:
1. Read `references/reconstruction-protocol.md` before implementing.
2. Capture rendering context: `html`/`body` attributes, theme and theme-control attributes, base URL, relevant asset paths, component states, and dependence on JavaScript initialization.
3. Do not automatically copy or execute source-page scripts. Reproduce the required state statically or implement minimum safe behavior. Record omitted dependencies and their impact.
4. Compare source and mockup at every tested viewport/state. Save `comparison.json`, using `comparison.example.json` as the structure.
5. Run `scripts/validate-evidence.py` against the final package where Python 3 is available. It uses only the standard library and is not an extraction runtime dependency.
6. Do not report full acceptance when comparison or package validation fails. The validator checks completeness and internal references, not visual truth.

A reconstruction comparison must cover text and component state, representative geometry, important styles, document and component overflow, and source/mockup screenshots. Report deviations and scope. Pixel identity is not required unless explicitly requested and supported by the comparison method.

## 8. Durable evidence package

For quantitative studies and comparisons, create a persistent evidence package independent of chat history:

```text
study/
├── report.html
├── evidence.json
└── screenshots/
    ├── <sample-id>__<viewport>__<timestamp>.png
    └── ...
```

Requirements:
- `report.html` contains scope, metric definitions, results, exclusions, limitations, and evidence links.
- `evidence.json` records URLs, timestamps, viewport, state, scroll position, readiness checks, metric contract, selected elements, results, and screenshot paths.
- Save a separate screenshot for each measured viewport/state where screenshot capture is available and relevant.
- Use unique sample IDs or timestamps; never overwrite an earlier evidence screenshot.
- Link each material report finding to one or more evidence IDs.
- Keep evidence files in the deliverable directory, not a temporary location.
- If the environment cannot create or retain a required artifact, state that explicitly and downgrade the deliverable's evidence status.

For purely qualitative, low-scope analysis, use a proportionate report; do not create empty placeholder artifacts. Read `references/evidence-schema.md` for the data contract and example.

## 9. Normalize design tokens

Keep three levels separate:

| Level | Meaning | Example |
|---|---|---|
| Primitive | Raw measured value | `#172033`, `16px`, `8px` |
| Semantic | Purpose assigned to a value | `text.primary`, `surface.canvas` |
| Component/composite | Value or rule used by a pattern | `button.primary.padding.inline` |

Rules:
- preserve original values, units, alpha, font stacks, and provenance;
- mark agent-assigned semantic aliases as inferred;
- do not invent a base spacing unit, type scale, breakpoint, or token hierarchy;
- do not merge similar values without evidence;
- preserve theme-specific and route-specific exceptions;
- validate generated exports before calling them implementation-ready.

## 10. Separate visual simplicity from page weight

Report these as independent dimensions:

1. **Visual simplicity:** perceived/observed visual structure, density, and ornamentation.
2. **Declared dependencies:** libraries and resources referenced by source code or manifests.
3. **Observed resources:** requests/resources actually observed during a defined capture.
4. **Transferred bytes:** measured network transfer under an explicitly stated capture method and time window.

Do not infer that a page is technically lightweight from sparse visuals, few images, or few visible components. Do not infer actual transfer from declared dependencies. If network capture is unavailable or incomplete, report transfer as `not_measured`.

When reporting bytes, state whether the figure represents encoded transfer, decoded resource size, cached resource size, or another measure. State cache behavior, cross-origin visibility limitations, failed requests, and the capture window when known. Never present a partial resource log as total page transfer.

## 11. Compare pages or implementations

Compare only equivalent samples:
- same metric contract;
- same viewport dimensions;
- same content region;
- same scroll position;
- same theme and interaction state;
- accepted readiness status.

Separate structural differences from visual differences. Distinguish measured deviations from subjective judgments. If contracts differ, do not rank or aggregate the values.

Do not call an implementation pixel-perfect based on visual resemblance alone. If exact pixel-difference tooling is unavailable, describe the comparison as qualitative.

## 12. Optional external tooling

A dedicated extraction package may be used only if already available or explicitly requested. It is never a prerequisite.

If explicitly requested:
1. confirm runtime and package availability;
2. check installed version and command help;
3. explain installation requirements and obtain authorization before installation or environment changes;
4. treat generated output as evidence to inspect, not verified fact;
5. apply the same readiness, metric, evidence, and quality gates.

Do not silently switch to external tooling when built-in capabilities are insufficient. Report the limitation and ask whether the user wants the optional route.

## 13. Deliver results

Choose deliverables based on the task. Do not generate every format by default.

A quantitative or comparative report must include:
1. **Scope:** URLs, routes, viewports, themes, states, and scroll positions.
2. **Readiness:** accepted/rejected sample counts and rejection reasons.
3. **Metric contract:** unit, selector, visibility/completeness, region, denominator, and formula.
4. **Results:** separate titles, complete items, text counts, and density metrics where applicable.
5. **Quality:** Usable / Usable with limitations / Insufficient, with reasons.
6. **Evidence:** stable evidence IDs and persistent screenshot references.
7. **Limitations:** unknowns, uninspected routes, missing capabilities, and non-comparable measures.

A design-system report should additionally cover foundations, components, responsive behavior, accessibility signals, tokens, and exact artifact filenames.

Never claim "complete design system", "site-wide", "WCAG compliant", "pixel-perfect", or "lightweight" unless the measurement scope and evidence support that exact claim.

## Acceptance test profiles

When validating this skill or a reconstruction workflow, cover three distinct source profiles where available:
- `static-document`: a document relying on browser defaults, with no external CSS. Treat the absence of external stylesheets as a valid source variant when the observed rendering is intentional; do not fail readiness solely because no external CSS exists.
- `responsive-themed`: a page with responsive CSS and at least one theme or theme-control attribute. Verify the active theme and compare at more than one viewport.
- `javascript-initialized`: a page whose visible content or component state changes after JavaScript initialization. Record pre/post initialization state and test the captured target state without automatically copying or executing source scripts.

Passing one profile does not establish coverage of the others. Record unavailable profiles as `NOT_TESTED`; do not claim broad dynamic-interface validation from a static document test.

## Failure and limitation handling

- **No browser capability:** use supplied source files or screenshots; otherwise state that live inspection is unavailable.
- **No DOM/CSS access:** perform visual analysis only and label estimates; reject CSS-derived metrics.
- **Readiness failure:** reject the sample; never use it in calculations or rankings.
- **Page blocked or login required:** stop and request an authorized access method.
- **Assets fail to load:** record missing assets and avoid dependent conclusions.
- **Dynamic or inconsistent page:** repeat only after identifying a meaningful stabilization method; report variability.
- **No durable file output:** disclose that the evidence package could not be retained.
- **Insufficient evidence:** state what additional evidence would resolve the gap.
