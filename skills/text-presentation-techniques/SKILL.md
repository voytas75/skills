---
name: text-presentation-techniques
version: 1.0.0
description: Select and compose text presentation techniques for dense, readable, operationally useful documents, reports, procedures, cheat sheets, dashboards, and technical communication. Use when structuring, compressing, formatting, comparing, annotating, or visually encoding text and data.
---

# Text Presentation Techniques

## Purpose

Select and combine text-presentation techniques to minimize reading effort and retrieval time without losing meaning, conditions, exceptions, units, scope, or relationships.

This skill is based on a 47-technique reference organized into five categories:
- **Conciseness**: reduce repetition and verbal overhead without deleting meaning.
- **Flow**: make sequence, navigation, causality, and decisions explicit.
- **Structure**: expose hierarchy, grouping, comparison, and dependencies.
- **Numbers and status**: present measurements, trends, thresholds, and visualized data.
- **Commands and code**: make syntax, execution, keyboard input, and expected output scannable.

## Governing rule

Optimize the cost of reading, not the number of characters. Compression is valid only when the reader can still recover:
- who or what is in scope;
- the action and its object;
- preconditions and exceptions;
- sequence and dependencies;
- units, denominators, ranges, and comparison periods;
- success criteria and failure states.

If compression removes one of these, restore the missing information.

## Workflow

1. **Identify the communication task**: define, instruct, compare, diagnose, decide, report, reference, or execute.
2. **Identify the reader**: expertise, familiarity with notation, language, device, print constraints, and accessibility needs.
3. **Identify the information shape**: prose, sequence, branching decision, state transition, comparison, hierarchy, numeric series, status, command, or code/output pair.
4. **Select the simplest suitable technique** from `references/TECHNIQUE-CATALOG.md`.
5. **Combine techniques only when each adds distinct information**. Avoid redundant emphasis, duplicate legends, and multiple encodings of the same fact.
6. **Apply a consistent visual grammar**: labels, separators, units, color categories, code notation, and status symbols.
7. **Check semantic completeness and rendering** using `references/QUALITY-CHECKS.md`.
8. **Adapt density and medium** using `references/DENSITY-AND-MEDIUM.md`.

## Selection principles

- One question or task should have one dominant presentation form.
- Use a sentence for one or two facts; use a table when comparing the same attributes across several entities.
- Use a decision tree when a condition changes the next path.
- Use a timeline only when time has operational significance.
- Use a causal chain only when the mechanism is known; correlation is not causation.
- Put the outcome or critical status first when it improves scanning, but do not omit security-critical context.
- State shared context once only if its scope unambiguously covers every following item.
- Replace repetition with a reference only when the referenced element exists and is easy to find.
- Define abbreviations at first use; do not invent ad hoc abbreviations.
- Use symbols only when the audience knows the notation or a legend is provided.
- Keep units and comparison periods explicit. A unit may appear once in a table header when it applies to the entire column.
- For numeric tables, align numbers by decimal position/right edge and use consistent precision.
- For code, distinguish input from output and state expected success evidence.
- For status, pair symbols with words; never rely on color alone.
- For charts, choose the visual form from the analytical question, not decoration.

## Category and color system

Use the five categories consistently when presenting a collection of techniques:
- Conciseness
- Flow
- Structure
- Numbers and status
- Commands and code

The source template demonstrates a category color system and several theme variants. Treat color as a secondary navigation aid:
- keep category-to-color mapping stable within one artifact;
- use no more than approximately five category hues;
- retain readable contrast;
- use a text label or other redundant cue;
- ensure meaning survives grayscale printing and color-vision differences.

The source identifies Okabe–Ito as a color-vision-conscious palette and labels warm/cool variants as weaker evidence. Do not claim that a palette is universally optimal for memory or learning. See `references/COLOR-AND-ACCESSIBILITY.md`.

## Density

Support three density modes:
- **Normal**: comfortable reading, more spacing, larger type.
- **Compact**: default for technical reference sheets and dense operational summaries.
- **Maximum**: only when the reader, display, and print output can still support legibility.

Do not reduce font size as the first response to overflow. Prefer removing redundancy, grouping related facts, shortening labels, or changing layout. See `references/DENSITY-AND-MEDIUM.md`.

## Technique inventory

The reference catalog contains 47 techniques:
- 01–16: concise definitions, telegraphic syntax, procedures, parameter labels, tables, matrices, decision trees, state transitions, causal chains, shared context, cross-references, abbreviations, relation symbols, aggregation, unit normalization, sparklines.
- 17–33: semantic grouping, timelines, frontloading, pipelines, syntax notation, task-to-command indexes, navigation paths, keyboard shortcuts, stateful checklists, status symbols, thresholds, footnotes, hierarchical numbering, code-to-meaning mapping, numeric alignment, recommended-option markers, command plus expected output.
- 34–47: chart selection, sparklines with markers, sparkbars, small multiples, direct-labeled bars, bullet graphs, min–median–max ranges, slopegraphs, heatmaps, status timelines, chart annotations, waffle charts, KPI trend tiles, and monospace text bars.

For exact selection criteria, limitations, and source-style examples, consult `references/TECHNIQUE-CATALOG.md`.

## Output behavior

- Produce the requested artifact, not a discussion of the workflow, unless explanation is requested.
- Preserve source terminology and distinctions where this skill is applied to the supplied reference.
- Do not invent facts, values, examples, status thresholds, evidence, or references.
- Label illustrative data explicitly.
- If the information supplied does not support a technique (for example, no time series for a sparkline), choose a different technique.
- If the requested medium cannot represent a feature reliably, state the limitation and use a supported alternative.

## References

- `references/TECHNIQUE-CATALOG.md`: all 47 techniques, purposes, selection criteria, and limits.
- `references/SELECTION-RULES.md`: decision framework for choosing and combining techniques.
- `references/COLOR-AND-ACCESSIBILITY.md`: category color, contrast, symbols, accessibility, and evidence limits.
- `references/DENSITY-AND-MEDIUM.md`: density modes, responsive layout, print, and medium-specific rules.
- `references/QUALITY-CHECKS.md`: semantic, visual, data, code, and rendering checks.
- `examples/reference-sheet.html`: self-contained, interactive example of a categorized reference sheet.
- `evals/evals.json`: evaluation cases for technique selection and faithful application.
