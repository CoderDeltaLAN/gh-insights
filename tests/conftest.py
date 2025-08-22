import respx
import pytest

@pytest.fixture(autouse=True)
def _respx_assert_all(mock_router: respx.MockRouter):
    # Fuerza que cualquier request no mockeada falle (igual en CI y local).
    with respx.mock(assert_all_mocked=True) as router:
        yield router
