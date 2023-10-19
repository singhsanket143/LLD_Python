from abc import ABC, abstractmethod
from subscriber import Subscriber

class Publisher(ABC):

    @abstractmethod
    def register(self, subscriber: Subscriber) -> None:
        """Register a subscriber."""
        pass

    @abstractmethod
    def deregister(self, subscriber: Subscriber) -> None:
        """Deregister a subscriber."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify all subscribers."""
        pass
