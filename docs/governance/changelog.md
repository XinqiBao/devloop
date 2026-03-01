# Workflow Governance Changelog

## 2026-03-01 — Unified Workflow Governance Rollout

Summary:
- Reorganized docs into `core`, `process`, `adapters`, and `governance`.
- Migrated governance source files to `docs/governance/*`.
- Added Claude and Codex adapter documentation.
- Added Codex install/update script (`scripts/install-codex.sh`).
- Updated README/CLAUDE entry points to canonical paths only.
- Removed legacy/obsolete artifacts from HEAD, including `archive/devloop-scheduler/`.
- Added merge-history policy (non-squash integration) and GitHub auth prerequisites in adapter docs.

Impact:
- Single canonical workflow source in repository HEAD.
- Claude marketplace delivery preserved.
- Codex install path enabled without process fork.

## Historical Design Notes (2026-02-22)

Consolidated from 4 handoff documents (v0-v3) created during brainstorming sessions.

### Session 1: Problem Definition (HANDOFF v0)
- Established three pain points: prompt instability, slow design convergence, context compact drift.
- Key decision: manual trigger, not automated service.
- Key decision: intent-driven issues, not implementation-driven.
- Rejected AI auto-discovering problems and filing issues (noise too high).
- Rejected OpenHands/SWE-agent integration (workflow gap, not tooling gap).

### Session 2: Deep Research (HANDOFF v1)
- Studied long-running agent patterns, CLAUDE.md practices, and community workflows.
- Identified "fresh start > compact" for context management.
- Mapped research findings to workflow-layer responsibilities.

### Session 3: Design Convergence (HANDOFF v2)
- Refined conclusions into actionable design.
- Defined two-layer architecture and scoped core commands.

### Session 4: Design Complete (HANDOFF v3)
- Completed design and implementation plan for execution phase.

## Discarded Alternatives

| Alternative | Why Discarded |
|-------------|---------------|
| Automated scheduler | Too complex for personal workflow; interactive mode preferred |
| AI auto-issue discovery | Noise too high |
| OpenHands/SWE-agent integration | Missing ingredient was workflow discipline |
| Heavy multi-context checkpoint system | User usage pattern favored lighter approach |
