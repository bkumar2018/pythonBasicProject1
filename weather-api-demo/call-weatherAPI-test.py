#write code to call weather api and write test cases to test it
import requests

def get_weather_data(api_key, location):
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
api_key = "xxxxxxxx-xxxxxx-xxxxxx-xxxxxx"
location = "Pune"
weather_data = get_weather_data(api_key, location)

if weather_data is not None:
    print("Current weather in", location, ":", weather_data["current"]["condition"]["text"])
else:
    print("Failed to retrieve weather data.")



