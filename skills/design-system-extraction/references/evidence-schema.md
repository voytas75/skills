# Evidence Schema

For quantitative studies and comparisons, retain a machine-readable evidence record and a human-readable report. The package must be usable without the chat history.

## Required package

```text
study/
├── report.html
├── evidence.json
└── screenshots/
    ├── sample-001__1440x900__20261108T052000Z.png
    └── sample-002__390x844__20261108T052100Z.png
```

Use unique sample identifiers and timestamps. Never overwrite an earlier screenshot. Save evidence in the deliverable directory, not a temporary path.

## Evidence record example

The following is a structural example. Replace all illustrative values with actual observations; never copy them as measurements.

```json
{
  "study_id": "example-study",
  "created_at": "2026-11-08T05:20:00Z",
  "target": {
    "requested_url": "https://example.invalid/",
    "final_url": "https://example.invalid/"
  },
  "metric_contract": {
    "metric_id": "complete_items_per_100k_css_px",
    "unit_name": "complete article card",
    "unit_selector": "article.card",
    "title_selector": "article.card h2",
    "include_rule": "A card with title, required metadata, and summary visible",
    "exclude_rule": "Promoted cards and cards clipped by the measurement region",
    "visibility_rule": "Relevant bounding box fully contained in the content region and viewport; text not clamped or truncated",
    "viewport_css_px": {
      "width": 1440,
      "height": 900
    },
    "content_region": {
      "selector": "main",
      "x": 120,
      "y": 160,
      "width": 1200,
      "height": 680
    },
    "scroll_position_css_px": {
      "x": 0,
      "y": 0
    },
    "theme": "light",
    "interaction_state": "default",
    "denominator": "content_area_css_px",
    "formula": "complete_item_count / content_area_css_px * 100000"
  },
  "samples": [
    {
      "sample_id": "sample-001",
      "captured_at": "2026-11-08T05:20:00Z",
      "status": "accepted",
      "readiness": {
        "requested_url_matches": true,
        "expected_content_present": true,
        "stylesheets_ready": true,
        "render_stable": true,
        "state_valid": true,
        "stability_tolerances": {
          "bounding_box_css_px": 0.5,
          "font_size_css_px": 0
        },
        "stability_samples": [
          {
            "width": 1200,
            "height": 680,
            "font_size_css_px": 16
          },
          {
            "width": 1200,
            "height": 680,
            "font_size_css_px": 16
          }
        ]
      },
      "selector_audit": {
        "matched_count": 8,
        "rendered_nonempty_count": 8,
        "fully_visible_count": 5,
        "representative_sample_count": 3
      },
      "metrics": {
        "title_count": 5,
        "complete_item_count": 3,
        "text_word_count": 96,
        "content_area_css_px": 816000,
        "content_density": 0.367647
      },
      "evidence": [
        {
          "evidence_id": "ev-001",
          "type": "screenshot",
          "path": "screenshots/sample-001__1440x900__20261108T052000Z.png"
        }
      ]
    }
  ],
  "findings": [
    {
      "finding_id": "finding-001",
      "claim": "Three complete cards are fully visible in the defined region.",
      "classification": "observed",
      "evidence_ids": ["ev-001"]
    }
  ],
  "limitations": []
}
```

The values above are illustrative and are not a valid result for any real website.

## Required fields

At minimum, `evidence.json` must preserve:
- study ID and creation time;
- requested and final URL;
- metric contract;
- timestamp, viewport, theme, state, and scroll position for each sample;
- readiness checks and accepted/rejected status;
- selector match counts and representative sample count;
- metric values and formulas;
- screenshot paths where captured;
- findings linked to evidence IDs;
- exclusions and limitations.

## Report requirements

`report.html` must include:
- scope and method;
- metric definitions;
- accepted and rejected sample counts;
- results and exclusions;
- evidence IDs linked to screenshots;
- limitations and non-comparable measures.

A report finding without an evidence ID is an unsupported assertion unless explicitly labelled as an inference or recommendation.

## Resource and transfer evidence

If page weight is discussed, record separately:
- declared dependencies;
- observed resource requests;
- transferred bytes and measurement method;
- capture start/end or navigation window;
- cache behavior and failed requests;
- cross-origin visibility limitations.

Do not describe `decodedBodySize` as transferred bytes. Do not treat missing cross-origin timing data as zero transfer. If a complete network record is unavailable, use `not_measured`.


## v1.4.0 outcome and reconstruction contract

Every `evidence.json` contains an `outcomes` object with three independent assessments:

```json
{
  "outcomes": {
    "extraction": {"status": "PASS", "rationale": "Source observations verified."},
    "reconstruction": {"status": "NOT_TESTED", "rationale": "No mockup was requested."},
    "functionality": {"status": "NOT_TESTED", "rationale": "No interaction implementation was requested."}
  }
}
```

Allowed statuses: `PASS`, `PARTIAL`, `FAIL`, `NOT_TESTED`. Each requires a non-empty rationale.

For reconstruction tasks, also include `task_type: "reconstruction"`, `rendering_context` with `html_attributes`, `body_attributes`, `theme`, `base_url`, `assets`, `component_states`, and `js_initialization_dependency`, plus `comparison_file: "comparison.json"`. The comparison must contain a non-empty `viewports` array with source/mockup screenshots, checks for text/state, geometry, important styles, document overflow, component overflow, deviations, and evidence IDs.

For non-reconstruction analysis, use `task_type: "analysis"`. Reconstruction and functionality may be `NOT_TESTED` with a reason.

## Machine validation

Run `python scripts/validate-evidence.py <package-directory>`. The validator uses Python 3 standard library modules only. It checks required fields, outcome statuses, screenshot file existence, safe relative paths, unique evidence IDs, finding-to-evidence references, and reconstruction comparison completeness/references. It does not verify measurement truth, visual fidelity, accessibility conformance, or functional behavior.
