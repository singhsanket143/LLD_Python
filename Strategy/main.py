from number_store import NumberStore
from ordered_insert_strategy import OrderedInsertStrategy
from unordered_insert_strategy import UnorderedInsertStrategy
from linear_search_strategy import LinearSearchStrategy
from binary_search_strategy import BinarySearchStrategy

store = NumberStore(OrderedInsertStrategy(), BinarySearchStrategy())
store.insert(5)
store.insert(3)
store.insert(10)

print(store.search(5))  # True
print(store.search(7))  # False

store.set_insert_strategy(UnorderedInsertStrategy())
store.set_search_strategy(LinearSearchStrategy())
store.insert(7)

print(store.search(7))  # True

