import requests
import random


user_agent = "jaysonc678@gmail.com"

BASE_URL = "https://api.weather.gov"

station_and_coords = ["EPZ",124,104]


#needed to access api
headers = {'User-Agent' : f'{user_agent}'}
#link to data
endpoint = f"{BASE_URL}/gridpoints/{station_and_coords[0]}/{station_and_coords[1]},{station_and_coords[2]}/forecast"

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

try:
    #open activities file based on forecast, choose random activity from there and print it
    with open("WeatherActivities/" + weather.lower() + ".txt", 'r') as f:
        activities = f.read().split('\n')
    #if there isnt a file for the forecast use default weather file
except FileNotFoundError:
    print("No specific activity found, defaulting to all weather activites")
    with open("WeatherBot/WeatherActivites/allweather.txt", 'r') as f:
        activities = f.read().split('\n')

print(f"An activity you can do in this weather is {random.choice(activities)}.")
