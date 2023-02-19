import random
from weatherData import WeatherData, Context
from currentConditionsDisplay import CurrentConditionsDisplay
from dispatcher import Dispatcher
from fahrenheitToCelsiusInterceptor import FahrenheitToCelsiusInterceptor
from highPressureInterceptor import HighPressureInterceptor
from highTemperatureInterceptor import HighTemperatureInterceptor

class Application:
    def __init__(self,temperature: int, humidity: int, pressure: int):
        
        
        self.weather_data = WeatherData()
        self.dispatcher = Dispatcher(self.weather_data)
        self.dispatcher.dispatch(Context(temperature, humidity, pressure))
        self.current_display = CurrentConditionsDisplay(self.weather_data)
        #self.weather_data.set_measurements(100, 100, 100)
        
        
        self.fahrenheit_to_celsius = FahrenheitToCelsiusInterceptor()
        self.high_temperature_alert = HighTemperatureInterceptor()
        self.high_pressure_alert = HighPressureInterceptor()
        self.dispatcher.register_interceptor(self.fahrenheit_to_celsius)
        self.dispatcher.register_interceptor(self.high_temperature_alert)
        self.dispatcher.register_interceptor(self.high_pressure_alert)
        

    

    # def run(self):
    #     temperature = 400
    #     humidity = 300
    #     #temperature = random.uniform(90, 100)
    #     pressure = random.uniform(90, 100)
    #     self.weather_data.set_measurements(temperature,humidity, pressure)
        
Application(100,50,30)

# execute.run()