# devloop

devloop is the owner's agent dotfiles: personal engineering habits, judgments, and tool preferences, versioned for use across development environments. Skills guide everyday work; setup references hold preferences used when configuring tools. These are deliberate personal defaults, not universal engineering rules. Project facts and effective settings stay in their own environments.

## Read and load

Skills use the client's native discovery and load when their decisions become relevant, including stages reached inside a longer task. Each skill can be selected directly; none requires loading `engineering` first.

| Skill | When it applies |
| --- | --- |
| [Engineering](plugins/devloop/skills/engineering/SKILL.md) | Investigation, software and API design, user-experience decisions, implementation, review, and verification; includes [engineering judgment](plugins/devloop/skills/engineering/references/judgment.md). |
| [Agent coordination](plugins/devloop/skills/agents/SKILL.md) | Deciding whether and how to split work, delegate bounded outcomes, run independent tasks in parallel, and manage worker context, lifecycle, and integration. |
| [Git worktrees](plugins/devloop/skills/worktrees/SKILL.md) | Choosing or moving a bare-repository/worktree layout and deciding what to retain or clean up after delivery. |
| [Commits](plugins/devloop/skills/commits/SKILL.md) | Planning and recording coherent commits, writing commit messages, updating or integrating branches, and reviewing history. |
| [Writing](plugins/devloop/skills/writing/SKILL.md) | Writing code comments, docstrings, documents, pull request descriptions, and durable explanations. |
| [Knowledge and continuity](plugins/devloop/skills/knowledge/SKILL.md) | Organizing scoped local knowledge, retaining findings, placing rationale, handing off, or recovering work; includes [scoped context](plugins/devloop/skills/knowledge/references/scoped-context.md). |

The [status-line preference](plugins/devloop/preferences/status-lines.md) applies when configuring an agent interface; effective tool settings stay in native configuration.

The plugin follows Claude Code's marketplace and plugin conventions. Codex can reuse the package through its native plugin support or a local adapter; [Applying devloop](APPLY.md) covers deployment and verification.

## Use with an agent

Give a coding agent access to devloop in the environment being assessed. Environment application and guidance extraction are owner-initiated maintenance tasks, started with these prompts rather than additional skills:

**Apply to a development environment**

```text
Read devloop's APPLY.md and relevant skills and setup preferences. Apply what is relevant to this development environment, then report the result and how you checked it. A no-change result is valid.
```

**Extract guidance into devloop**

```text
Read devloop's AGENTS.md and relevant skills. Inspect relevant engineering behavior and, where useful, history for recurring owner defaults, practices, judgments, or tool preferences worth carrying across projects or environments. Distinguish intentional owner choices from project or organization requirements, tool or machine constraints, and one-off behavior; report uncertain intent as a candidate. Compare candidates with devloop, strengthen existing guidance where possible, and make only warranted changes. Keep investigation proportional. No worthwhile new guidance is a valid result.
```

[Applying devloop](APPLY.md) explains how to use the guidance in a target environment. [Maintaining devloop](AGENTS.md) covers changes to this repository.
