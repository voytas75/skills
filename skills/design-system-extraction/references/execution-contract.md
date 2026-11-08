# Execution contract

Every run starts with `execution.json`. The manifest describes the intended work, not its results.

## Required fields

- `schema_version`: `1.5.0`.
- `study_id`: stable, non-empty identifier.
- `task_type`: `analysis`, `reconstruction`, `comparison`, or `audit`.
- `artifact_mode`: `snapshot`, `standalone_mockup`, `functional_implementation`, or `not_applicable`.
- `target.requested_url` and `target.final_url`, or a documented supplied-material target.
- `scope.pages`, `scope.viewports`, `scope.themes`, `scope.states`, and `scope.required_checks`.
- `capabilities`: explicit capability status map.
- `constraints`: array, empty if none.
- `created_at`: ISO-8601 timestamp.

## Task/artifact compatibility

- `analysis` and `audit` normally use `not_applicable`.
- `reconstruction` must use one of the three artifact modes.
- `comparison` may use `not_applicable` if comparing two existing interfaces without producing a new artifact.
- Do not silently reinterpret a task after execution begins. Record scope changes and their reasons.

## Viewports

Each viewport has a unique `id` and positive integer `width` and `height` in CSS pixels. Each required theme and state is a non-empty string. Each `required_checks` entry is a named criterion.

## Capabilities

Use `available`, `partial`, `unavailable`, or `not_checked`. Do not infer capability availability from the task description.

## Example

```json
{
  "schema_version": "1.5.0",
  "study_id": "example-study",
  "task_type": "reconstruction",
  "artifact_mode": "standalone_mockup",
  "target": {
    "requested_url": "https://example.org/",
    "final_url": "https://example.org/"
  },
  "scope": {
    "pages": ["/"],
    "viewports": [{"id": "desktop", "width": 1280, "height": 900}],
    "themes": ["light"],
    "states": ["default"],
    "required_checks": ["content_state", "geometry", "important_styles", "document_overflow", "component_overflow"]
  },
  "capabilities": {"browser": "available", "dom": "partial", "computed_styles": "partial", "screenshots": "available"},
  "constraints": [],
  "created_at": "2026-11-08T08:00:00Z"
}
```
