# Contributing

Keep contributions narrow and reviewable.

## Before editing

- Read `AGENTS.md`, the relevant skill, profile section, and source notes.
- Check `git status` and preserve unrelated changes.
- Decide whether the change is a skill, reference, adapter, evaluation, or documentation concern.

## Before committing

- Run `.\.venv\Scripts\python.exe scripts\validate_repo.py`.
- Run `.\.venv\Scripts\python.exe scripts\validate_evals.py` when skill behavior or triggers changed.
- Run `.\.venv\Scripts\python.exe scripts\validate_showcase.py` when showcase prompts, outputs, screenshots, or claims changed.
- Run `.\.venv\Scripts\python.exe -m unittest discover -s tests -v` when scripts changed.
- Scan the final diff for credentials, copied source text, placeholders, and unrelated churn.

Use imperative, specific commit subjects. Keep each skill, test/evaluation change, or architectural decision in its own commit when that produces a clearer history.
