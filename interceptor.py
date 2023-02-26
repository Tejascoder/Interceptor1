from abc import ABC, abstractmethod
from context import Context

class Interceptor(ABC):
    @abstractmethod
    def update(self, context: Context):
        pass