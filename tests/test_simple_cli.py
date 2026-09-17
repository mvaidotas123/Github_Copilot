import subprocess
import sys
import unittest
from pathlib import Path

from simple_cli import build_message


REPO_ROOT = Path(__file__).resolve().parents[1]


class SimpleCliTests(unittest.TestCase):
    def test_build_message_returns_expected_text(self):
        self.assertEqual(build_message("Alice", 2, 3), "Hello, Alice! 2 + 3 = 5")

    def test_cli_prints_expected_output(self):
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "simple_cli.py"), "--name", "Bob", "4", "5"],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.stdout.strip(), "Hello, Bob! 4 + 5 = 9")


if __name__ == "__main__":
    unittest.main()
