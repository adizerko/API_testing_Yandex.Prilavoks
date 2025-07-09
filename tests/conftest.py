import pytest

@pytest.fixture(scope="session")
def some_data():
    return {"example": 123}
