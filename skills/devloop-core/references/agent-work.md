# Agent Operations

These preferences apply when coding agents operate tools or coordinate other agents. They do not require delegation, a particular product, or a permission mode.

## Edit with the appropriate tool

Prefer native edit or patch tools for ordinary file changes and native Git commands for Git operations. Keep changes targeted and reviewable. Use scripts for genuine transformations or repeated automation when they make the change more reliable; avoid ad hoc whole-file rewriting merely because it is convenient. Parsing, investigation, and probes can still use scripts.

## Delegate bounded outcomes

When parallel agent work is authorized and useful, give each worker an outcome, ownership boundary, relevant context, and evidence needed for acceptance. Workers should carry their bounded work through implementation, checks, and ordinary in-scope delivery. Do not make the coordinator perform every edit or commit; commit and push authority still comes from the actual assignment.

The coordinator owns direction, dependencies, shared-resource conflicts, acceptance, and integration. Monitor progress, resolve stalls within existing authority, and revise assignments when evidence changes the plan. A worker's completion message is a claim to review against its output and checks.

Own the lifecycle of agents and temporary resources created for the task. Before closing a conversation or moving responsibility, ensure the responsible agent can reach the useful findings, current state, and next steps. Close resources when they are no longer needed; retain a useful checkpoint first when resumption matters. Do not close another task's sessions or remove existing branches and recovery material merely to make the environment look clean.
