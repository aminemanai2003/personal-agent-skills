# Security Review Report Format

Lead with the decision-relevant result:

```markdown
## Security Review: [scope]

### Summary
- Findings: [count by severity]
- Confidence: [high / mixed / limited]
- Scope: [files, diff, runtime, or workflow inspected]

### Findings

#### [SEC-001] [short title] ([severity])
- Location: path/to/file.ext:line
- Confidence: High
- Scenario: [attacker action and required preconditions]
- Evidence: [source-to-sink or policy path]
- Impact: [asset and consequence]
- Remedy: [smallest effective fix]

### Needs Verification
- [Question, missing evidence, location, and safe way to confirm]

### Residual Risk And Gaps
- [Uninspected deployment path, unavailable dependency data, or runtime behavior]
```

Rules:

- Findings come before a general summary of the changed files.
- Include line references and a concrete triggering path.
- Do not paste secrets, exploit payloads that are unnecessary for explanation, or private data.
- If no confirmed findings exist, say: `No high-confidence vulnerabilities identified.` Then state what was inspected and what remains unverified.
