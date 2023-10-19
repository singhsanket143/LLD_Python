from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self, description="", cost=0.0):
        self._description = description
        self._cost = cost

    
    def get_description(self) -> str:
        return self._description

    
    def get_cost(self) -> float:
        return self._cost
