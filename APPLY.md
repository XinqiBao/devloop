# Applying devloop

Use devloop when configuring a new or existing development environment. Prefer the client's native plugin manager and keep effective tool settings in native configuration, so neither depends on this development checkout at runtime. Claude Code defines the package conventions; other clients may need local adaptation. This is an owner-initiated task; use the prompt in [README.md](README.md).

## Inspect effective guidance

Identify the agents and work the environment must support. Trace each agent's normal instruction path, including referenced files and source precedence. If the path is unclear, check the agent's documentation or a representative session.

Keep each source within its scope:

| Source | How to use it |
| --- | --- |
| User-level entry points and referenced guidance | Follow the intended agents' user-level read path; this guidance may apply across projects. |
| Native agent configuration | Inspect relevant provider and tool settings in their native location. |
| Project instructions | Constrain work in that project. Inspect them when the project is a target, without promoting them to environment-wide policy. |
| Other checkouts, templates, and old files | Treat as reference material only when relevant. Their presence gives them no authority over the environment. |

Finding a file does not authorize editing it. For environment-wide work, do not survey unrelated repositories to infer user-level policy.

## Decide what to apply

Compare what the target already uses with the relevant skills and the optional [status-line preference](plugins/devloop/preferences/status-lines.md). The [Git layout preference](plugins/devloop/skills/engineering/references/git-layout.md) is available through the engineering skill when choosing a workspace layout; it does not authorize migrating existing repositories.

- Add guidance or tool preferences where the target has a real gap.
- Keep existing behavior when it already covers the need.
- Do not copy devloop's document layout to signal completeness.

A review may end with no changes.

## Choose deployment files

Put guidance where its intended readers already look. Keep provider and tool settings in native configuration. Meet compatible existing requirements; ask the owner to choose when requirements conflict or a choice would materially change the outcome.

Several agents may share one guidance file through short native entry points. Split content when readers, scopes, or maintenance needs differ enough to justify another file. Choose directory, linkage, and file count for the target environment.

Keep the payload's skill sources together with their references. Arrange for `engineering` to load throughout engineering work and for situational skills to be discoverable when needed. An instruction to read a skill is weaker than a native import of its content; verify the target client's behavior at session start and after compaction. Do not treat a link, a skill description, or a successful install as proof of loading.

## Install the plugin

The marketplace is defined in `.claude-plugin/`; the plugin payload is under `plugins/devloop/`. Install `devloop@devloop` from the `XinqiBao/devloop` Git marketplace. Reconcile an existing source with the same name and keep installation and updates managed by the client.

### Claude Code

The read-only `SessionStart` hook loads `engineering` at startup, resume, clear, compaction, and fork. It requires `sh` and `awk`. Verify actual engineering-defaults injection and situational skill selection outside this checkout, including after compaction. A `SessionStart` error does not block the session; inspect hook failures rather than assuming guidance loaded.

Reconcile superseded personal guidance when enabling the plugin. Preserve unrelated conversation preferences, host runbooks, and project rules. Installation does not perform this reconciliation.

### Codex

Where supported, Codex's native plugin manager discovers the same skills and `SessionStart` hook. Review and trust the plugin hook before relying on automatic injection: Codex reports new or changed hooks at session start, and `/hooks` shows the same review. Changed plugin content can require trust again. The hook can run outside the sandbox after trust; reserve `--dangerously-bypass-hook-trust` for automation that already vets the plugin.

If native integration is insufficient, a local link, copy, or thin guidance adapter may reuse the Claude-managed installation. Keep that adaptation outside this repository, identify its authoritative source and update path, and avoid competing policy copies.

Verify skill discovery and engineering-defaults loading at session start and after compaction. An explicit read route does not guarantee automatic restoration; report the actual behavior. Reconcile and remove superseded standalone guidance deliberately.

## Check the result

After deployment, check:

- Each intended agent can reach the guidance through its normal read path.
- Engineers can find the authoritative source without this checkout.
- Instructions do not conflict or duplicate policy, and references resolve.
- Applied tool preferences work in the intended clients.

Report what was verified and what remains uncertain.
