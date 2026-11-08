#!/usr/bin/env python3
"""Validate evidence package structure and internal references. Python 3 stdlib only."""
from __future__ import annotations
import json
import sys
from pathlib import Path

STATUSES = {"PASS", "PARTIAL", "FAIL", "NOT_TESTED"}
CLASSIFICATIONS = {"observed", "inferred", "unknown", "recommendation"}

def validate(root: Path) -> list[str]:
    errors: list[str] = []
    def check_file(value: object, label: str, required: bool = True) -> Path | None:
        if not isinstance(value, str) or not value.strip():
            if required: errors.append(f"{label}: missing file path")
            return None
        rel = Path(value)
        if rel.is_absolute() or ".." in rel.parts:
            errors.append(f"{label}: unsafe relative path: {value}")
            return None
        candidate = (root / rel).resolve()
        try: candidate.relative_to(root.resolve())
        except ValueError:
            errors.append(f"{label}: path escapes package: {value}")
            return None
        if not candidate.is_file():
            errors.append(f"{label}: file not found: {value}")
            return None
        return candidate

    evidence_path = check_file("evidence.json", "evidence.json")
    check_file("report.html", "report.html")
    if evidence_path is None: return errors
    try: data = json.loads(evidence_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"evidence.json: invalid JSON ({exc})"]
    if not isinstance(data, dict): return ["evidence.json: root must be an object"]

    for key in ("study_id", "created_at", "target", "samples", "findings", "limitations"):
        if key not in data: errors.append(f"evidence.json: missing required field '{key}'")
    target = data.get("target")
    if not isinstance(target, dict) or not target.get("requested_url") or not target.get("final_url"):
        errors.append("evidence.json: target.requested_url and target.final_url are required")
    task_type = data.get("task_type", "analysis")
    if task_type not in {"analysis", "reconstruction"}:
        errors.append("evidence.json: task_type must be 'analysis' or 'reconstruction'")

    outcomes = data.get("outcomes")
    if not isinstance(outcomes, dict):
        errors.append("evidence.json: outcomes object is required")
        outcomes = {}
    for key in ("extraction", "reconstruction", "functionality"):
        item = outcomes.get(key)
        if not isinstance(item, dict) or item.get("status") not in STATUSES or not isinstance(item.get("rationale"), str) or not item["rationale"].strip():
            errors.append(f"evidence.json: outcomes.{key} requires valid status and non-empty rationale")

    comparison = None
    if task_type == "reconstruction":
        context = data.get("rendering_context")
        if not isinstance(context, dict):
            errors.append("reconstruction: rendering_context object is required")
        else:
            for key in ("html_attributes", "body_attributes", "theme", "base_url", "assets", "component_states", "js_initialization_dependency"):
                if key not in context: errors.append(f"reconstruction: rendering_context.{key} is required")
        cp = check_file(data.get("comparison_file", "comparison.json"), "comparison.json")
        if cp:
            try: comparison = json.loads(cp.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc: errors.append(f"comparison.json: invalid JSON ({exc})")
            if isinstance(comparison, dict):
                viewports = comparison.get("viewports")
                if not isinstance(viewports, list) or not viewports:
                    errors.append("comparison.json: non-empty viewports array is required")
                else:
                    for i, vp in enumerate(viewports):
                        if not isinstance(vp, dict):
                            errors.append(f"comparison.json: viewports[{i}] must be an object"); continue
                        for field in ("viewport_css_px", "source_screenshot", "mockup_screenshot", "checks", "deviations", "evidence_ids"):
                            if field not in vp: errors.append(f"comparison.json: viewports[{i}].{field} is required")
                        check_file(vp.get("source_screenshot"), f"comparison viewports[{i}] source_screenshot")
                        check_file(vp.get("mockup_screenshot"), f"comparison viewports[{i}] mockup_screenshot")
                        checks = vp.get("checks")
                        required = ("text_and_component_state", "geometry", "important_styles", "document_overflow", "component_overflow")
                        if not isinstance(checks, dict):
                            errors.append(f"comparison.json: viewports[{i}].checks must be an object")
                        else:
                            for name in required:
                                if not isinstance(checks.get(name), dict) or checks[name].get("status") not in STATUSES:
                                    errors.append(f"comparison.json: viewports[{i}].checks.{name} requires a valid status")

    samples = data.get("samples")
    if not isinstance(samples, list):
        errors.append("evidence.json: samples must be an array"); samples = []
    evidence_ids: set[str] = set()
    for i, sample in enumerate(samples):
        if not isinstance(sample, dict):
            errors.append(f"samples[{i}] must be an object"); continue
        for field in ("sample_id", "captured_at", "status", "readiness", "viewport", "theme", "interaction_state", "scroll_position_css_px", "evidence"):
            if field not in sample: errors.append(f"samples[{i}].{field} is required")
        if sample.get("status") not in {"accepted", "rejected"}:
            errors.append(f"samples[{i}].status must be accepted or rejected")
        refs = sample.get("evidence")
        if not isinstance(refs, list):
            errors.append(f"samples[{i}].evidence must be an array"); continue
        for j, ref in enumerate(refs):
            if not isinstance(ref, dict) or not isinstance(ref.get("evidence_id"), str):
                errors.append(f"samples[{i}].evidence[{j}] requires evidence_id"); continue
            eid = ref["evidence_id"]
            if eid in evidence_ids: errors.append(f"duplicate evidence_id: {eid}")
            evidence_ids.add(eid)
            if ref.get("type") == "screenshot": check_file(ref.get("path"), f"screenshot {eid}")

    findings = data.get("findings")
    if not isinstance(findings, list):
        errors.append("evidence.json: findings must be an array"); findings = []
    finding_ids: set[str] = set()
    for i, finding in enumerate(findings):
        if not isinstance(finding, dict):
            errors.append(f"findings[{i}] must be an object"); continue
        fid = finding.get("finding_id")
        if not isinstance(fid, str) or not fid.strip() or fid in finding_ids:
            errors.append(f"findings[{i}]: missing or duplicate finding_id")
        else: finding_ids.add(fid)
        if not isinstance(finding.get("claim"), str) or not finding["claim"].strip():
            errors.append(f"findings[{i}].claim is required")
        if finding.get("classification") not in CLASSIFICATIONS:
            errors.append(f"findings[{i}].classification is invalid")
        refs = finding.get("evidence_ids")
        if not isinstance(refs, list) or (not refs and finding.get("classification") == "observed"):
            errors.append(f"findings[{i}].evidence_ids must link observed findings to evidence"); continue
        for ref in refs:
            if ref not in evidence_ids: errors.append(f"findings[{i}]: unknown evidence_id '{ref}'")

    if task_type == "reconstruction" and isinstance(comparison, dict):
        for i, vp in enumerate(comparison.get("viewports", [])):
            if isinstance(vp, dict):
                for ref in vp.get("evidence_ids", []):
                    if ref not in evidence_ids: errors.append(f"comparison viewports[{i}]: unknown evidence_id '{ref}'")
    return errors

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate-evidence.py <package-directory>", file=sys.stderr); return 2
    root = Path(sys.argv[1]).expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: package directory not found: {root}", file=sys.stderr); return 2
    errors = validate(root)
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for error in errors: print(f"- {error}")
        return 1
    print("PASS: evidence package structure and references are consistent")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
