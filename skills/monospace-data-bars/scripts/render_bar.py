#!/usr/bin/env python3
"""Render validated monospace data bars from JSON input."""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

VARIANTS = {"auto", "block", "ascii", "thin", "dots", "status", "delta", "threshold", "inline", "table"}
GLYPHS = {
    "block": ("█", "░"),
    "ascii": ("#", "."),
    "thin": ("━", "─"),
    "dots": ("●", "○"),
}


class InputError(ValueError):
    pass


def number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(f"{field} must be a number")
    result = float(value)
    if not math.isfinite(result):
        raise InputError(f"{field} must be finite")
    return result


def display_number(value: float | int) -> str:
    if isinstance(value, int):
        return str(value)
    if float(value).is_integer():
        return str(int(value))
    return format(value, ".12g")


def validate(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise InputError("input must be a JSON object")
    variant = data.get("variant", "block")
    if variant not in VARIANTS:
        raise InputError(f"variant must be one of: {', '.join(sorted(VARIANTS))}")
    if variant == "auto":
        variant = "block"
    width = data.get("width", 12)
    if isinstance(width, bool) or not isinstance(width, int) or not 1 <= width <= 80:
        raise InputError("width must be an integer from 1 to 80")
    unit = data.get("unit", "")
    if not isinstance(unit, str):
        raise InputError("unit must be a string")
    if unit != "%" and ("min" not in data or "max" not in data):
        raise InputError("non-percentage data requires explicit min and max scale bounds")
    low = number(data.get("min", 0), "min")
    high = number(data.get("max", 100), "max")
    if high <= low:
        raise InputError("max must be greater than min")
    fmt = data.get("format", "unicode")
    if fmt not in {"unicode", "ascii"}:
        raise InputError("format must be 'unicode' or 'ascii'")
    items = data.get("items")
    if not isinstance(items, list) or not items:
        raise InputError("items must be a non-empty array")
    clean = []
    global_threshold = data.get("threshold")
    if global_threshold is not None:
        global_threshold = number(global_threshold, "threshold")
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise InputError(f"items[{index}] must be an object")
        label = item.get("label")
        if not isinstance(label, str) or not label.strip():
            raise InputError(f"items[{index}].label must be a non-empty string")
        value = number(item.get("value"), f"items[{index}].value")
        if not low <= value <= high:
            raise InputError(f"items[{index}].value={display_number(value)} outside scale [{display_number(low)}, {display_number(high)}]")
        row = {"label": label, "value": value}
        if "status" in item:
            if not isinstance(item["status"], str) or not item["status"].strip():
                raise InputError(f"items[{index}].status must be a non-empty string")
            row["status"] = item["status"].strip()
        if "previous" in item:
            previous = number(item["previous"], f"items[{index}].previous")
            if not low <= previous <= high:
                raise InputError(f"items[{index}].previous outside scale [{display_number(low)}, {display_number(high)}]")
            row["previous"] = previous
        if "period" in item:
            if not isinstance(item["period"], str):
                raise InputError(f"items[{index}].period must be a string")
            row["period"] = item["period"]
        threshold = item.get("threshold", global_threshold)
        if threshold is not None:
            threshold = number(threshold, f"items[{index}].threshold")
            if not low <= threshold <= high:
                raise InputError(f"items[{index}].threshold outside scale [{display_number(low)}, {display_number(high)}]")
            row["threshold"] = threshold
        clean.append(row)
    if variant == "status" and any("status" not in row for row in clean):
        raise InputError("variant 'status' requires status for every item")
    if variant == "delta" and any("previous" not in row for row in clean):
        raise InputError("variant 'delta' requires previous for every item")
    if variant == "threshold" and any("threshold" not in row for row in clean):
        raise InputError("variant 'threshold' requires threshold for every item or a top-level threshold")
    return {"variant": variant, "width": width, "min": low, "max": high, "unit": unit,
            "format": fmt, "items": clean}


def cells(value: float, low: float, high: float, width: int) -> int:
    return int(math.floor(((value - low) / (high - low)) * width + 0.5))


def bar(value: float, low: float, high: float, width: int, filled: str, empty: str) -> str:
    count = cells(value, low, high, width)
    return filled * count + empty * (width - count)


def render(raw: Any) -> str:
    data = validate(raw)
    variant, width = data["variant"], data["width"]
    low, high, unit = data["min"], data["max"], data["unit"]
    items = data["items"]
    if data["format"] == "ascii" or variant == "ascii":
        filled, empty = "#", "."
    elif variant in GLYPHS:
        filled, empty = GLYPHS[variant]
    else:
        filled, empty = "█", "░"

    label_width = max(len(row["label"]) for row in items)

    def make_bar(row: dict[str, Any]) -> str:
        return bar(row["value"], low, high, width, filled, empty)

    def value_text(row: dict[str, Any]) -> str:
        return display_number(row["value"]) + unit

    lines: list[str] = []
    if variant == "inline":
        parts = [f'{r["label"]} {make_bar(r)} {value_text(r)}' for r in items]
        return " │ ".join(parts)
    if variant == "table":
        has_status = all("status" in r for r in items)
        header = f'{"RESOURCE":<{label_width}}  {"BAR":<{width}}  VALUE'
        if has_status:
            header += "  STATUS"
        lines.append(header)
        for r in items:
            line = f'{r["label"]:<{label_width}}  {make_bar(r)}  {value_text(r)}'
            if has_status:
                line += f'  {r["status"]}'
            lines.append(line)
        return "\n".join(lines)
    for row in items:
        line = f'{row["label"]:<{label_width}}  {make_bar(row)}  {value_text(row)}'
        if variant == "status":
            line += f'  {row["status"]}'
        elif variant == "delta":
            delta = row["value"] - row["previous"]
            delta_unit = " pp" if unit == "%" else (f" {unit}" if unit else "")
            sign = "+" if delta > 0 else ""
            line += f'  {sign}{display_number(delta)}{delta_unit}'
            if row.get("period"):
                line += f' vs {row["period"]}'
        elif variant == "threshold":
            pos = cells(row["threshold"], low, high, width)
            # Insert marker at the cell boundary; the value bar remains unchanged.
            chars = list(make_bar(row))
            chars.insert(min(pos, len(chars)), "│")
            line = f'{row["label"]:<{label_width}}  {"".join(chars)}  {value_text(row)} (target {display_number(row["threshold"])}{unit})'
        lines.append(line)
    if variant == "threshold":
        lines.insert(0, f'Scale: {display_number(low)}–{display_number(high)}{unit}; │ = threshold')
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON file path, or - for stdin")
    args = parser.parse_args()
    try:
        raw_text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
        data = json.loads(raw_text)
        print(render(data))
        return 0
    except (OSError, json.JSONDecodeError, InputError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
