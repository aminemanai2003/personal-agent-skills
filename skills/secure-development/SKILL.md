---
name: secure-development
description: Design or implement software with explicit trust boundaries, server-side authorization, safe input and output handling, protected sessions and secrets, vetted cryptography, least privilege, and supply-chain controls. Use when building or changing authentication, authorization, sessions, APIs, uploads, external requests, sensitive data, credentials, cryptographic behavior, payments, multi-tenant access, dependencies, CI/CD, or other security-relevant boundaries; do not trigger for ordinary low-risk code edits with no changed security surface.
---

# Secure Development

## Purpose

Integrate security into design and implementation decisions so the delivered behavior is safe by default without imposing cargo-cult controls on unrelated work.

## Inputs

- User workflow, assets at risk, data classification, actors, tenants, roles, and abuse consequences.
- Entry points, trust boundaries, deployment topology, authentication model, and authorization rules.
- Framework protections, existing security controls, secrets and key ownership, dependency manifests, and operational constraints.
- Applicable regulatory or contractual requirements, treated separately from actual threat reduction.

## Scope Boundary

Use this skill while designing or changing security-relevant behavior. Use `security-review` for a review-only vulnerability assessment. Compose through `build-feature` for end-to-end implementation and use `code-quality` for general implementation rules. Do not activate only because a file is production code.

## Process

1. Identify assets, actors, trust boundaries, entry points, privileged operations, and credible abuse cases. Read `references/trust-boundaries.md` when the feature crosses services, tenants, privilege levels, or external systems.
2. Define the security contract before coding: who may perform each action, what input is accepted, what data may be returned, how failure behaves, and what must be audited.
3. Reuse the repository's established authentication, authorization, validation, encryption, and secret-management mechanisms. Prefer maintained framework features and vetted libraries over custom security primitives.
4. Enforce authorization on the trusted server or service boundary for every protected object and action. Derive identity and tenant context from validated authentication state, not client-supplied ownership fields.
5. Validate untrusted input structurally and semantically at entry points; constrain size, type, range, path, URL destination, and resource cost. Use parameterized or structured APIs and context-appropriate output encoding.
6. Select session or token architecture from the clients and trust model. For browser sessions, prefer protected cookies when appropriate; never make browser local storage the default location for sensitive session material. Read `references/auth-sessions-and-apis.md` for auth, API, CSRF, CORS, SSRF, and upload decisions.
7. Keep credentials, private keys, signing material, and service secrets out of source, client bundles, logs, fixtures, and repository history. Define ownership, access, rotation, revocation, and failure behavior. Read `references/secrets-crypto-and-data.md` for cryptography and sensitive data.
8. Apply least privilege to processes, identities, database access, cloud roles, network reachability, and CI tokens. Fail closed when authorization or policy state is unavailable unless the explicit safety contract requires a different degraded mode.
9. Evaluate new and changed dependencies by provenance, maintenance, lockfile integrity, transitive impact, permissions, and known vulnerabilities. Pin and verify artifacts where the ecosystem supports it. Read `references/supply-chain-and-operations.md` for dependency, CI, logging, and deployment controls.
10. Add tests for unauthorized, cross-tenant, malformed, oversized, replayed, expired, and failure-path behavior relevant to the feature. Use deterministic security tooling as evidence, not as proof by itself.
11. Review the final data flow and diff for secrets, client-trusted authorization, unsafe defaults, verbose sensitive errors, logging exposure, and bypass paths. Record residual risks and operational requirements.

## Constraints

- Never invent cryptographic algorithms, protocols, password hashing, token signing, randomness, or key derivation.
- Do not treat JWT as inherently safer than stateful sessions or select it without an architectural reason. When used, validate the intended issuer, audience, algorithm, expiry, signature, and key lifecycle.
- Never trust client-side authorization, hidden UI, route guards, or unsigned client claims as the enforcement boundary.
- Do not store sensitive authentication or session material in browser local storage by default; document any exception and its threat tradeoff.
- Do not hardcode universal cookie modes, token lifetimes, rate limits, cipher choices, or password rules without product, platform, and current standards context.
- Do not log secrets, raw credentials, full tokens, private personal data, or unnecessary request bodies.
- Do not claim compliance, penetration-test coverage, or absence of vulnerabilities from a checklist or scanner result.
- Do not weaken TLS verification, origin restrictions, sandboxing, or authorization to make integration easier.

## Verification

- Each protected action has an explicit server-side authorization path and cross-user or cross-tenant tests where relevant.
- Untrusted inputs reach sensitive sinks only through appropriate validation and structured APIs.
- Session, token, secret, and key handling matches the actual client and deployment threat model.
- Sensitive failures expose useful operator evidence without leaking internals to untrusted users.
- Dependency and CI changes preserve lockfile integrity and least privilege.
- Security tests cover the realistic abuse paths introduced or changed by the work.
- Residual risk, untested external behavior, and required operational controls are visible in the handoff.

## Failure Modes

- Adding authentication while omitting object-level authorization.
- Accepting a user or tenant identifier from the request as proof of ownership.
- Moving a token to local storage because it is convenient for frontend code.
- Using encryption without a key ownership and rotation plan.
- Blocking every URL substring instead of positively constraining external destinations.
- Treating dependency audit output as a complete supply-chain review.
- Applying a generic security checklist without tracing the feature's actual data and privilege flow.

## Examples

**Multi-tenant API:** derive tenant identity from validated session state, authorize the requested object within that tenant, constrain fields, test cross-tenant access, and audit privileged changes.

**File upload:** limit size and count, inspect content rather than trusting the extension, generate server-side names, isolate storage, prevent execution, and verify authorization on upload and download.

## Sources

See `../../sources/secure-development.sources.md`.
