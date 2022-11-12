"""
Where everything begins...
"""

import uvicorn
from fastapi import FastAPI

from src.apis.core.liveness import liveness_handler
from src.apis.core.readiness import readiness_handler
from src.apis.core.checkup import checkup_handler
from src.apis.hello_world import hello_world_handler


app = FastAPI(
    openapi_url="/documentation/json",
    docs_url=None,
    redoc_url=None
)

# Core
app.include_router(liveness_handler.router)
app.include_router(readiness_handler.router)
app.include_router(checkup_handler.router)

# Hello World
app.include_router(hello_world_handler.router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)
