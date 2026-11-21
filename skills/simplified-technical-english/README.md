# Simplified Technical English skill

This skill makes an LLM write in Simplified Technical English (STE).
STE is a controlled language for technical documentation.
The specification ASD-STE100 gives the rules of STE and its dictionary.
The aerospace and defense industries use STE for their manuals.
Text in STE is clear, short, and easy to translate.

The skill obeys the rules that it gives. This README is in STE.

## Example

Text before the change:

> Prior to commencing the installation, it should be ensured that all
> components have been thoroughly inspected for damage.

Text after the change:

> Before you start the installation, examine all the components for damage.

## Contents of this repository

| File | Function |
|---|---|
| `SKILL.md` | The primary instructions for the LLM |
| `references/writing-rules.md` | The 53 writing rules, with examples |
| `references/word-list.md` | The 869 approved words |
| `references/substitutions.md` | Replacements for frequent unapproved words |
| `examples/before-after.md` | Examples of text before and after the change |
| `scripts/ste_check.py` | A check tool for the STE rules |
| `NOTICE.md` | Copyright information |

## How to install the skill for Claude

1. Clone this repository into your skills folder:

       git clone https://github.com/0xpili/simplified-technical-english.git ~/.claude/skills/simplified-technical-english

2. Tell Claude to write or examine technical text in STE.
3. Claude finds the skill and obeys the rules.

You can also start the skill directly. Type `/simplified-technical-english`.

## How to use the skill with a different LLM

1. Open `SKILL.md`. Copy its text into the system prompt of the LLM.
2. If the LLM accepts more text, add the text of `references/substitutions.md`.
3. For the best results, also add the text of `references/word-list.md`.
4. Tell the LLM to write technical text.
