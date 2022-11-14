from pydantic import BaseModel


class HeaderRequest(BaseModel):
    """
    Mia Platform required headers
    """

    CONFIGURATION_PATH: str
    CONFIGURATION_FILE_NAME: str
    BACKOFFICE_HEADER_KEY: str
    USERINFO_URL: str
    CLIENT_TYPE_HEADER_KEY: str
