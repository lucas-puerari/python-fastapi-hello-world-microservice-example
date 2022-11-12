"""
Readiness route
"""

from fastapi import APIRouter, status

from src.apis.schemas.status_ok_schema import StatusOkResponse


router = APIRouter()


@router.get(
    "/-/ready",
    response_model=StatusOkResponse,
    status_code=status.HTTP_200_OK,
    tags=["Readiness"]
)
def readiness():
    """
    This route can be used as a readinessProbe for Kubernetes. By default, the
    route will always response with an OK status and the 200 HTTP code as soon
    as the service is up.
    """

    return {"statusOk": True}
