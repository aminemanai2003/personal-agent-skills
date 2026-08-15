#!/usr/bin/env python3
"""Install canonical skill packages into Codex and Claude Code projects."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "skills"
HOST_PATHS = {
    "codex": Path(".agents") / "skills",
    "claude": Path(".claude") / "skills",
}


def directories_equal(left: Path, right: Path) -> bool:
    comparison = filecmp.dircmp(left, right)
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    if any(not filecmp.cmp(left / name, right / name, shallow=False) for name in comparison.common_files):
        return False
    return all(directories_equal(left / name, right / name) for name in comparison.common_dirs)


def selected_skills(names: list[str] | None) -> list[Path]:
    available = {path.name: path for path in SOURCE_ROOT.iterdir() if path.is_dir()}
    if not names:
        return [available[name] for name in sorted(available)]
    missing = sorted(set(names) - set(available))
    if missing:
        raise ValueError("unknown skills: " + ", ".join(missing))
    return [available[name] for name in names]


def install_skill(source: Path, destination_root: Path, force: bool) -> str:
    destination = destination_root / source.name
    if destination.exists():
        if directories_equal(source, destination):
            return "unchanged"
        if not force:
            raise FileExistsError(
                f"{destination} differs from the canonical skill; use --force to replace it"
            )
        shutil.rmtree(destination)
    destination_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return "installed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target",
        type=Path,
        default=ROOT,
        help="Project directory to receive host skill folders (default: this repository)",
    )
    parser.add_argument(
        "--host",
        choices=("codex", "claude", "both"),
        default="both",
        help="Host integration to install",
    )
    parser.add_argument(
        "--skill",
        action="append",
        dest="skills",
        help="Install one named skill; repeat for multiple skills",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an installed skill that differs from the canonical package",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.target.resolve()
    if not target.exists() or not target.is_dir():
        print(f"Target directory does not exist: {target}", file=sys.stderr)
        return 2

    try:
        skills = selected_skills(args.skills)
        hosts = tuple(HOST_PATHS) if args.host == "both" else (args.host,)
        for host in hosts:
            destination_root = target / HOST_PATHS[host]
            for source in skills:
                status = install_skill(source, destination_root, args.force)
                print(f"{host}: {source.name}: {status}")
    except (ValueError, FileExistsError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

