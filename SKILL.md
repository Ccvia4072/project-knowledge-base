---
name: project-knowledge-base
description: Initialize, recover, audit, and continuously maintain a durable project knowledge base. Use when the user says “启用知识库SOP”, asks to prevent memory loss from long context, requests long-term project memory, asks an AI to initialize a copied knowledge-base SOP, resumes an old project, or needs project facts, decisions, unresolved hardware-dependent work, debugging pitfalls, and evidence preserved across tasks and context compaction.
---

# Project Knowledge Base

Treat project memory as maintained engineering state, not a chat transcript.

## Initialize once

When the user asks to enable this SOP:

1. Read [references/initialization.md](references/initialization.md) completely.
2. Locate the project root and inspect `AGENTS.md`, existing memory/index files, documentation, decisions, issue notes, diagnostics, and source control before creating anything.
3. Adopt and upgrade an existing model-readable knowledge base instead of creating a competing one. Default to root `PROJECT_MEMORY.md` plus `knowledge-base/` only when no established equivalent exists.
4. Run `scripts/bootstrap_project_knowledge.py --project-root <root>` with the discovered relative knowledge directory, or perform the same operations manually if Python is unavailable.
5. Inspect the actual project and replace template placeholders with verified, source-linked content. Do not let an empty scaffold masquerade as initialized memory.
6. Run `scripts/audit_project_knowledge.py --project-root <root>` and repair every structural error.
7. Confirm that the managed project `AGENTS.md` block makes future agents read and maintain the knowledge base without another user trigger.

## Maintain on every task

The managed `AGENTS.md` instructions activate maintenance after the one-time setup.

1. At task start, read `PROJECT_MEMORY.md`, current state, and deferred work. Read debugging pitfalls before debugging or repeating a failed operation. Load decisions and diagnostics only as relevant.
2. Apply the truth hierarchy and update rules in [references/memory-model.md](references/memory-model.md).
3. Record raw logs and reproducible artifacts under diagnostics; keep entry files concise and link to evidence.
4. Update memory immediately after a material fact, decision, experiment, root cause, workaround, blocker, deployment, rollback, or supersession—not after every trivial command.
5. Before finalizing, reconcile current state, deferred work, pitfalls, decisions, and evidence. Never declare completion while a required deferred item remains unresolved.

## Mandatory memory lanes

Keep these distinct:

- verified current facts and immediate next action;
- durable decisions with rationale and supersession links;
- reproducible diagnostic evidence;
- open questions and labeled hypotheses;
- debugging pitfalls with prevention gates;
- a dedicated deferred-work ledger for anything impossible to determine or complete now but mandatory later.

For the required fields and compaction rules, read [references/maintenance-protocol.md](references/maintenance-protocol.md).

## Recovery behavior

When resuming after context compaction, task interruption, or a new AI session:

1. Reconstruct state from the knowledge base and live project evidence, not chat memory.
2. State the last verified position, unresolved blockers, stale assumptions, and next safe action.
3. Continue from the first incomplete step; do not restart the investigation unless evidence is missing or contradictory.

## Boundaries

- Never store passwords, tokens, private keys, or sensitive raw data.
- Never copy large logs into entry documents.
- Never silently replace a fact when the environment changes; mark it superseded and preserve the evidence trail.
- Never turn an inference into a verified fact.
- Never resolve deferred work without the specified acceptance evidence.
