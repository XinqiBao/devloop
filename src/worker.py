"""Worker: executes tasks via Claude Code CLI in isolated worktrees."""

from __future__ import annotations

import fnmatch
import json
import logging
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)

CONVENTIONAL_COMMIT_RE = re.compile(
    r"^(feat|fix|refactor|docs|test|chore|perf|build|ci|style|revert)"
    r"(\(.+\))?!?: .+"
)


class ValidationError(Exception):
    """Raised when worker output fails validation."""


class SkipError(Exception):
    """Raised when Claude decides to skip the task."""


@dataclass
class TaskResult:
    success: bool
    pr_url: str | None = None
    error: str | None = None
    skip_reason: str | None = None


def create_worktree(repo_path: Path, branch_name: str, base_ref: str = "origin/master") -> Path:
    """Create an isolated git worktree for a task."""
    worktree_path = repo_path / ".worktrees" / branch_name
    subprocess.run(
        ["git", "fetch", "origin"],
        cwd=repo_path, check=True, capture_output=True,
    )
    subprocess.run(
        ["git", "worktree", "add", "-b", branch_name, str(worktree_path), base_ref],
        cwd=repo_path, check=True, capture_output=True,
    )
    return worktree_path


def remove_worktree(repo_path: Path, branch_name: str) -> None:
    """Remove a git worktree and its branch."""
    worktree_path = repo_path / ".worktrees" / branch_name
    subprocess.run(
        ["git", "worktree", "remove", str(worktree_path), "--force"],
        cwd=repo_path, capture_output=True,
    )
    subprocess.run(
        ["git", "branch", "-D", branch_name],
        cwd=repo_path, capture_output=True,
    )


def assemble_prompt(
    template_path: Path,
    issue_number: int,
    issue_title: str,
    issue_body: str,
    project_claude_md: str = "",
) -> str:
    """Build the full prompt from template + issue + project context."""
    template = template_path.read_text()
    prompt = template.replace("{issue_number}", str(issue_number))
    prompt = prompt.replace("{issue_title}", issue_title)
    prompt = prompt.replace("{issue_body}", issue_body)

    if project_claude_md:
        prompt = f"## Project Context\n\n{project_claude_md}\n\n---\n\n{prompt}"
    return prompt


