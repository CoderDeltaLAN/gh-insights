from typing import Any, Dict, List

import httpx
import respx

from gh_insights.api import GITHUB_API, get_repo_languages, get_top_repos


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

    data: List[Dict[str, Any]] = get_top_repos(user, limit=2)
    assert [d["name"] for d in data] == ["repo-b", "repo-c"]


@respx.mock
def test_get_repo_languages_ok() -> None:
    owner, repo = "octocat", "hello-world"
    respx.get(f"{GITHUB_API}/repos/{owner}/{repo}/languages").mock(
        return_value=httpx.Response(200, json={"Python": 1200, "Shell": 300})
    )
    langs = get_repo_languages(owner, repo)
    # 1200 de 1500 = 80%, 300 de 1500 = 20%
    assert "Python" in langs and round(langs["Python"], 1) == 80.0
    assert "Shell" in langs and round(langs["Shell"], 1) == 20.0
