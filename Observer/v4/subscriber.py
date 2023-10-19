from __future__ import annotations
from abc import ABC, abstractmethod

class Subscriber(ABC):

    @abstractmethod
    def update(self, runs: int, wickets: int, overs: float) -> None:
        pass

    @abstractmethod
    def subscribe_to(self, publisher: 'Publisher') -> None:
        pass

    @abstractmethod
    def unsubscribe_from(self, publisher: 'Publisher') -> None:
        pass
