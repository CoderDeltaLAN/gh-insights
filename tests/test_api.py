from typing import Dict, List
import httpx
import respx

from gh_insights.api import get_top_repos, get_repo_languages, GITHUB_API


@respx.mock
def test_get_top_repos_ordenado_por_stars() -> None:
    user = "octocat"
    respx.get(
        f"{GITHUB_API}/users/{user}/repos",
        params={"per_page": "100", "sort": "stars", "direction": "desc"},
    ).mock(
        return_value=httpx.Response(
            200,
            json=[
                {"name": "repo-a", "stargazers_count": 3},
                {"name": "repo-b", "stargazers_count": 10},
                {"name": "repo-c", "stargazers_count": 7},
            ],
        )
    )

    data: List[Dict] = get_top_repos(user, limit=2)
    # Ahora validamos que vengan ordenados correctamente
    assert [d["name"] for d in data] == ["repo-b", "repo-c"]


@respx.mock
def test_get_repo_languages_ok() -> None:
    owner, repo = "octocat", "hello-world"
    respx.get(f"{GITHUB_API}/repos/{owner}/{repo}/languages").mock(
        return_value=httpx.Response(200, json={"Python": 1200, "Shell": 300})
    )

    langs = get_repo_languages(owner, repo)
    # Total = 1500, Python = 1200 → 80%, Shell = 300 → 20%
    assert round(langs["Python"], 1) == 80.0
    assert round(langs["Shell"], 1) == 20.0
