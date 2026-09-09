"""Print the current weather for a city, from the OpenWeatherMap API."""

import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

# Loads the .env one folder up.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

API_URL = "https://api.openweathermap.org/data/2.5/weather"


def main():
    api_key = os.environ.get("OPENWEATHER_API_KEY", "").strip()
    # The .env.example placeholder is non-empty, so check for it too.
    if not api_key or api_key == "your-openweathermap-key":
        sys.exit(
            "OPENWEATHER_API_KEY is not set. Get a free key at "
            "https://openweathermap.org/api and put it in the .env file one "
            "folder up, or set it as an environment variable."
        )

    city = input("Enter city name: ")
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(API_URL, params=params, timeout=10)

    if response.status_code == 200:
        weather_data = response.json()

        print(f"City: {weather_data['name']}")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    elif response.status_code == 401:
        print("Rejected by OpenWeatherMap (401): the API key is invalid or revoked.")
    elif response.status_code == 404:
        print(f"No such city: {city}")
    else:
        print(f"Failed to get weather data. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
