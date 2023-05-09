from typing import Any
from pydantic import BaseModel


class Result(BaseModel):
    actual: Any
    expected: Any
    tolerance: int | None = None
    status: str


class ValidationPointModel(BaseModel):
    levels: list[dict]
    metaData: dict
    results: list[dict[str, Result]]
