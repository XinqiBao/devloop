# devloop

devloop is a small, opinionated collection of portable engineering guidance for AI-assisted software development. It is a reference for coding agents, engineers at different experience levels, and future maintainers reassessing the decisions behind it. Project facts and tool settings belong in the environments where they apply.

## Use with an agent

Give a capable coding agent access to devloop while it works in the development environment being assessed. These requests can be used as written:

**Apply to a development environment**

```text
Read devloop's APPLY.md and relevant guidance. Apply useful engineering judgments to this development environment, whether it is new or already has guidance.
Inspect its effective user-level guidance, agent entry points, relevant native configuration, and project-level constraints where they affect the environment. Use the environment's authoritative locations and resolve compatible differences.
Check for conflicts, duplication, and broken references. Verify agents and engineers can use the result without access to devloop. A no-change conclusion is valid.
```

**Extract guidance into devloop**

```text
Inspect this development environment's effective guidance, including user-level instructions, agent entry points, relevant native configuration, and project-level constraints where they reveal reusable judgments.
Read devloop's AGENTS.md and compare candidates with its existing guidance. Add only portable judgments addressing a recurring need or important judgment boundary whose benefit justifies their maintenance cost. Keep local facts, private context, and tool settings out of devloop.
Review the guidance as a whole and the final diff for duplication, conflicts, and lost reasoning; a no-change conclusion is valid.
```

[Applying devloop](APPLY.md) explains how to use the guidance in a target environment. [Maintaining devloop](AGENTS.md) covers changes to this repository.

## Guidance

- [Engineering judgment](guidance/engineering.md): investigation, task boundaries, evidence, recoverability, and mechanisms.
- [Commits](guidance/commits.md): coherent engineering history and messages.
- [Durable knowledge](guidance/knowledge.md): what to retain and where it belongs.
- [Working context](guidance/context.md): optional continuity state for active work.
- [Engineering communication](guidance/communication.md): how to express decisions and evidence for later readers.

[CLAUDE.md](CLAUDE.md) is a minimal Claude Code adapter.
