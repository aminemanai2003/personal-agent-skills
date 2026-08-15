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

## Using the repository

Codex discovers repository-local skills from `.agents/skills`. During packaging, the canonical skills in `skills/` are mirrored or linked into that location without changing their content. Claude Code can use the same `SKILL.md` files through its project skill/plugin conventions; the thin adapters document any differences.

Read `personal/operating-profile.md` and `core/definition-of-done.md` before extending the system. Read only the relevant skill and referenced material for a task.

## Rule precedence

1. System and platform safety rules.
2. Explicit user instructions for the current task.
3. Repository and project rules discovered in `AGENTS.md`, `CLAUDE.md`, and equivalent files.
4. Objective engineering quality and applicable standards.
5. This repository's personal preferences.
6. A skill's local defaults.

When rules conflict, preserve the higher-precedence rule, state the conflict briefly, and choose the smallest change that satisfies the task.

## Status

This repository is being built iteratively. Research and architecture are established first; the operating profile and skills are added after the personalization interview and evaluated against realistic tasks.

