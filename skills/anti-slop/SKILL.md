---
name: anti-slop
description: Detect and remove generic, unjustified, inflated, or unfinished work across code, UI, prose, research, and agent behavior. Use when creating or reviewing substantial output, when a result feels templated, or before declaring a user-facing task complete.
---

# Anti-Slop

## Purpose

Raise specificity and usefulness by removing choices that are present because they are common defaults rather than because they serve the task.

## Inputs

- The user's actual outcome and audience.
- Repository conventions, domain constraints, and existing content.
- The draft implementation or output.
- Verification evidence already collected.

## Scope Boundary

Use this as a cross-cutting critique pass. It does not replace a domain review or implementation workflow; pair it with the skill that owns the code, UI, research, or writing task.

## Process

1. Restate the output's job in one concrete sentence.
2. Identify elements that do not help that job: abstractions, decoration, claims, sections, dependencies, or process steps.
3. Check for generic substitutions where project-specific evidence exists.
4. Check for hidden incompleteness: placeholder content, untested paths, missing states, vague citations, or completion claims based on one command.
5. Remove unnecessary elements before adding compensating explanation.
6. Replace remaining generic choices with domain-specific ones supported by the brief or repository.
7. Re-run the checks that prove the user-visible contract.

## Constraints

- Do not equate minimalism with quality; necessary complexity should remain.
- Do not erase an established brand or project convention merely because it is common.
- Do not turn this skill into a universal checklist that blocks trivial work.
- Do not criticize subjective taste as an objective defect without evidence.

## Verification

- Every prominent element has a task-specific reason.
- No placeholders, invented claims, unexplained metrics, or decorative filler remain.
- The result covers relevant failure and edge states.
- Completion claims name the evidence that supports them.
- Removing an element would now reduce usefulness, clarity, or correctness.

## Failure Modes

- Cosmetic cleanup that leaves an incorrect workflow untouched.
- Adding a new framework or design system to make output look intentional.
- Replacing one visual cliche with another.
- Rewriting concise factual prose into a longer style guide performance.
- Declaring work clean because search found no `TODO` markers.

## Examples

**UI:** remove nested decorative cards, keep the operational grouping, and add the missing loading/error states.

**Code:** delete a pass-through abstraction and reuse the repository's existing helper.

**Research:** replace a universal ranking with separate measured dimensions and stated assumptions.

## Sources

See `../../sources/anti-slop.sources.md`.
