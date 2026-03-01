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

## GitHub Auth Prerequisites (for push/PR flows)

When Claude workflows include `git push` or `gh pr create`, ensure GitHub auth is valid first:

```bash
gh auth status -h github.com
# if invalid or missing:
gh auth login -h github.com -p https -w
gh auth setup-git
```

If repository remote uses HTTPS, git may prompt for GitHub credentials unless credential helper is configured.
Prefer GitHub CLI auth + credential helper over manual password entry.

## Merge Strategy Requirement

Integration must preserve task-level commits:
- Default: merge commit (non-squash)
- Do not use squash merge for workflow-governance branches
- Record merge method in verification summary

## Verification

Run these checks after adapter changes:

```bash
claude plugin list | rg xdev || true
gh auth status -h github.com
rg -n "quality-first|evidence-before-claim" docs/adapters/claude
rg -n "docs/core|docs/process|docs/governance" docs/adapters/claude
```

Expected:
- xdev plugin remains installable/listed.
- GitHub auth is valid before push/PR actions.
- Adapter references shared principles (quality-first, evidence-before-claim).
- Canonical source paths are explicit.
