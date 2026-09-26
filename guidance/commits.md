# Commits

Useful Git history shows what changed, why the changes belong together, and how behavior evolved. It helps locate a regression or past decision. Sometimes it also lets a change be reverted on its own, though not every coherent commit can be safely reverted.

## Decide what belongs in one commit

A commit should have one understandable reason for changing the system. That reason matters more than file count or edit order. A behavior change, its tests, and the documentation needed to understand it often belong together. Unrelated cleanup has a different reason and makes the change harder to review when mixed in.

Splitting each implementation step can also obscure the reason for the change. If a commit makes sense only after reading the next one, consider grouping them. Use as many commits as needed to leave understandable units.

A preparatory refactor may deserve its own commit if it can be understood and verified on its own. A small rearrangement that only supports a behavior change is often clearer in the same commit. The reason for the work matters more than the order in which it was done.

## Write messages that explain intent

Use Conventional Commits by default so history is easy to scan. The format describes a commit; it does not determine its boundary. The message should still explain the change's intent.

Use a commit body when a surprising tradeoff or rejected alternative would otherwise be hard to understand later. History is a good place for the reason behind that past decision. If future work must routinely account for a constraint or decision, also record it where engineers will encounter it during that work. An old commit message is easy to miss.

Choose branches, pull requests, worktrees, merge style, and squash decisions for the task and repository. Whatever workflow is used, leave understandable history.
