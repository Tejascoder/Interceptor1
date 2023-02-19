class WeatherStation:
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
        self.observers = []

    def set_measurement(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)


class Display:
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(f"Temperature: {self.temperature} degrees Celsius")
        print(f"Humidity: {self.humidity}%")
        print(f"Pressure: {self.pressure} hPa")


class WeatherDataContext:
    def __init__(self, weather_station):
        self.weather_station = weather_station


class WeatherDataUpdateDispatcher:
    def register_weather_data_update_interceptor(self, interceptor):
        pass

    def remove_weather_data_update_interceptor(self, interceptor):
        pass


class WeatherDataUpdateInterceptor:
    def on_weather_data_update(self, weather_data):
        pass


class WeatherDataUpdateDispatcherImpl(WeatherDataUpdateDispatcher):
    def __init__(self):
        self.interceptors = []

    def register_weather_data_update_interceptor(self, interceptor):
        self.interceptors.append(interceptor)

    def remove_weather_data_update_interceptor(self, interceptor):
        self.interceptors.remove(interceptor)

    def dispatch_weather_data_update(self, weather_data):
        context = WeatherDataContext(self)
        for interceptor in self.interceptors:
            interceptor.on_weather_data_update(weather_data, context)


class LoggingWeatherDataUpdateInterceptor(WeatherDataUpdateInterceptor):
    def on_weather_data_update(self, weather_data, context):
        print("New weather data received:", weather_data)


weather_station = WeatherStation()
display = Display()
dispatcher = WeatherDataUpdateDispatcherImpl()

# Register the interceptor with the dispatcher
interceptor = LoggingWeatherDataUpdateInterceptor()
dispatcher.register_weather_data_update_interceptor(interceptor)

# Register the display with the weather station
weather_station.register_observer(display)

# Update the weather station readings
weather_station.set_measurement(25.0, 70.0, 1013.0)
weather_station.set_measurement(26.0, 71.0, 1012.0)
weather_station.set_measurement(27.0, 72.0, 1011.0)


# The interceptor should have printed the new weather data
