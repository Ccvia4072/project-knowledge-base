# Project knowledge base

This directory contains durable, model-readable engineering memory. It is not a transcript and not a dump of raw logs.

## Fast routing

- `current-state.md` — verified present state, active objective, configuration, and next action.
- `deferred-work.md` — mandatory future work blocked or unknowable now.
- `debugging-pitfalls.md` — recurring traps, root causes, fixes, and prevention gates.
- `open-questions.md` — unresolved questions and labeled hypotheses.
- `workflows.md` — reusable project procedures and SOPs.
- `terminology.md` — canonical names and ambiguity prevention.
- `decisions/` — durable ADRs and supersession history.
- `diagnostics/` — reproducible evidence, raw logs, scripts, manifests, hashes, and detailed reports.
- `archive/` — superseded summaries retained for history.

## Truth rules

1. Prefer live observation and current source/configuration over older summaries.
2. Label verified facts, observations, decisions, hypotheses, unknowns, and superseded claims distinctly.
3. Link material claims to project-relative evidence and include scope/date.
4. Never let an old environment, map, hardware revision, or test profile silently contaminate the current one.
5. Keep entry files concise and link to diagnostics instead of copying raw logs.
6. Preserve failed experiments and state what they do not prove.

## Maintenance

The project `AGENTS.md` requires every future AI to read the compact entry files and update this knowledge base after material changes. `PROJECT_MEMORY.md` is the always-read routing layer and should remain compact.
