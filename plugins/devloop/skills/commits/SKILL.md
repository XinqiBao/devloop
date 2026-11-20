---
name: commits
description: "Apply the owner's commit and history preferences when planning substantial work that will be committed, grouping changes, writing commit messages, updating or integrating branches, or reviewing history. Use during the work, not only at final delivery."
---

# Commits

These are the owner's defaults; apply them within current task intent and project requirements.

A commit should represent one coherent engineering purpose. History should show what changed, why the changes belong together, how behavior evolved, and where a decision or regression entered.

When committing is authorized, commit completed, checked purposes as the work progresses. Do not accumulate several finished purposes into one final diff and rely on a summary to recover their boundaries. Reassess the boundary before starting another purpose; a small task with one purpose may need only one commit.

## Choose boundaries by purpose

- **Keep related work together.** A behavior change, its tests, and the documentation needed to understand it often form one purpose across several files.
- **Separate unrelated purposes.** Cleanup that does not serve the behavior change makes both intentions harder to review when mixed in.
- **Separate a preparatory refactor when it stands alone.** A refactor that can be understood and verified independently may have its own commit. A small rearrangement that only enables the change is often clearer with it.
- **Keep one purpose intact.** Commits that only make sense after reading the next one make readers reconstruct the work from implementation steps.

File count and edit order do not identify a purpose. Use the number of commits the work needs, without targeting a count. Independent reversibility may help identify a boundary, but a coherent commit is not necessarily safe to revert alone.

## Explain intent in the message

Use Conventional Commits by default so history is easy to scan. The format describes a commit; it does not decide its boundary.

State the intent in the subject. Add a body when a surprising tradeoff or rejected alternative would otherwise be hard to recover.

History can preserve why a change was made. A constraint or decision that future work must routinely account for also belongs near the relevant code or interface; an old commit message is too easy to miss. [knowledge](../knowledge/SKILL.md) covers that placement.

## Choose workflow for the repository

When integrating a feature branch through a pull request, prefer a merge commit that preserves meaningful feature commits and the integration point. Retain the useful evolution of the work rather than routinely squashing it into one diff. Follow repository requirements or an explicit task decision when another integration style is appropriate; this preference does not require a branch or PR for every small change.

When an isolated feature branch needs a newer mainline, prefer a rebase if rewriting its commits has little coordination cost. Check ownership and downstream consumers first; repeated mainline merges can make the feature's evolution harder to follow. Shared branches, meaningful merge topology, and repository requirements can favor a merge instead. Follow existing rewrite authority and protect others' work, including on pushed branches. Choose final PR integration separately and verify affected behavior after resolving conflicts.
