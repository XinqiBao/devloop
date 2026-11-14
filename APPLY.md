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

Compare what the target already uses with the relevant skills and optional setup preferences for [Git layout](preferences/git-layout.md) and [status lines](preferences/status-lines.md). A setup preference is not authorization to migrate existing repositories or replace working configuration.

- Add guidance or tool preferences where the target has a real gap.
- Keep existing behavior when it already covers the need.
- Do not copy devloop's document layout to signal completeness.

A review may end with no changes.

## Choose deployment files

Put guidance where its intended readers already look. Keep provider and tool settings in native configuration. Meet compatible existing requirements; ask the owner to choose when requirements conflict or a choice would materially change the outcome.

Several agents may share one guidance file through short native entry points. Split content when readers, scopes, or maintenance needs differ enough to justify another file. Choose directory, linkage, and file count for the target environment.

Keep the skill sources together with their references. Arrange for `engineering` to load throughout engineering work and for situational skills to be discoverable when needed. An instruction to read a skill is weaker than a native import of its content; verify the target client's behavior at session start and after compaction. Do not treat a link, a skill description, or a successful install as proof of loading.

## Claude Code

The plugin and marketplace are defined in `.claude-plugin/`. The read-only `SessionStart` hook loads `engineering` at startup, resume, clear, compaction, and fork. It requires command-hook `args` support, `sh`, and `awk`.

Local-directory marketplaces load in place. Keep their package directory available at runtime and independent of the development checkout.

Reconcile superseded personal guidance when enabling the plugin. Preserve unrelated conversation preferences, host runbooks, and project rules. Installation does not perform this reconciliation.

Verify actual engineering-defaults injection and situational skill selection outside this checkout, including after compaction. A `SessionStart` error does not block the session; inspect hook failures rather than assuming guidance loaded.

## Codex

Expose the shared skills through native discovery, preserving references and sibling layout. The user-level location is `~/.agents/skills/`.

In the existing user-level `~/.codex/AGENTS.md`, add a short loading instruction such as:

```text
For engineering work, read ~/.agents/skills/engineering/SKILL.md before substantive work and again after context compaction. Use its routes to load situational devloop skills as work progresses. Keep devloop policy in the installed skills rather than copying it into this entry point.
```

Discovery exposes names and descriptions. This entry point asks the model to read the engineering defaults body; it does not provide the Claude hook's automatic injection. Verify loading and restoration after compaction on the target client. Reconcile installed copies deliberately when updating devloop.

## Check the result

After deployment, check:

- Each intended agent can reach the guidance through its normal read path.
- Engineers can find the authoritative source without this checkout.
- Instructions do not conflict or duplicate policy, and references resolve.
- Applied tool preferences work in the intended clients.

Report what was verified and what remains uncertain.
