# Claude Code Adapter

The portable source of truth is the `skills/` directory. Load a skill when its frontmatter description matches the task, then follow its process and verification sections.

Project-level preferences live in `personal/operating-profile.md`; do not duplicate them into every skill. Tool-specific invocation and packaging notes live under `adapters/claude-code/`.

