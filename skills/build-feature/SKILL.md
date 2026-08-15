---
name: build-feature
description: Implement a complete, repository-compatible feature from request through verification and handoff. Use when the user asks to add or change behavior across one or more files and expects the agent to carry the work through design, code, tests, and completion rather than only propose a plan.
---

# Build Feature

## Purpose

Deliver the requested behavior end to end with focused scope, repository sympathy, and evidence proportionate to the change.

## Inputs

- User outcome, acceptance criteria, constraints, and non-goals.
- Repository instructions, architecture, nearby patterns, tests, and commands.
- Affected public contracts, data, UI states, and external integrations.
- Current working-tree state and authorization boundary.

## Process

1. Orient: inspect instructions, status, relevant code, tests, and one comparable implementation.
2. Define: translate the request into observable outcomes, edge cases, and explicit non-goals.
3. Decide: resolve reversible technical details from evidence; escalate only material personal or irreversible choices.
4. Plan: identify the smallest coherent file and contract changes; expose a plan only when it helps coordination.
5. Implement: follow local patterns, preserve unrelated work, and keep each edit tied to an outcome.
6. Test: add behavior-focused coverage while implementing, not after the design has hardened.
7. Verify: run focused checks, broader checks for shared contracts, and direct UI/API inspection where applicable.
8. Critique: apply anti-slop and final-diff review; remove unnecessary abstractions, copy, decoration, and churn.
9. Handoff: lead with the result, list material verification, and state residual risk or skipped checks.

## Constraints

- Do not stop at a proposal when implementation is authorized and feasible.
- Do not expand into adjacent features or unrelated cleanup.
- Do not invent project conventions before searching for them.
- Do not treat a compiling implementation as a complete user workflow.
- Do not overwrite user changes or make irreversible external actions without authority.

## Verification

- Every acceptance criterion has observable evidence.
- Relevant edge and failure behavior is covered.
- Tests, types, lint, build, and runtime/UI checks pass where applicable.
- Shared contracts remain compatible or include an explicit migration.
- The final diff is focused, documented where needed, and free of secrets or placeholders.

## Failure Modes

- Coding from the prompt without reading the repository.
- Building an abstraction for hypothetical future variants.
- Adding tests that only confirm the chosen implementation.
- Completing backend logic while leaving UI loading/error states broken.
- Reporting success before rerunning checks after the final edit.

## Examples

**Narrow API feature:** update route, domain logic, validation, contract tests, and docs; avoid reorganizing unrelated modules.

**Frontend workflow:** implement the complete action including pending, success, validation, access, and server-error states, then inspect desktop and mobile behavior.

## Sources

See `../../sources/build-feature.sources.md`.

