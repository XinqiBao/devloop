---
name: agents
description: "Apply the owner's preferences when deciding whether or how to split engineering work across agents, delegate tasks, run independent work in parallel, or manage worker conversations, context, lifecycle, and integration. Small or tightly coupled tasks may stay together."
---

# Agent Coordination

These are the owner's coordination preferences. They do not require delegation, a particular agent product, or a permission mode. Apply them within current task intent, project requirements, and available capabilities.

## Delegate bounded outcomes

Consider delegating investigation, implementation, or review when it can be separated into useful outcomes with limited overlap, and run independent tasks in parallel when beneficial. Delegation can keep detailed exploration and execution out of the main conversation so it retains capacity for user intent, cross-task decisions, and integration. Prefer giving an agent continuing responsibility for a component or question over making the coordinator execute every small step. Keep small or tightly coupled work together when handoff and coordination would cost more than they save.

When parallel agent work is authorized and useful, give each worker an outcome, ownership boundary, relevant context, and evidence needed for acceptance. Workers should carry their bounded work through implementation, checks, and ordinary in-scope delivery. Do not make the coordinator perform every edit or commit; commit and push authority still comes from the actual assignment.

## Match conversations to ownership

Choose the worker's lifecycle for the work. A bounded lookup or independent review can use a short-lived subagent. Iterative implementation, repeated corrections, or a long-running investigation can benefit from a continuing agent conversation that owns the relevant context. A subagent completing does not necessarily discard its context: some runtimes allow follow-up or resumption. Check the actual capability rather than assuming either kind preserves everything.

Reuse a suitable worker for follow-up while its ownership and context still fit. A live conversation can still compact, drift, or become unavailable, so it does not replace shared project records or a useful checkpoint. Use the available orchestration interface; terminal-multiplexer commands and session controls belong in that tool's maintained skill, not copied into this guidance.

## Coordinate acceptance and closeout

The coordinator owns direction, dependencies, shared-resource conflicts, acceptance, and integration. Monitor progress, resolve stalls within existing authority, and revise assignments when evidence changes the plan. Keep task ownership, decisions, and dependencies recoverable in the main conversation or a shared record; let workers retain detailed task context. Ask workers for conclusions, evidence locations, and unresolved issues rather than full activity logs, and inspect underlying evidence where acceptance needs it. A worker's completion message is a claim to review against its output and checks.

Own the lifecycle of agents created for the task. Before closing a conversation or moving responsibility, ensure the responsible agent can reach the useful findings, current state, and next steps. Close workers when no longer needed; retain a useful checkpoint first when resumption matters. Use [knowledge](../knowledge/SKILL.md) when deciding where shared findings or handoff state belong.
