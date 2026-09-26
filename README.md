# devloop

devloop is a small, opinionated collection of portable engineering guidance for AI-assisted software development. It is a reference for coding agents, engineers at different experience levels, and future maintainers reassessing the decisions behind it. Project facts and tool settings belong in the environments where they apply.

Clone the repository and ask a capable coding agent to use it. Name the target project or environment when reviewing or applying guidance. For example:

- **Review:** "Review [target] against devloop. Report meaningful gaps and conflicts; make no changes."
- **Apply:** "Apply relevant devloop guidance to [target]. Inspect its existing instructions and conventions first."
- **Maintain:** "Review devloop for meaningful gaps, contradictions, or stale guidance. Make justified changes; a no-change conclusion is valid."

[Applying devloop](APPLY.md) explains how to use the guidance in a target environment. [Maintaining devloop](AGENTS.md) covers changes to this repository.

## Guidance

- [Engineering judgment](guidance/engineering.md): investigation, task boundaries, evidence, recoverability, and mechanisms.
- [Commits](guidance/commits.md): coherent engineering history and messages.
- [Durable knowledge](guidance/knowledge.md): what to retain and where it belongs.
- [Working context](guidance/context.md): optional continuity state for active work.
- [Engineering communication](guidance/communication.md): how to express decisions and evidence for later readers.

[CLAUDE.md](CLAUDE.md) is a minimal Claude Code adapter.
