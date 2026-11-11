# Task Execution Planner

**Version:** 0.2.0<br>
**Status:** Experimental<br>
**Author:** Voytas

A general-purpose Agent Skill for decomposing a concrete task and assigning each operation to:
- `LLM` — reasoning, interpretation, judgment, synthesis;
- `APP` — deterministic code/application processing;
- `TOOL` — existing external capabilities and sources;
- `HYBRID` — only when a step cannot practically be separated.

## What changed in 0.2.0

Based on three behavioral tests (current-information research, deterministic calculation, and a mixed API/code/LLM/human-decision workflow), the planner adds:
- scope and criteria gate;
- data provenance and source-substitution rules;
- input completeness/validity gate;
- explicit deterministic-processing contract;
- human decision vs. human approval gates;
- failure handling and adaptive replanning;
- stopping criteria for research;
- stronger distinction between evidence, derived values, assumptions, and judgment.

The test domains are examples only. The skill remains domain-agnostic.

## Scope

The skill produces plans; it does not execute them, connect tools, or authorize actions. Execution, if separately requested, must use actually available and authorized capabilities.

## Package

```text
task-execution-planner/
├── SKILL.md
├── README.md
├── DOCUMENTATION.html
└── references/
    └── plan-schema.yaml
```

## Use

Expose the `task-execution-planner` directory to a compatible Agent Skills host. Invoke it with a concrete task and ask for an execution plan. Markdown is the default output; the YAML schema is an optional planning contract.

## Design constraints

- No runtime, scripts, packages, or network access required for planning.
- Concise operational rules in `SKILL.md`; expanded rationale in `DOCUMENTATION.html`.
- No forced application or decomposition for simple tasks.
- Unknown tool availability remains explicit.
- No silent source substitution or unverified completion claims.
- No domain-specific provider, market, weather, or vendor rules in the core skill.

## Validation status

Structural checks: frontmatter fields, matching skill directory/name, line count, HTML parsing, ZIP contents, and schema structure. Behavioral coverage is specified in the documentation; these checks do not establish compatibility with every Agent Skills host or prove runtime behavior.
