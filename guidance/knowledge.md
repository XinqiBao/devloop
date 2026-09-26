# Durable Knowledge

An investigation may leave many observations, hypotheses, and explanations. Future work needs only some of them. Keep information when losing it would make a later decision harder, less reliable, or require repeating an investigation.

## Decide what to keep

Keep the constraints, decisions, and non-obvious reasons that later work will need. Evidence, exact identifiers, provenance, and unresolved uncertainty also matter when they help a reader apply or reassess a conclusion. These are examples, not fields to fill in. A conclusion without its scope or supporting evidence can mislead the next person who uses it.

Put each fact where a reader will look while making the relevant decision: near the code, interface, or project guidance it concerns. An API constraint kept only in an old commit message is easy to miss during later API work. State the current constraint near the interface and link to the history if its rationale matters. Different kinds of knowledge need not share one central home.

## Give each fact a clear home

Keep a project fact in the place responsible for it. Copies in several guidance files can drift; conflicting versions leave readers unsure which to trust. Link to the fact from other entry points when needed. Also state its scope: an observation about one module does not establish a rule for the whole project.

## Keep conclusions, not a transcript

Raw observations, failed approaches, and hypotheses may help while work is active. Once it ends, retain the conclusions and supporting detail that future work needs. Keep a failed approach when later work is likely to try it again without knowing why it failed. Retire the rest. [Working context](context.md) covers temporary state while work is active.

[Engineering communication](communication.md) covers how to present the information that remains, whether it is durable or temporary.
