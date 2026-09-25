# Commits

Useful Git history shows meaningful units of engineering change, not the order in which files happened to be edited. Group a commit around one coherent intent so a reader can understand why its parts belong together and, where possible, reason about reverting them together.

A behavior change, its tests, and related documentation can form one commit across several files. Keep unrelated cleanup separate if it is worth including. Splitting every implementation step also makes the history harder to review because the intent is scattered across commits.

Use Conventional Commits by default. A consistent, recognizable expression of change intent makes history easier to scan; the format describes a commit but does not decide its boundary.

Choose branches, pull requests, worktrees, merge style, and commit count according to the task and repository. Use a commit body when non-obvious rationale helps explain the change. Put enduring project knowledge where future readers will need it; a commit message should not be its only home.
