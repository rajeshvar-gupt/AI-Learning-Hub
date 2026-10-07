"""Run from repository root with the command in README.md."""
import contextlib
import io
import subprocess
import sys
import unittest
from pathlib import Path

from score_summary import parse_score, summarize_scores


class ScoreSummaryTests(unittest.TestCase):
    def run_cli(self, text):
        return subprocess.run(
            [sys.executable, str(Path(__file__).with_name("score_summary.py"))],
            input=text, text=True, capture_output=True, check=True, timeout=5,
        ).stdout

    def test_parse_boundaries_and_whitespace(self):
        for text, expected in [("0", 0), ("100", 100), (" 75 ", 75)]:
            with self.subTest(text=text):
                self.assertEqual(parse_score(text), expected)

    def test_reject_invalid_scores(self):
        for text in ["", "abc", "82.5", "-1", "101", "nan", "inf"]:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_score(text)

    def test_report_and_no_mutation_or_printing(self):
        scores = [70, 80, 90]
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            report = summarize_scores(scores)
        self.assertEqual(report, "Count: 3\nTotal: 240\nAverage: 80.00\nLowest: 70\nHighest: 90")
        self.assertEqual(scores, [70, 80, 90])
        self.assertEqual(output.getvalue(), "")

    def test_empty_single_zero_and_rounding(self):
        self.assertEqual(summarize_scores([]), "No scores recorded.")
        self.assertEqual(summarize_scores([0]), "Count: 1\nTotal: 0\nAverage: 0.00\nLowest: 0\nHighest: 0")
        self.assertIn("Average: 0.67", summarize_scores([0, 1, 1]))

    def test_cli_mixed_input_and_boundaries(self):
        output = self.run_cli("abc\n\n82.5\n-1\n101\n0\n100\n Q \n")
        self.assertEqual(output.count("Recorded:"), 2)
        self.assertEqual(output.count("Enter a whole-number score"), 3)
        self.assertEqual(output.count("Score must be between"), 2)
        self.assertTrue(output.endswith("Count: 2\nTotal: 100\nAverage: 50.00\nLowest: 0\nHighest: 100\n"))

    def test_cli_immediate_quit_and_eof(self):
        for text in ["q\n", ""]:
            with self.subTest(text=text):
                self.assertTrue(self.run_cli(text).endswith("No scores recorded.\n"))

    def test_cli_eof_preserves_accepted_scores(self):
        output = self.run_cli("75\n")
        self.assertIn("Input ended.", output)
        self.assertIn("Count: 1\nTotal: 75\nAverage: 75.00", output)

    def test_import_does_not_start_cli(self):
        folder = str(Path(__file__).parent)
        result = subprocess.run(
            [sys.executable, "-c", "import score_summary"],
            cwd=folder, input="", capture_output=True, text=True, check=True, timeout=5,
        )
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
