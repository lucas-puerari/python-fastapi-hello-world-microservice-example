# pylint: disable=unused-argument

import json
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

    # GET

    def test_200_get(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'
        body = [{'message': 'Hi :)'}]

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
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
        assert response.json() == body

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

    # GET BY ID

    def test_200_get_by_id(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'
        body = {'message': 'Hi :)'}

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
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
        assert response.json() == body

    def test_404_get_by_id(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_404_NOT_FOUND,
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

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET BY ID {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.get_by_id(BASEURL, _id)

    # COUNT

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
            body=json.dumps(body)
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
        assert response.json() == body

    def test_500_count(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/count/'
        body = '0'

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            body=body
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient COUNT {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.count(BASEURL)

    # POST

    def test_201_post(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.POST,
            uri=url,
            status=status.HTTP_201_CREATED,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.post(BASEURL, data=body)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.POST
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == body

    def test_500_post(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.POST,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient POST {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.post(url, data=body)

    # PUT

    def test_200_put(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.PUT,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.put(BASEURL, data=body)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.PUT
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    def test_201_put(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.PUT,
            uri=url,
            status=status.HTTP_201_CREATED,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.put(BASEURL, data=body)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.PUT
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == body

    def test_500_put(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.PUT,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient PUT {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.put(url, json=body)

    # PATCH

    def test_200_patch(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.PATCH,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.patch(BASEURL, _id, data=body)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.PATCH
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

    def test_404_patch(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'

        httpretty.register_uri(
            method=httpretty.PATCH,
            uri=url,
            status=status.HTTP_404_NOT_FOUND,
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient PATCH {url}"
                f" respond with status code {status.HTTP_404_NOT_FOUND}"
        ):
            mia_platform_client.patch(BASEURL, _id)

    # DELETE

    def test_204_delete(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'

        httpretty.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_204_NO_CONTENT,
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.delete(url)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.DELETE
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_500_delete(self, server):
        """
        TODO
        """

        url = f'{BASEURL}/'

        httpretty.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient DELETE {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.delete(url)

    # DELETE BY ID

    def test_204_delete_by_id(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'

        httpretty.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_204_NO_CONTENT,
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.delete_by_id(BASEURL, _id)
        headers = response.request.headers.items()

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.DELETE
        assert all(param in headers for param in REQUIRED_HEADERS)

        # Response
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_404_delete_by_id(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'

        httpretty.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_404_NOT_FOUND,
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient DELETE BY ID {url}"
                f" respond with status code {status.HTTP_404_NOT_FOUND}"
        ):
            mia_platform_client.delete_by_id(BASEURL, _id)

    def test_500_delete_by_id(self, server):
        """
        TODO
        """

        _id = 1
        url = f'{BASEURL}/{_id}/'

        httpretty.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient DELETE BY ID {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.delete_by_id(BASEURL, _id)
