# Host Smoke Evaluation

Date: 2026-08-15

## Attempt

Installed 15 packages into `.agents/skills` and invoked Codex CLI in ephemeral read-only mode with a representative `build-feature` trigger prompt.

## Result

The CLI discovered the repository and started a session, but the Responses API returned `401 Unauthorized` for both WebSocket and HTTPS transport. No model response was produced, and no repository files were modified.

## Interpretation

- Package installation and local discovery are verified independently by the installer smoke test and installed directory count.
- Host-level model precision/recall and variance remain unmeasured until a valid Codex/Claude API session is configured.
- This is an environment credential limitation, not a skill-package failure.

