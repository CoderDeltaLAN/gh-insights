from typing import Dict, List
import os

import httpx

GITHUB_API = "https://api.github.com"


def _headers() -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN")
    return {"Authorization": f"Bearer {token}"} if token else {}


def get_top_repos(user: str, limit: int = 5) -> List[Dict[str, object]]:
    """Devuelve los *limit* repos del usuario ordenados por estrellas (desc)."""
    url = f"{GITHUB_API}/users/{user}/repos"
    params = {"per_page": 100, "sort": "stars", "direction": "desc"}
    with httpx.Client(headers=_headers(), timeout=30.0) as client:
        resp = client.get(url, params=params)
        resp.raise_for_status()
        repos = resp.json()  # list[dict]
    repos.sort(key=lambda r: r.get("stargazers_count", 0) or 0, reverse=True)
    selected = repos[: int(limit)]
    return [
        {
            "name": r.get("name", ""),
            "full_name": r.get("full_name", ""),
            "stars": int(r.get("stargazers_count", 0) or 0),
            "forks": int(r.get("forks_count", 0) or 0),
            "html_url": r.get("html_url", ""),
        }
        for r in selected
    ]


def get_repo_languages(owner: str, repo: str) -> Dict[str, float]:
    """Devuelve porcentajes de lenguajes (0–100) para un repo."""
    url = f"{GITHUB_API}/repos/{owner}/{repo}/languages"
    with httpx.Client(headers=_headers(), timeout=30.0) as client:
        resp = client.get(url)
        resp.raise_for_status()
        data: Dict[str, int] = resp.json()

    total = sum(data.values()) or 1
    return {lang: (value / total) * 100.0 for lang, value in data.items()}
