from pydantic import BaseModel


class HeaderRequest(BaseModel):
    """
    Mia Platform required headers
    """

    LOG_LEVEL: str
    USERID_HEADER_KEY: str
    GROUPS_HEADER_KEY: str
    CLIENTTYPE_HEADER_KEY: str
    BACKOFFICE_HEADER_KEY: str
    MICROSERVICE_GATEWAY_SERVICE_NAME: str
