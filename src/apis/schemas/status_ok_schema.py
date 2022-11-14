from pydantic import BaseModel


class StatusOkResponse(BaseModel):
    """
    The Status Ok Response scheme describe the response of status endpoints
    """

    statusOk: bool
