from abc import ABC, abstractmethod

class Subscriber(ABC):

    @abstractmethod
    def update(self, runs: int, wickets: int, overs: float) -> None:
        """Update the subscriber with new scores."""
        pass
