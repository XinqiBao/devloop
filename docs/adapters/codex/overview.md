# Codex Adapter Overview

This adapter maps canonical workflow rules into Codex-compatible session behavior.

## Canonical Sources

Codex must consume shared rules from:
- `docs/core/principles.md`
- `docs/process/lifecycle.md`
- `docs/process/quality-gates.md`
- `docs/governance/*`

Codex adapter docs describe mapping and install mechanics only.

## Mapping Rules

- quality-first: no implementation claim without quality gates.
- evidence-before-claim: every task report includes command evidence.
- context-budget: batch execution and concise handoff between sessions.
- parallel-when-safe: parallel reads/checks only for independent tasks.
- self-improvement-loop: record process improvements in governance docs.

## Runtime Mapping

- Codex runtime instructions live in repository `AGENTS.md` and local adapter docs.
- Skills are discovered via `~/.agents/skills` and referenced by runtime instructions.
- This adapter does not fork process rules; it points to shared core/process docs.

## Verification

```bash
rg -n "quality-first|evidence-before-claim" docs/adapters/codex
rg -n "docs/core|docs/process|docs/governance" docs/adapters/codex
```

Expected: adapter text references shared rules and source paths explicitly.
