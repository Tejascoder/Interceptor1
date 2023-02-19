from interceptor import Interceptor
from context import Context

class HighTemperatureInterceptor(Interceptor):
    def process(self, context: Context):
        if context.temperature > 30:
            print("High temperature alert!")