from interceptor import Interceptor
from context import Context

class FahrenheitToCelsiusInterceptor(Interceptor):
    def update(self, context: Context):
        print('inside the converter interceptor')
        temperature = context.get_temperature()
        temperature = (temperature - 32) * 5 / 9
