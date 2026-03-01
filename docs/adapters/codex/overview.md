# Codex Adapter Overview

This adapter maps shared workflow rules into Codex runtime behavior.

## Canonical Inputs

- `docs/core/principles.md`
- `docs/process/lifecycle.md`
- `docs/process/quality-gates.md`
- `docs/governance/*`

## Mapping Rules

- Keep core/process definitions shared and unchanged.
- Use adapter docs only for runtime mapping and setup.
- Keep VCS automation provider-agnostic (host-detected, minimal toolchain).

## Runtime

- Codex runtime instructions come from repository guidance + local environment settings.
- Shared docs are exposed via `~/.agents/skills/devloop`.

## Verification

```bash
rg -n "quality-first|evidence-before-claim" docs/adapters/codex
rg -n "docs/core|docs/process|docs/governance" docs/adapters/codex
```
