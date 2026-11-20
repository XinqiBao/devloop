# Agent Operations

These preferences apply when coding agents operate tools or coordinate other agents. They do not require delegation, a particular product, or a permission mode.

## Edit with the appropriate tool

Prefer native edit or patch tools for ordinary file changes and native Git commands for Git operations. Keep changes targeted and reviewable. Use scripts for genuine transformations or repeated automation when they make the change more reliable; avoid ad hoc whole-file rewriting merely because it is convenient. Parsing, investigation, and probes can still use scripts.

## Report useful progress

Group routine operations without announcing each read, search, edit, or successful check. During longer work, give brief updates on useful findings, changes of direction, blockers, and what the next step will resolve. Avoid repeating plans or reassurance without new information.

Summarize routine successful output. Include relevant failure details or a precise route to them when they affect the next decision. Keep diagnostics and exit status available for verification rather than discarding them for a quieter transcript. At completion, state the result, relevant checks, and unresolved issues without replaying the activity log.

## Delegate bounded outcomes

Consider delegating investigation, implementation, or review when it can be separated into useful outcomes with limited overlap, and run independent tasks in parallel when beneficial. Delegation can keep detailed exploration and execution out of the main conversation so it retains capacity for user intent, cross-task decisions, and integration. Prefer giving an agent continuing responsibility for a component or question over making the coordinator execute every small step. Keep small or tightly coupled work together when handoff and coordination would cost more than they save.

When parallel agent work is authorized and useful, give each worker an outcome, ownership boundary, relevant context, and evidence needed for acceptance. Workers should carry their bounded work through implementation, checks, and ordinary in-scope delivery. Do not make the coordinator perform every edit or commit; commit and push authority still comes from the actual assignment.

Choose the worker's lifecycle for the work. A bounded lookup or independent review can use a short-lived subagent. Iterative implementation, repeated corrections, or a long-running investigation can benefit from a continuing agent conversation that owns the relevant context. A subagent completing does not necessarily discard its context: some runtimes allow follow-up or resumption. Check the actual capability rather than assuming either kind preserves everything.

Reuse a suitable worker for follow-up while its ownership and context still fit. A live conversation can still compact, drift, or become unavailable, so it does not replace shared project records or a useful checkpoint. Use the available orchestration interface; terminal-multiplexer commands and session controls belong in that tool's maintained skill, not copied into this guidance.

The coordinator owns direction, dependencies, shared-resource conflicts, acceptance, and integration. Monitor progress, resolve stalls within existing authority, and revise assignments when evidence changes the plan. Keep task ownership, decisions, and dependencies recoverable in the main conversation or a shared record; let workers retain detailed task context. Ask workers for conclusions, evidence locations, and unresolved issues rather than full activity logs, and inspect underlying evidence where acceptance needs it. A worker's completion message is a claim to review against its output and checks.

## Leave the environment tidy

Own the lifecycle of agents and temporary resources created for the task. Before closing a conversation or moving responsibility, ensure the responsible agent can reach the useful findings, current state, and next steps. Close resources when they are no longer needed; retain a useful checkpoint first when resumption matters.

Before declaring completion, review the workspace and environment changes introduced by the task. Remove disposable probes, scratch files, and debug output; stop owned background processes and sessions; revert temporary configuration changes that are not part of the result. Keep intended deliverables, useful knowledge, and necessary rollback material in clearly scoped locations rather than scattered among temporary artifacts.

Limit cleanup to resources whose ownership and purpose are established. Preserve pre-existing work, other tasks' sessions, and useful recovery material. A clean Git status alone does not account for ignored files or resources outside the checkout; making everything look empty is not a reason to discard useful state.

Respect explicit retention preferences when deciding what is disposable. For local project worktrees, follow [Git layout](git-layout.md).
