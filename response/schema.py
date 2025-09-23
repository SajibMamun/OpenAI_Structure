from pydantic import BaseModel, Field

class ResponseModel(BaseModel):
    response: str
    type:str

class RequestModel(BaseModel):
    question:str

class ResponseWeather(BaseModel):
    temperature:str
    humidity:str
