# Self-Improvement Loop

This project serves two functions:
1. Deploy shared skills/workflow to Claude and Codex.
2. Improve itself through continuous, evidence-based iteration.

## Loop

1. Observe friction in real usage.
2. Capture one concrete problem.
3. Propose the smallest rule/doc/tooling update.
4. Verify with command evidence.
5. Record decision/changelog updates.

## Triggers

Run this loop when:
- setup or onboarding is confusing,
- provider/tool auth fails repeatedly,
- workflow steps are skipped in practice,
- docs become hard to read.

## Information Sources (curated)

Official docs first:
- Claude Code docs: `https://docs.anthropic.com/en/docs/claude-code`
- Claude plugin marketplace/docs: `https://github.com/anthropics/claude-plugins-official`
- GitHub CLI docs: `https://cli.github.com/manual/`
- GitLab CLI docs: `https://gitlab.com/gitlab-org/cli`
- Git reference docs: `https://git-scm.com/docs`

Release signals:
- Claude Code release notes: `https://github.com/anthropics/claude-code/releases`
- Tooling release notes (`gh`, `glab`, language servers)

Community signals (for ideas, not authority):
- curated plugin/skill lists
- practitioner writeups with concrete examples

## Guardrails

- Keep provider-specific details in adapters only.
- Keep core/process provider-agnostic.
- Prefer deleting stale guidance over archiving it in active paths.
- If an improvement cannot be verified, do not merge it.
