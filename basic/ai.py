from schemas import requestModel, responseModel
from openai import OpenAI





class OpenAIService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("API key must be provided either as an argument")
        self.client = OpenAI(api_key=self.api_key)



    def generate_response(self, request: requestModel) -> responseModel:

        system_prompt = "Answer the question as truthfully as possible."

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are a helpful assistant." + system_prompt},
                {"role": "user", "content": request.question}
            ]
        )
        response = response.choices[0].message.content

        return responseModel(response=response, type="text")