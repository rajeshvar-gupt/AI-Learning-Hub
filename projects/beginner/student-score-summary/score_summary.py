"""Summarize whole-number scores from 0 to 100; no external packages."""


def parse_score(text):
    """Return a valid score or raise ValueError with a useful message."""
    try:
        score = int(text)
    except ValueError:
        raise ValueError("Enter a whole-number score from 0 to 100.") from None
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    return score


def summarize_scores(scores):
    """Return a report for a list of valid integer scores, without changing it."""
    if not scores:
        return "No scores recorded."
    count = len(scores)
    total = sum(scores)
    average = total / count
    return (
        f"Count: {count}\n"
        f"Total: {total}\n"
        f"Average: {average:.2f}\n"
        f"Lowest: {min(scores)}\n"
        f"Highest: {max(scores)}"
    )


def main():
    scores = []
    print("Student-score summary: enter whole numbers from 0 to 100.")
    while True:
        try:
            raw = input("Score (q to finish): ").strip()
        except EOFError:
            print("\nInput ended.")
            break
        if raw.lower() == "q":
            break
        try:
            score = parse_score(raw)
        except ValueError as error:
            print(error)
            continue
        scores.append(score)
        print(f"Recorded: {score}")
    print(summarize_scores(scores))


if __name__ == "__main__":
    main()
