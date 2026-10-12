# Worked examples

These fictional prompts illustrate [the parent workflow](../SKILL.md); no image
model was run. Actual output fidelity depends on the chosen model and settings.

## Background edit

**Input:** Replace the background of the supplied cyclist portrait with a snowy
forest, 8k, award-winning masterpiece. Do not change the cyclist.

```text
CORE INTENT: Place the existing cyclist in a snowy forest.
[TARGET TO CHANGE]: Replace only the background with a snowy forest.
[PRESERVATION LIST]: Preserve subject identity, face geometry, pose, clothing,
  bicycle geometry, framing, perspective, and existing subject illumination.
[REFERENCE ROLES]:
  - Reference Image 1: Extract strictly the cyclist and bicycle, not the background.
[OUTPUT SETTINGS]: Requested 8k output; confirm whether the selected tool supports it.
```

The award claim adds no physical constraint here. Requested resolution is retained
as a setting, not dismissed as universally useless. Do not invent a focal length.

## Compositing with coordinated lighting

**Input:** Place the chair from Image 1 in the room from Image 2. Match the room's
warm side light. Keep the chair's shape and fabric.

```text
CORE INTENT: Composite the reference chair into the reference room.
[TARGET TO CHANGE]: Replace the chair's environment with the room from Image 2,
  including coordinated chair illumination consistent with that room's warm side light.
[PRESERVATION LIST]: Preserve the chair's geometry, upholstery pattern, and fabric
  texture from Image 1, and room geometry and camera view from Image 2.
[REFERENCE ROLES]:
  - Reference Image 1: Extract strictly chair geometry and upholstery; exclude backdrop and lighting.
  - Reference Image 2: Extract strictly room geometry, camera view, and lighting setup; exclude furnishings to be replaced.
```

Lighting is a changed component of one compositing objective, not an invariant
or an extra fictional reference image. If scale or placement is consequential
and not apparent from the assets, ask before adding it.

## Generation without a reference

**Input:** Create a simple studio photograph of a blue ceramic mug on a gray table.

```text
CORE INTENT: Show a blue ceramic mug on a gray tabletop in a studio scene.
[TARGET TO CHANGE]: Create the described scene; no source image is being edited.
[PRESERVATION LIST]: Retain the requested blue ceramic material and gray tabletop;
  there are no original-image identity or camera invariants.
```
