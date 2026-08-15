# Showcase Methodology

The showcase compares the same AgentRouter-hosted `gpt-5.6-sol` model under two conditions:

- Baseline: isolated Git repository with no project instructions or personal skills.
- With skills: identical isolated repository with only the relevant canonical packages installed under `.agents/skills`.

Prompts, source material, model name, Codex CLI version, medium reasoning effort, sandbox permissions, and output constraints are held constant. The key difference is project-local skill availability. Final artifacts were generated with Codex CLI 0.147.0 on 2026-08-15. An initial research pilot exceeded the requested word ceiling in both conditions; it was excluded, the shared prompt was clarified to require a final word-count check, and both conditions were rerun.

The UI condition produces runnable code. The stored pages were re-captured from the unchanged artifacts at `1440 x 960` and `390 x 844` after an audit found that the first archived desktop images used different dimensions. The current paired PNGs are therefore comparable at the image level. Filtering, uncertainty, loading, empty, and warning paths were exercised in Chrome, and browser logs were checked for warnings and errors. The baseline mobile page fits the viewport; the skilled page expands to `632px` at a `390px` viewport because the wide line-of-business table causes page-level horizontal overflow.

Writing and research conditions preserve complete raw outputs. Examples are presented without AI-detector scores; the comparison is based on observable specificity, structure, constraint compliance, evidence use, interaction completeness, and prose quality. `scripts/validate_showcase.py` verifies the stored screenshot dimensions, reported word counts, and DOI coverage.

These are representative paired runs, not a statistical estimate of average model performance. Repeated trials would be required to measure variance.
