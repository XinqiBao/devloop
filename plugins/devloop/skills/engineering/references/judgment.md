# Engineering Judgment

Engineering decisions depend on the requested change, the system as it works now, and the evidence found during the work. The judgments below interact; they are not a sequence of steps or a set of required artifacts.

## Investigate in proportion to the decision

Inspect the affected behavior, instructions, state, and system boundaries before a consequential change. In an existing workspace, identify work already in progress before editing so you do not overwrite, revert, or include it in your change. Separate observations from assumptions. A task description may be stale, and a local view of the code may miss an important caller or constraint.

The case for further investigation grows with:

- **Uncertainty:** how much of the relevant behavior or constraint is still inferred rather than observed.
- **Impact:** how many users, paths, or components the change could affect.
- **Difficulty of reversal:** whether the change can be undone without further disruption.
- **Recovery cost:** what it would take to detect and repair a failure.

For example:

- A small documentation correction may need a targeted read and a link check.
- A change to shared runtime behavior may require tracing callers, checking integration boundaries, and observing current behavior.

Stop when further investigation is unlikely to change the decision; investigation also has a cost.

## Design for the actual need

Start from the intended capabilities and constraints, then assess whether the current design serves them. Existing code is evidence about the system, not sufficient reason to retain its structure. Evaluate proposed solutions, including the owner's suggestions, against the need; stay within the authorized scope of redesign.

Judge simplicity by the cost of understanding, operating, verifying, and changing the result. A short patch that hides failures or introduces hidden coupling can cost more than a direct implementation. Preserve required behavior and useful reasoning when simplifying.

Prefer independently understandable boundaries. Share code or split files when it improves understanding, ownership, or maintenance; uniformity alone is not a reason to couple independent components. Small cohesive configuration can stay inline.

Respect independently configured components. Improving one tool does not give it ownership of another plugin's settings or the user's surrounding environment. Prefer controls within the owned component; accept a bounded limitation when the alternative is unwanted coupling. Deliberate integration can be valid when it is part of the intended product contract. Similarly, contributor tooling should not become a product runtime dependency without a user-facing need.

## Keep task boundaries distinct

Establish the answers that matter to the work:

- **Outcome:** what needs to change.
- **Authority:** what you are allowed to change.
- **Constraints:** which existing requirements limit the solution.
- **Completion:** what would count as a satisfactory result.

A technically sound change can still solve the wrong problem or exceed the authority given. Use these boundaries during the work:

- Ask the owner when plausible interpretations materially change the outcome, risk, or authority needed.
- Within clear bounds, make routine implementation choices and continue through verification and ordinary repair.
- Revisit the owner decision if new evidence would materially expand the task.

Keep decision provenance honest. A recommendation accepted for the current task is not automatically a strong owner preference or a permanent requirement. Distinguish explicit intent from repository constraints, provisional choices, and inference when that distinction affects later decisions. A local trial does not establish an adopted portable default.

## Match claims to evidence

Evidence supports only what it actually checks. Choose the least costly checks or observations that cover the relevant failure risk:

- A passing unit test supports the behavior it exercises; it does not establish that an integration path works.
- A successful build establishes that the build succeeds; it does not establish correct runtime behavior.

Report what you checked, what relevant behavior remains unchecked, and any material uncertainty. Claim completion only at the scope the evidence supports. If a check fails, a new caller appears, or runtime behavior contradicts the diagnosis, revise the plan, implementation, or completion claim.

Verification checks whether the result holds; it is not a fixed set of gates.

Review against the intended outcome, supported behavior, and relevant constraints. Ground findings in concrete failures, violated requirements, or meaningful maintenance costs. Distinguish defects from optional improvements and stylistic alternatives; a suggestion is not automatically a reason to change the implementation. A review with no warranted changes is a valid result; do not pad it with unrelated suggestions.

Tests also have a maintenance cost. Protect supported contracts, meaningful state transitions, and consequential failure paths. Avoid assertions that merely mirror implementation structure and obstruct valid changes. During rapid iteration, run focused checks; complete the relevant delivery checks once the result is ready rather than rerunning every passed suite after each small edit.

## Preserve only the state needed to resume

Small work may already be recoverable from the code, diff, and history. Longer or uncertain work may need a brief current record of important findings, unresolved decisions, and next useful steps when reconstructing them would be costly or unreliable.

Keep such a record current and limited to the continuity need. Plans and progress notes are aids, not required deliverables. [knowledge](../../knowledge/SKILL.md) covers temporary state in more detail.

## Evaluate persistent mechanisms

Before adding a rule, script, hook, skill, abstraction, or dependency, check whether native capabilities and engineering judgment meet the need. A persistent mechanism adds costs for future contributors:

- Finding it when it matters.
- Understanding and using it correctly.
- Maintaining it as the system changes.
- Diagnosing failures it introduces or obscures.

A mechanism is worthwhile when it reliably reduces a recurring burden enough to justify those costs. A one-off inconvenience is weaker evidence. Judge the continuing benefit and cost, not whether the mechanism is custom or automated.

Prefer upstream-supported usage when it meets the need: upstream is more likely to maintain that path, while custom glue can drift. Verify the relevant limitation before adding a workaround. Keep it within the affected boundary and retain why it is needed and what would allow its removal; do not turn an environment-specific workaround into a product requirement.

Newness alone does not justify migration. Compatibility layers, fallback paths, and configurability should answer a real audience need; optional capability can be omitted when its continuing burden is greater than its value.
