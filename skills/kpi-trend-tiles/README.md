# kpi-trend-tiles

Agent Skill for creating and reviewing compact horizontal KPI tiles.

## Design target

Default composition follows the compact reference tile:

`[primary value] [metric label + delta/period] [optional sparkline]`

Example structure:
- left: `18 ms`
- middle: `Latency` and `↓ −12% vs previous 7 days`
- right: small sparkline, only when a real ordered series is supplied

The design prioritizes information density and fast scanning rather than large dashboard cards.

## Variants

- compact with sparkline;
- compact without sparkline;
- compact with favorable/unfavorable interpretation;
- delta-focused;
- target/threshold note;
- value-only when comparison data is unavailable.

## Structure

```text
kpi-trend-tiles/
├── SKILL.md
├── README.md
├── references/
│   ├── DATA-SEMANTICS.md
│   ├── DESIGN-SYSTEM.md
│   └── QUALITY-CHECKS.md
├── examples/
│   └── kpi-tiles.html
└── evals/
    └── evals.json
```

Load `SKILL.md` as the entry point. Read only the relevant reference. Example values are illustrative and must never be copied as user facts.
