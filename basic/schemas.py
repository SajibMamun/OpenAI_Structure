from pydantic import BaseModel

class responseModel(BaseModel):
    response: str
    type: str


class requestModel(BaseModel):
    question: str