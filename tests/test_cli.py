from typing import Any, Dict, List

from gh_insights.__main__ import cmd_top_repos


def test_cmd_top_repos_muestra_tabla(monkeypatch, capsys) -> None:
    # Fakes/fixtures
    fake_repos: List[Dict[str, Any]] = [
        {"name": "repo-x", "stargazers_count": 5},
        {"name": "repo-y", "stargazers_count": 2},
    ]

    def fake_get_top_repos(user: str, limit: int = 5) -> List[Dict[str, Any]]:
        assert user == "octocat"
        assert limit == 2
        return fake_repos

    def fake_get_repo_languages(owner: str, repo: str) -> Dict[str, int]:
        if repo == "repo-x":
            return {"Python": 100}
        return {"Shell": 50}

    # Monkeypatch de las funciones importadas en __main__
    import gh_insights.__main__ as m

    monkeypatch.setattr(m, "get_top_repos", fake_get_top_repos)
    monkeypatch.setattr(m, "get_repo_languages", fake_get_repo_languages)

    # Ejecutar el comando directamente
    cmd_top_repos(user="octocat", limit=2)

    out = capsys.readouterr().out
    # Verifica contenido clave de la tabla
    assert "Top 2 repos de octocat" in out
    assert "repo-x" in out and "repo-y" in out
    assert "Python" in out or "Shell" in out
    assert "⭐" in out or "Stars" in out
