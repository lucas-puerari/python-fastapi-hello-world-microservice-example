"""
Hello World route
"""

from fastapi import APIRouter, status

from src.apis.hello_world.hello_world_schema import HelloWordlResponse


router = APIRouter()


@router.get(
    "/",
    response_model=HelloWordlResponse,
    status_code=status.HTTP_200_OK,
    tags=["Hello World"]
)
def hello_world():
    """
    Say Hello
    """

    return { "message": "Hello World!" }
