# monospace-data-bars

Agent Skill for selecting, rendering, and validating monospace data bars.

## Contents

- `SKILL.md` — discovery metadata, selection workflow, operating contract.
- `references/VARIANTS.md` — visual template catalogue.
- `references/RENDERER.md` — JSON input contract and renderer behavior.
- `references/QUALITY-CHECKS.md` — validation rules and edge cases.
- `scripts/render_bar.py` — deterministic renderer; Python 3.10+, standard library only.
- `scripts/test_render_bar.py` — unit tests.
- `evals/evals.json` — positive, negative, and boundary evaluation cases.

## Quick use

```json
{
  "variant": "block",
  "unit": "%",
  "min": 0,
  "max": 100,
  "items": [
    {"label": "CPU", "value": 82},
    {"label": "Disk", "value": 73},
    {"label": "RAM", "value": 56}
  ]
}
```

```bash
python scripts/render_bar.py input.json
python -m unittest discover -s scripts -p 'test_*.py' -v
```

## Design contract

The agent selects a variant based on explicit user instructions and data semantics. The renderer only validates and formats; it does not infer status, target, intent, or scale. If no style is specified, the default is a 12-cell block bar (`█` / `░`) on a 0–100 scale for percentages.

## Compatibility

Portable Agent Skills structure. The bundled renderer requires Python 3.10 or later and no third-party packages. The skill instructions can also be followed manually by agents without Python execution.
