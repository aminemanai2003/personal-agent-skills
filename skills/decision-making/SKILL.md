---
name: decision-making
description: Make and document consequential engineering or product choices under incomplete information. Use when multiple reasonable approaches materially differ, constraints conflict, a dependency or architecture choice is needed, or the agent must decide whether to ask or proceed.
---

# Decision Making

## Purpose

Reach a defensible decision quickly enough to preserve momentum while exposing assumptions, costs, and reversibility.

## Inputs

- The decision to make and the deadline or urgency.
- Hard constraints, authorization boundaries, and success criteria.
- Repository evidence and comparable existing patterns.
- Options that are genuinely viable, including doing nothing.

## Process

1. Write the decision as a question with a concrete outcome.
2. Separate hard constraints from preferences and guesses.
3. Inspect existing decisions, code patterns, measurements, and standards before generating options.
4. Keep two or three materially distinct options; remove dominated or out-of-scope choices.
5. Compare correctness, compatibility, maintenance cost, reversibility, performance evidence, and delivery cost.
6. Prefer the smallest reversible choice that satisfies the outcome unless evidence justifies a larger commitment.
7. Ask the user only if the remaining difference is personal, irreversible, or outside current authority.
8. Record material decisions with context, choice, rationale, consequences, and revisit signal.

## Constraints

- Do not manufacture options merely to appear balanced.
- Do not use a numeric score when weights are subjective or unsupported.
- Do not let sunk cost decide an architecture choice.
- Do not treat popularity as proof of local fit.
- Do not hide a personal preference inside an objective-quality argument.

## Verification

- The chosen option satisfies every hard constraint.
- Rejected options and their decisive tradeoffs are understandable.
- Assumptions are testable or explicitly accepted.
- The decision has a rollback or revisit condition when uncertainty is material.
- The decision did not require authority that was never granted.

## Failure Modes

- Analysis paralysis over a reversible choice.
- Premature commitment before reading the repository.
- A dependency chosen because it is familiar rather than necessary.
- A vague “best practice” rationale with no project evidence.
- Asking the user a question that inspection or experimentation could answer.

## Examples

**Dependency:** choose the proven parser when hand-written parsing would own a complex grammar; record bundle/maintenance cost.

**Architecture:** follow the existing module boundary for a narrow feature; create an ADR only if the public contract or ownership changes.

## Sources

See `../../sources/decision-making.sources.md`.

