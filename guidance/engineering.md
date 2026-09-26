# Engineering Judgment

Engineering decisions depend on the requested change, the system as it works now, and the evidence found during the work. The judgments below interact; they are not a sequence of steps or a set of required artifacts.

## Investigate in proportion to the decision

Inspect the affected behavior, instructions, state, and system boundaries before a consequential change. Separate observations from assumptions: a task description may be stale, and a local view of the code may miss an important caller or constraint.

The case for further investigation grows with:

- **Uncertainty:** how much of the relevant behavior or constraint is still inferred rather than observed.
- **Impact:** how many users, paths, or components the change could affect.
- **Difficulty of reversal:** whether the change can be undone without further disruption.
- **Recovery cost:** what it would take to detect and repair a failure.

A small documentation correction may need a targeted read and a link check. Shared runtime behavior may require tracing callers, checking integration boundaries, and observing the current behavior. Stop when further investigation is unlikely to change the decision; investigation also has a cost.

## Keep task boundaries distinct

Establish the answers that matter to the work:

- **Outcome:** what needs to change.
- **Authority:** what you are allowed to change.
- **Constraints:** which existing requirements limit the solution.
- **Completion:** what would count as a satisfactory result.

A technically sound change can still solve the wrong problem or cross an authority boundary. Ask for an owner decision when plausible interpretations materially change the outcome, risk, or authority needed. Within clear bounds, make routine implementation choices and continue through verification and ordinary repair. Revisit the owner decision if new evidence would materially expand the task.

## Match claims to evidence

Evidence supports only what it actually checks. Choose observations and checks for the claims and risks that matter:

- A passing unit test supports the behavior it exercises; it does not establish that an integration path works.
- A successful build establishes that the build succeeds; it does not establish correct runtime behavior.

State completion and remaining uncertainty at the scope the evidence permits. A failing check, newly discovered caller, or contrary runtime observation may change the diagnosis, plan, implementation, or an earlier completion claim. Revise those conclusions when the evidence changes. Verification is a way to learn whether the result holds, not a fixed set of gates.

## Preserve only the state needed to resume

Small work may already be recoverable from the code, diff, and history. Longer or uncertain work may need a brief current record of important findings, unresolved decisions, and next useful steps when reconstructing them would be costly or unreliable.

Keep such a record current and limited to the continuity need. Plans and progress notes are aids, not required deliverables. [Working context](context.md) covers temporary state in more detail.

## Make persistent mechanisms earn their cost

Before adding a rule, script, hook, skill, abstraction, or dependency, check whether native capabilities and engineering judgment meet the need. A persistent mechanism adds costs for future contributors:

- finding it when it matters;
- understanding and using it correctly;
- maintaining it as the system changes;
- diagnosing failures it introduces or obscures.

A mechanism is worthwhile when it reliably reduces a recurring burden enough to justify those costs. A one-off inconvenience is weaker evidence. Judge the continuing benefit and cost, not whether the mechanism is custom or automated.
