# Density and Medium

## Density modes

### Normal
- comfortable reading size and spacing;
- suitable for longer reading, mixed audiences, and mobile;
- prioritize legibility over page count.

### Compact
- default for technical cheat sheets and operational reference documents;
- reduce repeated labels and whitespace;
- use small but legible typography and clear section separation;
- preserve enough spacing to distinguish cards and groups.

### Maximum
- use only when the reader and output medium support it;
- appropriate for a dense index or quick-reference sheet, not continuous reading;
- never shrink text until it becomes difficult to read;
- verify on the actual device and in print/PDF.

## Density optimization

Optimize in this order:
1. remove redundancy;
2. group related facts;
3. use concise labels;
4. select a better information structure;
5. use cross-references;
6. adjust column count and whitespace;
7. adjust font size last.

## Layout

- Use cards or columns for independent reference items.
- Keep each card together when printing where possible.
- Use consistent heading, body, note, and limit styles.
- Avoid overly narrow columns that create excessive wrapping.
- Keep tables readable; do not force a wide matrix into a narrow mobile viewport.
- On small screens, prefer a single column or horizontally scrollable table with clear indication.
- Keep sticky toolbars compact and ensure they do not obscure anchored content.

## Print and PDF

- Provide a dedicated print stylesheet.
- Hide interactive controls in print.
- Use explicit page size and margins only when the intended paper format is known.
- Preserve borders, category cues, and contrast where the browser supports print-color adjustment.
- Test page breaks, column flow, clipping, and small text in the resulting PDF.
- Do not assume browser print output matches the screen exactly.

## HTML interaction

For interactive reference sheets:
- use semantic buttons and labels;
- expose selected state with `aria-pressed`;
- make keyboard activation available;
- provide visible focus;
- avoid clickable text that looks like plain decoration;
- persist user preferences only when useful and privacy-appropriate;
- keep the content understandable when JavaScript or local storage is unavailable.

## Dark mode

- define separate background, surface, text, muted, border, and accent tokens;
- check contrast independently in each theme;
- avoid assuming that a palette suitable on white works on dark surfaces;
- preserve chart labels and status symbols in both themes.

## Markdown and plain text

- prefer headings, lists, tables, code spans, and fenced code blocks;
- use Unicode symbols only when the target renderer supports them;
- use monospace alignment only when the output is rendered in a monospace context;
- do not depend on multiple spaces for alignment in proportional fonts;
- include a text equivalent for chart-only information.
