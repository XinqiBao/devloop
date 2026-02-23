# xdev v2 Improvement Design

> Brainstormed and validated 2026-02-23. Execute incrementally.
> This document is self-contained — includes exact formats and schemas
> needed for implementation without further research.

## Strategy

Gradual improvement: perfect locally in dotfiles, then convert to plugin
when stable. Each section below is an independent work item.

## 1. Plugin Inventory (Done)

Created `docs/xdev-workflow/plugin-inventory.md`. Documents installed
plugins, evaluated plugins, redundancy analysis, installation steps,
and the plugin selection principle (high-coverage or don't install).

## 2. Commands → Skills Migration (P1)

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

### SKILL.md format reference

Each SKILL.md has YAML frontmatter + markdown body:

```yaml
---
name: xdev-implement               # lowercase, hyphens only, max 64 chars
description: >
  Use when handling an issue from the project's issue tracker.
  Follow issue-to-PR SOP: fetch, assess, branch, implement, validate, submit.
argument-hint: [issue-number]       # shown in autocomplete
# disable-model-invocation: true    # set true to prevent auto-invoke
# user-invocable: false             # set false to hide from /menu
# allowed-tools: Read, Grep, Bash   # tools allowed without permission prompt
# model: sonnet                     # override model for this skill
# context: fork                     # run in forked subagent context
# agent: general-purpose            # subagent type when context: fork
---

Your skill instructions in markdown...
Use $ARGUMENTS for passed arguments (e.g., issue number).
Use $ARGUMENTS[0] for first argument specifically.
Use !`command` for dynamic context injection (runs before sending to Claude).
```

Key frontmatter fields:

| Field | Default | Purpose |
|-------|---------|---------|
| `name` | directory name | Slash-command name |
| `description` | first paragraph | When to use (Claude reads this for auto-invoke) |
| `argument-hint` | none | Autocomplete hint |
| `disable-model-invocation` | false | Prevent Claude auto-loading |
| `user-invocable` | true | Show in /menu |
| `allowed-tools` | inherited | Permission-free tools |
| `model` | inherited | Override model |
| `context` | main | `fork` for subagent isolation |
| `hooks` | none | Skill-scoped lifecycle hooks |

Invocation control:
- Default: user AND Claude can invoke (description always in context)
- `disable-model-invocation: true`: user-only (description NOT in context)
- `user-invocable: false`: Claude-only (hidden from /menu)

### Migration steps

1. For each command, create `~/.claude/skills/<name>/SKILL.md`
2. Add frontmatter (name, description, argument-hint)
3. Move command body to markdown section
4. Add sub-files where useful (xdev-setup: CLAUDE.md template)
5. Test each skill: `/xdev-implement 42`, `/xdev-draft`, `/xdev-setup`
6. Verify: does Claude auto-invoke correctly? Does $ARGUMENTS work?
7. After validation, remove old `~/.claude/commands/xdev-*.md`
8. Update dotfiles repo `install-claude.sh` to deploy skills/ instead

### Tools

- `superpowers:writing-skills` — built-in skill for creating skills
- `skill-creator` plugin — optional, install if writing-skills is insufficient

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
- Multiple rule sources need to coexist (e.g., team rules + personal)
- Specific rules need project-level overrides

Rules files are additive and auto-loaded — no conflict risk. Located at:
- `~/.claude/rules/*.md` — user-wide rules
- `.claude/rules/*.md` — project-specific rules

### Not recommended now

54 lines is lean and effective. Splitting would be over-engineering.

## 4. Hooks Strengthening (P1-P2)

### Hooks configuration format

Hooks are defined in JSON settings files:
- `~/.claude/settings.json` — user-wide
- `.claude/settings.json` — project (shareable, committed)
- `.claude/settings.local.json` — project (gitignored, personal)
- `hooks/hooks.json` — inside a plugin

Structure:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/check-commit.sh",
            "timeout": 600
          }
        ]
      }
    ]
  }
}
```

Handler types:
- `command`: runs shell script. Exit 0 = pass, exit 2 = block.
- `prompt`: single-turn LLM judgment (`"type": "prompt", "prompt": "..."`)
- `agent`: multi-turn subagent with tools (`"type": "agent", "prompt": "..."`)

Hooks receive JSON on stdin with: session_id, cwd, hook_event_name,
tool_name, tool_input. Can output JSON with: continue, stopReason,
systemMessage, hookSpecificOutput.

### Hook 1: Commit format validation (HIGH priority)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/validate-commit-msg.sh"
          }
        ]
      }
    ]
  }
}
```

