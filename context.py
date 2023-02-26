class Context:
    def __init__(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def get_temperature(self):
        return self.temperature

    def get_pressure(self):
        return self.pressure

    def get_humidity(self):
        return self.humidity
