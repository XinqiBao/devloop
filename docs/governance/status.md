# Workflow Governance Status

Current state (2026-03-01): active.

## Project Purpose

1. Provide deployable workflow/skill guidance for Claude and Codex.
2. Preserve a built-in self-improvement mechanism for iterative quality gains.

## Canonical Scope

- `docs/core/*`
- `docs/process/*`
- `docs/adapters/*`
- `docs/governance/*`

## Delivery Model

- Claude: plugin delivery via `plugins/xdev/`.
- Codex: docs delivery via `scripts/install-codex.sh` (`~/.agents/skills/devloop`).

## Active Rules

1. one source of truth
2. evidence-before-claim
3. provider-agnostic core/process
4. non-squash integration for governance changes
5. minimal active documentation surface

## Improvement Entry

See `docs/governance/improvement.md` for the iterative improvement loop and source strategy.
