# Memory model and truth hierarchy

## Truth hierarchy

Prefer evidence in this order:

1. current live, read-only observation of the real system;
2. current source, configuration, tests, and generated manifests;
3. current knowledge-base entries linked to evidence;
4. older diagnostics and historical decisions;
5. manuals and external documentation;
6. chat summaries or model memory.

When sources conflict, do not average them. Record the conflict, identify scope and time, select the current authority with evidence, and mark old material superseded.

## Knowledge status

Label claims as one of:

- `verified`: directly supported by current evidence;
- `observed`: measured in a stated run but not generalized;
- `decision`: intentionally chosen within a stated scope;
- `hypothesis`: plausible but unproven;
- `unknown`: insufficient evidence;
- `superseded`: historically valid or previously believed but no longer authoritative.

Include date, scope/environment, and evidence path for material claims.

## Write routing

- Put the minimal high-value state and navigation links in `PROJECT_MEMORY.md`.
- Put present verified state and immediate next action in `current-state.md`.
- Put mandatory future work blocked now in `deferred-work.md`.
- Put uncertain questions that do not yet have an authorized/required completion plan in `open-questions.md`.
- Put reusable failure knowledge in `debugging-pitfalls.md`.
- Put durable choices in `decisions/`.
- Put raw logs, scripts, plots, snapshots, hashes, and detailed reports in `diagnostics/`.
- Put reusable project procedures in `workflows.md`.
- Move obsolete summaries to `archive/` only after updating inbound links and current authority.

## Prevent drift

- Use stable project-relative paths.
- Record hashes or version identifiers when exact deployed content matters.
- Preserve failed experiments; label why they failed and what they do not prove.
- Distinguish “not observed” from “proven absent”.
- Distinguish a training/test environment from production, competition, or another hardware revision.
- Do not copy raw logs into summary files; link to them.
- Do not duplicate one fact across many files. Keep one authority and link to it.
