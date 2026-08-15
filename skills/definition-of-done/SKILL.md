---
name: definition-of-done
description: Select and enforce proportional completion evidence for code, UI, research, documentation, and GitHub work. Use when preparing to claim completion, hand work off, merge, publish, or decide whether verification is sufficient.
---

# Definition Of Done

## Purpose

Turn "finished" into an evidence-backed claim matched to the task's actual blast radius.

## Inputs

- The requested behavior and acceptance criteria.
- Changed files, public contracts, and affected workflows.
- Available test, build, lint, type, browser, security, and data checks.
- Constraints that prevented any expected verification.

## Process

1. Translate the request into observable outcomes.
2. Identify the affected contracts: code, UI, API/schema, data, research claims, docs, or external state.
3. Choose the smallest verification set that covers those contracts and important failure paths.
4. Run focused checks early; run broader regression checks when shared behavior or public contracts changed.
5. Inspect the final diff and user-visible result, not only command exit codes.
6. Compare current evidence against every acceptance criterion.
7. Fix high-value gaps and repeat checks after the final change.
8. Report what passed, what was not run, and any remaining risk.

## Constraints

- Do not require irrelevant checks for a narrow documentation change.
- Do not use one passing unit test to support a system-wide claim.
- Do not treat automated accessibility or security tools as complete proof.
- Do not declare success while required sessions, deployments, or checks are still running.
- Do not hide skipped verification behind "should work" language.

## Verification

- Every requested outcome has direct evidence.
- Relevant edge, error, and compatibility paths were considered.
- Checks were rerun after the last material edit.
- The diff contains no secrets, placeholders, unrelated churn, or accidental artifacts.
- The final report accurately distinguishes verified behavior from residual risk.

## Failure Modes

- Stopping after the first green command.
- Testing implementation details while missing the user workflow.
- Running a broad suite that does not exercise the changed contract.
- Forgetting visual inspection after layout changes.
- Claiming research certainty from a plausible narrative without source support.

## Examples

**API schema change:** contract tests, compatibility behavior, generated clients if applicable, documentation, and final diff review.

**Small copy edit:** targeted render or preview plus spelling/context review; no unrelated full performance benchmark.

## Sources

See `../../sources/definition-of-done.sources.md`.
