# Agent Skills

Plan smaller changes. Review the evidence. Fix the right problem.

Practical skills for AI agents, each focused on a specific task.

## Pick a skill

- **[Feature Slice Planner](skills/feature-slice-planner/SKILL.md)** — Turn a feature into one manageable change with clear acceptance checks.
- **[Implementation Reviewer](skills/implementation-reviewer/SKILL.md)** — Check delivered work against the brief and identify gaps or scope drift.
- **[Divide and Conquer Analysis](skills/divide-and-conquer-analysis/SKILL.md)** — Break down a complex subject and bring the findings back into one conclusion.
- **[Image Prompt Analyzer and Refactorer](skills/ai-image-prompt-analyzer-and-refactorer/SKILL.md)** — Clarify what an image edit should change, preserve, and take from each reference.
- **[IT Procedure Builder](skills/it-procedure-builder/SKILL.md)** — Build and review an IT procedure with structured steps and local contract checks.
- **[Evidence-led Deliberation](skills/evidence-led-deliberation/SKILL.md)** — Coordinate OpenClaw subagents around evidence, disagreements, and bounded corrections.

## Python and delivery workflows

- **[GitHub Delivery Verification](skills/github-delivery-verification/SKILL.md)** — Verify the pushed commit, remote content, and CI results before calling delivery complete.
- **[Cross-platform Python Runtime Recovery](skills/cross-platform-python-runtime-recovery/SKILL.md)** — Trace Python startup failures across Windows and Linux without mixing their environments.
- **[uv Sync vs Dev Extras](skills/uv-sync-vs-dev-extras/SKILL.md)** — Explain missing packages and choose the right dependency groups, extras, and sync options.
- **[Python Optional Integration Boundaries](skills/python-optional-integration-boundaries/SKILL.md)** — Keep optional SDKs from breaking the core application and test their failure paths without a provider.

These four skills use MIT with owner-confirmed provenance; see [provenance](DRAFT-PROVENANCE.md).

## Install

With GitHub CLI's preview `gh skill` commands:

```bash
gh skill install voytas75/skills feature-slice-planner
```

Replace `feature-slice-planner` with a skill from the main catalog. Requirements and examples are in each skill's `SKILL.md`.

[MIT license](LICENSE). Rights to the five earlier adaptations also remain unverified; absence of source attribution does not establish authorship or permission to redistribute.
