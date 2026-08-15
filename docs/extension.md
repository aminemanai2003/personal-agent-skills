# Extending The System

## Add a skill

1. Confirm the workflow is meaningfully reusable and not already owned by an existing skill.
2. Use the host's skill initializer when available, or create the standard package manually (`skills/<name>/SKILL.md` plus only the resources it needs).
3. Write a concise frontmatter description that says what the skill does and when to trigger it.
4. Include Purpose, Inputs, Process, Constraints, Verification, Failure Modes, Examples, and Sources sections.
5. Add original implementation notes and external inspiration to `sources/<name>.sources.md`.
6. Add at least two positive and one near-miss case to `evals/evals.json`.
7. Update `architecture/skill-dependencies.md` only when a real behavioral edge exists.
8. Run repository and evaluation validators, inspect the diff, and commit the skill separately.

## Change a skill

Preserve the trigger boundary unless the evaluation cases demonstrate a problem. Change the smallest layer that fixes the failure: description for triggering, body for process, reference for detail, or adapter for host behavior.

## Personalize

Put a direct preference in `personal/operating-profile.md` only after it is confirmed or clearly labeled as inferred. Do not duplicate profile rules into every skill.

## Provenance

Record the repository, URL, maintainer, adoption/activity signal, license signal, useful principles, adaptation boundary, conflicts, and personal additions. Re-express concepts in original language; do not copy third-party skill bodies or assets wholesale.
