import requests

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()
def extract_weather_info(data):
    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    }
    return weather_info

def generate_report(weather_info):
    report = (
        f"Weather Report for {weather_info['city']}:\n"
        f"Temperature: {weather_info['temperature']}°C\n"
        f"Condition: {weather_info['description'].capitalize()}\n"
        f"Humidity: {weather_info['humidity']}%\n"
        f"Wind Speed: {weather_info['wind_speed']} m/s\n"
    )
    return report


def main():
    api_key = "YOUR_API_KEY"
    city = "London"
    
    data = get_weather_data(api_key, city)
    if data['cod'] != 200:
        print("Failed to get weather data:", data['message'])
        return
    
    weather_info = extract_weather_info(data)
    report = generate_report(weather_info)
    print(report)


if __name__ == "__main__":
    main()

