
from weatherData import WeatherData
from observer import Observer
from context import Context

class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
    
    def update(self, context: Context):
        self.temperature = context.temperature
        self.humidity = context.humidity
        self.display()
    
    def display(self):
        print(f"Current conditions: {self.temperature} F and {self.humidity}% humidity")