import json
import shutil
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
import importlib.util
spec = importlib.util.spec_from_file_location("validate_evidence", ROOT / "scripts" / "validate-evidence.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Validator = module.Validator

def make_package(root: Path, *, task="reconstruction", artifact="standalone_mockup"):
    (root / "screenshots" / "source").mkdir(parents=True, exist_ok=True)
    (root / "screenshots" / "target").mkdir(parents=True, exist_ok=True)
    (root / "report.html").write_text("<html><body>test report</body></html>", encoding="utf-8")
    for p in ("screenshots/source/source.png", "screenshots/target/target.png"):
        (root / p).write_bytes(b"fake-image-fixture")
    execution = {
        "schema_version":"1.5.0","study_id":"test-study","task_type":task,"artifact_mode":artifact,
        "target":{"requested_url":"https://example.test/","final_url":"https://example.test/"},
        "scope":{"pages":["/"],"viewports":[{"id":"desktop","width":1280,"height":900}],
                 "themes":["light"],"states":["default"],
                 "required_checks":["content_state","geometry","important_styles","document_overflow","component_overflow","asset_completeness"]},
        "capabilities":{"browser":"available","screenshots":"available"},"constraints":[],"created_at":"2026-11-08T08:00:00Z"
    }
    readiness = {k:{"status":"PASS","details":"verified"} for k in
        ("url_identity","content_identity","stylesheet_readiness","asset_readiness","render_stability","state_integrity","obstruction_check","capture_integrity")}
    evidence = {
        "schema_version":"1.5.0","study_id":"test-study","task_type":task,"artifact_mode":artifact,
        "created_at":"2026-11-08T08:00:00Z","target":execution["target"],
        "samples":[
            {"sample_id":"src-1","role":"source","status":"accepted","viewport_id":"desktop","theme":"light","state_id":"default","scroll_position_css_px":{"x":0,"y":0},"readiness":readiness,"evidence_ids":["ev-src"]},
            {"sample_id":"dst-1","role":"target","status":"accepted","viewport_id":"desktop","theme":"light","state_id":"default","scroll_position_css_px":{"x":0,"y":0},"readiness":readiness,"evidence_ids":["ev-dst"]}
        ],
        "evidence_registry":[
            {"evidence_id":"ev-src","type":"screenshot","path":"screenshots/source/source.png","captured_at":"2026-11-08T08:00:00Z","provenance":"test fixture"},
            {"evidence_id":"ev-dst","type":"screenshot","path":"screenshots/target/target.png","captured_at":"2026-11-08T08:00:00Z","provenance":"test fixture"}
        ],
        "findings":[{"finding_id":"f1","claim":"The fixture was captured.","classification":"observed","evidence_ids":["ev-src"]}],
        "limitations":[],"outcomes":{"reconstruction":{"status":"PASS","rationale":"fixture passes"}},
        "results":{"execution_completeness":"PASS","package_validation":"PASS","task_acceptance":"PASS"},
        "dependencies":[]
    }
    comparison = {
        "schema_version":"1.5.0","study_id":"test-study",
        "criteria":[{"criterion_id":c,"required":True,"status":"PASS","evidence_ids":["ev-src","ev-dst"]}
                    for c in execution["scope"]["required_checks"]],
        "comparisons":[{"comparison_id":"cmp-1","viewport_id":"desktop","theme":"light","state_id":"default",
            "element_id":"header.primary","match_status":"matched","source_sample_id":"src-1","target_sample_id":"dst-1",
            "source":{"rect":{"x":0,"y":0,"width":1280,"height":80}},
            "target":{"rect":{"x":0,"y":0,"width":1280,"height":80}},
            "deltas":{"geometry":{"height_css_px":0}},"tolerances":{"geometry_css_px":2},
            "result":"PASS","evidence_ids":["ev-src","ev-dst"]}]
    }
    for name, data in (("execution.json",execution),("evidence.json",evidence),("comparison.json",comparison)):
        (root / name).write_text(json.dumps(data, indent=2), encoding="utf-8")

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        make_package(self.root)
    def tearDown(self):
        self.tmp.cleanup()
    def data(self, name):
        p=self.root/name
        return json.loads(p.read_text(encoding="utf-8"))
    def save(self,name,obj):
        (self.root/name).write_text(json.dumps(obj,indent=2),encoding="utf-8")
    def errors(self):
        return Validator(self.root).validate()["errors"]
    def test_valid_reconstruction_package(self):
        self.assertEqual(self.errors(), [])
    def test_empty_readiness_rejected(self):
        d=self.data("evidence.json"); d["samples"][0]["readiness"]={}; self.save("evidence.json",d)
        self.assertTrue(any("readiness" in e for e in self.errors()))
    def test_accepted_sample_with_failed_readiness_rejected(self):
        d=self.data("evidence.json"); d["samples"][0]["readiness"]["render_stability"]["status"]="FAIL"; self.save("evidence.json",d)
        self.assertTrue(any("accepted sample" in e for e in self.errors()))
    def test_pass_contradicting_failed_required_check_rejected(self):
        d=self.data("comparison.json"); d["criteria"][1]["status"]="FAIL"; self.save("comparison.json",d)
        self.assertTrue(any("task_acceptance PASS contradicts" in e for e in self.errors()))
    def test_missing_required_viewport_pair_rejected(self):
        d=self.data("comparison.json"); d["comparisons"]=[]; self.save("comparison.json",d)
        self.assertTrue(any("missing paired coverage" in e for e in self.errors()))
    def test_unknown_evidence_reference_rejected(self):
        d=self.data("evidence.json"); d["findings"][0]["evidence_ids"]=["not-real"]; self.save("evidence.json",d)
        self.assertTrue(any("unknown evidence_id" in e for e in self.errors()))
    def test_source_dependency_in_standalone_rejected(self):
        d=self.data("evidence.json"); d["dependencies"]=[{"disposition":"retained","runtime_origin":"source_origin"}]; self.save("evidence.json",d)
        self.assertTrue(any("cannot retain runtime dependency" in e for e in self.errors()))
    def test_parent_path_rejected(self):
        d=self.data("evidence.json"); d["evidence_registry"][0]["path"]="../outside.png"; self.save("evidence.json",d)
        self.assertTrue(any("unsafe relative path" in e for e in self.errors()))
    def test_symlink_escape_rejected(self):
        outside=self.root.parent/"outside-fixture.txt"; outside.write_text("x",encoding="utf-8")
        try:
            (self.root/"escape.txt").symlink_to(outside)
            d=self.data("evidence.json"); d["evidence_registry"][0]["path"]="escape.txt"; self.save("evidence.json",d)
            self.assertTrue(any("escapes package" in e for e in self.errors()))
        finally:
            outside.unlink(missing_ok=True)
    def test_mismatched_viewport_pair_rejected(self):
        d=self.data("evidence.json"); d["samples"][1]["viewport_id"]="other"; self.save("evidence.json",d)
        self.assertTrue(any("viewport mismatch" in e for e in self.errors()))
    def test_missing_comparison_tolerance_rejected(self):
        d=self.data("comparison.json"); d["comparisons"][0]["tolerances"]={}; self.save("comparison.json",d)
        self.assertTrue(any("tolerances required" in e for e in self.errors()))
    def test_missing_report_rejected(self):
        (self.root/"report.html").unlink()
        self.assertTrue(any("report.html" in e for e in self.errors()))
    def test_analysis_manifest_validates_without_comparison(self):
        make_package(self.root, task="analysis", artifact="not_applicable")
        e=self.data("evidence.json"); e["samples"]=e["samples"][:1]; e["results"]["task_acceptance"]="PASS"; self.save("evidence.json",e)
        (self.root/"comparison.json").unlink()
        self.assertEqual(self.errors(), [])

    def test_legacy_package_without_execution_manifest_requires_migration(self):
        legacy_root = self.root / "legacy"
        legacy_root.mkdir()
        (legacy_root / "report.html").write_text("<html><body>legacy fixture</body></html>", encoding="utf-8")
        legacy_evidence = {
            "schema_version": "1.4.0",
            "study_id": "synthetic-legacy-study",
            "samples": [],
            "evidence": []
        }
        (legacy_root / "evidence.json").write_text(json.dumps(legacy_evidence), encoding="utf-8")
        report = Validator(legacy_root).validate()
        self.assertEqual(report["validation_status"], "FAIL")
        self.assertTrue(any("legacy_schema_requires_migration" in e for e in report["errors"]))

    def test_unsupported_schema_version_rejected(self):
        d=self.data("execution.json"); d["schema_version"]="1.4.0"; self.save("execution.json",d)
        self.assertTrue(any("schema_version must be 1.5.0" in e for e in self.errors()))

    def test_duplicate_sample_id_rejected(self):
        d=self.data("evidence.json"); d["samples"][1]["sample_id"]="src-1"; self.save("evidence.json",d)
        self.assertTrue(any("duplicate sample_id" in e for e in self.errors()))

    def test_missing_required_criterion_rejected(self):
        d=self.data("comparison.json"); d["criteria"]=[c for c in d["criteria"] if c["criterion_id"]!="geometry"]; self.save("comparison.json",d)
        self.assertTrue(any("required criterion missing: geometry" in e for e in self.errors()))

    def test_missing_element_identity_rejected(self):
        d=self.data("comparison.json"); d["comparisons"][0]["element_id"]=""; self.save("comparison.json",d)
        self.assertTrue(any("matched pair requires element_id" in e for e in self.errors()))

    def test_comparison_unknown_evidence_rejected(self):
        d=self.data("comparison.json"); d["comparisons"][0]["evidence_ids"]=["missing"]; self.save("comparison.json",d)
        self.assertTrue(any("unknown evidence_id" in e for e in self.errors()))

    def test_required_not_tested_blocks_pass(self):
        d=self.data("comparison.json"); d["criteria"][0]["status"]="NOT_TESTED"; self.save("comparison.json",d)
        self.assertTrue(any("task_acceptance PASS contradicts" in e for e in self.errors()))

    def test_rejected_sample_cannot_be_compared(self):
        d=self.data("evidence.json"); d["samples"][0]["status"]="rejected"; self.save("evidence.json",d)
        self.assertTrue(any("rejected sample cannot be compared" in e for e in self.errors()))

    def test_missing_required_readiness_control_rejected(self):
        d=self.data("evidence.json"); del d["samples"][0]["readiness"]["asset_readiness"]; self.save("evidence.json",d)
        self.assertTrue(any("missing readiness controls" in e for e in self.errors()))

    def test_invalid_artifact_mode_rejected(self):
        d=self.data("execution.json"); d["artifact_mode"]="maybe"; self.save("execution.json",d)
        self.assertTrue(any("invalid artifact_mode" in e for e in self.errors()))

    def test_observed_finding_without_evidence_rejected(self):
        d=self.data("evidence.json"); d["findings"][0]["evidence_ids"]=[]; self.save("evidence.json",d)
        self.assertTrue(any("observed claim requires evidence" in e for e in self.errors()))

    def test_estimated_finding_without_method_rejected(self):
        d=self.data("evidence.json"); d["findings"][0]["classification"]="estimated"; d["findings"][0].pop("method",None); self.save("evidence.json",d)
        self.assertTrue(any("estimated claim requires method" in e for e in self.errors()))

if __name__ == "__main__":
    unittest.main()
