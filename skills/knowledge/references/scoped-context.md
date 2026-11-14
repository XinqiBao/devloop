# Scoped Context

Local context holds information that should stay local or is not yet ready for tracked project records: personal environment knowledge, local runbooks, investigation evidence, or active task state. Some findings may later be verified and distilled into project guidance. These purposes have different lifetimes. A directory named `.context` does not make everything in it temporary, authoritative, or worth retaining.

The owner's preferred local convention is `.context/` with an explicit entry point. Use it when continuity or local knowledge warrants it; a small change recoverable from its diff may need no note. Keep this personal convention out of tracked repository requirements unless the project independently adopts it. Check existing ignore behavior before adding ignore rules.

Prefer tracked project records when the information needs to travel with the project or be read by other contributors and agents. An ignored `.context/` is a local supplement, not the default home for shared conventions, durable rationale, or parallel-work coordination that others cannot otherwise reach.

## Choose the scope

| Scope | Belongs here | Boundary |
| --- | --- | --- |
| User, such as `~/.context/` | Cross-project personal guidance, environment knowledge, and host runbooks | No project work packets or machine-specific facts presented as portable policy. Tool settings stay in native configuration. |
| Project shared, such as a repository or bare container's `.context/` | Shared local conventions, cross-worktree facts, and navigation to the responsible task | Do not duplicate each worktree's mutable task history here. Shared coordination state belongs here only when it genuinely spans those tasks. |
| Worktree or task, such as `<worktree>/.context/` | Its investigation, decisions, checks, unresolved issues, and next useful steps | Keep independent worktree state independent. Link to shared knowledge rather than aliasing several task directories to one mutable store. |

Scope and lifetime are separate decisions. A local host runbook can be durable; a project-wide migration checkpoint can be temporary. Keep project contracts and reusable design rationale in tracked project records where future contributors need them. Local context is subordinate to those records and does not authorize work.

Use an actual worktree and task identity when resuming. A branch name alone is insufficient: branches can be renamed or switched, and a checkout can be detached.

## Keep a bounded read path

Give each useful scope an entry point, normally `README.md`, with a short summary and links that say when to read more. Native agent entry files can point to it; keep policy in one place. Reference wider-scope context explicitly rather than assuming a parent directory is automatically discovered or authoritative.

Keep current constraints, unresolved decisions, and next steps easy to recover. Read historical evidence on demand. Mark superseded instructions and remove them from the active path while retaining history that still explains a useful decision.

On resumption, check retained claims against the current checkout, environment, and authorization. A stale plan or once-verified runtime observation may no longer hold.

## Retire, promote, or move deliberately

Keep active records current. When work ends, remove completed state from the default read path; retain requested reports, necessary evidence, and useful local knowledge according to their continuing purpose. Promote lasting project conclusions using [Knowledge and continuity](../SKILL.md), without leaving a competing copy.

During repository moves, worktree changes, or handoffs, account for useful ignored context separately from Git content. Verify that it reaches the intended scope and responsible reader before retiring the old location. Moving files alone does not transfer responsibility.

Do not turn context into a prompt archive, a routine-report obligation, or a duplicate of tracked facts. Ignored files are neither secure storage nor a backup: keep secrets and irreplaceable recovery data in appropriate systems. Temporary task artifacts may aid current work, but their presence does not justify indefinite retention.
