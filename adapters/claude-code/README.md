# Claude Code Adapter

Claude Code can consume the same portable `SKILL.md` packages through `.claude/skills` or plugin packaging. Install with `python scripts/install_skills.py --target <project> --host claude`. Keep host-specific discovery and packaging details here; do not duplicate methodology in adapter files.

The canonical source remains `skills/`. After installation, invoke a task matching the skill description and verify that the host loads only the relevant package and references.
