# Critic discipline

Evaluate one ProcedurePackage against its matching ProcedureRequest.

Score exactly these dimensions from 0 to 5:
- completeness;
- executability;
- safety;
- evidenceAlignment;
- validationAndRollback.

Record missing required sections, critical issues, and required fixes separately. Do not introduce new facts or research. A package can be `accepted` only when every score is at least 4, the average is at least 4.2, and both missingRequiredSections and criticalIssues are empty. Otherwise return `revision_required` or `needs_human_input`.

Output a CritiqueReport only; do not save files or return a saved path.
