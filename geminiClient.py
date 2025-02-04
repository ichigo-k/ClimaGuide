import os
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv(".env.local")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def ai_suggestions(location, weather_data):
    prompt = (f"Given the following weather data for {location}:Temperature: {weather_data['temperature']}K "
              f"Humidity: {weather_data['humidity']}%Wind Speed: {weather_data['wind_speed']} m/sConditions: {weather_data['description']}"
              f"I am a tourist looking for advice on how to spend my day. Based on the weather and location, "
              f"suggest activities I should try, including whether I should stay indoors or explore outdoor attractions. "
              f"Keep the response concise but informative, considering the heat and best times for certain activities.")

    response = model.generate_content(prompt)
    return response.text
