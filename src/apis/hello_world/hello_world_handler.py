"""
Hello World route
"""

from fastapi import APIRouter, status

from src.apis.schemas.message_schema import MessageResponse


router = APIRouter()


@router.get(
    "/",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    tags=["Hello World"]
)
def hello_world():
    """
    Say Hello
    """

    return {"message": "Hello World!"}
