# Quality Gates

Use these gates to decide whether a browser sample is eligible for measurement. These are acceptance rules, not advisory warnings.

## Gate A — Navigation and document identity

Accept only when:
- requested URL and final URL are recorded;
- final URL is the expected destination or an explicitly expected redirect;
- document is not `about:blank`, a browser error, unrelated redirect, or unexpected authentication page.

Otherwise reject with `url_mismatch`, `blank_document`, `browser_error`, `unexpected_redirect`, or `authentication_block`.

## Gate B — Expected content

Accept only when the expected page landmark and task-relevant content are present. Verify a meaningful selector or content signature, not merely a non-empty `<body>`.

Otherwise reject with `expected_content_missing` or `wrong_page_content`.

## Gate C — Stylesheet readiness

For CSS-derived measurements, verify applicable stylesheet loading and applied computed styles on representative elements. Record stylesheet evidence and computed-style evidence.

If only screenshots are available, the sample may support visual estimates but not exact CSS measurements. Mark CSS measurement readiness as failed.

Reject CSS-derived measurements with `styles_not_ready` when stylesheets are pending/failed or values are still default/transient.

## Gate D — Render stability

Take two consecutive samples of selected representative elements after the readiness conditions are met. Compare:
- bounding box: x, y, width, height;
- relevant computed properties: font family, font size, line height, color, background, spacing, and other properties used by the metric.

Use tolerances declared before measurement. Record both samples and the result.

Reject with `render_unstable` when any property required by the metric exceeds its declared tolerance. Do not average unstable samples.

## Gate E — State and obstruction

Verify viewport, theme, scroll position, and interaction state. Check that loading skeletons, consent banners, modal overlays, sticky elements, or clipping do not invalidate the measured region.

Reject with `state_mismatch` or `measurement_obstructed` when applicable.

## Sample disposition

Every sample must have exactly one status:
- `accepted`: passed every applicable gate;
- `rejected`: failed at least one required gate.

A rejected sample:
- must not enter aggregation, averages, rankings, token inference, or comparison;
- must retain its rejection reason and diagnostic evidence;
- may be retried only after a meaningful corrective action;
- must not be converted to accepted by changing its status without a new sample.

## Report-level acceptance

A quantitative report is:
- **Usable** when all included samples are accepted and the metric contracts match;
- **Usable with limitations** when valid samples support a partial result and excluded/missing samples are disclosed;
- **Insufficient** when readiness failures, incompatible contracts, or missing evidence prevent the requested conclusion.

A rejected sample does not invalidate unrelated accepted samples, but it must never contribute to their calculations.


## Acceptance profiles for skill regression tests

Use separate fixtures because they exercise different failure modes:

| Profile | Required characteristics | Acceptance focus |
|---|---|---|
| `static-document` | No external CSS; browser-default styles or intentional inline styling | Valid document identity/content; absence of external CSS is not a readiness failure by itself |
| `responsive-themed` | Responsive CSS and theme attribute/control | Correct theme context; multiple viewport captures; layout and overflow comparison |
| `javascript-initialized` | Content or component state changes after JS initialization | Capture initialized state and its dependency; do not assume source scripts can be safely reused |

A profile that was not run must be `NOT_TESTED`. Results from `static-document` alone do not validate dynamic or theme-dependent interfaces.
