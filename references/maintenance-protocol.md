# Continuous maintenance protocol

## Start-of-task read budget

Always read:

1. `PROJECT_MEMORY.md`;
2. `<knowledge-dir>/current-state.md`;
3. `<knowledge-dir>/deferred-work.md`.

When debugging, also read `debugging-pitfalls.md`. Load only relevant ADRs, workflows, open questions, and diagnostic summaries. Search first; do not ingest the entire evidence tree.

## Material update triggers

Update memory when any of these occurs:

- a fact is verified, falsified, or superseded;
- a configuration, deployment, interface, or environment changes;
- a meaningful test succeeds or fails;
- a root cause, workaround, rollback, or prevention gate is established;
- a durable design decision is made or reversed;
- work becomes blocked or unblocked;
- required future measurement/hardware/external coordination is discovered;
- the immediate next action changes;
- the task is interrupted before completion.

Do not update for trivial file reads or commands that teach nothing durable.

## Deferred work: mandatory future completion

Maintain a dedicated ledger for anything that cannot be determined or completed now because of missing hardware, unavailable venue, missing measurement, absent credentials/authority, external dependency, unsafe conditions, unavailable data, or another real blocker.

Every item must include:

- stable ID and title;
- status and priority;
- what cannot be known/done now;
- blocker and why it matters;
- affected components/claims;
- what is allowed and forbidden meanwhile;
- exact unblock condition;
- future data to collect;
- ordered completion/verification steps;
- acceptance evidence required before resolution;
- last-reviewed date.

Keep the item open across context compaction and new sessions. Never infer completion from elapsed time, a software-only simulation, or a loosely related success.

## Debugging pitfalls

Record a pitfall when it is reusable or likely to recur, not for every typo. Include:

- symptom and environment;
- first failing layer/time;
- root cause;
- misleading signals and wrong hypotheses;
- proven fix or workaround;
- prevention check, validator, or reusable tool;
- evidence and applicable scope;
- status (`active`, `mitigated`, `obsolete`).

If a pitfall recurs, update the original entry and strengthen its prevention gate instead of creating disconnected notes.

## Decisions and supersession

Use ADRs for decisions with alternatives or lasting consequences. A replacement ADR must identify what it supersedes and why. Historical evidence remains, but current entry points must route to the new authority.

## Context compaction

Keep `PROJECT_MEMORY.md` small enough to read every task—prefer under roughly 200 lines. Keep current state focused on “now”. Periodically consolidate repetitive run-log material into a dated diagnostic summary and archive obsolete summaries. Preserve evidence paths and decision history.

## Before final response

Reconcile:

- what is now verified;
- what changed;
- what failed and why;
- current deployed/configured state;
- next safe action;
- new or updated deferred items;
- new pitfalls or prevention gates;
- decisions and rollbacks;
- evidence paths.

If no material knowledge changed, do not manufacture an update. If material knowledge changed, do not finalize before persisting it.
