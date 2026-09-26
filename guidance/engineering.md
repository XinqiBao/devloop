# Engineering Work

Engineering decisions depend on the requested change, the system as it works today, and the evidence found during the work. The guidance below applies throughout a change. It does not prescribe a sequence of steps or required artifacts.

## Investigate what matters

Before a consequential change, inspect the affected behavior, instructions, current state, and system boundaries. A description may be stale. A small part of the code may not show how the whole path works. Distinguish what you observed from what you assume before basing a change on it.

Investigate more when you are less certain how the system works, the change affects more of it, or failure would be difficult to reverse or recover from. A small documentation correction may need only a targeted read and a link check. Changing shared runtime behavior may require tracing callers, checking integration boundaries, and observing the current behavior. Stop when further investigation is unlikely to change the decision; reading everything also has a cost.

## Know the task and its limits

Establish what needs to change, what you are allowed to change, which constraints apply, and how you will know the task is done. These are separate questions. A technically sound solution can still solve the wrong problem or change something outside the authorized scope.

Ask for a decision when different interpretations would materially change the result, risk, or authority needed. Make minor implementation choices within clear bounds and carry the work through verification and ordinary repair. If new evidence changes the intended outcome, scope, or risk, revisit the decision with the owner before expanding the task.

## Check what the evidence proves

Choose checks that address the important claims and risks. A passing unit test supports the behavior it exercises; it does not prove that an integration path works. A successful build does not prove that runtime behavior is correct. Do not claim more than the evidence shows, and state any remaining uncertainty that matters.

A failing check, a newly discovered caller, or a contrary runtime observation may change the diagnosis or the plan. It may also reopen a task previously thought complete. Revise the conclusion when evidence changes. Verification is part of learning whether the intended result holds, not a fixed set of gates at the end.

## Keep longer work resumable

Leave enough information to resume work after an interruption. For a small change, the code, diff, and history may already be enough. For longer or uncertain work, record unresolved decisions, important findings, and next steps if reconstructing them later would be costly or unreliable.

Keep that record current and limited to what resuming the work requires. Plans and progress notes are aids, not required deliverables. [Working context](context.md) explains when temporary state deserves its own place and when to retire it.

## Add mechanisms when they earn their cost

Before adding a rule, script, hook, skill, abstraction, or dependency, check whether existing tools and engineering judgment already meet the need. Every new mechanism requires future contributors to find, understand, debug, and maintain it.

That cost may be worthwhile when a recurring problem causes errors or inconsistent work and a mechanism reliably reduces the burden. A one-off inconvenience is weaker evidence. Compare the continuing benefit with the cost of keeping the mechanism useful as the system changes.
