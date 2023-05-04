from pydantic import BaseModel


class ValidationTagModel(BaseModel):
    name: str
    metaData: dict
