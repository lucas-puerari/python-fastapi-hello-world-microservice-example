"""
Hello World Schema
"""

from pydantic import BaseModel


class HelloWordlResponse(BaseModel):
    """
    Hello World Response Schema
    """

    message: str
