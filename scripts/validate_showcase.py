#!/usr/bin/env python3
"""Validate stored showcase artifacts and the claims made from them."""

from __future__ import annotations

import re
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "evals" / "showcase" / "outputs"
COMPARISONS = ROOT / "docs" / "assets" / "comparisons"
SOURCE_PACK = ROOT / "evals" / "showcase" / "research" / "source-pack.md"

IMAGE_PAIRS = (
    ("ui-before.png", "ui-after.png", "desktop"),
    ("ui-before-mobile.png", "ui-after-mobile.png", "mobile"),
)

EXPECTED_WORD_COUNTS = {
    "writing-before.md": 331,
    "writing-after.md": 320,
    "research-before.md": 1482,
    "research-after.md": 1438,
}

DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)


def png_size(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("not a valid PNG with an IHDR header")
    return struct.unpack(">II", header[16:24])


def word_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def doi_set(path: Path) -> set[str]:
    return {
        match.group(0).rstrip(".,;:)]}").lower()
        for match in DOI_PATTERN.finditer(path.read_text(encoding="utf-8"))
    }


def main() -> int:
    errors: list[str] = []

    for left_name, right_name, label in IMAGE_PAIRS:
        sizes: list[tuple[str, tuple[int, int]]] = []
        for name in (left_name, right_name):
            path = OUTPUTS / name
            if not path.exists():
                errors.append(f"missing {path.relative_to(ROOT)}")
                continue
            try:
                sizes.append((name, png_size(path)))
            except ValueError as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
        if len(sizes) == 2 and sizes[0][1] != sizes[1][1]:
            errors.append(
                f"{label} showcase images are not comparable: "
                f"{sizes[0][0]} is {sizes[0][1][0]}x{sizes[0][1][1]}, "
                f"{sizes[1][0]} is {sizes[1][1][0]}x{sizes[1][1][1]}"
            )

    for name in ("ui-before-after.png", "ui-mobile-before-after.png"):
        path = COMPARISONS / name
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
        else:
            try:
                png_size(path)
            except ValueError as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")

    for name, expected in EXPECTED_WORD_COUNTS.items():
        path = OUTPUTS / name
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
            continue
        actual = word_count(path)
        if actual != expected:
            errors.append(f"{path.relative_to(ROOT)}: expected {expected} words, found {actual}")

    if SOURCE_PACK.exists():
        expected_dois = doi_set(SOURCE_PACK)
        for name in ("research-before.md", "research-after.md"):
            path = OUTPUTS / name
            if path.exists() and doi_set(path) != expected_dois:
                errors.append(f"{path.relative_to(ROOT)}: DOI set does not match the controlled source pack")
    else:
        errors.append(f"missing {SOURCE_PACK.relative_to(ROOT)}")

    if errors:
        print("Showcase validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validated showcase images, word counts, and DOI coverage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
