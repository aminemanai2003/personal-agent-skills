# Root Cause Debugging Sources

Primary inspiration:

- `obra/superpowers`, `skills/systematic-debugging`, commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (MIT). Useful principles: reproduce before fixing, trace data to its origin, test one hypothesis at a time, and add regression coverage.
- `obra/superpowers`, `skills/systematic-debugging/root-cause-tracing.md`, same commit and license. Useful principle: follow the call and data chain backward rather than repairing only the deepest visible symptom.

Repository and activity signal:

- Source inspected on 2026-08-17. The repository was actively maintained and widely installed through the open skills ecosystem.

Adaptation boundary:

- Rewrote the workflow in this repository's concise contract format rather than copying the source skill body.
- Replaced absolute process language with an incident-safe exception for reversible containment.
- Added privacy limits for diagnostics, explicit intermittent-failure evidence, performance and concurrency guidance, authorization boundaries, and proportional verification.
- Did not copy source scripts, examples, diagrams, or creation logs.

Conflicts resolved:

- `build-feature` owns new behavior; this skill owns unexplained failures.
- `review-code` remains review-only; this skill may instrument and fix when authorized.
- `definition-of-done` audits completion evidence after the debugging workflow establishes a cause and fix.

Original implementation:

- The trigger boundary, diagnostic playbook, incident distinction, verification contract, and integration with this repository's skill graph are original.
