
import requests

#get input from user

city_name = input("Enter City: ")

geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&countrycode=IN"
response = requests.get(geocoding_url)

#calling API

data = response.json()

#make function about weather dashboard

def get_weather(data):

    #if for error handling

    if "results" in data:
        results = data["results"][0]
        city = results["name"]
        country = results["country"]
        latitude = results["latitude"]
        longitude = results["longitude"]
        #calling second API for weather reports
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
        response_2 = requests.get(weather_url)
        weather_data = response_2.json()

        temperature = weather_data["current"]["temperature_2m"]
        wind_speed = weather_data["current"]["wind_speed_10m"]
        print("=" *26)
        print("    Weather Dashboard")
        print("=" *26)
        print("City:",city)
        print("Country:",country)
        print("temperature:", temperature)
        print("wind_speed:", wind_speed)

    #if user input wrong city it print city not found!

    else:
        print("City not found!")

get_weather(data)