"""
Liveness route
"""

from fastapi import APIRouter, status


router = APIRouter()


@router.get(
    "/healthz",
    status_code=status.HTTP_200_OK,
    tags=["Liveness"]
)
def liveness():
    """
    Are you alive?
    """

    return
