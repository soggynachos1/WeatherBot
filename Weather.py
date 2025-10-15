import requests
import random

#needed to access api
headers = {'User-Agent' : 'jaysonc678@gmail.com'}
#link to data
endpoint = 'https://api.weather.gov/gridpoints/EPZ/124,104/forecast'

#get info from api then get specifically the first period
response = requests.get(endpoint, headers = headers)
data = response.json()["properties"]["periods"][0]

#save the forecast in lowercase
weather = data["shortForecast"].lower()

#raise error if api failed
if response:
    print("API accessed successfully.")
else:
    raise Exception(f"Non-success status code: {response.status_code}")

print(f"It is {weather} outside")

#open activities file based on forecast, choose random activity from there and print it
with open("WeatherActivities/" + weather.lower() + ".txt", 'r') as f:
    activities = f.read().split('\n')

    print(f"An activity you can do in this weather is {random.choice(activities)}.")
