import json
import pytest
import httpretty
from fastapi import status

from src.lib.mia_platform_client import MiaPlatformClient


class TestMiaPlatformClient:
    """
    Test all functionalities of Mia Platform Client
    """

    def validate_sent_headers(self, required_headers, response):
        """
        Validate requests headers
        """

        headers = response.request.headers.items()
        assert all(param in headers for param in required_headers)

    # Get

    def test_200_get(self, server):
        """
        Sucessfully retrive the resources from the collection
        """

        baseurl, required_headers = server

        url = f'{baseurl}/'
        body = [{'message': 'Hi :)'}]

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.get(url)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

        self.validate_sent_headers(required_headers, response)

    def test_500_get(self, server):
        """
        Error on retriving the resources from the collection
        """

        baseurl, _ = server

        url = f'{baseurl}/'

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient GET {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.get(url)

    # Get by id

    def test_200_get_by_id(self, server):
        """
        Sucessfully retrive the resource :id from the collection
        """

        baseurl, required_headers = server

        _id = 1
        url = f'{baseurl}/{_id}/'
        body = {'message': 'Hi :)'}

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.get_by_id(baseurl, _id)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

        self.validate_sent_headers(required_headers, response)

    def test_404_get_by_id(self, server):
        """
        Required resource :id no found in the collection
        """

        baseurl, _ = server

        _id = 1
        url = f'{baseurl}/{_id}/'

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
            mia_platform_client.get_by_id(baseurl, _id)

    def test_500_get_by_id(self, server):
        """
        Error on retriving the resource :id in the collection
        """

        baseurl, _ = server

        _id = 1
        url = f'{baseurl}/{_id}/'

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
            mia_platform_client.get_by_id(baseurl, _id)

    # Count

    def test_200_count(self, server):
        """
        Sucessfully count the resources in the collection
        """

        baseurl, required_headers = server

        url = f'{baseurl}/count/'
        body = '0'

        httpretty.register_uri(
            method=httpretty.GET,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.count(baseurl)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.GET

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

        self.validate_sent_headers(required_headers, response)

    def test_500_count(self, server):
        """
        Error on counting the resources in the collection
        """

        baseurl, _ = server

        url = f'{baseurl}/count/'
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
            mia_platform_client.count(baseurl)

    # Post

    def test_201_post(self, server):
        """
        Sucessfully create the resource in the collection
        """

        baseurl, required_headers = server

        url = f'{baseurl}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.POST,
            uri=url,
            status=status.HTTP_201_CREATED,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.post(baseurl, data=body)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.POST

        # Response
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == body

        self.validate_sent_headers(required_headers, response)

    def test_500_post(self, server):
        """
        Error on creating the resource in the collection
        """

        baseurl, _ = server

        url = f'{baseurl}/'
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

    # Put

    def test_200_put(self, server):
        """
        Sucessfully overwrite the resouce in the collection
        """

        baseurl, required_headers = server

        url = f'{baseurl}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.PUT,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.put(baseurl, data=body)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.PUT

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

        self.validate_sent_headers(required_headers, response)

    def test_201_put(self, server):
        """
        Sucessfully create the resource in the collection
        """

        baseurl, required_headers = server

        url = f'{baseurl}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.PUT,
            uri=url,
            status=status.HTTP_201_CREATED,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.put(baseurl, data=body)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.PUT

        # Response
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == body

        self.validate_sent_headers(required_headers, response)

    def test_500_put(self, server):
        """
        Error on creating / overwriting the resource in the collection
        """

        baseurl, _ = server

        url = f'{baseurl}/'
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

    # Patch

    def test_200_patch_by_id(self, server):
        """
        Sucessfully update the resource in the collection
        """

        baseurl, required_headers = server

        _id = 1
        url = f'{baseurl}/{_id}/'
        body = {'key': 'value'}

        httpretty.register_uri(
            method=httpretty.PATCH,
            uri=url,
            status=status.HTTP_200_OK,
            body=json.dumps(body)
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.patch(baseurl, _id, data=body)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.PATCH

        # Response
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == body

        self.validate_sent_headers(required_headers, response)

    def test_404_patch_by_id(self, server):
        """
        Resource :id to update not found in the collection
        """

        baseurl, _ = server

        _id = 1
        url = f'{baseurl}/{_id}/'

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
            mia_platform_client.patch(baseurl, _id)

    def test_500_patch_by_id(self, server):
        """
        Error on updating the resource :id in the collection
        """

        baseurl, _ = server

        _id = 1
        url = f'{baseurl}/{_id}/'

        httpretty.register_uri(
            method=httpretty.PATCH,
            uri=url,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

        mia_platform_client = MiaPlatformClient()

        with pytest.raises(
            Exception,
            match=f"Error - MiaPlatformClient PATCH {url}"
                f" respond with status code {status.HTTP_500_INTERNAL_SERVER_ERROR}"
        ):
            mia_platform_client.patch(baseurl, _id)

    # Delete

    def test_204_delete(self, server):
        """
        Sucessfully delete the resources from collection
        """

        baseurl, required_headers = server

        url = f'{baseurl}/'

        httpretty.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_204_NO_CONTENT,
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.delete(url)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.DELETE

        # Response
        assert response.status_code == status.HTTP_204_NO_CONTENT

        self.validate_sent_headers(required_headers, response)

    def test_500_delete(self, server):
        """
        Error on deleting the resources from the collection
        """

        baseurl, _ = server

        url = f'{baseurl}/'

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

    # Delete by id

    def test_204_delete_by_id(self, server):
        """
        Sucessfully delete the resource :id from the collection
        """

        baseurl, required_headers = server

        _id = 1
        url = f'{baseurl}/{_id}/'

        httpretty.register_uri(
            method=httpretty.DELETE,
            uri=url,
            status=status.HTTP_204_NO_CONTENT,
        )

        mia_platform_client = MiaPlatformClient()
        response = mia_platform_client.delete_by_id(baseurl, _id)

        # Request
        assert response.request.url == url
        assert response.request.method == httpretty.DELETE

        # Response
        assert response.status_code == status.HTTP_204_NO_CONTENT

        self.validate_sent_headers(required_headers, response)

    def test_404_delete_by_id(self, server):
        """
        Resource :id to delete not found in the collection
        """

        baseurl, _ = server

        _id = 1
        url = f'{baseurl}/{_id}/'

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
            mia_platform_client.delete_by_id(baseurl, _id)

    def test_500_delete_by_id(self, server):
        """
        Error on deleting the resource :id from the collection
        """

        baseurl, _ = server

        _id = 1
        url = f'{baseurl}/{_id}/'

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
            mia_platform_client.delete_by_id(baseurl, _id)
