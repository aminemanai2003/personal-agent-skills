---
name: review-ui
description: Conduct a complete UI review that combines rendered workflow inspection, design-system fit, accessibility, responsive behavior, and implementation evidence. Use when the user asks for UI or UX review, visual QA, frontend merge readiness, screenshot critique, or review-and-fix of an existing interface.
---

# Review UI

## Purpose

Turn visual inspection into prioritized, reproducible findings and, when explicitly requested, focused fixes that preserve the product's design language.

## Inputs

- Running app or renderable frontend, target routes, and supported viewports.
- Product audience, key workflows, design system, and acceptance criteria.
- Authorized test data/credentials and current implementation diff.
- Whether the request is review-only or includes fixes.

## Process

1. Inspect the product context, design tokens, route, and changed implementation.
2. Define the primary workflow and a state matrix for desktop and mobile.
3. Render and interact with the interface; use screenshots for stable evidence.
4. Evaluate hierarchy, density, domain fit, control choice, content clarity, feedback, and recovery.
5. Check layout stability, text fitting, focus, keyboard behavior, contrast signals, accessible names, and reduced motion.
6. Compare the result with the existing design system and the brief, not with a generic personal aesthetic.
7. Rank findings by user impact and cite viewport, state, element, evidence, and remedy.
8. If fixes are authorized, implement the smallest coherent corrections, rerender affected states, and rerun checks.
9. Report findings or fixes first, followed by untested states and residual risk.

## Constraints

- Do not change files for a review-only request.
- Do not review source code as a substitute for the rendered interface.
- Do not recommend cosmetic churn that conflicts with an established system.
- Do not ignore loading, error, empty, access, long-content, or mobile states.
- Do not claim accessibility conformance from automated tooling alone.

## Verification

- Representative desktop and mobile states were rendered or marked unavailable.
- The primary workflow was exercised with keyboard and pointer where applicable.
- Findings are reproducible and severity reflects blocked or degraded user outcomes.
- Authorized fixes were visually rechecked after the final edit.
- Screenshots and tool results correspond to the current code, not stale state.

## Failure Modes

- A generic design critique with no viewport or workflow evidence.
- Rebuilding the visual direction to address a narrow alignment defect.
- Passing the happy path while error content overlaps controls.
- Treating personal dislike of a palette as a bug.
- Fixing desktop layout while introducing mobile overflow.

## Examples

**Review-only:** report that a mobile modal traps the submit button below an unscrollable viewport, with reproduction and focused CSS remedy.

**Review and fix:** correct the modal layout, then capture mobile and desktop screenshots for empty, validation-error, and successful states.

## Sources

See `../../sources/review-ui.sources.md`.

