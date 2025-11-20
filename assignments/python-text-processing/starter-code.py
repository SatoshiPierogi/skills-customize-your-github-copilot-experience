"""
Starter Code for Python Text Processing Assignment

This scaffold provides a basic CLI for reading a text file and computing simple word counts.
Students: implement the functions marked TODO and extend the functionality.
"""

import argparse
import string
from collections import Counter
from typing import List


def read_file(path: str) -> str:
    """Read the contents of a file and return as a single string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def tokenize(text: str) -> List[str]:
    """Tokenize the text into words.

    This basic tokenizer removes punctuation and splits on whitespace. Make it
    more robust if you like (e.g., regex-based tokenization).
    """
    # TODO: Improve tokenization if desired
    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
    cleaned = text.translate(translator)
    tokens = cleaned.lower().split()
    return tokens


def count_words(tokens: List[str]) -> Counter:
    """Return a Counter of words from token list."""
    return Counter(tokens)


def write_report(output_path: str, report: str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)


def main():
    parser = argparse.ArgumentParser(description="Simple text processing utility")
    parser.add_argument("--input", required=True, help="Input text file path")
    parser.add_argument("--output", required=False, help="Optional output report path")
    parser.add_argument("--top", type=int, default=10, help="Top N words to show")
    args = parser.parse_args()

    text = read_file(args.input)
    tokens = tokenize(text)
    counts = count_words(tokens)

    total_words = sum(counts.values())
    unique_words = len(counts)

    top_n = counts.most_common(args.top)

    report_lines = [
        f"Total words: {total_words}",
        f"Unique words: {unique_words}",
        "Top words:",
    ]
    for word, c in top_n:
        report_lines.append(f"{word}: {c}")

    report = "\n".join(report_lines)
    print(report)
    if args.output:
        write_report(args.output, report)
        print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
