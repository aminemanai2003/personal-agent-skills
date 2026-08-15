# ADR 0001: Portable Skill Core

Status: accepted

## Decision

Store the canonical workflow and knowledge in portable `skills/<name>/SKILL.md` packages. Keep Codex and Claude Code integration as thin adapters.

## Rationale

The two hosts differ in discovery and packaging, but duplicating the workflow would create drift. A shared core preserves one reviewable source of truth while allowing small host-specific instructions.

## Consequences

- Skills must avoid host-specific assumptions in their main process.
- Adapters may describe discovery, tool names, and packaging only.
- Framework-specific detail belongs in referenced files with clear triggers.

## Alternatives rejected

- Host-specific copies of every skill: higher drift and maintenance cost.
- One global instruction file: poor triggering and excessive context.

