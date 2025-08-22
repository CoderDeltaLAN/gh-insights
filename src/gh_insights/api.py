from __future__ import annotations

import os
from typing import Dict, List

import httpx

GITHUB_API = "https://api.github.com"


def _headers() -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN")
    return {"Authorization": f"Bearer {token}"} if token else {}


def get_top_repos(user: str, limit: int = 10) -> List[Dict[str, object]]:
    """Devuelve los repos de un usuario ordenados por estrellas desc, limitados."""
    resp = httpx.get(
        f"{GITHUB_API}/users/{user}/repos",
        params={"per_page": "100", "sort": "stars", "direction": "desc"},
        headers=_headers(),
        timeout=30.0,
    )
    resp.raise_for_status()
    data: List[Dict[str, object]] = resp.json()

    # Asegurar orden descendente por estrellas y limitar
    data_sorted = sorted(
        data,
        key=lambda d: int(d.get("stargazers_count", 0) or 0),
        reverse=True,
    )
    return data_sorted[:limit]


def get_repo_languages(owner: str, repo: str) -> Dict[str, float]:
    """Devuelve los lenguajes con porcentajes (0-100)."""
    resp = httpx.get(
        f"{GITHUB_API}/repos/{owner}/{repo}/languages",
        headers=_headers(),
        timeout=30.0,
    )
    resp.raise_for_status()
    raw: Dict[str, int] = resp.json()
    total = sum(raw.values()) or 1
    return {lang: (bytes_ / total) * 100 for lang, bytes_ in raw.items()}
