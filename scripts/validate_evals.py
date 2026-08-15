#!/usr/bin/env python3
"""Validate evaluation coverage and trigger-boundary cases."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVAL_FILE = ROOT / "evals" / "evals.json"
SKILL_NAMES = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
REQUIRED_FIELDS = {
    "id",
    "prompt",
    "expected_skills",
    "forbidden_skills",
    "expected_behavior",
}


def main() -> int:
    if not EVAL_FILE.exists():
        print(f"Missing {EVAL_FILE.relative_to(ROOT)}")
        return 1

    data = json.loads(EVAL_FILE.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    errors: list[str] = []
    ids: set[str] = set()
    positive = Counter()
    negative = Counter()

    for index, case in enumerate(cases):
        label = case.get("id", f"case-{index}")
        missing = REQUIRED_FIELDS - set(case)
        if missing:
            errors.append(f"{label}: missing fields {', '.join(sorted(missing))}")
            continue
        if label in ids:
            errors.append(f"{label}: duplicate id")
        ids.add(label)
        if not case["prompt"].strip() or not case["expected_behavior"].strip():
            errors.append(f"{label}: prompt and expected behavior must be non-empty")
        expected = set(case["expected_skills"])
        forbidden = set(case["forbidden_skills"])
        unknown = (expected | forbidden) - SKILL_NAMES
        if unknown:
            errors.append(f"{label}: unknown skills {', '.join(sorted(unknown))}")
        overlap = expected & forbidden
        if overlap:
            errors.append(f"{label}: skills both expected and forbidden {', '.join(sorted(overlap))}")
        positive.update(expected)
        negative.update(forbidden)

    for skill in sorted(SKILL_NAMES):
        if positive[skill] < 2:
            errors.append(f"{skill}: needs at least two positive cases")
        if negative[skill] < 1:
            errors.append(f"{skill}: needs at least one near-miss/negative case")

    if errors:
        print("Evaluation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(cases)} cases across {len(SKILL_NAMES)} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

