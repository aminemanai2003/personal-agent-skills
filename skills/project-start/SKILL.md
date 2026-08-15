---
name: project-start
description: Orient an agent to a new or unfamiliar repository and establish a focused execution context before substantial work. Use when starting a project, entering an existing codebase, planning the first feature, creating repository instructions, or when output quality suggests missing project context.
---

# Project Start

## Purpose

Build the smallest reliable project map needed to make correct early decisions without loading the entire repository or inventing conventions.

## Inputs

- User outcome, repository path, current branch/status, and authorization boundary.
- Root instructions, README, manifests, configuration, CI, and architecture docs.
- Relevant source, test, schema, and deployment entry points.
- Existing issue/spec and known constraints.

## Scope Boundary

Use this for orientation before substantial work. Skip it for a narrow task when the relevant files, command, and contract are already known.

## Process

1. Inspect repository status and locate instruction files without modifying anything.
2. Read root documentation, manifests, commands, CI, and the directory structure.
3. Identify languages, frameworks, package boundaries, entry points, tests, generated code, and public contracts.
4. Trace one representative workflow related to the user's next task.
5. Record a compact project map: purpose, architecture, commands, conventions, boundaries, risks, and unresolved questions.
6. Separate evidence from inference; verify commands rather than assuming common defaults.
7. Define the first scoped outcome and non-goals.
8. Add or update project instructions only when requested or when they are a normal deliverable of project setup; keep them concise and repository-specific.
9. Choose the next workflow skill based on the task, not the category list.

## Constraints

- Do not read every file before useful work can begin.
- Do not create a new architecture when the repository already has one.
- Do not run destructive setup, migrations, deployments, or dependency upgrades during orientation.
- Do not paste secrets or local environment values into project context.
- Do not create generic rules files that repeat platform behavior.

## Verification

- The project map cites real files and verified commands.
- The relevant workflow and ownership boundary are understood.
- Generated, vendor, secret, and user-owned files are identified before edits.
- The first outcome is testable and narrow enough to review.
- Remaining unknowns are genuinely material rather than discoverable routine facts.

## Failure Modes

- Starting implementation from the README alone.
- Loading so much context that the current task becomes unclear.
- Assuming package-manager, test, or deployment commands.
- Writing a generic `AGENTS.md` that conflicts with local conventions.
- Treating an inferred architecture diagram as authoritative.

## Examples

**Existing monorepo:** identify package ownership, shared contracts, affected tests, and the command for the target workspace before editing.

**New project:** define audience, V1 outcome, non-goals, technical constraints, verification path, and a small initial structure before scaffolding.

## Sources

See `../../sources/project-start.sources.md`.
