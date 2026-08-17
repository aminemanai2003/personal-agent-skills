---
name: root-cause-debugging
description: Diagnose reproducible or intermittent software failures by tracing evidence from symptom to originating cause, testing one hypothesis at a time, and adding regression coverage. Use when a bug, failing test, build error, production incident, performance regression, race, timeout, or unexplained behavior requires investigation and a verified fix; do not use for a known mechanical edit whose cause and remedy are already established.
---

# Root Cause Debugging

## Purpose

Replace guess-and-check fixes with a short evidence loop that explains why the failure occurs, fixes the responsible boundary, and prevents recurrence.

## Inputs

- Observed symptom, expected behavior, impact, and first known occurrence.
- Reproduction steps, failing command, logs, stack traces, metrics, and environment details.
- Recent changes, comparable working paths, dependency or configuration differences, and relevant tests.
- Authorization for mitigation, instrumentation, code changes, and production access.

## Scope Boundary

Use this skill to investigate and fix an unexplained failure. Use `review-code` for a review-only request and `build-feature` when the requested behavior is new rather than broken. During an active incident, contain user harm first when authorized, then continue the root-cause investigation.

## Process

1. Define the failure precisely: expected result, actual result, affected scope, frequency, and earliest known occurrence.
2. Reproduce the smallest faithful case. Record exact commands, inputs, environment, timing, and whether reproduction is deterministic.
3. Read the complete error chain and inspect recent relevant changes before editing. Separate observations from interpretations.
4. Trace the failing value, state, or event backward across component boundaries until its first incorrect origin. Add narrow diagnostic instrumentation when existing evidence cannot locate the break.
5. Compare the failing path with one working path or known-good version. List meaningful differences without assuming which one matters.
6. State one falsifiable hypothesis with predicted evidence. Test it with the smallest experiment that changes one variable.
7. If disproved, preserve what the experiment taught, remove temporary changes, and form a new hypothesis. After repeated failed fixes reveal different coupling failures, stop and reassess the architecture instead of stacking patches.
8. Create a regression test or deterministic check that fails for the confirmed cause. For intermittent failures, make the trigger observable and repeatable enough to distinguish signal from chance.
9. Implement the smallest fix at the originating boundary. Add defense in depth only where it blocks a realistic recurrence or makes failure explicit.
10. Re-run the original reproduction, the regression check, adjacent tests, and broader checks proportional to the affected contract. Remove temporary diagnostics or convert useful ones into safe observability.

## Constraints

- Do not propose a code fix before gathering enough evidence to name a testable cause, except for an explicitly labeled reversible mitigation during an incident.
- Do not change multiple independent variables in one diagnostic experiment.
- Do not hide the failure with a catch-all exception, retry, timeout increase, cache clear, or test skip unless evidence shows that behavior is the correct contract.
- Do not expose secrets, personal data, or sensitive payloads through debugging logs.
- Do not require a perfect reproduction before collecting useful evidence from an intermittent or external failure.
- Do not claim root cause when only the immediate symptom or correlation is known.

## Verification

- The explanation connects the initiating condition to the observed failure through inspectable evidence.
- The regression check fails before the fix or otherwise demonstrates the original broken condition.
- The fix addresses the source rather than only suppressing the symptom.
- Original, adjacent, and relevant failure-path checks pass after the final change.
- Temporary experiments and unsafe diagnostic output are removed.
- Remaining uncertainty, environmental dependence, or unverified production behavior is stated explicitly.

## Failure Modes

- Editing the most suspicious line before reproducing or tracing the data flow.
- Treating a passing rerun as proof for a flaky failure.
- Adding retries to an invalid-state or authorization bug.
- Fixing a deep stack-frame symptom while the invalid value is created earlier.
- Preserving several speculative changes after only one appears to help.
- Declaring an external service the cause without boundary evidence.

## Examples

**Failing test:** reproduce the focused test, trace the malformed fixture to premature initialization, write a regression case, fix initialization, and rerun the focused and neighboring suites.

**Intermittent timeout:** capture timing at each boundary, distinguish queueing from execution latency, test the bottleneck hypothesis, then fix or bound the responsible stage rather than increasing every timeout.

## Sources

See `../../sources/root-cause-debugging.sources.md`.

For intermittent, multi-component, concurrency, and performance investigations, read `references/diagnostic-playbook.md`.
