---
name: github-delivery-verification
description: "Verify GitHub delivery against a fixed revision."
license: MIT
metadata:
  status: ready
  provenance: owner-confirmed
---

# GitHub delivery verification

## When to use
Verify an already authorized delivery; this workflow grants no push, merge,
rerun, security-query, or policy-change permission. Requires Git and an already
configured GitHub CLI. Never collect credentials in a receipt.

## Procedure
1. Discover the checkout and remote using `terminal`: `git remote -v`,
   `git status --short --branch`, and `git rev-parse HEAD`. Record the intended
   branch, full commit ID, approved path set, and intended file hashes. Include
   untracked and staged files when measuring scope; unstaged diffs omit them.
2. Query `git ls-remote --heads origin <branch>` and the local tracking ref.
   Fetch only if authorized to update local refs. Require intended HEAD,
   fresh tracking ref, and advertised branch SHA to agree. If the branch has
   advanced, distinguish delivery of the fixed commit from current-tip equality.
   Never repair a mismatch with another push or reset.
3. Read each approved file at the fixed SHA with
   `gh api repos/<owner>/<repo>/contents/<path>?ref=<sha>` through `terminal`.
   Decode base64 as bytes and compare with `git show <sha>:<path>` and the
   intended snapshot. Do not normalize whitespace or Unicode. For large files,
   use the fixed tree's blob SHA and Git Blobs response; require an untruncated
   tree before claiming complete membership. Account for every requested path.
4. Query `gh run list --repo <owner>/<repo> --commit <sha> --json
   databaseId,status,conclusion,headSha,url` and inspect relevant jobs with
   `gh run view`. Retry an initially empty result within a bounded observation
   window. Report queued, running, absent, skipped, and failed distinctly.
   Confirm actual gate coverage, not workflow names or aggregate counts.
5. Report fixed SHA, branch equality, byte readback, worktree state, and
   exact-SHA gate conclusions separately. An observer timeout is not CI failure.

## Pitfalls
A server bypass warning means an exception, not satisfied branch rules.
Green CI does not prove dependency-alert closure, native acceptance, or a later
commit. Do not expand a non-security delivery into alert remediation.

## Verification
Locate the installed `SKILL.md` using the client's skill metadata; let
`<skill-directory>` be its absolute parent directory. Resolve
[scripts/acceptance.py](scripts/acceptance.py) from that directory, not the
current working directory or a presumed repository checkout. Replace the
placeholders before running through `terminal`:

`terminal(command="python \"<skill-directory>/scripts/acceptance.py\"")`

Use the supported Python interpreter available on the host. Quote paths,
including paths with spaces; no repository-root working directory is required.
It tests SHA and exact-byte comparison only; no GitHub delivery occurs.
