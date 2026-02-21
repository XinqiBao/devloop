import json
import subprocess
import pytest
from pathlib import Path
from unittest.mock import MagicMock
from src.worker import (
    assemble_prompt,
    validate_result,
    ValidationError,
)


def test_assemble_prompt(tmp_path):
    template = tmp_path / "implement.md"
    template.write_text(
        "Issue #{issue_number}: {issue_title}\n\n{issue_body}"
    )
    prompt = assemble_prompt(
        template_path=template,
        issue_number=42,
        issue_title="feat(engine): add stop-loss",
        issue_body="Implement stop-loss order support.",
        project_claude_md="# MyProject\nBuild with cmake.",
    )
    assert "Issue #42" in prompt
    assert "feat(engine): add stop-loss" in prompt
    assert "stop-loss order support" in prompt
    assert "# MyProject" in prompt


def test_assemble_prompt_without_claude_md(tmp_path):
    template = tmp_path / "implement.md"
    template.write_text("Issue #{issue_number}: {issue_title}\n\n{issue_body}")
    prompt = assemble_prompt(
        template_path=template,
        issue_number=1,
        issue_title="test",
        issue_body="body",
    )
    assert "Project Context" not in prompt
    assert "Issue #1" in prompt


def test_validate_result_accepts_good_diff():
    assert validate_result(
        diff_stat="+50 -10",
        changed_files=["src/engine.py", "tests/test_engine.py"],
        commits=["feat(engine): add stop-loss"],
        forbidden_patterns=["*.secret"],
    )


def test_validate_result_rejects_no_changes():
    with pytest.raises(ValidationError, match="no changes"):
        validate_result(
            diff_stat="",
            changed_files=[],
            commits=[],
            forbidden_patterns=[],
        )


def test_validate_result_rejects_mass_deletion():
    with pytest.raises(ValidationError, match="deletion"):
        validate_result(
            diff_stat="+5 -600",
            changed_files=["src/main.py"],
            commits=["refactor: simplify"],
            forbidden_patterns=[],
        )


def test_validate_result_rejects_forbidden_files():
    with pytest.raises(ValidationError, match="forbidden"):
        validate_result(
            diff_stat="+10 -5",
            changed_files=[".github/workflows/ci.yml", "src/main.py"],
            commits=["feat: update ci"],
            forbidden_patterns=[".github/workflows/*"],
        )


def test_validate_result_rejects_bad_commit_message():
    with pytest.raises(ValidationError, match="commit"):
        validate_result(
            diff_stat="+10 -5",
            changed_files=["src/main.py"],
            commits=["updated stuff"],
            forbidden_patterns=[],
        )
