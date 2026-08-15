# Personal Agent Skills

A private, portable skills system for Amine's coding and research agents.

The repository combines reusable workflow knowledge with a small set of personal preferences. The goal is not to make an agent imitate a person mechanically. It is to make good professional judgment more consistent while preserving the ability to challenge weak assumptions.

## Design principles

- Evidence before completion claims.
- Inspect the repository and existing patterns before editing.
- Prefer small, composable workflows over a large instruction dump.
- Keep the shared skill core portable; put tool-specific behavior in adapters.
- Distinguish objective engineering quality from personal taste.
- Record provenance and adapt principles rather than copying external text.
- Make uncertainty, limitations, and unresolved decisions visible.

## Layout

```text
personal/       confirmed and inferred operating preferences
research/       ecosystem map and research notes
core/           cross-cutting quality and anti-slop rules
architecture/   dependencies, precedence, and composition rules
skills/         portable SKILL.md packages
sources/        provenance notes for composite skills
adapters/       Codex and Claude Code integration notes
evals/          realistic scenarios and evaluation records
decisions/      short architecture decision records
scripts/        deterministic validation helpers
```

## V1 Skill Catalog

- `personal-operating-profile`: apply confirmed and inferred preferences with precedence.
- `anti-slop`: remove generic, unjustified, and unfinished output.
- `decision-making`: choose defensible options under incomplete information.
- `definition-of-done`: match completion claims to direct evidence.
- `frontend-design`: create domain-specific interface directions.
- `visual-ux-review`: inspect rendered UI evidence and states.
- `code-quality`: implement and refactor compatible code.
- `research-quality`: calibrate claims to credible, reproducible evidence.
- `personal-writing`: write concise, factual project communication.
- `github-workflow`: move focused work through GitHub safely.
- `build-feature`: carry an authorized feature through implementation and handoff.
- `review-code`: report concrete code defects and regression risk.
- `review-ui`: orchestrate complete UI readiness reviews and focused fixes.
- `research-topic`: investigate a question through decision-ready synthesis.
- `project-start`: orient to an unfamiliar repository before substantial work.

## Install

The canonical source is `skills/`. Install the packages into a target project for both hosts:

```powershell
python scripts/install_skills.py --target C:\path\to\project --host both
```

Use `--host codex` or `--host claude` for one host. The installer is idempotent and refuses to overwrite a changed installed skill unless `--force` is supplied.

Codex discovers the installed packages from `.agents/skills`. Claude Code uses `.claude/skills`; host-specific notes are in `adapters/`.

## Use and extend

Read `personal/operating-profile.md` and `core/definition-of-done.md` before extending the system. Read only the relevant skill and referenced material for a task.

To add a skill, use the standard package shape (`SKILL.md`, optional `references/`, `scripts/`, or `assets/`) and add a provenance file under `sources/`. Keep the description trigger-specific, add positive and near-miss cases to `evals/evals.json`, then run:

```powershell
.\.venv\Scripts\python.exe scripts/validate_repo.py
.\.venv\Scripts\python.exe scripts/validate_evals.py
```

The repository uses small commits so each skill or support concern can be reviewed independently. See `docs/extension.md` and `CONTRIBUTING.md` for the full workflow.

## Rule precedence

1. System and platform safety rules.
2. Explicit user instructions for the current task.
3. Repository and project rules discovered in `AGENTS.md`, `CLAUDE.md`, and equivalent files.
4. Objective engineering quality and applicable standards.
5. This repository's personal preferences.
6. A skill's local defaults.

When rules conflict, preserve the higher-precedence rule, state the conflict briefly, and choose the smallest change that satisfies the task.

## Status

This repository is usable as a V1 system. The operating profile is evidence-backed but still provisional where the interview worksheet has unanswered personal choices. The deterministic evaluation suite passes; independent repeated model-run variance benchmarks remain a future improvement.
