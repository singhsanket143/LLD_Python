from typing import List
from search_strategy_interface import SearchStrategy

class BinarySearchStrategy(SearchStrategy):
    def search(self, numbers: List[int], num: int) -> bool:
        low, high = 0, len(numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == num:
                return True
            elif numbers[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return False

