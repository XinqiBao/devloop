# devloop

devloop is a focused, opinionated engineering reference for AI-assisted software development. Coding agents and engineers use it to make decisions; future maintainers use it to reassess them. Project facts and tool settings belong in the environments where they apply.

## Use with an agent

Give a coding agent access to devloop in the environment being assessed. These requests point to the documents that contain the actual guidance:

**Apply to a development environment**

```text
Read devloop's APPLY.md and relevant guidance. Apply the relevant guidance to this development environment, then report the result and how you checked it. A no-change result is valid.
```

**Extract guidance into devloop**

```text
Read devloop's AGENTS.md and relevant guidance. Assess whether this development environment reveals reusable engineering judgments missing from devloop. Make warranted changes and report the result. A no-change result is valid.
```

[Applying devloop](APPLY.md) explains how to use the guidance in a target environment. [Maintaining devloop](AGENTS.md) covers changes to this repository.

## Guidance

- [Engineering judgment](guidance/engineering.md): investigation, task boundaries, evidence, recoverability, and mechanisms.
- [Commits](guidance/commits.md): coherent engineering history and messages.
- [Durable knowledge](guidance/knowledge.md): what to retain and where it belongs.
- [Working context](guidance/context.md): optional continuity state for active work.
- [Engineering communication](guidance/communication.md): how to express decisions and evidence for later readers.

[CLAUDE.md](CLAUDE.md) is a minimal Claude Code adapter.
