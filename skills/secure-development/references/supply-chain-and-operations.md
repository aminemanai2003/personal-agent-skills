# Supply Chain And Security Operations

## Dependencies

- Prefer existing or standard-library capability when it meets the contract.
- Inspect maintainer, source, release activity, license, transitive graph, install scripts, permissions, and ecosystem advisories before adding a dependency.
- Commit and verify the ecosystem lockfile. Review unexpected transitive or integrity changes.
- Remove unused packages and avoid abandoned forks or packages selected only by name similarity.
- Treat an advisory as context: confirm affected version, reachable feature, exploit preconditions, and available remediation.

## Build And CI

- Minimize workflow and token permissions.
- Keep untrusted pull-request content away from privileged secrets and write-capable workflows.
- Pin or verify third-party build actions and artifacts when supported.
- Separate build, signing, and deployment authority; protect provenance and release approvals according to impact.
- Do not print environment contents or secret-bearing commands into logs.

## Configuration And Deployment

- Ship secure defaults and make dangerous modes explicit.
- Disable development diagnostics and sample credentials outside intended local use.
- Restrict service, database, object-store, and cloud identity permissions to required operations.
- Verify TLS and certificate handling through maintained platform defaults.

## Logging And Response

- Log security-relevant events with actor, action, target, result, time, and correlation identifiers where appropriate.
- Exclude credentials, tokens, private keys, sensitive payloads, and unnecessary personal data.
- Define alert ownership and response for high-impact events; logs without review or retention policy are not an operational control.
