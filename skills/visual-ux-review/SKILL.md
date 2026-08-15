---
name: visual-ux-review
description: Inspect a rendered interface for visual hierarchy, responsive behavior, interaction states, accessibility signals, and domain fit. Use when screenshots, a running app, a design artifact, or a completed frontend implementation needs evidence-based UX findings before approval.
---

# Visual UX Review

## Purpose

Find user-visible defects and weak design decisions by observing the interface in realistic states rather than reviewing source code alone.

## Inputs

- Running application, screenshots, or design artifact.
- Intended audience, key workflow, supported viewports, and design system.
- Test credentials/data if authorized.
- Available browser automation and accessibility tools.

## Process

1. Establish the primary workflow and expected states.
2. Inspect the initial viewport at representative desktop and mobile sizes.
3. Walk the workflow with mouse and keyboard; trigger loading, empty, validation, error, access, and success states where practical.
4. Check hierarchy, scan order, density, control affordance, labels, feedback, and recovery paths.
5. Check layout stability, text fitting, clipping, overlap, scroll traps, and dynamic resizing.
6. Check focus visibility, keyboard reachability, contrast signals, reduced motion, and accessible names.
7. Use automated checks as supporting evidence, then verify important findings visually.
8. Report findings first, ordered by user impact, with state, viewport, evidence, and a concrete remedy.

## Constraints

- Do not review only the polished happy path.
- Do not infer rendered quality from component code.
- Do not call subjective preference a defect unless it conflicts with the brief or system.
- Do not treat an automated accessibility pass as full accessibility validation.
- Do not recommend a redesign when a focused correction solves the workflow problem.

## Verification

- All critical workflows and relevant states were observed or explicitly marked untested.
- Findings identify where and when the problem occurs.
- Severity reflects user impact, not visual novelty.
- Recommended changes preserve the product's established language.
- Evidence includes screenshots, browser state, or reproducible steps when available.

## Failure Modes

- A list of generic heuristics with no observed defects.
- Reviewing one viewport while claiming responsive quality.
- Fixating on color taste while missing blocked actions.
- Reporting tool output without confirming whether it affects the real UI.
- Suggesting broad visual churn that creates new inconsistency.

## Examples

**High severity:** the mobile filter drawer opens behind a fixed table toolbar, blocking the primary workflow.

**Lower severity:** a secondary caption has inconsistent spacing but remains readable and does not affect navigation.

## Sources

See `../../sources/visual-ux-review.sources.md`.

