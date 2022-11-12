"""
Liveness tests
"""

from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_liveness_test():
    """
    Test if the application is up and runnig
    """

    response = client.get("/-/healthz")

    assert response.status_code == 200
    assert response.json() == {"statusOk": True}
