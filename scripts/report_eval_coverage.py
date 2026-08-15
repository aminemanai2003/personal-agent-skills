#!/usr/bin/env python3
"""Print deterministic positive and near-miss evaluation coverage by skill."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    data = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
    positive: Counter[str] = Counter()
    negative: Counter[str] = Counter()
    for case in data["cases"]:
        positive.update(case["expected_skills"])
        negative.update(case["forbidden_skills"])

    print("| Skill | Positive | Near-miss |")
    print("| --- | ---: | ---: |")
    for skill in sorted(path.name for path in (ROOT / "skills").iterdir() if path.is_dir()):
        print(f"| {skill} | {positive[skill]} | {negative[skill]} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

