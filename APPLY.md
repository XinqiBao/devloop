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

Compare what the target already uses with the relevant skills and the optional [status-line preference](plugins/devloop/preferences/status-lines.md). The [Git worktree preferences](plugins/devloop/skills/worktrees/SKILL.md) apply when choosing a workspace layout or deciding what to retain; they do not authorize migrating existing repositories.

- Add guidance or tool preferences where the target has a real gap.
- Keep existing behavior when it already covers the need.
- Do not copy devloop's document layout to signal completeness.

A review may end with no changes.

## Choose deployment files

Put guidance where its intended readers already look. Keep provider and tool settings in native configuration. Meet compatible existing requirements; ask the owner to choose when requirements conflict or a choice would materially change the outcome.

Several agents may share one guidance file through short native entry points. Split content when readers, scopes, or maintenance needs differ enough to justify another file. Choose directory, linkage, and file count for the target environment.

Keep each skill's sources together with its references and expose all skills through the client's native discovery. Let the agent choose relevant skills from the task, including decisions reached during longer work. Do not require `engineering` as an entry point or copy skill bodies into user instructions, session hooks, or startup prompts to force loading.

When replacing an older devloop deployment, remove its session-injection setup and mandatory-read routes from active adapters. Preserve unrelated interaction preferences, host runbooks, and project instructions. Historical backups are not active guidance and need not be rewritten. Installation alone does not reconcile these external files.

## Install the plugin

The marketplace is defined in `.claude-plugin/`; the plugin payload is under `plugins/devloop/`. Install `devloop@devloop` from the `XinqiBao/devloop` Git marketplace. Reconcile an existing source with the same name and keep installation and updates managed by the client.

### Claude Code

The native plugin manager exposes the skills for explicit invocation and implicit selection. This package has no session hook. Verify selection with natural requests outside this checkout; a successful install or visible description alone does not establish that the agent reads or follows a skill when relevant.

### Codex

Where supported, Codex's native plugin manager discovers the same skills.

If the client needs a local adaptation for skill discovery, expose the skill directories through its supported discovery locations. Keep that adaptation outside this repository, identify its authoritative source and update path, and avoid competing policy copies. Verify a concrete native limitation before adding a workaround.

Rely on the client's skill discovery and loading behavior. Report any observed limitation at its actual scope.

## Check the result

After deployment, check:

- Each intended agent can discover the skills through its native skill interface.
- Engineers can find the authoritative source without this checkout.
- Instructions do not conflict or duplicate policy, and references resolve.
- Relevant natural requests select useful guidance without old injection or mandatory-read routes; unrelated requests do not acquire unnecessary workflow.
- Applied tool preferences work in the intended clients.

Report what was verified and what remains uncertain.