def run_claude(
    prompt: str,
    working_dir: Path,
    max_turns: int = 30,
    model: str = "claude-opus-4-6",
    timeout_seconds: int = 3600,
) -> dict:
    """Invoke Claude Code CLI in headless mode. Returns parsed JSON output."""
    result = subprocess.run(
        [
            "claude", "-p", prompt,
            "--dangerously-skip-permissions",
            "--max-turns", str(max_turns),
            "--output-format", "json",
            "--model", model,
        ],
        cwd=working_dir,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Claude CLI failed (exit {result.returncode}): {result.stderr}")

    return json.loads(result.stdout)


def _parse_diff_stat(diff_stat: str) -> tuple[int, int]:
    """Parse +N -M from diff stat string into (added, deleted)."""
    added = deleted = 0
    for part in diff_stat.split():
        if part.startswith("+"):
            added += int(part.lstrip("+") or "0")
        elif part.startswith("-"):
            deleted += int(part.lstrip("-") or "0")
    return added, deleted


def validate_result(
    diff_stat: str,
    changed_files: list[str],
    commits: list[str],
    forbidden_patterns: list[str],
    max_deleted_lines: int = 500,
) -> bool:
    """Validate worker output before PR submission. Raises ValidationError on failure."""
    if not changed_files:
        raise ValidationError("Validation failed: no changes produced")

    _, deleted = _parse_diff_stat(diff_stat)
    if deleted > max_deleted_lines:
        raise ValidationError(
            f"Validation failed: excessive deletion ({deleted} lines > {max_deleted_lines} limit)"
        )

    for f in changed_files:
        for pattern in forbidden_patterns:
            if fnmatch.fnmatch(f, pattern):
                raise ValidationError(
                    f"Validation failed: forbidden file modified: {f} (matches {pattern})"
                )

    for msg in commits:
        if not CONVENTIONAL_COMMIT_RE.match(msg):
            raise ValidationError(
                f"Validation failed: bad commit message: '{msg}'"
            )

    return True


def _get_git_info(worktree_path: Path, base_ref: str) -> tuple[str, list[str], list[str]]:
    """Get diff stat, changed files, and commit messages from worktree."""
    diff_stat = subprocess.run(
        ["git", "diff", "--stat", base_ref],
        cwd=worktree_path, capture_output=True, text=True,
    ).stdout.strip()

    changed_files_raw = subprocess.run(
        ["git", "diff", "--name-only", base_ref],
        cwd=worktree_path, capture_output=True, text=True,
    ).stdout.strip()
    changed_files = [f for f in changed_files_raw.splitlines() if f]

    commits_raw = subprocess.run(
        ["git", "log", "--format=%s", f"{base_ref}..HEAD"],
        cwd=worktree_path, capture_output=True, text=True,
    ).stdout.strip()
    commits = [c for c in commits_raw.splitlines() if c]

    return diff_stat, changed_files, commits


def _create_pr(
    worktree_path: Path,
    branch_name: str,
    issue_number: int,
    issue_title: str,
    repo: str,
) -> str:
    """Push branch and create PR. Returns PR URL."""
    subprocess.run(
        ["git", "push", "-u", "origin", branch_name],
        cwd=worktree_path, check=True, capture_output=True,
    )
    result = subprocess.run(
        [
            "gh", "pr", "create",
            "--repo", repo,
            "--title", issue_title,
            "--body", f"Closes #{issue_number}\n\nAutomated implementation by devloop.",
            "--head", branch_name,
        ],
        cwd=worktree_path, capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def execute_task(
    repo_path: Path,
    repo: str,
    issue_number: int,
    issue_title: str,
    issue_body: str,
    prompts_dir: Path,
    max_turns: int = 30,
    model: str = "claude-opus-4-6",
    forbidden_patterns: list[str] | None = None,
    timeout_seconds: int = 3600,
) -> TaskResult:
    """Full task execution: worktree -> claude -> validate -> PR."""
    branch_name = f"devloop/issue-{issue_number}"
    forbidden = forbidden_patterns or []
    worktree_path = None

    try:
        worktree_path = create_worktree(repo_path, branch_name)
        log.info("Created worktree at %s", worktree_path)

        claude_md_path = worktree_path / "CLAUDE.md"
        project_claude_md = claude_md_path.read_text() if claude_md_path.exists() else ""

        prompt = assemble_prompt(
            template_path=prompts_dir / "implement.md",
            issue_number=issue_number,
            issue_title=issue_title,
            issue_body=issue_body,
            project_claude_md=project_claude_md,
        )
        output = run_claude(
            prompt, worktree_path,
            max_turns=max_turns, model=model,
            timeout_seconds=timeout_seconds,
        )

        result_text = output.get("result", "")
        if result_text.strip().startswith("SKIP"):
            reason = result_text.strip().removeprefix("SKIP:").strip()
            return TaskResult(success=False, skip_reason=reason)

        base_ref = "origin/master"
        diff_stat, changed_files, commits = _get_git_info(worktree_path, base_ref)
        validate_result(diff_stat, changed_files, commits, forbidden)

        pr_url = _create_pr(worktree_path, branch_name, issue_number, issue_title, repo)
        log.info("PR created: %s", pr_url)

        return TaskResult(success=True, pr_url=pr_url)

    except (ValidationError, SkipError, RuntimeError, subprocess.TimeoutExpired) as e:
        log.error("Task failed for issue #%d: %s", issue_number, e)
        return TaskResult(success=False, error=str(e))

    finally:
        if worktree_path:
            remove_worktree(repo_path, branch_name)
