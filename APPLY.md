# Applying devloop

Use devloop as a reference when configuring a new or existing development environment. When changes are needed, put engineering guidance in that environment's own files and tool preferences in native configuration so neither depends on this checkout at runtime.

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

Compare what the target already uses with the relevant judgments and optional tool preferences in devloop:

- Add guidance or tool preferences where the target has a real gap.
- Keep existing behavior when it already covers the need.
- Do not copy devloop's document layout to signal completeness.

A review may end with no changes.

## Choose deployment files

Put guidance where its intended readers already look. Keep provider and tool settings in native configuration. Meet compatible existing requirements; ask the owner to choose when requirements conflict or a choice would materially change the outcome.

Several agents may share one guidance file through short native entry points. Split content when readers, scopes, or maintenance needs differ enough to justify another file. Choose directory, linkage, and file count for the target environment.

## Check the result

After deployment, check:

- Each intended agent can reach the guidance through its normal read path.
- Engineers can find the authoritative source without this checkout.
- Instructions do not conflict or duplicate policy, and references resolve.
- Applied tool preferences work in the intended clients.

Report what was verified and what remains uncertain.
