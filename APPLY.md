# Applying devloop

Use devloop when configuring a new or existing development environment. Install relevant skills as a self-contained copy or package, and keep effective tool settings in native configuration, so neither depends on this development checkout at runtime. This is an owner-initiated task; use the prompt in [README.md](README.md).

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

Compare what the target already uses with the relevant skills and setup preferences in devloop. [Status-line preferences](preferences/status-lines.md) apply when configuring the environment's display; they do not need a runtime skill.

- Add guidance or tool preferences where the target has a real gap.
- Keep existing behavior when it already covers the need.
- Do not copy devloop's document layout to signal completeness.

A review may end with no changes.

## Choose deployment files

Put guidance where its intended readers already look. Keep provider and tool settings in native configuration. Meet compatible existing requirements; ask the owner to choose when requirements conflict or a choice would materially change the outcome.

Several agents may share one guidance file through short native entry points. Split content when readers, scopes, or maintenance needs differ enough to justify another file. Choose directory, linkage, and file count for the target environment.

Keep the skill sources together with their references. Arrange for `devloop-core` to load throughout engineering work and for situational skills to be discoverable when needed. An instruction to read a skill is weaker than a native import of its content; verify the target client's behavior at session start and after compaction. Do not treat a link, a skill description, or a successful install as proof of loading.

## Claude Code

The repository root is a Claude Code plugin, with a marketplace in `.claude-plugin/marketplace.json`. Use the preview or install commands in [README.md](README.md). For a local installation, put the complete package in a stable installation directory outside the development checkout. Claude Code loads local-directory marketplaces in place, even when a cache copy also exists; removing that source breaks loading. Treat that stable copy as the installed package and update it deliberately. Reconcile an existing marketplace named `devloop` rather than silently replacing its source. Use your normal model, authentication, and permission settings.

The plugin discovers skills from `skills/`. A read-only `SessionStart` hook emits the body of `devloop-core` from the installed package, together with its source and reference directory. It runs for `startup`, `resume`, `clear`, and `compact`; it does not load every situational skill. Requires a CLI that supports command-hook `args`, plus `sh` and `awk` on the hook's executable path. Validate against the installed CLI before relying on this format.

Confirm that the plugin is enabled and its skills appear in the client's skill listing. In a fresh session outside the devloop checkout, inspect the hook execution and emitted core context, then exercise a relevant task without naming a skill. Inspect the actual skill invocation or file-read events. Repeat after `/compact`; a model saying it remembers the rules is not sufficient evidence. If core loading fails, inspect the hook error and repair the installation; `SessionStart` errors do not block the session.

Reconcile an existing personal guidance copy when enabling the plugin. Preserve unrelated conversation preferences, host runbooks, and project rules; remove or retire superseded devloop policy copies only within the authorized application scope. A plugin install alone does not perform that reconciliation. After updating a plugin version, reload or restart as required by the installed client and check the effective package version.

## Codex

Use the same skill directories through Codex's native standalone-skill discovery. Copy the directories from `skills/` into `~/.agents/skills/`, preserving their reference files and sibling layout. Reconcile an existing directory with the same name before replacing it. The installed copy must remain usable without this development checkout.

In the existing user-level `~/.codex/AGENTS.md`, add a short loading instruction such as:

```text
For engineering work, read ~/.agents/skills/devloop-core/SKILL.md before substantive work and again after context compaction. Use its routes to load situational devloop skills as work progresses. Keep devloop policy in the installed skills rather than copying it into this entry point.
```

Start a fresh Codex session outside the devloop checkout. Verify that the installed skills are discoverable and that a normal engineering request causes the core and relevant situational body to be read. Check unrelated requests as well, so optional skills do not attract unrelated work.

This adaptation uses a native instruction to request core loading, rather than the Claude-specific hook. Discovery exposes names and descriptions; it does not itself inject the core body. Test restoration after compaction on the actual Codex client before claiming equivalent persistence. Reapply or reconcile installed copies deliberately when updating devloop.

## Check the result

After deployment, check:

- Each intended agent can reach the guidance through its normal read path.
- Engineers can find the authoritative source without this checkout.
- Instructions do not conflict or duplicate policy, and references resolve.
- Applied tool preferences work in the intended clients.

Report what was verified and what remains uncertain.
