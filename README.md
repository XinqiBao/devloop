# devloop

devloop holds the owner's engineering defaults and judgment for use across projects. Skills guide everyday work; setup references hold optional tool preferences. Project facts and effective settings stay in their own environments.

## Read and load

The core applies throughout engineering work. Situational skills load as their decisions become relevant.

| Skill | When it applies |
| --- | --- |
| [Engineering defaults](skills/devloop-core/SKILL.md) | Throughout engineering work; routes to relevant skills and [deeper judgment](skills/devloop-core/references/judgment.md). |
| [Commits](skills/devloop-commits/SKILL.md) | Grouping changes, writing commit messages, and reviewing history. |
| [Engineering communication](skills/devloop-communication/SKILL.md) | Writing documents, pull request descriptions, and durable explanations. |
| [Knowledge and continuity](skills/devloop-knowledge/SKILL.md) | Retaining findings, placing rationale, handing off, or recovering work; includes [working context](skills/devloop-knowledge/references/working-context.md). |

Setup preferences cover [Git layout](preferences/git-layout.md) and [status lines](preferences/status-lines.md). Apply them when configuring a relevant environment; effective tool settings stay in native configuration.

Claude Code uses the devloop plugin; Codex uses the same skills with a thin native entry point. [Applying devloop](APPLY.md) covers the integration details.

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
