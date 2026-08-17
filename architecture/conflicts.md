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
| `root-cause-debugging` vs known fix | Diagnose when the cause is unknown or disputed; use the ordinary implementation workflow when the exact correction is already established. |
| `secure-development` vs routine code work | Load it for changed trust boundaries, identity, sensitive data, parsers, external inputs, dependencies, or privileged operations; skip it for changes where security reasoning cannot alter the outcome. |
| `secure-development` vs `security-review` | Build or fix with the former; perform a review-only assessment with the latter unless the user separately authorizes remediation. |
| `security-review` vs `review-code` | Use `security-review` for exploitability and security-boundary analysis; combine with `review-code` when general correctness and regression findings are also requested. |
| `project-start` vs narrow task | Orient unfamiliar work; skip when the relevant files, command, and contract are already known. |
| `anti-slop` vs domain workflow | Use as a critique pass; do not let it replace the skill that owns correctness or domain evidence. |
| `definition-of-done` vs implementation | Audit evidence after or during work; it does not implement missing behavior. |
| `resume-and-ats` vs `professional-profile` | Use the former for resume/CV content and parsing; use the latter for LinkedIn, portfolio, GitHub profile, bio, and public proof. |
| career artifact skills vs `job-search-and-applications` | Use artifact skills for isolated edits; use the application skill when selecting opportunities, coordinating a role-specific package, tracking, or outreach. |
| career advice vs external action | Drafting and planning are allowed in scope; submitting, publishing, scheduling, or messaging requires explicit authorization and current-state verification. |

When same-level rules still conflict, choose the option that protects the stated outcome with the lowest irreversible cost, state the material assumption, and record an ADR if the decision changes a public boundary.

