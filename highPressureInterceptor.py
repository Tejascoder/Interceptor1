from interceptor import Interceptor
from context import Context

class HighPressureInterceptor(Interceptor):
    def process(self, context: Context):
        if context.pressure > 80:
            print("High pressure alert!")