import json
import pytest
from unittest.mock import patch
from src.picker import fetch_issues, pick_issue, Issue
from src.config import ProjectConfig


SAMPLE_ISSUES_JSON = json.dumps([
    {"number": 1, "title": "feat: old feature", "body": "desc",
     "labels": [{"name": "auto"}], "createdAt": "2026-01-01T00:00:00Z"},
    {"number": 2, "title": "fix: urgent bug", "body": "desc",
     "labels": [{"name": "auto"}, {"name": "devloop"}], "createdAt": "2026-02-01T00:00:00Z"},
    {"number": 3, "title": "chore: cleanup", "body": "desc",
     "labels": [{"name": "needs-discussion"}], "createdAt": "2026-02-15T00:00:00Z"},
])

PROJECT = ProjectConfig(
    name="Test", repo="owner/repo", local_path="/tmp/repo",
    labels_include=["auto", "devloop"],
    labels_exclude=["needs-discussion", "wontfix"],
)


@patch("src.picker._run_gh")
def test_fetch_issues(mock_gh):
    mock_gh.return_value = SAMPLE_ISSUES_JSON
    issues = fetch_issues(PROJECT)
    assert len(issues) == 3
    assert issues[0].number == 1


@patch("src.picker._run_gh")
def test_pick_issue_excludes_labels(mock_gh):
    mock_gh.return_value = SAMPLE_ISSUES_JSON
    issue = pick_issue(PROJECT)
    assert issue is not None
    assert issue.number != 3


@patch("src.picker._run_gh")
def test_pick_issue_prefers_more_matching_labels(mock_gh):
    mock_gh.return_value = SAMPLE_ISSUES_JSON
    issue = pick_issue(PROJECT)
    assert issue is not None
    assert issue.number == 2


@patch("src.picker._run_gh")
def test_pick_issue_returns_none_when_empty(mock_gh):
    mock_gh.return_value = "[]"
    issue = pick_issue(PROJECT)
    assert issue is None
