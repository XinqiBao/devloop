# Git Layout

When choosing a local layout for a repository that benefits from independent parallel work, prefer a bare repository with flat sibling worktrees. The container holds Git administration and shared local navigation; editing happens in the appropriate worktree.

For example:

```text
project/
  .git/                 bare repository
  .context/             shared local knowledge and navigation
  main/                 a checkout
  feature-a/            an independent worktree
  feature-b/            an independent worktree
```

Names and checkout roles depend on the repository. This preference does not require a worktree for every task or a particular baseline or merge policy. It does not authorize migrating an existing repository.

Keep local project worktrees by default after delivery, along with the branches they need. The disk cost is usually acceptable, and a completed task alone is not a reason to remove its checkout. Treat worktree removal as a separate cleanup decision within current authority, respecting repository constraints and actual storage pressure. Temporary validation fixtures created as disposable resources can still be retired when their useful results are preserved.

Keep mutable task context independent in each worktree, with explicit links to shared knowledge. See [Scoped context](../../knowledge/references/scoped-context.md) for the user, project, and task boundaries.

When a migration is authorized, inspect the actual Git layout and existing work first. Preserve uncommitted changes, useful ignored files, and local knowledge; verify worktree registrations and context entry points before retiring the old paths. Do not assume Git alone carries local continuity.
