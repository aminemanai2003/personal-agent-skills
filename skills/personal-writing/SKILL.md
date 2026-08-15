---
name: personal-writing
description: Write natural, specific, expert-level prose in Amine's preferred style. Use when drafting or revising handoffs, READMEs, documentation, issues, pull requests, review comments, research papers or summaries, decisions, and user-facing technical explanations.
---

# Personal Writing

## Purpose

Write prose that sounds authored by a knowledgeable person with a reason to communicate, not generated from a reusable response pattern.

## Inputs

- Audience, channel, and action the reader should take.
- Verified facts, source material, and relevant uncertainty.
- Repository terminology and any required template.
- The desired level of technical depth.

## Process

1. Identify the reader's first question and lead with its answer.
2. Separate verified facts from interpretation, recommendation, and unresolved risk.
3. Build the structure from the reader's real questions and the material's logic; do not force a stock introduction-body-conclusion rhythm or symmetrical list.
4. Use domain vocabulary, concrete nouns, and details that could only belong to this subject.
5. Prefer active voice and plain verbs, but vary sentence length and structure when the reasoning naturally requires it.
6. Include reasoning only where it helps evaluate a decision, understand a causal link, or reproduce a result.
7. State verification, skipped checks, limitations, and authority boundaries directly.
8. Remove canned transitions, throat-clearing, generic praise, repeated conclusions, inflated certainty, and meta-commentary.
9. Read the text as a continuous argument. Fix abrupt section stitching, repeated sentence shapes, and paragraphs that could be moved anywhere without changing the meaning.
10. Format only enough to support the channel and content.

## Constraints

- Do not begin with praise or a recap the reader already knows.
- Do not turn limitations into vague disclaimers.
- Do not use marketing claims, fake urgency, or unsupported superlatives.
- Do not bury critical findings below a long summary.
- Do not force one template across chat, docs, issues, and PR reviews.
- Do not use generic openers such as broad claims about a rapidly changing world, or transitions that merely announce the next section.
- Do not add a summary that repeats the preceding paragraph without advancing the reader's understanding.
- Do not optimize prose for an AI-detector score. Optimize it for originality, specificity, accuracy, and accountable authorship.
- Follow institutional, venue, or publisher rules that require disclosure of AI assistance.

## Verification

- The first paragraph answers the reader's main question.
- Every material claim is verified or clearly qualified.
- Actions, owners, and unresolved decisions are explicit when applicable.
- Tone matches the audience and avoids filler.
- Structure follows the subject's logic rather than a visible response template.
- Paragraphs contain specific evidence, reasoning, or action; none exist only to smooth over weak content.
- The text can be shortened no further without losing useful meaning.

## Failure Modes

- A polished narrative that hides the actual result.
- Over-formatting a simple handoff.
- Terse comments that state a problem but not its impact or remedy.
- Long explanations of routine implementation steps.
- Claiming certainty where source or test coverage is incomplete.
- Grammatically clean prose with generic content, repetitive cadence, and interchangeable transitions.
- Mechanical synonym replacement that disguises rather than improves weak reasoning.

## Examples

**Handoff:** "Implemented the compatibility path and added contract tests. Targeted tests and the build pass; browser verification was not applicable."

**Review finding:** "High: invalid policy dates are accepted and persisted. Reject them at the API boundary and add a regression test for the malformed payload."

## Sources

See `../../sources/personal-writing.sources.md`.

For longer prose, also read `references/natural-prose.md`.
