from abc import ABC,abstractmethod
class vehicle(ABC):
    def __init__(self,n):
        self.tyres=n
    @abstractmethod
    def work(self):
        pass