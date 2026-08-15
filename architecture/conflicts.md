# Conflict Rules

## Precedence

1. Platform and safety rules.
2. Explicit current user instruction.
3. Project-local instructions and established contracts.
4. Objective engineering, security, accessibility, and domain quality.
5. Confirmed personal preferences.
6. Inferred personal preferences.
7. Skill-local defaults.

## Known boundaries

| Potential conflict | Resolution |
| --- | --- |
| `frontend-design` vs `review-ui` | Create or reshape with the former; inspect/readiness/fix with the latter. |
| `visual-ux-review` vs `review-ui` | The former collects rendered evidence; the latter owns findings, readiness, and authorized fixes. |
| `research-quality` vs `research-topic` | The former supplies evidence standards; the latter owns an end-to-end question and synthesis. |
| `code-quality` vs `review-code` | The former mutates implementation; the latter reviews without mutation unless separately authorized. |
| `build-feature` vs `review-code` | Implement through `build-feature`; assess an existing patch with `review-code`. |
| `project-start` vs narrow task | Orient unfamiliar work; skip when the relevant files, command, and contract are already known. |
| `anti-slop` vs domain workflow | Use as a critique pass; do not let it replace the skill that owns correctness or domain evidence. |
| `definition-of-done` vs implementation | Audit evidence after or during work; it does not implement missing behavior. |

When same-level rules still conflict, choose the option that protects the stated outcome with the lowest irreversible cost, state the material assumption, and record an ADR if the decision changes a public boundary.

