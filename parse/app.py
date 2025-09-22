from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import OpenAIService
from openai import OpenAI
from schemas import requestModel, responseModel
from dotenv import load_dotenv
import os

load_dotenv()



app = FastAPI()


client = OpenAIService(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/generate", response_model=responseModel)
async def generate(request: requestModel) -> responseModel:
    responseModel = client.generate_response(request)
    return responseModel



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
