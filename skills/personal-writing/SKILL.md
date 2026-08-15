---
name: personal-writing
description: Write concise, factual, natural project communication in Amine's preferred style. Use when drafting final handoffs, READMEs, documentation, issues, pull requests, review comments, research summaries, decisions, or user-facing technical explanations.
---

# Personal Writing

## Purpose

Communicate the useful outcome, evidence, limitations, and next decision without marketing language or process theater.

## Inputs

- Audience, channel, and action the reader should take.
- Verified facts, source material, and relevant uncertainty.
- Repository terminology and any required template.
- The desired level of technical depth.

## Process

1. Identify the reader's first question and lead with its answer.
2. Separate verified facts from interpretation, recommendation, and unresolved risk.
3. Use the repository's vocabulary and concrete nouns.
4. Prefer active voice, plain verbs, and sentences that each do one job.
5. Include reasoning only where it helps evaluate a decision or reproduce a result.
6. State verification, skipped checks, limitations, and authority boundaries directly.
7. Remove filler, generic praise, repetition, inflated certainty, and meta-commentary.
8. Format only enough to make the content scannable in its channel.

## Constraints

- Do not begin with praise or a recap the reader already knows.
- Do not turn limitations into vague disclaimers.
- Do not use marketing claims, fake urgency, or unsupported superlatives.
- Do not bury critical findings below a long summary.
- Do not force one template across chat, docs, issues, and PR reviews.

## Verification

- The first paragraph answers the reader's main question.
- Every material claim is verified or clearly qualified.
- Actions, owners, and unresolved decisions are explicit when applicable.
- Tone matches the audience and avoids filler.
- The text can be shortened no further without losing useful meaning.

## Failure Modes

- A polished narrative that hides the actual result.
- Over-formatting a simple handoff.
- Terse comments that state a problem but not its impact or remedy.
- Long explanations of routine implementation steps.
- Claiming certainty where source or test coverage is incomplete.

## Examples

**Handoff:** "Implemented the compatibility path and added contract tests. Targeted tests and the build pass; browser verification was not applicable."

**Review finding:** "High: invalid policy dates are accepted and persisted. Reject them at the API boundary and add a regression test for the malformed payload."

## Sources

See `../../sources/personal-writing.sources.md`.
