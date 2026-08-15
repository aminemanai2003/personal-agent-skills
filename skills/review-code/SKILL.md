---
name: review-code
description: Review a patch, pull request, branch, or implementation for concrete defects and regression risk. Use when the user asks for code review, PR assessment, merge readiness, security or quality findings, or a second pass over completed code without authorizing changes.
---

# Review Code

## Purpose

Find actionable correctness, compatibility, security, performance, and maintainability problems that could change the decision to ship.

## Inputs

- Diff, branch, PR, issue/spec, and base behavior.
- Repository instructions, tests, public contracts, and relevant runtime context.
- Check results, review threads, and known limitations.

## Scope Boundary

This skill is review-only unless the user separately authorizes fixes. Use `code-quality` for implementation/refactoring and `build-feature` for end-to-end delivery.

## Process

1. Establish intent and expected behavior before judging implementation.
2. Inspect repository rules, diff scope, changed contracts, and surrounding code.
3. Read changed tests early to understand claimed behavior and blind spots.
4. Trace important success, edge, error, authorization, and compatibility paths.
5. Look for concrete defects across correctness, security, data integrity, performance, concurrency, and architecture.
6. Validate suspicious behavior with code evidence or a focused reproduction when feasible.
7. Rank findings by impact and likelihood; omit speculative style commentary.
8. Report findings first with file/line, scenario, impact, and the smallest effective remedy.
9. Then state open questions, test gaps, and a brief change summary.

## Constraints

- Do not modify code unless the user also asks for fixes.
- Do not report formatting preferences already enforced by tools.
- Do not flag a theoretical issue without a plausible triggering path.
- Do not inflate severity to make the review look substantial.
- Do not approve based only on green checks; confirm those checks cover the changed contract.

## Verification

- Each finding identifies a concrete behavior and supporting evidence.
- Severity matches user impact and reachability.
- File and line references point to the responsible code.
- Recommended remedies address root cause without unnecessary redesign.
- If no findings exist, remaining test gaps or residual risk are stated clearly.

## Failure Modes

- Summarizing the diff instead of reviewing it.
- Listing many nits while missing a compatibility regression.
- Treating missing tests as a defect without identifying the behavior at risk.
- Reporting a pre-existing issue unrelated to the patch as a blocker.
- Trusting a test name without reading what it asserts.

## Examples

**High:** an authorization check occurs after data is returned; cite the path and recommend moving enforcement to the boundary with a regression test.

**No findings:** say so directly, then note that the external integration path was not exercised if that is the remaining risk.

## Sources

See `../../sources/review-code.sources.md`.
