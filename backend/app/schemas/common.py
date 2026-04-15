from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ResponseBase(BaseModel):
    success: bool = True
    message: str = ""


class PaginationParams(BaseModel):
    page: int = 1
    page_size: int = 20
