# Design Decisions — xdev Workflow

Decisions from brainstorming sessions. Newest at the bottom.

## Architecture: Two-Layer Separation
**Decision**: Global layer (universal workflow) + Project layer (project knowledge)
**Rationale**: Portability across projects and machines. Workflow travels with the user via dotfiles; project layer stays with each project.

## Delivery: Dotfiles First, Plugin Later
**Decision**: Start with dotfiles repo management, optionally package as Claude Code plugin after stabilization.
**Rationale**: Dotfiles = fast iteration (edit file → immediately effective). User already has dotfiles repo. Once stable (validated on 3-4 projects), consider plugin.

## Naming: `xdev-` Prefix
**Decision**: Commands named `/xdev-implement`, `/xdev-draft`, `/xdev-setup`
**Rationale**: Short but distinctive, avoids conflicts with Superpower skills and other plugins.

## Three Commands
1. `/xdev-implement` — Handle an existing issue (fetch → assess → implement → test → PR)
2. `/xdev-draft` — Draft a new issue from a vague idea
3. `/xdev-setup` — Project health check + CLAUDE.md onboarding

## Language: English for All Artifacts
**Rationale**: Claude works best with English technical content. User's commits, issues, PRs are all English.

## Platform Agnostic
**Decision**: No hardcoding GitHub/GitLab specifics.
**Rationale**: Commands use generic terms and auto-detect available tools (gh, glab, MCP).

## Design + Implementation Together
**Decision**: Default to same context window for both.
**Rationale**: User rarely hits context compact. Splitting adds operational complexity.

## Project Health Checks: Quality-Focused
**Decision**: Check quality dimensions (tests? linting? CI?), not specific toolchains.
**Rationale**: Projects span multiple languages and build systems.

## Design Convergence Fix
**Decision**: Add explicit decision-making rules to global CLAUDE.md.
**Rationale**: Core frustration is Claude making design decisions unilaterally.

## Superpower Relationship
**Decision**: Complementary, not overlapping.
- CLAUDE.md = principles (what to do / not do)
- /xdev-* commands = workflow SOPs (process steps)
- Superpower skills = methodology (how to do things well)
- Project hooks = automated quality gates

## Context Management
**Decision**: Lightweight instructions in CLAUDE.md, no heavy checkpoint system.
**Rationale**: User rarely hits context compact. Instructions provide adequate safety net.

## Relationship to devloop Scheduler
**Decision**: xdev is the interactive workflow. devloop scheduler was designed for fully automated execution. User chose the interactive approach as primary. Scheduler code archived for potential future use.

## Delivery Evolution: Dotfiles → Plugin Marketplace (Pending)
**Decision**: Current delivery is dotfiles + manual symlink. Next step is
packaging as a personal Claude Code plugin (private marketplace), which
would enable `claude plugin install` for one-command setup and automatic
updates across machines.
**Rationale**: Dotfiles require running `install-claude.sh` after each
update and on each machine. Plugin packaging solves both: push to repo,
all machines get updates on next plugin refresh. This is the natural
evolution of the "Dotfiles First, Plugin Later" decision.
**Status**: Done. devloop repo is now a repository marketplace. See
"Plugin Packaging via Personal Marketplace" decision below.

## Two Deployment Layers (2026-02-23)
**Decision**: Plugin ships "process and tools" (skills, hooks, agents).
Dotfiles ship "principles and constraints" (CLAUDE.md, rules/).
**Rationale**: Plugins cannot distribute `~/.claude/CLAUDE.md` or
`~/.claude/rules/*.md` — these are user-level config, not plugin-level.
This aligns with the existing two-layer architecture (global + project)
and keeps concerns separated: behavioral principles in dotfiles,
workflow automation in plugin.

## Commands → Skills Migration (2026-02-23)
**Decision**: Migrate xdev commands from `~/.claude/commands/` to
`~/.claude/skills/` format, packaged in xdev plugin.
**Rationale**: Skills are now the recommended format in Claude Code.
Benefits: sub-directories for reference docs, frontmatter for
invocation control, cross-platform compatibility (Claude.ai, Desktop),
unified with superpowers skill system.
**Status**: Done. Skills in `plugins/xdev/skills/`. Old commands removed.

