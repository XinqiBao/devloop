"""Exercise the declared hook through a real shell without a model call or user configuration."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
PACKAGE = REPO / "plugins" / "devloop"


class CoreLoadingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="devloop-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "plugin with spaces and 'quotes'"
        shutil.copytree(PACKAGE / "hooks", self.root / "hooks")
        self.core = self.root / "skills/engineering/SKILL.md"
        self.core.parent.mkdir(parents=True)
        self.write_core("# Fixture guidance\n\nKeep this paragraph.\n\n---\n\nAnd this one.")
        self.cwd = Path(self.temp.name) / "unrelated project"
        self.cwd.mkdir()

    def write_core(self, body):
        self.core.write_text(
            "---\nname: engineering\ndescription: Test metadata only.\n---\n\n"
            + body + "\n"
        )

    def declared_session_start(self, root):
        config = json.loads((root / "hooks/hooks.json").read_text())
        return config["hooks"]["SessionStart"][0]

    def declared_hook_command(self, root):
        hook = self.declared_session_start(root)["hooks"][0]
        return hook["command"]

    def run_hook(self, *, source="startup", set_root=True, root=None):
        root = self.root if root is None else root
        env = os.environ.copy()
        env.pop("CLAUDE_PLUGIN_ROOT", None)
        if set_root:
            env["CLAUDE_PLUGIN_ROOT"] = str(root)
        return subprocess.run(
            self.declared_hook_command(root),
            shell=True,
            executable="/bin/sh",
            cwd=self.cwd,
            env=env,
            text=True,
            capture_output=True,
            input=json.dumps({"hook_event_name": "SessionStart", "source": source}),
            timeout=5,
        )

    def test_declared_hook_reads_installed_source_outside_checkout(self):
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(str(self.core), result.stdout)
        self.assertIn(str(self.core.parent), result.stdout)
        self.assertIn("# Fixture guidance\n\nKeep this paragraph.\n\n---\n\nAnd this one.", result.stdout)
        self.assertNotIn("Test metadata only", result.stdout)
        self.assertEqual(list(self.cwd.iterdir()), [])

    def test_declared_hook_loads_actual_engineering_body(self):
        core = PACKAGE / "skills/engineering/SKILL.md"
        result = self.run_hook(root=PACKAGE)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(str(core), result.stdout)
        self.assertIn("devloop:engineering source:", result.stdout)
        self.assertIn("# Engineering Defaults", result.stdout)
        self.assertNotIn("description:", result.stdout)
        self.assertEqual(list(self.cwd.iterdir()), [])

    def test_next_load_reads_changed_source(self):
        self.run_hook()
        self.write_core("# Updated guidance\n\nNew source content.")
        result = self.run_hook(source="compact")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("New source content.", result.stdout)
        self.assertNotIn("Keep this paragraph.", result.stdout)

    def test_missing_or_empty_core_reports_failure_without_policy_output(self):
        self.core.unlink()
        missing = self.run_hook()
        self.assertNotEqual(missing.returncode, 0)
        self.assertEqual(missing.stdout, "")
        self.assertIn(str(self.core), missing.stderr)
        self.write_core("")
        empty = self.run_hook()
        self.assertNotEqual(empty.returncode, 0)
        self.assertEqual(empty.stdout, "")
        self.assertTrue(empty.stderr)

    def test_missing_plugin_root_reports_failure(self):
        result = self.run_hook(set_root=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertTrue(result.stderr)


if __name__ == "__main__":
    unittest.main()
