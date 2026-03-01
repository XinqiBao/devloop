# devloop

This repository defines workflow governance, not application code.
Use canonical docs as the only authority.

## Canonical Sources

- `docs/core/principles.md`
- `docs/core/problem-statement.md`
- `docs/process/lifecycle.md`
- `docs/process/quality-gates.md`
- `docs/adapters/claude/overview.md`
- `docs/adapters/codex/overview.md`
- `docs/governance/status.md`
- `docs/governance/decisions.md`
- `docs/governance/changelog.md`

## Execution Rules

- Prefer updating canonical docs over duplicating policy text.
- Keep adapter docs as mappings; do not redefine core/process rules.
- Require verification evidence before any completion claim.

## Implementation Areas

- Claude plugin delivery: `plugins/xdev/`
- Codex setup/install path: `scripts/install-codex.sh`

