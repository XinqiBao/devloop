# devloop

devloop is a small, opinionated collection of portable engineering guidance for AI-assisted software development. Its active documents help capable coding agents make sound decisions and help developing engineers understand the judgment behind them. They also preserve enough reasoning for future maintainers to reassess the advice. Project facts and tool settings belong in the environments where they apply.

Start with a topic below, or clone the repository and ask a capable coding agent to review or apply it. Name the target project or environment in those requests. For example:

Review an environment:

> Review [target project or environment] against devloop. Report meaningful gaps and conflicts; make no changes.

Apply guidance:

> Apply relevant devloop guidance to [target project or environment]. Inspect its existing instructions and conventions first.

Maintain devloop:

> Review devloop's guidance for material gaps, contradictions, or stale instructions. Make justified changes; a no-change conclusion is valid.

## Guidance

- [Engineering work](guidance/engineering.md): reality, intent, evidence, recoverability, and the cost of mechanisms.
- [Commits](guidance/commits.md): coherent engineering history and useful commit messages.
- [Durable knowledge](guidance/knowledge.md): what future work needs and where to preserve it.
- [Working context](guidance/context.md): temporary state for interrupted or continuing work.

[Applying devloop](APPLY.md) covers use in another environment. [Maintaining devloop](AGENTS.md) gives repository-specific guidance; [CLAUDE.md](CLAUDE.md) is a minimal Claude Code adapter.