The script reads stdin JSON, checks if `tool_input.command` contains
`git commit`, extracts the commit message, validates conventional commits
format. Exit 2 to block with error message on stderr.

### Hook 2: Auto-format on edit (MEDIUM priority)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/auto-format.sh"
          }
        ]
      }
    ]
  }
}
```

Script detects project formatter from config files and runs it on the
edited file. PostToolUse — cannot block, runs after edit completes.

### Hook 3: Sensitive file protection (MEDIUM priority)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/protect-sensitive.sh"
          }
        ]
      }
    ]
  }
}
```

Script checks if edited file matches sensitive patterns (*.env, etc.).
Exit 2 to block the edit.

### Hook 4: Stop verification (EXPLORATORY)

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review the conversation. Were all tasks the user requested actually completed? If any task was missed or only partially done, respond with exit code 2 and explain what's missing."
          }
        ]
      }
    ]
  }
}
```

### Implementation order

1. Start with Hook 1 (commit format) — highest value, lowest risk
2. Write the shell script, add to settings.local.json
3. Test on a real project (try valid and invalid commit messages)
4. Once stable, add Hook 2 and 3
5. Hook 4 is exploratory — try when the others are proven

## 5. Plugin Packaging (P4, Future)

When sections 2-4 are stable (validated on 3-4 projects):

1. Install `plugin-dev` plugin for scaffolding and validation
2. Create plugin structure (see below)
3. CLAUDE.md stays in dotfiles repo (not in plugin — different layer)
4. Create repository marketplace repo
5. Publish and test cross-machine install

### Plugin structure target

```
xdev-plugin/
  .claude-plugin/
    plugin.json             # only manifest goes here
  skills/
    xdev-implement/
      SKILL.md
    xdev-draft/
      SKILL.md
    xdev-setup/
      SKILL.md
      templates/            # CLAUDE.md template, checklist
  hooks/
    hooks.json              # commit format, auto-format, file protection
  scripts/
    validate-commit-msg.sh
    auto-format.sh
    protect-sensitive.sh
  LICENSE
```

### plugin.json format

```json
{
  "name": "xdev",
  "version": "2.0.0",
  "description": "General-purpose AI dev workflow: issue-to-PR SOP, drafting, project setup",
  "author": {
    "name": "devloop"
  },
  "license": "MIT",
  "keywords": ["workflow", "development", "issues", "setup"]
}
```

Only `name` is required. Components at standard paths are auto-discovered.
Use `${CLAUDE_PLUGIN_ROOT}` in hook scripts for portable paths.

## Execution Priority

| Item | Priority | Status | When |
|------|----------|--------|------|
| Plugin inventory doc | P0 | Done | This session |
| STATUS.md update | P0 | Done | This session |
| Commands → Skills migration | P1 | Ready | Next session |
| Hooks: commit format | P1 | Ready | Next session |
| Hooks: auto-format | P2 | Ready | After commit hook works |
| Hooks: sensitive files | P2 | Ready | After commit hook works |
| Hooks: stop verification | P3 | Exploratory | When P1-P2 proven |
| CLAUDE.md modularization | P3 | Not needed yet | When CLAUDE.md grows |
| Plugin packaging | P4 | Designed | When workflow stable |

## Reference Links

- Skills docs: code.claude.com/docs/en/skills
- Hooks docs: code.claude.com/docs/en/hooks
- Plugins docs: code.claude.com/docs/en/plugins
- Subagents docs: code.claude.com/docs/en/sub-agents
- Official skills collection: github.com/anthropics/skills
- Awesome Claude Code: github.com/hesreallyhim/awesome-claude-code
- Skill best practices: platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
