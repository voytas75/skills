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
| [KPI Trend Tiles](skills/kpi-trend-tiles/SKILL.md) | Create compact horizontal metric tiles with grounded values, comparison periods, and optional time-series sparklines. |
| [Monospace Data Bars](skills/monospace-data-bars/SKILL.md) | Render validated numeric data as aligned text bars with explicit scales, units, and optional supplied targets or deltas. |
| [Text Presentation Techniques](skills/text-presentation-techniques/SKILL.md) | Choose concise text structures, tables, diagrams, and reference-sheet layouts while preserving scope, conditions, and evidence. |
| [Visual Knowledge Design](skills/visual-knowledge-design/SKILL.md) | Choose and create diagrams, charts, and visual learning aids that preserve source meaning, with retrieval practice when retention matters. |
| [Unicode Text Charts](skills/unicode-text-charts/SKILL.md) | Create text-native sparklines, heatmaps, hierarchies, timelines, and Gantt charts with explicit mappings and source-backed data; defines requirements for Braille plotting. |
| [Mnemonic Design](skills/mnemonic-design/SKILL.md) | Design memory hooks, cards, stories, and memory palaces using imagery, associations, and recall cues; memory-strength ratings are heuristic. |
| [Design System Extraction](skills/design-system-extraction/SKILL.md) | Inspect existing website designs, retain measurement evidence, and verify visual reconstructions with separate extraction, fidelity, and functionality outcomes. |

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

