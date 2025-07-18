import requests

api_key = "0f3fc60c7b4585c095741a6f450c4cae".strip()
city = input("Enter city name: ")
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:

    weather_data = response.json()

    print(f"City: {weather_data['name']}")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    print(f"Failed to get weather data. Status code: {response.status_code}")