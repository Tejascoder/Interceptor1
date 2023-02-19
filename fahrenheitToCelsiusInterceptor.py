from interceptor import Interceptor
from context import Context

class FahrenheitToCelsiusInterceptor(Interceptor):
    def process(self, context: Context):
        context.temperature = (context.temperature - 32) * 5 / 9