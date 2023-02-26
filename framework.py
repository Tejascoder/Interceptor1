from dispatcher import Dispatcher
from context import Context
class Framework:
    def __init__(self):
        self.ctx_object= None
        self.dispatcher= None

    def create_dispatcher(self):
        self.dispatcher = Dispatcher()
        return self.dispatcher

    def event(self, temperature: float, humidity: float, pressure: float):
        self.ctx_object= Context(temperature, humidity, pressure)
        self.dispatcher.dispatch(self.ctx_object)


