# Unified Workflow Governance Design (Claude + Codex)

## Goal

Create a high-quality, cross-platform workflow system where:

- `devloop` is the single source of truth.
- Claude and Codex are adapter targets, not separate rule universes.
- quality-first practices are enforced as executable process rules.
- repository HEAD stays clean (no legacy/obsolete docs in working tree).

## Scope

### In Scope

- Reorganize workflow documentation into platform-agnostic core/process layers plus platform adapters.
- Keep Claude marketplace distribution as primary Claude delivery method.
- Add Codex deployment pathway from the same source.
- Remove legacy/obsolete/duplicated docs from HEAD (Git history remains the archive).
- Encode quality principles into operational workflow steps.

### Out of Scope

- Cleaning Claude runtime history directories under `~/.claude/projects`, `~/.claude/debug`, `~/.claude/tasks`, `~/.claude/todos`.
- Rewriting historical Git commits or squashing project history.
- Building a full standalone product beyond repository-level governance.

## Design Principles

1. Single source first: every rule must have one authoritative location.
2. Platform adapters only map; they do not redefine core behavior.
3. Evidence before completion claims.
4. Prefer safe parallelism to reduce main-context pressure.
5. Clean HEAD policy: current repo state should represent current truth only.

## Architecture

### Layer 1: Core (platform-agnostic)

Contains invariant principles and quality standards:

- quality-first execution
- evidence-before-claim
- context-budget awareness
- parallel-when-safe
- self-improvement loop

No Claude- or Codex-specific wording.

### Layer 2: Process (platform-agnostic)

Contains operational workflows with explicit IO contracts:

- requirements clarification
- design and approval
- implementation planning
- execution and verification
- completion and retrospective updates

Each process section defines:

- Inputs
- Steps
- Outputs
- Acceptance criteria

### Layer 3: Adapters (platform-specific)

- `adapters/claude`: plugin/skills/hooks/marketplace mapping
- `adapters/codex`: skills/symlink/install mapping

Adapter documents may reference core/process, but must not introduce conflicting rules.

## Repository Structure Target

```text
docs/
  core/
  process/
  adapters/
    claude/
    codex/
  governance/
plugins/xdev/
scripts/
```

## Canonical Entry Points

Active onboarding should point to these paths only:

- `README.md` -> `docs/core`, `docs/process`, `docs/adapters`, `docs/governance`
- `CLAUDE.md` -> canonical source pointers, no duplicate policy body
- `scripts/install-codex.sh` -> Codex install/update path (`~/.agents/skills`)

`docs/xdev-workflow/` is retained as migration pointers only.

## Lifecycle Policy (Clean HEAD)

Policy decision:

- Remove legacy/obsolete/archive content from working tree.
- Keep only active, user-facing, maintainable materials in HEAD.
- Rely on Git history/tags/releases for traceability.

Practical implications:

- `archive/` directory is removed.
- old iterative docs are either migrated into active governance/core/process docs or deleted.
- README links only active docs.

## Quality Rules as Executable Workflow

The following become first-class workflow rules:

1. Quality-first gate:
   - No implementation without scoped acceptance criteria.
2. Evidence gate:
   - No “done” claim without explicit verification evidence.
3. Parallelism gate:
   - Use parallel execution for independent tasks.
   - Force serial mode for dependent/shared-state tasks.
4. Context-budget gate:
   - Split long initiatives into staged sessions with concise state handoff.
5. Self-improvement gate:
   - Each completed initiative captures actionable process improvements.

## Claude and Codex Delivery Model

### Claude

- Keep repository marketplace plugin model (`xdev@devloop`).
- Plugin remains delivery unit for skills/hooks.
- Dotfiles remain thin installer/reference layer.

### Codex

- Add codex adapter docs and install/update script.
- Codex setup references same core/process source and exposes required skills.
- No Codex-only process fork.

## Migration Strategy

1. Build new active structure (`core/process/adapters/governance`).
2. Migrate needed content from iterative docs.
3. Remove legacy/duplicate/archive content from HEAD.
4. Update plugin/docs/install references.
5. Validate Claude and Codex onboarding against same source.

## Verification Strategy

1. Structure checks:
   - All active docs reachable from README.
   - No broken references to removed legacy paths.
2. Policy checks:
   - Core docs contain no platform-specific coupling.
   - Adapter docs contain references, not divergent rules.
3. Delivery checks:
   - Claude plugin path and install instructions valid.
   - Codex install path and skill discovery instructions valid.

## Risks and Mitigations

1. Risk: broken links after cleanup.
   - Mitigation: explicit link audit before and after deletions.
2. Risk: accidental behavior drift between Claude and Codex.
   - Mitigation: shared-source rule plus adapter-only constraints.
3. Risk: over-engineering documentation.
   - Mitigation: enforce concise docs with clear ownership and acceptance criteria.

## Success Criteria

1. Single canonical workflow source exists in `devloop`.
2. No legacy/archive clutter in HEAD.
3. Claude and Codex both consume the same workflow logic.
4. Workflow rules explicitly prioritize quality over speed and require verification evidence.
