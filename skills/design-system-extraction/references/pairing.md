# Pairing, comparison and ledger
Pair per modality, not globally. A valid source-target comparison requires modality eligibility on both samples and compatible conditions. `capture_status` invalid blocks modalities dependent on that capture; asset/font uncertainty blocks only affected identity claims unless it physically corrupts the capture.

## Pair ledger
`pair-ledger.json`: `{schema_version:"1.6.1",study_id,required_modalities:[...],entries:[...]}`. One unique entry for every declared viewport × theme × state × required modality. Entry fields: `entry_id,viewport_id,theme,state_id,modality,status,source_sample_id,target_sample_id,alignment,result?,metric?,threshold?,reason?,evidence_ids`. `status`: `MEASURED|NOT_TESTED|NOT_COMPARABLE|BLOCKED`. `MEASURED` requires `result: PASS|FAIL|PARTIAL`, source/target sample IDs, evidence IDs, and metric/measurement reference. Other statuses require a non-empty reason and MUST NOT contain fabricated metric/result. `NOT_TESTED` is incomplete execution; `NOT_COMPARABLE` means observed conditions cannot be validly paired; `BLOCKED` means a prerequisite prevents the attempt. These are not package errors if correctly recorded, but they block acceptance for required modalities.

Ledger coverage is complete when each required combination/modality has exactly one entry, regardless of status. Missing, duplicate, unknown, or malformed entries are package errors. A failed measured pair is valid evidence and MUST remain in `comparison.json` or `visual-comparison.json`.

## Alignment
`alignment.method`: `exact_scroll|shared_anchor|normalized_document_progress|region_crop`; include source/target anchor and offsets, mapping rationale, and evidence. `exact_scroll` requires same CSS scroll position. `shared_anchor` allows different absolute scroll values only when the same semantic anchor (e.g. `document_bottom`, `footer_start`, stable element ID) is visible/aligned. `region_crop` requires equivalent region identity and crop dimensions. Record absolute scroll and anchor offset for both. Never compare non-equivalent footer captures as paired pixels.

## Geometry and styles
Comparison rows include stable `element_id`, `match_status: matched|unmatched|ambiguous`, sample IDs, source/target values, delta, tolerances, result, evidence IDs. Unmatched/ambiguous cannot PASS a required element comparison. Include root-cause analysis for material differences; cause classification `observed|inferred|unknown`.

## Visual comparison
Each declared screenshot comparison is a ledger modality. Same pixel dimensions; record metric/tool/version, color space, normalization, threshold, masks and rationale, masked/unmasked coverage, screenshots, actual metric, result. No rescaling. Diagnostic comparisons may be stored separately but MUST be labelled `diagnostic` and never silently promoted to acceptance evidence. A metric with different viewport dimensions or non-equivalent alignment is NOT_COMPARABLE, not FAIL/PASS.
