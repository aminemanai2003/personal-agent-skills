---
name: code-quality
description: Guide implementation and refactoring toward correct, readable, compatible, secure, and maintainable code. Use when writing production code, changing shared behavior, evaluating dependencies, modifying APIs or schemas, or cleaning up implementation structure.
---

# Code Quality

## Purpose

Produce code that fits the existing system, makes behavior explicit, and remains easy to verify and change.

## Inputs

- The behavioral contract and acceptance criteria.
- Repository instructions, nearby implementation patterns, tests, and public types.
- Data, security, performance, and compatibility boundaries.
- Available commands for tests, linting, typing, builds, and formatting.

## Scope Boundary

This skill governs implementation and refactoring. For a review-only request, use `review-code`; for a complete authorized feature, compose this skill through `build-feature`.

## Process

1. Read the files to change, their tests, and one comparable implementation.
2. Identify ownership boundaries and public contracts before designing the change.
3. Choose the smallest coherent implementation that matches established patterns.
4. Make invalid states difficult to represent with types, validation, and explicit errors where justified.
5. Keep orchestration separate from domain logic when their concerns diverge.
6. Add or update behavior-focused tests, including relevant edge and failure cases.
7. Run targeted checks, then broader checks proportional to shared impact.
8. Review the diff for duplication, dead paths, hidden coupling, secrets, and unnecessary dependencies.

## Constraints

- Do not refactor unrelated code during feature work.
- Do not add an abstraction until it removes real complexity or matches a local pattern.
- Do not add a dependency for a trivial convenience; use a proven library for complex domain behavior.
- Do not silently break public APIs, schemas, persisted data, or configuration.
- Do not optimize without a requirement or measurement when it reduces clarity.

## Verification

- Tests exercise observable behavior and would catch the intended regression.
- Type, lint, build, and focused test checks pass where available.
- Error and boundary behavior is explicit.
- Public contract changes include compatibility handling and documentation.
- The final diff is focused and understandable without a verbal walkthrough.

## Failure Modes

- Copying a nearby pattern that is itself obsolete or unrelated.
- Hiding complexity behind generic helpers or pass-through wrappers.
- Tests that mirror implementation details but miss user behavior.
- Catch-all error handling that destroys useful context.
- Large mixed commits combining cleanup, migration, and feature behavior.

## Examples

**Parser:** use a maintained structured parser for a real grammar; validate at the boundary and test malformed inputs.

**Shared API:** preserve old callers or introduce an explicit migration with compatibility tests and documentation.

## Sources

See `../../sources/code-quality.sources.md`.
