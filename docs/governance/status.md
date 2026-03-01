# Workflow Governance Status

> Living status for the unified workflow governance system.
> This file tracks current state, active entry points, and next improvements.

## Current Phase: Unified Governance Rollout Complete

Completion date: 2026-03-01

The repository now uses a single-source workflow model:

- Canonical rules in `docs/core` and `docs/process`
- Platform adapters in `docs/adapters/claude` and `docs/adapters/codex`
- Governance records in `docs/governance`
- Legacy archive content removed from HEAD

## Deployment State

Claude delivery (unchanged in capability):
- Personal marketplace plugin remains primary: `xdev@devloop`
- Plugin implementation path: `plugins/xdev/`
- Claude adapter docs: `docs/adapters/claude/*`

Codex delivery (newly added):
- Codex adapter docs: `docs/adapters/codex/*`
- Installer script: `scripts/install-codex.sh`
- Installation target: `~/.agents/skills/devloop -> <repo>/docs`

## Canonical Entry Points

Use these as onboarding and maintenance entry points:

- `README.md`
- `CLAUDE.md`
- `docs/core/principles.md`
- `docs/process/lifecycle.md`
- `docs/process/quality-gates.md`
- `docs/adapters/claude/overview.md`
- `docs/adapters/codex/overview.md`
- `docs/governance/decisions.md`
- `docs/governance/changelog.md`

`docs/xdev-workflow/` is migration-pointer space only and not canonical.

## Quality Gates in Effect

1. quality-first: no execution without acceptance criteria.
2. evidence-before-claim: no completion claims without command evidence.
3. context-budget: batch work with explicit checkpoints.
4. parallel-when-safe: parallel only for independent tasks.
5. self-improvement-loop: governance updates after meaningful changes.
6. history-integrity: preserve task-level commits via non-squash integration.

## Next Improvements

1. Validate both adapters on a fresh machine setup run.
2. Add a lightweight link-audit script for docs consistency checks.
3. Periodically review adapter docs to prevent rule drift.
