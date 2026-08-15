# Personal Operating Interview

Status: complete for V1

## Confirmed response

Amine's priorities are:

1. Non-generic UI that reflects human expert judgment and avoids visual slop.
2. Natural, specific writing without formulaic AI-style signals or prose slop.
3. Top-quality AI-assisted research papers that meet a human expert standard and avoid generic or synthetic-sounding scholarship.

No further workflow-preference interview is required for V1. The remaining questions below are retained only as future optional refinements.

Answer only the decisions that cannot be inferred from existing repositories. Short answers are enough; examples are more useful than adjectives.

## 1. Autonomy and risk

- When a change is reversible but broad, should the agent proceed and report, or pause for approval?
- What actions always require explicit approval (for example: deleting data, changing production configuration, publishing, merging)?
- When a task is ambiguous, do you prefer one recommended assumption or a short set of options?

## 2. Engineering tradeoffs

- Which tradeoff should dominate when they conflict: delivery speed, maintainability, runtime performance, or minimal diff?
- What is your default tolerance for adding a dependency when it removes meaningful complexity?
- Which languages/frameworks should receive special treatment in V1, if any?

## 3. Frontend and product judgment

- Which products or interfaces are your strongest visual references?
- How much visual experimentation is welcome when a brief is underspecified?
- Which accessibility, browser, or device targets are mandatory for your projects?

## 4. Writing and communication

- In final reports, do you prefer findings-first, a short narrative, or a fixed template?
- Should the agent challenge your ideas inline, in a separate risks section, or both?
- Which kinds of tone or phrasing should be avoided beyond marketing language?

## 5. Research and quantitative work

- What source hierarchy should the agent use when primary sources are unavailable?
- What level of reproducibility is required before a result is actionable?
- Which domains, metrics, or claims should always receive extra skepticism?

## 6. GitHub workflow

- Should the agent open PRs automatically after local verification, or stop before publication?
- What is your preferred merge policy (squash, merge commit, rebase) and required checks?
- Should issue/PR comments be terse, explanatory, or templated?

## 7. Success signal

- Name one recent agent result that felt excellent and one that felt generic or risky. What specifically made the difference?
