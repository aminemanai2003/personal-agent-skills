# Evaluation Contract

Each important skill gets realistic prompts in `evals/evals.json` and a record of observed failures. Evaluate both behavior and triggering: the agent should use a skill when appropriate, avoid it when out of scope, and produce evidence-backed results.

`scripts/validate_evals.py` validates the case schema and coverage only. A passing run does not prove that a model selected the expected skills or produced the expected behavior. Live model runs and repeated trials are separate evaluation work.

Minimum scenario coverage for a foundational workflow:

- one happy-path task;
- one ambiguous or underspecified task;
- one failure or partial-information task;
- one near-miss that should not trigger the skill.

Do not treat a passing checklist as proof of quality. Record concrete outputs, missed requirements, unnecessary changes, and regression risk.
