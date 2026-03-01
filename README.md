# devloop

Single-source workflow governance for AI-assisted development.
One canonical rule set, multiple delivery adapters.

## Active Documentation

- Core principles: `docs/core/principles.md`
- Problem statement: `docs/core/problem-statement.md`
- Lifecycle process: `docs/process/lifecycle.md`
- Quality gates: `docs/process/quality-gates.md`
- Claude adapter: `docs/adapters/claude/overview.md`
- Codex adapter: `docs/adapters/codex/overview.md`
- Governance status: `docs/governance/status.md`
- Governance decisions: `docs/governance/decisions.md`
- Governance changelog: `docs/governance/changelog.md`

## Delivery Paths

Claude:
- Marketplace plugin delivery remains primary: `claude plugin install xdev@devloop`
- Plugin implementation lives in `plugins/xdev/`

Codex:
- Install shared workflow docs for Codex discovery:
  - `bash scripts/install-codex.sh`

## Repository Layout

```text
docs/
  core/
  process/
  adapters/
    claude/
    codex/
  governance/
plugins/xdev/
scripts/install-codex.sh
```

## Notes

- Legacy material is removed from active onboarding paths.
- Integration policy: preserve task-level commit history; do not squash governance rollout branches.
- Before push/PR automation, verify GitHub auth: `gh auth status -h github.com`.
