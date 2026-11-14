# Applying devloop

Use devloop when configuring a new or existing development environment. Install the plugin through the client's native manager and keep effective tool settings in native configuration, so neither depends on this development checkout at runtime. This is an owner-initiated task; use the prompt in [README.md](README.md).

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

Compare what the target already uses with the relevant skills and the optional [status-line preference](preferences/status-lines.md). The [Git layout preference](skills/engineering/references/git-layout.md) is available through the engineering skill when choosing a workspace layout; it does not authorize migrating existing repositories.

- Add guidance or tool preferences where the target has a real gap.
- Keep existing behavior when it already covers the need.
- Do not copy devloop's document layout to signal completeness.

A review may end with no changes.

## Choose deployment files

Put guidance where its intended readers already look. Keep provider and tool settings in native configuration. Meet compatible existing requirements; ask the owner to choose when requirements conflict or a choice would materially change the outcome.

Several agents may share one guidance file through short native entry points. Split content when readers, scopes, or maintenance needs differ enough to justify another file. Choose directory, linkage, and file count for the target environment.

Keep the skill sources together with their references. Arrange for `engineering` to load throughout engineering work and for situational skills to be discoverable when needed. An instruction to read a skill is weaker than a native import of its content; verify the target client's behavior at session start and after compaction. Do not treat a link, a skill description, or a successful install as proof of loading.

## Install the shared package

The plugin and marketplace are defined in `.claude-plugin/`. Claude Code and Codex both consume `devloop@devloop` from the `XinqiBao/devloop` Git marketplace. Use each client's native marketplace and installation commands; reconcile an existing source with the same name and refresh it when needed. Keep installation and updates managed by the client.

### Claude Code

The read-only `SessionStart` hook loads `engineering` at startup, resume, clear, compaction, and fork. It requires `sh` and `awk`. Verify actual engineering-defaults injection and situational skill selection outside this checkout, including after compaction. A `SessionStart` error does not block the session; inspect hook failures rather than assuming guidance loaded.

Reconcile superseded personal guidance when enabling the plugin. Preserve unrelated conversation preferences, host runbooks, and project rules. Installation does not perform this reconciliation.

### Codex

Codex discovers the same skills from the installed package and runs the same `SessionStart` hook. Review and trust the plugin hook before relying on automatic injection: Codex reports new or changed hooks at session start, and `/hooks` shows the same review. Trust is required again after the hook changes. The hook can run outside the sandbox after trust; reserve `--dangerously-bypass-hook-trust` for automation that already vets the plugin.

Verify that the `devloop:*` skills are discoverable and that the engineering defaults are injected at session start and after compaction. Do not also copy the skills into a user-level entry point; that duplicates policy and drifts. Reconcile and remove superseded standalone copies deliberately.

## Check the result

After deployment, check:

- Each intended agent can reach the guidance through its normal read path.
- Engineers can find the authoritative source without this checkout.
- Instructions do not conflict or duplicate policy, and references resolve.
- Applied tool preferences work in the intended clients.

Report what was verified and what remains uncertain.
