# Trust Boundaries And Threat Framing

Use this reference for features that cross services, tenants, privilege levels, or external systems.

## Build The Model

Record:

- assets whose disclosure, modification, loss, or unavailability matters;
- actors, service identities, administrators, background jobs, and external providers;
- entry points and data stores;
- boundaries where identity, privilege, ownership, or validation changes;
- privileged actions and irreversible effects;
- realistic misuse, abuse, and failure cases.

Use a small data-flow sketch or table when three or more components participate. The model should identify where each authorization and validation decision is owned.

## Questions At Each Boundary

- Who controls this value before it crosses the boundary?
- How is identity authenticated, and what claims are trusted?
- Which object and action must be authorized?
- Can one tenant reference another tenant's object?
- Can the request consume unbounded CPU, memory, storage, bandwidth, or downstream calls?
- What happens if a dependency, policy service, clock, or key store is unavailable?
- What evidence is needed to investigate abuse without logging sensitive data?

## Risk Decisions

Rank concrete scenarios by plausible impact, reachability, and existing controls. Do not manufacture a universal numeric score. Document accepted risk with owner, reason, compensating controls, and revisit condition.
