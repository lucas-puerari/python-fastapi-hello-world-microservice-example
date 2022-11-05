"""
Readiness tests
"""

from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_readiness_test():
    """
    Test if the application is ready to handle a new request
    """

    response = client.get("/-/ready")

    assert response.status_code == 200
