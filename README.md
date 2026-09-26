# devloop

devloop is a small, opinionated collection of portable engineering guidance for AI-assisted software development. It is a reference for coding agents, engineers at different experience levels, and future maintainers reassessing the decisions behind it. Project facts and tool settings belong in the environments where they apply.

## Use with an agent

Give a capable coding agent access to devloop. For review or application, work in the target project or environment; for maintenance, work in this repository. These requests can be used as written:

**Review without changes**

```text
Review this project or environment against the relevant devloop guidance.
Report meaningful gaps and conflicts; make no changes.
```

**Apply guidance**

```text
Apply relevant devloop guidance to this project or environment.
Inspect its existing instructions and conventions first.
```

**Maintain devloop**

```text
Review devloop's guidance for meaningful gaps, contradictions, or stale instructions.
Make justified changes; a no-change conclusion is valid.
```

[Applying devloop](APPLY.md) explains how to use the guidance in a target environment. [Maintaining devloop](AGENTS.md) covers changes to this repository.

## Guidance

- [Engineering judgment](guidance/engineering.md): investigation, task boundaries, evidence, recoverability, and mechanisms.
- [Commits](guidance/commits.md): coherent engineering history and messages.
- [Durable knowledge](guidance/knowledge.md): what to retain and where it belongs.
- [Working context](guidance/context.md): optional continuity state for active work.
- [Engineering communication](guidance/communication.md): how to express decisions and evidence for later readers.

[CLAUDE.md](CLAUDE.md) is a minimal Claude Code adapter.
