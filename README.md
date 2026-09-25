# devloop

devloop is a small, opinionated collection of engineering guidance for AI-assisted software development.

It captures recurring engineering judgment that should remain useful across projects and capable coding agents. Project facts and tool configuration belong in the environments where they apply.

Clone the repository, start a capable coding agent from its root, and give it a relevant task. For example:

Review an environment:

> Review the current engineering environment against devloop. Report meaningful gaps and conflicts; make no changes.

Apply guidance:

> Apply relevant devloop guidance to the current engineering environment. Inspect its existing instructions and conventions first.

Maintain devloop:

> Review and improve devloop's guidance for clarity, consistency, and continued usefulness.

## Repository structure

- [`guidance/`](guidance/): topic-oriented engineering guidance.
- [APPLY.md](APPLY.md): how to apply relevant guidance to another environment.
- [AGENTS.md](AGENTS.md): instructions for maintaining devloop.
- [CLAUDE.md](CLAUDE.md): minimal Claude Code import of `AGENTS.md`.
