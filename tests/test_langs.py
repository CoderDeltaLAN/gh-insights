import pytest
from httpx import Response
import respx

from gh_insights.api import get_repo_languages


@pytest.mark.asyncio
@respx.mock
async def test_get_repo_languages() -> None:
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
    langs = get_repo_languages("torvalds", "linux")
    total = 1000 + 500 + 250  # 1750
    assert round(langs["C"], 1) == round(1000 / total * 100, 1)
    assert round(langs["Python"], 1) == round(500 / total * 100, 1)
    assert round(langs["Rust"], 1) == round(250 / total * 100, 1)
