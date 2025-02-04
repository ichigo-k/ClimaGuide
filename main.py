
from getCordinates import get_latlng
from geminiClient import ai_suggestions
from getWeather import get_weather
from datetime import datetime

location =input("Enter location: ")

latlng = get_latlng(location)
climateConditions = get_weather(latlng['lat'], latlng['lng'])
ai_response = ai_suggestions(location, climateConditions)


formatted_date = datetime.strptime(climateConditions['date'], "%Y-%m-%d %H:%M:%S").strftime("%d %b. %Y")

print("\n" + "=" * 50)
print(f"🌤️  Weather Report for {location.upper()} on {formatted_date}")
print("=" * 50)

print(f"\n🌡️ Temperature: {climateConditions['temperature']}K ({round(climateConditions['temperature'] - 273.15, 1)}°C)")
print(f"💧 Humidity: {climateConditions['humidity']}%")
print(f"🌬️  Wind Speed: {climateConditions['wind_speed']} m/s")
print(f"📝 Conditions: {climateConditions['description'].capitalize()}")

print("\n" + "-" * 50)
print(f"\n🔮 Gemini Analysis:\n{ai_response}")
print("\n" + "=" * 50)
