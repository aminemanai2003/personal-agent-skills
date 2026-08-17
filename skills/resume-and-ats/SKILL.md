---
name: resume-and-ats
description: Create, revise, audit, or tailor a resume or CV for a specific role while preserving factual accuracy and machine-readable structure. Use when asked about ATS compatibility, resume keywords, experience bullets, achievement extraction, section order, role-specific tailoring, recruiter readability, or consistency between a job description and a resume; do not use for LinkedIn-only work or the broader application strategy.
---

# Resume And ATS

## Purpose

Produce a truthful resume that is easy to parse, quick for a recruiter to evaluate, and visibly aligned with the target role without keyword stuffing or invented impact.

## Inputs

- Current resume or verified career history, projects, education, skills, and dates.
- Target job description, role family, seniority, geography, and language.
- Output constraints such as page count, file format, template, or application portal.
- Evidence for outcomes: numbers, scope, users, latency, revenue, quality, ownership, or other defensible signals.

## Scope Boundary

Use `professional-profile` for LinkedIn or portfolio positioning and `job-search-and-applications` for role prioritization, outreach, and application tracking. If editing a `.docx` or PDF artifact, combine this skill with the relevant document skill.

## Process

1. Extract the role's actual requirements into must-have capabilities, preferred evidence, domain language, and likely screening terms. Separate explicit requirements from inference.
2. Build a fact inventory from the candidate material. Mark each statement as verified, needs confirmation, or unavailable; never fill gaps with plausible claims.
3. Choose a clear section order based on the candidate's strongest relevant evidence. Keep standard headings and a simple reading order unless the target explicitly requires another format.
4. Tailor the summary, skills, and experience selection to the role. Use the employer's accurate terminology where it matches real experience; preserve natural language and synonyms where useful.
5. Rewrite bullets around action, technical or business context, and result. Use metrics only when supplied or derivable from evidence; otherwise describe concrete scope, complexity, ownership, or delivered behavior.
6. Remove unsupported claims, decorative filler, repeated skills, obsolete details, and content that consumes space without helping the target decision.
7. Check parsing safety and recruiter scan quality with `references/resume-workflow.md`. Treat ATS behavior as vendor-dependent; do not promise a score, ranking, or interview outcome.
8. Return the revised resume or exact edits plus an evidence-gap list for claims the candidate could strengthen.

## Constraints

- Do not invent employers, dates, degrees, titles, technologies, responsibilities, metrics, awards, publications, or proficiency.
- Do not change a job title in a way that misrepresents the official role; a clarifying functional label may be added transparently.
- Do not force every job-description phrase into the resume or hide keywords in formatting.
- Do not claim a universal ATS score, fixed match threshold, or guaranteed parsing behavior.
- Do not require quantified bullets when truthful qualitative evidence is stronger or numbers are unavailable.
- Preserve factual consistency across versions and flag conflicting dates or claims.

## Verification

- Every material claim maps to candidate-provided or otherwise verified evidence.
- The most relevant requirements have visible evidence, not merely keyword mentions.
- Headings, chronology, contact information, and dates are consistent and easy to parse.
- Bullets distinguish action, context, and outcome without vague self-praise.
- The final version remains readable to a human and does not contain keyword blocks, hidden text, placeholders, or unsupported scores.
- Any missing evidence or uncertain statement is explicitly listed for confirmation.

## Failure Modes

- Copying the job description until the resume no longer sounds like the candidate.
- Fabricating a percentage because every bullet is assumed to need a metric.
- Optimizing for an imagined ATS formula while weakening recruiter readability.
- Adding every technology ever used instead of showing relevant applied evidence.
- Reformatting into columns, icons, or text boxes without checking the destination parser.

## Examples

**Tailoring:** compare a backend internship description with verified project history, foreground matching API and database evidence, and list missing proof without inventing production scale.

**Achievement extraction:** turn notes about reducing a slow manual workflow into a concrete bullet after confirming the baseline, action, scope, and measured or observed result.

## Sources

See `../../sources/resume-and-ats.sources.md`.

Load `references/resume-workflow.md` when drafting, tailoring, or auditing a full resume.
