from typing import Any, Dict, List, Optional
import os

import httpx

# Constante base de la API
GITHUB_API = "https://api.github.com"


def _headers() -> Dict[str, str]:
    """Headers opcionales con token si está definido GITHUB_TOKEN."""
    token: Optional[str] = os.getenv("GITHUB_TOKEN")
    h: Dict[str, str] = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


from typing import List, Dict
import httpx

GITHUB_API = "https://api.github.com"


from typing import List, Dict
import httpx

GITHUB_API = "https://api.github.com"


from typing import List, Dict
import httpx

GITHUB_API = "https://api.github.com"


def get_top_repos(user: str, limit: int = 5) -> List[Dict]:
    """Obtiene los repos de un usuario ordenados por estrellas (desc)."""
    resp = httpx.get(
        f"{GITHUB_API}/users/{user}/repos",
        params={"per_page": "100", "sort": "stars", "direction": "desc"},
    )
    resp.raise_for_status()
    repos = resp.json()

    # Ordenar por estrellas descendente (doble seguridad)
    repos_sorted = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)

    return repos_sorted[:limit]


def get_repo_languages(owner: str, repo: str) -> Dict[str, float]:
    """
    Devuelve un diccionario {lenguaje: porcentaje} en lugar de bytes.
    El porcentaje es (bytes_lenguaje / suma_total) * 100.
    """
    url = f"{GITHUB_API}/repos/{owner}/{repo}/languages"
    resp = httpx.get(url, headers=_headers(), timeout=10)
    resp.raise_for_status()
    data: Dict[str, int] = resp.json()
    total = sum(data.values())
    if total == 0:
        return {}
    return {lang: (count / total) * 100 for lang, count in data.items()}
