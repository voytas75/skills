# Capture readiness and eligibility
Capture readiness answers: can this sample be measured reliably? It does NOT answer: does the target faithfully reproduce the source?

Required `capture_readiness` controls: `url_identity`, `content_identity`, `render_stability`, `state_integrity`, `obstruction_check`, `capture_integrity`; each `{status: PASS|FAIL|NOT_TESTED|NOT_APPLICABLE,details,rationale?,evidence_ids?}`. `accepted` capture requires applicable controls PASS/N/A. A failed control invalidates only affected sample/modalities; preserve raw capture and reason.

`asset_audit` is separate: `{status: PASS|PARTIAL|FAIL|NOT_TESTED,substitutions:[{asset,replacement,reason,evidence_ids}],unresolved:[{asset,reason,evidence_ids}],resolved_assets:[...]}`. Substitution/unresolved asset MUST NOT change capture status by itself. `asset_audit: PASS` requires empty substitutions/unresolved. Stylesheet loading is recorded separately from asset fidelity.

Each sample includes `capture_status: valid|partial|invalid`, `capture_readiness`, `asset_audit`, `measurement_eligibility` map (modality => `{status: eligible|ineligible|partial,reason,evidence_ids}`). Modality keys include `content`, `geometry`, `styles`, `visual`, `responsive`, `interaction`, `font_identity`, `asset_identity`. Eligibility is explicit and independent. Example: font identity ineligible while geometry/visual eligible.

A legacy `status: accepted|rejected` may be emitted for compatibility, but is descriptive only. Do not use it as a global comparison gate. Retain rejected/partial samples and permit eligible modality-specific measurements. Retries get new sample IDs; preserve history.

Stability tolerances apply only to repeated same-state captures. Record exact viewport, theme, state, DPR, zoom, browser, scroll/anchor, font/layout stability, and obstruction.
