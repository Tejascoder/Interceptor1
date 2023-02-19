from typing import List
from observer import Observer
from context import Context

class WeatherData:
    def __init__(self):
        self.observers: List[Observer] = []
        self.temperature = None
        self.humidity = None
        self.pressure = None
    
    def register_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def notify_observers(self, context: Context):
        for observer in self.observers:
            observer.update(context)
    
    def measurements_changed(self):
        context = Context(self.temperature, self.humidity, self.pressure)
        self.notify_observers(context)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()