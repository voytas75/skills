#!/usr/bin/env python3
"""Validate Design System Extraction v1.5.x packages (Python standard library only)."""
from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

VERSION = "1.6.0"
SCHEMA_VERSION = "1.6.0"
TASKS = {"analysis", "reconstruction", "comparison", "audit"}
ARTIFACTS = {"snapshot", "standalone_mockup", "functional_implementation", "not_applicable"}
OUTCOMES = {"PASS", "PARTIAL", "FAIL", "NOT_TESTED"}
READINESS = {"PASS", "FAIL", "NOT_APPLICABLE", "NOT_TESTED"}
ROLES = {"source", "target"}
REQUIRED_RECON_CHECKS = {"content_state", "geometry", "important_styles", "document_overflow", "component_overflow", "asset_completeness"}

class Validator:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks: list[str] = []
        self.files: dict[str, dict] = {}

    def err(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def read_json(self, rel: str, required: bool = True):
        p = self.safe_file(rel, required)
        if p is None:
            return None
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.err(f"{rel}: invalid JSON: {exc}")
            return None

    def safe_file(self, value, required=True):
        if not isinstance(value, str) or not value.strip():
            if required:
                self.err("missing required file path")
            return None
        rel = Path(value)
        if rel.is_absolute() or ".." in rel.parts:
            self.err(f"unsafe relative path: {value}")
            return None
        candidate = self.root / rel
        try:
            resolved = candidate.resolve(strict=True)
            resolved.relative_to(self.root)
        except FileNotFoundError:
            if required:
                self.err(f"file not found: {value}")
            return None
        except (ValueError, OSError):
            self.err(f"path escapes package or cannot be resolved: {value}")
            return None
        if not resolved.is_file():
            if required:
                self.err(f"not a file: {value}")
            return None
        return resolved

    @staticmethod
    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())

    def unique_ids(self, items, key, label):
        seen = set()
        if not isinstance(items, list):
            self.err(f"{label} must be an array")
            return
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                self.err(f"{label}[{i}] must be an object")
                continue
            ident = item.get(key)
            if not self.nonempty(ident):
                self.err(f"{label}[{i}].{key} is required")
            elif ident in seen:
                self.err(f"duplicate {key}: {ident}")
            else:
                seen.add(ident)

    def validate(self):
        self.checks.append("manifest")
        execution = self.read_json("execution.json", required=False)
        evidence = self.read_json("evidence.json")
        self.safe_file("report.html")
        if not isinstance(execution, dict):
            if isinstance(evidence, dict):
                self.err("legacy_schema_requires_migration: execution.json is absent or invalid; legacy packages are not silently upgraded")
            else:
                self.err("execution.json is required for schema v1.6.0 validation")
            return self.report()
        if not isinstance(evidence, dict):
            return self.report()

        for label, data in (("execution.json", execution), ("evidence.json", evidence)):
            if data.get("schema_version") != SCHEMA_VERSION:
                self.err(f"{label}: schema_version must be {SCHEMA_VERSION}")

        task = execution.get("task_type")
        artifact = execution.get("artifact_mode")
        if task not in TASKS: self.err("execution.json: invalid task_type")
        if artifact not in ARTIFACTS: self.err("execution.json: invalid artifact_mode")
        if evidence.get("task_type") != task: self.err("evidence.json: task_type differs from execution.json")
        if evidence.get("artifact_mode") != artifact: self.err("evidence.json: artifact_mode differs from execution.json")
        if evidence.get("study_id") != execution.get("study_id"): self.err("study_id differs between manifests")

        target = execution.get("target")
        if not isinstance(target, dict) or not self.nonempty(target.get("requested_url")) or not self.nonempty(target.get("final_url")):
            self.err("execution.json: target.requested_url and target.final_url are required")
        scope = execution.get("scope")
        if not isinstance(scope, dict):
            self.err("execution.json: scope object is required"); scope = {}
        viewports = scope.get("viewports")
        if not isinstance(viewports, list) or not viewports:
            self.err("execution.json: scope.viewports must be a non-empty array"); viewports = []
        vp_ids = set()
        for i, vp in enumerate(viewports):
            if not isinstance(vp, dict):
                self.err(f"scope.viewports[{i}] must be object"); continue
            vid = vp.get("id")
            if not self.nonempty(vid) or vid in vp_ids: self.err(f"scope.viewports[{i}]: missing or duplicate id")
            else: vp_ids.add(vid)
            if not isinstance(vp.get("width"), int) or vp["width"] <= 0 or not isinstance(vp.get("height"), int) or vp["height"] <= 0:
                self.err(f"scope.viewports[{i}]: width/height must be positive integers")
        for field in ("pages", "themes", "states", "required_checks"):
            if not isinstance(scope.get(field), list) or (field != "required_checks" and not scope[field]):
                self.err(f"execution.json: scope.{field} must be an array" + (" and non-empty" if field != "required_checks" else ""))

        samples = evidence.get("samples")
        if not isinstance(samples, list): self.err("evidence.json: samples must be array"); samples = []
        self.unique_ids(samples, "sample_id", "samples")
        sample_map = {}
        for i, sample in enumerate(samples):
            if not isinstance(sample, dict): continue
            sid = sample.get("sample_id")
            if self.nonempty(sid): sample_map[sid] = sample
            if sample.get("role") not in ROLES: self.err(f"samples[{i}].role must be source or target")
            if sample.get("status") not in {"accepted", "rejected"}: self.err(f"samples[{i}].status invalid")
            if sample.get("viewport_id") not in vp_ids: self.err(f"samples[{i}]: viewport_id not declared in execution scope")
            if sample.get("theme") not in (scope.get("themes") or []): self.err(f"samples[{i}]: theme not declared in execution scope")
            if sample.get("state_id") not in (scope.get("states") or []): self.err(f"samples[{i}]: state_id not declared in execution scope")
            readiness = sample.get("readiness")
            if not isinstance(readiness, dict) or not readiness:
                self.err(f"samples[{i}]: readiness must be a non-empty object")
            else:
                for name, control in readiness.items():
                    if not isinstance(control, dict) or control.get("status") not in READINESS or not self.nonempty(control.get("details")):
                        self.err(f"samples[{i}].readiness.{name}: requires valid status and non-empty details")
                        continue
                    if control["status"] == "NOT_APPLICABLE" and not self.nonempty(control.get("rationale")):
                        self.err(f"samples[{i}].readiness.{name}: NOT_APPLICABLE requires rationale")
            if sample.get("status") == "accepted" and isinstance(readiness, dict):
                required_controls = {"url_identity", "content_identity", "stylesheet_readiness", "asset_readiness", "render_stability", "state_integrity", "obstruction_check", "capture_integrity"}
                missing = required_controls - set(readiness)
                if missing: self.err(f"samples[{i}]: accepted sample missing readiness controls: {', '.join(sorted(missing))}")
                for name in required_controls & set(readiness):
                    ctrl = readiness[name]
                    if isinstance(ctrl, dict) and ctrl.get("status") not in {"PASS", "NOT_APPLICABLE"}:
                        self.err(f"samples[{i}]: accepted sample has non-passing readiness {name}")
            asset_ctrl = readiness.get("asset_readiness") if isinstance(readiness, dict) else None
            if isinstance(asset_ctrl, dict):
                substitutions = asset_ctrl.get("substitutions", [])
                unresolved = asset_ctrl.get("unresolved", [])
                if not isinstance(substitutions, list): self.err(f"samples[{i}].readiness.asset_readiness.substitutions must be array")
                if not isinstance(unresolved, list): self.err(f"samples[{i}].readiness.asset_readiness.unresolved must be array")
                if asset_ctrl.get("status") == "PASS" and (substitutions or unresolved):
                    self.err(f"samples[{i}]: asset_readiness PASS contradicts non-empty substitutions/unresolved assets")
            if not isinstance(sample.get("evidence_ids"), list): self.err(f"samples[{i}].evidence_ids must be array")

        registry = evidence.get("evidence_registry")
        if not isinstance(registry, list): self.err("evidence_registry must be array"); registry = []
        self.unique_ids(registry, "evidence_id", "evidence_registry")
        evidence_ids = {e.get("evidence_id") for e in registry if isinstance(e, dict) and self.nonempty(e.get("evidence_id"))}
        for i, ev in enumerate(registry):
            if not isinstance(ev, dict): continue
            if ev.get("type") not in {"screenshot","dom","computed_style","stylesheet","asset","network","manual_note","test_result"}:
                self.err(f"evidence_registry[{i}].type invalid")
            path = ev.get("path")
            if path is not None: self.safe_file(path)
            elif not self.nonempty(ev.get("source_ref")): self.err(f"evidence_registry[{i}]: path or source_ref required")
        for i, sample in enumerate(samples):
            if not isinstance(sample, dict): continue
            for eid in sample.get("evidence_ids", []) if isinstance(sample.get("evidence_ids"), list) else []:
                if eid not in evidence_ids: self.err(f"samples[{i}]: unknown evidence_id {eid}")

        findings = evidence.get("findings")
        if not isinstance(findings, list): self.err("findings must be array"); findings = []
        self.unique_ids(findings, "finding_id", "findings")
        for i, finding in enumerate(findings):
            if not isinstance(finding, dict): continue
            if not self.nonempty(finding.get("claim")): self.err(f"findings[{i}].claim required")
            if finding.get("classification") not in {"observed","inferred","estimated","unknown","recommendation"}:
                self.err(f"findings[{i}].classification invalid")
            refs = finding.get("evidence_ids")
            if not isinstance(refs, list): self.err(f"findings[{i}].evidence_ids must be array"); continue
            if finding.get("classification") == "observed" and not refs: self.err(f"findings[{i}]: observed claim requires evidence")
            for eid in refs:
                if eid not in evidence_ids: self.err(f"findings[{i}]: unknown evidence_id {eid}")
            if finding.get("classification") == "estimated" and not self.nonempty(finding.get("method")):
                self.err(f"findings[{i}]: estimated claim requires method")

        outcomes = evidence.get("outcomes")
        if not isinstance(outcomes, dict): self.err("outcomes object required"); outcomes = {}
        for key, item in outcomes.items():
            if not isinstance(item, dict) or item.get("status") not in OUTCOMES or not self.nonempty(item.get("rationale")):
                self.err(f"outcomes.{key}: requires valid status and rationale")
        results = evidence.get("results")
        if not isinstance(results, dict): self.err("results object required"); results = {}
        for key in ("execution_completeness", "package_validation", "task_acceptance"):
            if not isinstance(results.get(key), str) or results[key] not in OUTCOMES:
                self.err(f"results.{key}: valid outcome status required")

        if task in {"reconstruction", "comparison"}:
            self.checks.append("paired-comparison")
            comp = self.read_json("comparison.json")
            if not isinstance(comp, dict): comp = {}
            if comp.get("schema_version") != SCHEMA_VERSION: self.err(f"comparison.json: schema_version must be {SCHEMA_VERSION}")
            if comp.get("study_id") != execution.get("study_id"): self.err("comparison.json: study_id mismatch")
            criteria = comp.get("criteria")
            if not isinstance(criteria, list): self.err("comparison.json: criteria must be array"); criteria = []
            crit_map = {}
            for c in criteria:
                if isinstance(c, dict) and self.nonempty(c.get("criterion_id")):
                    if c["criterion_id"] in crit_map: self.err(f"duplicate criterion_id {c['criterion_id']}")
                    crit_map[c["criterion_id"]] = c
            for req in scope.get("required_checks", []):
                if req not in crit_map: self.err(f"comparison.json: required criterion missing: {req}")
            for c in criteria:
                if not isinstance(c, dict): continue
                if c.get("status") not in OUTCOMES: self.err(f"criterion {c.get('criterion_id')}: invalid status")
                if c.get("required") is True and c.get("status") == "PASS" and not c.get("evidence_ids"):
                    self.err(f"criterion {c.get('criterion_id')}: PASS requires evidence_ids")
                for eid in c.get("evidence_ids", []):
                    if eid not in evidence_ids: self.err(f"criterion {c.get('criterion_id')}: unknown evidence_id {eid}")
            comparisons = comp.get("comparisons")
            if not isinstance(comparisons, list): self.err("comparison.json: comparisons must be array"); comparisons = []
            self.unique_ids(comparisons, "comparison_id", "comparisons")
            pair_coverage = set()
            for i, pair in enumerate(comparisons):
                if not isinstance(pair, dict): continue
                for f in ("viewport_id","theme","state_id","element_id","match_status","source_sample_id","target_sample_id","source","target","deltas","tolerances","result","evidence_ids"):
                    if f not in pair: self.err(f"comparisons[{i}]: missing {f}")
                if pair.get("match_status") not in {"matched","unmatched","ambiguous"}: self.err(f"comparisons[{i}]: invalid match_status")
                if pair.get("result") not in OUTCOMES: self.err(f"comparisons[{i}]: invalid result")
                src = sample_map.get(pair.get("source_sample_id")); dst = sample_map.get(pair.get("target_sample_id"))
                if not src or src.get("role") != "source" or not dst or dst.get("role") != "target":
                    self.err(f"comparisons[{i}]: source/target sample references invalid")
                else:
                    if src.get("status") != "accepted" or dst.get("status") != "accepted":
                        self.err(f"comparisons[{i}]: rejected sample cannot be compared")
                    if src.get("viewport_id") != pair.get("viewport_id") or dst.get("viewport_id") != pair.get("viewport_id"):
                        self.err(f"comparisons[{i}]: viewport mismatch")
                    if src.get("theme") != pair.get("theme") or dst.get("theme") != pair.get("theme"):
                        self.err(f"comparisons[{i}]: theme mismatch")
                    if src.get("state_id") != pair.get("state_id") or dst.get("state_id") != pair.get("state_id"):
                        self.err(f"comparisons[{i}]: state mismatch")
                if pair.get("match_status") == "matched" and not self.nonempty(pair.get("element_id")):
                    self.err(f"comparisons[{i}]: matched pair requires element_id")
                tol = pair.get("tolerances")
                if not isinstance(tol, dict) or not tol:
                    self.err(f"comparisons[{i}]: tolerances required")
                else:
                    for k, v in tol.items():
                        if not isinstance(v, (int,float)) or v < 0: self.err(f"comparisons[{i}]: tolerance {k} must be non-negative number")
                for eid in pair.get("evidence_ids", []):
                    if eid not in evidence_ids: self.err(f"comparisons[{i}]: unknown evidence_id {eid}")
                pair_coverage.add((pair.get("viewport_id"),pair.get("theme"),pair.get("state_id")))
            required_combos = {(v.get("id"),t,s) for v in viewports if isinstance(v,dict) for t in scope.get("themes",[]) for s in scope.get("states",[])}
            # At least one paired comparison per required viewport/theme/state; element coverage is checked separately by required criteria.
            missing = required_combos - pair_coverage
            if missing: self.err(f"comparison.json: missing paired coverage combinations: {sorted(missing)}")
            deps = evidence.get("dependencies", [])
            if artifact == "standalone_mockup":
                if not isinstance(deps, list): self.err("standalone_mockup: dependencies must be array"); deps=[]
                for dep in deps:
                    if isinstance(dep, dict) and dep.get("disposition") == "retained" and dep.get("runtime_origin") == "source_origin":
                        self.err("standalone_mockup cannot retain runtime dependency on source origin")

        # v1.6.0 fidelity, interaction, and screenshot gates.
        if task == "reconstruction":
            self.checks.append("fidelity-runtime")
            fidelity = evidence.get("fidelity")
            required_dims = {"visual_fidelity", "functional_fidelity", "responsive_fidelity", "content_fidelity", "asset_fidelity"}
            if not isinstance(fidelity, dict):
                self.err("evidence.json: fidelity object required for reconstruction")
                fidelity = {}
            for dim in required_dims:
                item = fidelity.get(dim)
                if not isinstance(item, dict) or item.get("status") not in OUTCOMES or not self.nonempty(item.get("rationale")):
                    self.err(f"fidelity.{dim}: requires valid status and rationale")
                elif item.get("status") == "PASS" and not item.get("evidence_ids"):
                    self.err(f"fidelity.{dim}: PASS requires evidence_ids")
                elif isinstance(item, dict):
                    for eid in item.get("evidence_ids", []):
                        if eid not in evidence_ids: self.err(f"fidelity.{dim}: unknown evidence_id {eid}")

            runtime = self.read_json("measurements/runtime-tests.json", required=False)
            if not isinstance(runtime, dict):
                self.err("reconstruction requires measurements/runtime-tests.json")
                runtime = {}
            interactions = runtime.get("interactions")
            if not isinstance(interactions, list):
                self.err("runtime-tests.json: interactions array required")
                interactions = []
            controls = [x for x in interactions if isinstance(x, dict)]
            for i, control in enumerate(controls):
                for field in ("control_id", "role", "accessible_name", "source_status", "source_action", "source_result", "target_status", "target_action", "target_result", "result", "evidence_ids"):
                    if field not in control: self.err(f"runtime-tests.interactions[{i}]: missing {field}")
                if control.get("source_status") not in OUTCOMES or control.get("target_status") not in OUTCOMES or control.get("result") not in OUTCOMES:
                    self.err(f"runtime-tests.interactions[{i}]: invalid source/target/result status")
                for eid in control.get("evidence_ids", []):
                    if eid not in evidence_ids: self.err(f"runtime-tests.interactions[{i}]: unknown evidence_id {eid}")
            if fidelity.get("functional_fidelity", {}).get("status") == "PASS" and any(
                x.get("source_status") != "PASS" or x.get("target_status") != "PASS" or x.get("result") != "PASS"
                for x in controls
            ):
                self.err("functional_fidelity PASS contradicts untested or failed interaction coverage")
            if runtime.get("resolved_font_status") not in {"PASS", "FAIL", "NOT_TESTED"}:
                self.err("runtime-tests.json: resolved_font_status required")
            if not isinstance(runtime.get("font_runs"), list): self.err("runtime-tests.json: font_runs array required")

            visual = self.read_json("visual-comparison.json", required=False)
            if not isinstance(visual, dict):
                self.err("reconstruction requires visual-comparison.json")
                visual = {}
            if visual.get("schema_version") != SCHEMA_VERSION: self.err("visual-comparison.json: schema_version must be 1.6.0")
            if visual.get("study_id") != execution.get("study_id"): self.err("visual-comparison.json: study_id mismatch")
            pairs = visual.get("pairs")
            if not isinstance(pairs, list): self.err("visual-comparison.json: pairs array required"); pairs = []
            visual_coverage = set()
            for i, pair in enumerate(pairs):
                if not isinstance(pair, dict): self.err(f"visual-comparison.pairs[{i}] must be object"); continue
                for field in ("viewport_id", "theme", "state_id", "source_screenshot", "target_screenshot", "dimensions", "metric_value", "threshold", "masked_regions", "result", "evidence_ids"):
                    if field not in pair: self.err(f"visual-comparison.pairs[{i}]: missing {field}")
                for field in ("source_screenshot", "target_screenshot"):
                    self.safe_file(pair.get(field))
                if pair.get("result") not in OUTCOMES: self.err(f"visual-comparison.pairs[{i}]: invalid result")
                if not isinstance(pair.get("dimensions"), dict): self.err(f"visual-comparison.pairs[{i}]: dimensions object required")
                if not isinstance(pair.get("masked_regions"), list): self.err(f"visual-comparison.pairs[{i}]: masked_regions array required")
                for eid in pair.get("evidence_ids", []):
                    if eid not in evidence_ids: self.err(f"visual-comparison.pairs[{i}]: unknown evidence_id {eid}")
                visual_coverage.add((pair.get("viewport_id"), pair.get("theme"), pair.get("state_id")))
            required_visual = {(v.get("id"), t, st) for v in viewports if isinstance(v, dict) for t in scope.get("themes", []) for st in scope.get("states", [])}
            missing_visual = required_visual - visual_coverage
            if missing_visual: self.err(f"visual-comparison.json: missing screenshot comparison coverage: {sorted(missing_visual)}")
            if fidelity.get("visual_fidelity", {}).get("status") == "PASS" and any(
                p.get("result") != "PASS" for p in pairs if isinstance(p, dict)
            ):
                self.err("visual_fidelity PASS contradicts non-passing screenshot comparison")

        # Enforce outcome consistency against required comparison criteria.
        if task in {"reconstruction","comparison"} and isinstance(comp, dict):
            req_statuses = [c.get("status") for c in comp.get("criteria", []) if isinstance(c,dict) and c.get("required") is True]
            acceptance = results.get("task_acceptance")
            if acceptance == "PASS" and any(s != "PASS" for s in req_statuses):
                self.err("task_acceptance PASS contradicts required comparison criterion")
            if acceptance == "PASS" and any(s != "PASS" for s in req_statuses):
                self.err("task_acceptance PASS requires every required criterion to PASS")
            if acceptance == "PASS" and not req_statuses:
                self.err("task_acceptance PASS requires at least one required criterion")
            if acceptance == "PASS" and task == "reconstruction":
                fidelity = evidence.get("fidelity", {})
                required_dims = {"visual_fidelity", "functional_fidelity", "responsive_fidelity", "content_fidelity", "asset_fidelity"}
                nonpassing = [d for d in required_dims if not isinstance(fidelity.get(d), dict) or fidelity[d].get("status") != "PASS"]
                if nonpassing:
                    self.err(f"task_acceptance PASS requires all fidelity dimensions to PASS: {sorted(nonpassing)}")
        if task in {"analysis","audit"} and results.get("task_acceptance") == "PASS":
            if not samples or any(s.get("status") != "accepted" for s in samples if isinstance(s,dict)):
                self.err("analysis/audit task_acceptance PASS requires accepted samples")
        if artifact == "not_applicable" and task == "reconstruction":
            self.err("reconstruction task cannot use artifact_mode not_applicable")

        self.checks.append("outcome-consistency")
        return self.report()

    def report(self):
        return {
            "validator_version": VERSION,
            "schema_version": SCHEMA_VERSION,
            "validation_status": "PASS" if not self.errors else "FAIL",
            "errors": self.errors,
            "warnings": self.warnings,
            "checks_run": self.checks,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate-evidence.py <package-directory>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).expanduser()
    if not root.is_dir():
        print(f"ERROR: package directory not found: {root}", file=sys.stderr)
        return 2
    validator = Validator(root)
    report = validator.validate()
    validation_dir = root / "validation"
    try:
        validation_dir.mkdir(exist_ok=True)
        (validation_dir / "validator-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    except OSError:
        pass
    if report["errors"]:
        print(f"FAIL: {len(report['errors'])} validation error(s)")
        for error in report["errors"]:
            print(f"- {error}")
        return 1
    print("PASS: schema, references, declared scope and outcome consistency validated")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
