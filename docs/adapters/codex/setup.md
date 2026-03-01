# Codex Setup

This setup installs shared skills for Codex while keeping `devloop` as source of truth.

## Install / Update

From repository root:

```bash
bash scripts/install-codex.sh
```

What the installer does:
1. Ensure `~/.agents/skills` exists.
2. Create/update symlink:
   - `~/.agents/skills/devloop -> <repo>/docs`
3. Print follow-up verification commands.

## GitHub Auth (for push + PR automation)

If this environment needs to push branch changes or open PRs:

```bash
gh auth status -h github.com
# if token is invalid/missing:
gh auth login -h github.com -p https -w
gh auth setup-git
```

Notes:
- HTTPS remotes require valid GitHub credentials (personal access token via helper/OAuth), not account password.
- In sandboxed/isolated runtimes, host keychain credentials may be unavailable; run auth in your local shell.
- Re-check with `gh auth status -h github.com` before PR automation.

## Manual Install (fallback)

```bash
mkdir -p ~/.agents/skills
ln -sfn "$(pwd)/docs" ~/.agents/skills/devloop
```

## Verify

```bash
test -L ~/.agents/skills/devloop && echo "link-ok"
readlink ~/.agents/skills/devloop
find -L ~/.agents/skills/devloop -maxdepth 2 -type d | sort
gh auth status -h github.com
```

Expected:
- Symlink exists and points to current repository `docs` directory.
- Core/process/adapters/governance directories are discoverable through link.
- GitHub auth status is valid when push/PR actions are required.

## Local Config References

- Repository-level runtime instructions: `AGENTS.md`
- Project guidance entry point: `CLAUDE.md`
- Canonical workflow source: `docs/core`, `docs/process`, `docs/adapters`, `docs/governance`

Keep local config thin: reference canonical docs instead of duplicating policy text.
