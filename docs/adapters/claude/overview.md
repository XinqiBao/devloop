# Claude Adapter Overview

This adapter maps the platform-agnostic workflow to Claude-specific delivery and runtime behavior.

## Canonical Sources

Use these documents as the rule source:
- `docs/core/principles.md`
- `docs/process/lifecycle.md`
- `docs/process/quality-gates.md`
- `docs/governance/*`

The Claude adapter must reference these sources and must not redefine them.

## Delivery Model

Claude delivery stays plugin-first:

1. Install workflow plugin from repository marketplace:
   - `claude plugin install xdev@devloop`
2. Keep universal user-level guidance in dotfiles-managed `~/.claude/CLAUDE.md`.
3. Keep project-specific constraints in each repository's local `CLAUDE.md` and project `.claude/` settings.

## Responsibility Boundary

- `plugins/xdev/` owns Claude skills/hooks/scripts distribution.
- Dotfiles own cross-project personal policy text.
- Repository `docs/` own canonical workflow governance and process definitions.

## Verification

Run these checks after adapter changes:

```bash
claude plugin list | rg xdev || true
rg -n "quality-first|evidence-before-claim" docs/adapters/claude
rg -n "docs/core|docs/process|docs/governance" docs/adapters/claude
```

Expected:
- xdev plugin remains installable/listed.
- Adapter references shared principles (quality-first, evidence-before-claim).
- Canonical source paths are explicit.
