"""
Liveness route
"""

from fastapi import APIRouter, status

from src.apis.common.schemas.status_ok_schema import StatusOkResponse


router = APIRouter()


@router.get(
    "/-/healthz",
    response_model=StatusOkResponse,
    status_code=status.HTTP_200_OK,
    tags=["Liveness"]
)
def liveness():
    """
    This route can be used as a probe for load balancers, status dashboards and
    as a helthinessProbe for Kubernetes. By default, the route will always
    response with an OK status and the 200 HTTP code as soon as the service is
    up.
    """

    return {"statusOk": True}
