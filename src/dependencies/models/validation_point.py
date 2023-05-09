from typing import Any
from pydantic import BaseModel


class Result(BaseModel):
    actual: Any
    expected: Any
    tolerance: int | None = None
    status: str


class ValidationPointModel(BaseModel):
    levels: list[dict]
    meta_data: dict
