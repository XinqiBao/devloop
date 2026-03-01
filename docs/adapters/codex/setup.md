# Codex Setup

Install shared workflow docs for Codex without forking rules.

## Install / Update

From repository root:

```bash
bash scripts/install-codex.sh
```

Installer behavior:
1. Ensure `~/.agents/skills` exists.
2. Link `~/.agents/skills/devloop -> <repo>/docs`.
3. Print verification commands.

## Verify

```bash
test -L ~/.agents/skills/devloop && echo "link-ok"
readlink ~/.agents/skills/devloop
find -L ~/.agents/skills/devloop -maxdepth 2 -type d | sort
```

## VCS Preflight (Provider-Agnostic)

For environments that will push branches or open PR/MR:

```bash
git remote -v
command -v gh >/dev/null || command -v glab >/dev/null || true
```

Prefer the minimal valid path in current environment:
- SSH push with plain git when possible
- Provider CLI when PR/MR creation is required
- No provider-specific assumptions in base workflow rules

## Local References

- Runtime instructions: `AGENTS.md` (if present in environment)
- Repository guide: `CLAUDE.md`
- Canonical source: `docs/core`, `docs/process`, `docs/adapters`, `docs/governance`
