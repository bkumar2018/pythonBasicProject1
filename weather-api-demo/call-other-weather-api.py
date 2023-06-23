#write code to call weather api to forecast weather for a given location
import requests
import json

def get_weather_forecast(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid={}".format(lat, lon, "xxxxxx")
    response = requests.get(url)
    data = json.loads(response.text)
    return data

#call get_weather_forecast function with lat and lon
data = get_weather_forecast(37.8267, -122.4233)
print(data)

