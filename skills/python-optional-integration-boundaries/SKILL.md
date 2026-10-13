---
name: python-optional-integration-boundaries
description: "Keep optional SDK seams lazy, typed, and testable."
license: MIT
metadata:
  status: ready
  provenance: owner-confirmed
---

# Optional Python integration boundaries

## When to use
A base installation must work without an optional SDK, while integration code
needs a narrow typed contract. Requires Python 3.11+ for the bundled example;
no SDK installation, credentials, provider calls, or user databases are needed.

## Procedure
1. Define base behavior when the dependency is absent and test importing the
   public module without constructing an SDK. Import optional code only inside
   its factory. A readiness find_spec probe is not proof that importing works.
2. Catch only `ModuleNotFoundError` naming the exact optional top-level module.
   Re-raise missing transitive modules, ordinary ImportError, initialization
   failures, and absent required factories. Those mean broken/incompatible
   integration, not an absent optional feature. Do not suppress construction
   or provider failures as dependency absence.
3. Define a local Protocol for only the calls consumed. An annotation or cast
   does not validate a dynamic SDK: check required callable attributes at the
   boundary. Keep construction separate from availability and injected fakes.
4. Accept responses as object. Normalize a Mapping with string keys into a local
   `dict[str, object]`, recognize lists with a guard, then validate individual
   fields before use. A runtime-checkable to_dict Protocol checks shape, not
   return types; normalize the returned object again. Reject malformed payloads
   rather than silently claiming empty results are successful responses.
5. Exercise missing, present fake, broken transitive import, ordinary ImportError,
   invalid factory, and malformed response cases in isolation. If project type
   checks are available, report base and optional-profile checks separately;
   synthetic execution does not prove strict type-checker or SDK compatibility.

## Pitfalls
Avoid module-scope try/import/None fallbacks and broad ImportError handling.
Do not leak dynamic Any/Unknown payloads downstream or install an SDK just to
quiet diagnostics. Do not label fake composition as live provider acceptance.

## Verification
Locate the installed `SKILL.md` using the client's skill metadata; let
`<skill-directory>` be its absolute parent directory. Resolve
[scripts/acceptance.py](scripts/acceptance.py) from that directory, not the
current working directory or a presumed repository checkout. Replace the
placeholders before running through `terminal`:

`terminal(command="python \"<skill-directory>/scripts/acceptance.py\"")`

Use the supported Python interpreter available on the host. Quote paths,
including paths with spaces; no repository-root working directory is required.
The example boundary is in [scripts/boundary.py](scripts/boundary.py); resolve
assets from this skill directory. Its explicit fallback is illustrative, not
permission to change an existing product's fallback semantics.
