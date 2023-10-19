from abc import ABC, abstractmethod
from typing import List

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, numbers: List[int], num: int) -> bool:
        pass

