# Agent Skills

Reusable workflows for AI agents — plan a change, review an implementation, design an interface, or recover a Python runtime.

[Project skills](#project-skills) · [Install](#install) · [External skills](#external-skills) · [Libraries and references](#libraries-and-references)

**Need → choose a workflow → read requirements → apply → verify**

## Project skills

Choose by the outcome you need. Each link opens the full instructions.

| Skill | What it helps you do |
| :--- | :--- |
| [Feature Slice Planner](skills/feature-slice-planner/SKILL.md) | Turn a feature into one manageable change with clear acceptance checks. |
| [Implementation Reviewer](skills/implementation-reviewer/SKILL.md) | Compare an implementation with the requirements and find missing work or changes outside the agreed scope. |
| [Divide and Conquer Analysis](skills/divide-and-conquer-analysis/SKILL.md) | Break down a complex subject and bring the findings back into one conclusion. |
| [Image Prompt Analyzer and Refactorer](skills/ai-image-prompt-analyzer-and-refactorer/SKILL.md) | Clarify what an image edit should change, preserve, and take from each reference. |
| [IT Procedure Builder](skills/it-procedure-builder/SKILL.md) | Write an IT procedure and check for missing or inconsistent steps. |
| [Evidence-led Deliberation](skills/evidence-led-deliberation/SKILL.md) | Have OpenClaw agents investigate a question, compare their findings, and resolve disagreements. |
| [Operational Dashboard Design](skills/operational-dashboard-design/SKILL.md) | Design dashboards with clear problem indicators and checks for readability and accessibility. |
| [GitHub Delivery Verification](skills/github-delivery-verification/SKILL.md) | Verify the pushed commit, remote content, and CI results before calling delivery complete. |
| [Cross-platform Python Runtime Recovery](skills/cross-platform-python-runtime-recovery/SKILL.md) | Trace Python startup failures across Windows and Linux without mixing their environments. |
| [uv Sync vs Dev Extras](skills/uv-sync-vs-dev-extras/SKILL.md) | Explain missing packages and choose the right dependency groups, extras, and sync options. |
| [Python Optional Integration Boundaries](skills/python-optional-integration-boundaries/SKILL.md) | Keep optional SDKs from breaking the application and test failures without calling an external AI service. |

New to skills? Read the [introduction](SKILLS-INTRODUCTION.md).

<details>
<summary>Python workflow licensing and provenance</summary>

GitHub Delivery Verification, Cross-platform Python Runtime Recovery, uv Sync vs Dev Extras, and Python Optional Integration Boundaries are licensed under MIT. Their sources and licensing notes are documented in [provenance](DRAFT-PROVENANCE.md).

</details>

## Install

With GitHub CLI's preview [`gh skill`](https://cli.github.com/manual/gh_skill_install) commands:

```bash
gh skill install voytas75/skills feature-slice-planner
```

Replace `feature-slice-planner` with a project skill from the table. Requirements and examples are in its `SKILL.md`. External links below are not included in this installation.

## External skills

Browse by task. Expand a category for source links, deliverables, and limitations.

> [!IMPORTANT]
> Third-party links are separate from this project's packages. Inclusion does not imply installation, testing, or endorsement; content remains with its original authors.

<details>
<summary><strong>Text analysis, compression and restructuring</strong></summary>

- **[Compress Text](https://github.com/MartinForReal/compress-text-skill/tree/main/skills/compress-text)** — From `MartinForReal/compress-text-skill`: shorten and reorganize documents, prompts, or transcripts through semantic grouping, deduplication, and key-point-first structure, with readable and dense modes. Compares candidate rewrites and preserves distinct requirements, references, examples, and template tags; claimed meaning fidelity and token savings require independent checks, especially for protected or exact wording.

- **[Text Density Analyzer](https://github.com/Max-Levitskiy/skills/tree/main/plugins/ml-slop/skills/text)** — From `Max-Levitskiy/skills` (`ml-slop` plugin): audit documents for semantic and thematic repetition, filler, and information density, or rewrite them in a separate fix mode. Coordinates parallel analysis agents and a composite score; its two-pass rewrite requires source-to-output checks for unique claims, qualifiers, quotes, links, paths, and code. Depends on the package's analysis-agent instructions; scores and information preservation require independent verification.

</details>

<details>
<summary><strong>Architecture and diagrams</strong></summary>

- **[Architecture Diagram Generator](https://github.com/liuarui/skillsmd/tree/main/architecture)** — From `liuarui/skillsmd`: create layered system architecture diagrams using HTML/CSS templates, reusable layouts, and color-coded components. Intended for architecture visualization, not architecture validation or general-purpose flowcharts.

- **[Interactive Architecture Diagrams](https://github.com/konraddzbik/architecture-diagram-skill/tree/main/skills/architecture-diagram)** — From `konraddzbik/architecture-diagram-skill`: build a self-contained interactive HTML diagram with step-by-step data flows, deployment-mode toggles, and payload details, plus a companion Markdown description. Intended for browser-based exploration and workshops, not static inline diagrams or PDF handouts.

</details>

<details>
<summary><strong>Information cards and editorial design</strong></summary>

- **[Magazine](https://github.com/barkleesanders/claude-code-starter/tree/main/skills/magazine)** — From `barkleesanders/claude-code-starter`: turn digests, meeting notes, research summaries, and curated lists into an HTML magazine with distinct full-viewport spreads and print/PDF styling. Uses the package's design-system and spread references; its single-file output still loads Google Fonts externally, so offline use requires local or embedded fonts. Not intended for plain working documents or editable Google Docs.

- **[Infocard Generator](https://github.com/liuarui/skillsmd/tree/main/infocard)** — From `liuarui/skillsmd`: create editorial-style information cards with HTML/CSS embedded in Markdown for knowledge summaries, topic overviews, data highlights, and event announcements. Select layouts and typography based on content density, structure, and tone; not intended for architecture diagrams or data visualization.

- **[AlterLab VCD Layout Designer](https://github.com/roohe/agentic-super-skills/blob/master/skills_library/alterlab-vcd-layout-designer/SKILL.md)** — From `roohe/agentic-super-skills`: define publication grids, spread templates, page-by-page content plans, and print-production checklists for magazines, books, reports, and catalogs. Produces Markdown specifications rather than finished typeset publications; confirm margins, bleed, and binding requirements with the printer instead of treating its universal layout rules as production standards.

- **[Typography](https://github.com/petekp/agent-skills/blob/main/skills/typography/SKILL.md)** — From `petekp/agent-skills`: design and audit interface typography through type scales, font pairing, line length, spacing, and hierarchy, with ready-to-use CSS and Tailwind examples. Includes guidance on responsive text, dark mode, font loading, OpenType features, and internationalization; intended for digital interfaces rather than print-production layout.

- **[Editorial](https://github.com/bergside/awesome-design-skills/blob/main/skills/editorial/SKILL.md)** — From `bergside/awesome-design-skills` (metadata credits `typeui.sh`): write implementation-ready guidelines for an editorial-style design system using Gelasio typography, a restrained palette, and an 8pt spacing grid. Defines design tokens, component states, responsive behavior, accessibility acceptance criteria, and a QA checklist; produces design-system guidance rather than magazine layouts or finished publications.

- **[Typography System](https://github.com/event4u-app/agent-config/blob/main/dist/agent-src/skills/typography-system/)** — From `event4u-app/agent-config`: derive font pairings and a typographic scale from style constraints or an existing brand, then produce DTCG typography tokens and a stack-specific font-delivery plan with self-hosting as the default. Depends on the repository's font-pairing data, related skills, and `design-tokens` toolchain; not a standalone CSS typography guide.

- **[Editorial Grid](https://github.com/deMallory/editorial-claude-skills/tree/main/.claude/skills/editorial-grid)** — From `deMallory/editorial-claude-skills`: construct or critique editorial layout structure through page proportions, margin canons, modular grids, typographic scales, line metrics, and baseline rhythm. Covers print-derived grids and their translation to screens; GitHub Markdown cannot enforce its precise margins, columns, or baseline geometry.

</details>

<details>
<summary><strong>Web interface design</strong></summary>

- **[Web Design](https://github.com/pascalorg/skills/blob/main/web-design/SKILL.md)** — From `pascalorg/skills`: build and review web interfaces using a prioritized reference covering semantic HTML, responsive layout, typography, design tokens, component states, accessibility, motion, and performance, with CSS and Tailwind examples. Addresses interface implementation and design review rather than publication layout or presentation generation; its checklists do not replace browser, keyboard, and accessibility testing.

- **[Web Design Skill Pack](https://github.com/TobiasKulvik/web-design-skills/blob/main/SKILL.md)** — From `TobiasKulvik/web-design-skills`: coordinate framework-agnostic web design by selecting topical sub-skills for content structure, layout, typography, color, components, UX flows, SEO, internationalization, accessibility, and frontend implementation. The root file is an orchestrator and reading guide, not a standalone design reference; consult the linked sub-skills for detailed guidance.

- **[Frontend Design](https://github.com/thekorn/agent-skills/blob/main/skills/frontend-design/SKILL.md)** — From `thekorn/agent-skills`: turn a brief into coded web pages or components by choosing one distinctive aesthetic direction and defining typography, color, layout, and motion before implementation. Calls for responsive, semantic interfaces with tokenized styling and full code deliverables; its emphasis on expressive visual identity is not a substitute for runtime, accessibility, or production-readiness testing.

- **[Frontend Design (Anthropic)](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)** — From `anthropics/skills`: build or reshape interfaces around the brief's subject, audience, and visual identity, using a compact palette, typography plan, and layout sketches before coding. Reviews the plan against generic defaults and combines restrained motion, clear interface copy, and screenshot-based self-critique; accessibility and responsive-design guidance still require implementation testing.

</details>

<details>
<summary><strong>Data visualization</strong></summary>

- **[Visualization](https://github.com/atlassian-labs/data-visualization-skill/tree/main/skills/visualization)** — From `atlassian-labs/data-visualization-skill`: choose chart types and create or restyle Plotly charts from DataFrames using a shared style configuration, consistent colors, and direct labels. Covers interactive HTML and static image export, with guidance on axes, readability, and creation-date annotations.

</details>

<details>
<summary><strong>HTML presentations and visual summaries</strong></summary>

- **[Visualize](https://github.com/careerhackeralex/visualize/tree/main/skills/visualize)** — From `careerhackeralex/visualize`: create single-file HTML presentations, dashboards, infographics, timelines, and visual summaries using a shared skeleton, themes, and browser libraries.
  - **Instruction inconsistencies:** competing chart lifecycle patterns (`ChartManager.safeInit()` versus direct `new Chart()` and canvas replacement); conflicting animation and style guidance, including a hover-transform checklist despite an explicit ban on translated/scaled card hovers. Reconcile these instructions before use.
  - **Offline limitation:** the claimed offline, self-contained output depends on CDN-hosted chart/export libraries and Google Fonts; reliable offline use requires local or embedded dependencies and an offline acceptance test.
  - **Delivery mismatch:** automatic browser opening and `file://` links assume a local desktop. For Telegram, deliver the HTML as an attachment and provide a PNG/PDF preview when needed, rather than a local filesystem link.
  - **Reported test scope (not independently verified here):** one scenario, not full certification. The tester reported using custom Playwright checks and visual inspection; the official evaluator was not run because its dependencies were missing.

</details>

## Libraries and references

<details>
<summary>Browse collections, standards, and discovery tools</summary>

### Find skills

- **[skills.sh](https://skills.sh)** — Search the Agent Skills directory and browse trending skills; follow each result to its original source before installing.

### Repositories and references

- **[Skill-kit](https://github.com/Youmair/skill-kit)** — A concept-organized design knowledge library for AI agents, covering visual styles, palettes, typography, UI patterns, components, charts, and workflow rules, with source metadata and reusable CSS/Tailwind snippets. Browse `_MOC.md` to select relevant files; aggregated content retains per-file upstream licenses, including CC-BY-SA and custom terms, rather than one blanket MIT license.

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

</details>

---

[MIT license](LICENSE) · [Provenance](DRAFT-PROVENANCE.md) · [Markdown layout gallery](MARKDOWN-EXAMPLES.md)
