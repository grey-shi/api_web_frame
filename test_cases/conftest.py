import pytest


@pytest.fixture(scope="session", autouse=True)
def setup():
    print("22")
    yield
    print("11")