"""
Where everything begins...
"""

import uvicorn
from fastapi import FastAPI

from apis.helloWorld import hello_world_handler


app = FastAPI(openapi_url="/documentation/json")

app.include_router(hello_world_handler.router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)
