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

Names and checkout roles depend on the repository. This preference does not require a worktree for every task, a particular baseline or merge policy, or permanent branch retention. It does not authorize migrating an existing repository.

Keep mutable task context independent in each worktree, with explicit links to shared knowledge. See [Scoped context](../../knowledge/references/scoped-context.md) for the user, project, and task boundaries.

When a migration is authorized, inspect the actual Git layout and existing work first. Preserve uncommitted changes, useful ignored files, and local knowledge; verify worktree registrations and context entry points before retiring the old paths. Do not assume Git alone carries local continuity.
