from typing import List
from insert_strategy_interface import InsertStrategy
from search_strategy_interface import SearchStrategy

class NumberStore:
    def __init__(self, insert_strategy: InsertStrategy, search_strategy: SearchStrategy):
        self._numbers = []
        self._insert_strategy = insert_strategy
        self._search_strategy = search_strategy

    def insert(self, num: int):
        self._numbers = self._insert_strategy.insert(self._numbers, num)

    def search(self, num: int) -> bool:
        return self._search_strategy.search(self._numbers, num)

    def set_insert_strategy(self, strategy: InsertStrategy):
        self._insert_strategy = strategy

    def set_search_strategy(self, strategy: SearchStrategy):
        self._search_strategy = strategy

