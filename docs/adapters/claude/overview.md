# Claude Adapter Overview

This adapter maps shared workflow docs to Claude runtime usage.

## Canonical Inputs

- `docs/core/principles.md`
- `docs/process/lifecycle.md`
- `docs/process/quality-gates.md`
- `docs/governance/*`

## Delivery

- Install plugin: `claude plugin install xdev@devloop`
- Plugin source: `plugins/xdev/`

## Runtime Boundary

- User-level guidance remains in user-level Claude config.
- Repository workflow rules remain in this repository's docs.
- Adapter text must reference shared rules, not fork them.

## VCS Preflight (Provider-Agnostic)

Before push/PR automation, verify:

```bash
git remote -v
command -v gh >/dev/null || command -v glab >/dev/null || true
```

Use the simplest valid path in current environment:
1. SSH + `git push` when available
2. Provider CLI (`gh`/`glab`) when needed for PR/MR creation
3. Plain git workflow when provider CLI is unavailable

## Verification

```bash
claude plugin list | rg xdev || true
rg -n "quality-first|evidence-before-claim" docs/adapters/claude
rg -n "docs/core|docs/process|docs/governance" docs/adapters/claude
```
