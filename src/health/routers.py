from fastapi import status
from fastapi import APIRouter
from .models import HealthCheck


router = APIRouter(
    prefix="/health",
    tags=["healthcheck"],
)


@router.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. 
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="This looks healthy")

