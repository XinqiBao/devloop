# devloop

devloop is the owner's portable, versioned engineering guidance, authored as skills for use across projects. It preserves personal defaults, practices, and judgment, plus optional agent-tool preferences; these are not universal rules. Engineers can read the same material directly. Project facts and effective tool settings belong in the environments where they apply.

## Read and load

Skills are the maintained source of personal guidance. Loading frequency is separate from storage: the small core applies throughout engineering work, while situational skills load when their decisions become relevant. Native agent entry points provide loading instructions rather than a second set of policy.

| Skill | When it applies |
| --- | --- |
| [Engineering defaults](skills/devloop-core/SKILL.md) | Throughout engineering work; routes to relevant skills and [deeper judgment](skills/devloop-core/references/judgment.md). |
| [Commits](skills/devloop-commits/SKILL.md) | Grouping changes, writing commit messages, and reviewing history. |
| [Engineering communication](skills/devloop-communication/SKILL.md) | Writing documents, pull request descriptions, and durable explanations. |
| [Knowledge and continuity](skills/devloop-knowledge/SKILL.md) | Retaining findings, placing rationale, handing off, or recovering work; includes [working context](skills/devloop-knowledge/references/working-context.md). |
| [Status lines](skills/devloop-statusline/SKILL.md) | Configuring an agent's status display; optional and tool-specific. |

Loading a skill constrains authorized work; it does not authorize committing, publishing, or changing an environment. A file link is a reading path, not proof that a client has loaded its contents.

## Try the Claude Code plugin

From the project you want to work on, launch Claude Code with this checkout as a session-local plugin:

```sh
claude --plugin-dir /absolute/path/to/devloop
```

The plugin injects `devloop-core` at session start, resume, clear, and compaction. Other skills are available for automatic selection as work reaches their situations. The hook reads the core skill directly; it keeps no separate policy copy, performs no writes, and requires `sh` and `awk`.

For a local installation, first put a complete package copy in a stable installation directory, then register it:

```sh
claude plugin marketplace add /absolute/path/to/installed-devloop
claude plugin install devloop@devloop --scope user
```

Claude Code loads a local marketplace directory in place, so keep that installation directory available. Reconcile an existing marketplace named `devloop` before adding another source. [Applying devloop](APPLY.md) covers existing-guidance reconciliation, installation checks, and the lightweight Codex setup.

## Use with an agent

Give a coding agent access to devloop in the environment being assessed. Environment application and guidance extraction are owner-initiated maintenance tasks, started with these prompts rather than additional skills:

**Apply to a development environment**

```text
Read devloop's APPLY.md and relevant skills. Apply what is relevant to this development environment, then report the result and how you checked it. A no-change result is valid.
```

**Extract guidance into devloop**

```text
Read devloop's AGENTS.md and relevant skills. Inspect relevant engineering behavior and, where useful, history for recurring owner defaults, practices, judgments, or tool preferences worth carrying across projects or environments. Distinguish intentional owner choices from project or organization requirements, tool or machine constraints, and one-off behavior; report uncertain intent as a candidate. Compare candidates with devloop, strengthen existing guidance where possible, and make only warranted changes. Keep investigation proportional. No worthwhile new guidance is a valid result.
```

[Applying devloop](APPLY.md) explains how to use the guidance in a target environment. [Maintaining devloop](AGENTS.md) covers changes to this repository.

[CLAUDE.md](CLAUDE.md) is a minimal adapter for maintaining this repository, not the runtime entry point for personal guidance in other projects.

## Check changes

```sh
python3 -m unittest discover -s tests -v
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

The native validator may note that the repository's root `CLAUDE.md` is not plugin context; core loading uses the hook. These checks cover package structure and hook behavior. Also exercise implicit skill selection and core restoration in real sessions outside this checkout when changing loading or routing.
