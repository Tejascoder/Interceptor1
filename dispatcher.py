from typing import List
from interceptor import Interceptor
from context import Context
from application import WeatherData

class Dispatcher:
    def __init__(self):
        self.interceptors =[]

    def register_interceptor(self, interceptor: Interceptor):
        self.interceptors.append(interceptor)

    def remove_interceptor(self,interceptor: Interceptor):
        self.interceptors.remove(interceptor)
    
    def dispatch(self, context: Context):
        for interceptor in self.interceptors:
            interceptor.update(context)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.weather_data.temperature = temperature
        self.weather_data.humidity = humidity
        self.weather_data.pressure = pressure
        self.weather_data.context_object = Context(self.temperature, self.humidity, self.pressure)
        self.dispatch(self.weather_data.context_object)