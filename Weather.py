import requests
import random

headers = {'User-Agent' : 'jaysonc678@gmail.com'}
endpoint = 'https://api.weather.gov/gridpoints/EPZ/124,104/forecast'

response = requests.get(endpoint, headers = headers)
data = response.json()["properties"]["periods"][0]

weather = data["shortForecast"].lower()

if response:
    print("API accessed successfully.")
else:
    raise Exception(f"Non-success status code: {response.status_code}")

print(f"It is {weather} outside")

with open(weather.lower() + ".txt", 'r') as f:
    activities = f.read().split('\n')
    print(f"An activity you can do in this weather is {random.choice(activities)}.")