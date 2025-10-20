import requests
import random

#api setup
#---------------------------------------------------------------
def get_data_as_json(endpoint, headers):
    response = requests.get(endpoint, headers = headers)#raise error if api failed
    if response:
        print("API accessed successfully.")
    else:
        raise Exception(f"Non-success status code: {response.status_code}")
    return response.json()

user_agent = "jaysonc678@gmail.com"

#needed to access api
BASE_URL = "https://api.weather.gov"
headers = {'User-Agent' : f'{user_agent}'}

#get coordinates to gridpoints
#--------------------------------------------------------------------------------
coordinates = [32.9004,-105.9629]
coordinate_endpoint = f"{BASE_URL}/points/{coordinates[0]},{coordinates[1]}"

coordinate_data = get_data_as_json(coordinate_endpoint, headers)["properties"]
station_and_coords = [coordinate_data["gridId"], coordinate_data["gridX"], coordinate_data["gridY"]]

#get forecast from gridpoints
#-------------------------------------------------------------------------------------------
forecast_endpoint = f"{BASE_URL}/gridpoints/{station_and_coords[0]}/{station_and_coords[1]},{station_and_coords[2]}/forecast"
#get info from api then get specifically the first period
forecast_data = get_data_as_json(forecast_endpoint, headers)["properties"]["periods"][0]

#save the forecast in lowercase
weather = forecast_data["shortForecast"].lower()

#just for testing can be deleted
#----------------------------------------
print(f"It is {weather} outside")


try:
    #open activities file based on forecast, choose random activity from there and print it
    with open(f"WeatherBot/WeatherActivities/{weather.lower()}.txt", 'r') as f:
        activities = f.read().split('\n')
    #if there isnt a file for the forecast use default weather file
except FileNotFoundError:
    print("No specific activity found, defaulting to all weather activites")
    with open("WeatherBot/WeatherActivites/allweather.txt", 'r') as f:
        activities = f.read().split('\n')

print(f"An activity you can do in this weather is {random.choice(activities)}.")
