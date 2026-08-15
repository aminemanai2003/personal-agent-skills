from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install_skills.py"
SPEC = importlib.util.spec_from_file_location("install_skills", SCRIPT)
assert SPEC and SPEC.loader
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)


class InstallSkillsTests(unittest.TestCase):
    def make_source(self, root: Path) -> Path:
        source = root / "source" / "example-skill"
        (source / "references").mkdir(parents=True)
        (source / "SKILL.md").write_text("skill-v1\n", encoding="utf-8")
        (source / "references" / "guide.md").write_text("guide\n", encoding="utf-8")
        return source

    def test_install_and_idempotent_reinstall(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = self.make_source(root)
            destination = root / "target"

            self.assertEqual(INSTALLER.install_skill(source, destination, False), "installed")
            self.assertEqual(INSTALLER.install_skill(source, destination, False), "unchanged")

    def test_refuses_to_overwrite_modified_install(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = self.make_source(root)
            destination = root / "target"
            INSTALLER.install_skill(source, destination, False)
            installed_file = destination / source.name / "SKILL.md"
            installed_file.write_text("local-change\n", encoding="utf-8")

            with self.assertRaises(FileExistsError):
                INSTALLER.install_skill(source, destination, False)

    def test_force_replaces_modified_install(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = self.make_source(root)
            destination = root / "target"
            INSTALLER.install_skill(source, destination, False)
            installed_file = destination / source.name / "SKILL.md"
            installed_file.write_text("local-change\n", encoding="utf-8")

            self.assertEqual(INSTALLER.install_skill(source, destination, True), "installed")
            self.assertEqual(installed_file.read_text(encoding="utf-8"), "skill-v1\n")


if __name__ == "__main__":
    unittest.main()

