# AI-first initialization

## User interaction

The expected setup is conversational:

1. The user copies this folder anywhere inside the project.
2. The user says, for example: “我在当前工作空间中放了知识库SOP。为了防止上下文过长导致记忆丢失，请识别并启用它，在本工程中长期维护知识库。”
3. The AI locates this `SKILL.md`, inspects the project, installs the runtime skill into `.agents/skills/project-knowledge-base`, creates or adopts the knowledge base, updates `AGENTS.md`, fills initial memory, and audits the result.
4. Future tasks need no trigger phrase. Project `AGENTS.md` supplies persistent read/write instructions.

Command-line installation is a fallback, not the primary user workflow.

## Discover the project root

Prefer the Git root. If no repository exists, use the workspace root the user opened. Never install against a guessed parent directory.

## Discover existing memory

Before scaffolding, search for:

- `PROJECT_MEMORY.md`, `MEMORY.md`, `CONTEXT.md`, or an equivalent entry point;
- `knowledge-base/`, `docs/`, `decisions/`, ADRs, runbooks, and diagnostic/evidence directories;
- `AGENTS.md` rules that name authoritative project documentation;
- status, backlog, open-question, incident, postmortem, troubleshooting, and lessons-learned files.

Adopt an existing system when it can represent current state, deferred work, decisions, pitfalls, and evidence. Add missing lanes non-destructively. Do not create `.codex/project-knowledge` merely because another name differs.

## Bootstrap

With Python 3.8+ available:

```text
python <copied-sop>/scripts/bootstrap_project_knowledge.py --project-root <project-root>
```

For an existing non-default knowledge directory:

```text
python <copied-sop>/scripts/bootstrap_project_knowledge.py --project-root <project-root> --knowledge-dir <relative-path>
```

The script copies only runtime Skill files, adds or refreshes a bounded `AGENTS.md` block, and creates missing templates without overwriting project content.

If Python is unavailable, copy the same assets and managed block with available file tools. Keep paths project-relative and UTF-8.

## Build real initial memory

Scaffolding is not initialization. After creating files:

1. Inventory project purpose, architecture, active environments, build/test/deploy entry points, authoritative configs, and current task.
2. Use source files and live read-only checks as primary evidence.
3. Extract existing durable decisions and label obsolete ones as superseded.
4. Find all explicitly postponed, hardware-dependent, venue-dependent, externally blocked, or measurement-dependent work and put it in `deferred-work.md`.
5. Mine previous debugging records for recurring pitfalls. Record symptom, root cause, misleading interpretation, proven fix, prevention gate, and evidence.
6. Write a compact `PROJECT_MEMORY.md` that routes future agents to details rather than duplicating them.

## Verify persistence

Confirm:

- `.agents/skills/project-knowledge-base/SKILL.md` exists;
- the project `AGENTS.md` contains one managed knowledge block;
- `PROJECT_MEMORY.md` and all required knowledge lanes exist;
- entry documents contain project facts rather than untouched placeholders;
- a future agent can find the current objective, next action, blockers, and pitfalls without reading old chat.

Restart Codex if a newly installed Skill is not discovered immediately.
