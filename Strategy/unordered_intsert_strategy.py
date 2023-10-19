from typing import List
from insert_strategy_interface import InsertStrategy

class UnorderedInsertStrategy(InsertStrategy):
    def insert(self, numbers: List[int], num: int) -> List[int]:
        numbers.append(num)
        return numbers

