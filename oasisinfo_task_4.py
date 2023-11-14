import requests
import json
from tkinter import Tk, Label, Button

# Replace 'YOUR_API_KEY' with the API key you obtained from OpenWeatherMap
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.location_label = Label(root, text="Enter City:")
        self.location_label.pack()

        self.location_entry = Entry(root)
        self.location_entry.pack()

        self.result_label = Label(root, text="")
        self.result_label.pack()

        self.get_weather_button = Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

    def get_weather(self):
        city = self.location_entry.get()
        if city:
            try:
                # Make a request to the OpenWeatherMap API
                response = requests.get(BASE_URL.format(city, API_KEY))
                data = json.loads(response.text)

                # Extract relevant information from the API response
                temperature = data['main']['temp']
                description = data['weather'][0]['description']

                # Display the weather information
                result_text = f'Temperature: {temperature}°C\nDescription: {description}'
                self.result_label.config(text=result_text)
            except Exception as e:
                self.result_label.config(text="Error fetching weather data")
        else:
            self.result_label.config(text="Please enter a city")

if __name__ == "__main__":
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()
