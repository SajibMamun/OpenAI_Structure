from dotenv import load_dotenv
from ai import OpenAIClient
from schema import RequestModel, ResponseModel, ResponseWeather
from fastapi import FastAPI
import os

load_dotenv()

client = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

def is_weather_query(question: str) -> bool:
    """Check if the question is weather-related"""
    weather_keywords = [
        'weather', 'temperature', 'humidity', 'rain', 'sunny', 'cloudy', 
        'storm', 'wind', 'forecast', 'climate', 'hot', 'cold', 'warm', 
        'snow', 'precipitation', 'degrees', 'celsius', 'fahrenheit'
    ]
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in weather_keywords)

@app.post("/ask")
def ask_question(request: RequestModel):
    if is_weather_query(request.question):
        # Route to weather-specific response
        response = client.get_specific_response(request)
        return response
    else:
        # Route to general response
        response = client.get_response(request)
        return response

