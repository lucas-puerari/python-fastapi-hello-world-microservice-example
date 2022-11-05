"""
Readiness route
"""

from fastapi import APIRouter, status


router = APIRouter()


@router.get(
    "/ready",
    status_code=status.HTTP_200_OK,
    tags=["Readiness"]
)
def readiness():
    """
    Are you ready?
    """

    return
