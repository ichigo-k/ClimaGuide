import os
from dotenv import load_dotenv
import requests as req
import datetime


load_dotenv(".env.local")

OPEN_WEATHER_API_KEY= os.getenv("OPEN_WEATHER_API_KEY")


def get_weather(lat, lng):
    try:
        response = req.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lng}&appid={OPEN_WEATHER_API_KEY}").json()
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        for forecast in response["list"]:
            if today in forecast["dt_txt"]:  # Find the first forecast for today
                temp = forecast["main"]["temp"]
                description = forecast["weather"][0]["description"]
                humidity = forecast["main"]["humidity"]
                wind_speed = forecast["wind"]["speed"]

                return {
                    "date": forecast["dt_txt"],
                    "temperature": temp,
                    "description": description,
                    "humidity": humidity,
                    "wind_speed": wind_speed
                }

        return None
    except:
        print("Something went wrong")







