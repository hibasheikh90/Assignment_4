import requests
from pprint import pprint

API_KEY = '5539c6a9ed86cb751d27002cb361c3a2'

city = input("Enter city name: ")
base_url = f"http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city
weather_data = requests.get(base_url).json()

pprint(weather_data)


