from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass
