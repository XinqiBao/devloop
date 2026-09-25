# Working Context

Working context has a scope and a lifetime. It helps continue work or an investigation while that need remains active. Durable knowledge remains useful after the work ends because it records facts, constraints, or decisions needed later.

Preserve working context when an interruption, handoff, or later return would otherwise lose useful state that is costly or uncertain to reconstruct from code, commits, documentation, or other durable records. Merely doing work or having an open task is not enough reason to create persistent context.

## Scope

Keep context at the narrowest scope where it remains useful and truthful. Environment-level context may use `~/.context/`; repository-local context may use `<repo>/.context/`; a particular effort may need a narrower location.

These paths are optional conventions, not required destinations. Introduce an entry point or further structure only when retrieval or continuity needs justify it.

## Lifetime

Keep active context current and check it against the relevant environment before relying on it. When work ends or the state becomes stale, remove it from the active path. If a finding remains useful, preserve its distilled form in the appropriate durable location rather than keeping the whole working record active.

Working context is subordinate to tracked project truth. Do not use `.context/` as a prompt, transcript, or routine report archive, or duplicate durable project facts there. Ignored files are neither secret storage nor backup; store secrets appropriately and preserve irreplaceable information in a durable location.
