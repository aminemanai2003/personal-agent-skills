---
name: github-workflow
description: Execute focused Git and GitHub work from repository orientation through commits, pull requests, review handling, checks, merge, and closure. Use when preparing or inspecting a branch, publishing changes, addressing PR feedback, fixing CI, or merging and closing GitHub work.
---

# GitHub Workflow

## Purpose

Move a change through GitHub with a reviewable history, verified state, and no accidental scope or authority expansion.

## Inputs

- Repository, issue or PR, target branch, and requested external action.
- Working tree status, branch history, remotes, checks, and review threads.
- Repository contribution, commit, and merge conventions.
- Credentials already configured in an approved tool; never request secrets in prose.

## Process

1. Inspect repository instructions, status, branch, remotes, and the relevant issue or PR state.
2. Define the change boundary and preserve unrelated work.
3. Make small commits whose messages explain one coherent change.
4. Verify locally in proportion to risk and review the staged diff before each commit.
5. Before publishing, confirm the destination branch/repository and scan for credentials or private artifacts.
6. Summarize behavior, reasoning, verification, compatibility, and limitations in the PR.
7. For review feedback, inspect unresolved thread context, implement valid fixes, verify, and resolve only addressed threads.
8. For CI failures, inspect the failing job and logs before changing code.
9. Merge or close only when requested or when the user has authorized that workflow; confirm checks, review state, and mergeability immediately beforehand.

## Constraints

- Do not overwrite or discard unrelated working-tree changes.
- Do not force-push, rewrite shared history, publish, merge, close, or message without applicable authority.
- Do not expose tokens in commands, logs, remotes, commits, or comments.
- Do not mark a thread resolved when the underlying issue remains.
- Do not merge around required failing checks unless the user explicitly owns and accepts that policy exception.

## Verification

- Each commit is scoped, understandable, and free of secrets.
- Local checks and GitHub checks cover the changed contract.
- PR description matches the actual diff and test evidence.
- Required review threads are resolved for valid reasons.
- Remote branch, merge result, or closed state is confirmed through current GitHub state.

## Failure Modes

- Trusting a stale PR page or check result.
- Fixing a symptom in CI without reading the failing log.
- Mixing generated files or unrelated formatting into a feature commit.
- Resolving a comment because code changed nearby.
- Using a credential pasted into chat when a configured authenticated client exists.

## Examples

**Granular branch:** commit the validator, each independent skill, evaluation cases, and documentation as separate reviewable units.

**Merge request:** refresh checks and review state, merge with the repository's policy, then verify the PR reports merged and the issue is closed if linked.

## Sources

See `../../sources/github-workflow.sources.md`.

