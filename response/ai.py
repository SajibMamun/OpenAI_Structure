from schema import ResponseModel, RequestModel, ResponseWeather
from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def get_response(self, request: RequestModel) -> ResponseModel:
        prompt = "Your are a helpful assistant. "
        response=self.client.responses.create(
            model="gpt-4o",
            input=[{"role": "user", "content": request.question},
                   {"role":"assistant","content":prompt}],
            
        )
        return (ResponseModel(response=response.output_text,type="text"))
    



    def get_specific_response(self, request: RequestModel) -> ResponseWeather:
        prompt="Your are helpful weather assistant. provide the temperature and humidity only in summary"
        response=self.client.responses.parse(
            model="gpt-4o",
            input=[{"role": "user", "content": request.question},
                   {"role":"assistant","content":prompt}],

           text_format=ResponseWeather
            
        )

        return response.output_parsed
        
        