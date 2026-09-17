"""A very small command-line example for GitHub Copilot demos."""

from __future__ import annotations

import argparse


def build_message(name: str, first_number: int, second_number: int) -> str:
    """Return a friendly message and the sum of two numbers."""
    total = first_number + second_number
    return f"Hello, {name}! {first_number} + {second_number} = {total}"


def main() -> None:
    # argparse is part of Python's standard library and makes simple CLI tools easy to build.
    parser = argparse.ArgumentParser(
        description="Print a greeting and add two numbers."
    )
    parser.add_argument("--name", default="friend", help="Name used in the greeting")
    parser.add_argument("first_number", type=int, help="The first whole number")
    parser.add_argument("second_number", type=int, help="The second whole number")
    args = parser.parse_args()

    print(build_message(args.name, args.first_number, args.second_number))


if __name__ == "__main__":
    main()
