# Claude Plugin Stack

This file is the canonical inventory for Claude-side plugin composition and setup.

## Selection Rule

High-coverage or don't install:
- Add a plugin only if it covers substantial recurring needs.
- Avoid low-usage plugin sprawl that adds context and maintenance overhead.

## Current Stack (Baseline)

Workflow core:
- `superpowers@claude-plugins-official`
- `pr-review-toolkit@claude-plugins-official`
- `commit-commands@claude-plugins-official`
- `xdev@devloop` (repository marketplace)

Supporting plugins:
- `context7@claude-plugins-official`
- `security-guidance@claude-plugins-official`
- `hookify@claude-plugins-official`
- `claude-md-management@claude-plugins-official`

Language servers (install by language):
- `pyright-lsp@claude-plugins-official`
- `clangd-lsp@claude-plugins-official`
- `lua-lsp@claude-plugins-official`

## New Machine Setup (Claude)

```bash
claude plugin install superpowers@claude-plugins-official
claude plugin install pr-review-toolkit@claude-plugins-official
claude plugin install commit-commands@claude-plugins-official
claude plugin install context7@claude-plugins-official
claude plugin install security-guidance@claude-plugins-official

claude plugin install hookify@claude-plugins-official
claude plugin install claude-md-management@claude-plugins-official
claude plugin install xdev@devloop

claude plugin install pyright-lsp@claude-plugins-official
claude plugin install clangd-lsp@claude-plugins-official
claude plugin install lua-lsp@claude-plugins-official
```

## Mapping to Shared Workflow

Shared principle mapping:
- quality-first -> enforced via plugin skills + hooks + review flow
- evidence-before-claim -> enforced via execution/verification skill patterns

Shared process mapping:
- clarify/design/plan/execute/verify/improve -> orchestrated by skills and project conventions

See `docs/core/principles.md` and `docs/process/*.md` for canonical definitions.
