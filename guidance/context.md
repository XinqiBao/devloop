# Working Context

An interruption, handoff, or later return can lose useful state that is not yet in code or durable project records. Working context preserves that state while the work is active. It is justified when reconstructing the state from code, commits, documentation, or other durable records would be costly, uncertain, or likely to miss something important.

A small change whose state is clear from the diff may need no extra record. A multi-day investigation with unresolved hypotheses, eliminated approaches, and a next meaningful validation step may benefit from a short working note. Having an open task alone does not justify persistent context.

## Scope

Keep context at the narrowest scope where it remains useful and truthful. A local assumption placed in environment-wide guidance can appear to govern unrelated work. Environment-level context may use `~/.context/`; repository-local context may use `<repo>/.context/`; a specific effort may use a narrower location. These are optional conventions, not required destinations or a prescribed directory layout.

## Lifetime and authority

Working context should describe current state. Check it against the present environment before relying on it, especially after an interruption. Stale context can actively mislead by presenting an old assumption, plan, or unresolved issue as current.

When its continuity value ends, remove or retire it from the active path. Distill anything that remains useful into the appropriate durable location, using the judgment in [Durable Knowledge](knowledge.md). Working context is subordinate to tracked project truth; it should not become a second authority for project facts.

Do not use `.context/` as a prompt, transcript, or routine report archive, a duplicate home for durable facts, a secret store, or a backup system. Ignored files are not automatically secret or durable. Store secrets appropriately and preserve irreplaceable information in an appropriate durable location.
