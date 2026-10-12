---
name: feature-slice-planner
description: Turn a broad feature idea, project goal, refactor target, or vague implementation request into one bounded next slice with acceptance checks, rollback, and anti-goals. Use when the user asks to narrow scope, choose the next implementation step, break work into a small shippable slice, plan before coding, decide what to do now vs later, or prepare a concise build brief before delegating to a coding agent. Do not use when the next step is already obvious and small enough to do directly.
---

# Feature Slice Planner

Use this skill to reduce scope before implementation.

## Purpose

Produce exactly one recommended next slice from a broader goal.

Prefer this skill when the problem is too wide, fuzzy, or expansion-prone for immediate implementation.

Do not use this skill to create a roadmap, multi-sprint plan, repo-wide discovery, or general product strategy.

## Required input

Extract or ask for:

- `goal` — required
- `constraints` — optional; include only real scope guards
- `context files` — optional; include only clear SSOT files or files explicitly provided by the user
- `size` — optional; use `small` by default
- `audience` — optional

If the goal is missing or too vague to plan responsibly, ask exactly one clarifying question.

If the goal is already narrow enough to implement directly, do not use this skill.

## Strong defaults

- Default size: `small`
- Default output for chat: concise markdown summary
- Use JSON output only when another step needs machine-readable structure
- Prefer minimal context over broad repo ingestion

## What this skill must not do

Do not:

- expand into roadmap generation
- crawl the whole repo by default
- redesign unrelated contracts
- produce multiple competing slices unless the user explicitly asks
- auto-delegate to a coding agent
- write backlog, tickets, or files unless explicitly asked

One good slice is better than five speculative ones.

## Execution (instruction-only)

No wrapper, private project, framework, or executable is required.

1. Normalize the goal and actual constraints. Read only supplied canonical context;
   separate facts from assumptions. **Check:** the goal and hard boundaries are explicit.
2. Identify the smallest useful user-visible seam that advances the goal. Select
   exactly one slice, naming a concrete artifact (file, command, endpoint, document,
   or interface). **Check:** it can be reviewed and delivered independently.
3. List only work needed for that seam under Do now; defer adjacent work under
   Do later. Respect the requested size: micro is one narrow behavior, small is one
   bounded seam, medium may span coupled components but remains one deliverable.
   **Check:** no roadmap or unrelated redesign has entered the slice.
4. Write observable acceptance checks, including a specific test, smoke command,
   or inspection method and its expected result. Describe a practical rollback and
   explicit anti-goals. **Check:** a reviewer can distinguish pass, fail, and unknown.
5. Return the contract below, tailored to the audience. Do not implement, delegate,
   write files, or claim tests ran. **Check:** exactly one slice is recommended.

For requested JSON, use `recommended_slice`, `why_this_now`, `do_now`, `do_later`,
`acceptance_checks`, `rollback`, `anti_goals`, and optional `open_questions`.
Use strings for the first two fields and rollback; use arrays of strings for lists.
This is a portable output convention, not compatibility with a private runtime API.

## Output contract for chat

Present the result in this order:

1. **Recommended slice**
2. **Why this now**
3. **Do now**
4. **Do later**
5. **Acceptance checks**
6. **Rollback**
7. **Anti-goals**
8. **Open questions** only if truly needed

Keep the response tight. Do not dump raw JSON into chat unless the user asks for it.

## Output shaping rules

Summarize the planner output into operator-friendly language.

Preserve the planner’s bounded posture:

- keep exactly one recommended slice
- keep acceptance checks concrete
- keep rollback practical
- keep anti-goals explicit

If the tool output is broader than the task requires, compress it back to one bounded slice.

## Context-file policy

Attach context files only when they materially improve the slice recommendation.

Good examples:

- explicit SSOT doc
- current contract doc
- reviewed benchmark sample
- one specific implementation checklist

Bad examples:

- whole repo docs
- broad notes folders
- unrelated design material
- “just in case” files

## When to skip this skill

Skip this skill when:

- the user asked for a direct small change
- the next step is already obvious
- the task is pure implementation with no scope ambiguity
- a simple answer or direct coding action is enough

## Worked example

See [references/worked-example.md](references/worked-example.md) for a neutral
input and a complete bounded output. Before returning, check that the deliverable,
acceptance method, rollback, and anti-goals agree with the supplied constraints.
