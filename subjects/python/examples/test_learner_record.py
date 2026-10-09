import subprocess
import sys
import unittest
from pathlib import Path

from learner_record import LearnerRecord


class LearnerRecordTests(unittest.TestCase):
    def test_empty_record_and_id_normalization(self):
        record = LearnerRecord(" L01 ")
        self.assertEqual(record.learner_id, "L01")
        self.assertIsNone(record.average())
        self.assertEqual(record.summary(), "L01: no scores")

    def test_invalid_ids(self):
        for value in ["", "   ", None, 123]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    LearnerRecord(value)

    def test_scores_boundaries_and_duplicates(self):
        record = LearnerRecord("L01")
        for score in [0, 100, 100]:
            record.add_score(score)
        self.assertEqual(record.scores(), [0, 100, 100])
        self.assertAlmostEqual(record.average(), 200 / 3)
        self.assertEqual(record.summary(), "L01: 3 scores, average 66.67")

    def test_zero_is_not_missing(self):
        record = LearnerRecord("L01")
        record.add_score(0)
        self.assertEqual(record.average(), 0)
        self.assertEqual(record.summary(), "L01: 1 scores, average 0.00")

    def test_invalid_scores_leave_state_unchanged(self):
        record = LearnerRecord("L01")
        record.add_score(70)
        for score in [-1, 101, 70.5, "70", True, None]:
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    record.add_score(score)
                self.assertEqual(record.scores(), [70])

    def test_instances_and_returned_lists_are_independent(self):
        first, second = LearnerRecord("L01"), LearnerRecord("L02")
        first.add_score(90)
        snapshot = first.scores()
        snapshot.append(0)
        self.assertEqual(first.scores(), [90])
        self.assertEqual(second.scores(), [])
        second.add_score(40)
        self.assertEqual(first.average(), 90)

    def test_demo_output(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("learner_record.py"))],
            capture_output=True, text=True, check=True, timeout=5,
        )
        self.assertEqual(result.stdout,
            "L01: 2 scores, average 80.00\nL02: no scores\n"
            "L02: 1 scores, average 0.00\nStored scores: [70, 90]\n")

    def test_import_has_no_output(self):
        result = subprocess.run(
            [sys.executable, "-c", "import learner_record"],
            cwd=Path(__file__).parent, capture_output=True, text=True, check=True, timeout=5,
        )
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
