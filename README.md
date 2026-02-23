# xdev

A portable, project-agnostic AI dev workflow for personal projects using
Claude Code CLI.

## What It Does

Three slash commands that standardize AI-assisted development:

- `/xdev-implement` — Handle an issue: fetch → assess → implement → test → PR
- `/xdev-draft` — Draft a well-structured issue from a vague idea
- `/xdev-setup` — Project health check + CLAUDE.md onboarding

Plus a global `CLAUDE.md` with development principles that auto-load every session.

## Install

```bash
git clone git@github.com:XinqiBao/devloop.git
cd devloop
# Files are also managed via dotfiles:
# ~/git/dotfiles/install-claude.sh
```

## Documentation

- [Status & What's Next](docs/xdev-workflow/STATUS.md)
- [Design Document](docs/xdev-workflow/design.md)
- [Design Decisions](docs/xdev-workflow/decisions.md)

## Archive

The `archive/devloop-scheduler/` directory contains an earlier automated
scheduler design. The interactive xdev workflow replaced it as the
primary approach.
