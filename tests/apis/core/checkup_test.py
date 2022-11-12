"""
Check-up tests
"""

from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_checkup_test():
    """
    Test the availability of all the service's dependencies
    """

    response = client.get("/-/check-up")

    assert response.status_code == 200
    assert response.json() == {"statusOk": True}
