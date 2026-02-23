# xdev v2 Improvement Design

> Brainstormed and validated 2026-02-23. Execute incrementally.

## Strategy

Gradual improvement: perfect locally in dotfiles, then convert to plugin
when stable. Each section below is an independent work item.

## 1. Plugin Inventory (Execute Now)

Create `docs/xdev-workflow/plugin-inventory.md` documenting all installed
plugins, evaluated plugins, redundancy analysis, and installation steps
for new machines. See that file for details.

## 2. Commands → Skills Migration (Execute Later)

Migrate `/xdev-implement`, `/xdev-draft`, `/xdev-setup` from
`~/.claude/commands/` to `~/.claude/skills/` format.

### Target structure

```
~/.claude/skills/
  xdev-implement/
    SKILL.md          # Converted from commands/xdev-implement.md
  xdev-draft/
    SKILL.md          # Converted from commands/xdev-draft.md
  xdev-setup/
    SKILL.md          # Converted from commands/xdev-setup.md
    templates/        # CLAUDE.md templates, health check references
```

### Benefits

- Sub-directories for reference docs (templates, checklists)
- Frontmatter for invocation control (auto vs user-only)
- Cross-platform compatibility (Claude.ai, Claude Desktop)
- Unified with superpowers skill system

### Migration steps

1. Install skill-creator plugin (optional, for validation)
2. Convert each command to SKILL.md with frontmatter
3. Add sub-files where beneficial (e.g., CLAUDE.md template for setup)
4. Test each skill in real projects
5. Remove old commands/ files after validation

### Tools

- `superpowers:writing-skills` — built-in skill for creating skills
- `skill-creator` plugin — optional, for guided creation

## 3. CLAUDE.md + Rules Architecture (Record, Don't Execute)

### Current state

Global `~/.claude/CLAUDE.md` is 54 lines — within optimal range (50-100).
Well-structured with Development Principles + Git Convention.

### Architecture decision

**Plugin ships "process and tools" (skills, hooks, agents).**
**CLAUDE.md ships "principles and constraints" (via dotfiles).**

Two-layer separation:
- Plugin: `claude plugin install xdev` → skills, hooks, agents
- Dotfiles: `install-claude.sh` → CLAUDE.md, rules/

### Rules modularization trigger

Consider splitting CLAUDE.md into `~/.claude/rules/*.md` when:
- CLAUDE.md exceeds 80-100 lines
- Multiple rule sources need to coexist (e.g., team rules + personal rules)
- Specific rules need project-level overrides

Rules files are additive and auto-loaded. No conflict risk.

### Not recommended now

Current 54-line CLAUDE.md is lean and effective. Splitting would be
over-engineering at this stage.

## 4. Hooks Strengthening (Execute Later)

### Hook 1: Commit format validation (HIGH priority)

- Event: `PreToolUse` on `Bash(git commit)`
- Type: `command`
- Purpose: Enforce conventional commits format as a hard gate
- Blocks non-compliant commits before they happen
- Implements the "block at commit, not write" strategy from STATUS.md

### Hook 2: Auto-format on edit (MEDIUM priority)

- Event: `PostToolUse` on `Edit`
- Type: `command`
- Purpose: Auto-run project formatter after file edits
- Detect formatter from project config (.prettierrc, pyproject.toml, etc.)
- "Never send an LLM to do a linter's job"

### Hook 3: Sensitive file protection (MEDIUM priority)

- Event: `PreToolUse` on `Edit`
- Matcher: file pattern `*.env|*credentials*|*secret*`
- Type: `command`
- Purpose: Block editing sensitive files, warn user

### Hook 4: Stop verification (EXPLORATORY)

- Event: `Stop`
- Type: `prompt`
- Purpose: LLM self-check that all requested tasks are truly complete
- Uses new prompt-type hook handler for judgment-based verification

### Implementation notes

- Hooks go in `.claude/settings.local.json` (per-machine) or
  `hooks/hooks.json` (when packaged as plugin)
- Start with Hook 1 (commit format) — highest value, lowest risk
- Test each hook on a real project before adding the next

## 5. Plugin Packaging (Future)

When all the above are stable (validated on 3-4 projects):

1. Use `plugin-dev` plugin for scaffolding and validation
2. Create plugin structure with skills, hooks, agents
3. CLAUDE.md stays in dotfiles repo (not in plugin)
4. Publish to repository marketplace for cross-machine install

### Plugin structure target

```
xdev-plugin/
  .claude-plugin/
    plugin.json
  skills/
    xdev-implement/SKILL.md
    xdev-draft/SKILL.md
    xdev-setup/SKILL.md + templates/
  hooks/
    hooks.json        # commit format, auto-format, file protection
  agents/             # (if needed)
```

## Execution Priority

| Item | Priority | When |
|------|----------|------|
| Plugin inventory doc | P0 | This session |
| STATUS.md update | P0 | This session |
| Commands → Skills migration | P1 | Next session |
| Hooks: commit format | P1 | Next session |
| Hooks: auto-format | P2 | After commit hook works |
| Hooks: sensitive files | P2 | After commit hook works |
| Hooks: stop verification | P3 | Exploratory |
| CLAUDE.md modularization | P3 | When CLAUDE.md grows |
| Plugin packaging | P4 | When workflow is stable |
