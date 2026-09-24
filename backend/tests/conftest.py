import pytest
from fastapi.testclient import TestClient
from app.main import main

#File must be exactly this name to be known as a pytest fixture file.

#Will handle copying the json to a temp file for usage in test

@pytest.fixture
def client():
    app = main()
    return TestClient(app)