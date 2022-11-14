import pytest
import httpretty
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def client():
    """
    This client can call the developed application
    """

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def server():
    """
    This server can receive requests and mock the response
    """

    httpretty.enable(verbose=True, allow_net_connect=False)
    yield
    httpretty.disable()
    httpretty.reset()
