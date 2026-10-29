# Agent Skills

Plan smaller changes. Review the evidence. Fix the right problem.

Practical skills for AI agents, each focused on a specific task.

**New to Agent Skills? Start with the [English beginner introduction](SKILLS-INTRODUCTION.md).**

## Pick a skill

- **[Feature Slice Planner](skills/feature-slice-planner/SKILL.md)** — Turn a feature into one manageable change with clear acceptance checks.
- **[Implementation Reviewer](skills/implementation-reviewer/SKILL.md)** — Check delivered work against the brief and identify gaps or scope drift.
- **[Divide and Conquer Analysis](skills/divide-and-conquer-analysis/SKILL.md)** — Break down a complex subject and bring the findings back into one conclusion.
- **[Image Prompt Analyzer and Refactorer](skills/ai-image-prompt-analyzer-and-refactorer/SKILL.md)** — Clarify what an image edit should change, preserve, and take from each reference.
- **[IT Procedure Builder](skills/it-procedure-builder/SKILL.md)** — Build and review an IT procedure with structured steps and local contract checks.
- **[Evidence-led Deliberation](skills/evidence-led-deliberation/SKILL.md)** — Coordinate OpenClaw subagents around evidence, disagreements, and bounded corrections.

- **[Operational Dashboard Design](skills/operational-dashboard-design/SKILL.md)** — Build data-first dashboards with accessible exception cues and evidence-backed visual QA.

## Python and delivery workflows

- **[GitHub Delivery Verification](skills/github-delivery-verification/SKILL.md)** — Verify the pushed commit, remote content, and CI results before calling delivery complete.
- **[Cross-platform Python Runtime Recovery](skills/cross-platform-python-runtime-recovery/SKILL.md)** — Trace Python startup failures across Windows and Linux without mixing their environments.
- **[uv Sync vs Dev Extras](skills/uv-sync-vs-dev-extras/SKILL.md)** — Explain missing packages and choose the right dependency groups, extras, and sync options.
- **[Python Optional Integration Boundaries](skills/python-optional-integration-boundaries/SKILL.md)** — Keep optional SDKs from breaking the core application and test their failure paths without a provider.

These four skills use MIT with owner-confirmed provenance; see [provenance](DRAFT-PROVENANCE.md).

## Install

With GitHub CLI's preview [`gh skill`](https://cli.github.com/manual/gh_skill_install) commands:

```bash
gh skill install voytas75/skills feature-slice-planner
```

Replace `feature-slice-planner` with a skill from the main catalog. Requirements and examples are in each skill's `SKILL.md`.

## Worth exploring

### Find skills

- **[skills.sh](https://skills.sh)** — Search the Agent Skills directory and browse trending skills; follow each result to its original source before installing.

### Repositories and references

- **[Agent Skills standard](https://github.com/agentskills/agentskills)** — The specification, documentation, and reference tooling for the portable skill format.
- **[Matt Pocock's skills](https://github.com/mattpocock/skills)** — Composable engineering workflows for requirements, debugging, TDD, reviews, and handoffs.
- **[Superpowers](https://github.com/obra/superpowers)** — A software development methodology built around planning, testing, verification, and subagent workflows.
- **[Anthropic skills](https://github.com/anthropics/skills)** — Official examples covering documents, design, communication, and technical work; individual packages have different license terms.
- **[OpenAI plugins](https://github.com/openai/plugins)** — Current Codex plugin examples, including bundled skills and MCP integrations; the earlier `openai/skills` catalog is deprecated.
- **[Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills)** — A broad discovery index linking to official and community skill sources.
- **[Vercel agent skills](https://github.com/vercel-labs/agent-skills)** — Engineering guidance for React, Next.js, web interfaces, and Vercel workflows.
- **[Vercel skills CLI](https://github.com/vercel-labs/skills)** — Tooling for discovering and installing skills across supported agent clients.
- **[Microsoft skills](https://github.com/microsoft/skills)** — Skills and supporting resources for Azure SDKs and Microsoft Foundry.
- **[Trail of Bits skills](https://github.com/trailofbits/skills)** — Security analysis, auditing, and testing workflows; check the applicable CC-BY-SA license terms before adapting content.

These are discovery and learning resources, not blanket endorsements. Review each package's instructions, scripts, dependencies, permissions, and license before use. Popularity does not establish safety or compatibility with your agent.

[MIT license](LICENSE).
