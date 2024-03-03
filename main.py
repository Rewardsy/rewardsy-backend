"""Entrypoint to invoke the FastAPI application service with."""

from fastapi import FastAPI, status
from pydantic import BaseModel
import uvicorn
from src.health.routers import router as health_router

app = FastAPI(
    title="Rewardsy-Backend",
    version = "0.1.0",

)

app.include_router(health_router)

def main() -> None:
    """Entrypoint to invoke when this module is invoked on the remote server."""
    # See the official documentations on how "0.0.0.0" makes the service available on
    # the local network - https://www.uvicorn.org/settings/#socket-binding
    uvicorn.run("main:app", host="0.0.0.0",reload=True)


if __name__ == "__main__":
    main()

