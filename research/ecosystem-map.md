# Ecosystem Map

Research date: 2026-08-15

This map records principles adapted from public projects. It is not a source-code import list. Repository-level license data can be incomplete, so every implementation must verify the relevant file's license before redistributing text or assets.

| Repository | Maintainer | Adoption/activity signal | License signal | Useful principles | Adaptation boundary | Candidate contribution |
| --- | --- | --- | --- | --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic | 169k stars; pushed 2026-08-13 | Repo license not detected; some skills declare terms | Progressive disclosure, `SKILL.md` anatomy, eval loop, concise trigger descriptions | Reimplement concepts; do not copy skill bodies or assets; verify per-skill terms | Skill authoring, frontend, document workflows |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Anthropic | 141k stars; pushed 2026-08-14 | Repo license not detected | Project context, terminal-native workflow, tool-aware instructions | Treat product behavior as reference; no proprietary text | Codex/Claude adapter notes |
| [openai/codex](https://github.com/openai/codex) | OpenAI | 106k stars; pushed 2026-08-15 | Apache-2.0 | Repository-local `AGENTS.md`, inspect-first execution, terminal verification | Use public conventions; preserve platform/system precedence | Codex adapter |
| [openai/plugins](https://github.com/openai/plugins) | OpenAI | 5k stars; pushed 2026-07-14 | Repo license not detected | Thin packaging and tool integration boundaries | Keep core portable; avoid assuming one host | Packaging adapters |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | GitHub/community | 38k stars; pushed 2026-08-14 | MIT | Discoverable instruction and agent configuration patterns | Curate, do not copy community entries wholesale | Repository orientation |
| [obra/superpowers](https://github.com/obra/superpowers) | Jesse Michael Han | 272k stars; pushed 2026-08-13 | MIT | Root-cause debugging, explicit plans, verification-before-completion, reviewable change sizing | Adapt workflow logic to this profile; retain local scope and precedence | Build feature, review code, debugging |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani | 87k stars; pushed 2026-08-14 | MIT | Context hierarchy, doubt-driven development, source-driven research, ADRs | Rework examples and priorities for Amine's projects | Project start, research, documentation |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock | 218k stars; pushed 2026-08-13 | MIT | Practical engineering skill organization and reusable TypeScript guidance | Borrow structure and principles only | Code quality, review code |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel Labs | 30k stars; pushed 2026-08-15 | Per-package terms; verify before reuse | Focused performance rules, composition, framework-specific references | Keep React rules optional and scoped; no universal frontend claims | Frontend quality |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | Vercel Labs | 774 stars; pushed 2026-04-06 | MIT | Concrete web UI review checks and interaction states | Combine with accessibility and personal UI preferences | Review UI |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP community | High-adoption reference collection | Per-server licenses vary | Tool boundary and integration patterns | Treat each server as untrusted external code; verify terms | Tool adapters |
| [microsoft/playwright](https://github.com/microsoft/playwright) | Microsoft | Mature browser automation project | Verify current license in repo | Deterministic browser verification and screenshots | Use only when browser checks are warranted | Visual UX review |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | Deque | 7k stars; pushed 2026-08-13 | MPL-2.0 | Automated accessibility checks as a complement to human review | Do not treat automated passes as accessibility proof | Review UI |
| [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) | OWASP | 33k stars; pushed 2026-08-14 | CC-BY-SA-4.0 | Security review checklists and threat-aware boundaries | Adapt facts with attribution; do not copy prose or imply certification | Code quality, security |
| [conventional-commits/conventionalcommits.org](https://github.com/conventional-commits/conventionalcommits.org) | Community | 9k stars; pushed 2026-03-11 | MIT | Machine-readable, scoped commit conventions | Apply only where project/team accepts the convention | GitHub workflow |
| [adr/madr](https://github.com/adr/madr) | MADR community | 2k stars; pushed 2026-08-03 | License not detected | Lightweight decision records with explicit status and consequences | Use a small local template; verify any copied template terms | Decision making |

## Cross-source synthesis

- Most useful skills are procedural: they define inputs, checkpoints, and evidence.
- Descriptions do the triggering work; bodies should remain scoped and progressively disclosed.
- Verification and review should be first-class phases, not an optional closing sentence.
- Framework-specific guidance belongs behind a trigger or reference file, not in the global profile.
- The main conflict risk is over-triggering: anti-slop, review, and completion rules must compose without forcing every task through every checklist.

