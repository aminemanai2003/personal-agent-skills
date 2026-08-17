# Authentication, Sessions, And API Boundaries

## Authentication And Recovery

- Use established framework or identity-provider flows.
- Protect login, enrollment, password reset, account recovery, MFA changes, and email or phone changes as separate high-risk workflows.
- Avoid account enumeration in untrusted responses while preserving useful rate and abuse signals for operators.
- Re-authenticate or require stronger assurance for materially sensitive actions when the product risk justifies it.

## Authorization

- Default deny protected operations.
- Check action and object authorization at the server boundary on every request.
- Derive the acting identity and tenant from validated authentication state.
- Treat administrative, support, and background-job privileges as explicit roles with narrow scope and auditability.

## Browser Sessions And Tokens

- Choose stateful sessions or tokens from system constraints, not fashion.
- When cookies carry session authority, consider HttpOnly, Secure, appropriate SameSite behavior, narrow domain/path scope, rotation, invalidation, and CSRF protection together.
- Do not expose sensitive session material to browser JavaScript unless the architecture truly requires it and the XSS tradeoff is accepted.
- For signed tokens, constrain accepted algorithms and validate issuer, audience, time claims, signature, and key lifecycle. Encryption and signing solve different problems.

## APIs And External Requests

- Validate request schemas, field allowlists, pagination, sizes, and cost.
- Prevent mass assignment by mapping accepted fields explicitly.
- Constrain outbound destinations by scheme, host, port, resolution, redirect behavior, and network reachability when user influence exists.
- Configure CORS for intended browser origins and methods; CORS is not authorization.
- Apply rate and abuse controls according to endpoint cost, identity confidence, and consequence rather than one global constant.

## Uploads

- Enforce size, count, and content rules before expensive processing.
- Generate storage names and keep untrusted filenames out of paths and headers.
- Store uploads outside executable or public roots unless deliberate access control mediates delivery.
- Treat parsers, image processors, document converters, and archive extraction as additional attack surfaces.
