import os
import logging
import requests

from src.apis.schemas.header_schema import HeaderRequest


class MiaPlatformAuth(requests.auth.AuthBase):
    """
    Attaches http headers to the given request object
    """

    def __init__(self):
        self.header_request = HeaderRequest(
            LOG_LEVEL=os.environ.get('LOG_LEVEL'),
            USERID_HEADER_KEY=os.environ.get('USERID_HEADER_KEY'),
            GROUPS_HEADER_KEY=os.environ.get('GROUPS_HEADER_KEY'),
            CLIENTTYPE_HEADER_KEY=os.environ.get('CLIENTTYPE_HEADER_KEY'),
            BACKOFFICE_HEADER_KEY=os.environ.get('BACKOFFICE_HEADER_KEY'),
            MICROSERVICE_GATEWAY_SERVICE_NAME=os.environ.get(
                'MICROSERVICE_GATEWAY_SERVICE_NAME'),
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
        logging.debug(f'Start - MiaPlatformClient COUNT {url}')

        response = self.session.get(f'{url}/count/', **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient COUNT {url}/count/" \
                f" respond with status code {response.status_code}"
            logging.error(message)
            raise Exception(message)

        logging.debug(f'End - MiaPlatformClient GET BY ID {url}')

        return response

    def post(self, url, data=None, **kwargs):
        logging.debug(f'Start - MiaPlatformClient POST {url}')

        response = self.session.post(url, data, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient POST {url}" \
                f" respond with status code {response.status_code}"
            logging.error(message)
            raise Exception(message)

        logging.debug(f'End - MiaPlatformClient POST {url}')

        return response

    def put(self, url, data=None, **kwargs):
        logging.debug(f'Start - MiaPlatformClient PUT {url}')

        response = self.session.put(url, data, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient PUT {url}" \
                f" respond with status code {response.status_code}"
            logging.error(message)
            raise Exception(message)

        logging.debug(f'End - MiaPlatformClient PUT {url}')

        return response

    def patch(self, url, _id, data=None, **kwargs):
        logging.debug(f'Start - MiaPlatformClient PATCH {url}/{_id}/')

        response = self.session.patch(f'{url}/{_id}/', data, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient PATCH {url}/{_id}/" \
                f" respond with status code {response.status_code}"
            logging.error(message)
            raise Exception(message)

        logging.debug(f'End - MiaPlatformClient PATCH {url}/{_id}/')

        return response

    def delete(self, url, **kwargs):
        logging.debug(f'Start - MiaPlatformClient DELETE {url}')

        response = self.session.delete(url, **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient DELETE {url}" \
                f" respond with status code {response.status_code}"
            logging.error(message)
            raise Exception(message)

        logging.debug(f'End - MiaPlatformClient DELETE {url}')

        return response

    def delete_by_id(self, url, _id, **kwargs):
        logging.debug(f'Start - MiaPlatformClient DELETE BY ID {url}/{_id}/')

        response = self.session.delete(f'{url}/{_id}/', **kwargs)

        if (response.status_code < 200 or response.status_code >= 300):
            message = f"Error - MiaPlatformClient DELETE BY ID {url}/{_id}/" \
                f" respond with status code {response.status_code}"
            logging.error(message)
            raise Exception(message)

        logging.debug(f'End - MiaPlatformClient DELETE BY ID {url}/{_id}/')

        return response
