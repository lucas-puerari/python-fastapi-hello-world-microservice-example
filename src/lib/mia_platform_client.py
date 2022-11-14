import logging
import requests

from src.apis.schemas.header_schema import HeaderRequest


class MiaPlatformAuth(requests.auth.AuthBase):
    """
    Attaches http headers to the given request object
    """

    def __init__(self):
        self.header_request = HeaderRequest(
            CONFIGURATION_PATH='./',
            CONFIGURATION_FILE_NAME='test-config.test',
            BACKOFFICE_HEADER_KEY='isbackoffice',
            USERINFO_URL='http://auth0-client/userinfo',
            CLIENT_TYPE_HEADER_KEY='client-type',
        )

    def __call__(self, req):
        for key, value in self.header_request.__dict__.items():
            req.headers[key] = value
        return req


class MiaPlatformClient():
    """
    Provides a simple interface to do http requests within a Mia Platform
    application cluster
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.auth = MiaPlatformAuth()

    def get(self, url, **kwargs):
        logging.debug(f'Start - MiaPlatformClient GET {url}')

        response = self.session.get(url, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient GET {url}" \
                f" respond with status code {response.status_code}"
            logging.error(message)
            raise Exception(message)

        logging.debug(f'End - MiaPlatformClient GET {url}')

        return response

    def get_by_id(self, url, _id, **kwargs):
        logging.debug(f'Start - MiaPlatformClient GET BY ID {url}/{_id}/')

        response = self.session.get(f'{url}/{_id}/', **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient GET BY ID {url}/{_id}/" \
                f" respond with status code {response.status_code}"
            logging.error(message)
            raise Exception(message)

        logging.debug(f'End - MiaPlatformClient GET BY ID {url}/{_id}/')

        return response

    def count(self, url, **kwargs):
        return self.session.get(f'{url}/count/', **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.session.post(self, url, data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.session.put(self, url, data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.session.patch(self, url, data, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(self, url, **kwargs)

    def options(self, url, **kwargs):
        return self.session.options(self, url, **kwargs)

    def head(self, url, **kwargs):
        return self.session.head(self, url, **kwargs)
