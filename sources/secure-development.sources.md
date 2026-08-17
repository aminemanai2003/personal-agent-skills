# Secure Development Sources

Primary standards and guidance:

- OWASP Application Security Verification Standard (ASVS), official project page inspected 2026-08-17: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Cheat Sheet Series, including Authentication, Session Management, Secrets Management, Cryptographic Storage, and REST Security, official pages inspected 2026-08-17: https://cheatsheetseries.owasp.org/
- NIST SP 800-218, Secure Software Development Framework (SSDF) Version 1.1, official page inspected 2026-08-17: https://csrc.nist.gov/pubs/sp/800/218/final

Public skill comparison:

- `oakoss/agent-skills`, `application-security`, commit `85e3a3919d9e0ec7f7302a5143ec4b3e66f5f6ad` (skill declares MIT; repository metadata did not expose a root license during inspection). Useful breadth: threat modeling, API, data, supply-chain, and operational categories.
- `getsentry/skills`, `security-review`, commit `24fdb833b9e67670a027e3b482189100a69ff7f9` (Apache-2.0 repository; its OWASP-derived reference material is CC BY-SA 4.0). Useful distinction: trace attacker control and framework mitigation before treating a pattern as vulnerable.

Adaptation boundary:

- Wrote original workflow and references from primary standards and general security principles; no OWASP-derived Sentry reference body was copied.
- Rejected universal JWT, cookie, password, algorithm, token-lifetime, rate-limit, and compliance prescriptions that require system-specific current guidance.
- Split implementation from review so implicit triggers do not turn every coding task into a security audit.
- Added explicit authorization, local-storage, secret exposure, supply-chain, operational, privacy, and residual-risk boundaries.

Original implementation:

- The trigger description, four conditional references, verification contract, and integration with this repository's build and review skills are original.
