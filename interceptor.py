from abc import ABC, abstractmethod
from context import Context

class Interceptor(ABC):
    @abstractmethod
    def process(self, context: Context):
        pass