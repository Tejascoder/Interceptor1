from interceptor import Interceptor
from context import Context

class HighTemperatureInterceptor(Interceptor):
    def update(self, context: Context):
        temperature= context.get_temperature()
        print('inside temperature interceptor')
        if temperature > 30:
            print("High temperature alert!")