from repo_radar.scoring import score_repo


def test_score_repo_all_signals_present():
    assert score_repo(
        has_readme=True,
        recently_updated=True,
        has_issues=True,
        has_ci_hint=True,
    ) == 100


def test_score_repo_missing_signals():
    assert score_repo(
        has_readme=False,
        recently_updated=True,
        has_issues=False,
        has_ci_hint=False,
    ) == 30
