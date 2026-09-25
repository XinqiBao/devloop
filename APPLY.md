# Applying devloop

Apply relevant guidance, not devloop's file structure. The source documents organize ideas for reading; they do not prescribe the target environment's files or configuration.

## Understand the target

Read the relevant guidance and inspect the target's existing instructions, capabilities, and legitimate constraints. Determine whether the request calls for full adoption, selective adoption, or review only.

Clarify intent when different interpretations would materially change the result. Reconcile genuine conflicts and surface those that remain unresolved.

## Express the guidance

Keep only the persistent guidance that is useful in the target environment. It may fit in one existing file, several files, native agent configuration, or an environment-level guidance location. It may require no change when already expressed effectively. Put provider and tool settings in their native configuration.

The result must work without access to the devloop checkout.

## Verify the result

Check references and, where practical, confirm that the intended agents can discover and use the guidance. A review-only request can end with findings or a no-change conclusion.
