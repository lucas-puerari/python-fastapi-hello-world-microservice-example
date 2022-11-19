import os
import pytest
import httpretty
from dotenv import load_dotenv
from fastapi.testclient import TestClient

from src.app import app
from src.apis.schemas.header_schema import HeaderRequest


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

    load_dotenv('default.env')

    baseurl = 'http://testserver'
    require_headers = HeaderRequest(
        LOG_LEVEL=os.environ.get('LOG_LEVEL'),
        USERID_HEADER_KEY=os.environ.get('USERID_HEADER_KEY'),
        GROUPS_HEADER_KEY=os.environ.get('GROUPS_HEADER_KEY'),
        CLIENTTYPE_HEADER_KEY=os.environ.get('CLIENTTYPE_HEADER_KEY'),
        BACKOFFICE_HEADER_KEY=os.environ.get('BACKOFFICE_HEADER_KEY'),
        MICROSERVICE_GATEWAY_SERVICE_NAME=os.environ.get(
            'MICROSERVICE_GATEWAY_SERVICE_NAME'),
    ).__dict__.items()

    httpretty.enable(verbose=False, allow_net_connect=False)

    yield baseurl, require_headers

    httpretty.disable()
    httpretty.reset()
