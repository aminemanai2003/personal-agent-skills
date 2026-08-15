---
name: frontend-design
description: Design or substantially reshape user interfaces with domain-specific visual and interaction choices. Use when building a new page, component system, app surface, dashboard, landing experience, or when an existing UI needs a coherent new direction rather than a narrow defect fix.
---

# Frontend Design

## Purpose

Create an interface whose hierarchy, controls, content, and visual language show coherent human expert judgment and could not be mistaken for an unrelated product with different labels.

## Inputs

- Product, audience, primary workflow, and success condition.
- Existing design system, screenshots, assets, routes, and component patterns.
- Content, data density, supported devices, accessibility needs, and technical stack.
- Brand constraints and explicit visual references.

## Scope Boundary

Use this for creating or substantially reshaping a direction. For inspection of an existing rendered interface, use `visual-ux-review` or the higher-level `review-ui` workflow.

## Process

1. Inspect the existing product and identify the first-screen job.
2. Name the audience, workflow, information hierarchy, and required states.
3. If a design system exists, extend it consistently; identify the few axes the brief leaves open.
4. Define a compact direction: palette roles, typography roles, spacing, layout tracks, control language, and one justified signature element.
5. Test the direction against an unrelated product: if the same layout, copy rhythm, palette, and component composition would still work after relabeling, revise it from the subject's real materials, data, terminology, and workflow.
6. Map common actions to familiar controls: icons for tools, toggles for binary state, tabs for views, menus for option sets, and inputs for values.
7. Build the usable workflow first, including loading, empty, error, access, focus, and reduced-motion behavior.
8. Use stable responsive dimensions for boards, grids, toolbars, counters, and dynamic content.
9. Inspect desktop and mobile renders as a design critic, not only as a tester. Revise generic composition, weak type hierarchy, arbitrary spacing, fake content, and decoration that does not support the subject.
10. Make a final subtraction pass, then ensure the remaining distinctive choices form one coherent system rather than scattered novelty.

## Constraints

- Do not make a marketing landing page when the request is for an app or tool.
- Do not stack cards inside cards or frame every section as a floating card.
- Do not use gradients, decorative blobs, oversized type, or rounded text pills as automatic style choices.
- Do not imitate a fashionable visual style without connecting it to the product's subject, audience, and content.
- Do not use placeholder statistics, generic names, or polished fake content when real domain content can be represented.
- Do not replace an established product language with personal defaults.
- Do not invent explanatory interface copy about features or keyboard shortcuts.
- Do not ship controls that lack expected states or accessible names.

## Verification

- The primary workflow is immediately findable and usable.
- Visual choices can be traced to the subject, audience, brand, or task.
- The interface fails the relabeling test: moving it to an unrelated product would require structural and visual redesign, not only new text.
- Typography, spacing, density, color, and interaction feel intentionally directed as one system.
- Text and controls fit without overlap at supported viewports.
- Keyboard focus, contrast, reduced motion, and state feedback are coherent.
- Screenshots or rendered inspection confirm the implementation matches the intended direction.

## Failure Modes

- A generic hero, metrics row, and three-card grid unrelated to the product.
- Quiet-looking UI that is too sparse for repeated operational work.
- A distinctive mockup whose actual controls are incomplete.
- Desktop polish with broken mobile hierarchy.
- New colors, radii, or typography that fight the existing system.
- A technically polished page that still resembles the default output for dozens of unrelated prompts.

## Examples

**Operations dashboard:** dense scan-friendly table, restrained status color, predictable filters, persistent actions, and clear empty/error states.

**Object-focused page:** show the actual object in the first viewport and leave a visible cue to the next section; avoid an abstract split hero.

## Sources

See `../../sources/frontend-design.sources.md`.
