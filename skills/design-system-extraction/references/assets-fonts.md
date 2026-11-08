# Asset and font fidelity
Inventory source and target fonts, icons, logos, SVG, raster images, CSS resources. For each: identity, origin, status, license/policy constraint, target disposition (`retained|recreated|substituted|omitted|unresolved`), impact, evidence.

A policy prohibiting source asset copying creates an explicit substitution constraint; it does not make captures unmeasurable. Keep source asset observation and target asset choice distinct.

Font checks:
- record CSS declared family stack separately from actual resolved font;
- where available, inspect platform-resolved fonts per node/text run/glyph (e.g. Chromium CDP `CSS.getPlatformFontsForNode`);
- record text sample, node/selector, declared family, resolved families, glyph count, fallback, method, browser/version, evidence;
- `document.fonts.check()` or FontFace loaded state alone is not proof of glyph resolution;
- if resolved font cannot be determined, `font_identity` is `NOT_TESTED`/ineligible; geometry and screenshot modalities may remain eligible;
- report glyph-level fallback and unknown/noncanonical font names without inventing canonical identities.

Substitution/unresolved asset => `asset_fidelity` cannot PASS unless explicitly excluded before execution and accepted by frozen scope. Even then, record limitation; do not erase the substitution.