## Hooks as Hard Quality Gates (2026-02-23)
**Decision**: Use hooks for enforcement, CLAUDE.md for guidance.
Priority: commit format validation (PreToolUse), sensitive file
protection (PreToolUse).
**Rationale**: CLAUDE.md rules are "soft" — Claude may ignore them under
context pressure. Hooks are deterministic and cannot be bypassed.
**Status**: Done. Native Python hooks in `plugins/xdev/hooks/`.

## Plugin Selection: High-Coverage or Don't Install (2026-02-23)
**Decision**: Only install a third-party plugin if it covers your needs
substantially. If you only need a small fraction of a plugin's features,
prefer building the specific capability yourself or using a simpler tool.
**Rationale**: Each plugin adds coupling — its conventions, its context
overhead, its update cycle. A plugin that mostly sits unused is pure cost.
Building the specific piece you need keeps the setup minimal, understood,
and under your control. This preserves elegance and reduces the risk of
plugin bloat.
**Application**:
- superpowers: high coverage — brainstorming, planning, TDD, debugging,
  review, git workflow. All features used regularly. Keep.
- pr-review-toolkit: high coverage — 6 review agents, all useful. Keep.
- commit-commands: high coverage — /commit and /commit-push-pr both used. Keep.
- dev-agent-skills: low coverage — mostly duplicates what commit-commands +
  pr-review-toolkit already provide. Don't install.
- skill-creator: medium — useful specifically during migration. Install
  temporarily, remove after.
- ralph-wiggum: evaluate by trial — if the loop feels overkill for most
  tasks, don't keep it.

## xdev as Facade over Plugin Ecosystem (2026-02-23)
**Decision**: Keep `/xdev-*` skills as the user's unified entry point.
Internally, xdev skills can reference and leverage existing plugins
(feature-dev agents, hookify rules, etc.) rather than reimplementing.
**Rationale**:
- User only needs to remember their own commands (`/xdev-implement`,
  `/xdev-draft`, `/xdev-setup`) — no need to memorize dozens of
  plugin-specific commands.
- xdev skills act as a thin orchestration layer that adds user-specific
  preferences (issue tracker integration, branch naming, scope control)
  on top of the plugin ecosystem's heavy lifting.
- When a plugin provides a superior capability (e.g., feature-dev's
  parallel agent exploration), xdev can reference it rather than
  building a weaker version.
- Custom additions remain easy: add xdev-specific steps that no plugin
  covers (e.g., issue fetching, PR conventions).
**Key plugins to integrate**:
- `feature-dev`: 7-phase workflow with parallel agents (covers most of
  xdev-implement's workflow, but stronger). xdev-implement can reference
  feature-dev's agents or patterns.
- `hookify`: Simplified hook creation via markdown rules. Replaces
  hand-written JSON/scripts for quality gates.
- `claude-md-management`: CLAUDE.md audit and session learnings capture.
  Complements xdev-setup.
**Status**: Done. xdev-implement enhanced with parallel agents,
hookify kept for ad-hoc rules, claude-md-management installed.

## Native Hooks over hookify (2026-02-23, supersedes "Hooks via hookify")
**Decision**: Use native hook scripts in xdev plugin instead of hookify
markdown rules.
**Rationale**: Native hooks (hooks.json + Python scripts) are auto-deployed
with the plugin — `claude plugin install xdev@devloop` gets hooks working
immediately. hookify rules are project-local (.claude/*.local.md) and
require manual symlinks per project. Native hooks follow the same pattern
as security-guidance and other official plugins. hookify remains installed
for ad-hoc project-specific rules.
**Status**: Done. Two native hooks in `plugins/xdev/`.

## Plugin Packaging via Personal Marketplace (2026-02-23)
**Decision**: devloop repo serves as a personal Claude Code marketplace.
xdev plugin installed via `claude plugin install xdev@devloop`.
**Rationale**: Accelerated from P4 to immediate. The marketplace approach
provides one-command install/update across machines. Plugin contains
skills + hooks + scripts. CLAUDE.md stays in dotfiles (two-layer
separation preserved). No need for intermediate local-skills phase.
**Status**: Done. Marketplace manifest at `.claude-plugin/marketplace.json`.
