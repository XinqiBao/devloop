# Working Context

Working context has a scope and a lifetime. Keep it at the narrowest scope where it remains useful and truthful, and subordinate it to durable tracked project truth.

Environment-level context may use `~/.context/`; repository-local context may use `<repo>/.context/`; active work may need a narrower location. These are optional conventions, not structures other projects or users must adopt. Introduce an entry point or further organization only when retrieval or continuity needs justify it.

Keep active context current and check it against the relevant environment before relying on it. Move completed or stale state out of the active path. Do not turn `.context/` into a prompt, transcript, or report archive, or duplicate durable project facts there.

Ignored files are neither secret storage nor backup. Store secrets appropriately and preserve irreplaceable information in a durable location.
