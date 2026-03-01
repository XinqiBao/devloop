# Design History — xdev Workflow

Consolidated from 4 handoff documents (v0–v3) created during the
brainstorming sessions on 2026-02-22.

## Timeline

### Session 1: Problem Definition (HANDOFF v0)
- Established the three pain points: prompt instability, slow design
  convergence, context compact drift
- Key decision: **manual trigger**, not automated service
- Key decision: **intent-driven issues**, not implementation-driven
- Rejected: AI auto-discovering problems and filing issues (noise too high)
- Rejected: OpenHands/SWE-agent (what's missing is workflow, not tooling)
- Core conclusion: "Fix the workflow, not the tools"

### Session 2: Deep Research (HANDOFF v1)
- Studied Anthropic's long-running agent patterns, Claude 4 best practices,
  CLAUDE.md writing guides, community patterns (CCPM, etc.)
- Identified that "fresh start > compact" is the key insight for context
  management — not progress files or feature lists
- Mapped research findings to pain points: CLAUDE.md solves prompt
  instability, decision-making rules solve convergence, lightweight
  context instructions are sufficient for compact risk
- Identified the role separation: CLAUDE.md vs commands vs Superpower skills

### Session 3: Design Convergence (HANDOFF v2)
- Refined conclusions into actionable design
- Defined the two-layer architecture (global + project)
- Scoped the three commands (implement, draft, setup)
- Created initial command specifications

### Session 4: Design Complete (HANDOFF v3)
- Completed full design document with architecture diagrams
- Wrote detailed implementation plan (7 tasks)
- Confirmed all decisions with user
- Created session-transition prompts for execution phase

## Discarded Alternatives

| Alternative | Why Discarded |
|-------------|---------------|
| Automated scheduler (devloop) | Too complex for personal use; interactive workflow preferred |
| AI auto-issue discovery | Noise too high, no mature tools |
| OpenHands/SWE-agent integration | Missing ingredient is workflow, not tooling |
| Heavy multi-context checkpoint system | User rarely hits context compact; lightweight instructions suffice |
| Plugin packaging (Phase 1) | Dotfiles = faster iteration; plugin deferred to Phase 3 |
| Separate design/implementation contexts | Most issues fit single context; splitting adds friction |
