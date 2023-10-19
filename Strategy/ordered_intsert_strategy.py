from typing import List
from insert_strategy_interface import InsertStrategy

class OrderedInsertStrategy(InsertStrategy):
    def insert(self, numbers: List[int], num: int) -> List[int]:
        numbers.append(num)
        numbers.sort()
        return numbers

