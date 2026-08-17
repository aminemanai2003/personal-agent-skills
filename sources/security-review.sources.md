# Security Review Sources

Primary standards and guidance:

- OWASP Application Security Verification Standard (ASVS): https://owasp.org/www-project-application-security-verification-standard/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- NIST SP 800-218 SSDF Version 1.1: https://csrc.nist.gov/pubs/sp/800/218/final

Public skill comparison:

- `getsentry/skills`, `security-review`, commit `24fdb833b9e67670a027e3b482189100a69ff7f9` (Apache-2.0 repository; its OWASP-derived skill reference is separately marked CC BY-SA 4.0). Useful principles: investigate attacker control, framework mitigation, and data flow before reporting; load category guidance conditionally.
- `github/awesome-copilot`, `skills/security-review`, commit `406c31f848e641e9ccb33277cb03b51b015c27c7` (MIT). Useful principles: scope resolution, dependency and secret inventory, cross-file review, self-verification, and review-only patch handling.

Adaptation boundary:

- Rewrote the workflow and report format in original language; no source body or reference files were copied.
- Narrowed the output to evidence-backed findings and explicit needs-verification questions, matching this repository's review-first conventions.
- Added a compact matrix instead of a large static checklist so irrelevant security categories do not load for every review.

Original implementation:

- Trigger boundary, confidence gate, severity reasoning, secret-reporting rule, and integration with `review-code` and `secure-development` are original.
