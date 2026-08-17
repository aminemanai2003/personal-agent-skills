# Diagnostic Playbook

Load only the section matching the failure shape.

## Multi-Component Failures

Build a boundary table before changing behavior:

| Boundary | Input observed | Output observed | Configuration/version | Timing | Result |
| --- | --- | --- | --- | --- | --- |

Instrument before and after the suspected boundary. Record identifiers and structural facts, not secrets or full sensitive payloads. Verify configuration propagation rather than assuming that local, CI, staging, and production use the same values.

## Intermittent Failures

1. Record failure frequency and the number of trials.
2. Control one source of variance at a time: seed, clock, network, scheduling, test order, or external dependency.
3. Prefer condition-based synchronization over arbitrary sleeps.
4. Preserve timestamps and correlation identifiers across components.
5. Treat one passing rerun as inconclusive; compare failure rates before and after the proposed fix.

## Concurrency and Races

- Draw the relevant state transitions and ownership rules.
- Identify shared mutable state, missing atomicity, stale reads, duplicate delivery, and ordering assumptions.
- Add a deterministic barrier, fake clock, controlled scheduler, or repeated stress test when available.
- Verify both safety properties, such as no double spend, and liveness properties, such as eventual completion.

## Performance Regressions

1. Define the metric, workload, environment, and baseline.
2. Separate CPU, memory, I/O, network, lock contention, queueing, and downstream latency.
3. Profile the representative path instead of optimizing from intuition.
4. Confirm that the proposed change improves the target metric without shifting cost to an unacceptable dimension.

## External and Environmental Failures

- Capture the request boundary, response or error class, retry behavior, timeout, and provider status evidence.
- Compare local and failing environments by concrete versions and configuration.
- When the external cause cannot be eliminated, implement bounded handling, observability, and an explicit failure contract.

## Stop Signals

Pause and reassess when:

- three attempted fixes produce unrelated new failures;
- the issue requires broad redesign to preserve a supposedly simple invariant;
- reproduction depends on unknown production state that current authorization cannot inspect;
- evidence points to data loss, security exposure, or destructive migration risk beyond the requested authority.
