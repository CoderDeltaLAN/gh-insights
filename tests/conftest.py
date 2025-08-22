import respx
import pytest

@pytest.fixture(autouse=True)
def _respx_assert_all():
    with respx.mock(assert_all_mocked=True):
        yield
