# xdev

A portable, project-agnostic AI dev workflow using Claude Code CLI.
Standardizes common development processes through slash commands and
persistent development principles.

## What It Does

Three slash commands that standardize AI-assisted development:

- `/xdev-implement` — Handle an issue: fetch → assess → implement → test → PR
- `/xdev-draft` — Draft a well-structured issue from a vague idea
- `/xdev-setup` — Project health check + CLAUDE.md onboarding

Plus a global `CLAUDE.md` with development principles that auto-load
every session.

## Install

```bash
git clone git@github.com:XinqiBao/devloop.git
# Managed via dotfiles — run install script to symlink:
~/git/dotfiles/install-claude.sh
```

## Documentation

- [Status & Improvement Directions](docs/xdev-workflow/STATUS.md)
- [Design Document](docs/xdev-workflow/design.md)
- [Design Decisions](docs/xdev-workflow/decisions.md)

## Archive

The `archive/devloop-scheduler/` directory contains an earlier automated
scheduler design that was superseded by this interactive workflow approach.
