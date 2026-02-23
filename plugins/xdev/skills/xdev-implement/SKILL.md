---
name: xdev-implement
description: >
  You are handling an issue from the project's issue tracker.
argument-hint: "[issue-number]"
---

You are handling an issue from the project's issue tracker.
Follow this SOP strictly. Use $ARGUMENTS as the issue number if provided.

## Step 1: Understand

- Fetch the issue content (title, body, labels, comments).
  Use whatever tool is available (gh, glab, MCP, or ask the user to provide).
- Read the project's CLAUDE.md and understand the codebase structure.
- Dispatch **2 parallel explorer subagents** to map the codebase:
  - Explorer 1: Trace the execution paths related to the issue scope.
    Identify affected files, dependencies, and existing patterns.
  - Explorer 2: Find existing tests, related test infrastructure, and
    code conventions relevant to the change.
- Synthesize explorer findings before proceeding.

## Step 2: Assess Complexity

Before writing any code, assess:
- Is the issue clear enough to implement? If not, ask the user for clarification.
- Are there multiple valid approaches? If yes, dispatch **2 parallel architect
  subagents**, each exploring a different approach with trade-offs.
  Present the approaches to the user and let them choose.
  Do NOT pick one silently.
- Is this too large for a single context? If yes, suggest splitting into
  smaller issues before starting.

## Step 3: Branch and Implement

- Create a feature branch: `<type>/issue-<number>-<short-description>`
- Implement the change following existing codebase patterns.
- Write tests for the change (unless pure documentation).
- Make small, focused commits using Conventional Commits format.

## Step 4: Validate

Before submitting, dispatch **2 parallel reviewer subagents**:
- Reviewer 1 (spec compliance): Verify the implementation matches the
  issue requirements line by line. Check acceptance criteria.
- Reviewer 2 (code quality): Check for bugs, security issues, convention
  violations, unnecessary changes outside scope.

If reviewers find issues, fix them and re-review until both pass.

## Step 5: Submit

- Push the branch and create a merge/pull request linking the issue.
- Title: concise summary. Body: what changed and why.

## Escape Hatch

If at any point:
- The issue is unclear → ask the user, do not guess.
- The implementation risk is too high → explain the risk and stop.
- The scope is larger than expected → suggest splitting into multiple issues.

## Subagent Dispatch Guide

Use the Task tool with these subagent types:
- **Explorers**: `subagent_type: "Explore"` — read-only codebase analysis
- **Architects**: `subagent_type: "Plan"` — design approaches (read-only)
- **Reviewers**: `subagent_type: "general-purpose"` — code review with full tool access

Always provide full context (issue content, relevant file paths, specific
question) in the subagent prompt. Do NOT reference files by path alone.
