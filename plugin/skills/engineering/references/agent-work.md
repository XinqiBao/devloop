# Agent Operations

These preferences apply when coding agents operate tools or coordinate other agents. They do not require delegation, a particular product, or a permission mode.

## Edit with the appropriate tool

Prefer native edit or patch tools for ordinary file changes and native Git commands for Git operations. Keep changes targeted and reviewable. Use scripts for genuine transformations or repeated automation when they make the change more reliable; avoid ad hoc whole-file rewriting merely because it is convenient. Parsing, investigation, and probes can still use scripts.

## Delegate bounded outcomes

Consider parallel work when investigation, implementation, or review can be separated into useful outcomes with limited overlap. Prefer giving an agent continuing responsibility for a component or question over making the coordinator execute every small step. Keep tightly coupled decisions together; parallelism has coordination and context costs.

When parallel agent work is authorized and useful, give each worker an outcome, ownership boundary, relevant context, and evidence needed for acceptance. Workers should carry their bounded work through implementation, checks, and ordinary in-scope delivery. Do not make the coordinator perform every edit or commit; commit and push authority still comes from the actual assignment.

Choose the worker's lifecycle for the work. A bounded lookup or independent review can use a short-lived subagent. Iterative implementation, repeated corrections, or a long-running investigation can benefit from a continuing agent conversation that owns the relevant context. A subagent completing does not necessarily discard its context: some runtimes allow follow-up or resumption. Check the actual capability rather than assuming either kind preserves everything.

Reuse a suitable worker for follow-up while its ownership and context still fit. A live conversation can still compact, drift, or become unavailable, so it does not replace shared project records or a useful checkpoint. Use the available orchestration interface; terminal-multiplexer commands and session controls belong in that tool's maintained skill, not copied into this guidance.

The coordinator owns direction, dependencies, shared-resource conflicts, acceptance, and integration. Monitor progress, resolve stalls within existing authority, and revise assignments when evidence changes the plan. A worker's completion message is a claim to review against its output and checks.

Own the lifecycle of agents and temporary resources created for the task. Before closing a conversation or moving responsibility, ensure the responsible agent can reach the useful findings, current state, and next steps. Close resources when they are no longer needed; retain a useful checkpoint first when resumption matters. Do not close another task's sessions or remove existing branches and recovery material merely to make the environment look clean.
