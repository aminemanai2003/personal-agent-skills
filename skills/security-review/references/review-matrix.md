# Security Review Matrix

Load only categories relevant to the reviewed surface.

| Surface | Questions | Evidence to trace |
| --- | --- | --- |
| Authorization | Can an actor access or mutate another object, tenant, role, or workflow stage? | Identity, object lookup, policy decision, error path |
| Authentication and sessions | Can credentials, reset flows, tokens, or sessions be forged, replayed, fixed, or escalated? | Issuance, verification, rotation, expiry, invalidation, client storage |
| Injection and output | Can external data reach SQL, shell, templates, HTML, headers, logs, or interpreters unsafely? | Source, transformations, parameterization, encoding, sink |
| SSRF and outbound calls | Can an attacker influence destination, scheme, port, redirects, or resolved address? | Input source, allowlist, DNS and redirect handling, network placement |
| Files and parsers | Can names, paths, archives, uploads, XML, or serialized data escape intended boundaries? | Validation, normalization, storage, parser mode, resource limits |
| Secrets and data | Are credentials, keys, tokens, or sensitive fields exposed, over-retained, or over-authorized? | Source, logs, responses, bundles, backups, access policy, rotation |
| Cryptography | Is a vetted primitive used for the actual property, with correct key and randomness handling? | Algorithm, mode, key source, purpose, verification, migration |
| Business logic | Can limits, ordering, retries, races, prices, approvals, or state transitions be bypassed? | Invariants, concurrency, replay, idempotency, authorization |
| Dependencies and CI | Can untrusted content influence privileged build, release, or dependency execution? | Event trust, permissions, pins, lockfile, artifacts, secrets |

## Confidence Gate

- **Confirmed:** attacker or external influence is established, the vulnerable path is reachable, and the mitigation is absent or bypassable.
- **Needs verification:** a plausible concern exists but a source, configuration, runtime, or deployment fact is missing.
- **Observation:** defense-in-depth or maintenance advice without a demonstrated security impact. Do not present it as a vulnerability finding.

## Framework Checks

Before reporting, inspect the framework's actual behavior: escaping, parameterization, middleware order, route guards, CSRF handling, token validation, safe parser defaults, and deployment configuration. Never infer protection or vulnerability from a function name alone.
