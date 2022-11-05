"""
Hello World Example
"""

from fastapi import APIRouter

from apis.helloWorld.hello_world_schema import HelloWordlResponse


router = APIRouter()


@router.get(
    "/",
    response_model=HelloWordlResponse,
    tags=["hello world"]
)
def hello_world():
    """
    Say Hello
    """

    return { "message": "Hello World!" }
