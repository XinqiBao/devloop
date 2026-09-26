# Engineering Work

Good engineering decisions depend on the task's intent, the system as it exists, and the evidence that emerges. The principles below interact throughout a change. They guide judgment; they are not ordered stages or required artifacts.

## Work from relevant reality

Before a consequential change, inspect the behavior, instructions, state, and boundaries that could affect it. A description may be stale, and an architecture inferred from a small part of the code may be wrong. Separate what you observed from what you assume so that an unverified belief does not quietly become the basis for a change.

Investigation should be proportional to the decision. Greater uncertainty, wider impact, harder reversal, or higher recovery cost call for stronger evidence. A local documentation correction that is easy to undo may need only a targeted read and a link check. A change to shared runtime behavior may require tracing callers, checking integration boundaries, and observing the behavior it will replace. Neither case benefits from reading everything: investigation has a cost, and its purpose is to reduce uncertainty that matters to the decision.

## Preserve intent and authority

Keep the requested outcome, authorized scope, legitimate constraints, and meaningful success conditions together. They answer different questions: what should change, what you may change, what limits the solution, and what would count as a satisfactory result. A technically sound change can still be wrong if it solves a different problem or crosses an authority boundary.

Clarify ambiguity when plausible interpretations would materially change the result, risk, or authority needed. Minor implementation choices within clear bounds usually do not need a handoff. Once the important boundaries are understood, continue through implementation, verification, and ordinary repair. Autonomy does not extend to silently expanding the task: new evidence that changes the intended outcome, scope, or risk may require another decision from the owner.

## Let evidence revise the work

Choose checks and observations for the claims and risks that matter. A passing unit test supports the behavior it exercises; it does not establish that an integration path works. A successful build establishes that the build succeeded, not that runtime behavior is correct. State conclusions at the same scope as their evidence, including meaningful uncertainty that remains.

Evidence can change more than the implementation. A failing check, a newly discovered caller, or a contrary runtime observation may invalidate the diagnosis, the plan, or an earlier completion claim. Revisit those conclusions instead of treating them as commitments. Verification is a way to learn whether the intended result holds, not a fixed set of gates to perform after the work.

## Keep substantial work recoverable

Work should remain understandable and resumable if interrupted. For a small change, the code, diff, and history may already show enough. A longer or uncertain effort may need a brief current record of unresolved decisions, important findings, and next useful steps when reconstructing them would be costly or unreliable.

Preserve only the state that continuity needs, and revise it when evidence changes. Plans and progress notes are aids, not required deliverables. [Working context](context.md) explains when temporary state deserves its own place and when it should be retired.

## Prefer judgment and native capability

Before adding a rule, script, hook, skill, abstraction, dependency, or other persistent mechanism, consider whether existing tools and informed judgment already handle the need. A new mechanism becomes part of the engineering surface: future contributors must find it, understand it, follow it, debug it, and keep it correct as the environment changes.

That cost can be justified. A recurring problem that repeatedly causes errors or inconsistent work may warrant automation or a durable rule, especially when the mechanism reliably reduces the burden. A one-off inconvenience gives weaker evidence. Judge a mechanism by the benefit it continues to provide relative to its ongoing cost, not by whether automation or simplicity is inherently preferable.
