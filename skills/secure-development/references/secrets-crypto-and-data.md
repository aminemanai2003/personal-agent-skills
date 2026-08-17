# Secrets, Cryptography, And Sensitive Data

## Secrets And Keys

- Store secrets in an approved secret manager or protected runtime configuration, not source, images, client bundles, fixtures, logs, or command history.
- Give each secret an owner, purpose, minimum readers, rotation method, revocation path, and expiry where supported.
- Prefer short-lived workload identity over long-lived static credentials when the platform supports it.
- Treat a pasted, logged, or committed credential as compromised and rotate it.

## Cryptography

- Use maintained libraries and current platform guidance.
- Define the security property first: password verification, confidentiality, integrity, authenticity, or random identifier generation.
- Keep keys separate from ciphertext and restrict key use, not only key read access.
- Use cryptographically secure randomness for secrets and security tokens.
- Never design a custom cipher, signature format, password hashing scheme, or token protocol.

## Passwords And Recovery

- Use a password-hashing function and parameters recommended by current authoritative guidance and supported by the deployment environment.
- Preserve migration paths for existing hashes.
- Protect reset tokens against guessing, replay, reuse, leakage, and indefinite validity.

## Data Minimization

- Collect and retain only data required for the stated purpose.
- Restrict sensitive fields in responses, logs, analytics, backups, support tools, and lower environments.
- Define deletion, retention, export, and breach-response behavior where the data classification requires it.
- Do not assume encryption at rest compensates for excessive application or operator access.
