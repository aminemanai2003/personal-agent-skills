---
name: research-quality
description: Define evidence standards for technical, product, scientific, actuarial, and quantitative research. Use when gathering sources, comparing tools or methods, making factual claims, designing benchmarks, interpreting data, or reviewing research credibility.
---

# Research Quality

## Purpose

Keep conclusions traceable to credible evidence and proportionate to what the sources or data actually establish.

## Inputs

- The research question, decision, audience, and required freshness.
- Domain definitions and material assumptions.
- Available primary sources, official documentation, datasets, and secondary analysis.
- Reproducibility, privacy, time, and access constraints.

## Scope Boundary

This skill supplies evidence standards for any research. Use `research-topic` when the request is an end-to-end investigation with source collection, comparison, synthesis, and a recommendation.

## Process

1. Frame a falsifiable question and define ambiguous terms.
2. State what evidence would change the answer.
3. Build a source hierarchy: primary evidence first, then credible synthesis, then clearly labeled informal signals.
4. Record source date, provenance, scope, conflicts, and access limitations.
5. Separate extracted facts, calculations, assumptions, and interpretation.
6. For quantitative work, preserve data lineage, method, parameters, units, and uncertainty.
7. Test alternative explanations and look for disconfirming evidence.
8. Synthesize the answer with confidence calibrated to evidence strength.

## Constraints

- Do not cite a search snippet or repository popularity as proof of a claim.
- Do not invent citations, dates, measurements, or source access.
- Do not collapse different metrics into an arbitrary score.
- Do not rank methods universally when results depend on domain, data, or operating constraints.
- Do not hide contradictory evidence or inaccessible primary sources.

## Verification

- Material factual claims map to inspectable sources.
- Sources are current enough and authoritative for the claim.
- Calculations are reproducible with units and assumptions.
- Conflicts, uncertainty, and domain limits are explicit.
- The conclusion answers the framed question without exceeding the evidence.

## Failure Modes

- Collecting many low-signal sources instead of a few decisive ones.
- Treating official marketing as independent validation.
- Reporting benchmark numbers without hardware, data, or method context.
- Confusing absence of evidence with evidence of absence.
- Producing a polished narrative before checking provenance.

## Examples

**Library comparison:** use official compatibility/support data, release activity, issue evidence, and a task-specific prototype; do not choose by stars alone.

**Actuarial benchmark:** report separate error, calibration, stability, and computational measures with dataset assumptions; avoid a universal winner.

## Sources

See `../../sources/research-quality.sources.md`.
