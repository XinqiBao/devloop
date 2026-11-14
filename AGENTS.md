# Maintaining devloop

Read [README.md](README.md) and the relevant guidance before changing this repository.

Keep guidance used during engineering work in `plugin/skills/`, including personal preferences that apply at a particular decision. Keep setup-only tool preferences in `plugin/preferences/`. Treat a skill's entry point and its references as one maintained topic. Native loaders and plugin packaging may select or expose that content, but must not maintain a second policy copy. Keep application and extraction as explicit prompts, not skills.

## Scope and selection

Keep tracked material in English. Keep general engineering guidance independent of any checkout or agent product. Clearly scope agent-specific preferences and keep them separate from general guidance. Do not present private context, local settings, or repository-specific rules as portable guidance.

When extracting from an environment:

- Examine relevant behavior, guidance, and history only as far as the candidate warrants.
- Compare candidate defaults, practices, judgments, and preferences with existing devloop topics.
- Add material only when there is reason to treat it as an intentional owner choice that recurs across projects or environments and would materially change future engineering behavior. Observed behavior alone is a candidate, not a preference. Prefer native capability over unnecessary mechanisms.

Strengthen an existing topic before adding a document. Split a topic only when its audience or decisions warrant a separate read path. Prune obsolete material after checking what useful reasoning or behavior would be lost.

## Writing and review

Write direct engineering guidance. Remove unnecessary material, but keep the reasoning needed to apply a judgment.

Choose headings, prose, lists, comparisons, or examples according to the information. Follow [Writing](plugin/skills/writing/SKILL.md) without imposing a template or teaching basic tools.

Before claiming completion:

- Review the guidance as a whole for duplication, conflicts, accidental workflow requirements, and stale references.
- Check that an engineer can follow the reasoning and an agent can identify the operative guidance.
- Review the final diff, links, and affected behavior.

## Package checks

For package changes, use the relevant checks:

```sh
python3 -m unittest discover -s tests -v
claude plugin validate plugin/.claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

When changing loading or routing, also exercise implicit skill selection and engineering-defaults restoration in real sessions outside this checkout. Runtime engineering-defaults loading uses the hook. Keep repository surfaces—root documentation, tests, and the repository adapter—outside `plugin/`.

Use focused behavioral checks for the decision being changed. A larger eval suite is useful for recurring misrouting or uncertain behavioral benefit; compare with a baseline when measuring improvement. Do not run a full model-graded suite for every wording change or equate skill invocation with better decisions.
