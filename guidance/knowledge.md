# Durable Knowledge

Investigation can produce many observations, hypotheses, and explanations, especially during AI-assisted work. Only some of that material should remain after the task. Preserve information when losing it would make future engineering meaningfully harder, less reliable, or more likely to repeat avoidable investigation.

## Keep what future work needs

Durable information may include a constraint, decision, non-obvious rationale, recurring lesson, important evidence, exact identifier, provenance, or meaningful remaining uncertainty. These are possibilities, not fields to fill in. Record enough for a future reader to use and, when necessary, evaluate the conclusion. A bare conclusion can be misleading when its evidence or scope is essential to judging whether it still applies.

Put knowledge where its likely reader will look while making the relevant decision: near the code, interface, or project guidance it concerns. For example, an API constraint kept only in an old commit message is easy to miss during later API work. Express the current constraint near the interface, with a link to historical rationale if that history matters. There is no need for one central home for every kind of knowledge.

## Keep authority clear

Avoid copying the same authoritative project fact across guidance layers. Copies can drift as the project changes; once they disagree, engineers and agents must decide which to trust. Keep the fact in its natural authoritative location and refer to it elsewhere when another entry point needs to make it discoverable. Scope claims carefully so a local observation does not become an unsupported project-wide rule.

## Distill investigation

While work is active, raw observations, failed approaches, hypotheses, prompts, and intermediate reasoning may help continuity. When the work ends, keep the conclusions, constraints, rationale, evidence, provenance, and unresolved questions that future work actually needs. A failed approach may be worth recording if its reason for failure would otherwise be rediscovered. Retire the rest rather than preserving a transcript because it exists. [Working context](context.md) covers temporary continuity state while an effort remains active.

Keep tracked engineering artifacts direct, concise, and in English by default, subject to explicit task intent and legitimate project conventions. Concision means removing material that does not help the reader, not stripping out reasoning needed to apply the guidance. Routine prompt residue, agent narration, and automatic AI or tool attribution usually add little. Preserve them when they affect a decision, provenance, reproducibility, or future interpretation.
