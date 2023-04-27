from typing import Any
from pydantic import BaseModel


class ResultInfo(BaseModel):
    actual: Any
    expected: Any
    tolerance: Any = None
    status: str


if __name__ == "__main__":
    result = ResultInfo(actual=1, expected=1, tolerance=0.1, status="pass")
    print(result.json())
    result = ResultInfo(actual=[1, 2, 3], expected=[1, 2, 3], tolerance=0.1, status="pass")
    print(result.json())
    result = ResultInfo(actual={"a": 1, "b": 2}, expected={"a": 1, "b": 2}, tolerance=0.1, status="pass")
    print(result.json())
    result = ResultInfo(actual="a", expected="a", status="pass")
    print(result.json())
    result_dict = {
        "actual": 1,
        "expected": 1,
        "tolerance": 0.1,
        "status": "pass"
    }
    result = ResultInfo(**result_dict)
    print(result.json())
