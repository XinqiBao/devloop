# xdev Workflow — Status

> This is the living document for cross-session continuity.
> Read this first when resuming work on the xdev workflow.

## Current Phase: v2 Core Complete

v1 (2026-02-22): Core workflow components installed and functional.
v2 (2026-02-23): Plugin packaging, skills migration, and native hooks done.

### What's deployed

- **xdev plugin** (`xdev@devloop`) — installed from repository marketplace
  - Skills: `/xdev-implement`, `/xdev-draft`, `/xdev-setup`
  - Hooks: commit format validation, sensitive file protection
- **Personal marketplace** — devloop repo serves as `devloop` marketplace
- **Global CLAUDE.md** — Development principles + git convention (via dotfiles)
- **Dotfiles** — `~/git/dotfiles/claude/` + `install-claude.sh`
- **10 plugins installed**: superpowers, pr-review-toolkit, commit-commands,
  context7, security-guidance, hookify, claude-md-management, lua-lsp,
  pyright-lsp, clangd-lsp + xdev@devloop

### Key changes in v2

- Commands → Skills migration (from `~/.claude/commands/` to plugin skills)
- xdev-implement enhanced with parallel agent pattern (explorer/architect/reviewer)
- Native hooks in plugin (not hookify rules) for cross-machine portability
- devloop repo = repository marketplace (`claude plugin install xdev@devloop`)

## Next Actions (Priority Order)

### P2: CLAUDE.md → Rules Modularization
- Consider splitting when CLAUDE.md exceeds 80-100 lines
- Not needed now (54 lines, well-structured)
- `.claude/rules/*.md` are additive and auto-loaded

### P2: Skill prompt quality refinement
- Test each skill on real projects and collect friction points
- Add few-shot examples where Claude misinterprets intent
- Ensure `$ARGUMENTS` handling works correctly
- Consider `allowed-tools` restrictions for each skill

### P3: Hooks expansion
- Auto-format after file edits (PostToolUse, project-specific)
- Stop verification hook (prompt handler for task completion check)
- PreCompact hook for context re-injection after compaction

### P3: Plugin ecosystem review
- Evaluate skill-creator for skill improvement workflow
- Consider ralph-loop for iterative polishing
- Periodic check for new plugins that complement xdev

## Completed Actions

### P0: Install New Plugins (Done 2026-02-23)
- Installed hookify and claude-md-management
- No conflicts with existing plugins

### P1: Commands → Skills Migration (Done 2026-02-23)
- Migrated all 3 commands to SKILL.md format in xdev plugin
- Enhanced xdev-implement with parallel agent pattern
- Old commands removed from `~/.claude/commands/` and dotfiles
- Skills delivered via plugin (`xdev@devloop`)

### P1: Hooks (Done 2026-02-23)
- Created native Python hooks (not hookify rules) for:
  - Conventional commits format validation (PreToolUse/Bash, warn)
  - Sensitive file protection (PreToolUse/Edit|Write, block)
- Hooks packaged in xdev plugin, auto-deployed on install
- Tested with valid and invalid scenarios

### P0: Plugin Packaging (Done 2026-02-23, was P4)
- devloop repo serves as repository marketplace
- `.claude-plugin/marketplace.json` at repo root
- `plugins/xdev/` contains skills + hooks + scripts
- `claude plugin install xdev@devloop` works

## Improvement Directions

Ongoing areas for refinement. Not tasks — directions to explore.

### Skill Prompt Quality
- Are the prompts specific enough? Claude ignores vague instructions
  but follows explicit imperatives.
- Steps that Claude skips or reorders indicate unclear priority.
- Few-shot examples help prevent misinterpretation.

### Global CLAUDE.md Effectiveness
- Current length (~54 lines) is in the optimal range (50-100).
- Best practice: pointers to docs, not embedded snippets.
- Best practice: rules a linter can enforce should be hooks.
- Anti-pattern: rules too general get ignored under context compression.

### Hooks Expansion
- 17 lifecycle events available
- 3 handler types: command, prompt, agent
- Consider: Stop (completion verification), PreCompact (context re-injection)

### Plugin Ecosystem Integration
- See `docs/xdev-workflow/plugin-inventory.md` for full inventory
- Key finding: superpowers + pr-review-toolkit + commit-commands = comprehensive
- hookify kept installed for ad-hoc project-level rules

### Architecture: Two Deployment Layers
- **Plugin layer**: skills, hooks, agents → `claude plugin install xdev@devloop`
- **Dotfiles layer**: CLAUDE.md, rules → `install-claude.sh`
- This two-layer separation is intentional and documented in decisions.md

## Project Nature

This is a general-purpose AI dev workflow — not tied to any specific
project, language, or platform. It should work equally well on any
engineering project.

The workflow evolves through two channels:
1. **Usage feedback**: friction encountered during real use drives fixes.
2. **External research**: community practices, new Claude Code features,
   prompt engineering insights.

The goal is convergence toward a stable, minimal workflow — not feature
accumulation.

## File Map

| File | Purpose |
|------|---------|
| `docs/xdev-workflow/STATUS.md` | This file — current state and direction |
| `docs/xdev-workflow/design.md` | Architecture and component specs (v2) |
| `docs/xdev-workflow/plugin-inventory.md` | Plugin catalog, setup guide, ecosystem analysis |
| `docs/xdev-workflow/decisions.md` | All design decisions with rationale |
| `docs/xdev-workflow/research-notes.md` | Research findings from design phase |
| `docs/xdev-workflow/requirements.md` | Original pain points and constraints |
| `docs/xdev-workflow/history.md` | Design session history (v0–v3) |
| `docs/xdev-workflow/implementation-plan.md` | v1 implementation plan (completed) |
| `docs/plans/2026-02-23-xdev-v2-design.md` | v2 design plan (executed, kept as reference) |
| `.claude-plugin/marketplace.json` | Personal marketplace manifest |
| `plugins/xdev/` | xdev plugin (skills, hooks, scripts) |
| `~/git/dotfiles/claude/` | Dotfiles source (CLAUDE.md) |
| `~/.claude/CLAUDE.md` | Installed global principles |
| `archive/devloop-scheduler/` | Original automated scheduler (archived) |

## Session Prompts

### General improvement session (recommended default):
```
读 docs/xdev-workflow/STATUS.md 了解当前状态。
搜索网上最新的 Claude Code 最佳实践、CLAUDE.md 写法、命令设计等，
结合 Improvement Directions 中的方向，提出具体改进并执行。
```

### Execute a specific task:
```
读 docs/xdev-workflow/STATUS.md 和 docs/plans/2026-02-23-xdev-v2-design.md。
执行 Next Actions 中的 [具体任务名]。
```

### Based on usage feedback:
```
读 docs/xdev-workflow/STATUS.md。我在用 [skill/hook/CLAUDE.md] 时发现
[具体问题]，来改进。
```

### Revisit a design decision:
```
读 docs/xdev-workflow/STATUS.md 和 decisions.md。
我想重新考虑：[具体决策]。原因：[理由]
```
