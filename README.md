# devloop

devloop is a small, opinionated reference for AI-assisted software engineering. It offers durable practices and an agent-facing way to assess them against a real environment. Read it to decide what, if anything, is worth adopting; using it does not require installation.

The intended readers are engineers and capable agents working in existing projects. Specific user and project intent outranks these general practices. Investigation and verification should scale with risk, and an environment review can correctly end with no changes.

This is not a framework, CLI, installer, dotfiles manager, synchronization system, runtime dependency, machine snapshot, or mandatory agent workflow. Guidance should live at the narrowest justified scope and remain useful if this checkout is moved or deleted.

## Read

- [PRACTICES.md](PRACTICES.md): the outcomes and constraints to evaluate, not a prescribed lifecycle.
- [ADOPT.md](ADOPT.md): one entry point for first-time assessment, later review, or considering a new practice.
- [AGENTS.md](AGENTS.md): instructions for maintaining this repository; not guidance to copy into another project.
- [CLAUDE.md](CLAUDE.md): a minimal compatibility import for Claude Code versions that do not directly load `AGENTS.md`.

## Use

Ask an agent with access to this repository, for example:

> Read devloop's PRACTICES.md and assess whether any practice would improve this project. Inspect existing instructions and capabilities first; report a no-change outcome when appropriate.

> Use devloop's ADOPT.md to review my agent setup. Do not edit my configuration before showing me any material conflict or migration choice.

These are requests for contextual judgment, not permission to install files or override existing instructions. No tracked file needs a live link to this checkout. Earlier implementations remain in Git history, not in the active guidance.

Licensing remains unresolved: no root license file was tracked, although an earlier README and plugin metadata claimed MIT.
