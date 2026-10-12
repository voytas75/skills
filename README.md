# Agent Skills

A small collection of reusable skills for AI agents: practical instructions for clear analysis, explicit uncertainty, and evidence-based conclusions.

## Available skills

### [Divide and Conquer Analysis](skills/divide-and-conquer-analysis/SKILL.md)

Analyze a problem, decision, system, document, process, offer, or plan by breaking it into meaningful parts, checking their dependencies, and synthesizing a verified conclusion.

- **Use it for:** structured analysis of a specific subject.
- **Method:** define scope → break down → analyze parts → check dependencies → synthesize → verify.
- **Principles:** distinguish facts from assumptions, make uncertainty visible, and avoid unnecessary complexity.

**Example request:**

> Use divide-and-conquer-analysis to assess this migration plan. Identify dependencies, risks, missing evidence, and a practical final recommendation.

## Installation

With a GitHub CLI version that supports `gh skill`:

```bash
gh skill install voytas75/skills divide-and-conquer-analysis
```

Use `gh skill install --help` to select your agent and installation scope. The skill commands are currently in preview.

Alternatively, read the linked `SKILL.md` and follow your agent's instructions for installing local skills.

## License

[MIT](LICENSE).
