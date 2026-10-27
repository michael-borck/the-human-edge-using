#!/usr/bin/env python3
"""Local manuscript checks for The Human Edge: Using AI with Judgement.

Checks: configured files exist, exactly one H1 per chapter or appendix,
no em-dashes (house style), no leftover course-site markup, word counts.
Does not certify factual accuracy, links, or print layout.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: uv pip install pyyaml")

BOOK = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((BOOK / "_quarto.yml").read_text(encoding="utf-8"))


def configured_files(entries):
    result = []
    for entry in entries or []:
        if isinstance(entry, str):
            result.append(entry)
        elif isinstance(entry, dict):
            result.extend(configured_files(entry.get("chapters")))
    return result


def main():
    book = CONFIG.get("book", {})
    files = configured_files(book.get("chapters")) + configured_files(book.get("appendices"))
    errors = []
    total_words = 0
    for name in files:
        path = BOOK / name
        if not path.exists():
            errors.append(f"missing configured file: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        words = len(text.split())
        total_words += words
        h1 = len(re.findall(r"^# ", text, flags=re.M))
        if name not in ("index.qmd",) and h1 != 1:
            errors.append(f"{name}: expected exactly one H1, found {h1}")
        for marker, label in [("—", "em-dash"), ("::: kicker", "site kicker div"),
                              ("{=html}", "raw html block"), ("nav-home", "site frontmatter")]:
            if marker in text:
                errors.append(f"{name}: leftover {label} ({marker!r})")
        print(f"{name:45} {words:6} words")
    print(f"{'TOTAL':45} {total_words:6} words")
    if errors:
        print("\nERRORS:")
        for message in errors:
            print(f"  {message}")
        return 1
    print("\nAll manuscript checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
