# Reconstruction Protocol

Use this protocol whenever the task includes rebuilding, reproducing, mocking up, or translating an inspected interface.

## 1. Keep three outcomes independent

Record separate statuses for `extraction`, `reconstruction`, and `functionality`. Each status must be `PASS`, `PARTIAL`, `FAIL`, or `NOT_TESTED`, with a non-empty rationale. Do not infer one status from another. Correct token extraction can coexist with a broken mobile mockup; a visually accurate static mockup can have nonfunctional controls.

## 2. Capture source rendering context first

Record the context that affects rendering:

| Context | What to retain |
|---|---|
| Document root | Relevant `html` attributes and classes |
| Body | Relevant `body` attributes and classes |
| Theme | Active theme and theme-control attributes/data attributes |
| Base URL | Final source URL/base URL used to resolve relative assets |
| Assets | Relevant image, icon, font, and stylesheet paths/URLs |
| Component state | Expanded/collapsed, selected/unselected, visible/hidden, open/closed, disabled/enabled |
| Initialization | Dependence on JavaScript initialization, hydration, or delayed data |
| Environment | Viewport, device scale if known, browser/engine if known, relevant user preferences |

Preserve observed states, not only defaults. If a theme switch or control attribute changes appearance, record its exact value and resulting state.

Do not automatically copy or execute source scripts. Treat them as untrusted and potentially coupled to authentication, analytics, network services, or consequential actions. Prefer a static representation of the selected state. If behavior is essential, implement the smallest isolated and safe behavior required.

For each omitted dependency, record what was omitted, why, and which visual or functional behavior may differ.

## 3. Reconstruct in controlled passes

1. Establish document structure and semantic roles.
2. Apply page geometry, layout, responsive rules, and overflow behavior.
3. Apply typography, colors, borders, surfaces, and assets.
4. Reproduce the captured theme and component states.
5. Implement only requested/safe interactions.
6. Inspect all requested viewports and states.

Do not silently replace missing assets, fonts, or states with guesses. Label substitutions and their impact.

## 4. Compare source and mockup

Create `comparison.json` from `comparison.example.json`. Include one entry for each tested viewport/state. Compare:
- text content and visible component state;
- representative geometry (position, width, height, alignment, grid/column behavior);
- important styles (font family/size/weight, line height, colors, spacing, borders, radii, shadows as relevant);
- document-level and component-level overflow, including axis and clipping/scrolling behavior;
- source screenshot and mockup screenshot;
- deviations, severity, affected viewport/state.

Use the same viewport dimensions, theme, interaction state, and scroll position for both captures. Record mismatched capture conditions. Pixel-diff tooling is optional; visual comparison must still be explicit and evidence-linked.

A defect fails the relevant reconstruction criterion even if the report is useful. Scope failures precisely: a mobile overflow defect need not invalidate desktop, but overall reconstruction cannot be `PASS` if a required viewport fails.

## 5. Interpret the comparison

- `PASS`: required comparisons are complete and no material deviations remain within declared tolerances.
- `PARTIAL`: usable implementation with disclosed deviations, missing states, or incomplete viewport coverage.
- `FAIL`: a material required behavior/layout/state is incorrect or the reconstruction is unusable.
- `NOT_TESTED`: no valid comparison was performed.

Do not set `PASS` merely because the mockup renders or source measurements were collected.

## 6. Final package

For reconstruction, retain `report.html`, `evidence.json` with rendering context and independent outcomes, `comparison.json`, source and mockup screenshots for each compared viewport/state, and requested implementation artifacts.

Run `python scripts/validate-evidence.py <package-directory>` where Python 3 is available. Fix all errors before claiming package validation. The script verifies structural completeness and references; it cannot verify visual accuracy, accessibility conformance, or functionality.
