---
name: security-review
description: Perform a review-only security assessment of a diff, feature, repository, API, workflow, dependency change, or deployment configuration. Use when asked to find vulnerabilities, review for security issues, audit authentication or authorization, check injection, secrets, cryptography, SSRF, uploads, CI/CD, or supply-chain risk; report concrete reachable findings and evidence without editing files unless a separate fix request authorizes changes.
---

# Security Review

## Purpose

Find security defects that can change the ship decision, while filtering pattern matches that are neutralized by data flow, configuration, framework protections, or unreachable code.

## Inputs

- Review scope: diff, files, route, service, repository, workflow, dependency graph, or deployment configuration.
- Intended behavior, threat model, actors, assets, trust boundaries, and authorization assumptions.
- Framework and runtime versions, relevant configuration, tests, check results, and deployment context.
- Permission to inspect related code and run read-only diagnostics; authorization for fixes is separate.

## Scope Boundary

This skill is review-only. Use `secure-development` while implementing or designing security-relevant behavior, `review-code` for a general defect review, and `definition-of-done` for release evidence. Do not report generic hardening advice as a vulnerability unless it has a plausible impact and reachable path.

## Process

1. Confirm scope, expected behavior, changed trust boundaries, and whether the request is review-only. Inspect repository rules and the relevant diff before scanning broadly.
2. Inventory entry points, identities, privileged actions, sensitive assets, parsers, stores, outbound requests, file operations, dependencies, and CI or deployment authority.
3. Detect candidate issues across authorization, authentication and sessions, injection, XSS and CSRF, SSRF, path and file handling, deserialization, cryptography, secrets, sensitive data, business logic, dependencies, and CI/CD. Load only the matching guidance in `references/review-matrix.md`.
4. Trace each candidate from attacker-controlled or externally influenced input to the security-sensitive operation. Inspect validation, encoding, authorization, middleware, configuration, framework behavior, and deployment assumptions across files.
5. Verify exploitability and impact. Distinguish confirmed findings, needs-verification questions, and low-confidence hardening observations. Do not elevate a theoretical pattern to a vulnerability.
6. Rank confirmed findings by realistic impact, reachability, required privilege, exploit complexity, affected scope, and available mitigation. Use severity labels as communication aids, not as a substitute for reasoning.
7. Report findings first using `references/report-format.md`, with file and line, scenario, evidence, impact, confidence, and the smallest effective remedy. State clearly when no high-confidence findings were identified.
8. Report scope limitations, untested runtime or deployment paths, and remaining uncertainty. Do not modify files or claim a clean bill of health from static pattern scans alone.

## Constraints

- Do not report a vulnerability solely because a dangerous-looking API exists; establish attacker influence and a reachable sink.
- Do not treat test fixtures, dead code, constants, server-controlled configuration, or framework-safe APIs as exploitable without a concrete path.
- Do not assume client-side checks, hidden fields, CORS, or UI visibility enforce authorization.
- Do not expose discovered credentials in the report; identify the secret type and location, then recommend rotation and containment.
- Do not run intrusive exploitation, destructive commands, or production changes without explicit authorization and a safe scope.
- Do not modify the reviewed patch under a review-only request.
- Do not claim compliance, penetration-test coverage, or absence of risk from a checklist, scanner, or untested environment.

## Verification

- Every reported finding has a reachable path, affected asset, impact, and supporting code or configuration evidence.
- Data-flow and framework checks were performed before severity was assigned.
- Findings are ordered by decision impact and contain actionable, proportionate remedies.
- Secret findings avoid reproducing credential material and include containment guidance.
- Review scope, skipped paths, tool limitations, and residual risk are explicit.
- A no-findings result states what was inspected and what remains unverified.

## Failure Modes

- Listing OWASP categories without tracing any actual path.
- Reporting every hardcoded string as a secret or every missing header as a blocker.
- Calling a server-controlled URL SSRF without proving user influence.
- Confusing authentication with object-level authorization.
- Recommending patches before explaining exploitability.
- Approving because tests are green while changed security boundaries were not exercised.

## Examples

**API review:** trace an object ID from route input through authorization and query; report an IDOR only if a user can reach another user's object and the check is absent or bypassable.

**CI review:** inspect event trust, workflow permissions, checkout behavior, and secret exposure before reporting a pull-request command or expression injection risk.

## Sources

See `../../sources/security-review.sources.md`.

Load `references/review-matrix.md` and `references/report-format.md` as needed.
