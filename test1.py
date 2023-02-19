class WeatherMeasurement:
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

class WeatherMeasurementContextObject:
    def __init__(self, measurements):
        self.measurements = measurements

class WeatherMeasurementInterceptor:
    def on_pre_measurement_received(self, context):
        pass
    
    def on_post_measurement_received(self, context):
        pass

class WeatherData:
    def __init__(self):
        self.measurements = []
        self.interceptors = []
        
    def add_measurement(self, measurement):
        self.measurements.append(measurement)
        self.notify_interceptors()
        
    def register_interceptor(self, interceptor):
        self.interceptors.append(interceptor)
        
    def remove_interceptor(self, interceptor):
        self.interceptors.remove(interceptor)
        
    def notify_interceptors(self):
        context = WeatherMeasurementContextObject(self.measurements)
        for interceptor in self.interceptors:
            interceptor.on_pre_measurement_received(context)
            
        for interceptor in self.interceptors:
            interceptor.on_post_measurement_received(context)

class LoggingInterceptor(WeatherMeasurementInterceptor):
    def on_pre_measurement_received(self, context):
        print("Logging interceptor: About to receive new weather measurements")
        
    def on_post_measurement_received(self, context):
        print(f"Logging interceptor: New weather measurements received: {context.measurements}")

class FilteringInterceptor(WeatherMeasurementInterceptor):
    def on_pre_measurement_received(self, context):
        print("Filtering interceptor: About to receive new weather measurements")
        
    def on_post_measurement_received(self, context):
        filtered_measurements = [m for m in context.measurements if m.temperature > 20]
        print(f"Filtering interceptor: New weather measurements after filtering: {filtered_measurements}")
        context.measurements = filtered_measurements

if __name__ == '__main__':
    weather_data = WeatherData()
    
    logging_interceptor = LoggingInterceptor()
    filtering_interceptor = FilteringInterceptor()
    
    weather_data.register_interceptor(logging_interceptor)
    weather_data.register_interceptor(filtering_interceptor)
    
    weather_data.add_measurement(WeatherMeasurement(25, 50, 1000))
    weather_data.add_measurement(WeatherMeasurement(15, 60, 990))