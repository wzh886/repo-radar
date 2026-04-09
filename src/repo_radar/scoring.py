from __future__ import annotations


def score_repo(*, has_readme: bool, recently_updated: bool, has_issues: bool, has_ci_hint: bool) -> int:
    score = 0
    score += 25 if has_readme else 0
    score += 30 if recently_updated else 0
    score += 20 if has_issues else 0
    score += 25 if has_ci_hint else 0
    return score
