"""Beginner classes example using fictional learner IDs."""


class LearnerRecord:
    """Keep a learner ID and validated scores in memory."""

    def __init__(self, learner_id):
        if not isinstance(learner_id, str) or not learner_id.strip():
            raise ValueError("Learner ID must be nonempty text.")
        self.learner_id = learner_id.strip()
        self._scores = []

    def add_score(self, score):
        """Add an integer from 0 to 100; reject invalid values before mutation."""
        if type(score) is not int or not 0 <= score <= 100:
            raise ValueError("Score must be an integer from 0 to 100.")
        self._scores.append(score)

    def scores(self):
        """Return a copy so callers cannot modify the stored list through it."""
        return self._scores.copy()

    def average(self):
        """Return None when no scores exist, otherwise the arithmetic mean."""
        if not self._scores:
            return None
        return sum(self._scores) / len(self._scores)

    def summary(self):
        mean = self.average()
        if mean is None:
            return f"{self.learner_id}: no scores"
        return f"{self.learner_id}: {len(self._scores)} scores, average {mean:.2f}"


def main():
    first = LearnerRecord("L01")
    second = LearnerRecord("L02")
    first.add_score(70)
    first.add_score(90)
    print(first.summary())
    print(second.summary())
    second.add_score(0)
    print(second.summary())
    snapshot = first.scores()
    snapshot.append(100)
    print(f"Stored scores: {first.scores()}")


if __name__ == "__main__":
    main()
