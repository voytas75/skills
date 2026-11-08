# Fidelity and runtime verification (v1.6.0)

## 1. Independent fidelity dimensions

Every reconstruction must report these dimensions independently, each with `PASS`, `PARTIAL`, `FAIL`, or `NOT_TESTED`, a rationale, evidence references, and declared scope:

- `visual_fidelity`: geometry, typography, color, borders, imagery, icons, and visual hierarchy.
- `functional_fidelity`: links, buttons, menus, forms, accordions, search, and other in-scope controls.
- `responsive_fidelity`: required viewport behavior, reflow, breakpoint transitions, and overflow.
- `content_fidelity`: text, order, labels, landmarks, and semantic roles.
- `asset_fidelity`: fonts, iconography, logos, illustrations, and other visual assets.

Element-ID match coverage is a pairing metric only. It MUST NOT be presented as a visual-fidelity score.

## 2. Asset and font readiness

Each sample's `readiness.asset_readiness` MUST include:
- `status`: readiness status;
- `details`: concise explanation;
- `substitutions`: array of objects `{asset, replacement, reason}`;
- `unresolved`: array of asset identifiers or descriptions.

A sample MUST NOT claim `asset_readiness.status: PASS` when either array is non-empty. Use `PARTIAL` only in the fidelity dimension; readiness statuses are `PASS`, `FAIL`, `NOT_APPLICABLE`, `NOT_TESTED`. Therefore an unavailable/substituted asset normally makes readiness `FAIL` or `NOT_TESTED`, not PASS.

Font reporting MUST distinguish CSS `font-family` declarations from actual resolved fonts. Where browser instrumentation supports it, record resolved fonts per text run or glyph (e.g. Chromium `CSS.getPlatformFontsForNode`). If unsupported, report `resolved_font_status: NOT_TESTED`; do not infer resolution from `document.fonts.check()` or a loaded FontFace alone. Record missing glyphs/fallbacks and the exact text sample.

A no-copy/no-hotlink asset policy may prohibit use of original assets. In that case record the limitation and classify the affected fidelity as `PARTIAL`/`FAIL` according to the manifest. Do not conceal a substitution.

## 3. Interaction discovery and safe execution

Read-only capture does not prohibit reversible interaction tests. Use a fresh isolated browser context/profile, no authenticated personal account, no real payment/submission, and no destructive action.

For each visible in-scope interactive control:
1. Record source initial state and accessible name/role.
2. Execute a safe, reversible action where possible (open/close menu, expand/collapse, toggle local preference, focus, reveal search).
3. Record resulting state, URL change, focus behavior, keyboard behavior, and reversibility.
4. Reset context or reload and verify initial state.
5. Reproduce the observed behavior in the target and execute the same test.
6. Record expected vs observed outcome and evidence for both sides.

For navigation links, verify destination and navigation behavior without submitting forms or triggering sensitive transactions. If an action is unsafe or cannot be tested, mark it `NOT_TESTED` with a reason; it cannot count as PASS.

`measurements/runtime-tests.json` MUST contain:
- `interactions`: array of `{control_id, role, accessible_name, source_status, source_action, source_result, target_status, target_action, target_result, result, evidence_ids}`;
- `resolved_font_status`: `PASS`, `FAIL`, or `NOT_TESTED`;
- `font_runs`: array with `text`, `declared_family`, `resolved_families`, `fallback_detected`;
- `limitations`: array.

A reconstruction with visible interactive controls cannot receive `functional_fidelity: PASS` if any required control is missing, target behavior is not tested, or source behavior is not tested. If the task explicitly scopes behavior out, record that exclusion in the manifest before execution.

## 4. Screenshot visual regression

For each required viewport/theme/state, capture source and target screenshots using identical viewport dimensions, device scale factor, browser engine/version, zoom, scroll position, and state. Wait for fonts and layout stability; record these settings.

Create `visual-comparison.json` with:
- `schema_version`, `study_id`, `method`, `metric`, `thresholds`;
- `pairs`: one entry per required viewport/theme/state, with source and target screenshot paths, dimensions, metric value, threshold, masked regions (with rationale), result, and evidence IDs.

Allowed metrics include raw pixel difference, SSIM, or a documented perceptual metric. State color space, normalization, and masking method. Do not mask large layout regions to hide discrepancies. Report both masked and unmasked coverage. If image comparison tooling is unavailable, mark it `NOT_TESTED`; visual fidelity cannot be PASS for a reconstruction task.

Screenshot comparison is complementary: DOM geometry, computed styles, semantic content, and behavior tests remain required.

## 5. Geometry root-cause analysis

For material geometry differences, record:
- affected stable element IDs;
- source/target rects and deltas;
- first ancestor where cumulative geometry diverges;
- likely cause classified as observed/inferred/unknown;
- evidence supporting the diagnosis;
- correction applied or reason not corrected.

Do not claim a causal diagnosis from a downstream delta alone. For example, a footer offset may be cumulative from text wrapping, missing content, line-height, or preceding section spacing.

## 6. Acceptance gates

For `standalone_mockup` reconstruction:
- `visual_fidelity`, `responsive_fidelity`, and `content_fidelity` are required.
- `asset_fidelity` is required when the source uses non-text visual assets or custom fonts.
- `functional_fidelity` is required when visible interactive controls are in scope (default: in scope).
- paired screenshot comparison is required for each declared viewport/theme/state.
- every required dimension must be PASS for `task_acceptance: PASS`.
- PARTIAL, FAIL, NOT_TESTED, missing evidence, missing viewport/state, or incomplete control coverage blocks PASS.

For `functional_implementation`, functional fidelity is always required, including keyboard/focus/error states defined in the manifest.

A task may still be accepted with known limitations only when those limitations were explicitly scoped out before execution and the acceptance profile permits that exclusion. Do not retroactively waive failed criteria.

## 7. Reporting

Report dimensions independently. Do not collapse them into an opaque weighted score. If a composite score is requested, publish the formula, weights, missing-data policy, and raw dimension statuses. Default is no composite score.
