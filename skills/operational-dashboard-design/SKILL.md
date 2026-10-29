---
name: operational-dashboard-design
description: Use when designing operational dashboards.
---

# Operational Dashboard Design

Build a data-first dashboard with the flow **overview → attention → detail → act**. Keep the primary view free of explanatory sentences without hiding information needed to interpret data or operate controls.

## When to Use

- Design or review an operational dashboard, KPI view, or compact analytical graphic.
- Help users identify exceptions and take a defined action from the affected data.
- Refactor a cluttered dashboard into a consistent, scannable visual system.

Do not use this as a universal rule for narrative reports, educational graphics, onboarding, or interfaces that need explicit instructions. Static graphics cannot rely on tooltips or pretend to provide interactive actions.

## Inputs and Prerequisites

Obtain the dataset or precise schema, intended audience, operational decision, delivery format (mockup, image, HTML, or working dashboard), and target device. Identify metric units, time windows, baselines, thresholds, desired direction, and permitted actions.

No specific library, service, or agent client is required. Use available tools to inspect data, build the requested artifact, and test it. Ask only for missing decision-critical information; label provisional assumptions. Never invent measurements, thresholds, actions, or successful QA results.

## Procedure

### 1. Establish the data contract

- Check totals, aggregation, denominators, units, time windows, and baseline comparability with actual calculations.
- Distinguish zero, missing, stale, unavailable, and not applicable values; never silently convert missing data to zero.
- Define whether higher or lower values are problematic for each metric. For neutral metrics such as spend, use an approved budget or range; without one, use neutral styling and do not imply a problem.
- Keep statistical uncertainty and data freshness visible when they affect decisions.

**Complete when:** every displayed metric has a defined interpretation and known data limitations.

### 2. Define hierarchy and action

- Start with the overall state, then exceptions flagged directly on the data, then detail.
- Set attention priority from severity and decision relevance, not from arbitrary visual decoration.
- Place the action on or beside the affected datum: for example, an actionable heatmap cell opens its relevant detail or workflow.
- Use meaningful accessible names, visible focus, and clear interactive affordances. Never invent a remediation action or execute it as part of designing the view.

**Complete when:** each flag has a defined reason and a real action or an explicitly non-interactive detail destination.

### 3. Choose visual encodings

Prefer position on a common scale, then length, then angle/area, then color when they suit the task. This is a design heuristic, not a guarantee that one encoding fits every dataset.

Default visual vocabulary:
- **Classed heatmap:** discrete, labeled thresholds for exception scanning.
- **Bullet graph:** value, comparable target, and meaningful ranges instead of gauges. Align scales when comparisons require it.
- **Segmented share bar:** parts of a defined whole instead of pie charts, including two-category shares. Show the denominator and do not imply a whole for overlapping categories.
- **Sparkline:** compact temporal context with enough endpoint, scale, or range information to avoid misleading comparisons.
- **Consistent detail surface:** tooltips with an equivalent focus/tap-accessible popover or detail panel.

If this vocabulary cannot honestly represent the requested task, explain the mismatch and propose a suitable alternative rather than forcing the data into it.

**Complete when:** every component supports a comparison or decision and its scale is interpretable.

### 4. Apply sparse language and accessible salience

- On the primary data view use concise metric names, values, units, period labels, baseline labels, and necessary control/status labels; no narrative insights or explanatory paragraphs.
- A compact comparison such as `▼ 15% vs Sep` must identify what is compared and whether the change is favorable. An arrow alone must not encode severity.
- Put supporting explanations in details, but never make essential meaning hover-only. Provide keyboard and touch access, accessible names, and an equivalent text/data representation where appropriate.
- Use sequential scales for ordered magnitude, diverging scales around a meaningful midpoint, or classed scales for defined thresholds.
- Increase visual intensity toward an established problem. Where low values are bad, reverse the severity mapping; where both extremes are bad, use two-sided thresholds.
- Pair color with a non-color cue such as shape, icon, pattern, border, or explicit short status label.
- Target at least 4.5:1 contrast for ordinary text and 3:1 for large text and meaningful graphical/control boundaries. Test actual foreground/background combinations and interaction states; avoid accent text on an unverified accent tint.
- Remove decorations, redundant gridlines, and unnecessary backgrounds. Keep legends, labels, and guides when they are needed to interpret the data.

**Complete when:** the view remains understandable without color, hover, or explanatory sentences on its primary data surface.

### 5. Build and verify the requested artifact

Deliver the requested format, not merely a design description. For a working dashboard, exercise its interactions and data states; for an image or mockup, clearly identify non-functional controls.

Run the verification checklist below. Correct confirmed defects, and label unexercised checks **not verified**. Do not call a specification an implemented dashboard or a structural review a usability test.

**Complete when:** the artifact is delivered with evidence-backed QA and explicit limitations.

## Verification

- **Data:** calculated totals and shares reconcile; units, time windows, denominators, and baselines match; missing/stale/neutral states are tested.
- **Salience:** inspect the rendered view and check whether the intended exception is prominent. Distinguish a visual review from a measured user attention test.
- **Color:** inspect a real color-vision simulation when tooling permits; independently confirm that non-color cues convey severity. Simulation alone does not establish accessibility.
- **Contrast:** measure rendered color pairs and relevant states; report the method and failures rather than asserting compliance from palette names.
- **Language:** inspect the primary surface for explanatory sentences, retaining necessary control, status, and safety wording.
- **Interaction:** exercise keyboard navigation, visible focus, focus/tap details, dismissal, and the intended action route without performing unapproved external actions.
- **Layout:** check the target viewport, clipping, overflow, long labels, and representative empty/single/multiple-item states.
- **Integrity:** legends and scales are sufficient, layout rules do not conflict, and the output does not invent data or imply unsupported actions.

## Output Contract

Return:
1. The requested artifact or its verified location.
2. A brief description of the primary decision and action path.
3. A compact QA report separating passed, failed, and not-verified checks, with methods or evidence.
4. Remaining assumptions or blockers and one concrete next step if unfinished.

The no-narrative rule applies to the dashboard's primary data surface, not to this delivery report, accessibility text, or essential error/safety messages.

## Pitfalls

- Minimalism that removes necessary context is ambiguity, not efficiency.
- A red value is not necessarily a problem; severity requires a metric-specific rule.
- A tooltip is not an accessible substitute for essential visible or focus-accessible information.
- Sparse graphics can still mislead through incompatible scales, truncated ranges, or missing denominators.
- Do not claim WCAG conformance from a contrast check alone.
- Do not claim eye-tracking, color-vision simulation, or tested interactions without actually performing them.
