# Mnemonic Design

**Version:** 2.0.0 · **Author:** voytas75 · **Category:** learning-and-information-design

A modular Agent Skill for designing, generating, and validating memory aids. It prioritizes accurate retrieval and retention over novelty or decorative mnemonics.

## Package
`SKILL.md`, `VERSION`, `CHANGELOG.md`, `references/`, `assets/`, and `examples/`.

## Installation
Copy the `mnemonic-design` directory into the skills directory supported by your agent runtime. Keep the directory name identical to the frontmatter `name`.

## Example requests
- Create mnemonics for these technical terms.
- Help me memorize the OSI layers and test recall.
- Build a memory palace for this ordered list.
- Encode this number using a reversible mnemonic system.
- Create contrastive memory cards for easily confused concepts.
- Build a spaced review plan for these exam facts.

## Constraints
Mnemonics preserve source accuracy; retrieval must be tested; no numerical strength score is used; memory aids do not replace understanding or practical skill. Review intervals are adaptive heuristics, not universal prescriptions.

## Validation
Run `skills-ref validate` when available. Static validation does not prove agent behavior. Test vocabulary, sequences, numbers, technical concepts, and procedures separately.
