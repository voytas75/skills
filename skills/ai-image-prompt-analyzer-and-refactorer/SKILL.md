---
name: ai-image-prompt-analyzer-and-refactorer
description: Refactor image-generation or editing prompts into explicit change/preserve constraints and functional reference-image roles.
---

# Image prompt refactoring

1. **Extract the actual goal.** Separate generation from editing. Identify the
   subject, physical scene, and supplied references. If a critical target or
   conflicting requirement is unclear, ask one focused question rather than invent
   identity, pose, or camera metadata. **Check:** the goal is explicit.
2. **Remove or concretize noise.** This workflow prefers physical constraints to
   vague quality inflation. Remove unsupported award/platform/superlative claims;
   translate meaningful style or lighting requests into observable properties.
   Resolution, HDR, and renderer names are not universally ineffective: they may
   matter to a specific model or requested workflow. Keep real output settings
   separate from the descriptive prompt, and preserve an explicitly requested
   rendering style or ask before discarding it. **Check:** no meaningful user
   constraint was silently deleted and no universal model-effect claim is made.
3. **Separate change from preservation.** For an edit, select one bounded edit
   objective. Preserve applicable identity, facial structure, pose, garment,
   framing, perspective, and lighting except properties explicitly changed.
   Do not assert unknown exact focal lengths. If compositing needs coordinated
   lighting changes, name those within the same objective, never as invariants.
   For a new image use a creation target, not fictional original-image invariants.
   **Check:** nothing is simultaneously changed and preserved.
4. **Assign references by function.** Give each image one distinct extraction role,
   such as subject identity/garment or environment geometry/materials. Explicitly
   exclude unintended transfer. Read [references/worked-examples.md](references/worked-examples.md)
   when the roles or edit boundary need illustration. **Check:** every supplied
   reference has a role; conflicting roles are resolved or queried.
5. **Return this inspectable schema.** Omit reference roles when none exist and
   omit output settings when none were requested. For generation, preservation
   can state only user-specified invariants or say no original image exists.

```text
CORE INTENT: <Physical summary of goal>
[TARGET TO CHANGE]: <One bounded edit objective, or creation target>
[PRESERVATION LIST]: <Applicable unchanged properties; exclude changes>
[REFERENCE ROLES]:
  - Reference Image 1: Extract strictly <distinct role; exclusions if needed>.
[OUTPUT SETTINGS]: <Requested supported settings, separate from scene description>
```

**Done:** the prompt makes the target, invariants, and reference roles explicit;
no contradictions or invented metadata remain. This skill produces text only,
not images. Prompt structure is not a guarantee of deterministic model obedience.
