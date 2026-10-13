---
name: cross-platform-python-runtime-recovery
description: "Recover Python runtimes with separate host evidence."
license: MIT
metadata:
  status: ready
  provenance: owner-confirmed
---

# Cross-platform Python runtime recovery

## When to use
A Python entry point fails on Linux/WSL or Windows. Requires the project's
supported interpreter and test runner; Git and uv commands below are conditional
on project tooling. Do not install native components or call providers merely
to diagnose a local failure.

## Procedure
1. Read the first deterministic traceback using `read_file`. Separate symbol
   scope/control flow, dependency API, native runtime, and checkout identity.
   A preceding browser warning does not explain a later Python NameError.
2. Inspect declarations, lockfile, entry point, and interpreter provenance.
   Use independent native checkouts and environments; never share a virtualenv
   across operating systems. Record `sys.executable`, `sys.platform`, and
   `sys.prefix` without copying private environment variables into evidence.
3. Add a focused provider-free regression at the public entry point before a
   source repair. Keep heavy imports inside factories. Pass needed helpers via
   explicit return values or a small dependency carrier, not hidden globals.
   Assert cleanup after success and application failure; preserve the original
   error if cleanup also fails. Confirm RED then GREEN where repair is needed.
4. Through `terminal`, run Linux commands from its own checkout:
   `git status --porcelain`, `git rev-parse HEAD`,
   `.venv/bin/python -m pytest -q <focused-test>`.
   In a native Windows PowerShell terminal, independently run:
   `git status --porcelain`, `git rev-parse HEAD`,
   `& .\.venv\Scripts\python.exe -m pytest -q <focused-test>`.
   For uv-managed projects first verify `uv lock --check`; a later
   `uv run --locked --group dev ...` may sync the environment and needs approval.
   Use `--extra dev` instead if dev is an extra, not a group.
5. Run only an established no-provider help/dry-run entry point. If an environment
   has wrong-platform links or ownership, inspect it with native tools and stop
   before deletion. Replacement requires explicit approval and proof the target
   is disposable, ignored, untracked, and confined to that checkout.

## Pitfalls
Native Git is the authority for a Windows checkout with newline representation
noise. Do not stage widespread WSL-reported changes blindly. Driver and browser
compatibility need their own version/probe evidence, not a Python-only test.

## Verification
Locate the installed `SKILL.md` using the client's skill metadata; let
`<skill-directory>` be its absolute parent directory. Resolve
[scripts/acceptance.py](scripts/acceptance.py) from that directory, not the
current working directory or a presumed repository checkout. Replace the
placeholders before running through `terminal`:

`terminal(command="python \"<skill-directory>/scripts/acceptance.py\"")`

The bundled synthetic check requires Python 3.11+ (`BaseException.add_note`).
Use the supported Python interpreter available on the host. Quote paths,
including paths with spaces; no repository-root working directory is required.
This synthetic lifecycle test and static command review do not qualify native
Windows, browser, driver, permissions, or the user's application.
