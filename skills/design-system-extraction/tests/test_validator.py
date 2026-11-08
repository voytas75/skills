import json, tempfile, unittest, importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("validator",ROOT/"scripts"/"validate-evidence.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
Validator=mod.Validator

def package(root, ledger_status="MEASURED", sample_status="valid", asset_status="PARTIAL"):
    (root/"screenshots").mkdir(exist_ok=True); (root/"measurements").mkdir(exist_ok=True)
    (root/"report.html").write_text("<html>report</html>",encoding="utf-8")
    for f in ("s.png","t.png"): (root/"screenshots"/f).write_bytes(b"synthetic")
    execution={"schema_version":"1.6.1","study_id":"synthetic-1","task_type":"reconstruction",
      "artifact_mode":"standalone_mockup","target":{"requested_url":"https://example.invalid","final_url":"https://example.invalid"},
      "scope":{"pages":["/"],"viewports":[{"id":"desktop","width":1280,"height":800}],
      "themes":["light"],"states":["initial"],"required_checks":["geometry","asset_completeness"]}}
    controls={k:{"status":"PASS","details":"synthetic stable capture"} for k in
      ("url_identity","content_identity","render_stability","state_integrity","obstruction_check","capture_integrity")}
    sample=lambda sid,role,path: {"sample_id":sid,"role":role,"captured_at":"2026-11-08T00:00:00Z",
      "viewport_id":"desktop","theme":"light","state_id":"initial","scroll_position_css_px":{"x":0,"y":0},
      "capture_status":sample_status,"capture_readiness":controls,
      "asset_audit":{"status":asset_status,"substitutions":[{"asset":"font","replacement":"Arial","reason":"policy"}] if asset_status!="PASS" else [],
        "unresolved":[]},
      "measurement_eligibility":{m:{"status":"eligible","reason":"capture supports this modality"} for m in
       ("content","geometry","styles","visual","responsive","interaction","font_identity","asset_identity")},
      "evidence_ids":[path]}
    samples=[sample("src","source","ev-s"),sample("dst","target","ev-t")]
    registry=[{"evidence_id":"ev-s","type":"screenshot","path":"screenshots/s.png","provenance":"synthetic"},
      {"evidence_id":"ev-t","type":"screenshot","path":"screenshots/t.png","provenance":"synthetic"}]
    dims=("visual_fidelity","functional_fidelity","responsive_fidelity","content_fidelity","asset_fidelity")
    evidence={"schema_version":"1.6.1","study_id":"synthetic-1","task_type":"reconstruction","artifact_mode":"standalone_mockup",
      "samples":samples,"evidence_registry":registry,"findings":[{"finding_id":"f1","claim":"synthetic capture","classification":"observed","evidence_ids":["ev-s"]}],
      "fidelity":{d:{"status":"PASS","rationale":"synthetic","evidence_ids":["ev-s","ev-t"]} for d in dims},
      "dependencies":[],"results":{"execution_completeness":"PASS","package_validation":"PASS","task_acceptance":"PASS"}}
    criteria=[{"criterion_id":c,"required":True,"status":"PASS","evidence_ids":["ev-s","ev-t"]} for c in ("geometry","asset_completeness")]
    comparison={"schema_version":"1.6.1","study_id":"synthetic-1","criteria":criteria,"comparisons":[{
      "comparison_id":"cmp-1","viewport_id":"desktop","theme":"light","state_id":"initial","modality":"geometry",
      "element_id":"header","match_status":"matched","source_sample_id":"src","target_sample_id":"dst",
      "source":{"rect":{"x":0,"y":0,"width":1280,"height":80}},"target":{"rect":{"x":0,"y":0,"width":1280,"height":80}},
      "deltas":{"height":0},"tolerances":{"geometry_css_px":2},"alignment":{"method":"exact_scroll"},
      "result":"PASS","evidence_ids":["ev-s","ev-t"]}]}
    modalities=["geometry","visual"]
    entries=[]
    for m in modalities:
      e={"entry_id":"entry-"+m,"viewport_id":"desktop","theme":"light","state_id":"initial","modality":m,"status":ledger_status,
         "evidence_ids":["ev-s","ev-t"]}
      if ledger_status=="MEASURED":
        e.update({"source_sample_id":"src","target_sample_id":"dst","result":"PASS",
          "metric":{"name":"synthetic-metric","value":0.0,"unit":"normalized"},"alignment":{"method":"exact_scroll"}})
      else: e["reason"]="synthetic test did not produce comparable capture"
      entries.append(e)
    ledger={"schema_version":"1.6.1","study_id":"synthetic-1","required_modalities":modalities,"entries":entries}
    visual={"schema_version":"1.6.1","study_id":"synthetic-1","pairs":[{"viewport_id":"desktop","theme":"light","state_id":"initial",
      "source_screenshot":"screenshots/s.png","target_screenshot":"screenshots/t.png","result":"PASS","evidence_ids":["ev-s","ev-t"]}]}
    runtime={"interactions":[{"control_id":"menu","source_status":"PASS","target_status":"PASS","result":"PASS"}],
      "resolved_font_status":"NOT_TESTED","font_runs":[]}
    for name,obj in (("execution.json",execution),("evidence.json",evidence),("comparison.json",comparison),
      ("pair-ledger.json",ledger),("visual-comparison.json",visual)):
      (root/name).write_text(json.dumps(obj,indent=2),encoding="utf-8")
    (root/"measurements"/"runtime-tests.json").write_text(json.dumps(runtime,indent=2),encoding="utf-8")

class Tests(unittest.TestCase):
  def setUp(self):
    self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name); package(self.root)
  def tearDown(self): self.tmp.cleanup()
  def data(self,n): return json.loads((self.root/n).read_text())
  def save(self,n,x): (self.root/n).write_text(json.dumps(x,indent=2))
  def errors(self): return Validator(self.root).validate()["errors"]
  def test_valid(self): self.assertEqual(self.errors(),[])
  def test_substitution_does_not_block_capture_or_geometry(self):
    e=self.data("evidence.json"); self.assertEqual(e["samples"][1]["capture_status"],"valid")
    self.assertEqual(e["samples"][1]["measurement_eligibility"]["geometry"]["status"],"eligible")
    self.assertEqual(self.errors(),[])
  def test_asset_pass_with_substitution_rejected(self):
    e=self.data("evidence.json"); e["samples"][1]["asset_audit"]["status"]="PASS"; self.save("evidence.json",e)
    self.assertTrue(any("asset_audit PASS contradicts" in x for x in self.errors()))
  def test_asset_partial_does_not_reject_geometry_pair(self):
    self.assertFalse(any("ineligible" in x for x in self.errors()))
  def test_missing_ledger_rejected(self):
    (self.root/"pair-ledger.json").unlink()
    self.assertTrue(any("missing required file: pair-ledger.json" in x for x in self.errors()))
  def test_missing_combination_rejected(self):
    l=self.data("pair-ledger.json"); l["entries"].pop(); self.save("pair-ledger.json",l)
    self.assertTrue(any("missing coverage" in x for x in self.errors()))
  def test_duplicate_combination_rejected(self):
    l=self.data("pair-ledger.json"); l["entries"].append(dict(l["entries"][0],entry_id="duplicate")); self.save("pair-ledger.json",l)
    self.assertTrue(any("duplicate ledger combination" in x for x in self.errors()))
  def test_not_tested_is_valid_package_record(self):
    package(self.root,ledger_status="NOT_TESTED")
    e=self.data("evidence.json"); e["results"]["execution_completeness"]="PARTIAL"; e["results"]["task_acceptance"]="FAIL"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_not_tested_cannot_support_acceptance_pass(self):
    e=self.data("evidence.json"); e["results"]["task_acceptance"]="PASS"
    package(self.root,ledger_status="NOT_TESTED")
    e=self.data("evidence.json"); e["results"]["task_acceptance"]="PASS"; self.save("evidence.json",e)
    self.assertTrue(any("task_acceptance PASS contradicts ledger" in x for x in self.errors()))
  def test_measured_fail_is_valid_package_record(self):
    l=self.data("pair-ledger.json")
    for x in l["entries"]: x["result"]="FAIL"
    self.save("pair-ledger.json",l)
    v=self.data("visual-comparison.json"); v["pairs"][0]["result"]="FAIL"; self.save("visual-comparison.json",v)
    e=self.data("evidence.json"); e["results"]["task_acceptance"]="FAIL"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_measured_requires_metric(self):
    l=self.data("pair-ledger.json"); l["entries"][0].pop("metric"); self.save("pair-ledger.json",l)
    self.assertTrue(any("requires metric" in x for x in self.errors()))
  def test_unmeasured_cannot_have_metric(self):
    l=self.data("pair-ledger.json"); l["entries"][0]["status"]="NOT_TESTED"; l["entries"][0]["reason"]="not run"; l["entries"][0].pop("result"); l["entries"][0].pop("metric")
    self.save("pair-ledger.json",l)
    e=self.data("evidence.json"); e["results"]["execution_completeness"]="PARTIAL"; e["results"]["task_acceptance"]="FAIL"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_rejected_legacy_sample_can_be_eligible_modality(self):
    e=self.data("evidence.json"); e["samples"][0]["status"]="rejected"; e["samples"][0]["capture_status"]="partial"
    e["samples"][0]["measurement_eligibility"]["geometry"]["status"]="eligible"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_modality_ineligible_blocks_only_that_modality(self):
    e=self.data("evidence.json"); e["samples"][0]["measurement_eligibility"]["font_identity"]["status"]="ineligible"
    e["samples"][0]["measurement_eligibility"]["font_identity"]["reason"]="resolved font unknown"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_pair_cannot_use_ineligible_modality(self):
    e=self.data("evidence.json"); e["samples"][0]["measurement_eligibility"]["geometry"]["status"]="ineligible"
    e["samples"][0]["measurement_eligibility"]["geometry"]["reason"]="invalid rect"; self.save("evidence.json",e)
    self.assertTrue(any("ineligible for geometry" in x for x in self.errors()))
  def test_footer_shared_anchor_allowed(self):
    c=self.data("comparison.json"); c["comparisons"][0]["alignment"]={"method":"shared_anchor","rationale":"align document_bottom","source_anchor":"document_bottom","target_anchor":"document_bottom","source_scroll_y":1000,"target_scroll_y":1200}
    self.save("comparison.json",c); self.assertEqual(self.errors(),[])
  def test_nonexact_alignment_requires_reason(self):
    c=self.data("comparison.json"); c["comparisons"][0]["alignment"]={"method":"shared_anchor"}
    self.save("comparison.json",c); self.assertTrue(any("requires rationale" in x for x in self.errors()))
  def test_undeclared_viewport_in_ledger_rejected(self):
    l=self.data("pair-ledger.json"); l["entries"][0]["viewport_id"]="tablet"; self.save("pair-ledger.json",l)
    self.assertTrue(any("undeclared combination" in x for x in self.errors()))
  def test_bad_status_rejected(self):
    l=self.data("pair-ledger.json"); l["entries"][0]["status"]="PASS"; self.save("pair-ledger.json",l)
    self.assertTrue(any("status invalid" in x for x in self.errors()))
  def test_capture_valid_contradiction_rejected(self):
    e=self.data("evidence.json"); e["samples"][0]["capture_readiness"]["render_stability"]["status"]="FAIL"; self.save("evidence.json",e)
    self.assertTrue(any("capture_status valid contradicts" in x for x in self.errors()))
  def test_invalid_capture_can_still_be_recorded(self):
    e=self.data("evidence.json"); e["samples"][0]["capture_status"]="invalid"
    for item in e["samples"][0]["measurement_eligibility"].values():
      item["status"]="ineligible"; item["reason"]="capture unstable"
    self.save("evidence.json",e)
    c=self.data("comparison.json"); c["comparisons"]=[]; self.save("comparison.json",c)
    l=self.data("pair-ledger.json")
    for x in l["entries"]:
      x["status"]="BLOCKED"; x["reason"]="source capture invalid"; x.pop("source_sample_id",None); x.pop("target_sample_id",None); x.pop("result",None); x.pop("metric",None); x.pop("alignment",None)
    self.save("pair-ledger.json",l)
    e=self.data("evidence.json"); e["results"]["execution_completeness"]="PARTIAL"; e["results"]["task_acceptance"]="FAIL"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_unknown_evidence_ref_rejected(self):
    e=self.data("evidence.json"); e["findings"][0]["evidence_ids"]=["missing"]; self.save("evidence.json",e)
    self.assertTrue(any("unknown evidence_id" in x for x in self.errors()))
  def test_path_traversal_rejected(self):
    e=self.data("evidence.json"); e["evidence_registry"][0]["path"]="../bad.png"; self.save("evidence.json",e)
    self.assertTrue(any("unsafe path" in x for x in self.errors()))
  def test_missing_report_rejected(self):
    (self.root/"report.html").unlink(); self.assertTrue(any("report.html" in x for x in self.errors()))
  def test_schema_version_rejected(self):
    e=self.data("evidence.json"); e["schema_version"]="1.6.0"; self.save("evidence.json",e)
    self.assertTrue(any("schema_version must be 1.6.1" in x for x in self.errors()))
  def test_study_mismatch_rejected(self):
    l=self.data("pair-ledger.json"); l["study_id"]="other"; self.save("pair-ledger.json",l)
    self.assertTrue(any("pair-ledger schema/study mismatch" in x for x in self.errors()))
  def test_required_fidelity_pass_needs_evidence(self):
    e=self.data("evidence.json"); e["fidelity"]["asset_fidelity"]["evidence_ids"]=[]; self.save("evidence.json",e)
    self.assertTrue(any("asset_fidelity PASS requires evidence" in x for x in self.errors()))
  def test_task_acceptance_not_auto_upgraded(self):
    e=self.data("evidence.json"); e["results"]["task_acceptance"]="FAIL"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_visual_screenshot_paths_must_exist(self):
    v=self.data("visual-comparison.json"); v["pairs"][0]["target_screenshot"]="screenshots/missing.png"; self.save("visual-comparison.json",v)
    self.assertTrue(any("referenced file missing" in x for x in self.errors()))
  def test_functional_partial_not_package_error(self):
    e=self.data("evidence.json"); e["fidelity"]["functional_fidelity"]["status"]="PARTIAL"; e["results"]["task_acceptance"]="FAIL"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_sample_duplicate_id_rejected(self):
    e=self.data("evidence.json"); e["samples"].append(dict(e["samples"][0])); self.save("evidence.json",e)
    self.assertTrue(any("duplicate sample_id" in x for x in self.errors()))
  def test_asset_audit_not_tested_valid(self):
    e=self.data("evidence.json"); e["samples"][0]["asset_audit"]["status"]="NOT_TESTED"; self.save("evidence.json",e)
    self.assertEqual(self.errors(),[])
  def test_execution_acceptance_conflict_rejected(self):
    e=self.data("evidence.json"); e["results"]["task_acceptance"]="PASS"
    l=self.data("pair-ledger.json"); l["entries"][0]["result"]="FAIL"; self.save("pair-ledger.json",l); self.save("evidence.json",e)
    self.assertTrue(any("task_acceptance PASS contradicts ledger" in x for x in self.errors()))
  def test_required_criterion_missing(self):
    c=self.data("comparison.json"); c["criteria"]=[]; self.save("comparison.json",c)
    self.assertTrue(any("missing required criterion" in x for x in self.errors()))
  def test_source_origin_dependency_rejected(self):
    e=self.data("evidence.json"); e["dependencies"]=[{"disposition":"retained","runtime_origin":"source_origin"}]; self.save("evidence.json",e)
    self.assertTrue(any("source-origin runtime dependency" in x for x in self.errors()))

  def test_visual_ledger_requires_actual_screenshot_pair(self):
    v=self.data("visual-comparison.json"); v["pairs"]=[]; self.save("visual-comparison.json",v)
    self.assertTrue(any("visual ledger MEASURED missing screenshot pair" in x for x in self.errors()))
  def test_visual_pair_result_must_match_ledger(self):
    v=self.data("visual-comparison.json"); v["pairs"][0]["result"]="FAIL"; self.save("visual-comparison.json",v)
    self.assertTrue(any("visual screenshot result does not match ledger" in x for x in self.errors()))
  def test_measured_ledger_requires_alignment(self):
    l=self.data("pair-ledger.json"); l["entries"][0].pop("alignment"); self.save("pair-ledger.json",l)
    self.assertTrue(any("MEASURED requires valid alignment" in x for x in self.errors()))

if __name__=="__main__": unittest.main()
