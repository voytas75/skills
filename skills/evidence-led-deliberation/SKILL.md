---
name: "evidence-led-deliberation"
description: "Coordinate native OpenClaw subagents for complex, verifiable work using a lightweight ledger, evidence, and bounded repair rounds."
---

# Evidence-led Deliberation (OpenClaw)

Use this skill only when a task has multiple dependent steps, a material cost of error, and observable acceptance criteria. Do not use it for ordinary questions, trivial edits, or work whose result cannot be checked. Prefer the configured native OpenClaw model for child calls. If spawn rejects the target agent's default as an unknown/unusable model before accepting a run, retry once with an explicitly available, policy-permitted native model (for example the verified current-session model). This is a per-run override, not permission to change agent configuration or relax its model policy. An accepted run must not be duplicated merely because completion is slow.

1. Define the deliverable, non-goals, acceptance criteria, maximum three repair rounds, and allowed write scope. If a material criterion is missing, ask the user before creating work. Choose an authorized writable work area outside the target repository; use a relative layout such as `work/deliberation/<task-id>/brief.md`. Do not assume a particular host, home directory, or preconfigured work area. Record the contract there; confirm every criterion can be checked.

2. Create `plan.md`, `notes.md`, `tasks.json`, `evidence.md`, and `candidates/` under the same task directory. Keep secrets, unrelated private context, and raw chain-of-thought out of this ledger. Confirm the directory contains the empty ledger files and no existing candidate is overwritten.

3. Spawn one hidden native subagent as an architect with isolated context. Give it the brief and require 2–3 genuinely distinct approaches, principal risks, and a concrete verification method for each. Instruct it not to perform external actions or implementation. Save only its concise conclusions in `notes.md`; confirm the selected approach is justified by the acceptance criteria.

4. Create one bounded task in `tasks.json` for the selected approach. Spawn one hidden native subagent as a worker with isolated context, giving it the brief, selected notes, and exact write scope limited to `candidates/<version>/`. Require the requested artifact, stated assumptions, and a short handoff; do not allow it to declare the task complete without evidence. Inspect its resulting paths and diff before accepting the handoff: the write scope is an instruction, not filesystem enforcement. Confirm a new versioned candidate exists.

5. Verify the candidate and record the method, result, and remaining gaps in `evidence.md`; mark it `verified`, `failed`, or `inconclusive`. Use the strongest available evidence and follow the runtime, broad-suite, and Python-package branches in [references/verification.md](references/verification.md). Run generated code only through the established execution policy in a disposable isolated environment; without such an environment, mark runtime verification inconclusive.

6. If verification fails or is inconclusive, follow the repair-round procedure in [references/verification.md](references/verification.md).

7. Choose the best candidate by verified acceptance criteria, never merely by a subagent's confidence. Preserve it and its evidence. Return the result, verification evidence, unresolved limitations, and the ledger path. If no candidate meets the criteria, return `inconclusive`, state the blocker, and identify the best supported partial result.

## Native-tool lifecycle

Discover the available native spawn and wait/history tools through the host tool
catalog; names and input schemas may differ by OpenClaw version. Do not replace
missing tools with shell, CLI, or direct RPC calls. Hidden sessions and isolated
context are requested capabilities, not guaranteed security boundaries. If a
required capability is unavailable, report the blocker instead of assuming it.

For each accepted spawn, record its run/session handle and completion mode in
`tasks.json`. Collect collector-mode children with the native collection tool;
for announcing children, await the accepted completion event and yield when
required. Do not busy-poll, treat a running status as success, or duplicate an
accepted run. Inspect each returned artifact and evidence before proceeding.
Keep ownership of unfinished work until its completion or a concrete blocker.

## Role prompts

- **Architect:** "Analyze only. Give distinct approaches, risks, and a check for each. Do not implement or take actions."
- **Worker:** "Complete only the assigned bounded task. Write only inside the assigned candidate directory. Return the artifact, assumptions, and a concise handoff."
- **Reviewer:** "Use supplied evidence to identify one highest-value repair or a switch of approach. Do not claim success without external evidence."

## Guardrails

- Keep at most one architect, one worker, and one reviewer active for a task at a time.
- Prefer deterministic checks over model review; reviewer output is a hypothesis, not proof.
- Never overwrite a verified candidate, mutate user configuration, send external messages, or run destructive actions as part of deliberation.
- Stop early when all acceptance criteria are verified; do not spend rounds polishing an already accepted result.
