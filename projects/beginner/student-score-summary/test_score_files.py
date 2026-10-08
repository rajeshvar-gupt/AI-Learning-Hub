import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from score_files import load_scores, save_scores


class ScoreFileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "scores.txt"

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, str(Path(__file__).with_name("score_files.py")), *map(str, args)],
            capture_output=True, text=True, timeout=5,
        )

    def test_round_trip_and_format(self):
        scores = [0, 70, 100, 70]
        save_scores(self.path, scores)
        self.assertEqual(self.path.read_bytes(), b"0\n70\n100\n70\n")
        self.assertEqual(load_scores(self.path), scores)

    def test_empty_file(self):
        save_scores(self.path, [])
        self.assertEqual(load_scores(self.path), [])

    def test_existing_file_preserved(self):
        self.path.write_text("80\n", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            save_scores(self.path, [90])
        self.assertEqual(self.path.read_text(), "80\n")
        result = self.cli("save", self.path, "90")
        self.assertEqual(result.returncode, 1)
        self.assertIn("already exists", result.stderr)

    def test_invalid_save_does_not_create_file(self):
        for scores in [[50, 101], [-1], [80.5], [True], ["80"]]:
            with self.subTest(scores=scores):
                with self.assertRaises(ValueError):
                    save_scores(self.path, scores)
                self.assertFalse(self.path.exists())

    def test_invalid_lines_fail_with_line_number(self):
        for bad in ["abc", "", "82.5", "-1", "101"]:
            with self.subTest(bad=bad):
                self.path.write_text(f"70\n{bad}\n90\n", encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Line 2:"):
                    load_scores(self.path)
                result = self.cli("load", self.path)
                self.assertEqual(result.returncode, 1)
                self.assertIn("Line 2:", result.stderr)
                self.assertNotIn("Count:", result.stdout)

    def test_whitespace_crlf_and_no_final_newline(self):
        self.path.write_bytes(b" 70 \r\n100")
        self.assertEqual(load_scores(self.path), [70, 100])

    def test_missing_path_and_parent(self):
        for args in [("load", self.path), ("save", self.path / "nested.txt", "50")]:
            result = self.cli(*args)
            self.assertEqual(result.returncode, 1)
            self.assertIn("not found", result.stderr)

    def test_directory_and_invalid_encoding(self):
        result = self.cli("load", self.temp.name)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Cannot complete load", result.stderr)
        self.path.write_bytes(b"\xff")
        result = self.cli("load", self.path)
        self.assertEqual(result.returncode, 1)
        self.assertIn("UTF-8", result.stderr)

    def test_cli_save_reload_and_empty(self):
        result = self.cli("save", self.path, "70", "80", "90")
        self.assertEqual(result.returncode, 0, result.stderr)
        result = self.cli("load", self.path)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Count: 3\nTotal: 240\nAverage: 80.00\nLowest: 70\nHighest: 90\n")
        empty = self.path.with_name("empty.txt")
        self.assertEqual(self.cli("save", empty).returncode, 0)
        self.assertEqual(self.cli("load", empty).stdout, "No scores recorded.\n")

    def test_cli_invalid_score_and_extra_load_arguments(self):
        self.assertEqual(self.cli("save", self.path, "abc").returncode, 1)
        self.assertFalse(self.path.exists())
        self.assertEqual(self.cli("load", self.path, "70").returncode, 2)

    def test_permission_error_message(self):
        from score_files import main
        import contextlib
        import io
        output = io.StringIO()
        with patch("builtins.open", side_effect=PermissionError("Permission denied")):
            with contextlib.redirect_stderr(output):
                code = main(["save", str(self.path), "70"])
        self.assertEqual(code, 1)
        self.assertIn("Permission denied", output.getvalue())


if __name__ == "__main__":
    unittest.main()
