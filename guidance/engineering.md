# Engineering Work

Engineering decisions should follow the task's intent, the system's actual behavior, and the evidence that emerges. The principles below guide judgment rather than prescribe a sequence of steps.

## Work from relevant reality

Inspect the affected behavior, instructions, state, and boundaries before consequential changes. Distinguish what was observed from what is assumed.

A small, reversible change may need only a few targeted checks; higher uncertainty, impact, or recovery cost calls for deeper investigation. The aim is enough evidence for the decision, not exhaustive reading.

## Preserve intent and authority

Keep the requested outcome, authorized scope, legitimate constraints, and meaningful success conditions in view. Clarify ambiguity that could change the result or exceed authority.

Once these are clear, continue through implementation, verification, and ordinary repair without routine handoffs. Surface a material change in risk or intent rather than silently redefining the task.

## Let evidence revise the work

Choose tests, review, and observations that address the change's meaningful risks. A passing check supports only what it actually covers; a failing check or contrary observation may require revising the plan or reopening a previous conclusion. Explain remaining uncertainty when claiming completion.

## Keep substantial work recoverable

Leave enough coherent progress and current working state for the work to be understood and resumed after an interruption. A short change may need none beyond the code and commit history; longer work may need a brief record of open decisions and next steps. Plans and progress files are aids when needed, not required artifacts.

## Prefer judgment and native capability

Use existing tools and engineering judgment before adding a rule, script, hook, skill, abstraction, or dependency. A permanent mechanism becomes something future work must discover, understand, obey, debug, and keep correct. That cost can be worthwhile when the mechanism repeatedly reduces risk, effort, or inconsistency. A one-off inconvenience is usually weak evidence for adding one.
