# Governance Decisions

Only active decisions are listed here. Historical discussion is kept in git history.

## 1. Single Source

Canonical rules live in `docs/core`, `docs/process`, `docs/adapters`, and `docs/governance`.
No duplicate policy bodies across files.

## 2. Minimal Surface

Active docs must stay concise.
Process artifacts, migration stubs, and exploratory notes are not kept in active paths.

## 3. Adapter Boundary

Adapters map runtime/platform behavior.
Adapters do not redefine core principles or lifecycle semantics.

## 4. Provider-Agnostic VCS

Workflow rules must not be tied to a single git hosting provider.
Tooling should detect environment capabilities (SSH, provider CLI, plain git) and choose the minimal valid path.

## 5. History Integrity

Integration keeps task-level commit history.
Merge strategy for governance changes is non-squash.

## 6. Delivery Split

- Claude delivery: `plugins/xdev/`
- Codex delivery: `scripts/install-codex.sh` + `~/.agents/skills/devloop`

This split is operational only; workflow logic remains shared.
