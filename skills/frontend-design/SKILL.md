---
name: frontend-design
description: Design or substantially reshape user interfaces with domain-specific visual and interaction choices. Use when building a new page, component system, app surface, dashboard, landing experience, or when an existing UI needs a coherent new direction rather than a narrow defect fix.
---

# Frontend Design

## Purpose

Create an interface whose hierarchy, controls, content, and visual language follow the product's real work instead of generic page templates.

## Inputs

- Product, audience, primary workflow, and success condition.
- Existing design system, screenshots, assets, routes, and component patterns.
- Content, data density, supported devices, accessibility needs, and technical stack.
- Brand constraints and explicit visual references.

## Process

1. Inspect the existing product and identify the first-screen job.
2. Name the audience, workflow, information hierarchy, and required states.
3. If a design system exists, extend it consistently; identify the few axes the brief leaves open.
4. Define a compact direction: palette roles, typography roles, spacing, layout tracks, control language, and one justified signature element.
5. Map common actions to familiar controls: icons for tools, toggles for binary state, tabs for views, menus for option sets, and inputs for values.
6. Build the usable workflow first, including loading, empty, error, access, focus, and reduced-motion behavior.
7. Use stable responsive dimensions for boards, grids, toolbars, counters, and dynamic content.
8. Inspect desktop and mobile renders, revise generic or incoherent choices, and remove decoration that does not support the subject.

## Constraints

- Do not make a marketing landing page when the request is for an app or tool.
- Do not stack cards inside cards or frame every section as a floating card.
- Do not use gradients, decorative blobs, oversized type, or rounded text pills as automatic style choices.
- Do not replace an established product language with personal defaults.
- Do not invent explanatory interface copy about features or keyboard shortcuts.
- Do not ship controls that lack expected states or accessible names.

## Verification

- The primary workflow is immediately findable and usable.
- Visual choices can be traced to the subject, audience, brand, or task.
- Text and controls fit without overlap at supported viewports.
- Keyboard focus, contrast, reduced motion, and state feedback are coherent.
- Screenshots or rendered inspection confirm the implementation matches the intended direction.

## Failure Modes

- A generic hero, metrics row, and three-card grid unrelated to the product.
- Quiet-looking UI that is too sparse for repeated operational work.
- A distinctive mockup whose actual controls are incomplete.
- Desktop polish with broken mobile hierarchy.
- New colors, radii, or typography that fight the existing system.

## Examples

**Operations dashboard:** dense scan-friendly table, restrained status color, predictable filters, persistent actions, and clear empty/error states.

**Object-focused page:** show the actual object in the first viewport and leave a visible cue to the next section; avoid an abstract split hero.

## Sources

See `../../sources/frontend-design.sources.md`.

