from interceptor import Interceptor
from context import Context

class HighPressureInterceptor(Interceptor):
    def update(self, context: Context):
        pressure= context.get_pressure()
        print('inside pressure interceptor')
        if pressure > 80:
            print("High pressure alert!")