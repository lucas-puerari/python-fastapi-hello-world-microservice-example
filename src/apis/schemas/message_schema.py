from pydantic import BaseModel


class MessageResponse(BaseModel):
    """
    The Message Response scheme represents the simplest response that is possible to return
    """

    message: str
