# xdev

General-purpose AI dev workflow using Claude Code CLI.

## Quick Reference

- Status & direction: `docs/xdev-workflow/STATUS.md`
- Design doc: `docs/xdev-workflow/design.md`
- Decisions: `docs/xdev-workflow/decisions.md`

## Project Structure

- `docs/xdev-workflow/` — All design and status documents
- `plugins/xdev/` — xdev plugin (skills, hooks, scripts)
- `.claude-plugin/` — Personal marketplace manifest
- `archive/devloop-scheduler/` — Archived automated scheduler (not active)

## Working on This Project

This project defines a workflow, not application code. Changes are
typically to documentation and plugin files (`plugins/xdev/`).
Read `docs/xdev-workflow/STATUS.md` first to understand current state
and improvement directions.

After making changes, update STATUS.md and commit to preserve progress.
