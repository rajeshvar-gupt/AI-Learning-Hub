"""Save/load UTF-8 score files. Run --help for commands."""
import argparse
import sys

from score_summary import parse_score, summarize_scores


def save_scores(path, scores):
    """Create a new file of valid integer scores; never overwrite a file."""
    for score in scores:
        if type(score) is not int or not 0 <= score <= 100:
            raise ValueError("Scores must be integers from 0 to 100.")
    with open(path, "x", encoding="utf-8") as handle:
        for score in scores:
            handle.write(f"{score}\n")


def load_scores(path):
    """Read all scores, rejecting the whole load on any invalid line."""
    scores = []
    with open(path, "r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                score = parse_score(line.strip())
            except ValueError as error:
                raise ValueError(f"Line {line_number}: {error}") from None
            scores.append(score)
    return scores


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["save", "load"])
    parser.add_argument("path", help="File path, relative to the current directory or absolute")
    parser.add_argument("scores", nargs="*", help="Whole-number marks for save only")
    args = parser.parse_args(argv)
    if args.command == "load" and args.scores:
        parser.error("load takes a path only")
    try:
        if args.command == "save":
            scores = []
            for text in args.scores:
                scores.append(parse_score(text))
            save_scores(args.path, scores)
            print(f"Saved {len(scores)} scores to {args.path}")
        else:
            scores = load_scores(args.path)
            print(summarize_scores(scores))
    except FileExistsError:
        print("Cannot save: file already exists. Choose a new filename.", file=sys.stderr)
        return 1
    except FileNotFoundError:
        print("File or parent folder not found. Check the path.", file=sys.stderr)
        return 1
    except UnicodeError:
        print("Cannot read file: expected UTF-8 text.", file=sys.stderr)
        return 1
    except (OSError, ValueError) as error:
        print(f"Cannot complete {args.command}: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
