# Selection Rules

## Decision map

| Information shape / task | Preferred form | Avoid when |
|---|---|---|
| One term and its function | One-sentence definition | Scope cannot fit without losing conditions |
| Short operational instruction | Telegraphic syntax | Actor, condition, or success test becomes ambiguous |
| Ordered steps | Verb + object sequence | Branches or state changes need explicit representation |
| Branching condition | Decision tree | No meaningful branching exists |
| Lifecycle | State transitions | Transition conditions are unknown |
| Known mechanism | Causal chain | Evidence shows correlation only |
| Shared attributes across entities | Comparison table | Only one or two facts are compared |
| Permissions/capabilities | Matrix | Legend or cell meaning is unclear |
| Repeated related fields | Semantic groups | Groups are arbitrary or overlap |
| Time-dependent actions | Timeline | Timing is incidental |
| Current metric plus history | Sparkline/KPI tile | No real ordered series |
| Category ranking | Sorted bars | Exact values are not available or baseline is misleading |
| Result versus defined goal | Bullet graph | Target or bands are not defined |
| Distribution and outliers | Range summary | Sample is too small or distribution details are unavailable |
| Two time points | Slopegraph | More than two periods are central |
| Two-dimensional intensity | Heatmap with values | Scale is not comparable or numbers are omitted |
| Status over time | Status strip | Time intervals are not known |
| Proportion | Waffle or 100% bar | Denominator is missing |
| Command reference | Task → command index | Commands are unverified or environment-specific |
| Command verification | Command + expected output | Output is not deterministic or not supplied |
| Plain-text relative magnitude | Monospace bar | Exact quantitative comparison is required |

## Combining techniques

Combine only when the techniques answer different questions. Examples:
- decision tree + command index: choose path, then find command;
- table + status symbols: compare entities and expose state;
- sparkline + KPI tile: show current value and a real time-series shape;
- command + expected output + checklist: execute, verify, then confirm completion;
- timeline + causal annotation: show when an event occurred and its established effect.

Avoid:
- table + repeated prose that restates every cell;
- chart + redundant legend when direct labels suffice;
- multiple accent colors and bold styles on the same item;
- duplicate definitions of the same abbreviation;
- sparkline and delta with unclear or mismatched periods;
- status color without text or symbol.

## Compression ladder

When content is too long, apply in order:
1. Remove repeated wording.
2. Move shared scope into a clear heading.
3. Convert repeated label/value prose into labeled pairs.
4. Group semantically related facts.
5. Use a table for repeated attributes.
6. Replace repeated detail with a stable cross-reference.
7. Use compact notation only if the audience understands it.
8. Reduce spacing or font size only after semantic and structural optimization.

## Audience adaptation

- Expert audience: concise syntax, command pipelines, abbreviations, symbols, and compact tables may be efficient.
- Mixed audience: define terms, use explicit labels, and prefer prose around unfamiliar notation.
- Nontechnical audience: avoid command syntax as a substitute for instructions; label status in plain language.
- Accessibility or print constraints: ensure meaning survives color removal, zoom, and text extraction.
