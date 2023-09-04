import requests


base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
api_key = "b6907d289e10d714a6e88b30761fae22"



def get_weather_data(city, country):
    params = {"q": f"{city},{country}", "appid": api_key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data. Please check your input and try again.")
        return None



def get_temperature(data, date_time):
    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['main']['temp']
    return None



def get_wind_speed(data, date_time):
    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['wind']['speed']
    return None


# Function to get pressure
def get_pressure(data, date_time):
    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['main']['pressure']
    return None


if __name__ == "__main__":
    city = "London"
    country = "us"
    weather_data = get_weather_data(city, country)

    if weather_data:
        while True:
            print("\nMenu:")
            print("1. Get Temperature")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
                temperature = get_temperature(weather_data, date_time)
                if temperature is not None:
                    print(f"Temperature at {date_time}: {temperature}°C")
                else:
                    print("Data not found for the given date and time.")
            elif choice == "2":
                date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
                wind_speed = get_wind_speed(weather_data, date_time)
                if wind_speed is not None:
                    print(f"Wind Speed at {date_time}: {wind_speed} m/s")
                else:
                    print("Data not found for the given date and time.")
            elif choice == "3":
                date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
                pressure = get_pressure(weather_data, date_time)
                if pressure is not None:
                    print(f"Pressure at {date_time}: {pressure} hPa")
                else:
                    print("Data not found for the given date and time.")
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
