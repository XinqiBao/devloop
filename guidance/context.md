# Working Context

Working context preserves useful state that is not yet in code or durable project records. Use it when an interruption or later return would make that state costly, uncertain, or unreliable to reconstruct. It is optional: a small change clear from its diff may need no extra record, while a multi-day investigation with unresolved hypotheses and a next validation step may benefit from a short note. An open task alone does not justify a persistent note.

## Scope and authority

Keep context at the narrowest scope where it remains useful and truthful. A local assumption placed in environment-wide guidance can appear to govern unrelated work. Environment-level context may use `~/.context/`; repository-local context may use `<repo>/.context/`; a specific effort may use a narrower location. These are possible locations, not a required layout.

Working context is subordinate to tracked project truth. Check it against the present environment before relying on it, especially after an interruption. A stale assumption, plan, or unresolved issue can misdirect later work.

## Retire or promote

Keep working context current while it helps continuity. When that need ends, remove it from the active path. Distill any lasting conclusion into its proper durable location using [Durable Knowledge](knowledge.md); do not leave a second authority for project facts.

Do not use `.context/` as a prompt or transcript archive, a routine report store, a duplicate home for durable facts, a secret store, or a backup system. Ignored files are not automatically secret or durable; store secrets and irreplaceable information in appropriate locations.
