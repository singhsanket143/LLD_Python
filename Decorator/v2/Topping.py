from abc import ABC, abstractmethod
from Pizza import Pizza

class Topping(Pizza, ABC):
    def __init__(self, pizza: Pizza, description: str, cost: float):
        super().__init__(description, cost)
        self._pizza = pizza

    def get_description(self) -> str:
        return super().get_description() + " " + self._pizza.get_description()

    def get_cost(self) -> float:
        return super().get_cost() + self._pizza.get_cost()
