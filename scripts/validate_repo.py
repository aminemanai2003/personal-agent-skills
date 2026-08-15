#!/usr/bin/env python3
"""Validate skill packages and repository-level contracts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SOURCES = ROOT / "sources"
REQUIRED_SECTIONS = {
    "purpose",
    "inputs",
    "process",
    "constraints",
    "verification",
    "failure modes",
    "examples",
    "sources",
}


def parse_frontmatter(content: str) -> tuple[dict[str, object], str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data, match.group(2)


def headings(body: str) -> set[str]:
    return {
        match.group(1).strip().lower()
        for match in re.finditer(r"^##\s+(.+?)\s*$", body, re.MULTILINE)
    }


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return ["SKILL.md is missing"]

    content = skill_file.read_text(encoding="utf-8")
    if "[TODO" in content or re.search(r"\bTODO:\s", content):
        errors.append("contains a template TODO")

    try:
        frontmatter, body = parse_frontmatter(content)
    except (ValueError, yaml.YAMLError) as exc:
        return [str(exc)]

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if name != skill_dir.name:
        errors.append(f"frontmatter name {name!r} does not match directory")
    if not isinstance(description, str) or not description.strip():
        errors.append("description is missing")
    elif len(description) > 1024:
        errors.append("description exceeds 1024 characters")
    elif "use when" not in description.lower():
        errors.append("description does not state when to use the skill")

    missing = REQUIRED_SECTIONS - headings(body)
    if missing:
        errors.append("missing sections: " + ", ".join(sorted(missing)))

    source_file = SOURCES / f"{skill_dir.name}.sources.md"
    if not source_file.exists():
        errors.append(f"missing provenance file {source_file.relative_to(ROOT)}")

    agent_file = skill_dir / "agents" / "openai.yaml"
    if not agent_file.exists():
        errors.append("agents/openai.yaml is missing")
    elif "Help with" in agent_file.read_text(encoding="utf-8"):
        errors.append("agents/openai.yaml still has generated placeholder copy")

    return errors


def main() -> int:
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    failures: list[str] = []
    for skill_dir in skill_dirs:
        for error in validate_skill(skill_dir):
            failures.append(f"{skill_dir.name}: {error}")

    if failures:
        print("Repository validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validated {len(skill_dirs)} skill packages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
