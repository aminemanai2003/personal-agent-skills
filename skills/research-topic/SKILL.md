---
name: research-topic
description: Carry a substantive research question from framing through source collection, analysis, original synthesis, and expert reporting. Use when the user asks to investigate a technology, method, scientific or actuarial topic, benchmark options, produce an evidence-backed recommendation, or develop a rigorous research paper.
---

# Research Topic

## Purpose

Produce a decision-ready answer whose claims, assumptions, conflicts, and remaining uncertainty can be inspected and reproduced.

## Inputs

- Research question, audience, decision, scope, and freshness requirement.
- Definitions, domain constraints, and excluded topics.
- Available sources, datasets, repositories, and access limitations.
- Expected output form and time budget.

## Scope Boundary

This owns an end-to-end research question and decision-ready synthesis. Use `research-quality` alone for a narrow evidence or claim audit.

## Process

1. Frame the question, decision, definitions, and stopping criteria.
2. List decisive subquestions and what evidence would change the conclusion.
3. Search primary sources first: standards, official documentation, papers, original data, maintained repositories, and release history.
4. Use secondary sources to discover context or conflicts, not as automatic proof.
5. Record a compact source map with provenance, date, scope, quality, license when relevant, and contribution to the answer.
6. Extract facts separately from calculations, assumptions, and interpretation.
7. Compare options on task-relevant dimensions without manufacturing a universal score.
8. Seek disconfirming evidence, reconcile contradictions, and test key claims with a small experiment when practical.
9. For a paper, build a claim-evidence outline and read `references/research-paper-standard.md` before prose drafting.
10. Synthesize an original argument: outcome first, strongest evidence, tradeoffs, limitations, and implications. Do not reproduce the order or phrasing of source summaries.
11. Edit for natural expert prose: remove canned transitions, repetitive framing, generic significance claims, and paragraphs without evidence or reasoning.
12. Audit material claims and citation metadata against sources; stop when new research is unlikely to change the decision or argument.

## Constraints

- Do not collect sources indefinitely after the decision is stable.
- Do not cite popularity, snippets, or generated summaries as primary evidence.
- Do not copy source text beyond necessary quotation and license limits.
- Do not hide unavailable sources or failed reproductions.
- Do not turn separate quantitative dimensions into an arbitrary composite ranking.
- Do not present generated prose, citations, calculations, or interpretations as verified until they have been checked.
- Do not make the paper sound authoritative by hiding methodological uncertainty or required AI-use disclosure.

## Verification

- Every material factual claim maps to an inspectable source.
- Source dates and versions are appropriate for the question.
- Calculations or experiments include enough method detail to reproduce them.
- Conflicts and uncertainty are visible in the synthesis.
- The recommendation follows from the evidence and stated priorities.
- The paper makes a specific contribution, preserves a traceable argument, and reads as one authored work rather than stitched summaries.

## Failure Modes

- A source dump with no decision or synthesis.
- A recommendation driven by stars, branding, or familiarity.
- Overclaiming from one benchmark or dataset.
- Treating lack of primary access as permission to imply certainty.
- Continuing research because no explicit stop condition was set.
- A polished manuscript with no defensible contribution, shallow literature engagement, or generic discussion.

## Examples

**Framework selection:** compare official support, compatibility, maintenance, local fit, and a representative prototype; state which constraint decides the recommendation.

**Model benchmark:** preserve dataset splits, hardware, seeds, metric definitions, uncertainty, and domain limitations; report dimensions separately.

## Sources

See `../../sources/research-topic.sources.md`.

For academic manuscripts, read `references/research-paper-standard.md`.
