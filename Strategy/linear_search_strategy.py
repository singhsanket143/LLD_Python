from typing import List
from search_strategy_interface import SearchStrategy

class LinearSearchStrategy(SearchStrategy):
    def search(self, numbers: List[int], num: int) -> bool:
        for n in numbers:
            if n == num:
                return True
        return False

