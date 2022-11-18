# pylint: disable=unused-argument

import pytest
import httpretty
from fastapi import status

from src.lib.mia_platform_client import MiaPlatformClient
from src.apis.schemas.header_schema import HeaderRequest


REQUIRED_HEADERS = HeaderRequest(
    CONFIGURATION_PATH='./',
    CONFIGURATION_FILE_NAME='test-config.test',
    BACKOFFICE_HEADER_KEY='isbackoffice',
    USERINFO_URL='http://auth0-client/userinfo',
    CLIENT_TYPE_HEADER_KEY='client-type',
).__dict__.items()


BASEURL = 'http://testserver'


class TestMiaPlatformClient:
    """
    Test all functionalities of Mia Platform Client
    """

    def test_200_get(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'
        body = '[{"message": "Hi :)"}]'

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=body
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.get(url)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.text == body

    def test_500_get(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'
        body = ''

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            body=body
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.get(url)

    def test_200_get_by_id(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'
        body = '{"message": "Hi :)"}'

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=body
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.get_by_id(BASEURL, _id)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.text == body

    def test_404_get_by_id(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'
        body = ''

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_404_NOT_FOUND,
            body=body
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET BY ID {url}"
                f" respond with status code {status.HTTP_404_NOT_FOUND}"
        ):
            mia_platform_client.get_by_id(BASEURL, _id)

    def test_500_get_by_id(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'
        body = ''

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            body=body
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET BY ID {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.get_by_id(BASEURL, _id)

    def test_200_count(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/count/'
        body = '0'

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=body
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.count(BASEURL)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.text == body
