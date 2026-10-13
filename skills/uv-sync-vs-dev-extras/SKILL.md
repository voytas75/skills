---
name: uv-sync-vs-dev-extras
description: "Diagnose uv groups, extras, and environment drift."
license: MIT
metadata:
  status: ready
  provenance: owner-confirmed
---

> Based on owner-confirmed original operational procedures; distributed under MIT.
> See [provenance](../../DRAFT-PROVENANCE.md).

# uv groups, extras, and reconciliation

## When to use
Developer packages disappear after sync or an entry point runs in the wrong
profile. Requires uv; first check `uv --version` and installed command help via
`terminal`. Read pyproject and lockfile using `read_file` before any sync.

## Procedure
1. Distinguish `[project.dependencies]`, `[project.optional-dependencies]`, and
   `[dependency-groups]`. An extra named dev and a group named dev are different.
   Inspect `[tool.uv].default-groups`: the usual default is the dev group, not
   the dev extra; configuration can select other defaults or all groups.
2. Map the desired profile explicitly. Through `terminal`, use
   `uv sync --locked --extra dev` for an extra, or
   `uv sync --locked --group dev` for a group. Use `--no-default-groups`
   to suppress configured defaults; `--only-group dev` excludes the project
   and defaults. Exclusions override inclusions. Do not migrate metadata or
   enable every extra simply to hide a missing optional dependency.
3. Explain exactness correctly: `uv sync` removes extraneous packages by default;
   `--inexact` retains them. Current `uv run` syncs inexactly by default;
   `--exact` opts into removal. Repeat profile flags for reproducibility even
   when leftover packages make an inexact run appear to work.
4. Separate lock freshness from environment state. `--locked` checks freshness
   and refuses lock changes; `--frozen` trusts the existing lock without that
   check. `uv run --no-sync` avoids synchronization and implies frozen behavior;
   it does not prove environment freshness. All ordinary run/sync commands can
   mutate an environment. Do not apply them to an unapproved project environment.
5. Reproduce only in an authorized disposable area. Compare installed package
   membership before/after each profile, not just a successful command exit.
   Distinguish offline fixture evidence from the real project's resolution.

## Pitfalls
Manual `uv pip install -e '.[dev]'` does not change sync selections. Ownership,
wrong interpreter, stale locks, and optional imports are separate hypotheses.
Do not use --active to modify the agent environment or auto-upgrade uv.

## Verification
Run `terminal(command="python skills/uv-sync-vs-dev-extras/scripts/acceptance.py
<authorized-scratch-directory>")`. The offline fixture uses synthetic wheels,
no registry or build backend; it checks groups, extras, exactness, and run flags.
Current behavior references: [dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/)
and [sync](https://docs.astral.sh/uv/concepts/projects/sync/).
