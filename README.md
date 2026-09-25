# devloop

devloop is a small, opinionated collection of engineering guidance for AI-assisted software development.

It captures recurring engineering judgment that should remain useful across projects and capable coding agents. Project facts and tool configuration belong in the environments where they apply.

Clone the repository, start a capable coding agent from its root, and give it a relevant task. Name the target project or environment in review and apply requests. For example:

Review an environment:

> Review [target project or environment] against devloop. Report meaningful gaps and conflicts; make no changes.

Apply guidance:

> Apply relevant devloop guidance to [target project or environment]. Inspect its existing instructions and conventions first.

Maintain devloop:

> Review devloop's guidance for material gaps, contradictions, or stale instructions. Make justified changes; a no-change conclusion is valid.

## Repository structure

- [`guidance/`](guidance/): topic-oriented engineering guidance.
- [APPLY.md](APPLY.md): how to apply relevant guidance to another environment.
- [AGENTS.md](AGENTS.md): instructions for maintaining devloop.
- [CLAUDE.md](CLAUDE.md): minimal Claude Code import of `AGENTS.md`.
