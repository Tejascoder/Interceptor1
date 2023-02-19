from typing import List

class Observer:
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

class DisplayElement:
    def display(self):
        pass

class Context:
    def __init__(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

class CurrentConditionsDisplay(Observer, DisplayElement):
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
        print(f"Current conditions: {self.temperature:.2f}°F and {self.humidity}% humidity")

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

class Interception:
    def process(self, context: Context):
        pass

class Dispatcher:
    def __init__(self, weather_data: WeatherData):
        self.interceptors: List[Interception] = []
        self.weather_data = weather_data
    
    def register_interceptor(self, interceptor: Interception):
        self.interceptors.append(interceptor)
    
    def dispatch(self, context: Context):
        for interceptor in self.interceptors:
            interceptor.process(context)

class FahrenheitToCelsiusInterceptor(Interception):
    def process(self, context: Context):
        context.temperature = (context.temperature - 32) * 5 / 9

class HighTemperatureInterceptor(Interception):
    def process(self, context: Context):
        if context.temperature > 32:
            print("High temperature alert!")
    
class Application:
    def __init__(self, temperature: float, humidity: float, pressure: float):
        self.weather_data = WeatherData()
        
        self.dispatcher = Dispatcher(self.weather_data)
        
        self.fahrenheit_to_celsius = FahrenheitToCelsiusInterceptor()
        
        self.high_temperature = HighTemperatureInterceptor()
        
        self.dispatcher.register_interceptor(self.fahrenheit_to_celsius)
        
        self.dispatcher.register_interceptor(self.high_temperature)
        
        #self.weather_data.set_measurements(temperature, humidity, pressure)
        self.current_display = CurrentConditionsDisplay(self.weather_data)
        

if __name__ == "__main__":
    app = Application(100, 50, 30)
