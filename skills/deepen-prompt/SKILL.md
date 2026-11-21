---
name: deepen-prompt
description: Rewrites a task or prompt into a deeper version (not a bigger one). Before rewriting, answers what a top professional in the field would do that was not asked for, the rawest material they would start from, the specific methods and tools they would use, and what outside of the model or user would show the result is right. Then produces a paste-ready rewritten prompt that asks for exactly that. Use when the user says deepen, go deeper, make this prompt better, what would an expert do, sharpen this task, or before non-trivial research, analysis, debugging, or data work where a shallow answer is likely. Based on Felix Rieseberg's depth prompt.
license: MIT
metadata:
  author: voytas75
  version: 1.0.0
  source: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
---

# Deepen prompt

Turn a task into the version a field-leading professional would actually do: same scope, deeper work.

The output is a short diagnosis plus a rewritten prompt the user can run.

Core original prompt (Felix Rieseberg, 13 October 2026):

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

## Core rule: deeper, not bigger

Depth changes **how** the work is done (inputs, instruments, verification).  
Bigness changes **how much** is delivered (more sections, more features, more pages).  
Reject bigness. Keep the user's goal and scope. Do not add deliverables, features, or side quests.

## Procedure

1. Restate the user's task in one sentence (scope-preserving).
2. Answer the four questions, each in 1–3 concrete lines specific to this task. Avoid generic advice.
   - What would a top professional do here that was not asked for?
   - What is the rawest material they would start from (logs, raw data, primary sources, transcripts, not summaries or dashboards)?
   - Which specific methods and tools would they use (name them: databases + statistical models, particular libraries, instruments, workflows)?
   - What, other than the model or the user, would show the result is right (external judge, reproducible check, held-out data, independent measurement)?
3. Rewrite the prompt so that it explicitly asks for the raw material, the named methods/tools, the outside verification, and any hard target. Keep it concise and paste-ready.
4. Stop. Do not execute the rewritten prompt unless the user explicitly asks to run it.

## Anti-patterns

- Expanding scope or adding sections "for completeness".
- Role-play ("act as a senior X") without changing methods or inputs.
- Self-grading or "I have verified this" without an external check.
- Starting from already-digested summaries when raw material is available.
- Vague "best practices" or "use a professional approach".

## Output template

```
**Diagnosis**
- Expert action not asked for: ...
- Rawest material: ...
- Methods & tools: ...
- Outside verification: ...

**Rewritten prompt**
[paste-ready prompt that asks for exactly the above]
```

## Notes

- Prefer named, runnable instruments over vocabulary changes.
- If raw material or external verification is unavailable, state the prerequisite clearly rather than inventing a substitute.
- Credit the idea to Felix Rieseberg; this packaging adds procedure, anti-patterns, and output template.
