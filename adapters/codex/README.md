# Codex Adapter

Codex loads repository-local instructions from `AGENTS.md` and discovers skills from `.agents/skills`. Install the canonical packages with `python scripts/install_skills.py --target <project> --host codex`. Keep the canonical skill content in `skills/`; do not edit the installed copy directly.

Smoke check from a target project: inspect `.agents/skills/<name>/SKILL.md`, then start a normal Codex task whose wording matches the frontmatter description. The installer refuses to overwrite a locally modified package without `--force`.