- **[Document Design](https://github.com/jamditis/claude-skills-journalism/tree/master/pdf-playground/skills/document-design)** — From `jamditis/claude-skills-journalism` (`pdf-playground`): create branded HTML proposals, reports, one-pagers, newsletters, slides, and flyers for browser-based PDF export, using bundled templates and brand configuration. Defaults to US Letter rather than A4; requires visual checks for content overflow and footer clearance, replacement of unresolved slide assets, and local or embedded fonts for offline use. Produces HTML with PDF export instructions, not an automatically verified final PDF.

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

- **[UI/UX Pro Max](https://github.com/sidiangongyuan/codex-skills-library/blob/main/skills/ui-ux-pro-max/SKILL.md)** — From `sidiangongyuan/codex-skills-library`: design, implement, or review web and mobile interfaces using searchable product patterns, palettes, typography, charts, accessibility guidance, and frontend-stack recommendations. Requires Python 3 and bundled search scripts/data, with optional master and page-specific design-system files; prioritizes accessibility, safe interaction, and product fit over visual novelty. Recommendations remain candidates until checked against the existing product and validated in rendered states, supported viewports, and relevant devices.

- **[HTML Design Styles](https://github.com/chrismccoy/forge/blob/master/lib/html-design-styles/SKILL.md)** — From `chrismccoy/forge`: build or restyle HTML/CSS pages and components using a user-selected named aesthetic, with prescribed palettes, typography, layouts, and component patterns rather than an improvised generic theme. The root file routes to shared and style-specific references via Claude plugin paths, which need adaptation in other runtimes; its default Tailwind CDN output is not offline self-contained. Review accessibility independently: the instructions permit specified styles to retain WCAG deviations with only a warning comment.

- **[Web Design](https://github.com/pascalorg/skills/blob/main/web-design/SKILL.md)** — From `pascalorg/skills`: build and review web interfaces using a prioritized reference covering semantic HTML, responsive layout, typography, design tokens, component states, accessibility, motion, and performance, with CSS and Tailwind examples. Addresses interface implementation and design review rather than publication layout or presentation generation; its checklists do not replace browser, keyboard, and accessibility testing.

- **[Web Design Skill Pack](https://github.com/TobiasKulvik/web-design-skills/blob/main/SKILL.md)** — From `TobiasKulvik/web-design-skills`: coordinate framework-agnostic web design by selecting topical sub-skills for content structure, layout, typography, color, components, UX flows, SEO, internationalization, accessibility, and frontend implementation. The root file is an orchestrator and reading guide, not a standalone design reference; consult the linked sub-skills for detailed guidance.

- **[Frontend Design](https://github.com/thekorn/agent-skills/blob/main/skills/frontend-design/SKILL.md)** — From `thekorn/agent-skills`: turn a brief into coded web pages or components by choosing one distinctive aesthetic direction and defining typography, color, layout, and motion before implementation. Calls for responsive, semantic interfaces with tokenized styling and full code deliverables; its emphasis on expressive visual identity is not a substitute for runtime, accessibility, or production-readiness testing.

- **[Frontend Design (Anthropic)](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)** — From `anthropics/skills`: build or reshape interfaces around the brief's subject, audience, and visual identity, using a compact palette, typography plan, and layout sketches before coding. Reviews the plan against generic defaults and combines restrained motion, clear interface copy, and screenshot-based self-critique; accessibility and responsive-design guidance still require implementation testing.

</details>

<details>
<summary><strong>Data visualization</strong></summary>

- **[Data Visualization (Anthropic)](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/data-visualization/SKILL.md)** — From `anthropics/knowledge-work-plugins`: choose charts by data relationship and create static figures or interactive HTML using Python, matplotlib, seaborn, and Plotly. Covers readable labels, meaningful scales, uncertainty, purposeful color, and accessible alternatives; code examples and accessibility guidance require execution and inspection on the actual data rather than being treated as validated outputs.

- **[Visualization](https://github.com/atlassian-labs/data-visualization-skill/tree/main/skills/visualization)** — From `atlassian-labs/data-visualization-skill`: choose chart types and create or restyle Plotly charts from DataFrames using a shared style configuration, consistent colors, and direct labels. Covers interactive HTML and static image export, with guidance on axes, readability, and creation-date annotations.

</details>

<details>
<summary><strong>HTML presentations and visual summaries</strong></summary>

- **[To HTML](https://github.com/pbi-agent/skills/blob/main/skills/to-html/SKILL.md)** — From `pbi-agent/skills`: turn concepts, analyses, implementation plans, and code reviews into task-focused HTML artifacts with cards, SVG charts, tables, annotated snippets, and lightweight interaction or copy/export controls. Defaults to a single file with inline CSS and JavaScript, grounded data, and separate evidence and interpretation; optional Mermaid rendering uses jsDelivr and is unsuitable for offline or confidential work without local adaptation. Requires browser checks at narrow and desktop widths and testing of every interactive control.

- **[Visual Explainer (journalism adaptation)](https://github.com/jamditis/claude-skills-journalism/tree/master/visual-explainer)** — From `jamditis/claude-skills-journalism` (metadata credits `nicobailon` upstream and journalism adaptations by `jamditis`): create HTML explainers, diagrams, timelines, source networks, investigation maps, slide decks, and visual plan or diff reviews. Uses package-local templates, references, and vendored diagram libraries, including Mermaid zoom/pan controls; external font loading means a single HTML file does not guarantee offline self-containment. Browser opening and optional Vercel publication are separate delivery actions, not requirements for using the catalog link.

- **[Visualize](https://github.com/careerhackeralex/visualize/tree/main/skills/visualize)** — From `careerhackeralex/visualize`: create single-file HTML presentations, dashboards, infographics, timelines, and visual summaries using a shared skeleton, themes, and browser libraries.
  - **Instruction inconsistencies:** competing chart lifecycle patterns (`ChartManager.safeInit()` versus direct `new Chart()` and canvas replacement); conflicting animation and style guidance, including a hover-transform checklist despite an explicit ban on translated/scaled card hovers. Reconcile these instructions before use.
  - **Offline limitation:** the claimed offline, self-contained output depends on CDN-hosted chart/export libraries and Google Fonts; reliable offline use requires local or embedded dependencies and an offline acceptance test.
  - **Delivery mismatch:** automatic browser opening and `file://` links assume a local desktop. For Telegram, deliver the HTML as an attachment and provide a PNG/PDF preview when needed, rather than a local filesystem link.
  - **Reported test scope (not independently verified here):** one scenario, not full certification. The tester reported using custom Playwright checks and visual inspection; the official evaluator was not run because its dependencies were missing.

</details>

<details>
<summary><strong>Research and evidence gathering</strong></summary>

- **[Root Cause Analysis](https://microsoft.github.io/cat-agent-skills/skills/root-cause-analysis)** — From Microsoft's CAT Agent Skills gallery (credited to Nayananshu Garai): diagnose incidents and recurring failures through a precise problem statement, 5 Whys, and a six-category Fishbone diagram, separating root causes from contributing factors and prioritizing corrective actions. Requires the bundled HTML diagram template and labels factors as confirmed, unverified, or disproven; its confirmation rule refers only to facts supplied by the user, not independent system verification. Intended for structured diagnosis and post-mortems rather than general planning.

- **[Research](https://github.com/yeachan-heo/oh-my-claudecode/tree/main/skills/research)** — From `yeachan-heo/oh-my-claudecode`: investigate an open question using repository files and documentation first, official external documentation when needed, and complementary searches by file, symbol, caller, or history. Returns sourced findings, contradictions, and remaining uncertainty, with parallel investigation for independent questions; research explicitly excludes implementation as a side effect.

</details>

<details>
<summary><strong>Software change impact and delivery review</strong></summary>

- **[ADR Skill](https://github.com/vercel/ai/tree/main/skills/adr-skill)** — From `vercel/ai`: create, consult, and maintain Architecture Decision Records for agent-assisted implementation, starting with repository discovery and a human-confirmed intent summary. Captures alternatives, measurable constraints, non-goals, affected paths, implementation plans, and verification criteria, with templates and Node.js helpers for records, statuses, and indexes. Marked internal in its metadata; bundled helpers and review resources are required for the full workflow, and an accepted ADR is not proof that its implementation has been verified.

- **[Change Impact Analysis](https://github.com/affaan-m/ECC/blob/main/skills/change-impact/SKILL.md)** — From `affaan-m/ECC`: map the evidence-backed impact of a planned change on callers, data, schemas, public contracts, tests, documentation, deployment, migration, and rollback, then reconcile that map with the implemented diff and verification results. Read-only by default, with explicit unknowns and checks for unauthorized scope drift; routes durable decisions, contracts, and regression evidence to related ECC skills and existing project records rather than creating parallel sources of truth. Its companion skills are separate dependencies, not inspected or included by this listing.

</details>

<details>
<summary><strong>Statistical analysis and analytical quality assurance</strong></summary>

- **[Statistical Analysis](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/statistical-analysis/SKILL.md)** — From `anthropics/knowledge-work-plugins`: analyze distributions, trends, seasonality, outliers, correlations, and hypothesis tests, with descriptive statistics, simple forecasting, and Python examples. Emphasizes effect sizes, confidence intervals, practical significance, and common inferential pitfalls; its simplified test-selection rules and sample-size heuristics are starting points, not substitutes for checking assumptions, power, and the study design.

- **[Validate Data](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/validate-data/SKILL.md)** — From `anthropics/knowledge-work-plugins`: review an analysis before sharing by checking methodology, population and metric definitions, data quality, SQL joins, denominators, period alignment, calculation spot-checks, charts, and supported conclusions. Returns prioritized issues, required caveats, and a readiness assessment; meaningful verification requires access to source data, queries, and results, while connector setup is documented separately in the parent plugin.

</details>

## Libraries and references

<details>
<summary>Browse collections, standards, and discovery tools</summary>

### Find skills

- **[skills.sh](https://skills.sh)** — Search the Agent Skills directory and browse trending skills; follow each result to its original source before installing.

### Repositories and references

- **[NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)** — An experimental evaluation tool, not a single standalone skill: check static quality and security, detect overlapping guidance, and compare sandboxed agent runs with and without a skill. Includes an agent-facing `skills/skillevaluator/` package and CI templates; basic quality checks can run without an LLM, while security scanning, deduplication, and live evaluation have separate scanner, provider, and sandbox requirements. Static scores do not establish safety or agent effectiveness; model and managed-sandbox use can incur charges. Licensed under Apache 2.0 with additional third-party notices.

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
