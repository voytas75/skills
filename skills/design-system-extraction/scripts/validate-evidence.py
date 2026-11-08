#!/usr/bin/env python3
"""Validate Design System Extraction v1.6.1 evidence packages (stdlib only)."""
from __future__ import annotations
import json, sys
from pathlib import Path
from datetime import datetime, timezone

VERSION = "1.6.1"
SCHEMA_VERSION = "1.6.1"
OUTCOMES = {"PASS","PARTIAL","FAIL","NOT_TESTED"}
LEDGER_STATES = {"MEASURED","NOT_TESTED","NOT_COMPARABLE","BLOCKED"}
READINESS = {"PASS","FAIL","NOT_TESTED","NOT_APPLICABLE"}
MODALITIES = {"content","geometry","styles","visual","responsive","interaction","font_identity","asset_identity"}
CAPTURE_CONTROLS = {"url_identity","content_identity","render_stability","state_integrity","obstruction_check","capture_integrity"}
TASKS = {"analysis","reconstruction","comparison","audit"}
ARTIFACTS = {"snapshot","standalone_mockup","functional_implementation","not_applicable"}

class Validator:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.errors = []
        self.warnings = []
        self.checks = []
    def err(self, msg): self.errors.append(msg)
    def nonempty(self, x): return isinstance(x,str) and bool(x.strip())
    def read(self, rel, required=True):
        p=self.root/rel
        if not p.is_file():
            if required: self.err(f"missing required file: {rel}")
            return None
        try: return json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            self.err(f"{rel}: invalid JSON: {e}"); return None
    def safe(self, rel):
        if not self.nonempty(rel): self.err("empty package path"); return
        p=(self.root/rel).resolve()
        try: p.relative_to(self.root)
        except ValueError: self.err(f"unsafe path escapes package: {rel}"); return
        if not p.is_file(): self.err(f"referenced file missing: {rel}")
    def ids(self, rows, field, label):
        seen=set()
        for i,row in enumerate(rows):
            if not isinstance(row,dict): self.err(f"{label}[{i}] must be object"); continue
            val=row.get(field)
            if not self.nonempty(val): self.err(f"{label}[{i}].{field} required")
            elif val in seen: self.err(f"duplicate {field}: {val}")
            else: seen.add(val)
        return seen
    def validate(self):
        self.checks.append("manifest")
        ex=self.read("execution.json")
        ev=self.read("evidence.json")
        if not isinstance(ex,dict) or not isinstance(ev,dict): return self.report()
        if ex.get("schema_version") != SCHEMA_VERSION: self.err(f"execution.json schema_version must be {SCHEMA_VERSION}")
        if ev.get("schema_version") != SCHEMA_VERSION: self.err(f"evidence.json schema_version must be {SCHEMA_VERSION}")
        task=ex.get("task_type"); artifact=ex.get("artifact_mode")
        if task not in TASKS: self.err("execution.json task_type invalid")
        if artifact not in ARTIFACTS: self.err("execution.json artifact_mode invalid")
        sid=ex.get("study_id")
        if not self.nonempty(sid) or ev.get("study_id") != sid: self.err("study_id missing or inconsistent")
        if ev.get("task_type") != task or ev.get("artifact_mode") != artifact: self.err("evidence task/artifact mode mismatch")
        target=ex.get("target")
        if not isinstance(target,dict) or not self.nonempty(target.get("requested_url")) or not self.nonempty(target.get("final_url")):
            self.err("execution target requested_url/final_url required")
        scope=ex.get("scope") if isinstance(ex.get("scope"),dict) else {}
        vps=scope.get("viewports")
        if not isinstance(vps,list) or not vps: self.err("scope.viewports must be non-empty array"); vps=[]
        vpids=set()
        for i,v in enumerate(vps):
            if not isinstance(v,dict): self.err(f"viewport[{i}] must be object"); continue
            vid=v.get("id")
            if not self.nonempty(vid) or vid in vpids: self.err(f"viewport[{i}] id missing/duplicate")
            else: vpids.add(vid)
            if not all(isinstance(v.get(k),int) and v[k]>0 for k in ("width","height")): self.err(f"viewport[{i}] dimensions invalid")
        for k in ("pages","themes","states"):
            if not isinstance(scope.get(k),list) or not scope[k]: self.err(f"scope.{k} must be non-empty array")
        if not isinstance(scope.get("required_checks"),list): self.err("scope.required_checks must be array")
        themes=scope.get("themes",[]); states=scope.get("states",[])
        samples=ev.get("samples")
        if not isinstance(samples,list): self.err("evidence.samples must be array"); samples=[]
        self.ids(samples,"sample_id","samples")
        smap={}
        for i,s in enumerate(samples):
            if not isinstance(s,dict): continue
            sid0=s.get("sample_id")
            if self.nonempty(sid0): smap[sid0]=s
            if s.get("role") not in {"source","target"}: self.err(f"samples[{i}] role invalid")
            if s.get("viewport_id") not in vpids or s.get("theme") not in themes or s.get("state_id") not in states:
                self.err(f"samples[{i}] references undeclared viewport/theme/state")
            if s.get("capture_status") not in {"valid","partial","invalid"}: self.err(f"samples[{i}] capture_status invalid")
            cr=s.get("capture_readiness")
            if not isinstance(cr,dict): self.err(f"samples[{i}] capture_readiness required"); cr={}
            for c in CAPTURE_CONTROLS:
                item=cr.get(c)
                if not isinstance(item,dict) or item.get("status") not in READINESS or not self.nonempty(item.get("details")):
                    self.err(f"samples[{i}] capture_readiness.{c} invalid")
                elif item.get("status")=="NOT_APPLICABLE" and not self.nonempty(item.get("rationale")):
                    self.err(f"samples[{i}] capture_readiness.{c} N/A requires rationale")
            if s.get("capture_status")=="valid" and any(cr.get(c,{}).get("status") not in {"PASS","NOT_APPLICABLE"} for c in CAPTURE_CONTROLS):
                self.err(f"samples[{i}] capture_status valid contradicts failed/untested capture readiness")
            aa=s.get("asset_audit")
            if not isinstance(aa,dict) or aa.get("status") not in OUTCOMES: self.err(f"samples[{i}] asset_audit status required")
            else:
                subs=aa.get("substitutions",[]); unresolved=aa.get("unresolved",[])
                if not isinstance(subs,list) or not isinstance(unresolved,list): self.err(f"samples[{i}] asset_audit arrays invalid")
                if aa.get("status")=="PASS" and (subs or unresolved): self.err(f"samples[{i}] asset_audit PASS contradicts substitutions/unresolved")
            elig=s.get("measurement_eligibility")
            if not isinstance(elig,dict): self.err(f"samples[{i}] measurement_eligibility required")
            else:
                if s.get("capture_status")=="invalid" and any(isinstance(x,dict) and x.get("status")=="eligible" for x in elig.values()):
                    self.err(f"samples[{i}] invalid capture cannot mark any modality eligible")
                for mod,entry in elig.items():
                    if mod not in MODALITIES or not isinstance(entry,dict) or entry.get("status") not in {"eligible","ineligible","partial"} or not self.nonempty(entry.get("reason")):
                        self.err(f"samples[{i}] measurement_eligibility.{mod} invalid")
            if not isinstance(s.get("evidence_ids"),list): self.err(f"samples[{i}] evidence_ids must be array")

        registry=ev.get("evidence_registry")
        if not isinstance(registry,list): self.err("evidence_registry must be array"); registry=[]
        eids=self.ids(registry,"evidence_id","evidence_registry")
        for i,item in enumerate(registry):
            if not isinstance(item,dict): continue
            if item.get("type") not in {"screenshot","dom","computed_style","stylesheet","asset","network","manual_note","test_result","metric"}:
                self.err(f"evidence_registry[{i}] type invalid")
            if item.get("path") is not None: self.safe(item.get("path"))
            elif not self.nonempty(item.get("source_ref")): self.err(f"evidence_registry[{i}] path/source_ref required")
        for i,s in enumerate(samples):
            for eid in s.get("evidence_ids",[]) if isinstance(s.get("evidence_ids"),list) else []:
                if eid not in eids: self.err(f"samples[{i}] unknown evidence_id {eid}")
        findings=ev.get("findings",[])
        if not isinstance(findings,list): self.err("findings must be array"); findings=[]
        self.ids(findings,"finding_id","findings")
        for i,f in enumerate(findings):
            if not isinstance(f,dict): continue
            if not self.nonempty(f.get("claim")): self.err(f"finding[{i}] claim required")
            if f.get("classification") not in {"observed","inferred","estimated","unknown","recommendation"}: self.err(f"finding[{i}] classification invalid")
            refs=f.get("evidence_ids",[])
            if not isinstance(refs,list): self.err(f"finding[{i}] evidence_ids invalid"); refs=[]
            if f.get("classification")=="observed" and not refs: self.err(f"finding[{i}] observed claim requires evidence")
            if f.get("classification")=="estimated" and not self.nonempty(f.get("method")): self.err(f"finding[{i}] estimated claim requires method")
            for eid in refs:
                if eid not in eids: self.err(f"finding[{i}] unknown evidence_id {eid}")

        self.safe("report.html")
        results=ev.get("results")
        if not isinstance(results,dict): self.err("evidence.results required"); results={}
        for k in ("execution_completeness","package_validation","task_acceptance"):
            if results.get(k) not in OUTCOMES: self.err(f"results.{k} invalid")
        fidelity=ev.get("fidelity",{})
        if task=="reconstruction":
            dims={"visual_fidelity","functional_fidelity","responsive_fidelity","content_fidelity","asset_fidelity"}
            if not isinstance(fidelity,dict): self.err("evidence.fidelity required"); fidelity={}
            for d in dims:
                item=fidelity.get(d)
                if not isinstance(item,dict) or item.get("status") not in OUTCOMES or not self.nonempty(item.get("rationale")):
                    self.err(f"fidelity.{d} requires status/rationale")
                elif item.get("status")=="PASS" and not item.get("evidence_ids"):
                    self.err(f"fidelity.{d} PASS requires evidence")
                elif isinstance(item,dict):
                    for eid in item.get("evidence_ids",[]):
                        if eid not in eids: self.err(f"fidelity.{d} unknown evidence_id {eid}")

        if task in {"reconstruction","comparison"}:
            self.checks.append("pair-ledger")
            comp=self.read("comparison.json")
            ledger=self.read("pair-ledger.json")
            if isinstance(comp,dict):
                if comp.get("schema_version")!=SCHEMA_VERSION or comp.get("study_id")!=ex.get("study_id"): self.err("comparison manifest schema/study mismatch")
                crit=comp.get("criteria",[])
                if not isinstance(crit,list): self.err("comparison.criteria must be array"); crit=[]
                cmap={}
                for c in crit:
                    if isinstance(c,dict) and self.nonempty(c.get("criterion_id")): cmap[c["criterion_id"]]=c
                for req in scope.get("required_checks",[]):
                    if req not in cmap: self.err(f"comparison missing required criterion {req}")
                for c in crit:
                    if isinstance(c,dict) and c.get("status") not in OUTCOMES: self.err(f"criterion {c.get('criterion_id')} status invalid")
                rows=comp.get("comparisons",[])
                if not isinstance(rows,list): self.err("comparison.comparisons must be array"); rows=[]
                self.ids(rows,"comparison_id","comparisons")
                for i,p in enumerate(rows):
                    if not isinstance(p,dict): continue
                    if p.get("result") not in OUTCOMES: self.err(f"comparison[{i}] result invalid")
                    if p.get("match_status") not in {"matched","unmatched","ambiguous"}: self.err(f"comparison[{i}] match_status invalid")
                    src=smap.get(p.get("source_sample_id")); dst=smap.get(p.get("target_sample_id"))
                    if not src or not dst or src.get("role")!="source" or dst.get("role")!="target": self.err(f"comparison[{i}] sample refs invalid")
                    else:
                        if src.get("viewport_id")!=p.get("viewport_id") or dst.get("viewport_id")!=p.get("viewport_id"): self.err(f"comparison[{i}] viewport mismatch")
                        if src.get("theme")!=p.get("theme") or dst.get("theme")!=p.get("theme"): self.err(f"comparison[{i}] theme mismatch")
                        if src.get("state_id")!=p.get("state_id") or dst.get("state_id")!=p.get("state_id"): self.err(f"comparison[{i}] state mismatch")
                        modality=p.get("modality","geometry")
                        for side,sample in (("source",src),("target",dst)):
                            ent=sample.get("measurement_eligibility",{}).get(modality,{})
                            if ent.get("status")=="ineligible": self.err(f"comparison[{i}] {side} sample ineligible for {modality}")
                    if p.get("match_status")=="matched" and not self.nonempty(p.get("element_id")): self.err(f"comparison[{i}] matched requires element_id")
                    if not isinstance(p.get("evidence_ids"),list) or not p.get("evidence_ids"): self.err(f"comparison[{i}] evidence_ids required")
                    for eid in p.get("evidence_ids",[]):
                        if eid not in eids: self.err(f"comparison[{i}] unknown evidence_id {eid}")
                    if not isinstance(p.get("tolerances"),dict) or not p.get("tolerances"): self.err(f"comparison[{i}] tolerances required")
                    align=p.get("alignment")
                    if not isinstance(align,dict) or align.get("method") not in {"exact_scroll","shared_anchor","normalized_document_progress","region_crop"}:
                        self.err(f"comparison[{i}] alignment method invalid")
                    elif align.get("method")!="exact_scroll" and not self.nonempty(align.get("rationale")):
                        self.err(f"comparison[{i}] non-exact alignment requires rationale")
            if isinstance(ledger,dict):
                if ledger.get("schema_version")!=SCHEMA_VERSION or ledger.get("study_id")!=ex.get("study_id"): self.err("pair-ledger schema/study mismatch")
                reqmods=ledger.get("required_modalities")
                if not isinstance(reqmods,list) or not reqmods or any(m not in MODALITIES for m in reqmods): self.err("pair-ledger required_modalities invalid")
                entries=ledger.get("entries")
                if not isinstance(entries,list): self.err("pair-ledger entries must be array"); entries=[]
                self.ids(entries,"entry_id","pair-ledger.entries")
                actual=set()
                for i,e in enumerate(entries):
                    if not isinstance(e,dict): continue
                    key=(e.get("viewport_id"),e.get("theme"),e.get("state_id"),e.get("modality"))
                    if key in actual: self.err(f"duplicate ledger combination {key}")
                    actual.add(key)
                    if e.get("viewport_id") not in vpids or e.get("theme") not in themes or e.get("state_id") not in states or e.get("modality") not in reqmods: self.err(f"ledger[{i}] references undeclared combination")
                    status=e.get("status")
                    if status not in LEDGER_STATES: self.err(f"ledger[{i}] status invalid")
                    if status=="MEASURED":
                        if e.get("result") not in {"PASS","PARTIAL","FAIL"}: self.err(f"ledger[{i}] MEASURED requires PASS/PARTIAL/FAIL result")
                        if not self.nonempty(e.get("source_sample_id")) or not self.nonempty(e.get("target_sample_id")): self.err(f"ledger[{i}] MEASURED requires source/target samples")
                        if not e.get("evidence_ids"): self.err(f"ledger[{i}] MEASURED requires evidence")
                        if not isinstance(e.get("metric"),dict) and not self.nonempty(e.get("measurement_ref")): self.err(f"ledger[{i}] MEASURED requires metric or measurement_ref")
                        if not isinstance(e.get("alignment"),dict) or e["alignment"].get("method") not in {"exact_scroll","shared_anchor","normalized_document_progress","region_crop"}:
                            self.err(f"ledger[{i}] MEASURED requires valid alignment")
                    else:
                        if not self.nonempty(e.get("reason")): self.err(f"ledger[{i}] {status} requires reason")
                        if "metric" in e or "result" in e: self.err(f"ledger[{i}] non-measured entry cannot contain metric/result")
                    for eid in e.get("evidence_ids",[]):
                        if eid not in eids: self.err(f"ledger[{i}] unknown evidence_id {eid}")
                    if status=="MEASURED":
                        src=smap.get(e.get("source_sample_id")); dst=smap.get(e.get("target_sample_id"))
                        if not src or not dst or src.get("role")!="source" or dst.get("role")!="target": self.err(f"ledger[{i}] invalid source/target sample refs")
                        else:
                            mod=e.get("modality")
                            for side,sample in (("source",src),("target",dst)):
                                elig=sample.get("measurement_eligibility",{}).get(mod,{})
                                if elig.get("status")=="ineligible": self.err(f"ledger[{i}] {side} sample ineligible for {mod}")
                expected={(v.get("id"),t,s,m) for v in vps if isinstance(v,dict) for t in themes for s in states for m in (reqmods or [])}
                missing=expected-actual
                extra=actual-expected
                if missing: self.err(f"pair-ledger missing coverage: {sorted(missing)}")
                if extra: self.err(f"pair-ledger unexpected coverage: {sorted(extra)}")
                if results.get("execution_completeness")=="PASS" and any(e.get("status")!="MEASURED" for e in entries if isinstance(e,dict)):
                    self.err("execution_completeness PASS contradicts incomplete ledger")
                if results.get("task_acceptance")=="PASS" and any(e.get("status")!="MEASURED" or e.get("result")!="PASS" for e in entries if isinstance(e,dict)):
                    self.err("task_acceptance PASS contradicts ledger")
                if results.get("task_acceptance")=="PASS":
                    if any(c.get("required") is True and c.get("status")!="PASS" for c in (comp.get("criteria",[]) if isinstance(comp,dict) else []) if isinstance(c,dict)):
                        self.err("task_acceptance PASS contradicts required comparison criteria")
                    if task=="reconstruction" and any(not isinstance(fidelity.get(d),dict) or fidelity[d].get("status")!="PASS" for d in ("visual_fidelity","functional_fidelity","responsive_fidelity","content_fidelity","asset_fidelity")):
                        self.err("task_acceptance PASS requires all fidelity dimensions PASS")
            deps=ev.get("dependencies",[])
            if artifact=="standalone_mockup" and isinstance(deps,list):
                for d in deps:
                    if isinstance(d,dict) and d.get("disposition")=="retained" and d.get("runtime_origin")=="source_origin":
                        self.err("standalone_mockup retains source-origin runtime dependency")
        if task=="reconstruction":
            runtime=self.read("measurements/runtime-tests.json",required=False)
            if not isinstance(runtime,dict): self.err("runtime-tests.json required"); runtime={}
            if runtime.get("resolved_font_status") not in {"PASS","FAIL","NOT_TESTED"}: self.err("runtime-tests resolved_font_status invalid")
            if not isinstance(runtime.get("font_runs"),list): self.err("runtime-tests font_runs required")
            controls=runtime.get("interactions",[])
            if not isinstance(controls,list): self.err("runtime-tests interactions must be array"); controls=[]
            if fidelity.get("functional_fidelity",{}).get("status")=="PASS":
                if any(c.get("result")!="PASS" or c.get("source_status")!="PASS" or c.get("target_status")!="PASS" for c in controls if isinstance(c,dict)):
                    self.err("functional_fidelity PASS contradicts interaction failures/untested controls")
            if "visual" in (ledger.get("required_modalities",[]) if isinstance(ledger,dict) else []):
                visual=self.read("visual-comparison.json")
                if isinstance(visual,dict):
                    if visual.get("schema_version")!=SCHEMA_VERSION or visual.get("study_id")!=ex.get("study_id"): self.err("visual-comparison schema/study mismatch")
                    # Visual comparisons are represented by the visual modality in the ledger.
                    # Each MEASURED ledger item must reference a real source and target screenshot.
                    visual_pairs=visual.get("pairs",[])
                    if not isinstance(visual_pairs,list): self.err("visual-comparison pairs must be array"); visual_pairs=[]
                    visual_keys=set()
                    for i,p in enumerate(visual_pairs):
                        if not isinstance(p,dict): self.err(f"visual pair[{i}] invalid"); continue
                        for k in ("source_screenshot","target_screenshot"): self.safe(p.get(k))
                        if p.get("result") not in {"PASS","PARTIAL","FAIL"}: self.err(f"visual pair[{i}] result invalid")
                        key=(p.get("viewport_id"),p.get("theme"),p.get("state_id"))
                        if None in key: self.err(f"visual pair[{i}] missing viewport/theme/state")
                        if key in visual_keys: self.err(f"duplicate visual pair {key}")
                        visual_keys.add(key)
                    if isinstance(ledger,dict):
                        for entry in ledger.get("entries",[]):
                            if isinstance(entry,dict) and entry.get("modality")=="visual" and entry.get("status")=="MEASURED":
                                key=(entry.get("viewport_id"),entry.get("theme"),entry.get("state_id"))
                                if key not in visual_keys: self.err(f"visual ledger MEASURED missing screenshot pair {key}")
                                elif not any(isinstance(p,dict) and (p.get("viewport_id"),p.get("theme"),p.get("state_id"))==key and p.get("result")==entry.get("result") for p in visual_pairs):
                                    self.err(f"visual screenshot result does not match ledger {key}")
        self.checks.append("outcome-consistency")
        return self.report()
    def report(self):
        return {"validator_version":VERSION,"schema_version":SCHEMA_VERSION,
                "validation_status":"PASS" if not self.errors else "FAIL",
                "errors":self.errors,"warnings":self.warnings,"checks_run":self.checks,
                "timestamp":datetime.now(timezone.utc).isoformat()}

def main():
    if len(sys.argv)!=2:
        print("Usage: python scripts/validate-evidence.py <package-directory>",file=sys.stderr); return 2
    root=Path(sys.argv[1]).expanduser()
    if not root.is_dir(): print(f"Not a directory: {root}",file=sys.stderr); return 2
    report=Validator(root).validate()
    out=root/"validation"/"validator-report.json"
    try:
        out.parent.mkdir(exist_ok=True); out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    except OSError: pass
    print(("PASS" if not report["errors"] else "FAIL")+f": {len(report['errors'])} validation error(s)")
    for e in report["errors"]: print("- "+e)
    return 0 if not report["errors"] else 1

if __name__=="__main__": raise SystemExit(main())
