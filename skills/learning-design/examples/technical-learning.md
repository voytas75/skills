# Example: technical skill acquisition

## Request
"Create a learning path for an administrator who wants to learn PowerShell troubleshooting."

## Assumptions
The learner knows basic PowerShell syntax. The target is practical troubleshooting, not memorizing cmdlets. The environment is a safe test machine.

## Outcomes
Given a documented Windows issue and access to a test system, the learner can:
1. collect relevant evidence using appropriate commands and logs;
2. form and test hypotheses without making unsupported changes;
3. identify a likely cause and justify it with evidence;
4. apply a safe remediation and verify the result;
5. document findings and rollback considerations.

## Sequence
1. **Foundations:** pipeline, objects, errors, event logs, process/service basics. Diagnose with short tasks.
2. **Demonstration:** walk through one troubleshooting case, making hypothesis and evidence selection explicit.
3. **Guided practice:** learner investigates a similar issue using a checklist and hints.
4. **Independent practice:** learner receives a new issue and chooses commands and evidence.
5. **Transfer:** change the subsystem, symptoms, or constraints; require the learner to adapt the method.
6. **Retention:** delayed case reconstruction without the original walkthrough.

## Assessment
Use a realistic fault-injection lab. Rubric: evidence relevance, hypothesis quality, safe change control, verification, and documentation. Critical safety errors prevent a pass.

## Adaptation
If commands are memorized but diagnosis is weak, use contrasting cases and ask the learner to justify evidence selection. If the learner diagnoses correctly but makes unsafe changes, practice change planning, impact analysis, and rollback separately.
