# Commits

Git history is an engineering artifact. Useful history helps a future reader see what changed, why related changes belonged together, and how behavior evolved. It can also help locate where a regression or decision entered the system and, when appropriate, isolate a change for reversal. Not every coherent change can be safely reverted on its own; reversibility informs commit boundaries but does not define them.

## Group by engineering intent

A commit should express one understandable reason for changing the system. File count, edit order, and implementation steps are poor substitutes for that reason. A behavior change, the tests that establish it, and documentation needed to understand it may form one coherent commit across several files. Unrelated cleanup in the same commit obscures both intentions and makes later review harder.

The opposite mistake is to split one change into commits that only record small steps. When each commit needs the next one to explain its purpose, the history makes readers reconstruct the change instead of showing its intent. Use as many commits as the work needs to leave understandable units, rather than aiming for a particular count.

A preparation refactor may deserve its own commit if it has an independent purpose and can be understood and verified on its own. A small local rearrangement that exists solely to support the behavior change is often clearer with that change. This distinction matters more than whether the refactor happened first.

## Explain the change

Commit messages should state intent consistently enough to make history readable and scannable. Use Conventional Commits by default as devloop's current convention for that purpose. The format describes a commit; it does not decide what belongs in one.

Use a commit body when the reason for a particular change would otherwise be hard to recover, such as a surprising tradeoff or rejected alternative. Rationale tied to that historical decision belongs in history. A constraint or decision that future work must routinely know also belongs in the active project location where its readers will find it; a commit message alone is easy to miss.

Choose branches, pull requests, worktrees, merge style, squash decisions, and commit count for the task and repository. Those workflow choices do not replace the goal of leaving understandable engineering history.
