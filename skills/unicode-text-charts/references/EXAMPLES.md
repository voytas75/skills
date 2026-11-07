# Synthetic mapping fixtures

All inputs below are invented test data, not measurements.

## Sparkline

Input values: `0, 1, 2, 3, 4, 5, 6, 7`; units: arbitrary test units; eight successive samples, no calendar dates. Bounds: 0–7. Mapping: eight evenly spaced levels, nearest level.

```text
Samples  ▁▂▃▄▅▆▇█  final: 7
```

## Heatmap

Bands: `[0,25)` → `░`; `[25,50)` → `▒`; `[50,75)` → `▓`; `[75,100]` → `█`; missing → `?`.

```text
     A B C D
R1   ░ ▒ ▓ █
R2   ? ░ ▒ █
```

Exact values: R1 = `0,25,50,100`; R2 = `missing,10,40,80`. Scale: 0–100 test units.

## Tree

Explicit edges: Root→A, Root→B, A→File 1. Sibling order: A then B.

```text
Root
├── A
│   └── File 1
└── B
```

## Timeline

Events occur at hours 0, 2, and 4 from a supplied test origin. Each horizontal step represents one hour; labels below identify actual offsets.

```text
●─◆─●
0 2 4 h
```

Legend: `●` event; `◆` milestone. Exact event offsets remain authoritative.

## Gantt

Axis: four one-day cells numbered 0–3. Half-open intervals: A `[0,2)`, B `[2,4)`.

```text
Day  0123
A    ██..
B    ..██
```

Legend: `█` task active; `.` no task interval in that cell. This does not represent completion.

## Braille fixture, not a complete chart

One active upper-left dot (dot 1): `⠁` = U+2801. All eight dots: `⣿` = U+28FF. These validate character encoding only, not a signal, axes, plotting algorithm, or rendering quality.
