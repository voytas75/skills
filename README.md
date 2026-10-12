# Agent Skills

Six reusable skills for bounded planning, evidence-led review, and clear output.

## Catalog

| Skill | Use it for |
| --- | --- |
| [Divide and Conquer Analysis](skills/divide-and-conquer-analysis/SKILL.md) | Break a subject into meaningful parts, check dependencies, and synthesize a verified conclusion. |
| [Implementation Reviewer](skills/implementation-reviewer/SKILL.md) | Compare delivered work with one brief or acceptance contract; distinguish gaps, scope drift, and unknowns. |
| [Feature Slice Planner](skills/feature-slice-planner/SKILL.md) | Choose one small implementation slice with concrete acceptance checks, rollback, and anti-goals. |
| [Image Prompt Analyzer and Refactorer](skills/ai-image-prompt-analyzer-and-refactorer/SKILL.md) | Separate image-edit targets, preserved properties, reference roles, and real output settings. |
| [IT Procedure Builder](skills/it-procedure-builder/SKILL.md) | Produce and critique chat-only IT procedure packages with bundled schemas, prompts, and local contract tests. |
| [Evidence-led Deliberation](skills/evidence-led-deliberation/SKILL.md) | Coordinate native OpenClaw subagents through a lightweight ledger and bounded evidence-based repair rounds. |

Reviewer, planner, and image refactorer are instruction-only. Procedure helpers
require Node.js 18+ and no third-party Node packages. Deliberation requires an
OpenClaw host with suitable native subagent tools and an authorized work area.
No private project runtime or machine-specific path is required.

## Installation

With a GitHub CLI version supporting the preview `gh skill` commands:

```bash
gh skill install voytas75/skills feature-slice-planner
```

Replace the final name with any catalog skill. Consult `gh skill install --help`
for agent and installation scope. Alternatively, install the complete linked
skill directory following your agent's local-skill instructions; keep its assets.

## Local validation

From the repository root:

```bash
gh skill publish --dry-run
git diff --check
node skills/it-procedure-builder/scripts/test-contracts.mjs
node skills/it-procedure-builder/scripts/validate-package.mjs \
  skills/it-procedure-builder/examples/fixtures/accepted-procedure-package.json \
  skills/it-procedure-builder/examples/fixtures/accepted-critique-report.json
```

Dry-run validates skill packaging, not model behavior or publication readiness.
The procedure helper tests a local contract subset, not full JSON Schema,
evidence-source truth, infrastructure safety, or image/model output quality.

## License and provenance

The repository contains an [MIT license](LICENSE). The five added packages were
adapted from owner-supplied local skill sources for portability; those sources
contained no package-level license, author attribution, or third-party notices.
That absence does **not** establish authorship or redistribution rights. Their
original authorship and compatibility with the repository MIT grant remain
unverified; the owner must confirm rights before redistribution or publication.
No upstream provenance or license approval is claimed by these adaptations.
