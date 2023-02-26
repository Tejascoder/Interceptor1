from typing import List
from observer import Observer
from context import Context
from fahrenheitToCelsiusInterceptor import FahrenheitToCelsiusInterceptor
from highTemperatureInterceptor import HighTemperatureInterceptor
from highPressureInterceptor import HighPressureInterceptor

class WeatherData:

    def __init__(self):
        self.observers: List[Observer] = []
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.context_object= None

    def interceptor_factory(self,type):
        interceptor_types= {'temperature': HighTemperatureInterceptor, 'pressure':HighPressureInterceptor,'convert':FahrenheitToCelsiusInterceptor}
        return interceptor_types[type]()

    def create_interceptor(self,type= 'temperature'):
        return self.interceptor_factory(type)

    def register_interceptor(self,interceptor, dispatcher):
        dispatcher.register_interceptor(interceptor)

    def remove_interceptor(self,interceptor, dispatcher):
        dispatcher.remove_interceptor(interceptor)