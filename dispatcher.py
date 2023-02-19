from typing import List
from interceptor import Interceptor
from weatherData import WeatherData
from context import Context

class Dispatcher:
    def __init__(self, weather_data: WeatherData):
        self.interceptors =[]
        self.weather_data = weather_data
    
    def register_interceptor(self, interceptor: Interceptor):
        self.interceptors.append(interceptor)
    
    def dispatch(self, context: Context):
        for interceptor in self.interceptors:
            interceptor.process(context)
