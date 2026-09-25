# devloop

devloop is a small, opinionated collection of engineering guidance for AI-assisted software development.

Clone the repository, start a capable coding agent from its root, and ask it to work with the relevant guidance. For example:

- Review the current engineering environment against devloop and report meaningful gaps.
- Apply relevant devloop guidance to the current engineering environment.
- Review and improve devloop's guidance for clarity, consistency, and continued usefulness.

## Repository map

- [Engineering work](guidance/engineering.md): principles for carrying out engineering tasks.
- [Commits](guidance/commits.md): coherent Git history and contextual workflow choices.
- [Durable knowledge](guidance/knowledge.md): persistent engineering information.
- [Working context](guidance/context.md): scope and lifetime of temporary context.
- [APPLY.md](APPLY.md): how relevant guidance is applied to a real environment.
- [AGENTS.md](AGENTS.md): instructions for maintaining devloop itself.

`CLAUDE.md` imports `AGENTS.md` for Claude Code. devloop supplies guidance, not a required runtime dependency or workflow tool.
