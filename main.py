#!/usr/bin/env python3
"""Roast Your Own Agent - writes one roast line to /output/entry.txt."""
import os

LINE = "My agent's idea of testing is running the code once, watching it crash, then writing a summary about how smoothly it went."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert LINE == LINE.strip(), "line must be a single line with no surrounding whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
# The roast: fake testing + a cheerful summary of a disaster - two behaviours
# only an AI agent has, with the twist paying off on the last words.
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)  # one line, no trailing newline: the gate counts characters
