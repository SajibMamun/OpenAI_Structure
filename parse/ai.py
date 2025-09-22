from openai import OpenAI
import os
from schemas import requestModel, responseModel



class OpenAIService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("API key must be provided either as an argument")
        self.client = OpenAI(api_key=self.api_key)




    def generate_response(self, request: requestModel) -> responseModel:
        
        response = self.client.chat.completions.parse(
            model="gpt-4o",
            messages=[{"role": "user", "content": request.question},
                      {"role": "system", "content": "Extract the event name, date, and participants from the question."}
                      ],

            response_format=responseModel
            )
        
        response=response.choices[0].message.parsed


        return responseModel(event_name=response.event_name, date=response.date, participants=response.participants)

