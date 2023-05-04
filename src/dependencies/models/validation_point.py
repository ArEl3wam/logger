from typing import Any
from pydantic import BaseModel


class ResultInfo(BaseModel):
    actual: Any
    expected: Any
    tolerance: Any = None
    status: str


class Result(BaseModel):
    name: str
    result_info: ResultInfo


class ValidationPointModel(BaseModel):
    levels: list[dict]
    metaData: dict
    results: list[Result]
