import pytest
import respx
from httpx import Response
from gh_insights.api import get_repo_languages

@pytest.mark.asyncio
@respx.mock
async def test_get_repo_languages():
    # Simular respuesta de la API de GitHub
    url = "https://api.github.com/repos/torvalds/linux/languages"
    respx.get(url).mock(
        return_value=Response(
            200,
            json={
                "C": 1000,
                "Python": 500,
                "Rust": 250,
            },
        )
    )

    # Ejecutar la función
    langs = get_repo_languages("torvalds", "linux")

    # Validar contenido en porcentajes
    assert "C" in langs
    assert round(langs["C"], 1) == 57.1
    assert round(langs["Python"], 1) == 28.6
    assert round(langs["Rust"], 1) == 14.3

