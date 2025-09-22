from pydantic import BaseModel

class responseModel(BaseModel):
    event_name: str
    date: str
    participants: list[str]

class requestModel(BaseModel):
    question: str