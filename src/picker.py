"""Issue picker: fetch and prioritize GitHub issues."""

from __future__ import annotations

import json
import logging
import subprocess
from dataclasses import dataclass

from src.config import ProjectConfig

log = logging.getLogger(__name__)


@dataclass
class Issue:
    number: int
    title: str
    body: str
    labels: list[str]
    created_at: str


def _run_gh(args: list[str]) -> str:
    """Run a gh CLI command and return stdout."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True, text=True, check=True,
    )
    return result.stdout


def fetch_issues(project: ProjectConfig) -> list[Issue]:
    """Fetch open issues from a GitHub repository."""
    raw = _run_gh([
        "issue", "list",
        "--repo", project.repo,
        "--state", "open",
        "--json", "number,title,body,labels,createdAt",
        "--limit", "50",
    ])
    items = json.loads(raw)
    return [
        Issue(
            number=item["number"],
            title=item["title"],
            body=item.get("body", ""),
            labels=[l["name"] for l in item.get("labels", [])],
            created_at=item.get("createdAt", ""),
        )
        for item in items
    ]


def _has_existing_pr(repo: str, issue_number: int) -> bool:
    """Check if an issue already has a linked PR."""
    try:
        raw = _run_gh([
            "pr", "list",
            "--repo", repo,
            "--search", f"#{issue_number}",
            "--json", "number",
            "--limit", "5",
        ])
        prs = json.loads(raw)
        return len(prs) > 0
    except subprocess.CalledProcessError:
        return False


def _score_issue(issue: Issue, project: ProjectConfig) -> float:
    """Score an issue for prioritization. Higher = better."""
    score = 0.0
    for label in issue.labels:
        if label in project.labels_include:
            score += 10.0
    score += 1.0
    return score


def pick_issue(project: ProjectConfig) -> Issue | None:
    """Pick the highest-priority actionable issue from a project."""
    issues = fetch_issues(project)

    candidates = []
    for issue in issues:
        if any(label in project.labels_exclude for label in issue.labels):
            continue
        if project.labels_include:
            if not any(label in project.labels_include for label in issue.labels):
                continue
        candidates.append(issue)

    if not candidates:
        return None

    candidates.sort(key=lambda i: (-_score_issue(i, project), i.created_at))
    return candidates[0]
