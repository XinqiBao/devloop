# Commits

A commit should represent one coherent engineering purpose. Useful history lets a reader see what changed, why it belonged together, how behavior evolved, and where a decision or regression entered.

## Choose boundaries by purpose

- **Keep related work together.** A behavior change, its tests, and the documentation needed to understand it often form one purpose across several files.
- **Separate unrelated purposes.** Cleanup that does not serve the behavior change makes both intentions harder to review when mixed in.
- **Separate a preparatory refactor when it stands alone.** A refactor that can be understood and verified independently may have its own commit. A small rearrangement that only enables the change is often clearer with it.
- **Keep one purpose intact.** Commits that only make sense after reading the next one make readers reconstruct the work from implementation steps.

File count and edit order do not identify a purpose. Use the number of commits the work needs, without targeting a count. Independent reversibility may help identify a boundary, but a coherent commit is not necessarily safe to revert alone.

## Explain intent in the message

Use Conventional Commits by default to make history easy to scan. The format describes a commit; it does not decide its boundary. State the intent in the message, and add a body when a surprising tradeoff or rejected alternative would otherwise be hard to recover.

History can preserve why a past change was made. A constraint or decision that future work must routinely account for also belongs where that work happens; an old commit message is too easy to miss. [Durable Knowledge](knowledge.md) covers that placement.

## Choose workflow for the repository

Branches, pull requests, worktrees, merge style, and squash decisions depend on the task and repository. Whatever workflow is used, leave understandable engineering history.
