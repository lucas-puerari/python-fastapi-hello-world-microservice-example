"""
Hello World tests
"""

from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_hello_world():
    """
    Test say Hello
    """

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
