import requests

def get_weather():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeather API key
    city = input("Enter municipality name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        print(f"Weather in {city}: {description}")
        print(f"Temperature: {temperature} °C")
    else:
        print("City not found or API error.")


# Run the program
get_weather()