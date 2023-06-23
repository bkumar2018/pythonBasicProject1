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
api_key = "xcxcxcxcxxc"
location = "Pune"
weather_data = get_weather_data(api_key, location)

if weather_data is not None:
    print("Current weather in", location, ":", weather_data["current"]["condition"]["text"])
else:
    print("Failed to retrieve weather data.")


#write function to call time zone api and get the time zone
def get_time_zone(api_key, location):
    base_url = "https://api.weatherapi.com/v1/timezone.json"
    params = {
        "key": api_key,
        "q": location
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

#call get_time_zone function
time_zone_data = get_time_zone(api_key, location)
if time_zone_data is not None:
    print("Time zone in", location, ":", time_zone_data["location"]["tz_id"])
else:
    print("Failed to retrieve time zone data.")


