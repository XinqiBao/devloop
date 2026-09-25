# Commits

Use Conventional Commits by default to describe a change's intent. The format does not determine commit boundaries.

Group work by coherent engineering intent, not by file count or implementation step. A behavior change, its tests, and related documentation can belong in one commit even when they touch several files.

Separate unrelated changes so readers can understand and, when needed, revert them independently. Excessive fragmentation also makes history harder to follow when each commit explains only a small implementation step.

Choose branches, pull requests, worktrees, merge style, and commit count according to the task and repository. Use a commit body when non-obvious rationale helps explain the change. Put enduring project knowledge where future readers will need it; a commit message should not be its only home.
