# Applying devloop

Apply the engineering judgment relevant to the target environment, not devloop's file layout. The result should make sense to that environment's engineers and agents without access to this checkout.

## Understand the target

Inspect the target's existing instructions, conventions, native capabilities, and legitimate constraints. They show where guidance already works, where a gap exists, and which authority governs the decision. Adding a parallel devloop-shaped layer where the same judgment is already expressed can create conflicting instructions and make the current source harder to find.

Determine whether the task calls for a review, selective application, or broader adoption. Full adoption means the relevant principles are effectively represented, not that the target mirrors this repository. A review may end in findings, and no change may be the right conclusion when the target already expresses the relevant judgment well.

## Express the guidance

Put a missing principle where its intended readers will naturally find and use it. That may be an existing project guidance file, native agent configuration, or several existing locations with distinct responsibilities. For example, if engineers and agents already consult a project guidance file, add a missing engineering principle there rather than creating a parallel devloop directory. Keep provider and tool settings in their native configuration.

Select only the guidance that fits the target's needs and authority. Reconcile differences when both intents can be preserved. When two legitimate requirements cannot both be satisfied, or the choice would materially change the intended behavior, surface the conflict for an owner decision rather than silently overriding target-specific direction.

## Check the result

Review the resulting guidance for conflicts, duplication, and references to this checkout. Check links and, where practical, confirm that its intended readers or agents can discover and use it.
