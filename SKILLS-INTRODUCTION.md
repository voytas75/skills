# Agent Skills — from first encounter to your own instructions

Agent Skills are a way to package instructions and resources for an AI assistant to use on specific tasks. You do not need to start with programming: the simplest skill is a folder containing one readable text file.

**How to read this page:** new to the topic? Start with section 1. Familiar with prompts and agent tools? Jump to the structure of a skill. Looking for more depth? Explore the history, limitations, and primary sources below.

## Contents

- [1. I do not know what skills are yet](#1-i-do-not-know-what-skills-are-yet)
- [2. I know the basics — what does a skill look like?](#2-i-know-the-basics--what-does-a-skill-look-like)
- [3. I want to understand more](#3-i-want-to-understand-more)
- [4. Where does this repository fit?](#4-where-does-this-repository-fit)
- [5. Limitations and safe use](#5-limitations-and-safe-use)
- [6. Learn from the sources](#6-learn-from-the-sources)

## 1. I do not know what skills are yet

Imagine a new teammate. They can write, analyze information, and use a computer, but they do not know your team's way of working. You give them an **onboarding folder**: when to follow a procedure, the steps involved, an example of a good result, and the things they must not do. A skill plays a similar role for an AI agent.

Here, an agent means an application using an AI model that can do more than answer questions: it can perform tasks with the tools made available to it. A skill describes **how to approach a particular kind of work**. For example, it might help break a large software feature into a small change, review implementation against requirements, or prepare an IT procedure.

Instead of pasting a long prompt every time, you keep the instructions in files. You can improve them, review their changes, and share them with a team. A good skill includes not just steps, but also conditions for use, task boundaries, and a way to check the result.

### What a skill is not

- **It is not model training.** Instructions enter the context during a task; using a skill does not change the model's weights or permanently teach it a new ability.
- **It is not a separate model or a standalone agent.** It is material for an application that must know how to discover and use it.
- **It is not the same as a tool.** A tool performs an operation, such as reading a file. A skill can explain when and how to use that tool, and may include a helper script.
- **It is not MCP.** Model Context Protocol standardizes connections between AI applications and external systems, data, and tools; it also supports resources and prompts. A skill organizes instructions and resources for a particular job. They can complement each other: the connection provides access, while the skill describes a procedure for using it.

## 2. I know the basics — what does a skill look like?

According to the [Agent Skills specification](https://agentskills.io/specification), the minimum is a directory containing a `SKILL.md` file. It uses Markdown — plain text with simple formatting for headings and lists — preceded by YAML metadata between `---` lines.

Example file: `meeting-summary/SKILL.md`:

```markdown
---
name: meeting-summary
description: Summarizes supplied meeting notes. Use when the user asks for decisions and action items after a meeting.
---

# Meeting summary

1. Read the supplied notes. Do not invent missing facts.
2. List decisions and action items, including an owner and deadline.
3. If an owner or deadline is missing, mark it as unspecified.
4. Finish with open questions. Do not send the summary yourself.
```

The specification requires `name` and `description`. The `name` must contain 1–64 characters, use lowercase letters, numbers, and hyphens only, and match the parent directory name. It must neither start nor end with a hyphen nor contain consecutive hyphens. The `description` must contain 1–1,024 characters; it should explain both **what the skill does** and **when to use it**.

A larger folder might look like this:

```text
meeting-summary/
├── SKILL.md
├── references/   # additional guidance and examples
├── assets/       # output templates
└── scripts/      # optional helper code
```

The extra directories are optional organizational conventions, not required structure. As a recommended practice, start with one instruction file and add resources only when they help. The example above needs no script, email access, or calendar connection.

### Check structure, then test behavior

Check the metadata and directory name against the specification. For an optional structural check, the official [reference library](https://github.com/agentskills/agentskills/tree/main/skills-ref) provides this command after installation:

```bash
skills-ref validate path/to/skill
```

Its README explicitly describes the library as demonstration-only, not intended for production. Structural validation does not establish factual accuracy, safety, or client compatibility. Next, try representative tasks in your intended client, including incomplete inputs and cases where the skill should not apply, and inspect the results.

## 3. I want to understand more

### Why does the agent not read everything at once?

A central principle is **progressive disclosure** — loading details gradually:

1. First, the agent receives short metadata for available skills: their names and descriptions.
2. When a task matches, it reads the full `SKILL.md`.
3. Only when needed does it consult referenced material or run helper code, if the environment permits it.

Think of scanning folder labels, opening the relevant folder, and reading the necessary attachment. This helps limit the amount of material in the model's context. It does not provide an unlimited context window or guarantee that the agent always selects the right instructions.

This is the pattern described in the specification and Anthropic's engineering article. **Agent Skills defines a portable file format, not a universal execution environment.** Each client determines how skills are discovered, selected, loaded, and used, including which tools and permissions are available. A valid folder does not guarantee automatic discovery or activation, access to its resources, or permission to execute scripts. Dependencies and support for extra fields also vary.

### Where did the format come from?

The [official standard website](https://agentskills.io/home) credits **Anthropic** with originally developing the Agent Skills format. Two public milestones should be distinguished:

- **October 16, 2025 — public launch of Agent Skills in Claude.** The [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview#october-16-2025) include “We've launched Agent Skills” under this date, describing folders and the initial feature release. A [product announcement](https://claude.com/resources/articles/skills) accompanied the launch.
- **December 18, 2025 — publication of Agent Skills as an open standard.** An update at the beginning of the announcement and the [engineering article](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) dates this change explicitly.

These are dates of public release and the standard announcement, **not an established date for the first internal idea or prototype**. These sources do not justify crediting Anthropic with inventing the entire idea of reusable instructions for agents.

The engineering article credits **Barry Zhang, Keith Lazuka, and Mahesh Murag** as its writers and acknowledges a broader Anthropic team. Writing the article is not evidence that any one of those people independently “invented skills.”

## 4. Where does this repository fit?

The [`voytas75/skills` repository](README.md) is a practical collection of skills, not the source of the standard's definition or an official Anthropic catalog. Its instructions cover topics such as planning small changes, reviewing implementation, analyzing complex subjects, and building procedures.

Start with [Feature Slice Planner](skills/feature-slice-planner/SKILL.md): notice its conditions for use, expected output, and scope controls. Then compare it with [Implementation Reviewer](skills/implementation-reviewer/SKILL.md), which checks delivered work against a brief — a description of the task. This illustrates the difference between planning instructions and evaluation instructions.

The README describes the catalog and flags unverified rights to five earlier adaptations. For four Python and delivery workflow skills, the owner has confirmed that they derive from their own procedures and are shared under MIT — see the [provenance information](DRAFT-PROVENANCE.md). This is an owner's confirmation, not an independent legal assessment; a file being available on GitHub does not by itself prove authorship or permission to redistribute it.

## 5. Limitations and safe use

A skill does not eliminate model errors. Ambiguous instructions, outdated resources, or missing data can still lead to bad results. Test it on several real tasks and inspect the output rather than judging only how fluent the response sounds.

**Treat someone else's skill as unverified instructions and potentially untrusted code.** Consider three layers of risk:

- **Instructions:** prompt injection — instructions designed to redirect the agent — conflicts with higher-priority rules, or attempts to disclose private data. Markdown does not execute code by itself, but can influence an agent's actions.
- **Code:** scripts and dependencies may modify files, install software, or communicate over the network.
- **Permissions:** the impact depends on which secrets, repositories, accounts, data, and tools the application makes accessible to the agent.

Reading the files is useful, but is not a complete audit. Access controls and isolation must be enforced by the application or execution environment, not merely requested in the skill's text. Consequential operations still need appropriate oversight.

Before use:

- Read `SKILL.md`, linked files, and scripts; inspect network destinations and dependencies.
- Keep secrets out of shared instructions and examples.
- Provide only the tools and data required; use isolation and action approvals where the platform supports them.
- Require separate approval for sensitive operations, such as publishing, sending messages, or deleting data.
- Check the license and environment requirements.

A skill's instructions **should not replace user consent or the application's permission policy**. Support for the experimental `allowed-tools` field varies across clients; do not treat it as a universal security boundary.

## 6. Learn from the sources

1. [Introducing Agent Skills — Anthropic / Claude](https://claude.com/resources/articles/skills): an accessible product introduction, including a dated update about the open standard.
2. [Equipping agents for the real world with Agent Skills — Anthropic Engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills): structure, progressive loading, code, and risks; also the source for the article writers' names.
3. [Agent Skills — official overview](https://agentskills.io/home): the format's purpose, origin, and ecosystem.
4. [Agent Skills specification](https://agentskills.io/specification): required fields, names, resources, and organization rules — the best reference when writing your own skill.
5. [Claude Platform — October 16, 2025 release notes](https://platform.claude.com/docs/en/release-notes/overview#october-16-2025): primary confirmation of the public launch date.
6. [Official introduction to MCP](https://modelcontextprotocol.io/docs/getting-started/intro): explains the connection layer, which is distinct from skill instructions.

The simplest next step: choose one recurring task, write down when to use the instructions and what a good result looks like, then test a short skill. Do not start by collecting dozens of skills.
