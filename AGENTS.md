# Maintaining devloop

Read [README.md](README.md) and the relevant guidance before changing this repository.

## Scope and selection

Keep tracked material in English. Keep general engineering guidance independent of any checkout or agent product. Clearly scope agent-specific preferences and keep them separate from general guidance. Do not present private context, local settings, or repository-specific rules as portable guidance.

When extracting from an environment:

- Examine relevant behavior, guidance, and history only as far as the candidate warrants.
- Compare candidate defaults, practices, judgments, and preferences with existing devloop topics.
- Add material only when there is reason to treat it as an intentional owner choice that recurs across projects or environments and would materially change future engineering behavior. Observed behavior alone is a candidate, not a preference. Prefer native capability over unnecessary mechanisms.

Strengthen an existing topic before adding a document. Split a topic only when its audience or decisions warrant a separate read path. Prune obsolete material after checking what useful reasoning or behavior would be lost.

## Writing and review

Write direct engineering guidance. Remove unnecessary material, but keep the reasoning needed to apply a judgment.

Choose headings, prose, lists, comparisons, or examples according to the information. Follow [Engineering Communication](guidance/communication.md) without imposing a template or teaching basic tools.

Before claiming completion:

- Review the guidance as a whole for duplication, conflicts, accidental workflow requirements, and stale references.
- Check that an engineer can follow the reasoning and an agent can identify the operative guidance.
- Review the final diff, links, and affected behavior.
