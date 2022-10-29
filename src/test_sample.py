"""
This is a sample test file
"""

from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_hello_world():
    """
    Test say Hello
    """

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == { "message": "Hello World!" }
