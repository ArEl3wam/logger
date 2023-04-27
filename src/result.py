from pydantic import BaseModel

from resultinfo import ResultInfo


class Result(BaseModel):
    name: str
    result_info: ResultInfo


if __name__ == "__main__":
    result_info = ResultInfo(actual=1, expected=1, tolerance=0.1, status="pass")
    result = Result(name="result1", result_info=result_info)
    print(result.json())

    result_info = ResultInfo(actual="RC", expected="RC", status="pass")
    result = Result(name="fec_errors", result_info=result_info)
    print(result.dict())
