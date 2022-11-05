"""
Where everything begins...
"""

import uvicorn
from fastapi import FastAPI


app = FastAPI(openapi_url="/documentation/json")


@app.get("/")
def hello_world():
    """
    Say Hello
    """

    return { "message": "Hello World!" }


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)
