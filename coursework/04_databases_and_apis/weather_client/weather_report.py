"""What is this written for?

Consuming a third-party REST API from Python: it asks for a city name, calls the
OpenWeatherMap current-weather endpoint with `requests`, and prints the fields of
interest out of the JSON response.

The API key never lives in this file. Put it in the .env one folder up (copy
.env.example), or set OPENWEATHER_API_KEY in your environment:

    PowerShell:  $env:OPENWEATHER_API_KEY = "your-key"
    Git Bash:    export OPENWEATHER_API_KEY="your-key"
"""

import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

# Reads coursework/04_databases_and_apis/.env if it exists. Real environment
# variables take precedence, so nothing is overridden in CI or production.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

API_URL = "https://api.openweathermap.org/data/2.5/weather"


def main():
    api_key = os.environ.get("OPENWEATHER_API_KEY", "").strip()
    # The placeholder from .env.example is a non-empty string, so check for it
    # explicitly - otherwise it reaches the API and comes back as an opaque 401.
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
