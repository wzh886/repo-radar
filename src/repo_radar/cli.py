from __future__ import annotations

import argparse

from .scoring import score_repo


def main() -> None:
    parser = argparse.ArgumentParser(prog="repo-radar")
    parser.add_argument("--has-readme", action="store_true")
    parser.add_argument("--recently-updated", action="store_true")
    parser.add_argument("--has-issues", action="store_true")
    parser.add_argument("--has-ci-hint", action="store_true")
    args = parser.parse_args()

    total = score_repo(
        has_readme=args.has_readme,
        recently_updated=args.recently_updated,
        has_issues=args.has_issues,
        has_ci_hint=args.has_ci_hint,
    )
    print(total)


if __name__ == "__main__":
    main()
