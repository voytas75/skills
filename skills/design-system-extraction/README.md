# Design System Extraction

Analyze and document the design system of an existing website or supplied interface materials without requiring a dedicated extraction package.

## What it does

- Identifies colors, typography, spacing, layout, geometry, and component patterns.
- Examines responsive behavior, interaction states, and motion.
- Builds evidence-based design-token inventories.
- Compares pages and implementations.
- Supports quantitative content-density studies with explicit measurement definitions.
- Produces persistent reports and evidence packages for reproducibility.

## Reliability model

The skill does not accept a page sample merely because navigation completed. Quantitative measurements pass a readiness gate: expected URL and content, stylesheet readiness, and stable selected measurements across two consecutive samples.

Comparisons use a shared metric contract. Invalid samples are rejected rather than included with a low-confidence label. Reports link important findings to retained evidence.

## Requirements

There is no mandatory extraction package. The skill does not require `design-extract`, `designlang`, Node.js, npm, Playwright, or Chromium.

It requires some way to inspect the target: an available browser, DOM/CSS inspection, screenshots, source files, or user-provided materials. Analysis depth depends on available evidence.

## Optional integration

[design-extract](https://github.com/Manavarya09/design-extract) may be used only when already available or explicitly requested. It is not installed, invoked, or assumed by default.

## Files

- `SKILL.md` — operational instructions for the AI agent.
- `references/measurement-protocol.md` — common metric definitions and comparability rules.
- `references/quality-gates.md` — sample acceptance and rejection rules.
- `references/evidence-schema.md` — persistent evidence package and JSON structure.
- `references/reconstruction-protocol.md` — source-context capture and reconstruction fidelity.
- `comparison.example.json` — per-viewport source/mockup comparison template.
- `scripts/validate-evidence.py` — package consistency validator (Python 3 standard library only).

The README is written for people; the skill and references are written for reliable agent execution.


## Reconstruction quality

Extraction, reconstruction fidelity, and functionality are assessed independently. Reconstruction records source rendering context and compares source with mockup at each tested viewport/state. The validator checks package completeness and references; it does not determine whether visual observations are true.

The validator is an optional local QA helper. Python 3 is needed only to run it, not to use the skill's analysis method.

## Regression profiles

Regression coverage distinguishes `static-document`, `responsive-themed`, and `javascript-initialized` sources. A page with no external CSS is a valid profile when its browser-default or inline rendering is intentional; lack of an external stylesheet is not an automatic failure.
