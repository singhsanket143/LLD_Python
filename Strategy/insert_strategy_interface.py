from abc import ABC, abstractmethod
from typing import List

class InsertStrategy(ABC):
    @abstractmethod
    def insert(self, numbers: List[int], num: int) -> List[int]:
        pass

