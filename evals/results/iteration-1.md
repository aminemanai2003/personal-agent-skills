# Evaluation Iteration 1

Date: 2026-08-15

## Method

Reviewed all 45 realistic cases in `evals/evals.json` against skill descriptions, process ownership, constraints, and expected composition. Each of the 15 skills had at least two positive cases and one near-miss case. This pass evaluated trigger intent and workflow completeness; it did not use an independent model-run variance benchmark.

## Results

| Skill family | Positive cases | Near-miss coverage | Result |
| --- | ---: | ---: | --- |
| Personal profile and decisions | 6 | 4 | Pass with boundary notes |
| Anti-slop and completion | 6 | 6 | Pass with boundary notes |
| Code implementation and review | 10 | 9 | Pass after mutation/review clarification |
| Frontend creation and review | 10 | 9 | Pass after creation/inspection clarification |
| Research standards and workflow | 8 | 7 | Pass after standard/workflow clarification |
| Writing and GitHub | 7 | 6 | Pass |
| Project orientation | 5 | 5 | Pass after narrow-task exclusion |

Counts overlap because composite cases intentionally exercise more than one skill.

## Failures Found

1. `review-ui` and `visual-ux-review` both described rendered inspection without clearly assigning orchestration and evidence-collection ownership.
2. `research-topic` and `research-quality` both covered comparison and benchmarks without distinguishing end-to-end investigation from evidence standards.
3. `code-quality` and `review-code` needed an explicit mutation boundary for review-only prompts.
4. `frontend-design` needed a direct exclusion for narrow review of an existing render.
5. `project-start` could over-trigger on small tasks in an already-understood file.
6. Cross-cutting `anti-slop` and `definition-of-done` needed to state that they do not replace the task-owning workflow.

## Refinement

Commit `f4d15fe` added explicit scope boundaries to ten skills. No skill was split or added; the failures came from trigger ownership, not missing capability.

## Remaining Risk

The cases establish a strong deterministic review set, but actual host triggering can vary by model and platform version. A later benchmark should run the same cases repeatedly in Codex and Claude Code and record precision, recall, unnecessary skill loading, and outcome quality.

